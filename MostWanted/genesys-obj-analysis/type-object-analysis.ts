import KaitaiStream from 'kaitai-struct/KaitaiStream';
import { readFile, writeFile } from 'fs/promises';
import { GenericGenObject } from './generic-gen-object';
import { readdirSync } from 'fs';
import { stringify as YAMLStringify } from 'yaml';
import { CleanKStruct } from '../helpers/recursiveOmit';

const toLEHash = (num: number) => {
    return num.toString(16).replace(/^(.(..)*)$/, "0$1").match(/../g).reverse().join("").padEnd(8, '0').match(/(..)/g).join("_").toUpperCase();
}

// const LEToString = (num: number) => {
//     return num.toString(16).replace(/^(.(..)*)$/, "0$1").match(/../g).map(s => parseInt(s, 16));
// }

const LEToDecimal = (str: string) => {
    return parseInt(str.replace(/([A-F0-9]{2})_([A-F0-9]{2})_([A-F0-9]{2})_([A-F0-9]{2})/gi, '$4$3$2$1'), 16);
}

interface GenesysObjectData {
    idString: string;
    idValue: number;
    typeName: string;
    extraInfos?: any;
};
 
let inProgressInfoList: GenesysObjectData[] = [];

const extractBasicInfo = async (directory: string, fileName: string) => {

    const path = __dirname + `/${directory}/GenesysObject/${fileName}.dat`;
    const file = await readFile(path);
    const parsed: CleanKStruct<GenericGenObject> = new GenericGenObject(new KaitaiStream(file));


    const newObjData: GenesysObjectData = {
        idString: fileName,
        idValue: parseInt('0x' + LEToDecimal(fileName), 16),
        typeName: parsed.data ? parsed.data.constructor.name : 'unknown?'
    };

    let extraInfos: any = {};
    switch (newObjData.typeName) {
        case 'GenesysObjCollection': {
            const dataCollection = parsed.data as CleanKStruct<GenericGenObject.GenesysObjCollection>;

            extraInfos.count = dataCollection.collectionCount;
            const objTypes: Set<string> = new Set();

            for (const [idx, entry] of dataCollection.objCollection.entries()) {
                objTypes.add((entry.data.data as GenericGenObject).data.constructor.name);
            }
            extraInfos.types = Array.from(objTypes);
            newObjData.extraInfos = extraInfos;
        } break;
        case 'GenesysGenEasyGuidePage': {
            const pageInfo = parsed.data as CleanKStruct<GenericGenObject.GenesysGenEasyGuidePage>;
            
            extraInfos.text = [];
            for (const [idx, txtID] of pageInfo.instText0x1c.entries()) {
                extraInfos.text.push(toLEHash(txtID));
            }
        } break;
        case 'GenesysGenRaceBalancingProfile': {
            const profile = parsed.data as CleanKStruct<GenericGenObject.GenesysGenRaceBalancingProfile>;

            extraInfos.minSpeed = profile.minSpeed0x14;
            extraInfos.maxSpeed = profile.maxSpeed0x10;
        } break;
        case 'GenesysGenRaceBalancingData': {
            const data = parsed.data as CleanKStruct<GenericGenObject.GenesysGenRaceBalancingData>;
            
            extraInfos.opponentDataCount = data.instOpponentData0x18.length;
        } break;
        case 'GenesysGenOnlineRoute': {
            const route = parsed.data as CleanKStruct<GenericGenObject.GenesysGenOnlineRoute>;

            extraInfos.checkpointCount = route.instCheckpoints0xc.length;
        } break;
        case 'GenesysGenEventArena': {
            const arena = parsed.data as CleanKStruct<GenericGenObject.GenesysGenEventArena>;

            extraInfos.numLockdownPoints = arena.instArenaData0x20.arrayCountFor0x14;
            extraInfos.numPointToPointCheckpoints = arena.instArenaData0x20.arrayCountFor0x18;
            extraInfos.numRepairPoints = arena.instArenaData0x20.arrayCountFor0x1c;
            extraInfos.numSpawnLocations = arena.instArenaData0x20.arrayCountFor0x20;
            extraInfos.numChevrons = arena.instArenaData0x20.arrayCountFor0x28;
            extraInfos.numCustomChevronList = arena.instArenaData0x20.arrayCountFor0x2c;
            extraInfos.numTeamSpawnLocations = arena.instArenaData0x20.arrayCountFor0x30;
        } break;
        case 'GenesysGenEventList': {
            const evList = parsed.data as CleanKStruct<GenericGenObject.GenesysGenEventList>;
            
            extraInfos.count = evList.arrayCountFor0x10;        
        } break;
        case 'GenesysGenStorePackList': {
            const spList = parsed.data as CleanKStruct<GenericGenObject.GenesysGenStorePackList>;
            
            extraInfos.count = spList.arrayCountFor0x10;
        } break;
        case 'GenesysGenThankYouScreenItem': {
            const item = parsed.data as CleanKStruct<GenericGenObject.GenesysGenThankYouScreenItem>;
            
            extraInfos.messageID = item.message0x14;
        } break;
        case 'GenesysGenEntitlement': {
            const item = parsed.data as CleanKStruct<GenericGenObject.GenesysGenEntitlement>;
            
            extraInfos.name = item.name0x1c.instBuffer0x0;
            extraInfos.description = item.description0xc.instBuffer0x0;
            extraInfos.entitlementTag = item.entitlementTag0x14.instBuffer0x0;
        } break;
        case 'GenesysGenStorePack': {
            const item = parsed.data as CleanKStruct<GenericGenObject.GenesysGenStorePack>;
            
            extraInfos.count = item.arrayCountFor0x18;
        } break;
        case 'GenesysGenNucleusEntitlementTag': {
            const item = parsed.data as CleanKStruct<GenericGenObject.GenesysGenNucleusEntitlementTag>;
            
            extraInfos.tag = item.tag0xc.instBuffer0x0;
        } break;
        case 'GenesysGenNucleusGrantMappingsList': {
            const item = parsed.data as CleanKStruct<GenericGenObject.GenesysGenNucleusGrantMappingsList>;
            
            extraInfos.itemCount = item.arrayCountFor0x10;
        } break;
        case 'GenesysGenPhysicsCrashingRules': {
            const item = parsed.data as CleanKStruct<GenericGenObject.GenesysGenPhysicsCrashingRules>;
            
            extraInfos.GenesysGenPhysicsCrashingRulesImpactRulesCount = item.arrayCountFor0x10;
            extraInfos.GenesysGenPhysicsCrashingRulesImpactRulesCount = item.arrayCountFor0x14;
            extraInfos.GenesysGenPhysicsCrashingRulesImpactRulesCount = item.arrayCountFor0x18;
            extraInfos.GenesysGenPhysicsCrashingRulesImpactRulesCount = item.arrayCountFor0x20;
            extraInfos.LandingRulesCount = item.arrayCountFor0x1c;
            extraInfos.PlayerRulesCount = item.arrayCountFor0x24;
            extraInfos.PropsRulesCount = item.arrayCountFor0x28;
            extraInfos.RoadblockRulesCount = item.arrayCountFor0x2c;
            extraInfos.TrafficRulesCount = item.arrayCountFor0x30;
            extraInfos.WorldRulesCount = item.arrayCountFor0x34;
        } break;
        case 'GenesysGenGameplayRevengeBonus': {
            const item = parsed.data as CleanKStruct<GenericGenObject.GenesysGenGameplayRevengeBonus>;
            
            extraInfos.instFeatureCount = item.arrayCountFor0x2c
            extraInfos.instGenesysGenNitrousParametersCount = item.arrayCountFor0x24
            extraInfos.instGenesysGenPerformanceModifierCount = item.arrayCountFor0x28
        } break;
        case 'GenesysGenCarSelectData': {
            const item = parsed.data as CleanKStruct<GenericGenObject.GenesysGenCarSelectData>;
            
            extraInfos.uimemoryLimit = item.uimemoryLimit0x88;
            extraInfos.uiresourceLimit = item.uiresourceLimit0x8c;
            extraInfos.instCopPlacementsCount = item.arrayCountFor0x7c;
            extraInfos.instRacerPlacementsCount = item.arrayCountFor0x84;
        } break;
        default: {
            extraInfos = undefined;
        }
    }
    newObjData.extraInfos = extraInfos;

    inProgressInfoList.push(newObjData);
    // console.log(parsed.data.constructor.name);

    return;
}

const process_files = async (directory: string, names: string[], resultName: string) => {
    for (const name of names) {
        try {
            await extractBasicInfo(directory, name);
        } catch(e) {
            console.log(e);
            process.exit();
            // localErrors.add(name);
        }
    }

    const out = [];
    for (const info of inProgressInfoList) {
        out.push(`${info.idString} (${info.idValue}): ${info.typeName}`);
        if (info.extraInfos) {
            out.push('more info:');
            out.push(YAMLStringify(info.extraInfos).split('\n').map(v => '  ' + v).join('\n'));
        } else {
            out.push('');
        }
    }

    inProgressInfoList = [];

    await writeFile(__dirname + `/_generated_from_obj_analysis/${resultName}_objects.txt`, out.join('\n'), 'ascii');
}

const main = async () => {
    // THIS IS WHERE YOU PLACE THE PATHS TO THE GenesysType FOLDERS
    // the first part is the path, the 2nd part is what the resulting file will be named
    const pathNameResultPair = [
        ['../all_unpacked/gamemodes', 'gamemodes'],
        ['../all_unpacked/globalresources', 'globalresources'],
        ['../all_unpacked/HL_31208', 'HL_31208'],
        ['../all_unpacked/HSM/UILISTS/20809', 'HSM_UILISTS_20809'],
        ['../all_unpacked/physicsconfig', 'physicsconfig'],
        ['../all_unpacked/traffic', 'traffic'],
        ['../all_unpacked/vehicle_waves', 'vehicle_waves'],
        ['../all_unpacked/VEH_122699_LO', 'VEH_122699_LO'],
        ['../all_unpacked/TRAFFICATTRIBS', 'TRAFFICATTRIBS'],
        ['../all_unpacked/TRK_UNIT1', 'TRK_UNIT1'],
        ['../all_unpacked/easyguide', 'easyguide'],
        ['../all_unpacked/unpacked_vehicles', 'vehicles'],
        ['../all_unpacked/gameplay', 'gameplay']
    ];

    for (const [path, fileName] of pathNameResultPair) {
        const names = readdirSync(__dirname + `/${path}/GenesysObject`)
            .map(n => n.slice(0, n.length - 4));
        
        inProgressInfoList = [];
        await process_files(path, names, fileName);
    }
}

main();
