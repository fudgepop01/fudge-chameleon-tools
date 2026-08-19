import { readFile, writeFile } from "fs/promises";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import KaitaiStream from "kaitai-struct/KaitaiStream"
import { BUILD_FILE } from "./_rebalancingData";
import { CleanKStruct } from "../../helpers/recursiveOmit";

// ts-node attemptRebuild.ts && py ../../../bundle_packer_unpacker.py --pack MW ../../../all_unpacked/gamemodes/IDs.BIN ../../../_repacked GAMEMODES.BNDL

const rebalancingDatas = [
    '04_A4_11_00',
    '0A_22_1D_00',
    '0C_2F_20_00',
    '13_6A_21_00',
    '1A_E4_1F_00',
    '1F_AB_0F_00',
    '22_71_21_00',
    '25_B4_0F_00',
    '26_A4_11_00',
    '29_AB_0F_00',
    '29_E4_1F_00',
    '2D_04_16_00',
    '2D_15_11_00',
    '2D_70_21_00',
    '2D_79_16_00',
    '36_70_21_00',
    '38_B4_0F_00',
    '38_D5_16_00',
    '38_E4_1F_00',
    '3B_4A_13_00',
    '43_2E_17_00',
    '47_30_17_00',
    '47_E4_1F_00',
    '4A_A5_11_00',
    '4B_67_22_00',
    '58_02_0F_00',
    '59_E7_10_00',
    '5A_2F_17_00',
    '5D_A4_11_00',
    '5E_03_16_00',
    '5F_A8_0F_00',
    '60_70_21_00',
    '62_70_21_00',
    '67_A4_11_00',
    '6A_2E_17_00',
    '6E_15_11_00',
    '71_E4_1F_00',
    '77_BF_17_00',
    '7E_E1_15_00',
    '7F_67_22_00',
    '80_5C_15_00',
    '80_E4_1F_00',
    '87_E1_15_00',
    '8D_B3_0F_00',
    '90_E4_1F_00',
    '94_70_21_00',
    '95_79_16_00',
    '9E_E4_1F_00',
    'A4_6A_21_00',
    'A6_C0_17_00',
    'A7_03_16_00',
    'B5_76_21_00',
    'B7_C0_17_00',
    'B8_70_21_00',
    'BB_F6_15_00',
    'C3_BF_17_00',
    'CA_16_11_00',
    'CC_16_11_00',
    'D1_41_22_00',
    'D4_D4_16_00',
    'D6_A5_11_00',
    'D7_44_19_00',
    'E0_76_21_00',
    'E1_70_21_00',
    'E1_AA_17_00',
    'E4_A3_11_00',
    'EA_E0_15_00',
    'EE_DF_15_00',
    'F4_68_21_00',
    'F9_E0_15_00',
    'FC_71_21_00',
    'FD_68_21_00',
]

const ParseRebalancingDataFile = async (fileName: string) => {
    const res = (await readFile(__dirname + `/datas/original/${fileName}.dat`));
    const data = new GenObj.GenesysGenRaceBalancingData(new KaitaiStream(res));
    return data;
}

const WriteRebalancingDataFile = async (data: Uint8Array, name: string) => {
    await writeFile(__dirname + `/datas/modded/${name}.dat`, data);
}

const main = async () => {
    for (const [idx, file] of rebalancingDatas.entries()) {
        console.log(`[${idx + 1} / ${rebalancingDatas.length}] reading and modding ${file}...`);
        const parsed = await ParseRebalancingDataFile(file);
    
        // makes room for heat levels
        while (parsed.instOpponentData0x18.length > 8) {
            parsed.instOpponentData0x18.pop();
        }

        for (const [idx, balancingData] of parsed.instOpponentData0x18.entries()) {            
            balancingData.behindDistance0x14 = -300;
            balancingData.aheadDistance0x10 = 400;
            balancingData.startCutoffRatio0x24 = 0.2;        
            balancingData.endCutoffRatio0x18 = 0.2;
            // gives a fighting chance when using a slower 
            // car against a much faster car
            balancingData.endSpeedValueAhead0x1c = 1;
            balancingData.endSpeedValueBehind0x20 = 1;
            // we can make them rubberband a LITTLE, as a treat    
            balancingData.startSpeedValueAhead0x28 = 0.25;
            balancingData.startSpeedValueBehind0x2c = 1.5;
        }
        
        const newData = BUILD_FILE(parsed);
        await WriteRebalancingDataFile(newData, file);
        await writeFile(__dirname + `../../../../all_unpacked/gamemodes/GenesysObject/${file}.dat`, newData);
        console.log(`${file} written successfully...`);
    }
    console.log("all done!");
}

main();