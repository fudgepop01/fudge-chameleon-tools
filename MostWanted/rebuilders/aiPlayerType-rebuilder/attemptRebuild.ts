import { readFile, writeFile } from "fs/promises";
import { GenericGenObject as GenObj } from "../generic-gen-object";
import KaitaiStream from "kaitai-struct/KaitaiStream"
import { BUILD_FILE } from "./_aiPlayerType";
import { CleanKStruct } from "../helpers/recursiveOmit";

// ts-node attemptRebuild.ts && mv ./8E_FA_06_00/8E_FA_06_00.dat ../../all_unpacked/gameplay/GenesysObject && py ../../bundle_packer_unpacker.py --pack MW ../../all_unpacked/gameplay/IDs_GAMEPLAY.json ../../_repacked GAMEPLAY.BNDL
const ParseAIPlayerTypesFile = async () => {
    const res = (await readFile(__dirname + '/8E_FA_06_00/original.dat'));
    const events = new GenObj(new KaitaiStream(res)).data as GenObj.GenesysObjCollection;
    return events;
}

const WriteAIPlayerTypesFile = async (data: GenObj.GenesysObjCollection) => {
    await writeFile(__dirname + '/8E_FA_06_00/8E_FA_06_00.dat', BUILD_FILE(data));
}

const main = async () => {
    const parsed = await ParseAIPlayerTypesFile();

    for (const [idx, pType] of parsed.objCollection.map(v => (v.data.data as GenObj).data as GenObj.GenesysGenAiplayerType).entries()) {
        pType.aggressionDelay0x1c *= 0.25;
        pType.aggressionFrequency0x20 *= 3;
        pType.weaponUseChance0xb8 = Math.max(20, pType.weaponUseChance0xb8)
        pType.shortcutTakingPercentage0x68 = Math.max(20, pType.shortcutTakingPercentage0x68)
        if (pType.isCop0xb5) {
            pType.canRhino0xb1 = 1;
            pType.doUturns0xb2 = 1;
            pType.spawnSpeed0x6c *= 2;
            if (pType.spawnSpeed0x6c < 100) {
                pType.spawnSpeed0x6c = 100;
            }
            pType.speedMatchingMaxDistance0x74 = 250;
            pType.speedMatchingMaxSpeed0x78 = 250;
            pType.speedMatchingMinSpeed0x80 = 50;
            pType.minTimeBetweenWeaponUses0x60 *= 0.5
            if (pType.behaviour0xa6 === 0) {
                pType.behaviour0xa6 = 13;
            }
            if (pType.unkEnum0xa8 === 11) {
                pType.unkEnum0xa8 = 12;
            }

        } else {
            pType.minTimeBetweenWeaponUses0x60 = 20
        }

        // console.log('analysys stuff', idx, { unkInt: pType.uint8T0xb7 })

    }

    await WriteAIPlayerTypesFile(parsed);
    console.log("written successfully...");
}

main();