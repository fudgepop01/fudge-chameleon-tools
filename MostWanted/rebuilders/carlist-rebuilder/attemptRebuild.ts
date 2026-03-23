import { readFile, writeFile } from "fs/promises";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import KaitaiStream from "kaitai-struct/KaitaiStream"
import { BUILD_FILE } from "./_allowedVehicleList";
import { CleanKStruct } from "../../helpers/recursiveOmit";

// ts-node attemptRebuild.ts && mv ./F7_30_0F_00/F7_30_0F_00.dat ../../all_unpacked/gameplay/GenesysObject && py ../../bundle_packer_unpacker.py --pack MW ../../all_unpacked/gameplay/IDs.BIN ../../_repacked GAMEPLAY.BNDL
const ParseEventsFile = async () => {
    const res = (await readFile(__dirname + '/F7_30_0F_00/original.dat'));
    const events = new GenObj(new KaitaiStream(res)).data as GenObj.GenesysObjCollection;
    return events;
}

const WriteEventsFile = async (data: GenObj.GenesysObjCollection) => {
    await writeFile(__dirname + '/F7_30_0F_00/F7_30_0F_00.dat', BUILD_FILE(data));
}

const main = async () => {
    const parsed = await ParseEventsFile();

    // CleanKStruct<GenObj.GenesysGenGameplayAllowedVehicleList>

    // UNCOMMENT TO ADD AN ENTRY IN THE LIST THAT HAS EVERY VEHICLE ID IN THE GAME

    // const newEntry: any = {
    //     baseObject: {
    //         dynamicGamedata: new Array(8).fill(0),
    //         muTypeVersion: 0xEDFCC052
    //     },
    //     arrayCountFor0x10: 1,
    //     gameChangerId0xc: 2282052,
    //     instGenesysGenGameplayAllowedVehicleListVehicleAndMods0x10:[]
    // };

    // const alias = newEntry.instGenesysGenGameplayAllowedVehicleListVehicleAndMods0x10
    // const carIDList = [
    //     1085698,
    //     2196263,
    //     1160082,
    //     2196529,
    //     2196595,
    //     122672,
    //     1160139,
    //     122675,
    //     2196131,
    //     1160025,
    //     866774,
    //     2196065,
    //     122682,
    //     393276,
    //     122692,
    //     2076005,
    //     393001,
    //     621053,
    //     122701,
    //     2196466,
    //     300097,
    //     2196197,
    //     1160480,
    //     122714,
    //     122716,
    //     2076137,
    //     1399602,
    //     589261,
    //     392074,
    //     2076203,
    //     1085091,
    //     2076339,
    //     1085633,
    //     1097100,
    //     1085958,
    //     1085511,
    //     1551590,
    //     122757,
    //     2076070,
    //     122765,
    //     122769,
    //     122773,
    //     866832,
    //     2076462,
    //     435169,
    //     2076524,
    //     535435,
    //     2076266,
    //     2196399,
    //     1085007,
    //     2076399,
    //     1085186,
    //     2196000,
    //     1085830,
    //     535621,
    //     1085576,
    //     2196334,
    //     122704,
    //     1160350,
    //     122814,
    //     1085764,

    //     1467242,
    //     1399322,
    //     1467164,
    //     1467172,
    //     1467179,
    //     1467186,
    //     1467156,
    //     510072,
    //     122713,
    //     122706,
    //     122699,
    //     1399539,

    //     2277489,
    //     2277456,
    //     2277467,
    //     2277478,
    //     2277252,
    //     2277210,
    //     2277224,
    //     2277238,
    //     2255978,
    //     2255945,
    //     2255956,
    //     2255967,
    //     2255934,
    //     2255901,
    //     2255912,
    //     2255923,
    //     2277368,
    //     2277332,
    //     2277344,
    //     2277356,

    //     122816,
    //     122818,
    //     122819,
    //     122821,
    //     122822,
    //     122824,
    //     122827,
    //     122828,
    //     122829,
    //     122830,
    //     392322,
    // ]

    // for (const carID of carIDList) {
    //     alias.push({
    //         baseObject: {
    //             dynamicGamedata: new Array(8).fill(0),
    //             muTypeVersion: 0x39073EA4
    //         },
    //         vehicle0xc: carID,
    //         arrInlineTargetScores0x18: [-1, -1, -1],
    //         arrInlineTargetSpeeds0x1e: [-1, -1, -1],
    //         difficulty0x2a: 3,
    //         instMods0x14: [],
    //         float32T0x10: 1
    //     })
    // }
    // parsed.objCollection.push({data: {data: {data: newEntry}}} as any);

    await WriteEventsFile(parsed);
    console.log("written successfully...");
}

main();