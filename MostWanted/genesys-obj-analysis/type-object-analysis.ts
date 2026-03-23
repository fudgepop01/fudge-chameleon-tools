import KaitaiStream from 'kaitai-struct/KaitaiStream';
import { readFile, writeFile } from 'fs/promises';
import { GenericGenObject as GenObjBE } from '../ParserStuff-BE/generic-gen-object-BE';
import { GenericGenObject as GenObjLE } from '../ParserStuff-LE/generic-gen-object';
import { readdirSync } from 'fs';
import { stringify as YAMLStringify } from 'yaml';
import { CleanKStruct } from '../helpers/recursiveOmit';
import { evtname_LE } from '../helpers/event_names';
import { carname_LE } from '../helpers/car_names';

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
];

let ROOT_PATH = __dirname + '/';
let BNDL_LIST = [];
let GenericGenObject: typeof GenObjBE | typeof GenObjLE;
let isE3 = false;
if (process.argv[2] === 'E3') {
    isE3 = true;
    ROOT_PATH += E3_PATH;
    BNDL_LIST = E3_BNDLS;
    GenericGenObject = GenObjBE;
} else {
    ROOT_PATH += RETAIL_PATH;
    BNDL_LIST = RETAIL_BNDLS;
    GenericGenObject = GenObjLE;
}


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

    const path = ROOT_PATH + `/${directory}/GenesysObject/${fileName}.dat`;
    const file = await readFile(path);
    const parsed: CleanKStruct<GenObjLE> = new GenericGenObject(new KaitaiStream(file)) as GenObjLE;


    const newObjData: GenesysObjectData = {
        idString: fileName,
        idValue: parseInt('0x' + LEToDecimal(fileName), 16),
        typeName: parsed.data ? parsed.data.constructor.name : 'unknown?'
    };

    let extraInfos: any = {};
    try {

        switch (newObjData.typeName) {
            case 'GenesysObjCollection': {
                const dataCollection = parsed.data as CleanKStruct<GenObjLE.GenesysObjCollection>;
                extraInfos.count = dataCollection.collectionCount;
                const objTypes: Set<string> = new Set();
                // console.log(dataCollection.objCollection);

                if (newObjData.idString === `00_04_60_79`) {
                    console.log(dataCollection);
                    if (1 < 2) process.exit();
                }
    
                for (const [idx, entry] of dataCollection.objCollection.entries()) {
                    objTypes.add((entry.data.data as GenObjLE).data.constructor.name);
                }
                extraInfos.types = Array.from(objTypes);
    
                if (fileName === `AC_1D_10_00`) {
                    extraInfos.copTypes =  [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const ctype = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenGameplayCopType>;
                        const d = {
                            playerType: ctype.aiplayerType0xc,
                            bool0x14: ctype.bool8T0x14,
                            gameChangerId: ctype.gameChangerId0x10,
                            canSpawnBehind: ctype.canSpawnBehind0x15,
                            canSpawnHeadOn: ctype.canSpawnHeadOn0x16,
                            canSpawnIntercepting: ctype.canSpawnIntercepting0x17,
                            bool0x18: ctype.bool8T0x18,
                            bool0x19: ctype.bool8T0x19,
                        };
                        extraInfos.copTypes.push(d);
                    }
                } else if (fileName === `1C_F5_05_00`) {
                    extraInfos.heatLevels = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const heatLevel = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenHeatLevel>;
                        const d = {
                            idx,
                            gameChangerId: heatLevel.gameChangerId0x70,
                            heatLevelNumber: heatLevel.displayNumber0x116
                        };
                        extraInfos.heatLevels.push(d);
                    }
                } else if (fileName === `5B_5D_04_00`) {
                    extraInfos.eventDatas = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const eventType = (entry.data.data as any).data;
                        if (eventType instanceof GenObjLE.GenesysGenOfflineEvent) {
                            if (eventType.ptrArrGameplayTriggers0x7c) {
                                const d = {
                                    idx,
                                    gameMode: toLEHash(eventType.baseObject.gameMode0x1c),
                                    gameChangerId: evtname_LE[eventType.baseObject.gameChangerId0x18] ?? toLEHash(eventType.baseObject.gameChangerId0x18),
                                    triggers: eventType.instGameplayTriggers0x7c.map(toLEHash),
                                    timeline: eventType.instTimeline0xa0?.map(toLEHash),
                                    balancingData: toLEHash(eventType.raceBalancingData0x94),
                                    balancingProfile: toLEHash(eventType.raceBalancingProfile0x98),
    
                                };
                                extraInfos.eventDatas.push(d);
                            }
                        }
                    }
    
                } else if (fileName === `3D_FB_06_00` || fileName === `optional_modded_3D_FB_06_00`) {
                    // gameplay triggers
                    extraInfos.triggerDatas = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const triggerData = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenGameplayTrigger>;
                        const getPredicateData = (p: any) => p.instBuffer0x0.length > 1 ? p.instBuffer0x0 : undefined;  
                        const d = {
                            idx,
                            idhash: toLEHash(triggerData.gameChangerId0x14),
                            predicate: getPredicateData(triggerData.predicate0xc),
                            inputTriggers: triggerData.instInput0x1c?.map(v => v.trigger0xc) ?? [],
                            addToMinimap: triggerData.addToMiniMap0x2a,
                            outputs: triggerData.instOutput0x20?.map(v => ({
                                predicate: getPredicateData(v.predicate0xc),
                                roadblocks: v.instRoadblockInstance0x20?.map(rbi => ({
                                    idhash: toLEHash((rbi.data.data as any).gameChangerId0xc),
                                    placement: (rbi.data.data as any).placement0x10,
                                    type: (rbi.data.data as any).type0x14
                                })),
                                aiplayers: v.instAiplayers0x18?.map(aip => ({
                                    placement: (aip.data.data as CleanKStruct<GenObjLE.GenesysGenGameplayTriggerAiplayerInformation>).placement0xc,
                                    idhash: toLEHash((aip.data.data as CleanKStruct<GenObjLE.GenesysGenGameplayTriggerAiplayerInformation>).instAiplayerInstance0x10.gameChangerId0x10),
                                    type: (aip.data.data as CleanKStruct<GenObjLE.GenesysGenGameplayTriggerAiplayerInformation>).instAiplayerInstance0x10.type0x18,
                                }))
                            }))
                        };
                        extraInfos.triggerDatas.push(d);
                    }
                } else if (fileName === `8E_FA_06_00`) {
                    extraInfos.aiPlayerTypes = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const aiType = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenAiplayerType>;
                        const d = {
                            idx,
                            id: aiType.gameChangerId0x10,
                            rolloutID: aiType.rollout0x14,
                            aggressionType: aiType.aggressionType0xa4,
                            enum0xa8: aiType.unkEnum0xa8,
                            weavingType: aiType.weavingType0xac,
                            behaviour: aiType.behaviour0xa6,
                            allowedToRespawn: aiType.allowedToRespawn0xb0,
                            canRhino: aiType.canRhino0xb1,
                            bool8T0x86: aiType.bool8T0xb6,
                            nitrousUsage: aiType.nitrousUsage0xaa,
                            doUturns: aiType.doUturns0xb2,
                            isAggressor: aiType.isAggressor0xb3,
                            isBlacklist: aiType.isBlacklist0xb4,
                            isCop: aiType.isCop0xb5
                        };
                        extraInfos.aiPlayerTypes.push(d);
                    }
                } else if (fileName === `94_61_04_00`) {
                    extraInfos.rolloutTypes = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const rollout = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenRollout>;
                        const d = {
                            idx,
                            id: rollout.gameChangerId0x38,
                            name: rollout.name0x40,
                            vehicle: carname_LE[rollout.vehicle0x58] ?? rollout.vehicle0x58,
                            colour: rollout.colour0x30,
                            bodyUpgrade: rollout.bodyUpgrade0x24,
                            chassisUpgrade: rollout.chassisUpgrade0x2c,
                            nitrousUpgrade: rollout.nitrousUpgrade0x44,
                            characters: rollout.instCharacters0x28,
                            uniqIdInst: rollout.instCgsCoreUniqueId0x3c,
                            isOnlineRollout: rollout.isOnlineRollout0x6b,
                            isPlayerRollout: rollout.isPlayerRollout0x6c,
                            weaponData: {
                                weaponID: rollout.weaponData0xc.weapon0xc,
                                weaponUpgrades: rollout.weaponData0xc.instWeaponUpgrades0x10,
                            },
                        };
                        extraInfos.rolloutTypes.push(d);
                    }
                }
    
                newObjData.extraInfos = extraInfos;
            } break;
            case 'GenesysGenSequence': {
                const sequences = parsed.data as CleanKStruct<GenObjLE.GenesysGenSequence>;
                sequences.instSequenceItems0x20
                extraInfos.count = sequences.arrayCountFor0x20;
                const objTypes: Set<string> = new Set();
    
                for (const [idx, entry] of sequences.instSequenceItems0x20.entries()) {
                    objTypes.add((entry.data.data as GenObjLE).data.constructor.name);
                }
                extraInfos.sequenceTypes = Array.from(objTypes);
    
            } break;
            case 'GenesysGenEasyGuidePage': {
                const pageInfo = parsed.data as CleanKStruct<GenObjLE.GenesysGenEasyGuidePage>;
                
                extraInfos.text = [];
                for (const [idx, txtID] of pageInfo.instText0x1c.entries()) {
                    extraInfos.text.push(toLEHash(txtID));
                }
            } break;
            case 'GenesysGenRaceBalancingProfile': {
                const profile = parsed.data as CleanKStruct<GenObjLE.GenesysGenRaceBalancingProfile>;
    
                extraInfos.minSpeed = profile.minSpeed0x14;
                extraInfos.maxSpeed = profile.maxSpeed0x10;
                extraInfos.id = profile.gameChangerId0xc;
            } break;
            case 'GenesysGenRaceBalancingData': {
                const data = parsed.data as CleanKStruct<GenObjLE.GenesysGenRaceBalancingData>;
                
                extraInfos.opponentDataCount = data.instOpponentData0x18.length;
                extraInfos.extraScheduleTime = data.extraScheduleTime0x14;
                extraInfos.extraCrashScheduleTime = data.extraCrashScheduleTime0x10;
    
                extraInfos.opponentData = [];
                for (const [idx, entry] of data.instOpponentData0x18.entries()) {
                    const d = {
                        idx,
                        id: entry.gameChangerId0xc,
                        startCutoffRatio: entry.startCutoffRatio0x24,
                        endCutoffRatio: entry.endCutoffRatio0x18,
                        aheadDistance: entry.aheadDistance0x10,
                        behindDistance: entry.behindDistance0x14,
                        startSpeedValueAhead: entry.startSpeedValueAhead0x28,
                        endSpeedValueAhead: entry.endSpeedValueAhead0x1c,
                        startSpeedValueBehind: entry.startSpeedValueBehind0x2c,
                        endSpeedValueBehind: entry.endSpeedValueBehind0x20
                    };
                    extraInfos.opponentData.push(d);
                }
    
            } break;
            case 'GenesysGenOnlineRoute': {
                const route = parsed.data as CleanKStruct<GenObjLE.GenesysGenOnlineRoute>;
    
                extraInfos.checkpointCount = route.instCheckpoints0xc.length;
            } break;
            case 'GenesysGenEventArena': {
                const arena = parsed.data as CleanKStruct<GenObjLE.GenesysGenEventArena>;
                
                extraInfos.numLockdownPoints = arena.instArenaData0x20.arrayCountFor0x14;
                extraInfos.numPointToPointCheckpoints = arena.instArenaData0x20.arrayCountFor0x18;
                extraInfos.numRepairPoints = arena.instArenaData0x20.arrayCountFor0x1c;
                extraInfos.numSpawnLocations = arena.instArenaData0x20.arrayCountFor0x20;
                extraInfos.numChevrons = arena.instArenaData0x20.arrayCountFor0x28;
                extraInfos.numCustomChevronList = arena.instArenaData0x20.arrayCountFor0x2c;
                extraInfos.numTeamSpawnLocations = arena.instArenaData0x20.arrayCountFor0x30;
            } break;
            case 'GenesysGenEventList': {
                const evList = parsed.data as CleanKStruct<GenObjLE.GenesysGenEventList>;
                
                extraInfos.count = evList.arrayCountFor0x10;        
            } break;
            case 'GenesysGenStorePackList': {
                const spList = parsed.data as CleanKStruct<GenObjLE.GenesysGenStorePackList>;
                
                extraInfos.count = spList.arrayCountFor0x10;
            } break;
            case 'GenesysGenThankYouScreenItem': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenThankYouScreenItem>;
                
                extraInfos.messageID = item.message0x14;
            } break;
            case 'GenesysGenEntitlement': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenEntitlement>;
                
                extraInfos.name = item.name0x1c.instBuffer0x0;
                extraInfos.description = item.description0xc.instBuffer0x0;
                extraInfos.entitlementTag = item.entitlementTag0x14.instBuffer0x0;
            } break;
            case 'GenesysGenStorePack': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenStorePack>;
                
                extraInfos.count = item.arrayCountFor0x18;
            } break;
            case 'GenesysGenNucleusEntitlementTag': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenNucleusEntitlementTag>;
                
                extraInfos.tag = item.tag0xc.instBuffer0x0;
            } break;
            case 'GenesysGenNucleusGrantMappingsList': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenNucleusGrantMappingsList>;
                
                extraInfos.itemCount = item.arrayCountFor0x10;
            } break;
            case 'GenesysGenPhysicsCrashingRules': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenPhysicsCrashingRules>;
                
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
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenGameplayRevengeBonus>;
                
                extraInfos.instFeatureCount = item.arrayCountFor0x2c
                extraInfos.instGenesysGenNitrousParametersCount = item.arrayCountFor0x24
                extraInfos.instGenesysGenPerformanceModifierCount = item.arrayCountFor0x28
            } break;
            case 'GenesysGenCarSelectData': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenCarSelectData>;
                
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
    } catch(E) {
        newObjData.extraInfos = undefined;
    }

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

    await writeFile(ROOT_PATH + `/_generated_from_obj_analysis/${resultName}_objects.txt`, out.join('\n'), 'ascii');
}

const main = async () => {
    // THIS IS WHERE YOU PLACE THE PATHS TO THE GenesysType FOLDERS
    // the first part is the path, the 2nd part is what the resulting file will be named
    const pathNameResultPair = BNDL_LIST

    for (const [path, fileName] of pathNameResultPair) {
        const names = readdirSync(ROOT_PATH + `/${path}/GenesysObject`)
            .map(n => n.slice(0, n.length - 4));
        
        inProgressInfoList = [];
        await process_files(path, names, fileName);
    }
}

main();
