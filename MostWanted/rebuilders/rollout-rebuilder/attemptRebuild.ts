import { readFile, writeFile } from "fs/promises";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import KaitaiStream from "kaitai-struct/KaitaiStream"
import { BUILD_FILE } from "./_rollout";
import { CleanKStruct } from "../../helpers/recursiveOmit";
import { carname_LE } from "../../helpers/car_names";

// ts-node attemptRebuild.ts && mv ./94_61_04_00/94_61_04_00.dat ../../../all_unpacked/gameplay/GenesysObject && py ../../../bundle_packer_unpacker.py --pack MW ../../../all_unpacked/gameplay/IDs_GAMEPLAY.json ../../../_repacked GAMEPLAY.BNDL
const ParseRolloutsFile = async () => {
    const res = (await readFile(__dirname + '/94_61_04_00/original.dat'));
    const events = new GenObj(new KaitaiStream(res)).data as GenObj.GenesysObjCollection;
    return events;
}

const WriteRolloutsFile = async (data: GenObj.GenesysObjCollection) => {
    await writeFile(__dirname + '/94_61_04_00/94_61_04_00.dat', BUILD_FILE(data));
}

const carNames = Object.entries(carname_LE)
    .filter(([k, v]) => {
        // console.log(k, k.startsWith('(cut)'));
        return (isNaN(+k) && !k.startsWith('(cut)') && !k.startsWith('(traffic)') && !k.startsWith('(livery)'))
    })
    .map(([k, v]) => k) as any[];

// const trafficCarNames = Object.entries(carname_LE)
//     .filter(([k, v]) => {
//         // console.log(k, k.startsWith('(cut)'));
//         return (k.startsWith('(traffic)'))
//     })
//     .map(([k, v]) => k) as any[];

// for (const v of carNames) {
//     console.log(v);
// }
// if (1 < 2) process.exit();

const main = async () => {
    const parsed = await ParseRolloutsFile();

    for (const [idx, rollout] of parsed.objCollection.map(v => (v.data.data as GenObj).data as GenObj.GenesysGenRollout).entries()) {
        if (rollout.isPlayerRollout0x6c || rollout.isOnlineRollout0x6b) continue;

        // const id = carname_LE[carNames[Math.floor(Math.random() * carNames.length)]]
        // rollout.vehicle0x58 = id;


        // aipt 0   > rollout 3 crown vic
        // aipt 5   > rollout 2 crown vic
        // aipt 10  > rollout 4 ford explorer
        // aipt 18  > rollout 8 vette z06
        // aipt 19  > rollout 2 crown vic
        // aipt 33  > rollout 2 crown vic
        // aipt 69  > rollout 2 crown vic
        // aipt 74  > rollout 34 dodge charger srt8
        // aipt 76  > rollout 36 SWAT van
        // aipt 130 > rollout 57 alfa romeo 4C
        // aipt 177 > rollout 103 alfa romeo 4C

    // switch(idx) {
    //     case 30: rollout.vehicle0x58 = carname_LE['chevrolet corvette ZR1']; rollout.colour0x30 = 0x00_16_32_0D; break;
    //     case 31: rollout.vehicle0x58 = carname_LE['chevrolet corvette ZR1']; rollout.colour0x30 = 0x00_12_46_27; break;
    //     case 32: rollout.vehicle0x58 = carname_LE['chevrolet corvette ZR1']; rollout.colour0x30 = 0x00_12_46_28; break;
    //     case 33: rollout.vehicle0x58 = carname_LE['chevrolet corvette ZR1']; rollout.colour0x30 = 0x00_12_46_2A; break;
    //     case 34: rollout.vehicle0x58 = carname_LE['chevrolet corvette ZR1']; rollout.colour0x30 = 0x00_12_46_2E; break;
    //     case 35: rollout.vehicle0x58 = carname_LE['chevrolet corvette ZR1']; rollout.colour0x30 = 0x00_12_46_30; break;
    //     case 36: rollout.vehicle0x58 = carname_LE['chevrolet corvette ZR1']; rollout.colour0x30 = 0x00_12_46_31; break;
    // }
        // switch(idx) {
        //     // ford crown vic police
        //     case 2: rollout.vehicle0x58 = carname_LE["koenigsegg agera"]; rollout.colour0x30 = 0; break; // carname_LE["aston martin DB5"]; rollout.colour0x30 = 0; break;
        //     // ford crown vic police
        //     case 3: rollout.vehicle0x58 = carname_LE["koenigsegg agera"]; rollout.colour0x30 = 0; break; // carname_LE["pontiac firebird"]; rollout.colour0x30 = 0; break;
        //     // ford explorer police
        //     case 4: rollout.vehicle0x58 = carname_LE["koenigsegg agera"]; rollout.colour0x30 = 18445830; break; // carname_LE["dodge viper SRT8"]; rollout.colour0x30 = 0; break;
        //     // chevrolet corvette Z06 police
        //     case 8: rollout.vehicle0x58 = carname_LE["koenigsegg agera"]; rollout.colour0x30 = 18445831; break; // carname_LE["bmw M3 E46"]; rollout.colour0x30 = 0; break;
        //     // chevrolet corvette Z06 police
        //     case 26: rollout.vehicle0x58 = carname_LE["koenigsegg agera"]; rollout.colour0x30 = 18445831; break; // carname_LE["lamborghini diablo"]; rollout.colour0x30 = 0; break;
        //     // dodge charger SRT8 police
        //     case 34: rollout.vehicle0x58 = carname_LE["koenigsegg agera"]; rollout.colour0x30 = 18445832; break; // carname_LE["porsche 911 GT2"]; rollout.colour0x30 = 0; break;
        //     // dodge charger SRT8 police
        //     case 35: rollout.vehicle0x58 = carname_LE["koenigsegg agera"]; rollout.colour0x30 = 18445832; break; // carname_LE["nissan 350Z"]; rollout.colour0x30 = 0; break;
        //     // SWAT Van
        //     case 36: rollout.vehicle0x58 = carname_LE["koenigsegg agera"]; rollout.colour0x30 = 18445833; break; // carname_LE["bugatty veyron Vitesse"]; rollout.colour0x30 = 0; break;
        //     // dodge charger SRT8 police 
        //     case 53: rollout.vehicle0x58 = carname_LE["koenigsegg agera"]; rollout.colour0x30 = 18445832; break; // carname_LE["land rover evoque"]; rollout.colour0x30 = 0; break;
        // }

        // if (!rollout.isPlayerRollout0x6c && !rollout.isOnlineRollout0x6b) {
        //     if (!rollout.instCharacters0x28) {
        //         rollout['_instCharacters0x28'] = [];
        //         rollout.instCharacters0x28.push(0x00_10_8D_4F);
        //         rollout.instCharacters0x28.push(0x00_10_8D_51);
        //         rollout.instCharacters0x28.push(0x00_10_8D_53);
        //         rollout.instCharacters0x28.push(0x00_10_8D_5B);
        //     }
        //     // if (!rollout.instCgsCoreUniqueId0x3c) {
        //     //     rollout['_instCgsCoreUniqueId0x3c'] = [];
        //     //     rollout.instCgsCoreUniqueId0x3c.push(0x00_10_8D_DB);
        //     //     rollout.instCgsCoreUniqueId0x3c.push(0x00_10_8D_DD);
        //     //     rollout.instCgsCoreUniqueId0x3c.push(0x00_10_8D_DF);
        //     //     rollout.instCgsCoreUniqueId0x3c.push(0x00_10_8D_E1);
        //     // }
        // }

        // if ((carname_LE[rollout.vehicle0x58] as string).startsWith('(cop)')) {
        // } else {
            // const idx = Math.floor(Math.random() * carNames.length);
            // console.log(idx, id);
        // }

        // rollout.weaponData0xc.weapon0xc = 406622;
        // rollout.weaponData0xc.arrayCountFor0x10 = 1;
        // rollout.weaponData0xc["_instWeaponUpgrades0x10"] = [];
        // rollout.weaponData0xc.instWeaponUpgrades0x10.length = 0;
        // rollout.weaponData0xc.instWeaponUpgrades0x10.push(4722832)
    }

    await WriteRolloutsFile(parsed);
    console.log("written successfully...");
}

main();
