import { readFile, writeFile } from "fs/promises";
import { Event as GameEvents } from "./parse-event";
import KaitaiStream from "kaitai-struct/KaitaiStream"
import { BUILD_event_file } from "./build-event";

// ts-node attemptRebuild.ts && mv ./5B_5D_04_00/5B_5D_04_00.dat ../../all_unpacked/gamemodes/GenesysObject && py ../../bundle_packer_unpacker.py --pack MW ../../all_unpacked/gamemodes/IDs.BIN ../../_repacked GAMEMODES.BNDL
const ParseEventsFile = async () => {
    const res = (await readFile(__dirname + '/5B_5D_04_00/original.dat'));
    const events = new GameEvents(new KaitaiStream(res));
    return events;
}

const WriteEventsFile = async (EventData: GameEvents) => {
    await writeFile(__dirname + '/5B_5D_04_00/5B_5D_04_00.dat', BUILD_event_file(EventData));
}

const main = async () => {
    const parsed = await ParseEventsFile();


    for (const [idx, switcher] of parsed.allEvents.map(v => (v.data.data as GameEvents.EventSwitcher)).entries()) {
        if (switcher.offlineEvent) {
            const offlineEvent = switcher.offlineEvent;

            switch (offlineEvent.baseObject.gameMode0x1c) {
                case 0x51282100:
                case 0x01F40500:
                case 0xD0B82100:
                case 0x1ECF1700:
                case 0x1E330400:
                    continue;
            }

            offlineEvent.baseObject.chevronList0x3c = 0;
            offlineEvent.chevronPtrPtrTable0xb4 = 0;
            offlineEvent.customChevronPtrPtrTable0xb8 = 0;

            offlineEvent.nitrousAllowed0xec = 0;
            offlineEvent.copSpawning0xe8 = 1;
            offlineEvent.trafficEnabled0xf0 = 1;
            offlineEvent.trafficDensity0xb0 = 2;
            offlineEvent.weaponsAllowed0xf2 = 1;
            offlineEvent.noRacingLineTraffic0xed = 0;

            // force cops
            // offlineEvent.defaultHeatLevelsPtr0x6c = 1;
            // offlineEvent.defaultHeatLevels0x6c.length = 0;
            // offlineEvent.defaultHeatLevels0x6c.push(1700216);

            // perma-night
            offlineEvent.baseObject.timeOfDay0x34 = 1;
            offlineEvent.baseObject.cycleTimeOfDay0x28 = Math.floor(Math.random() * 8);
            offlineEvent.baseObject.finishTimeOfDay0x2c = Math.floor(Math.random() * 8);
            offlineEvent.baseObject.overrideSunDirection0x47 = 1;
            offlineEvent.baseObject.sunDirection0x30 = 360 - (Math.random() * 360 * 2);

            offlineEvent.baseObject.isAlternativeWeather0x44 = (Math.random() > 0.5) ? 1 : 0;
            offlineEvent.baseObject.isRainActive0x45 = (Math.random() > 0.5) ? 1 : 0;
            offlineEvent.baseObject.isThunderActive0x46 = (Math.random() > 0.5) ? 1 : 0;

            // Wet
            offlineEvent.baseObject.roadSurfaceConditions = 0;

            if (offlineEvent.baseObject.gameChangerId0x18 === 0x99E41F00) {
                console.log(idx);
                const hstakes = (parsed.allEvents[408].data.data as GameEvents.EventSwitcher).offlineEvent;
                offlineEvent.name0x84 = hstakes.name0x84;
                offlineEvent.nameFormatted0x88 = hstakes.nameFormatted0x88;
                offlineEvent.baseObject.cinematicName0x10 = hstakes.baseObject.cinematicName0x10;
                offlineEvent.eventIntro0x70 = hstakes.eventIntro0x70;
                offlineEvent.eventOutro0x74 = hstakes.eventOutro0x74;
            }

            if (offlineEvent.baseObject.gameChangerId0x18 === 0x44672200) {
                // const mwvenom = (parsed.allEvents[329].data.data as GameEvents.EventSwitcher).offlineEvent;
            
                // offlineEvent.baseObject.autotestCheckpoints0xc = mwvenom.baseObject.autotestCheckpoints0xc;
                // offlineEvent.baseObject.chevronList0x3c = mwvenom.baseObject.chevronList0x3c;
                // if (mwvenom.baseObject.customChevronPtrArray) {
                //     offlineEvent.baseObject.customChevronPtrArray.length = 0;
                //     offlineEvent.baseObject.customChevronPtrArray.push(...mwvenom.baseObject.customChevronPtrArray);
                // }
                // offlineEvent.baseObject.cycleTimeOfDay0x28 = mwvenom.baseObject.cycleTimeOfDay0x28;
                // offlineEvent.baseObject.finishTimeOfDay0x2c = mwvenom.baseObject.finishTimeOfDay0x2c;
                // offlineEvent.baseObject.float0x38 = mwvenom.baseObject.float0x38;
                // offlineEvent.baseObject.gameChangerId0x18 = mwvenom.baseObject.gameChangerId0x18;
                // offlineEvent.baseObject.gameMode0x1c = mwvenom.baseObject.gameMode0x1c;
                // offlineEvent.baseObject.gamePack0x20 = mwvenom.baseObject.gamePack0x20;
                // offlineEvent.baseObject.isAlternativeWeather0x44 = mwvenom.baseObject.isAlternativeWeather0x44;
                // offlineEvent.baseObject.isRainActive0x45 = mwvenom.baseObject.isRainActive0x45;
                // offlineEvent.baseObject.isThunderActive0x46 = mwvenom.baseObject.isThunderActive0x46;
                // offlineEvent.baseObject.overrideSunDirection0x47 = mwvenom.baseObject.overrideSunDirection0x47;
                // offlineEvent.baseObject.roadSurfaceConditions = mwvenom.baseObject.roadSurfaceConditions;
                // offlineEvent.baseObject.sunDirection0x30 = mwvenom.baseObject.sunDirection0x30;
                // offlineEvent.baseObject.timeOfDay0x34 = mwvenom.baseObject.timeOfDay0x34;
                // offlineEvent.baseObject.uint80x4a = mwvenom.baseObject.uint80x4a;
                // offlineEvent.baseObject.uniqueId0x24 = mwvenom.baseObject.uniqueId0x24;
                // if (mwvenom.baseObject.uniqueIdArray) {
                //     offlineEvent.baseObject.uniqueIdArray.length = 0;
                //     offlineEvent.baseObject.uniqueIdArray.push(...mwvenom.baseObject.uniqueIdArray);
                // }
                // if (mwvenom.additionalAssets0x54) {
                //     offlineEvent.additionalAssets0x54.length = 0;
                //     offlineEvent.additionalAssets0x54.push(...mwvenom.additionalAssets0x54);
                // }
                // if (mwvenom.aiHints0x58) {
                //     offlineEvent.aiHints0x58.length = 0;
                //     offlineEvent.aiHints0x58.push(...mwvenom.aiHints0x58);
                // }
                // if (mwvenom.aiPlayerInformationArray0xc0) {
                //     offlineEvent.aiPlayerInformationArray0xc0.length = 0;
                //     offlineEvent.aiPlayerInformationArray0xc0.push(...mwvenom.aiPlayerInformationArray0xc0);
                // }
                // offlineEvent.allowedVehicleList0x5c = mwvenom.allowedVehicleList0x5c;
                // if (mwvenom.alternateRoutes0xc4) {
                //     offlineEvent.alternateRoutes0xc4.length = 0;
                //     offlineEvent.alternateRoutes0xc4.push(...mwvenom.alternateRoutes0xc4);
                // }
                // offlineEvent.bool0xe9 = mwvenom.bool0xe9;
                // offlineEvent.bool0xea = mwvenom.bool0xea;
                // offlineEvent.bool0xeb = mwvenom.bool0xeb;
                // offlineEvent.bool0xee = mwvenom.bool0xee;
                // offlineEvent.bool0xf1 = mwvenom.bool0xf1;
                // if (mwvenom.checkpointInfoArray0xc8) {
                //     offlineEvent.checkpointInfoArray0xc8.length = 0;
                //     offlineEvent.checkpointInfoArray0xc8.push(...mwvenom.checkpointInfoArray0xc8);
                // }
                // if (mwvenom.checkpoints0x64) {
                //     offlineEvent.checkpoints0x64.length = 0;
                //     offlineEvent.checkpoints0x64.push(...mwvenom.checkpoints0x64);
                // }
                // if (mwvenom.chevronPtrArray0xb4) {
                //     offlineEvent.chevronPtrArray0xb4.length = 0;
                //     offlineEvent.chevronPtrArray0xb4.push(...mwvenom.chevronPtrArray0xb4);
                // }
                // offlineEvent.copSpawning0xe8 = mwvenom.copSpawning0xe8;
                // if (mwvenom.customChevronPtrArray0xb8) {
                //     offlineEvent.customChevronPtrArray0xb8.length = 0;
                //     offlineEvent.customChevronPtrArray0xb8.push(...mwvenom.customChevronPtrArray0xb8);
                // }
                // if (mwvenom.defaultHeatLevels0x6c) {
                //     offlineEvent.defaultHeatLevels0x6c.length = 0;
                //     offlineEvent.defaultHeatLevels0x6c.push(...mwvenom.defaultHeatLevels0x6c);
                // }
                // offlineEvent.demoMode = mwvenom.demoMode;
                // offlineEvent.feedbackMessageGroup0x78 = mwvenom.feedbackMessageGroup0x78;
                // if (mwvenom.gameplayConditionPtrArray0xbc) {
                //     offlineEvent.gameplayConditionPtrArray0xbc.length = 0;
                //     offlineEvent.gameplayConditionPtrArray0xbc.push(...mwvenom.gameplayConditionPtrArray0xbc);
                // }
                // if (mwvenom.gameplayTriggers0x7c) {
                //     offlineEvent.gameplayTriggers0x7c.length = 0;
                //     offlineEvent.gameplayTriggers0x7c.push(...mwvenom.gameplayTriggers0x7c);
                // }
                // offlineEvent.laps0xf6 = mwvenom.laps0xf6;
                // offlineEvent.nextStoryEvent0x8c = mwvenom.nextStoryEvent0x8c;
                // offlineEvent.nitrousAllowed0xec = mwvenom.nitrousAllowed0xec;
                // offlineEvent.noRacingLineTraffic0xed = mwvenom.noRacingLineTraffic0xed;
                // offlineEvent.raceBalancingData0x94 = mwvenom.raceBalancingData0x94;
                // offlineEvent.raceBalancingProfile0x98 = mwvenom.raceBalancingProfile0x98;
                // offlineEvent.spawnPosition0x9c = mwvenom.spawnPosition0x9c;
                // offlineEvent.startWithEngineOn0xef = mwvenom.startWithEngineOn0xef;
                // offlineEvent.targetScore0xcc = mwvenom.targetScore0xcc;
                // if (mwvenom.targetSpeed0xa8) {
                //     offlineEvent.targetSpeed0xa8.length = 0;
                //     offlineEvent.targetSpeed0xa8.push(...mwvenom.targetSpeed0xa8);
                // }
                // if (mwvenom.targetTime0xac) {
                //     offlineEvent.targetTime0xac.length = 0;
                //     offlineEvent.targetTime0xac.push(...mwvenom.targetTime0xac);
                // }
                // if (mwvenom.timeline0xa0) {
                //     offlineEvent.timeline0xa0.length = 0;
                //     offlineEvent.timeline0xa0.push(...mwvenom.timeline0xa0);
                // }
                // offlineEvent.trafficDensity0xb0 = mwvenom.trafficDensity0xb0;
                // offlineEvent.trafficEnabled0xf0 = mwvenom.trafficEnabled0xf0;
                // offlineEvent.trafficOverrides0x4c = mwvenom.trafficOverrides0x4c;
                // offlineEvent.typeName0xa4 = mwvenom.typeName0xa4;
                // offlineEvent.uniqueId0x60 = mwvenom.uniqueId0x60;
                // offlineEvent.uniqueId0x68 = mwvenom.uniqueId0x68;
                // offlineEvent.uniqueId0x80 = mwvenom.uniqueId0x80;
                // offlineEvent.uniqueId0x90 = mwvenom.uniqueId0x90;
                // offlineEvent.weaponsAllowed0xf2 = mwvenom.weaponsAllowed0xf2;
            }
            
            // if (offlineEvent.baseObject.gameChangerId0x18 === 0x44672200) {
            //     // offlineEvent.allowedVehicleList0x5c = 0;
            //     // const revCheckpointsInfo = offlineEvent.checkpointInfoArray0xc8;
            //     // revCheckpointsInfo.reverse();
            //     // offlineEvent.checkpointInfoArray0xc8.concat(revCheckpointsInfo)
            //     // for (const [i, ch] of (offlineEvent.checkpointInfoArray0xc8).entries()) {
            //         //     ch.sequence0xc = i;
            //         // }

            //     offlineEvent.timeline0xa0[0] = 1556824;

            //     offlineEvent.gameplayTriggers0x7c.length = 0;
            //     offlineEvent.gameplayTriggers0x7c.push(2090401);
            //     offlineEvent.gameplayTriggers0x7c.push(2090406);
            //     offlineEvent.gameplayTriggers0x7c.push(2090413);
                                    
            //     // venom
            //     // offlineEvent.allowedVehicleList0x5c = 0;
            //     // offlineEvent.baseObject.bool0x48 = 0;
            //     // offlineEvent.baseObject.float0x38 = 0;
            //     // offlineEvent.baseObject.uint80x4a = 1;
            //     // offlineEvent.baseObject.uniqueId0x24 = 0;
            //     // offlineEvent.uniqueId0x60 = 2090331;
            //     // offlineEvent.uniqueId0x68 = 0;
            //     // offlineEvent.uniqueId0x80 = 2090138;
            //     // offlineEvent.uniqueId0x90 = 0;
            //     // offlineEvent.bool0xe9 = 1;
            //     // offlineEvent.bool0xea = 0;
            //     // offlineEvent.bool0xeb = 0;
            //     // offlineEvent.bool0xee = 0;
            //     // offlineEvent.bool0xf1 = 1;

            //     // // high stakes
            //     // "bool0x48": 1,
            //     // "float0x38": 1,
            //     // "uint80x4a": 1,
            //     // "uniqueId0x24": 0,
            //     // "uniqueId0x60": 995395,
            //     // "uniqueId0x68": 0,
            //     // "uniqueId0x80": 2254703,
            //     // "uniqueId0x90": 0,
            //     // "bool0xe9": 0,
            //     // "bool0xea": 1,
            //     // "bool0xeb": 0,
            //     // "bool0xee": 1,
            //     // "bool0xf1": 1

            //     // // mw1
            //     // "bool0x48": 1,
            //     // "float0x38": 1,
            //     // "uint80x4a": 1,
            //     // "uniqueId0x24": 0,
            //     // "uniqueId0x60": 1689533,
            //     // "uniqueId0x68": 1836280,
            //     // "uniqueId0x80": 1933460,
            //     // "uniqueId0x90": 0,
            //     // "bool0xe9": 1,
            //     // "bool0xea": 0,
            //     // "bool0xeb": 0,
            //     // "bool0xee": 0,
            //     // "bool0xf1": 1

            //     // offlineEvent.laps0xf6 = 3;
            //     offlineEvent.checkpoints0x64.length = 0;

            //     const customCheckpointArray = [1186978,1186981,983499,1592406,2191204,1186983,983499,1186981,1519709,1433882,1433883,1829136,2189817,2189848,2287131,2194297,2193126,2193113,2193122,2193123,2193124,1442947,1442948,1442949,1496428,1442951,1519228,1439952];

            //     // const customCheckpointArray = [1186978,1186981,1556310,983502,1556308,1496497,1556761,2216875,1909553,983500,1556310,2216873,1496496,2216873,2216872,983500,1186993,1186981,983497,1433882,1433883,1556108,2189817,2189848,2189817,1186997,1556108,2287142,1264002,1700233,983507,1496257,983497];
            //     for (let i = 0; i < customCheckpointArray.length; i += 1) {
            //         offlineEvent.checkpoints0x64.push(customCheckpointArray[i]);
            //     }

            //     offlineEvent.baseObject.roadSurfaceConditions = 0;
            //     offlineEvent.baseObject.isThunderActive0x46 = 0;
            //     offlineEvent.trafficEnabled0xf0 = 1;
            //     offlineEvent.trafficDensity0xb0 = 2;
            //     offlineEvent.nitrousAllowed0xec = 1;
            //     offlineEvent.weaponsAllowed0xf2 = 1;
            //     offlineEvent.copSpawning0xe8 = 1;
            //     offlineEvent.noRacingLineTraffic0xed = 0;

            //     // const aiinfoLength = offlineEvent.aiPlayerInformationArray0xc0.length;
            //     // for (let i = 0; i < aiinfoLength; i++) {
            //     //     const toPush = offlineEvent.aiPlayerInformationArray0xc0[i];
            //     //     toPush.placement0x14 = aiinfoLength + i + 1;
            //     //     offlineEvent.aiPlayerInformationArray0xc0.push(toPush);
            //     // }
            // }
        }
    }
    
    await WriteEventsFile(parsed);
    console.log("written successfully...");
}

main();