import KaitaiStream from 'kaitai-struct/KaitaiStream';
import { readdir, readFile, writeFile } from 'fs/promises';
import { GenericGenObject as GenObjBE } from '../ParserStuff-BE/generic-gen-object-BE';
import { GenericGenObject as GenObjLE } from '../ParserStuff-LE/generic-gen-object';
import { existsSync, readdirSync } from 'fs';
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
    [RETAIL_PATH + '/../all_unpacked/FBG_2090138', 'fbg_2090138'],
    [RETAIL_PATH + '/../all_unpacked/GLOBALCONFIG', 'GLOBALCONFIG'],
];

let ERRORS = "";

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


const ConstructedGCIDMap: {[key: string]: string} = {};
let ExistingGCIDMap: {[key: string]: string} = {};
const addGameChangerId = (num: number, typeName: string) => {
    if (num) {
        const hash = toLEHash(num);
        // if (ConstructedGCIDMap[hash] && ConstructedGCIDMap[hash].length < typeName.length) return undefined;
        if (num != 0) { ConstructedGCIDMap[hash] = typeName; }
        return hash;
    }
    return undefined;
}

const ConstructedUnknownGCIDMap: {[key: string]: Set<string>} = {};
const trackUnknownGCID = (num: number, typeName: string) => {
    if (num) {
        const hash = toLEHash(num);
        if (num != 0) { 
            if (ConstructedUnknownGCIDMap[hash])
                ConstructedUnknownGCIDMap[hash].add(typeName);
            else
                ConstructedUnknownGCIDMap[hash] = new Set([typeName]);
        }
        return hash;
    }
    return undefined;
}

const addUniqId = (number: number) => {
    const hash = toLEHash(number);
    return `{$ID$${hash}}`;
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
const invertEnum = (enumObj: {[key: string]: number}) => {
    return Object.fromEntries(Object.entries(enumObj).map((k, v) => [v, k]));
}

interface GenesysObjectData {
    idString: string;
    idValue: number;
    typeName: string;
    extraInfos?: any;
};
 
const addExtraInfos = (parsed: any, fileName: string, extraInfos: any) => {
    try {

        const traverseAndAdd = (obj: any, path: string, topStructName: string) => {
            for (let k of Object.keys(obj)) {
                if (k.startsWith('_')) 
                        k = k.slice(1);
                    
                if (k.startsWith('gameChangerId')) {
                    addGameChangerId(obj[k], `(${topStructName}) ${obj.constructor.name} ${fileName}${path}`)
                } else if (k.startsWith('cgsCoreUniqueId')) {
                    extraInfos[path + k] = addUniqId(obj[k]);
                } else if (!['_io', '_parent', '_read', '_root', '_is_le'].includes(k)) {
                    if (Array.isArray(obj[k])) {
                        for (const [idx, val] of obj[k].entries()) {
                            traverseAndAdd(val, `${path}/${k}[${idx}]`, topStructName);
                        }
                    }
                    else if (typeof obj[k] === 'object') {
                        traverseAndAdd(obj[k], (k === 'data') ? path : `${path}/${k}`, topStructName);
                    }
                    else if (typeof obj[k] === 'number' && obj[k] > 0x3300 && !k.startsWith("ptr") && !k.startsWith("int") && !k.startsWith("uint") && !k.startsWith("float")) {
                        if (obj.constructor.name === 'GenObj') {
                            trackUnknownGCID(obj[k], `(${topStructName}) ${obj.constructor.name} ${fileName}/${k}`);
                        } else {
                            trackUnknownGCID(obj[k], `(${topStructName}) ${obj.constructor.name} ${fileName}/${k}`);
                        }
                    }
                }
            }
        }
    
        if (parsed?.data) {
            // if (parsed.data.constructor.name === 'GenesysGenVehiclesPerformanceUpgrades') {
            //     try {
            //         const thing = (parsed.data as GenObjLE.GenesysGenVehiclesPerformanceUpgrades);
            //         console.log(Object.getOwnPropertyDescriptors(thing));
            //     } catch {
            //         console.log('ERROR W/: ' + fileName);
            //     }
            //     // console.log(Object.keys(parsed.data));
            //     // const thing = (parsed.data as GenObjLE.GenesysGenVehiclesPerformanceUpgrades);
            //     // console.log(Object.keys(thing['standard0x60']));
            //     // console.log(thing['standard0x60']['_instGenesysGenVehiclesUpgradeBase0x10']);
            //     process.exit();
            // }
    
            for (let k of Object.keys(parsed.data)) {
                if (!['_io', '_parent', '_read', '_root', '_is_le'].includes(k)) {
                    if (k.startsWith('_')) 
                        k = k.slice(1);
                    if (Array.isArray(parsed.data[k])) {
                        for (const [idx, val] of parsed.data[k].entries()) {
                            traverseAndAdd(val, `/${k}[${idx}]`, parsed.data.constructor.name);
                        }
                    }
                    else if (typeof parsed.data[k] === 'object') {
                        traverseAndAdd(parsed.data[k], '/' + k, parsed.data.constructor.name);
                    }
                }
    
                if (k.startsWith('gameChangerId')) {
                    addGameChangerId(parsed.data[k], `${parsed.data.constructor.name} ${fileName}`)
                } else if (k.startsWith('cgsCoreUniqueId')) {
                    extraInfos[k] = addUniqId(parsed.data[k]);
                } 
                else if (typeof parsed.data[k] === 'number' && parsed.data[k] > 0x3300 && !k.startsWith("ptr") && !k.startsWith("int") && !k.startsWith("uint") && !k.startsWith("float")) {
                    if (parsed.data.constructor.name === 'GenObj') {
                        trackUnknownGCID(parsed.data[k], `(${parsed.data.constructor.name}) ${parsed.data.constructor.name} ${fileName}/${k}`);
                    } else {
                        trackUnknownGCID(parsed.data[k], `(${parsed.data.constructor.name}) ${parsed.data.constructor.name} ${fileName}/${k}`);
                    }
                }
            }
        }
    } catch {
        // shrugs
    }
}

let inProgressInfoList: GenesysObjectData[] = [];
const extractBasicInfo = async (directory: string, fileName: string) => {

    const path = ROOT_PATH + `/${directory}/GenesysObject/${fileName}.dat`;
    const file = await readFile(path);
    
    let parsed: CleanKStruct<GenObjLE>;
    parsed = new GenericGenObject(new KaitaiStream(file)) as GenObjLE;

    const newObjData: GenesysObjectData = {
        idString: fileName,
        idValue: parseInt('0x' + LEToDecimal(fileName), 16),
        typeName: parsed.data ? parsed.data.constructor.name : 'unknown?'
    };

    const location = `(${directory.substring(directory.lastIndexOf('/') + 1)}/${fileName})`;
    addGameChangerId(LEToDecimal(fileName), `${newObjData.typeName} ${location}`);

    const extractAIPlayertype = (aiType: CleanKStruct<GenObjLE.GenesysGenAiplayerType>, idx?: number) => {
        const d = {
            idx: idx ?? undefined,
            id: addGameChangerId(aiType.gameChangerId0x10, `AiplayerType` + (idx ? `[${idx}]` : ` ${location}`)),
            rolloutID: addUniqId(aiType.rollout0x14),
            aggressionType: aiType.aggressionType0xa4,
            aggressionFrequency: aiType.aggressionFrequency0x20,
            aggressionDelay: aiType.aggressionDelay0x1c,
            chasingBehaviour: aiType.chasingBehaviour0xa8,
            weavingType: aiType.weavingType0xac,
            behaviour: aiType.behaviour0xa6,
            allowedToRespawn: aiType.allowedToRespawn0xb0,
            canRhino: aiType.canRhino0xb1,
            shortcutTakingPercentage0x68: aiType.shortcutTakingPercentage0x68,
            nitrousUsage: aiType.nitrousUsage0xaa,
            doUturns: aiType.doUturns0xb2,
            isAggressor: aiType.isAggressor0xb3,
            isBlacklist: aiType.isBlacklist0xb4,
            isCop: aiType.isCop0xb5,
            speedMatchingMaxDistance0x74: aiType.speedMatchingMaxDistance0x74,
            speedMatchingMaxSpeed0x78: aiType.speedMatchingMaxSpeed0x78,
            speedMatchingMinSpeed0x80: aiType.speedMatchingMinSpeed0x80,
            speedMatchingSpeedDifference0x84: aiType.speedMatchingSpeedDifference0x84,
            customTakedownAction0xc: addUniqId(aiType.customTakedownAction0xc),
            flatOutInitialTime0x30: aiType.flatOutInitialTime0x30,
            flatOutTime0x34: aiType.flatOutTime0x34,
            speed: aiType.speed0x70
        };        

        for (const k of Object.keys(aiType)) {
            if (k.startsWith('float')) {
                d[k] = aiType[k];
            }
        }


        return d;
    } 


    let extraInfos: any = {};
    try {

        switch (newObjData.typeName) {
            case 'GenesysObjCollection': {
                const dataCollection = parsed.data as CleanKStruct<GenObjLE.GenesysObjCollection>;
                extraInfos.count = dataCollection.collectionCount;
                const objTypes: Set<string> = new Set();
                // console.log(dataCollection.objCollection);
    
                for (const [idx, entry] of dataCollection.objCollection.entries()) {
                    const data = (entry.data.data as GenObjLE).data;
                    objTypes.add(data.constructor.name);
                }
                extraInfos.types = Array.from(objTypes);
    
                if (fileName === `AC_1D_10_00`) {
                    extraInfos.copTypes =  [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const ctype = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenGameplayCopType>;
                        const d = {
                            idx,
                            playerType: addUniqId(ctype.aiplayerType0xc),
                            gameChangerId: addGameChangerId(ctype.gameChangerId0x10, `CopType[${idx}]`),
                            canSpawnAhead: ctype.canSpawnAhead0x14,
                            canSpawnBehind: ctype.canSpawnBehind0x15,
                            canSpawnHeadOn: ctype.canSpawnHeadOn0x16,
                            canSpawnIntercepting: ctype.canSpawnIntercepting0x17,
                            bool0x18: ctype.bool8T0x18,
                            canSpawnWaiting: ctype.canSpawnWaiting0x19,
                        };
                        extraInfos.copTypes.push(d);
                    }
                } else if (fileName === `1C_F5_05_00`) {
                    extraInfos.heatLevels = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const heatLevel = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenHeatLevel>;

                        const coordination = heatLevel.coordination0xc;
                        const cph0xc = coordination.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc;
                        const cph0x30 = coordination.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30;

                        const cph0x30Obj = {
                            float32T0x10: cph0x30.float32T0x10,
                            float32T0x14: cph0x30.float32T0x14,
                            timeInBehaviour0x18: cph0x30.timeInBehaviour0x18,
                            takedownThreshold0x23: cph0x30.takedownThreshold0x23,
                            spawnCops0x22: cph0x30.spawnCops0x22,
                            roadblock: addUniqId(cph0x30.roadblock0xc),
                            copBehaviour: cph0x30.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c?.map(cb => ({
                                behaviour: cb.copBehaviour0x14,
                                uniqueId: addUniqId(cb.cgsCoreUniqueId0xc),
                                maxSpeed: cb.copMaxSpeed0x10,
                                positioning: cb.positioning0x16
                            }))
                        }

                        const cph0xcObj = {
                            float32T0x10: cph0xc.float32T0x10,
                            float32T0x14: cph0xc.float32T0x14,
                            timeInBehaviour0x18: cph0xc.timeInBehaviour0x18,
                            takedownThreshold0x23: cph0xc.takedownThreshold0x23,
                            spawnCops0x22: cph0xc.spawnCops0x22,
                            roadblock: addUniqId(cph0x30.roadblock0xc),
                            copBehaviour: cph0xc.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c?.map(cb => ({
                                behaviour: cb.copBehaviour0x14,
                                uniqueId: addUniqId(cb.cgsCoreUniqueId0xc),
                                maxSpeed: cb.copMaxSpeed0x10,
                                positioning: cb.positioning0x16
                            }))
                        } 

                        let cphInstObj;
                        if (coordination.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x58) {
                            const cphInstArr = coordination.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x58;
                            cphInstObj = cphInstArr.map(cphInst => ({
                                float32T0x10: cphInst.float32T0x10,
                                float32T0x14: cphInst.float32T0x14,
                                timeInBehaviour0x18: cphInst.timeInBehaviour0x18,
                                takedownThreshold0x23: cphInst.takedownThreshold0x23,
                                spawnCops0x22: cphInst.spawnCops0x22,
                                roadblock: addUniqId(cph0x30.roadblock0xc),
                                copBehaviour: cphInst.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c?.map(cb => ({
                                    behaviour: cb.copBehaviour0x14,
                                    uniqueId: addUniqId(cb.cgsCoreUniqueId0xc),
                                    maxSpeed: cb.copMaxSpeed0x10,
                                    positioning: cb.positioning0x16,
                                }))
                            }))
                        }

                        const d = {
                            idx,
                            gameChangerId: addGameChangerId(heatLevel.gameChangerId0x70, `HeatLevel[${idx}]`),
                            heatLevelNumber: heatLevel.displayNumber0x116,
                            allowCooldown: heatLevel.allowCooldown0x110,
                            pursuitRadius: heatLevel.pursuitRadius0xdc,
                            b8_x111: heatLevel.bool8T0x111,
                            forceDisplayNumber0x113: heatLevel.forceDisplayNumber0x113,
                            int16: heatLevel.int16T0x100,
                            coordination: {
                                f0x54: coordination.float32T0x54,
                                pursuitBehavior0xc: cph0xcObj,
                                pursuitBehaviour0x30: cph0x30Obj,
                                additionalPursuitBehaviorArray: cphInstObj
                            },
                            formationAhead: heatLevel.instFormationAhead0xf0,
                            formationBehind: heatLevel.instFormationBehind0xf8,
                            unkFormation: heatLevel.instUint8T0xf4,
                            unkFormation2: heatLevel.instUint8T0xfc,
                            // uknEnum: heatLevel.unkEnum0xec,
                            playerSpeedLimit: heatLevel.playerSpeedLimit0xd8
                        }
                        
                        for (const k of Object.keys(heatLevel)) {
                            if (k.startsWith('float')) {
                                d[k] = heatLevel[k];
                            }
                        }

                        extraInfos.heatLevels.push(d);
                    }
                } else if (fileName === `5B_5D_04_00`) {
                    extraInfos.eventDatas = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const eventType = (entry.data.data as any).data;
                        addGameChangerId(eventType.baseObject.gameChangerId0x18, `${eventType.constructor.name}[${idx}]`);
                        if (eventType instanceof GenObjLE.GenesysGenOfflineEvent) {
                            const d = {
                                idx,
                                gameMode: toLEHash(eventType.baseObject.gameMode0x1c),
                                gameChangerId: evtname_LE[eventType.baseObject.gameChangerId0x18] ?? toLEHash(eventType.baseObject.gameChangerId0x18),
                                triggers: eventType.instGameplayTriggers0x7c?.map(addUniqId),
                                timeline: eventType.instTimeline0xa0?.map(addUniqId),
                                heatLevels: eventType.instDefaultHeatLevels0x6c?.map(addUniqId),
                                balancingData: addUniqId(eventType.raceBalancingData0x94),
                                balancingProfile: addUniqId(eventType.raceBalancingProfile0x98),
                                trafficOverrides: eventType.trafficOverrides0x4c.toString(),
                                introCutsceneId: addUniqId(eventType.eventIntro0x70),
                                uid0x68: addUniqId(eventType.cgsCoreUniqueId0x68),
                                uid0x80: addUniqId(eventType.cgsCoreUniqueId0x80),
                                uid0x90: addUniqId(eventType.cgsCoreUniqueId0x90),
                                timeOfDay0x34: eventType.baseObject.timeOfDay0x34,
                                cycleTimeOfDay0x28: eventType.baseObject.cycleTimeOfDay0x28,
                                finishTimeOfDay0x2c: eventType.baseObject.finishTimeOfDay0x2c,
                                overrideSunDirection0x47: eventType.baseObject.overrideSunDirection0x47,
                                sunDirection0x30: eventType.baseObject.sunDirection0x30,
                                isAlternativeWeather0x44: eventType.baseObject.isAlternativeWeather0x44,
                                checkpointCount: eventType.instCheckpoints0x64?.length,
                                checkpointInfo: eventType.instCheckpointInfo0xc8?.length,
                                aihintsCount: eventType.instAihints0x58?.length,
                                lapsCount: eventType.laps0xf6
                            };

                            extraInfos.eventDatas.push(d);
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
                            idhash: addGameChangerId(triggerData.gameChangerId0x14, `GameplayTrigger[${idx}]`),
                            predicate: getPredicateData(triggerData.predicate0xc),
                            inputTriggers: triggerData.instInput0x1c?.map(v => addUniqId(v.trigger0xc)) ?? [],
                            addToMinimap: triggerData.addToMiniMap0x2a,
                            outputs: triggerData.instOutput0x20?.map(v => ({
                                predicate: getPredicateData(v.predicate0xc),
                                roadblocks: v.instRoadblockInstance0x20?.map((rbi, _idx) => ({
                                    idhash: addUniqId((rbi.data.data as any).gameChangerId0xc),//, `GameplayTrigger[${idx}].roadblocks[${_idx}]`),
                                    placement: (rbi.data.data as any).placement0x10,
                                    type: addUniqId((rbi.data.data as any).type0x14),
                                })),
                                aiplayers: v.instAiplayers0x18?.map((aip, _idx) => ({
                                    placement: (aip.data.data as CleanKStruct<GenObjLE.GenesysGenGameplayTriggerAiplayerInformation>).placement0xc,
                                    idhash: addUniqId((aip.data.data as CleanKStruct<GenObjLE.GenesysGenGameplayTriggerAiplayerInformation>).instAiplayerInstance0x10.gameChangerId0x10),//, `GameplayTrigger[${idx}].aiPlayers[${_idx}]`),
                                    type: addUniqId((aip.data.data as CleanKStruct<GenObjLE.GenesysGenGameplayTriggerAiplayerInformation>).instAiplayerInstance0x10.type0x18),
                                }))
                            }))
                        };
                        extraInfos.triggerDatas.push(d);
                    }
                } else if (fileName === `8E_FA_06_00`) {
                    extraInfos.aiPlayerTypes = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const aiType = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenAiplayerType>;
                        extraInfos.aiPlayerTypes.push(extractAIPlayertype(aiType, idx));
                    }
                } else if (fileName === `94_61_04_00`) {
                    extraInfos.rolloutTypes = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const rollout = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenRollout>;
                        const d = {
                            idx,
                            id: addGameChangerId(rollout.gameChangerId0x38, `Rollout[${idx}]`),
                            name: addUniqId(rollout.name0x40),
                            vehicle: carname_LE[rollout.vehicle0x58] ?? rollout.vehicle0x58,
                            colour: addUniqId(rollout.colour0x30),
                            bodyUpgrade: addUniqId(rollout.bodyUpgrade0x24),
                            chassisUpgrade: addUniqId(rollout.chassisUpgrade0x2c),
                            nitrousUpgrade: addUniqId(rollout.nitrousUpgrade0x44),
                            characters: rollout.instCharacters0x28?.map(addUniqId),
                            uniqIdInst: rollout.instCgsCoreUniqueId0x3c?.map(addUniqId),
                            isOnlineRollout: rollout.isOnlineRollout0x6b,
                            isPlayerRollout: rollout.isPlayerRollout0x6c,
                            weaponData: {
                                weaponID: addUniqId(rollout.weaponData0xc.weapon0xc),
                                weaponUpgrades: rollout.weaponData0xc.instWeaponUpgrades0x10?.map(addUniqId),
                            },
                        };
                        extraInfos.rolloutTypes.push(d);
                    }
                } else if (fileName === `C1_37_09_00`) {
                    extraInfos.roadblockDefs = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const roadblock = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenRoadBlockDefinition>;
                        const d = {
                            idx,
                            id: addGameChangerId(roadblock.gameChangerId0x14, `RoadblockDefinition[${idx}]`),
                            primaryLayer: addUniqId(roadblock.primaryLayer0x1c),
                            frontLayers: roadblock.instFrontLayers0x10?.map(addUniqId),
                            backLayers: roadblock.instBackLayers0xc?.map(addUniqId),
                            sequence: addUniqId(roadblock.sequence0x20),
                            layerDistance: roadblock.layerDistance0x24,
                            unkUniqIDs: roadblock.instCgsCoreUniqueId0x18?.map(addUniqId),
                        };
                        extraInfos.roadblockDefs.push(d);
                    }
                } else if (fileName === `C2_37_09_00`) {
                    extraInfos.roadblockLayers = [];
                    for (const [idx, entry] of dataCollection.objCollection.entries()) {
                        const layer = (entry.data.data as any).data as CleanKStruct<GenObjLE.GenesysGenRoadBlockLayer>;
                        
                        if (layer.middleItem0xc.gameChangerId0xc !== 0) {
                            addGameChangerId(layer.middleItem0xc.gameChangerId0xc, `RoadblockLayer[${idx}].middleItem`)
                        }
                        if (layer.instLeftItems0x30) 
                            for (const [_idx, it] of layer.instLeftItems0x30?.entries()) {
                                if (it.gameChangerId0xc !== 0) {
                                    addGameChangerId(it.gameChangerId0xc, `RoadblockLayer[${idx}].leftItems[${_idx}]`)
                                }
                            }
                        if (layer.instRightItems0x34) 
                            for (const [_idx, it] of layer.instRightItems0x34.entries()) {
                                if (it.gameChangerId0xc !== 0) {
                                    addGameChangerId(it.gameChangerId0xc, `RoadblockLayer[${idx}].rightItems[${_idx}]`)
                                }
                            }
                        
                        const d = {
                            idx,
                            id: addGameChangerId(layer.gameChangerId0x24, `RoadblockLayer[${idx}]`),
                            distance: layer.distance0x28,
                            firstDistance: layer.firstDistance0x2c,
                            middleItem: {
                                angle: layer.middleItem0xc.angle0x14,
                                id: toLEHash(layer.middleItem0xc.gameChangerId0xc),
                                uniqID: addUniqId(layer.middleItem0xc.roadBlockObject0x10)
                            },
                            leftItems: layer.instLeftItems0x30?.map(it => ({
                                angle: it.angle0x14,
                                id: toLEHash(it.gameChangerId0xc),
                                uniqID: addUniqId(it.roadBlockObject0x10)
                            })),
                            rightItems: layer.instRightItems0x34?.map(it => ({
                                angle: it.angle0x14,
                                id: toLEHash(it.gameChangerId0xc),
                                uniqID: addUniqId(it.roadBlockObject0x10)
                            }))                            
                        };
                        extraInfos.roadblockLayers.push(d);
                    }
                }

                newObjData.extraInfos = extraInfos;
            } break;
            case 'GenesysGenSequence': {
                const sequences = parsed.data as CleanKStruct<GenObjLE.GenesysGenSequence>;
                sequences.instSequenceItems0x20
                extraInfos.count = sequences.arrayCountFor0x20;
                const objTypes: Set<string> = new Set();
    
                addGameChangerId(sequences.gameChangerId0x14, `Sequence (${fileName})`)

                for (const [idx, entry] of sequences.instSequenceItems0x20.entries()) {
                    const data = (entry.data.data as GenObjLE).data;
                    objTypes.add(data.constructor.name);

                    if (data instanceof GenObjLE.GenesysGenSpawnAicopCar) {
                        if (!extraInfos.aiCopSpawns) extraInfos.aiCopSpawns = [];

                        const d = {
                            idx,
                            bool8T0x7a: data.bool8T0x7a,
                            directionBinding0x50: data.directionBinding0x50.instBuffer0x0,
                            positionBinding0x58: data.positionBinding0x58.instBuffer0x0,
                            spawnWithName0x60: data.spawnWithName0x60.instBuffer0x0,
                            aiPlayerType: addUniqId(data.aiPlayerType0x68),
                            spawnTrigger0x6c: addUniqId(data.spawnTrigger0x6c),
                            float32T0x70: data.float32T0x70,
                            position0x40: data.position0x40.arrInlineElements0x0,
                            directionx30: data.direction0x30.arrInlineElements0x0,
                            instAiplayerInstance0x74: {
                                type: addUniqId(data.instAiplayerInstance0x74.type0x18),
                                primaryColour0x14: addUniqId(data.instAiplayerInstance0x74.primaryColour0x14),
                                backUpColour0xc: addUniqId(data.instAiplayerInstance0x74.backUpColour0xc),
                                gameChangerId0x10: addUniqId(data.instAiplayerInstance0x74.gameChangerId0x10)//, `SpawnAicopCar (${fileName})[${idx}]`)
                            },
                        }
                        extraInfos.aiCopSpawns.push(d);
                    } else if (data instanceof GenObjLE.GenesysGenGameplaySequenceItem) {
                        if (!extraInfos.gameplaySequenceItems) extraInfos.gameplaySequenceItems = [];
                        
                        const d = {
                            idx,
                            triggerType: `(${data.triggerType0x28}) ` + (GenObjLE.ECeFb0600[data.triggerType0x28]),
                            data: addUniqId(data.data0x24)
                        }

                        extraInfos.gameplaySequenceItems.push(d);
                    }

                }
                extraInfos.sequenceTypes = Array.from(objTypes);
    
            } break;
            case 'GenesysGenAiplayerType': {
                const playerType = parsed.data as CleanKStruct<GenObjLE.GenesysGenAiplayerType>;
                
                extraInfos = extractAIPlayertype(playerType);
            } break;
            case 'GenesysGenEasyGuidePage': {
                const pageInfo = parsed.data as CleanKStruct<GenObjLE.GenesysGenEasyGuidePage>;
                
                addGameChangerId(pageInfo.gameChangerId0xc, `EasyGuidePage (${fileName})`)

                extraInfos.nextPage = addUniqId(pageInfo.nextPage0x10);
                extraInfos.referencedPages = pageInfo.instReferencedPages0x14?.map(addUniqId);

                extraInfos.text = [];
                for (const [idx, txtID] of pageInfo.instText0x1c.entries()) {
                    extraInfos.text.push(toLEHash(txtID));
                }
            } break;
            case 'GenesysGenRaceBalancingProfile': {
                const profile = parsed.data as CleanKStruct<GenObjLE.GenesysGenRaceBalancingProfile>;
    
                addGameChangerId(profile.gameChangerId0xc, `RaceBalancingProfile (${fileName})`)

                extraInfos.minSpeed = profile.minSpeed0x14;
                extraInfos.maxSpeed = profile.maxSpeed0x10;
                extraInfos.id = profile.gameChangerId0xc;
            } break;
            case 'GenesysGenRaceBalancingData': {
                const data = parsed.data as CleanKStruct<GenObjLE.GenesysGenRaceBalancingData>;
                
                addGameChangerId(data.gameChangerId0xc, `RaceBalancingData (${fileName})`)
                for (const [idx, dat] of data.instOpponentData0x18.entries()) {
                    if (dat.gameChangerId0xc !== 0) {
                        addGameChangerId(dat.gameChangerId0xc, `RaceBalancingData (${fileName}) data[${idx}]`)
                    }
                }

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
    
                addGameChangerId(route.gameChangerId0x10, `OnlineRoute (${fileName})`)

                extraInfos.checkpointCount = route.instCheckpoints0xc.length;
            } break;
            case 'GenesysGenEventArena': {
                const arena = parsed.data as CleanKStruct<GenObjLE.GenesysGenEventArena>;
                
                addGameChangerId(arena.gameChangerId0xc, `EventArena (${fileName})`)

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
                
                addGameChangerId(evList.gameChangerId0xc, `EventList (${fileName})`)

                extraInfos.count = evList.arrayCountFor0x10;        
            } break;
            case 'GenesysGenStorePackList': {
                const spList = parsed.data as CleanKStruct<GenObjLE.GenesysGenStorePackList>;
                
                addGameChangerId(spList.gameChangerId0xc, `StorePackList (${fileName})`)

                extraInfos.count = spList.arrayCountFor0x10;
            } break;
            case 'GenesysGenThankYouScreenItem': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenThankYouScreenItem>;
                
                addGameChangerId(item.gameChangerId0xc, `ThankYouScreenItem (${fileName})`)

                extraInfos.messageID = addUniqId(item.message0x14);
            } break;
            case 'GenesysGenEntitlement': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenEntitlement>;
                
                addGameChangerId(item.gameChangerId0x24, `Entitlement (${fileName})`)

                extraInfos.name = item.name0x1c.instBuffer0x0;
                extraInfos.description = item.description0xc.instBuffer0x0;
                extraInfos.entitlementTag = item.entitlementTag0x14.instBuffer0x0;
            } break;
            case 'GenesysGenStorePack': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenStorePack>;
                
                addGameChangerId(item.gameChangerId0x14, `StorePack (${fileName})`)

                extraInfos.count = item.arrayCountFor0x18;
            } break;
            case 'GenesysGenNucleusEntitlementTag': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenNucleusEntitlementTag>;
                
                addGameChangerId(item.gameChangerId0x14, `NucleusEntitlementTag (${fileName})`)

                extraInfos.tag = item.tag0xc.instBuffer0x0;
            } break;
            case 'GenesysGenNucleusGrantMappingsList': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenNucleusGrantMappingsList>;
                
                addGameChangerId(item.gameChangerId0xc, `NucleusGrantMappingsList (${fileName})`)
                
                extraInfos.itemCount = item.arrayCountFor0x10;
            } break;
            case 'GenesysGenPhysicsCrashingRules': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenPhysicsCrashingRules>;
                
                addGameChangerId(item.gameChangerId0xc, `CrashingRules (${fileName})`)

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
                
                addGameChangerId(item.gameChangerId0x14, `RevengeBonus (${fileName})`)

                extraInfos.instFeatureCount = item.arrayCountFor0x2c
                extraInfos.instGenesysGenNitrousParametersCount = item.arrayCountFor0x24
                extraInfos.instGenesysGenPerformanceModifierCount = item.arrayCountFor0x28
            } break;
            case 'GenesysGenCarSelectData': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenCarSelectData>;
                
                addGameChangerId(item.gameChangerId0x80, `CarSelectData (${fileName})`)

                extraInfos.uimemoryLimit = item.uimemoryLimit0x88;
                extraInfos.uiresourceLimit = item.uiresourceLimit0x8c;
                extraInfos.instCopPlacementsCount = item.arrayCountFor0x7c;
                extraInfos.instRacerPlacementsCount = item.arrayCountFor0x84;
            } break;
            case 'GenesysGenRaceCarPhysicalDefinitionPhysicalDefinition': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenRaceCarPhysicalDefinition>;
                
                addGameChangerId(item.gameChangerId0xc, `RaceCarPhysicalDefinition (${fileName})`)
                extraInfos = undefined;
            } break;
            case 'GenesysGenGameLogicConfig': {
                const item = parsed.data as CleanKStruct<GenObjLE.GenesysGenGameLogicConfig>;
                
                // extraInfos.blacklistDataList = addUniqId(item.blacklistDataList0x84);
                extraInfos.defaultRespawnSpeed0x220 = item.defaultRespawnSpeed0x220
                extraInfos.defaultRespawnSpeedScalar0x224 = item.defaultRespawnSpeedScalar0x224
                // extraInfos.allowedVehicleList0x5c = addUniqId(item.allowedVehicleList0x5c)
                // extraInfos.defaultRollout0xa4 = addUniqId(item.defaultRollout0xa4)
                // extraInfos.driftAnglePower0x228 = item.driftAnglePower0x228
                // extraInfos.driftGameMode0xb0 = addUniqId(item.driftGameMode0xb0)
                extraInfos.eventStartRadius0x244 = item.eventStartRadius0x244
                // extraInfos.freedriveGameMode0xd8 = addUniqId(item.freedriveGameMode0xd8)
                // extraInfos.gameplayCopType0xf0 = addUniqId(item.gameplayCopType0xf0)
                // extraInfos.instChangeCarList0x94 = item.instChangeCarList0x94.map(addUniqId)
                // extraInfos.introEvent0xfc = addUniqId(item.introEvent0xfc)
                // extraInfos.introRaceEvent0x100 = addUniqId(item.introRaceEvent0x100)
                // extraInfos.raceGameMode0x170 = addUniqId(item.raceGameMode0x170)
                extraInfos.raceRespawnSpeed0x268 = item.raceRespawnSpeed0x268
                extraInfos.raceRespawnSpeedScalar0x26c = item.raceRespawnSpeedScalar0x26c
                // extraInfos.roadblockDefinitionList0x1ac = addUniqId(item.roadblockDefinitionList0x1ac)
                // extraInfos.roadblockLayerList0x1b0 = addUniqId(item.roadblockLayerList0x1b0)
                // extraInfos.rolloutBodyStock0x1b8 = addUniqId(item.rolloutBodyStock0x1b8)
                // extraInfos.rolloutChassis0x1bc = addUniqId(item.rolloutChassis0x1bc)
                // extraInfos.rolloutChassisStock0x1c0 = addUniqId(item.rolloutChassisStock0x1c0)
                // extraInfos.rolloutEngineStock0x1c4 = addUniqId(item.rolloutEngineStock0x1c4)
                // extraInfos.rolloutNitrous0x1cc = addUniqId(item.rolloutNitrous0x1cc)
                // extraInfos.rolloutNitrousStock0x1d0 = addUniqId(item.rolloutNitrousStock0x1d0)
                // extraInfos.defaultRollout0xa4 = addUniqId(item.defaultRollout0xa4)
                extraInfos.staticBustDistance0x288 = item.staticBustDistance0x288
                extraInfos.staticBustSpeed0x28c = item.staticBustSpeed0x28c
                extraInfos.staticBustTimer0x290 = item.staticBustTimer0x290
                for (const k of Object.keys(item)) {
                    if (k.startsWith('float')) {
                        extraInfos[k] = item[k];
                    }
                }
                extraInfos.uint32T0x2c8 = item.uint32T0x2c8;
                extraInfos.uint16T0x2d4 = item.uint16T0x2d4;
                extraInfos.defaultHeatLevels = item.instDefaultHeatLevels0xa0.map(addUniqId);
                
                addExtraInfos(parsed, fileName, extraInfos);
            } break;
            default: {
                extraInfos = {};
            }
        }

        addExtraInfos(parsed, fileName, extraInfos);

        if (extraInfos && Object.keys(extraInfos).length === 0) {
            extraInfos = undefined;
        }

        newObjData.extraInfos = extraInfos;
    } catch(E) {
        ERRORS += `ERROR: ${E.name}, ${newObjData.typeName} -- ${directory} -- ${fileName}\n`
        // console.log("ERROR: ", directory, fileName)
        newObjData.extraInfos = undefined;
        // console.log(E)
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
            ERRORS += `ERROR PARSING: ${e.name} -- ${directory} -- ${name}\n`;
            // console.log(`ERROR PARSING: ${e.name}`, directory, name);
            // console.log(e);
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

    const content = out.join('\n')
        .replace(/\{\$ID\$([0-9A-F_]+)\}/g, (fullMatch, p1) => {
            if (ExistingGCIDMap[p1]) {
                return `(${p1}): ${ExistingGCIDMap[p1]}`;
            }
            return p1;
        });

    inProgressInfoList = [];

    await writeFile(ROOT_PATH + `/_generated_from_obj_analysis/${resultName}_objects.txt`, content, 'ascii');
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


    if (existsSync(ROOT_PATH + `/_generated_from_obj_analysis/GCIDList.txt`)) {
        ExistingGCIDMap = JSON.parse(await readFile(ROOT_PATH + `/_generated_from_obj_analysis/GCIDList.txt`, 'ascii'));
    }

    for (const [idx, [path, fileName]] of pathNameResultPair.entries()) {
        const names = readdirSync(ROOT_PATH + `/${path}/GenesysObject`)
            .map(n => n.slice(0, n.length - 4));

        inProgressInfoList = [];
        console.log(`${idx} / ${pathNameResultPair.length}: ${fileName}`);
        await process_files(path, names, fileName);
    }

    const ConstructedUnknownGCIDMapPost = {};
    for (const [k, v] of Object.entries(ConstructedUnknownGCIDMap)) {
        ConstructedUnknownGCIDMapPost[k] = Array.from(v);
    }
    await writeFile(ROOT_PATH + `/_generated_from_obj_analysis/GCIDList.txt`, JSON.stringify(ConstructedGCIDMap, null, 2), 'ascii');
    await writeFile(ROOT_PATH + `/_generated_from_obj_analysis/GCIDUnknownList.txt`, JSON.stringify(ConstructedUnknownGCIDMapPost, null, 2), 'ascii');
    await writeFile(ROOT_PATH + `/_generated_from_obj_analysis/_ERRORS_LIST.txt`, ERRORS, 'ascii');
}

main();
