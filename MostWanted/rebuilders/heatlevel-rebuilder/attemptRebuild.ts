import { readFile, writeFile } from "fs/promises";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import KaitaiStream from "kaitai-struct/KaitaiStream"
import { BUILD_FILE } from "./_heatLevel";
import { CleanKStruct } from "../../helpers/recursiveOmit";
import { Endianness } from "../../helpers/rebuilderAddins";
import { Endian } from "construct-js";

// ts-node attemptRebuild.ts && mv ./1C_F5_05_00/1C_F5_05_00.dat ../../../all_unpacked/gameplay/GenesysObject && py ../../../bundle_packer_unpacker.py --pack MW ../../../all_unpacked/gameplay/IDs_gameplay.json ../../../_repacked GAMEPLAY.BNDL
const ParseHeatLevelsFile = async () => {
    const res = (await readFile(__dirname + '/1C_F5_05_00/original.dat'));
    const events = new GenObj(new KaitaiStream(res)).data as GenObj.GenesysObjCollection;
    return events;
}

const WriteHeatLevelsFile = async (EventData: GenObj.GenesysObjCollection) => {
    await writeFile(__dirname + '/1C_F5_05_00/1C_F5_05_00.dat', BUILD_FILE(EventData));
}

// const randBehaviours = [0, 2, 3, 4, 6, 7, 8, 9, 1, 11, 12, 13, 15] // crashes?
// Chasing, Blocking, Bruising, Rhino, ?, Idle, Default
// const randBehaviours = [0, 1, 2, 3, 4, 5, 6];
const BEHAVIOURS = {
    chasing: 0,
    blocking: 1,
    bruising: 2,
    rhino: 3,
    intercepting: 4,
    idle: 5,
    default: 6
}
const randBehaviours = [
    BEHAVIOURS.chasing, 
    // BEHAVIOURS.bruising, 
    BEHAVIOURS.rhino,
    // BEHAVIOURS.intercepting,
    BEHAVIOURS.default
];
const copTypes = [
    0x00_19_45_09,
    0x00_19_45_0A,
    0x00_19_45_0B,
    0x00_19_45_0E,
    0x00_19_45_0F,
    0x00_19_45_11,
    0x00_19_45_14,
    0x00_19_45_17,
    0x00_19_45_18,
    0x00_19_45_1A,
    0x00_19_45_1B,
    0x00_19_46_2B,
    0x00_19_46_2C,
    0x00_19_46_2F,
    0x00_19_46_3D,
    0x00_19_46_3E,
    0x00_19_46_3F,
    0x00_19_46_40,
    0x00_19_46_41,
    0x00_19_46_42,
    0x00_19_46_43,
    0x00_19_F1_81,
    0x00_1C_8F_2D,
    0x00_1C_8F_41,
    0x00_21_6E_D5,
]

// wild cops
// const copTypes = [0x00_19_45_17, 0x00_19_45_1B, 0x00_19_46_3E, 0x00_19_46_40, 0x00_19_46_41, 0x00_19_46_42]

// positioning?
// 0 (behind), 1 (closer behind)
const main = async () => {
    const parsed = await ParseHeatLevelsFile();

    const basicCop: CleanKStruct<GenObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour> = {
        baseObject: {
            dynamicGamedata: new Uint8Array(8),
            muTypeVersion: 0x02_1B_2E_66
        },
        cgsCoreUniqueId0xc: 0,
        positioning0x16: 0,
        copMaxSpeed0x10: 300,
        copBehaviour0x14: 0
    } as any;

    const randomizeCop = (cb: any, heatLevel: number, forceCopIdx?: number) => {
        cb.copMaxSpeed0x10 = 300;
        if (forceCopIdx != undefined && forceCopIdx < copTypes.length) {
            cb.cgsCoreUniqueId0xc = copTypes[forceCopIdx];
        } else {
            cb.cgsCoreUniqueId0xc = copTypes[Math.floor(Math.random() * copTypes.length)];
        }
        cb.copBehaviour0x14 = (heatLevel === 0) ? (Math.random() < 0.5 ? BEHAVIOURS.idle : BEHAVIOURS.default) : randBehaviours[Math.floor(Math.random() * randBehaviours.length)];
    }

    const makeNewCops = (copArray: any[], heatLevelNumber: number, idx?: number) => {
        if (copArray) {
            while (copArray.length < 10) {
                const newCop = structuredClone(basicCop);
                randomizeCop(newCop, heatLevelNumber, idx);
                newCop.positioning0x16 = Math.floor(Math.random() * 6) - 3;
                copArray.push(newCop);
            }
        }
    }

    // const makeNewCops = (copArray: any[], heatLevelNumber: number, idx?: number) => {
    //     if (copArray) {
    //         while (copArray.length < 10) {
    //             const newCop = structuredClone(basicCop);
    //             randomizeCop(newCop, heatLevelNumber, idx);
    //             copArray.push(newCop);
    //         }
    //     }
    // }

    // wildest cop types
    /**
     * 7: rhino bullet hell / 0x00_19_45_17,
     * 10: wave of tier 1 cops / 0x00_19_45_1B
     * 15: wave of tier 2 cops / 0x00_19_46_3E
     * 17: tier 1 cops (WITH SPIKES) / 0x00_19_46_40
     * 18: rhino hell (again) - intercepting + heat-on / 0x00_19_46_41
     * 19: more corvettes (can spawn behind) / 0x00_19_46_42
     */
    for (const [idx, heatLevel] of parsed.objCollection.map(v => (v.data.data as GenObj).data as CleanKStruct<GenObj.GenesysGenHeatLevel>).entries()) {
        // let copIdx = idx;
        // if (idx > 0) copIdx -= 1;
        // if (idx === 9) copIdx -= 3;
        // copIdx = copIdx % copTypes.length;
        if (idx === 0) {
            heatLevel.playerSpeedLimit0xd8 = 200;
        }
        let copIdx = undefined;

        heatLevel['_instFormationAhead0xf0'] = [];
        heatLevel['_instFormationBehind0xf8'] = [];
        heatLevel['_instUint8T0xf4'] = [];

        // if (heatLevel.instFormationAhead0xf0) {
        //     heatLevel.instFormationAhead0xf0.length = 0;
        //     heatLevel.instFormationAhead0xf0.push(0);
        //     // heatLevel.instFormationAhead0xf0.push(0);
        //     // heatLevel.instFormationAhead0xf0.push(1);
        //     heatLevel.instFormationAhead0xf0.push(1);
        // }
        // if (heatLevel.instFormationBehind0xf8) {
        //     heatLevel.instFormationBehind0xf8.length = 0;
        //     heatLevel.instFormationBehind0xf8.push(0);
        //     // heatLevel.instFormationBehind0xf8.push(0);
        //     // heatLevel.instFormationBehind0xf8.push(1);
        //     heatLevel.instFormationBehind0xf8.push(1);
        // }

        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.timeInBehaviour0x18 = 30;
        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.spawnCops0x22 = 0;
        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.timeInBehaviour0x18 = 70;
        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.spawnCops0x22 = 1;

        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.takedownThreshold0x23 = 20;
        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.takedownThreshold0x23 = 20;

        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.float32T0x10 = 3000;
        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.float32T0x14 = -1;
        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.float32T0x10 = 3000;
        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.float32T0x14 = -1;

        heatLevel.coordination0xc.float32T0x54 = 80;
        
        const heatLevelNumber = heatLevel.displayNumber0x116;
        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c?.forEach((v) => randomizeCop(v, heatLevelNumber, copIdx));
        heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c?.forEach((v) => randomizeCop(v, heatLevelNumber, copIdx));
        heatLevel.coordination0xc.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x58?.forEach((val, _idx) => {
            val.float32T0x10 = 3000;
            val.float32T0x14 = -1;
            val.takedownThreshold0x23 = 20;

            val.spawnCops0x22 = 1;
            val.timeInBehaviour0x18 = 30;
            val.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c
                .forEach((v) => randomizeCop(v, heatLevelNumber, copIdx))
        });

        if (idx < 10) {
            // heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.arrayCountFor0x1c = 1;              
            makeNewCops(heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c, heatLevelNumber, copIdx);
            // heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.arrayCountFor0x1c = 1;
            makeNewCops(heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c, heatLevelNumber, copIdx);
            heatLevel.coordination0xc.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x58?.forEach(element => {
                makeNewCops(element.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c, heatLevelNumber, copIdx);                
            });
        }

        if (idx === 33) {
            heatLevel.int16T0x100 = -1;
            
            heatLevel.float32T0xac = 100;
            heatLevel.float32T0xb4 = 300;
            heatLevel.float32T0xbc = 2;
            heatLevel.float32T0xc0 = 10;
            heatLevel.float32T0xe4 = 10;
            heatLevel.float32T0xe8 = 20;

            let copArr = [];
            let cops: {behavior: number, type: number}[] = [
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 0 // crown vic
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 0 // crown vic
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 0 // crown vic
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 17 // crown vic with spikes
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 18 // rhino
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 18 // rhino
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 8 // Z06 +spikes
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 8 // Z06 +spikes
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 16 // dodge charger SRT8
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 16 // dodge charger SRT8
                },
            ]
            for (const cop of cops) {
                let newCop = structuredClone(basicCop);
                newCop.cgsCoreUniqueId0xc = copTypes[cop.type];
                newCop.copBehaviour0x14 = cop.behavior;
                copArr.push(newCop)
            }
            heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.ptrArrGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c = 1;
            heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc['_instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c'] = copArr;
            
            let beh = heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc;
            beh.spawnCops0x22 = 1;
            beh.takedownThreshold0x23 = 20;
            beh.timeInBehaviour0x18 = 60;
            // makeNewCops(heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c, heatLevelNumber, copIdx);

            copArr = [];
            cops = [
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 22 // SWAT
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 22 // SWAT
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 22 // SWAT
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 19 // z06 with spikes
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 18 // rhino
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 18 // rhino
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 22 // SWAT
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 8 // Z06 +spikes
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 18 // rhino
                },
                {
                    behavior: BEHAVIOURS.rhino,
                    type: 18 // rhino
                },
            ]
            for (const cop of cops) {
                let newCop = structuredClone(basicCop);
                newCop.cgsCoreUniqueId0xc = copTypes[cop.type];
                newCop.copBehaviour0x14 = cop.behavior;
                copArr.push(newCop)
            }
            heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.ptrArrGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c = 1;
            heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30['_instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c'] = copArr;
            beh = heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30;
            beh.spawnCops0x22 = 1;
            beh.takedownThreshold0x23 = 20;
            beh.timeInBehaviour0x18 = 60;

            // makeNewCops(heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c, heatLevelNumber, copIdx);
            heatLevel.coordination0xc.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x58?.forEach(element => {
                makeNewCops(element.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c, heatLevelNumber, copIdx);                
            });

            console.log("heat 33 cop count:");
            console.log(heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c.length);
            console.log(heatLevel.coordination0xc.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c.length);
        }
        
        heatLevel.chaseSpawnRadius0x80 = Math.min(heatLevel.chaseSpawnRadius0x80, 200);
        heatLevel.pursuitRadius0xdc = 100 + 20 * heatLevel.displayNumber0x116;
        heatLevel.copSightRangeWhenChasing0xa4 = 150 + 35 * heatLevel.displayNumber0x116;
        heatLevel.copSightRangeWhenAlert0xa0 = 200;
        heatLevel.chaseCullRadius0x7c = 350;
        // threshold to advance to next level
        // heatLevel.int16T0x100

        // culling stuff?
        // heatLevel.float32T0xac = 0;
        // heatLevel.float32T0xb4 = 0;

        // heatLevel.float32T0xc0 = 100;
        // heatLevel.float32T0xe4 = 100;
        // heatLevel.float32T0xe8 = 100;
    }

    // Endianness.primary = Endian.Big;
    // Endianness.secondary = Endian.Little;

    await WriteHeatLevelsFile(parsed);
    console.log("written successfully...");
}

main();