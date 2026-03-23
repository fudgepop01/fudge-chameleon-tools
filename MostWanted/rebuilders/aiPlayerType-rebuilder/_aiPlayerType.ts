import { BaseField, Endian, Pointer32 as _Pointer32, Struct, StructType, U16, U32, U32s, U8, U8s, I8, I16, I32, I16s } from "construct-js";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import { F32, F32s } from "../../helpers/floatfield";
import { CleanKStruct } from "../../helpers/recursiveOmit";

const u1 = U8;
const u2 = U16;
const u4 = U32;
const s1 = I8;
const s2 = I16;
const s4 = I32;

const f4 = F32;
const IMPORT_ARRAY: StructType[] = [];
let MAIN_STRUCT: StructType;
let PtrPath: string[] = [];

PtrPath.toString = () => {
    return PtrPath.join('.');
}

const P32 = (offsetName: string, pathOffset?: number) => {
    if (PtrPath.length === 0 || PtrPath.slice(0, pathOffset).length === 0) {
        return _Pointer32(MAIN_STRUCT, offsetName);
    }
    return _Pointer32(MAIN_STRUCT, PtrPath.slice(0, pathOffset).join('.').replace(/\.\./g, '.') + '.' + offsetName);
}

const NullableP32 = (isDefined: number | object | undefined, name: string, pathOffset?: number) => {
    return isDefined ? P32(name, pathOffset) : u4(0);
}

const PUSH_IMPORT = (ImportID: number, _P32: ReturnType<typeof _Pointer32>) => {
    const event_import = Struct('event_import_base')
        .field('ID', u4(ImportID, Endian.Big))
        .field('always-1', u4(0x1, Endian.Big))
        .field('offset', _P32)
        .field('padding', U8s([0, 0, 0, 0]));

    IMPORT_ARRAY.push(event_import);
}

const BUILD_ptr_ptr_table = (offsetName: string, structName: string, builder: CallableFunction, arrayData: GenObj.Ptr[]) => {
    // PtrPath.push(offsetName);
    const data = Struct(structName + 'Array');
    const ptrArray = Struct(structName + 'PtrArray');
    
    if (arrayData) {
        for (const [idx, val] of arrayData.map(v => v.data.data as any).entries()) {
            data
                .field(`entry_${idx}`, builder(`${offsetName}Data.entry_${idx}`, val));
            
            ptrArray
                .field(`ptr_entry_${idx}`, P32(`${offsetName}Data.entry_${idx}`));
        }
    }
    if (PtrPath.includes('event_array.event_4')) {
        console.log(PtrPath + '.' + offsetName);
        console.log(arrayData);
        console.log(data);
        console.log(ptrArray);
    }


    // PtrPath.pop();
    return {
        data,
        ptrArray
    };
}

const APPEND_genesys_object = (builder: StructType, obj: CleanKStruct<GenObj.GenObj>, id?: number) => {
    // PtrPath.push('base_object');

    builder
        .field('dynamicData', U8s(new Array(8).fill(0)))
        .field('muID', U32(obj.muTypeVersion, Endian.Big));
    
    if (id) {
        PUSH_IMPORT(id, P32('dynamicData'))
    }
    
    // PtrPath.pop();
}

const BUILD_genesys__gen__aiplayer_type = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenAiplayerType>) => {
    PtrPath.push(offsetName)

    const out = Struct('aiplayer_type');
    APPEND_genesys_object(out, obj.baseObject, 0x6F_FA_06_00);
    out
        .field('cgs_core__unique_id_0xc', u4(obj.cgsCoreUniqueId0xc))
        .field('game_changer_id_0x10', u4(obj.gameChangerId0x10))
        .field('rollout_0x14', u4(obj.rollout0x14))
        .field('ptr_arr_target_placement_0x18', NullableP32(obj.ptrArrTargetPlacement0x18, 'arrTargetPlacement_p0'))
        .field('aggression_delay_0x1c', f4(obj.aggressionDelay0x1c))
        .field('aggression_frequency_0x20', f4(obj.aggressionFrequency0x20))
        .field('blinded_time_scale_0x24', f4(obj.blindedTimeScale0x24))
        .field('escaping_speed_0x28', f4(obj.escapingSpeed0x28))
        .field('fail_jump_daze_time_0x2c', f4(obj.failJumpDazeTime0x2c))
        .field('flat_out_initial_time_0x30', f4(obj.flatOutInitialTime0x30))
        .field('flat_out_time_0x34', f4(obj.flatOutTime0x34))
        .field('hit_damage_percentage_to_daze_0x38', f4(obj.hitDamagePercentageToDaze0x38))
        .field('hit_daze_time_0x3c', f4(obj.hitDazeTime0x3c))
        .field('max_damage_for_speed_effect_0x40', f4(obj.maxDamageForSpeedEffect0x40))
        .field('max_event_balancing_distance_0x44', f4(obj.maxEventBalancingDistance0x44))
        .field('max_speed_for_distance_0x48', f4(obj.maxSpeedForDistance0x48))
        .field('min_damage_for_speed_effect_0x4c', f4(obj.minDamageForSpeedEffect0x4c))
        .field('min_event_balancing_distance_0x50', f4(obj.minEventBalancingDistance0x50))
        .field('min_shortcut_time_0x54', f4(obj.minShortcutTime0x54))
        .field('min_speed_for_distance_0x58', f4(obj.minSpeedForDistance0x58))
        .field('min_throttle_damage_percent_0x5c', f4(obj.minThrottleDamagePercent0x5c))
        .field('min_time_between_weapon_uses_0x60', f4(obj.minTimeBetweenWeaponUses0x60))
        .field('respawn_time_0x64', f4(obj.respawnTime0x64))
        .field('shortcut_taking_percentage_0x68', f4(obj.shortcutTakingPercentage0x68))
        .field('spawn_speed_0x6c', f4(obj.spawnSpeed0x6c))
        .field('speed_0x70', f4(obj.speed0x70))
        .field('speed_matching_max_distance_0x74', f4(obj.speedMatchingMaxDistance0x74))
        .field('speed_matching_max_speed_0x78', f4(obj.speedMatchingMaxSpeed0x78))
        .field('float32_t_0x7c', f4(obj.float32T0x7c))
        .field('speed_matching_min_speed_0x80', f4(obj.speedMatchingMinSpeed0x80))
        .field('speed_matching_speed_difference_0x84', f4(obj.speedMatchingSpeedDifference0x84))
        .field('toughness_0x88', f4(obj.toughness0x88))
        .field('turn_at_junction_percentage_0x8c', f4(obj.turnAtJunctionPercentage0x8c))
        .field('uturn_min_time_0x90', f4(obj.uturnMinTime0x90))
        .field('weapon_avoidance_percentage_0x94', f4(obj.weaponAvoidancePercentage0x94))
        .field('weapon_use_delay_at_event_start_0x98', f4(obj.weaponUseDelayAtEventStart0x98))
        .field('weaving_duration_0x9c', f4(obj.weavingDuration0x9c))
        .field('weaving_frequency_0xa0', f4(obj.weavingFrequency0xa0))
        .field('aggression_type_0xa4', u2(obj.aggressionType0xa4))
        .field('behaviour_0xa6', u2(obj.behaviour0xa6))
        .field('unk_enum_0xa8', u2(obj.unkEnum0xa8))
        .field('nitrous_usage_0xaa', u2(obj.nitrousUsage0xaa))
        .field('weaving_type_0xac', u2(obj.weavingType0xac))
        .field('array_count_for_0x18', u2(obj.arrayCountFor0x18))
        .field('allowed_to_respawn_0xb0', u1(obj.allowedToRespawn0xb0))
        .field('can_rhino_0xb1', u1(obj.canRhino0xb1))
        .field('do_uturns_0xb2', u1(obj.doUturns0xb2))
        .field('is_aggressor_0xb3', u1(obj.isAggressor0xb3))
        .field('is_blacklist_0xb4', u1(obj.isBlacklist0xb4))
        .field('is_cop_0xb5', u1(obj.isCop0xb5))
        .field('bool8_t_0xb6', u1(obj.bool8T0xb6))
        .field('uint8_t_0xb7', u1(obj.uint8T0xb7))
        .field('weapon_use_chance_0xb8', u1(obj.weaponUseChance0xb8))
        .field('padding', U8s(new Array(3).fill(0)))


    if (obj.instTargetPlacement0x18) {
        for (const [idx, val] of obj.instTargetPlacement0x18.entries()) {
            out.field(`arrTargetPlacement_p${idx}`, u4(val))
        }
    }

    PtrPath.pop()

    return out;
}

export const BUILD_FILE = (obj: CleanKStruct<GenObj.GenesysObjCollection>) => {
    IMPORT_ARRAY.splice(0, IMPORT_ARRAY.length)

    const AIPTFile = Struct('aiPlayerTypeFile')
    MAIN_STRUCT = AIPTFile;

    APPEND_genesys_object(AIPTFile, obj.baseObject, 0xF8_FF_FF_FF)

    AIPTFile
        .field('GameChangerID', u4(obj.unkId))
        .field('Item', P32('aipPtrs'))
        .field('ItemCount', u4(obj.objCollection?.length ?? 0))


    const aipPtrs = Struct('aipPtrs');
    const allAips = Struct('allAips');

    if (obj.objCollection) {
        for (const [idx, itm] of obj.objCollection.entries()) {
            allAips
                .field(`aip_${idx}`, BUILD_genesys__gen__aiplayer_type(`aips.aip_${idx}`, (itm.data.data as GenObj).data as GenObj.GenesysGenAiplayerType));
            aipPtrs.field(`aip_${idx}_ptr`, P32(`aips.aip_${idx}`))
        }
    }

    AIPTFile.field('aipPtrs', aipPtrs);
    AIPTFile.field('aips', allAips);

    const currentSize = AIPTFile.computeBufferSize();
    const bytesToPad = 0x10 - (currentSize % 0x10);

    if (bytesToPad > 0) {
        AIPTFile.field('PRE_IMPORT_PADDING', U8s(new Array(bytesToPad)));
    }
    

    // console.log(AIPTFile);
    IMPORT_ARRAY.sort((a, b) => {
        return (a.get('offset') as BaseField).get() - (b.get('offset') as BaseField).get()
    });
    for (const [idx, imp] of IMPORT_ARRAY.entries()) {
        const offsetField = (imp.get('offset') as BaseField);

        const aip_import = Struct('aip_import')
            .field('ID', imp.get('ID'))
            .field('always-1', imp.get('always-1'))
            .field('offset', U32((offsetField.get() | 0x80_00_00_00) >>> 0, Endian.Little))
            .field('padding', U8s([0, 0, 0, 0]));

        AIPTFile.field(`IMPORT_${idx}`, aip_import);
    }

    return AIPTFile.toUint8Array();
}
