import { BaseField, Endian, Pointer32 as _Pointer32, Struct, StructType, U16, U32, U32s, U8, U8s, I8, I16, I32, I16s } from "construct-js";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import { F32, F32s } from "../../helpers/floatfield";
import { CleanKStruct } from "../../helpers/recursiveOmit";

const u1 = U8;
const u2 = U16;
const u4 = U32;
const s1 = I8;
const s2 = I16;
const s4 = I32;

const f4 = F32;
const IMPORT_ARRAY: StructType[] = [];
let MAIN_STRUCT: StructType;
let PtrPath: string[] = [];

PtrPath.toString = () => {
    return PtrPath.join('.');
}

const P32 = (offsetName: string, pathOffset?: number) => {
    if (PtrPath.length === 0 || PtrPath.slice(0, pathOffset).length === 0) {
        return _Pointer32(MAIN_STRUCT, offsetName);
    }
    return _Pointer32(MAIN_STRUCT, PtrPath.slice(0, pathOffset).join('.').replace(/\.\./g, '.') + '.' + offsetName);
}

const NullableP32 = (isDefined: number | object | undefined, name: string, pathOffset?: number) => {
    return isDefined ? P32(name, pathOffset) : u4(0);
}

const PUSH_IMPORT = (ImportID: number, _P32: ReturnType<typeof _Pointer32>) => {
    const event_import = Struct('event_import_base')
        .field('ID', u4(ImportID, Endian.Big))
        .field('always-1', u4(0x1, Endian.Big))
        .field('offset', _P32)
        .field('padding', U8s([0, 0, 0, 0]));

    IMPORT_ARRAY.push(event_import);
}

const BUILD_ptr_ptr_table = (offsetName: string, structName: string, builder: CallableFunction, arrayData: GenObj.Ptr[]) => {
    // PtrPath.push(offsetName);
    const data = Struct(structName + 'Array');
    const ptrArray = Struct(structName + 'PtrArray');
    
    if (arrayData) {
        for (const [idx, val] of arrayData.map(v => v.data.data as any).entries()) {
            data
                .field(`entry_${idx}`, builder(`${offsetName}Data.entry_${idx}`, val));
            
            ptrArray
                .field(`ptr_entry_${idx}`, P32(`${offsetName}Data.entry_${idx}`));
        }
    }
    if (PtrPath.includes('event_array.event_4')) {
        console.log(PtrPath + '.' + offsetName);
        console.log(arrayData);
        console.log(data);
        console.log(ptrArray);
    }


    // PtrPath.pop();
    return {
        data,
        ptrArray
    };
}

const BUILD_data_array = (offsetName: string, structName: string, builder: CallableFunction, arrayData: any[]) => {
    PtrPath.push(offsetName);
    const data = Struct(structName + 'Array');
    if (arrayData) {
        for (const [idx, val] of arrayData.entries()) {
            data
                .field(`entry_${idx}`, builder(`entry_${idx}`, val));
        }
    }
    PtrPath.pop();
    return data;
}

const BUILD_vpu_vector3 = (offsetName: string, obj: CleanKStruct<GenObj.RwMathVpuVector3>) => {
    PtrPath.push(offsetName);
    const vpu_vector3 = Struct('vpu_vector3')
        .field('elements', F32s(obj.arrInlineElements0x0));
        
    PtrPath.pop();
    return vpu_vector3;
}

const APPEND_genesys_object = (builder: StructType, obj: CleanKStruct<GenObj.GenObj>, id?: number) => {
    // PtrPath.push('base_object');

    builder
        .field('dynamicData', U8s(new Array(8).fill(0)))
        .field('muID', U32(obj.muTypeVersion, Endian.Big));
    
    if (id) {
        PUSH_IMPORT(id, P32('dynamicData'))
    }
    
    // PtrPath.pop();
}

const BUILD_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenGameplayAllowedVehicleListVehicleAndMods>) => {
    PtrPath.push(offsetName);

    const out = Struct('vehicle_and_mods');
    
    APPEND_genesys_object(out, obj.baseObject, 0xAA_1D_10_00);
    
    out
        .field('vehicle_0xc', u4(obj.vehicle0xc))
        .field('float32_t_0x10', f4(obj.float32T0x10))
        .field('ptr_arr_mods_0x14', NullableP32(obj.instMods0x14, offsetName + '_instMods', -1))
        .field('inline_arr_target_scores_0x18', I16s(obj.arrInlineTargetScores0x18))
        .field('inline_arr_target_speeds_0x1e', I16s(obj.arrInlineTargetSpeeds0x1e))
        .field('array_count_for_0x14', u2(obj.instMods0x14 ? obj.instMods0x14.length : 0))
        .field('array_count_for_0x18', u2(obj.arrInlineTargetScores0x18.length))
        .field('array_count_for_0x1e', u2(obj.arrInlineTargetSpeeds0x1e.length))
        .field('difficulty_0x2a', u1(obj.difficulty0x2a))
        .field('padding', U8s(new Array(1).fill(0)))
    

    // console.log(out.computeBufferSize());

    const modsArray = Struct('instModsArray');
    if (obj.instMods0x14) {
        modsArray
            .field('instMods0x14', U32s(obj.instMods0x14));
    }

    PtrPath.pop();
    return {
        mainObj: out,
        modsArray
    };
}

const BUILD_genesys__gen__gameplay__allowed_vehicle_list = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenGameplayAllowedVehicleList>) => {
    PtrPath.push(offsetName)
    const out = Struct('allowed_vehicle_list');

    APPEND_genesys_object(out, obj.baseObject, 0xF5_30_0F_00);
    out
        .field('game_changer_id_0xc', u4(obj.gameChangerId0xc))
        .field('ptr_arr_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10', 
            NullableP32(obj.instGenesysGenGameplayAllowedVehicleListVehicleAndMods0x10, 'vehsList'))
        .field('array_count_for_0x10', u2(obj.instGenesysGenGameplayAllowedVehicleListVehicleAndMods0x10?.length ?? 0))
        .field('padding', U8s(new Array(2).fill(0)))

    if (obj.instGenesysGenGameplayAllowedVehicleListVehicleAndMods0x10) {
        const instVehs = Struct('vehs');
        const instModsArr = [];
        for (const [idx, val] of obj.instGenesysGenGameplayAllowedVehicleListVehicleAndMods0x10.entries()) {
            const built = BUILD_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods(`vehsList.entry_${idx}`, val)
            instVehs
                .field(`entry_${idx}`, built.mainObj);
            instModsArr.push(built.modsArray);
        }
        for (const [idx, arr] of instModsArr.entries()) {
            instVehs.field(`entry_${idx}_instMods`, arr);
        }
        out
            .field(`vehsList`, instVehs)
    }

    PtrPath.pop()

    return out;
}

export const BUILD_FILE = (obj: CleanKStruct<GenObj.GenesysObjCollection>) => {
    IMPORT_ARRAY.splice(0, IMPORT_ARRAY.length)

    const vehListFile = Struct('vehicleListFile')
    MAIN_STRUCT = vehListFile;

    APPEND_genesys_object(vehListFile, obj.baseObject, 0xF8_FF_FF_FF)

    vehListFile
        .field('GameChangerID', u4(obj.unkId))
        .field('Item', P32('vehPtrs'))
        .field('ItemCount', u4(obj.objCollection?.length ?? 0))


    const vehListPointers = Struct('vehPtrs');
    const allVehLists = Struct('allVehLists');

    if (obj.objCollection) {
        for (const [idx, itm] of obj.objCollection.entries()) {
            allVehLists
                .field(`veh_${idx}`, BUILD_genesys__gen__gameplay__allowed_vehicle_list(`vehls.veh_${idx}`, (itm.data.data as GenObj).data as GenObj.GenesysGenGameplayAllowedVehicleList));
            vehListPointers.field(`veh_${idx}_ptr`, P32(`vehls.veh_${idx}`))
        }
    }

    vehListFile.field('vehPtrs', vehListPointers);
    vehListFile.field('vehls', allVehLists);

    const currentSize = vehListFile.computeBufferSize();
    const bytesToPad = 0x10 - (currentSize % 0x10);

    if (bytesToPad > 0) {
        vehListFile.field('PRE_IMPORT_PADDING', U8s(new Array(bytesToPad)));
    }
    

    // console.log(vehListFile);
    IMPORT_ARRAY.sort((a, b) => {
        return (a.get('offset') as BaseField).get() - (b.get('offset') as BaseField).get()
    });
    for (const [idx, imp] of IMPORT_ARRAY.entries()) {
        const offsetField = (imp.get('offset') as BaseField);

        const veh_import = Struct('veh_import')
            .field('ID', imp.get('ID'))
            .field('always-1', imp.get('always-1'))
            .field('offset', U32((offsetField.get() | 0x80_00_00_00) >>> 0, Endian.Little))
            .field('padding', U8s([0, 0, 0, 0]));

        vehListFile.field(`IMPORT_${idx}`, veh_import);
    }

    return vehListFile.toUint8Array();
}
