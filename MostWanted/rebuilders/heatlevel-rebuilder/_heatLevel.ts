import { BaseField, Endian, Pointer32 as _Pointer32, Struct, U32,U8s, U32s } from "construct-js";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import { CleanKStruct } from "../../helpers/recursiveOmit";
import { APPEND_genesys_object, AppendImportsToFile, f4, flattenPtrPath, IMPORT_ARRAY, MAIN_STRUCT, NullableP32, P32, PtrPath, s1, s2, u1, u2, u4 } from "../../helpers/rebuilderAddins";

const BUILD_cop_behaviour = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour>) => {
    PtrPath.push(offsetName)

    const out = Struct('cop_behaviour');
    APPEND_genesys_object(out, obj.baseObject, 0x68_32_11_00, -3, offsetName);
    out
    .field("cgs_core__unique_id_0xc", u4(obj.cgsCoreUniqueId0xc))
    .field("cop_max_speed_0x10", f4(obj.copMaxSpeed0x10))
    .field("cop_behaviour_0x14", u2(obj.copBehaviour0x14))
    .field("positioning_0x16", s1(obj.positioning0x16))
    .field("padding", U8s(new Array(1).fill(0)))

    PtrPath.pop()

    return out;
}

const BUILD_pursuit_behaviour = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour>) => {
    PtrPath.push(offsetName)

    const copBehaviourPtrName = flattenPtrPath() + 'copBehaviour';
    const copBehaviour = Struct('behaviour');
    if (obj.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c) {
        for (const [idx, behaviour] of obj.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c.entries()) {
            copBehaviour
                .field(`copBehaviour_${idx}`, BUILD_cop_behaviour(copBehaviourPtrName + `.copBehaviour_${idx}`, behaviour))
        }
    }

    const out = Struct('pursuit_behaviour');
    APPEND_genesys_object(out, obj.baseObject, 0x67_32_11_00, offsetName.includes('inst') ? -2 : -2, offsetName);

    out
    .field("roadblock_0xc",u4(obj.roadblock0xc))
    .field("float32_t_0x10",f4(obj.float32T0x10))
    .field("float32_t_0x14",f4(obj.float32T0x14))
    .field("timeInBehaviour_0x18",f4(obj.timeInBehaviour0x18))
    .field("ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c",
        NullableP32(obj.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c, copBehaviourPtrName, -2))
    .field("array_count_for_0x1c",u2(obj.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour0x1c?.length ?? 0))
    .field("spawn_cops_0x22",u1(obj.spawnCops0x22))
    .field("takedownThreshold_0x23",u1(obj.takedownThreshold0x23))


    PtrPath.pop()

    return {
        pursuitBehaviour: out,
        copBehaviour: {
            ptrName: copBehaviourPtrName,
            data: copBehaviour
        }
    };
}

const BUILD_behaviour_coordination = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenHeatLevelBehaviourCoordination>) => {
    PtrPath.push(offsetName)

    const coordination0xc = {
        ptrName: 'coord0xc',
        data: BUILD_pursuit_behaviour(offsetName + '.behaviour0xc', obj.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0xc)
    }
    const coordination0x30 = {
        ptrName: 'coord0x30',
        data: BUILD_pursuit_behaviour(offsetName + '.behaviour0x30', obj.genesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x30)
    }
    const additionalCoordinationArray: {ptrName: string, data: ReturnType<typeof BUILD_pursuit_behaviour>}[] = [];
    if (obj.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x58) {
        for (const [idx, entry] of obj.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x58.entries()) {
            additionalCoordinationArray.push({ptrName: `instCoord_${idx}`, data: BUILD_pursuit_behaviour(`instCoord_${idx}`, entry)});
        }
    }
 
    const out = Struct('behaviour_coordination');
    APPEND_genesys_object(out, obj.baseObject, 0x65_32_11_00);
    out
    .field("behaviour0xc", coordination0xc.data.pursuitBehaviour)
    .field("behaviour0x30", coordination0x30.data.pursuitBehaviour)
    .field("float32_t_0x54", f4(obj.float32T0x54))
    .field("ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58", 
        NullableP32(obj.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x58, additionalCoordinationArray.length ? additionalCoordinationArray[0].ptrName : '', -1))
    .field("array_count_for_0x58", u2(obj.instGenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour0x58?.length ?? 0))
    .field("padding", U8s(new Array(2).fill(0)))

    PtrPath.pop()
    return {
        behaviourCoordination: out,
        coordination0xc,
        coordination0x30,
        additionalCoordinationArray
    };
}

const BUILD_genesys__gen__heat_level = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenHeatLevel>) => {
    PtrPath.push(offsetName)

    const instT831d10000xec = Struct('struct_instT831d10000xec')
        .field('data', U32s(!obj.instT831d10000xec ? [] : [...obj.instT831d10000xec]));
    const instFormationAhead0xf0 = Struct('struct_instFormationAhead0xf0')
        .field('data', U8s(!obj.instFormationAhead0xf0 ? [] : [...obj.instFormationAhead0xf0]))
    const instUint8T0xf4 = Struct('struct_instUint8T0xf4')
        .field('data', U8s(!obj.instUint8T0xf4 ? [] : [...obj.instUint8T0xf4]))
    const instFormationBehind0xf8 = Struct('struct_instFormationBehind0xf8')
        .field('data', U8s(!obj.instFormationBehind0xf8 ? [] : [...obj.instFormationBehind0xf8]))
    const instUint8T0xfc = Struct('struct_instUint8T0xfc')
        .field('data', U8s(!obj.instUint8T0xfc ? [] : [...obj.instUint8T0xfc]))

    const coordination = BUILD_behaviour_coordination('coordination_0xc', obj.coordination0xc);

    const out = Struct('heat_level');
    APPEND_genesys_object(out, obj.baseObject, 0x15_F5_05_00);
    out
        .field('coordination_0xc', coordination.behaviourCoordination)
        .field('cgs_core__unique_id_0x6c', u4(obj.cgsCoreUniqueId0x6c))
        .field('game_changer_id_0x70', u4(obj.gameChangerId0x70))
        .field('helicopter_0x74', u4(obj.helicopter0x74))
        .field('aim_for_payload_time_0x78', f4(obj.aimForPayloadTime0x78))
        .field('chaseCullRadius_0x7c', f4(obj.chaseCullRadius0x7c))
        .field('chaseSpawnRadius0x80', f4(obj.chaseSpawnRadius0x80))
        .field('cooldownCullRadius0x84', f4(obj.cooldownCullRadius0x84))
        .field('cooldownSpawnRadius0x88', f4(obj.cooldownSpawnRadius0x88))
        .field('cooldownTime0x8c', f4(obj.cooldownTime0x8c))
        .field('cop_hearing_range_for_idle_player_0x90', f4(obj.copHearingRangeForIdlePlayer0x90))
        .field('cop_hearing_range_for_moving_player_0x94', f4(obj.copHearingRangeForMovingPlayer0x94))
        .field('cop_sight_cone_angle_when_alert_0x98', f4(obj.copSightConeAngleWhenAlert0x98))
        .field('cop_sight_cone_angle_when_idle_0x9c', f4(obj.copSightConeAngleWhenIdle0x9c))
        .field('cop_sight_range_when_alert_0xa0', f4(obj.copSightRangeWhenAlert0xa0))
        .field('cop_sight_range_when_chasing_0xa4', f4(obj.copSightRangeWhenChasing0xa4))
        .field('cop_sight_range_when_idle_0xa8', f4(obj.copSightRangeWhenIdle0xa8))
        .field('float32_t_0xac', f4(obj.float32T0xac))
        .field('cullRacerRadius0xb0', f4(obj.cullRacerRadius0xb0))
        .field('float32_t_0xb4', f4(obj.float32T0xb4))
        .field('cullWreckedRadius0xb8', f4(obj.cullWreckedRadius0xb8))
        .field('float32_t_0xbc', f4(obj.float32T0xbc))
        .field('float32_t_0xc0', f4(obj.float32T0xc0))
        .field('helicopterInitialDelay0xc4', f4(obj.helicopterInitialDelay0xc4))
        .field('helicopterRespawnTime0xc8', f4(obj.helicopterRespawnTime0xc8))
        .field('helicopterTimeActive0xcc', f4(obj.helicopterTimeActive0xcc))
        .field('patrollingCullRadius0xd0', f4(obj.patrollingCullRadius0xd0))
        .field('patrollingSpawnRadius0xd4', f4(obj.patrollingSpawnRadius0xd4))
        .field('playerSpeedLimit0xd8', f4(obj.playerSpeedLimit0xd8))
        .field('pursuit_radius_0xdc', f4(obj.pursuitRadius0xdc))
        .field('search_radius_0xe0', f4(obj.searchRadius0xe0))
        .field('float32_t_0xe4', f4(obj.float32T0xe4))
        .field('float32_t_0xe8', f4(obj.float32T0xe8))
        .field('unk_enum_0xec', NullableP32(obj.instT831d10000xec, 'instT831d10000xec'))
        .field('ptr_arr_formation_ahead_0xf0', NullableP32(obj.instFormationAhead0xf0, 'instFormationAhead0xf0'))
        .field('ptr_arr_uint8_t_0xf4', NullableP32(obj.instUint8T0xf4, 'instUint8T0xf4'))
        .field('ptr_arr_formation_behind_0xf8', NullableP32(obj.instFormationBehind0xf8, 'instFormationBehind0xf8'))
        .field('ptr_arr_uint8_t_0xfc', NullableP32(obj.instUint8T0xfc, '0xfc.instUint8T0xfc'))
        .field('int16_t_0x100', s2(obj.int16T0x100))
        .field('array_count_for_0xec', u2(obj.instT831d10000xec?.length ?? 0))
        .field('uint16_t_0x104', u2(obj.uint16T0x104))
        .field('array_count_for_0xf0', u2(obj.instFormationAhead0xf0?.length ?? 0))
        .field('array_count_for_0xf4', u2(obj.instUint8T0xf4?.length ?? 0))
        .field('array_count_for_0xf8', u2(obj.instFormationBehind0xf8?.length ?? 0))
        .field('array_count_for_0xfc', u2(obj.instUint8T0xfc?.length ?? 0))
        .field('threshold_0x10e', u2(obj.threshold0x10e))
        .field('allow_cooldown_0x110', u1(obj.allowCooldown0x110))
        .field('bool8_t_0x111', u1(obj.bool8T0x111))
        .field('force_cooldown_0x112', u1(obj.forceCooldown0x112))
        .field('forceDisplayNumber0x113', u1(obj.forceDisplayNumber0x113))
        .field('helicopter_permanent_0x114', u1(obj.helicopterPermanent0x114))
        .field('aim_for_payload_angle_0x115', u1(obj.aimForPayloadAngle0x115))
        .field('display_number_0x116', u1(obj.displayNumber0x116))
        .field('padding', U8s(new Array(1).fill(0)))

    out
        .field(coordination.coordination0xc.data.copBehaviour.ptrName,coordination.coordination0xc.data.copBehaviour.data)
        .field(coordination.coordination0x30.data.copBehaviour.ptrName,coordination.coordination0x30.data.copBehaviour.data)    

    for (const coord of coordination.additionalCoordinationArray) {
        out.field(coord.ptrName, coord.data.pursuitBehaviour);
    }
    for (const coord of coordination.additionalCoordinationArray) {
        out.field(coord.data.copBehaviour.ptrName, coord.data.copBehaviour.data)
    }


    // instances
    out
        .field('instT831d10000xec', instT831d10000xec)
        .field('instFormationAhead0xf0', instFormationAhead0xf0)
        .field('instUint8T0xf4', instUint8T0xf4)
        .field('instFormationBehind0xf8', instFormationBehind0xf8)
        .field('instUint8T0xfc', instUint8T0xfc)


    const bufSize = out.computeBufferSize();
    if (bufSize % 4 != 0) {
        const toAdd = 4 - bufSize % 4;
        out.field('__PADDING__', U8s(new Array(toAdd).fill(0)));
    }

    PtrPath.pop()

    return out;
}

export const BUILD_FILE = (obj: CleanKStruct<GenObj.GenesysObjCollection>) => {
    IMPORT_ARRAY.splice(0, IMPORT_ARRAY.length)

    const HeatLevelFile = Struct('heatLevelFile')
    MAIN_STRUCT[0] = HeatLevelFile;

    APPEND_genesys_object(HeatLevelFile, obj.baseObject, 0xF8_FF_FF_FF)

    HeatLevelFile
        .field('GameChangerID', u4(obj.unkId))
        .field('Item', P32('heatLevelPtrs'))
        .field('ItemCount', u2(obj.objCollection?.length ?? 0))
        .field('padding', u2(0));


    const heatLevelPtrs = Struct('heatLevelPtrs');
    const allHeatLevels = Struct('allHeatLevels');

    if (obj.objCollection) {
        for (const [idx, itm] of obj.objCollection.entries()) {
            allHeatLevels
                .field(`hlevel_${idx}`, BUILD_genesys__gen__heat_level(`hlevels.hlevel_${idx}`, (itm.data.data as GenObj).data as GenObj.GenesysGenHeatLevel));
            heatLevelPtrs.field(`hlevel_${idx}_ptr`, P32(`hlevels.hlevel_${idx}`))
        }
    }

    HeatLevelFile.field('heatLevelPtrs', heatLevelPtrs);
    HeatLevelFile.field('hlevels', allHeatLevels);

    const currentSize = HeatLevelFile.computeBufferSize();
    const bytesToPad = 0x10 - (currentSize % 0x10);

    if (bytesToPad > 0) {
        HeatLevelFile.field('PRE_IMPORT_PADDING', U8s(new Array(bytesToPad)));
    }
    

    AppendImportsToFile();

    return HeatLevelFile.toUint8Array();
}
