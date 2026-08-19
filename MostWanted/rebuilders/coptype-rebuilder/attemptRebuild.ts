import { readFile, writeFile } from "fs/promises";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import KaitaiStream from "kaitai-struct/KaitaiStream"
import { BUILD_FILE } from "./_coptype";
import { CleanKStruct } from "../../helpers/recursiveOmit";
import { carname_LE } from "../../helpers/car_names";
import { playertype_BE, playertype_LE } from "../../helpers/aiplayertypes";

// ts-node attemptRebuild.ts && mv ./AC_1D_10_00/AC_1D_10_00.dat ../../../all_unpacked/gameplay/GenesysObject && py ../../../bundle_packer_unpacker.py --pack MW ../../../all_unpacked/gameplay/IDs_GAMEPLAY.json ../../../_repacked GAMEPLAY.BNDL
const ParseCopTypesFile = async () => {
    const res = (await readFile(__dirname + '/AC_1D_10_00/original.dat'));
    const events = new GenObj(new KaitaiStream(res)).data as GenObj.GenesysObjCollection;
    return events;
}

const WriteCopTypesFile = async (data: GenObj.GenesysObjCollection) => {
    await writeFile(__dirname + '/AC_1D_10_00/AC_1D_10_00.dat', BUILD_FILE(data));
}

// for (const v of carNames) {
//     console.log(v);
// }
// if (1 < 2) process.exit();

const copPlayerTypes = [
    0x00_05_F5_59,
    0x00_05_F6_48,
    0x00_06_FA_77,
    0x00_06_FB_46,
    0x00_06_FB_FA,
    0x00_06_FC_21,
    0x00_06_FC_4B,
    0x00_08_C8_18,
    0x00_08_C8_19,
    0x00_08_C8_1A,
    0x00_08_C8_81,
    0x00_09_01_FB,
    0x00_0E_92_E4,
    0x00_0E_93_58,
    0x00_10_1D_8E,
    0x00_11_14_B4,
    0x00_11_A3_A0,
    0x00_11_A3_EC,
    0x00_11_A6_75,
    0x00_11_A6_76,
    0x00_11_A6_AB,
    0x00_11_A6_AC,
    0x00_11_A6_DA,
    0x00_11_A6_F2,
    // 0x00_11_A7_42,
    // 0x00_11_A7_43,
    0x00_12_7E_62,
    0x00_12_7E_63,
    0x00_12_7E_64,
    0x00_12_7E_9B,
    0x00_15_E1_57,
    0x00_16_02_EB,
    0x00_16_02_EC,
    0x00_16_02_ED,
    0x00_16_02_EE,
    0x00_16_02_EF,
    0x00_16_02_F0,
    0x00_16_02_F1,
    0x00_16_02_F2,
    0x00_16_02_F3,
    0x00_16_02_F4,
    0x00_17_2D_D9,
    0x00_17_2D_DA,
    0x00_17_C1_E9,
    0x00_19_45_28,
    0x00_19_47_F5,
    // 0x00_19_F1_85,
    // 0x00_19_F1_86,
    0x00_21_6E_D6,
    // 0x00_21_6F_24,
    // 0x00_21_6F_29,
    // 0x00_21_6F_2A,
    // 0x00_21_6F_2B,
    // 0x00_21_6F_33,
    // 0x00_21_6F_35,
    // 0x00_21_6F_36,
    // 0x00_21_6F_3A
]

const main = async () => {
    const parsed = await ParseCopTypesFile();

    for (const [idx, copType] of parsed.objCollection.map(v => (v.data.data as GenObj).data as GenObj.GenesysGenGameplayCopType).entries()) {
        // copType.aiplayerType0xc = copPlayerTypes[(idx) % copPlayerTypes.length];//copPlayerTypes[Math.floor(Math.random() * copPlayerTypes.length)];
        copType.canSpawnAhead0x14 = 1;
        copType.canSpawnBehind0x15 = 1;
        copType.canSpawnHeadOn0x16 = 1;
        copType.canSpawnIntercepting0x17 = 1;
        copType.bool8T0x18 = 1;
        copType.canSpawnWaiting0x19 = 0;
    }

    await WriteCopTypesFile(parsed);
    console.log("written successfully...");
}

main();