import KaitaiStream from 'kaitai-struct/KaitaiStream';
import { readdir, readFile, writeFile } from 'fs/promises';
import { GenesysType as GenesysTypeBE } from '../ParserStuff-BE/genesys-type-BE';
import { GenesysType as GenesysTypeLE } from '../ParserStuff-LE/genesys-type';
// import { argv } from 'process';
import { readdirSync } from 'fs';
import { stringify as YamlStringify } from 'yaml';

interface TypeDictionary {
    [key: string]: {
        name: string,
        objectHash: string,
        muVersionID: string,
        extends: string,
        isEnum: boolean,
        types: {
            muID: string,
            hash: string,
            tableEntryOffset: number,
            unhashedName: string,
            alignment: number,
            offset: number,
            valueTypeBits: number[],
            arrayCountSpecified: number,
            arrayCountProperyOffset: number
        }[]
    }
};

const E3_PATH = `../E3_BUILD`;
const E3_BNDLS = [
    [E3_PATH + '/unpacked/GLOBALRESOURCES', 'GLOBALRESOURCES'],
    [E3_PATH + '/unpacked/GAMEMODES', 'GAMEMODES'],
    [E3_PATH + '/unpacked/GAMEPLAY', 'GAMEPLAY'],
    [E3_PATH + '/unpacked/WEAPONS_445406', 'WEAPONS_445406'],
    [E3_PATH + '/unpacked/WEAPONS_457359', 'WEAPONS_457359'],
];

const RETAIL_PATH = '.';
const RETAIL_BNDLS = [
    [RETAIL_PATH + '/../all_unpacked/gamemodes', 'gamemodes'],
    [RETAIL_PATH + '/../all_unpacked/globalresources', 'globalresources'],
    [RETAIL_PATH + '/../all_unpacked/HL_31208', 'HL_31208'],
    [RETAIL_PATH + '/../all_unpacked/HSM/UILISTS/20809', 'HSM_UILISTS_20809'],
    [RETAIL_PATH + '/../all_unpacked/physicsconfig', 'physicsconfig'],
    [RETAIL_PATH + '/../all_unpacked/traffic', 'traffic'],
    [RETAIL_PATH + '/../all_unpacked/vehicle_waves', 'vehicle_waves'],
    [RETAIL_PATH + '/../all_unpacked/VEH_122699_LO', 'VEH_122699_LO'],
    [RETAIL_PATH + '/../all_unpacked/TRAFFICATTRIBS', 'TRAFFICATTRIBS'],
    [RETAIL_PATH + '/../all_unpacked/TRK_UNIT1', 'TRK_UNIT1'],
    [RETAIL_PATH + '/../all_unpacked/easyguide', 'easyguide'],
    [RETAIL_PATH + '/../all_unpacked/unpacked_vehicles', 'vehicles'],
    [RETAIL_PATH + '/../all_unpacked/gameplay', 'gameplay'],
    [RETAIL_PATH + '/../all_unpacked/ui/screens2/264716', 'ui_264716'],
    [RETAIL_PATH + '/../all_unpacked/ui/screens2/371621', 'ui_371621'],
    [RETAIL_PATH + '/../all_unpacked/EN_US/FEEDBACKGROUPS/457708', 'fbg_457708'],
    [RETAIL_PATH + '/../all_unpacked/FBG_2090138', 'fbg_2090138'],
    [RETAIL_PATH + '/../all_unpacked/GLOBALCONFIG', 'GLOBALCONFIG'],
];

let ROOT_PATH = __dirname + '/';
let BNDL_LIST = [];
let GenesysType: typeof GenesysTypeBE | typeof GenesysTypeLE;
const IS_E3 = process.argv[2] === 'E3';
if (IS_E3) {
    ROOT_PATH += E3_PATH;
    BNDL_LIST = E3_BNDLS;
    GenesysType = GenesysTypeBE;
} else {
    ROOT_PATH += RETAIL_PATH;
    BNDL_LIST = RETAIL_BNDLS;
    GenesysType = GenesysTypeLE;
}

let typeDictionary: TypeDictionary = {};
let localTypeDictionary: TypeDictionary = {};
let versionLookup: Map<number, string> = new Map();
let localVersionLookup: Map<number, string> = new Map();
let errors: Set<string> = new Set();
let localErrors: Set<string> = new Set();
let typeExtensions = {};

let nameToHash: Map<string, string> = new Map();

let knownHashes: Map<string, string> = new Map();

let scaffoldedKSY: string;

// let longestName = 0;

const toLEHash = (num: number) => {
    return num.toString(16).replace(/^(.(..)*)$/, "0$1").match(/../g).reverse().join("").padEnd(8, '0').match(/(..)/g).join("_").toUpperCase();
}

const LEToString = (num: number) => {
    return num.toString(16).replace(/^(.(..)*)$/, "0$1").match(/../g).map(s => parseInt(s, 16));
}

const extractFullHash = (te: GenesysTypeLE.GenesysTypeEntry | GenesysTypeBE.GenesysTypeEntry) => {
    if (te instanceof GenesysTypeLE.GenesysTypeEntry) {
        let val = ([...te.typeHashId]).map(v => v.toString(16).padStart(2, '0').toUpperCase()).join('_').slice(0, 11)
        if (te.typeHashId[6] != 0) {
            // if (Math.random() < 1) process.exit();
            val += '_' + te.typeHashId[4];
            val += '_' + te.typeHashId[6];
        }
        else if (te.typeHashId[4] != 0) {
            val += '_' + te.typeHashId[4];
        }
        else if (val.endsWith('_00')) { val = val.slice(0, 11); }
        return val;
    } else if (te instanceof GenesysTypeBE.GenesysTypeEntry) {
        let val = ([...te.typeHashId]).map(v => v.toString(16).padStart(2, '0').toUpperCase()).join('_').slice(12, 23)
        if (te.typeHashId[1] != 0) {
            // if (Math.random() < 1) process.exit();
            val += '_' + te.typeHashId[3];
            val += '_' + te.typeHashId[1];
        }
        else if (te.typeHashId[3] != 0) {
            val += '_' + te.typeHashId[3];
        }
        else if (val.endsWith('_00')) { val = val.slice(0, 11); }
        return val;
    }
    
}

const checkHashError = (hash: string) => {
    if (IS_E3) {
        return hash.endsWith('_1') || hash.match(/_1_\d$/g);
    }
    return hash.endsWith('_1');
}
const correctStandardHashError = (hash: string) => {
    return hash.slice(0, hash.length - 2);
}
const correctE3HashError = (hash: string) => {
    return hash.replace(/_1_(\d)$/g, '_0_$1');    
}

const extractType = async (directory: string, name: string) => {
    if (Object.keys(localTypeDictionary).includes(name)) return;
    // console.log(name);

    const path = __dirname + `/${directory}/GenesysType/${name}.dat`;
    const file = await readFile(path);
    const parsed = new GenesysType(new KaitaiStream(file));
    const fileLength = parsed._io._byteLength;
    const typeData = parsed.typeData as GenesysTypeLE.GenesysNativetypeObjectData;    
    
    const hasName = typeData.muTypeInfoPtr && typeData.muTypeInfoPtr.data != undefined;
    
    let typeInfo: GenesysTypeLE.GenesysTypeInformation;
    let typeName: string;
    let typeOffset: number;
    let typeNameEndOffset: number;

    if (!hasName || parsed.meNativeType === GenesysType.ENativeType.E_NATIVETYPE_ENUMERATION) {
        typeName = name;
    } else {
        typeInfo = (typeData.muTypeInfoPtr.data.data as GenesysTypeLE.GenesysTypeInformation)
        typeName = typeInfo.mpNamePtr.data.data as string;
    }
    nameToHash.set(typeName, name);

    // console.log(Object.keys(parsed.typeData));
    // console.log(typeData.muId);
    localTypeDictionary[name] = {
        name: typeName,
        extends: "",
        objectHash: toLEHash(typeData.muId),
        muVersionID: toLEHash(typeData.muVersion),
        isEnum: parsed.meNativeType === GenesysType.ENativeType.E_NATIVETYPE_ENUMERATION,
        types: [],
    };
    localVersionLookup.set(typeData.muVersion, name);

    // console.log(Object.keys(localTypeDictionary).length)
    // console.log(name, localTypeDictionary["9F_57_FE_8C"]);
    // const prop = entries[entries.length - 1].data as GenesysTypeLE.GenesysProperty;

    let finalOffset;
    if (hasName) {
        const genTypeInfo = (typeData.muTypeInfoPtr.data.data as GenesysTypeLE.GenesysTypeInformation)
        finalOffset = genTypeInfo.mpNamePtr.offset + (genTypeInfo.mpNamePtr.data.data as string).length;
    } else {
        finalOffset = typeData.mpaPropertiesPtr.offset + typeData.mpaPropertiesPtr.entries.length * parsed.sizes.genesysProperty;
    }
    const typeTableStart = 0x10 - (finalOffset % 0x10) + finalOffset;
    
    if (!hasName) {
        // console.log("in type table start thing");
        
        if (parsed.meNativeType === GenesysType.ENativeType.E_NATIVETYPE_ENUMERATION) {
            // parses enums specifically
        } else {
            // parses types without a name
            if (typeData.muBaseTypeVersion) {           
                try {
                    const baseTypeTableEntry = new GenesysType.GenesysTypeEntry(new KaitaiStream(file.subarray(typeTableStart, typeTableStart + 0x10)));
                    let hash = extractFullHash(baseTypeTableEntry);
                    if (checkHashError(hash)) {
                        try {
                            await readFile(__dirname + `/${directory}/GenesysType/${hash}.dat`);
                        } catch {
                            let chkHash = correctStandardHashError(hash);
                            if (IS_E3) {
                                try {
                                    await readFile(__dirname + `/${directory}/GenesysType/${chkHash}.dat`);
                                } catch {
                                    chkHash = correctE3HashError(hash);
                                }
                            }
                            hash = chkHash;
                        }
                    }
                    localTypeDictionary[name].extends = hash;
                } catch {
                }
                
                if (!localTypeDictionary[name].extends) {
                    const extendsFrom = localVersionLookup.get(typeData.muBaseTypeVersion);
                    if (extendsFrom) {   
                        localTypeDictionary[name].extends = extendsFrom;
                    }
                }
            }
        }
        // console.log("before properties");

        const propertiesList = (typeData.mpaPropertiesPtr.entries).map(v => v.data as GenesysTypeLE.GenesysProperty);
        // console.log(`${name} prop length: ${propertiesList.length}`);
        for (const [i, prop] of propertiesList.entries()) {
            // console.log(prop.muId);
            // process.exit();
            
            let hash = localVersionLookup.get(prop.muTypeVersion) ?? "";
            if (hash.length === 0 && parsed.meNativeType !== GenesysType.ENativeType.E_NATIVETYPE_ENUMERATION) {
                try {
                    let offs = i * 0x10 + typeTableStart + ((typeData.muBaseTypeVersion != 0) ? 0x10 : 0);
                    const tableEntry = new GenesysType.GenesysTypeEntry(new KaitaiStream(file.subarray(offs, offs + 0x10)));
                    hash = extractFullHash(tableEntry);
                } catch {}
            }
            
            let maybeName = LEToString(prop.muId);
            let isValidText = true;
            for (const ch of maybeName) {
                if (ch != 0x00 && (ch < 0x30 || (ch > 0x39 && ch < 0x41) || (ch > 0x5A && ch < 0x61) || ch > 0x7A)) {
                    isValidText = false;
                    break;
                }
            }
            let innerName;
            if (isValidText) {
                innerName = maybeName.map(n => String.fromCharCode(n)).join("");
            }

            const LEHash = toLEHash(prop.muId);
            const unhashedName = knownHashes.get(LEHash) ?? innerName;

            localTypeDictionary[name].types.push({
                muID: (`muId: {${LEHash}}${unhashedName ? ` ("${unhashedName}")` : "" }`),
                hash: hash,
                alignment: prop.muTypeAlignment,
                unhashedName: unhashedName,
                offset: prop.muOffset,
                arrayCountSpecified: prop.muCount,
                arrayCountProperyOffset: prop.mpArrayCountPropertyPtr ? ((typeData.mpaPropertiesPtr.entries)[(prop.mpArrayCountPropertyPtr - typeData.mpaPropertiesPtr.offset) / 0x1C].data as any as GenesysTypeLE.GenesysProperty).muOffset : -1,
                valueTypeBits: [prop.mValueType.eValueTypeP1, prop.mValueType.eValueTypeP2, prop.mValueType.eValueTypeP3, prop.mValueType.eValueTypeP4],//[prop.mValueType.eValueTypeP1, prop.mValueType.eValueTypeP2, prop.mValueType.eValueTypeP3, prop.mValueType.eValueTypeP4],
                tableEntryOffset: i
            });
            
            if (localVersionLookup.get(prop.muTypeVersion)) {
                try {
                    await extractType(directory, localVersionLookup.get(prop.muTypeVersion))
                } catch {
                    localErrors.add(localVersionLookup.get(prop.muTypeVersion));
                }
            }
        }

        // if (name === "93_F3_05_00") {
        //     console.log(localTypeDictionary[name]);
        //     process.exit();
        // }
    } else {
        // parses things with a name
        
        if (typeData.muBaseTypeVersion) {
            try {
                const baseTypeTableEntry = new GenesysType.GenesysTypeEntry(new KaitaiStream(file.subarray(typeTableStart, typeTableStart + 0x10)));
                let hash = extractFullHash(baseTypeTableEntry);

                if (checkHashError(hash)) {
                    try {
                        await readFile(__dirname + `/${directory}/GenesysType/${hash}.dat`);
                    } catch {
                        let chkHash = correctStandardHashError(hash);
                        if (IS_E3) {
                            try {
                                await readFile(__dirname + `/${directory}/GenesysType/${chkHash}.dat`);
                            } catch {
                                chkHash = correctE3HashError(hash);
                            }
                        }
                        hash = chkHash;
                    }
                }
                localTypeDictionary[name].extends = hash;

            } catch {}
        }

        for (let i = typeTableStart + ((typeData.muBaseTypeVersion != 0) ? 0x10 : 0), j = 0; i < file.length; i += 0x10, j++) {
            const tableEntry = new GenesysType.GenesysTypeEntry(new KaitaiStream(file.subarray(i, i + 0x10)));
            let hash = extractFullHash(tableEntry);
            
            const innerTypeData = (typeData.mpaPropertiesPtr.entries)[j].data as any as GenesysTypeLE.GenesysProperty;
            
            let maybeName = LEToString(innerTypeData.muId);
            let isValidText = true;
            // console.log(maybeName);
            for (const ch of maybeName) {
                if (ch != 0x00 && (ch < 0x30 || (ch > 0x39 && ch < 0x41) || (ch > 0x5A && ch < 0x61) || ch > 0x7A)) {
                    isValidText = false;
                    break;
                }
            }
            let innerName = "";
            if (isValidText) {
                innerName = maybeName.map(n => String.fromCharCode(n)).join("");
            }
            
            const LEHash = toLEHash(innerTypeData.muId);
            const unhashedName = knownHashes.get(LEHash) ?? innerName;       
            
            // if (LEHash === "6A_44_FE_ED") {
            //     console.log("thing was found: ", knownHashes.get(LEHash));
            // }
            
            localTypeDictionary[name].types.push({
                muID: (`muId: {${LEHash}}${unhashedName ? ` ("${unhashedName}")` : "" }`),
                hash: hash,
                alignment: innerTypeData.muTypeAlignment,
                unhashedName: unhashedName,
                offset: innerTypeData.muOffset,
                arrayCountSpecified: innerTypeData.muCount,
                arrayCountProperyOffset: innerTypeData.mpArrayCountPropertyPtr ? ((typeData.mpaPropertiesPtr.entries)[(innerTypeData.mpArrayCountPropertyPtr - typeData.mpaPropertiesPtr.offset) / 0x1C].data as any as GenesysTypeLE.GenesysProperty).muOffset : -1,
                valueTypeBits: [innerTypeData.mValueType.eValueTypeP1, innerTypeData.mValueType.eValueTypeP2, innerTypeData.mValueType.eValueTypeP3, innerTypeData.mValueType.eValueTypeP4],
                tableEntryOffset: tableEntry.position
            });

            try {
                await extractType(directory, hash)
            } catch {
                localErrors.add(hash);
            }
        }
    }

    if (localTypeDictionary[name].extends.length > 0) { 
        if (!typeExtensions[localTypeDictionary[name].extends]) {
            typeExtensions[localTypeDictionary[name].extends] = new Set();
        }
        typeExtensions[localTypeDictionary[name].extends].add(name);
    }

    return;
}

const extractEnum = async (directory: string, name: string) => {
    if (Object.keys(localTypeDictionary).includes(name) && localTypeDictionary[name].types.length > 0) return;
    
    const path = __dirname + `/${directory}/GenesysType/${name}.dat`;
    const file = await readFile(path);

    const parsed = new GenesysType(new KaitaiStream(file));
    const typeData = parsed.typeData as GenesysTypeLE.GenesysNativetypeObjectData;

    // localErrors.add(name);
}

const sortDepdendencies = (dict: TypeDictionary) => {
    const dependencyHashes = {};
    for (const [hash, data] of Object.entries(dict).sort(([h1, d1], [h2, d2]) => (d1.name < d2.name) ? -1 : (d1.name > d2.name) ? 1 : 0)) {
        dependencyHashes[hash] = new Set();
        for (const t of data.types) {
            (dependencyHashes[hash]).add(t.hash);
        }
        dependencyHashes[hash].add(data.extends);
    }
    // console.log(dependencyHashes);

    const helper = (src: {[key: string]: Set<string>}, keys: string[], entry: [number, string], visited: {[key: string]: boolean}, res: any[]) => {
        visited[entry[1]] = true;
        // console.log(src[entry[1]]);
        for (const val of src[entry[1]]) {
            if (visited[val] === false)
                helper(src, keys, [keys.indexOf(val), val], visited, res)
        }

        res.unshift(entry[1]);
    }

    const topoSort = (src: {[key: string]: Set<string>}) => {
        const keys = Object.keys(src);

        const visited: {[key: string]: boolean} = {}
        for (const k of keys) visited[k] = false;
        const result = [];
        for (const [idx, key] of keys.entries()) {
            // console.log(idx);
            if (visited[key] === false) 
                helper(src, keys, [idx, key], visited, result); 
        }

        return result;
    }
    
    return (topoSort(dependencyHashes) as string[]).reverse()
}

const createDictionaryData = (dict: TypeDictionary, errorSet: Set<string>) => {
    // console.log(errorSet);

    const order = sortDepdendencies(dict);
    const out = ["146165144147145160157160060061o", "\n"];
    // for (const [hash, data] of Object.entries(dict).sort(([h1, d1], [h2, d2]) => (d1.name < d2.name) ? -1 : (d1.name > d2.name) ? 1 : 0)) {
    for (const hash of order) {
        const data = dict[hash];
        
        let extendsFrom = (dict[data.extends] ?? {name: data.extends}).name;
        out.push(`${data.name}${extendsFrom.length > 0 ? ' extends ' + extendsFrom: ''}\n  >> 14: (${hash})\n  >> id: (${data.muVersionID})`);
        // out.push(`>> 15: (${data.objectHash})`);
        // if (data.name === "02_5E_0F_00") {
        //     console.log(data.name, data);
        // }
        for (const t of data.types) {
            // console.log(t.hash);
            // console.log(dict[t.hash]);
            // if (Math.random() < 1) process.exit();

            let builder = "  0x" + (t.offset.toString(16).toUpperCase()).padEnd(4, ' ')+ ": ";            
            if (dict[t.hash] == undefined) {
                builder += t.hash;
            } else {
                builder += (dict[t.hash].name ?? t.hash);
            }
            if (t.arrayCountSpecified > 1) {
                builder += ` [${t.arrayCountSpecified}]`;
            }
            for (const val of t.valueTypeBits) {
                if (val === 0) break;
                else if (val === 1) builder += " *";
                else if (val === 2) builder += ` [size @ 0x${t.arrayCountProperyOffset.toString(16).toUpperCase()}]`;
                else if (val === 3) builder += " (offset)";
                else if (val === 4) builder += " (count)";
            }

            builder += `\n           ${t.muID}`;
            out.push(builder);
        }
        out.push("");
    }

    if (errorSet.size > 0) {
        out.push("\n> enum (or error) files: ");
        out.push([...errorSet.values()].join('\n'));
    }

    return out.join('\n');
}

const toSnakeCase = (str: string) => {
    // console.log(str);
    return str.replace(/\./g, '_').replace(/([a-z_])([A-Z])/g, '$1_$2').toLowerCase();
}

const commonTypesList = ['char','bool8_t','uint32_t','int32_t','uint16_t','int16_t','uint8_t','int8_t','float32_t','str','u1','u2','u4','s1','s2','s4','f4'];
const commonTypesToKaitaiType = (t: string) => {
    switch (t) {
        case 'char': return 'str';
        case 'bool8_t': return 'u1';
        case 'uint32_t': return 'u4';
        case 'int32_t': return 's4';
        case 'uint16_t': return 'u2';
        case 'int16_t': return 's2';
        case 'uint8_t': return 'u1';
        case 'int8_t': return 's1';
        case 'float32_t': return 'f4';
        case 'CgsCore.UniqueId': return 'u4';
        case 'CgsCore.StringBase': return 'string_base';
        case 'Genesys.Object': return 'genesys_object';
        default:
            return undefined;
    }
}

const commonTypesToSize = (t: string, types?: {[key: string]: KaitaiStructData}): number => {
    switch (t) {
        case 'char': return 1; 
        case 'bool8_t': return 1; 
        case 'uint32_t': return 4; 
        case 'int32_t': return 4; 
        case 'uint16_t': return 2; 
        case 'int16_t': return 2; 
        case 'uint8_t': return 1; 
        case 'int8_t': return 1; 
        case 'float32_t': return 4;
        case 'str': return 1;
        case 'u1': return 1;
        case 'u2': return 2;
        case 'u4': return 4;
        case 's1': return 1;
        case 's2': return 2;
        case 's4': return 4;
        case 'f4': return 4;

        case 'CgsCore.UniqueId': return 4;
        case 'Genesys.Object': return 12; 
        default:
            if (types && types[t]) {
                return types[t].instances['size']?.value as number ?? 4;
            }
            return 4;
    }
}


interface KaitaiSeqEntry {
    id: string;
    size?: string | number;
    type?: string;
    doc?: string;
    repeat?: 'expr';
    ['repeat-expr']?: string | number; 
}

interface KaitaiInstance {
    value?: string | number;
    pos?: string;
    type?: string;
    doc?: string;
    size?: string | number;
    ['if']?: string;
    repeat?: 'expr';
    ['repeat-expr']?: string | number;
}

interface KaitaiStructData {
    seq: KaitaiSeqEntry[];
    instances: {
        [key: string]: KaitaiInstance;
    }
}

interface KaitaiGeneratorOutput {
    thisType: KaitaiStructData
    types: {
        [key: string]: KaitaiStructData;
    };
    enums: {[key: string]: {[key: number]: string}};
}

interface KaitaiInstances {[key: string]: KaitaiInstance}

const generateParserEnum = (data: TypeDictionary[''], enums: KaitaiGeneratorOutput['enums']) => {
    const newEnum = {};
    for (const [idx, t] of data.types.entries()) {
        let unhashedName = t.unhashedName;
        if (unhashedName && unhashedName.charAt(0).match(/\d/g)) {
            unhashedName = 'ev' + unhashedName;
        }
        
        newEnum[idx] = 
            unhashedName ? toSnakeCase(unhashedName) : `ev${idx}`;
    }
    enums['e_' + data.name.toLowerCase()] = newEnum;
}

const generateParserStructs = (target: string, dict: TypeDictionary, types: {[key: string]: KaitaiStructData}, enums: KaitaiGeneratorOutput['enums']): KaitaiGeneratorOutput | undefined => {
    const targetHash = nameToHash.get(target);

    const seq: KaitaiSeqEntry[] = [];
    const instances: KaitaiInstances = {};
    // for (const [hash, data] of Object.entries(dict).sort(([h1, d1], [h2, d2]) => (d1.name < d2.name) ? -1 : (d1.name > d2.name) ? 1 : 0)) {

    if (!dict[targetHash]) {
        return {
            thisType: {
                seq,
                instances
            },
            types: types,
            enums: enums
        };
    }

    const data = dict[targetHash];
    
    // if (target === 'Genesys.Gen.SequenceItem') {
    //     console.log(data)
    // }

    if (!data.types.length) {
        return {
            thisType: {
                seq,
                instances
            },
            types: types,
            enums: enums
        };
    }
    else if (data.types[0].hash === '') {
        generateParserEnum(data, enums);
        return {
            thisType: {
                seq,
                instances
            },
            types: types,
            enums: enums
        };
    }
    
    let parentSize = 0;

    let hasBase = false;
    if (data.extends && dict[data.extends].name === 'Genesys.Object') {
        hasBase = true;
        seq.push({
            id: 'base_object',
            type: 'genesys_object'
        });
    } else if (data.extends && dict[data.extends].name) {
        hasBase = true;
        const parsedBase = generateParserStructs(dict[data.extends].name, dict, types, enums);
        let ksyBaseName = toSnakeCase(dict[data.extends].name);
        if (ksyBaseName.match(/^\d/g)) {
            ksyBaseName = 't_' + ksyBaseName;
        }
        if (parsedBase) {
            types[ksyBaseName] = parsedBase.thisType;
            parentSize = parsedBase.thisType.instances['size'].value as number;
        }

        seq.push({
            id: 'base_object',
            type: ksyBaseName
        })
    } else if (data.extends) {
        hasBase = true;
        const newEntry = {id: 'base_object', type: data.extends};
        if (data.extends.match(/^[0-9]/g)) {
            newEntry.type = 't_' + newEntry.type;
        }
        seq.push(newEntry);
    }

    const arrayLengthOffsets: {[key: number]: number} = {};
    
    for (const [idx, t] of data.types.entries()) {
        if (t.offset < parentSize) continue;    

        // some of the hackiest code i've ever written good LORD
        if (idx != 0) {
            const prevSeq = seq[seq.length - 1];
            let prevOffset = seq.length === 1 ? 0 : data.types[idx - 1].offset;
            let prevSize = ((prevSeq.size as number) ?? (commonTypesToSize(prevSeq?.type, types) ?? prevSeq.size as number));
            if (prevSeq.repeat) {
                prevSize *= prevSeq['repeat-expr'] as number;
            }

            const postPosition = prevOffset + prevSize;
            if (postPosition != t.offset) {
                seq.push({id: `padding_pre_0x${t.offset.toString(16)}`, size: t.offset - postPosition})
            }
        } else if (t.offset > 0xC) {
            seq.push({id: `padding_pre_data_0x${t.offset.toString(16)}`, size: t.offset - 0xC})
        }

        if (arrayLengthOffsets[t.offset] != undefined) {
            const newSeqEntry: KaitaiSeqEntry = {
                id: 'array_count_for_0x' + arrayLengthOffsets[t.offset].toString(16).toLowerCase()
            };

            let typeName
            try {
                typeName = commonTypesToKaitaiType(dict[t.hash].name) 
                    ?? toSnakeCase(dict[t.hash].name);
            } catch {
                console.log(2, t.hash);
                process.exit();
            }
            newSeqEntry.type = typeName;

            if (t.unhashedName) {
                newSeqEntry.doc = `"${t.unhashedName}"`;   
            }
            if (newSeqEntry.type.match(/^[0-9]/g)) {
                newSeqEntry.type = `t_` + newSeqEntry.type;
            }

            seq.push(newSeqEntry);
            continue;
        }

        const newSeqEntry: KaitaiSeqEntry = {
            id: ''
        };

        let idPrefix = "";
        let id = "";
        let idOffset = `_0x${t.offset.toString(16).toLowerCase()}`;
        let typeName = '';
        let willBeInstance = false;
        let instanceArray = false;

        if (t.unhashedName) {
            id = toSnakeCase(t.unhashedName);
        } else if (dict[t.hash] == undefined) {
            id = t.hash.toLowerCase();
        } else {
            id = toSnakeCase(dict[t.hash].name);
            if (id.match(/^\d/g)) {
                id = 't_' + id;
            }
            if (!commonTypesList.includes(id) && !types[id]) {
                const newStructData = generateParserStructs(dict[t.hash].name, dict, types, enums);
                types[id] = newStructData.thisType;
            }
        }

        // console.log(0, id)

        if (!dict[t.hash]) {
            // console.log(target, t);
            typeName = t.hash;
        } else {
            typeName = commonTypesToKaitaiType(dict[t.hash].name) 
                ?? toSnakeCase(dict[t.hash].name)
                ?? id;
        }

        // console.log(typeName, dict[t.hash].name, id);

        newSeqEntry.type = typeName;

        for (const val of t.valueTypeBits) {
            if (val === 0) break;
            else if (val === 1) { 
                willBeInstance = true;
                newSeqEntry.type = 'u4';
                idPrefix += "ptr_" // " *";
            } 
            else if (val === 2) {
                instanceArray = true;
                arrayLengthOffsets[t.arrayCountProperyOffset] = t.offset;
                idPrefix += "arr_" // ` [size @ 0x${t.arrayCountProperyOffset.toString(16).toUpperCase()}]`;
            }
            else if (val === 3) {
                willBeInstance = true;
                idPrefix += "ofs_"; // " (offset)";
                newSeqEntry.type = 'u4';
            }
            else if (val === 4) idPrefix += "cnt_" // " (count)";
        }

        if (t.arrayCountSpecified && t.arrayCountSpecified > 1) {
            idPrefix += 'inline_';
            newSeqEntry.repeat = 'expr';
            newSeqEntry['repeat-expr'] = t.arrayCountSpecified;
            willBeInstance = false;
        }
        
        if (id.charAt(0).match(/\d/g)) {
            idPrefix += 'id_';
        }

        newSeqEntry.id = idPrefix + id + idOffset;
        
        let nameToCompare = dict[t.hash] ? dict[t.hash].name : typeName;
        let treatAsEnum = (dict[t.hash] && dict[t.hash].isEnum)
         || (!dict[t.hash] && nameToCompare.match(/([A-Fa-f0-9]{2}_){3}/g)); 

        if (treatAsEnum) {
            
            newSeqEntry.doc = `enum; ${nameToCompare.toLowerCase()}`;
            if (idx + 1 < data.types.length) {
                typeName = ({
                    1: 'u1',
                    2: 'u2',
                    4: 'u4'
                })[data.types[idx + 1].offset - t.offset] ?? 'u1';
                newSeqEntry.type = typeName;
            } else {
                typeName = ({
                    1: 'u1',
                    2: 'u2',
                    4: 'u4'
                })[4 - t.offset % 4]
                newSeqEntry.type = typeName;
            }
            if (newSeqEntry.id.match(/_[A-Fa-f0-9]{2}_/g)) {
                newSeqEntry.id = `unk_enum` + idOffset;
            }
        }

        if (willBeInstance) {
            let instanceTypeName = typeName;
            let extendsNonGeneric = false;
            if (typeName.match(/^\d/g)) 
                instanceTypeName = `t_` + typeName;
            // console.log(typeName);
            if (typeExtensions[t.hash]) {
                instanceTypeName = `generic_gen_object`
                extendsNonGeneric = true;
            };

            if (idPrefix.includes('ptr_ptr_') || idPrefix.includes('_arr_ptr')) {
                instanceTypeName = `ptr('${instanceTypeName}')`;
            }
            const instanceId = `inst_` + id + idOffset;
            instances[instanceId] = {
                pos: newSeqEntry.id,
                type: instanceTypeName,
                ["if"]: `${newSeqEntry.id} != 0`,
                doc: extendsNonGeneric ? `'instance of ${dict[t.hash].name}'` : undefined
            }
            if (instanceArray) {
                if (typeName == 'str') {
                    instances[instanceId].size = `array_count_for${idOffset}`
                } else {
                    instances[instanceId].repeat = 'expr';
                    instances[instanceId]['repeat-expr'] = `array_count_for${idOffset}`;
                }
            }

        }

        if (!commonTypesList.includes(typeName) && !types[typeName]) {
            const newStructData = generateParserStructs(nameToCompare, dict, types, enums);
            types[typeName] = newStructData.thisType;
        }

        if (newSeqEntry.type === 'cgs_resource__handle') {
            newSeqEntry.size = 0x8;
            delete newSeqEntry.type;
        } else if (newSeqEntry.type.match(/^\d/g)) {
            newSeqEntry.type = `t_` + newSeqEntry.type;
        }

        seq.push(newSeqEntry);
    }

    const lastType = data.types[data.types.length - 1];
    if (lastType) {
        const lastSeq = seq[seq.length - 1];
        let lastSeqSize = commonTypesToSize(seq[seq.length - 1].type, types);
        if (lastSeq.repeat) {
            lastSeqSize *= lastSeq['repeat-expr'] as number; 
        }
        
        let finalSize = (lastType.offset >= parentSize ? lastType.offset : 0) + lastSeqSize;
    
        if (finalSize % 4 != 0) {
            seq.push({
                id: 'padding',
                size: 4 - (finalSize % 4)
            });
            finalSize += 4 - (finalSize % 4);
        }
    
        instances['size'] = { value: finalSize }
        instances['mu_version_hash'] = { value: '0x' + data.muVersionID.toLowerCase() }
    }

    // if (data.name.startsWith('rw.math.vpu.Vector')) {
    //     seq.push({
    //         id: 'vec_padding',
    //         size: 0x10 - (instances['size'].value as number)
    //     });
    //     instances['size'] = { value: 0x10 }
    // }

    for (const t of Object.keys(types)) {
        if (t.match(/^[0-9]/g)) {
            types[`t_` + t] = types[t];
            delete types[t];
        }
    }

    const out = {
        thisType: {
            seq,
            instances
        },
        types: types,
        enums: enums
    };
    return out;
}

const generateParser = (target: string, dict: TypeDictionary, errorSet: Set<string>) => {
    // console.log(errorSet);

    // const order = sortDepdendencies(dict);

    // for (const [hash, data] of Object.entries(dict).sort(([h1, d1], [h2, d2]) => (d1.name < d2.name) ? -1 : (d1.name > d2.name) ? 1 : 0)) {
    
    let out: {enums?: any, types?: any, seq?: any, instances?: any} = {
        enums: {},
        types: {}
    };
    if (target === 'generic_gen_object') {
        let types: {[key: string]: KaitaiStructData} = {};
        let enums = {};
        for (const [k, v] of Object.entries(dict)) {
            const generated = generateParserStructs(v.name, dict, types, enums);
            types[toSnakeCase(v.name)] = generated.thisType;
        }

        let seq = [
            {id: "save_ofs", size: 0, if: 'ofs < 0'},
            {id: 'obj', type: 'genesys_object'}
        ];
        let instances = {
            ofs: {
                value: '_io.pos'
            },
            data: {
                pos: 'ofs',
                type: {
                    ['switch-on']: 'obj.mu_type_version',
                    cases: {} 
                }
            }
        }
        types['genesys_object'] = {
            seq: [
                {id: 'dynamic_gamedata', size: 0x8},
                {id: 'mu_type_version', type: IS_E3 ? 'u4le' : 'u4be'}
            ],
            instances: {}
        };

        for (const [name, t] of Object.entries(types)) {
            // console.log(name, t.instances['mu_version_hash']);
            if (t.instances['mu_version_hash']) {
                instances.data.type.cases[t.instances['mu_version_hash'].value] = name;
            }
        }
        types['genesys_obj_collection'] = {
            seq: [
                {id: 'base_object', type: 'gen_obj'},
                {id: 'unk_id', type: 'u4'},
                {id: 'collection_start_offset', type: 'u4'},
                {id: 'collection_count', type: 'u2'},
                {id: 'padding', size: 0x2}
            ],
            instances: {
                obj_collection: {
                    pos: 'collection_start_offset',
                    type: "ptr('generic_gen_object')",
                    repeat: 'expr',
                    "repeat-expr": 'collection_count'
                }
            }
        }
        delete types.string_base;


        instances.data.type.cases['0xbc_85_5d_7f'] = 'genesys_obj_collection';

        out = {
            seq,
            instances,
            enums,
            types
        }
    } else {
        const targetHash = nameToHash.get(target);
        if (!dict[targetHash]) {
            return 'TYPE NOT FOUND: ' + target;
        }
    
        const structParserResult = generateParserStructs(target, dict, {}, {});
        delete structParserResult.types.string_base;
        
        out = {
            seq: structParserResult.thisType.seq,
            instances: structParserResult.thisType.instances,
            enums: structParserResult.enums,
            types: structParserResult.types
        };
    }


    // if (errorSet.size > 0) {
    //     out.push("\n> enum (or error) files: ");
    //     out.push([...errorSet.values()].join('\n'));
    // }

    const switcherTypes = [];
    for (const name of Object.keys(out.types)) {
        switcherTypes.push(`'"${name}"': ${name}`);
    }
    if (target === 'generic_gen_object') {
        switcherTypes.push(`'"generic_gen_object"': generic_gen_object`)
    }

    
    return scaffoldedKSY
        .replace(`$$NAME$$`, toSnakeCase(target.substring(target.lastIndexOf('.') + 1)))
        .replace(`# $$DATA$$`, YamlStringify(out))
        .replace(`# $$SWITCHER_TYPES$$`, switcherTypes.join('\n'.padEnd(13, ' ')))
        .replace(/genesys_object/g, 'gen_obj')
        .replace(/ptr\('gen_obj'\)/g, `ptr('generic_gen_object')`);
}

const process_files = async (directory: string, names: string[], resultName: string) => {
    for (const name of names) {
        try {
            await extractType(directory, name);
        } catch(e) {
            console.log(e);
            process.exit();
            localErrors.add(name);
        }
    }

    for (const err of localErrors) {
        // console.log("localerr: ", err);
        try {
            await extractEnum(directory, err);
        } catch {
            if (err.endsWith('_1')) {
                try {
                    await extractEnum(directory, err.slice(0, err.length - 2));
                    localErrors.delete(err);
                } catch {
                    delete localTypeDictionary[err];
                    console.log("ENUM ERROR: " + err)
                }
            } else {
                delete localTypeDictionary[err];
                console.log("ENUM ERROR: " + err)
            }
            // console.log(e);
        }
    }

    await writeFile(ROOT_PATH + `/_generated_from_type_tool/${resultName}_output.txt`, createDictionaryData(localTypeDictionary, localErrors), 'ascii');
    
    typeDictionary = {...typeDictionary, ...localTypeDictionary};
    versionLookup = new Map([...versionLookup, ...localVersionLookup]);
    errors = new Set([...errors, ...localErrors]);

    localTypeDictionary = {};
    localVersionLookup = new Map();
    localErrors = new Set();
    // console.log(localErrors);
}

const main = async () => {
    // THIS IS WHERE YOU PLACE THE PATHS TO THE GenesysType FOLDERS
    // the first part is the path, the 2nd part is what the resulting file will be named
    
    let pathNameResultPair = BNDL_LIST;
    
    if (process.argv[2] === 'EVERYTHING') {
        const FULL_DIR = await readdir(__dirname + '/../ALL_BNDL')
        pathNameResultPair = FULL_DIR.filter(v => !v.endsWith('.BNDL') && !v.endsWith(`.exe`) && !v.endsWith('.py') && v != '_generated_from_type_tool').map(v => {
            return ['/../ALL_BNDL/' + v, v];
        })
    }

    (await readFile(ROOT_PATH + "/foundHashes.txt", "ascii")).split("\n").forEach(v => {
        let pair = v.split(',');
        // console.log(pair);
        knownHashes.set(pair[0], pair[1]);
    })

    for (const [idx, [path, fileName]] of pathNameResultPair.entries()) {
        const names = readdirSync(ROOT_PATH + `/${path}/GenesysType`)
            .map(n => n.slice(0, n.length - 4));


        console.log(`${idx} / ${pathNameResultPair.length}: ${fileName}`);
        await process_files(path, names, fileName);
    }
    // sortDepdendencies(typeDictionary);
    await writeFile(ROOT_PATH + `/_generated_from_type_tool/MERGED_output.txt`, createDictionaryData(typeDictionary, errors), 'ascii');
    
    scaffoldedKSY = await readFile(ROOT_PATH + `/KSY_SCAFFOLD.ksy`, 'ascii');

    // console.log(typeExtensions);
    const typeIdx = process.argv[2] !== 'E3' ? 2 : 3;
    console.log(typeIdx);
    let generatedParserType = process.argv[typeIdx];
    if (generatedParserType == 'all' || generatedParserType == 'EVERYTHING') {
        generatedParserType = 'generic_gen_object';
    }
    if (generatedParserType) {
        await writeFile(ROOT_PATH + `/_generated_from_type_tool/${toSnakeCase(generatedParserType.substring(generatedParserType.lastIndexOf('.') + 1))}.ksy`, generateParser(generatedParserType, typeDictionary, errors), 'ascii');
    }
}

main();
