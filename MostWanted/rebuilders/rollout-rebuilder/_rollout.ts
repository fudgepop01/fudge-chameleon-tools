import { BaseField, Endian, Pointer32 as _Pointer32, Struct, U32,U8s, U32s } from "construct-js";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import { CleanKStruct } from "../../helpers/recursiveOmit";
import { APPEND_genesys_object, AppendImportsToFile, f4, flattenPtrPath, IMPORT_ARRAY, MAIN_STRUCT, NullableP32, P32, PtrPath, s1, s2, u1, u2, u4 } from "../../helpers/rebuilderAddins";

const BUILD_genesys__gen__rollout = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenRollout>) => {
    PtrPath.push(offsetName)

    const instCharacters0x28 = Struct('struct_instCharacters0x28')
        .field('data', U32s(!obj.instCharacters0x28 ? [] : [...obj.instCharacters0x28]));
    const instNumberPlate0x48 = Struct('struct_instNumberPlate0x48')
        .field('data', U32s(!obj.instNumberPlate0x48 ? [] : [...obj.instNumberPlate0x48]));
    const instCgsCoreUniqueId0x3c = Struct('struct_instCgsCoreUniqueId0x3c')
        .field('data', U32s(!obj.instCgsCoreUniqueId0x3c ? [] : [...obj.instCgsCoreUniqueId0x3c]));

    PtrPath.push('weapon_data_0xc');

    const weaponData = Struct('struct_weaponData');
    APPEND_genesys_object(weaponData, obj.weaponData0xc.baseObject, 0x5E_64_04_00);

    const instWeaponUpgrades0x10 = Struct('struct_instWeaponUpgrades0x10')
        .field('data', U32s(!obj.weaponData0xc.instWeaponUpgrades0x10 ? [] : [...obj.weaponData0xc.instWeaponUpgrades0x10]));


    weaponData
        .field("weapon_0xc", u4(obj.weaponData0xc.weapon0xc))
        .field("ptr_arr_weapon_upgrades_0x10", NullableP32(obj.weaponData0xc.instWeaponUpgrades0x10, 'instWeaponUpgrades0x10', -1))
        .field("array_count_for_0x10", u2(obj.weaponData0xc.instWeaponUpgrades0x10?.length ?? 0))
        .field("padding", U8s(new Array(2).fill(0)));
    
    PtrPath.pop();

    const out = Struct('rollout');
    APPEND_genesys_object(out, obj.baseObject, 0x8F_61_04_00);
    out
      .field("weapon_data_0xc", weaponData)
      .field("body_upgrade_0x24", u4(obj.bodyUpgrade0x24))
      .field("ptr_arr_characters_0x28", NullableP32(obj.instCharacters0x28, 'instCharacters0x28'))
      .field("chassis_upgrade_0x2c", u4(obj.chassisUpgrade0x2c))
      .field("colour_0x30", u4(obj.colour0x30))
      .field("damage_bar_profile_0x34", u4(obj.damageBarProfile0x34))
      .field("game_changer_id_0x38", u4(obj.gameChangerId0x38))
      .field("ptr_arr_cgs_core__unique_id_0x3c", NullableP32(obj.ptrArrCgsCoreUniqueId0x3c, 'instCgsCoreUniqueId0x3c'))
      .field("name_0x40", u4(obj.name0x40))
      .field("nitrous_upgrade_0x44", u4(obj.nitrousUpgrade0x44))
      .field("ptr_arr_number_plate_0x48", NullableP32(obj.ptrArrNumberPlate0x48, 'instNumberPlate0x48'))
      .field("cgs_core__unique_id_0x4c", u4(obj.cgsCoreUniqueId0x4c))
      .field("revenge_bonus_0x50", u4(obj.revengeBonus0x50))
      .field("cgs_core__unique_id_0x54", u4(obj.cgsCoreUniqueId0x54))
      .field("vehicle_0x58", u4(obj.vehicle0x58))
      .field("dirt_amount_0x5c", f4(obj.dirtAmount0x5c))
      .field("dust_amount_0x60", f4(obj.dustAmount0x60))
    // doc: '"CharactersCount"'
      .field("array_count_for_0x28", u2(obj.instCharacters0x28?.length ?? 0))
      .field("array_count_for_0x3c", u2(obj.instCgsCoreUniqueId0x3c?.length ?? 0))
    // doc: '"NumberPlateCount"'
      .field("array_count_for_0x48", u2(obj.instNumberPlate0x48?.length ?? 0))
      .field("bool8_t_0x6a", u1(obj.bool8T0x6a))
      .field("is_online_rollout_0x6b", u1(obj.isOnlineRollout0x6b))
      .field("is_player_rollout_0x6c", u1(obj.isPlayerRollout0x6c))
      .field("padding", U8s(new Array(3).fill(0)))
   
    if (obj.weaponData0xc.instWeaponUpgrades0x10) {
        out
            .field('instWeaponUpgrades0x10', instWeaponUpgrades0x10);
    }

    if (obj.instCharacters0x28)
        out.field('instCharacters0x28', instCharacters0x28);
    if (obj.instCgsCoreUniqueId0x3c)
        out.field('instCgsCoreUniqueId0x3c', instCgsCoreUniqueId0x3c)
    if (obj.instNumberPlate0x48)
        out.field('instNumberPlate0x48', instNumberPlate0x48);

    PtrPath.pop()

    return out;
}

export const BUILD_FILE = (obj: CleanKStruct<GenObj.GenesysObjCollection>) => {
    IMPORT_ARRAY.splice(0, IMPORT_ARRAY.length)

    const rolloutFile = Struct('rolloutsFile')
    MAIN_STRUCT[0] = rolloutFile;

    APPEND_genesys_object(rolloutFile, obj.baseObject, 0xF8_FF_FF_FF)

    rolloutFile
        .field('GameChangerID', u4(obj.unkId))
        .field('Item', P32('roPtrs'))
        .field('ItemCount', u2(obj.objCollection?.length ?? 0))
        .field('padding', u2(0));


    const roPtrs = Struct('roPtrs');
    const allRollouts = Struct('allRollouts');

    if (obj.objCollection) {
        for (const [idx, itm] of obj.objCollection.entries()) {
            allRollouts
                .field(`rollout_${idx}`, BUILD_genesys__gen__rollout(`rollouts.rollout_${idx}`, (itm.data.data as GenObj).data as GenObj.GenesysGenRollout));
            roPtrs.field(`rollout_${idx}_ptr`, P32(`rollouts.rollout_${idx}`))
        }
    }

    rolloutFile.field('roPtrs', roPtrs);
    rolloutFile.field('rollouts', allRollouts);

    const currentSize = rolloutFile.computeBufferSize();
    const bytesToPad = 0x10 - (currentSize % 0x10);

    if (bytesToPad > 0 && bytesToPad < 0x10) {
        rolloutFile.field('PRE_IMPORT_PADDING', U8s(new Array(bytesToPad)));
    }

    AppendImportsToFile();

    return rolloutFile.toUint8Array();
}
