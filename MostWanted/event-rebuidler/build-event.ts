import { BaseField, Endian, Pointer32 as _Pointer32, Struct, StructType, U16, U32, U32s, U8, U8s } from "construct-js";
import { Event as EVT } from "./parse-event";
import { BUILD_genesys_object } from "./genesys-object";
import { F32, F32s } from "../helpers/floatfield";
import { CleanKStruct } from "../helpers/recursiveOmit";

const u1 = U8;
const u2 = U16;
const u4 = U32;
const f4 = F32;




const EVENT_IMPORT_ARRAY: StructType[] = [];
let MAIN_EVENT_DATA: StructType;
let PtrPath: string[] = [];

const P32 = (offsetName: string) => {
    if (PtrPath.length === 0) {
        return _Pointer32(MAIN_EVENT_DATA, offsetName);
    }
    return _Pointer32(MAIN_EVENT_DATA, PtrPath.join('.').replace(/\.\./g, '.') + '.' + offsetName);
}

const NullableP32 = (isDefined: number | object | undefined, name: string) => {
    return isDefined ? P32(name) : u4(0);
}

const PUSH_EVENT_IMPORT = (ImportID: number, _P32: ReturnType<typeof _Pointer32>) => {
    const event_import = Struct('event_import_base')
        .field('ID', u4(ImportID, Endian.Big))
        .field('always-1', u4(0x1, Endian.Big))
        .field('offset', _P32)
        .field('padding', U8s([0, 0, 0, 0]));

    EVENT_IMPORT_ARRAY.push(event_import);
}

const BUILD_ptr_ptr_table = (offsetName: string, structName: string, builder: CallableFunction, arrayData: EVT.Ptr[]) => {
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

const BUILD_data_array = (offsetName: string, structName: string, builder: CallableFunction, arrayData: any[]) => {
    PtrPath.push(offsetName);
    const data = Struct(structName + 'Array');
    if (arrayData) {
        for (const [idx, val] of arrayData.entries()) {
            data
                .field(`entry_${idx}`, builder(`entry_${idx}`, val));
        }
    }
    PtrPath.pop();
    return data;
}

const BUILD_vpu_vector3 = (offsetName: string, obj: CleanKStruct<EVT.VpuVector3>) => {
    PtrPath.push(offsetName);
    const vpu_vector3 = Struct('vpu_vector3')
        .field(`x`, f4(obj.x))
        .field(`y`, f4(obj.y))
        .field(`z`, f4(obj.z))
        .field(`unused2`, f4(obj.unused2))
    
    PtrPath.pop();
    return vpu_vector3;
}

const BUILD_genesys__gen__challenge_action__action_base__feedback_data = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionActionBaseFeedbackData>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__action_base__feedback_data = Struct('genesys__gen__challenge_action__action_base__feedback_data')
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`unique_id_0xc`, u4(obj.uniqueId0xc))
        .field(`unique_id_0x10`, u4(obj.uniqueId0x10))
        .field(`unique_id_0x14`, u4(obj.uniqueId0x14))
        .field(`unique_id_0x18`, u4(obj.uniqueId0x18))
        .field(`unique_id_0x1c`, u4(obj.uniqueId0x1c))
        .field(`enum_13_37_11_00`, u2(obj.enum13371100))
        .field(`bool_0x22`, u1(obj.bool0x22))
        .field(`padding-fdbackdata`, U8s([0]))

    PUSH_EVENT_IMPORT(0x12_37_11_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__challenge_action__action_base__feedback_data;
}

const BUILD_genesys__gen__challenge_action__accumulation_helper_data = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionAccumulationHelperData>) => {
    PtrPath.push(offsetName);

    const genesys__gen__challenge_action__accumulation_helper_data = Struct('genesys__gen__challenge_action__accumulation_helper_data')
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`unique_id_0xc`, u4(obj.uniqueId0xc))
        .field(`uint32_0x10`, u4(obj.uint320x10))
        .field(`enum_0f_39_11_00`, u2(obj.enum0f391100))
        .field(`bool_0x16`, u1(obj.bool0x16))
        .field(`padding`, U8s([0]))
    
    PUSH_EVENT_IMPORT(0x06_39_11_00, P32(`base_object`));
    
    PtrPath.pop();
    return genesys__gen__challenge_action__accumulation_helper_data;
}

const BUILD_type_finder_for_genesys__gen__challenge_action__action_base = (offsetName: string, obj: CleanKStruct<EVT.TypeFinderForGenesysGenChallengeActionActionBase>) => {
    // console.log(obj.obj.muTypeVersion.toString(16));
    
    switch (obj.obj.muTypeVersion) {
        case 0xE3_70_B2_CC: 
            return BUILD_genesys__gen__challenge_action__accumulate_distance(offsetName, obj.actionType as EVT.GenesysGenChallengeActionAccumulateDistance)
        case 0x2B_A8_0E_31: 
            return BUILD_genesys__gen__challenge_action__accumulate_near_misses(offsetName, obj.actionType as EVT.GenesysGenChallengeActionAccumulateNearMisses)
        case 0xD7_89_93_D1: 
            return BUILD_genesys__gen__challenge_action__accumulate_takedowns(offsetName, obj.actionType as EVT.GenesysGenChallengeActionAccumulateTakedowns)
        case 0x47_DE_09_5B: 
            return BUILD_genesys__gen__challenge_action__accumulate_time(offsetName, obj.actionType as EVT.GenesysGenChallengeActionAccumulateTime)
        case 0x0A_5F_28_EF: 
            return BUILD_genesys__gen__challenge_action__car_state(offsetName, obj.actionType as EVT.GenesysGenChallengeActionCarState)
        case 0x79_8B_78_5D: 
            return BUILD_genesys__gen__challenge_action__coop_accumulate_distance(offsetName, obj.actionType as EVT.GenesysGenChallengeActionCoopAccumulateDistance)
        case 0x63_66_35_21: 
            return BUILD_genesys__gen__challenge_action__do_jump(offsetName, obj.actionType as EVT.GenesysGenChallengeActionDoJump)
        case 0xB3_B4_2A_12: 
            return BUILD_genesys__gen__challenge_action__get_to_location(offsetName, obj.actionType as EVT.GenesysGenChallengeActionGetToLocation)
        case 0xC0_99_71_A8: 
            return BUILD_genesys__gen__challenge_action__hit_trigger(offsetName, obj.actionType as EVT.GenesysGenChallengeActionHitTrigger)
        case 0x3F_12_39_21: 
            return BUILD_genesys__gen__challenge_action__jump_over_players(offsetName, obj.actionType as EVT.GenesysGenChallengeActionJumpOverPlayers)
        case 0xC8_AC_8F_6A: 
            return BUILD_genesys__gen__challenge_action__jump_stats(offsetName, obj.actionType as EVT.GenesysGenChallengeActionJumpStats)
        case 0xE3_E6_76_A8: 
            return BUILD_genesys__gen__challenge_action__speed_camera_action(offsetName, obj.actionType as EVT.GenesysGenChallengeActionSpeedCameraAction)
        case 0xD7_8C_A2_95: 
            return BUILD_genesys__gen__challenge_action__speed_run(offsetName, obj.actionType as EVT.GenesysGenChallengeActionSpeedRun)
    }
    
    throw "UNIDENTIFIED ACTION!!";
    // return type_finder_for_genesys__gen__challenge_action__action_base;
}

const BUILD_genesys__gen__challenge_action__action_base = (offsetName: string, _parent: StructType, obj: CleanKStruct<EVT.GenesysGenChallengeActionActionBase>) => {    
    // PtrPath.push(offsetName);
    // will always have a parent
    _parent
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`feedback_data`, 
            BUILD_genesys__gen__challenge_action__action_base__feedback_data(`feedback_data`, obj.feedbackData))
        .field(`unique_id_0x30`, u4(obj.uniqueId0x30))
        .field(`unique_id_0x34`, u4(obj.uniqueId0x34))
        .field(`game_changer_id_0x38`, u4(obj.gameChangerId0x38))
    
    _parent
        .field(`accumulation_data_ptr_0x3c`, NullableP32(obj.accumulationData, 'accumulation_data'))
        .field(`enum_2d_39_11_00`, u2(obj.enum2d391100))
        .field(`scoring_method`, u2(obj.scoringMethod))
        .field(`can_fail`, u2(obj.canFail))
        .field(`who`, u2(obj.who))

    const accumulation_data_obj = obj.accumulationData;

    // PtrPath.pop();
    return accumulation_data_obj;
}

const BUILD_genesys__gen__challenge__challenge_part = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeChallengePart>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge__challenge_part = Struct('genesys__gen__challenge__challenge_part')
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`unique_id_0xc`, u4(obj.uniqueId0xc))
        .field(`game_changer_id_0x10`, u4(obj.gameChangerId0x10))
        .field(`instruction_0x14`, u4(obj.instruction0x14))
        .field(`unique_id_0x18`, u4(obj.uniqueId0x18))
        .field(`short_instruction_0x1c`, u4(obj.shortInstruction0x1c))
    
    genesys__gen__challenge__challenge_part
        .field(`action_base_ptr_ptr_table_0x20`, P32('action_base_ptr_table'))
        .field(`enum_53_37_11_00`, u2(obj.enum53371100))
        .field(`enum_58_39_11_00`, u2(obj.enum58391100))
        .field(`uint16_0x28`, u2(obj.uint160x28))
        .field(`bool_0x2a`, u1(obj.bool0x2a))
        .field(`array_count_for_0x20`, u1(obj.actionBasePtrTable.length))
    
    const action_base_ptr_table = BUILD_ptr_ptr_table(`action_base_ptr_table`, 'action_base_ptr_table', BUILD_type_finder_for_genesys__gen__challenge_action__action_base, obj.actionBasePtrTable as EVT.Ptr[]);
    
    genesys__gen__challenge__challenge_part
        .field('action_base_ptr_table', action_base_ptr_table.ptrArray)
        .field('action_base_ptr_tableData', action_base_ptr_table.data)

    PUSH_EVENT_IMPORT(0xC8_36_11_00, P32('base_object'));
    
    PtrPath.pop();
    return genesys__gen__challenge__challenge_part;
}

const BUILD_genesys__gen__challenge__location = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeLocation>) => {    
    PtrPath.push(offsetName);
    
    const genesys__gen__challenge__location = Struct('genesys__gen__challenge__location')
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`unique_id_0xc`, u4(obj.uniqueId0xc))
        .field(`display_trigger_ptr_array_0x10`, NullableP32(obj.displayTriggerPtrArray0x10, 'displayTriggerArray'))
        .field(`game_changer_id_0x14`, u4(obj.gameChangerId0x14))
        .field(`trigger_ptr_array_0x18`, NullableP32(obj.triggerPtrArray0x18, 'triggerArray'))
        .field(`array_count_for_0x10`, u2(obj.displayTriggerArr0x10.length))
        .field(`array_count_for_0x18`, u2(obj.triggerArr0x18.length))
    
    const _displayTriggerArray = Struct('displayTriggerArr')
        .field('data', U32s(!obj.displayTriggerArr0x10 ? [] : Object.values(obj.displayTriggerArr0x10).map(v => v as number)));
    const _triggerArray = Struct('triggerArray')
        .field('data', U32s(!obj.triggerArr0x18 ? [] : Object.values(obj.triggerArr0x18).map(v => v as number)));

    genesys__gen__challenge__location
        .field('displayTriggerArray', _displayTriggerArray)
        .field('triggerArray', _triggerArray)

    PUSH_EVENT_IMPORT(0xCC_36_11_00, P32(`base_object`));

    PtrPath.pop();
    return genesys__gen__challenge__location;
}

const BUILD_genesys__gen__chevron = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChevron>) => {
    PtrPath.push(offsetName);
    const genesys__gen__chevron = Struct('genesys__gen__chevron')
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`game_changer_id_0xc`, u4(obj.gameChangerId0xc))
        .field(`road_section_0x10`, u4(obj.roadSection0x10))
        .field(`should_block_start_0x14`, u1(obj.shouldBlockStart0x14))
        .field(`padding`, U8s([0, 0, 0]))
    
    PtrPath.pop();
    return genesys__gen__chevron;
}

const BUILD_genesys__gen__custom_chevron = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenCustomChevron>) => {
    PtrPath.push(offsetName);
    const genesys__gen__custom_chevron = Struct('genesys__gen__custom_chevron')
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`game_changer_id_0xc`, u4(obj.gameChangerId0xc))

    genesys__gen__custom_chevron
        .field(`float_array_ptr_0x10`, P32('floatArray0x10'))
        .field(`float_array_ptr_0x14`, P32('floatArray0x14'))
        .field(`float_array_ptr_0x18`, P32('floatArray0x18'))
        .field(`array_count_for_0x10`, u2(obj.floatArray0x10.length))
        .field(`array_count_for_0x14`, u2(obj.floatArray0x14.length))
        .field(`array_count_for_0x18`, u2(obj.floatArray0x18.length))
        .field(`invert_normal_0x22`, u1(obj.invertNormal0x22))
        .field(`padding`, U8s([0]))
    
    genesys__gen__custom_chevron
        .field('floatArray0x10', F32s(Array.from(obj.floatArray0x10)))
        .field('floatArray0x14', F32s(Array.from(obj.floatArray0x14)))
        .field('floatArray0x18', F32s(Array.from(obj.floatArray0x18)))

    PUSH_EVENT_IMPORT(0x9F_FA_06_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__custom_chevron;
}

const BUILD_genesys__gen__gameplay__condition = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenGameplayCondition>) => {    
    PtrPath.push(offsetName);
    const genesys__gen__gameplay__condition = Struct('genesys__gen__gameplay__condition')
    
    // unused in final
    // const stringsPtrArray0xc = BUILD_data_array('stringPtrArray', , obj.stringsPtrArray0xc)
    const _referenceArray = Struct('referneceArray')
        .field('data', U32s(!obj.referenceArray0x14 ? [] : Object.values(obj.referenceArray0x14).map(v => v as number)));
    const _valuesArray = Struct('valuesArray')
        .field('data', U32s(!obj.valuesArray0x18 ? [] : Object.values(obj.valuesArray0x18).map(v => v as number)));

    genesys__gen__gameplay__condition
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`strings_ptr_array_0xc`, u4(0))
        .field(`game_changer_id_0x10`, u4(obj.gameChangerId0x10))
        .field(`reference_ptr_array_0x14`, NullableP32(obj.referenceArray0x14, 'referenceArray'))
        .field(`values_ptr_array_0x18`, NullableP32(obj.valuesArray0x18, 'valuesArray'))
        .field(`test_type_val`, u2(obj.testTypeVal))
        .field(`type_val`, u2(obj.typeVal))
        .field(`array_count_for_0x14`, u2(obj.referenceArray0x14?.length ?? 0))
        .field(`array_count_for_0xc`, u2(0))
        .field(`array_count_for_0x18`, u2(obj.valuesArray0x18?.length ?? 0))
        .field(`padding`, U8s([0, 0]))

    genesys__gen__gameplay__condition
        .field(`referenceArray`, _referenceArray)
        .field(`valuesArray`, _valuesArray)
    
    PUSH_EVENT_IMPORT(0x67_F1_0E_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__gameplay__condition;
}

const BUILD_genesys__gen__offline_event__ai_player_information = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenOfflineEventAiPlayerInformation>) => {
    PtrPath.push(offsetName);
    const genesys__gen__offline_event__ai_player_information = Struct('genesys__gen__offline_event__ai_player_information')
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`ai_player_type_0xc`, u4(obj.aiPlayerType0xc))
        .field(`back_up_colour_0x10`, u4(obj.backUpColour0x10))
        .field(`placement_0x14`, u4(obj.placement0x14))
        .field(`primary_colour_0x18`, u4(obj.primaryColour0x18))
    
    PUSH_EVENT_IMPORT(0x9A_1D_10_00, P32(`base_object`));            

    PtrPath.pop();
    return genesys__gen__offline_event__ai_player_information;
}

const BUILD_genesys__gen__offline_event__alternate_routes = (offsetName: string, objs: CleanKStruct<EVT.GenesysGenOfflineEventAlternateRoutes>[]) => {
    PtrPath.push(offsetName);
    const alternateRoutesArray = Struct('alternateRoutesArray');
    
    if (objs) {
        const count = objs.length;
        for (let i = 0; i < count; i++) {
            alternateRoutesArray
                .field(`${i}_base_object`, BUILD_genesys_object(objs[i].baseObject))
                .field(`${i}_checkpoint_0xc`, u4(objs[i].checkpoint0xc))
                .field(`${i}_route_marker_ptr_array_0x10`, NullableP32(objs[i].routeMarkerPtrArray0x10, `${i}_routeMarkerArray`))
                .field(`${i}_array_count_for_0x10`, u2(objs[i].routeMarkerArray0x10.length))
                .field(`${i}_padding`, U8s([0, 0]))
        }
    
        for (let i = 0; i < count; i++) {
            const _routeMarkerArray = Struct('routeMarkerArray')
                .field('data', U32s(!objs[i].routeMarkerArray0x10 ? [] : Object.values(objs[i].routeMarkerArray0x10).map(v => v as number)));
        
            alternateRoutesArray
                .field(`${i}_routeMarkerArray`, _routeMarkerArray)
        }
        
        for (let i = 0; i < count; i++) {
            PUSH_EVENT_IMPORT(0x63_F1_0E_00, P32(`${i}_base_object`));            
        }
    }

    PtrPath.pop();
    return alternateRoutesArray;
}

const BUILD_genesys__gen__offline_event__checkpoint_info = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenOfflineEventCheckpointInfo>) => {
    PtrPath.push(offsetName);
    const genesys__gen__offline_event__checkpoint_info = Struct('genesys__gen__offline_event__checkpoint_info')
        .field(`base_object`, BUILD_genesys_object(obj.baseObject))
        .field(`sequence_0xc`, u4(obj.sequence0xc))
        .field(`type_val`, u2(obj.typeVal))
        .field(`bool_0x12`, u1(obj.bool0x12))
        .field(`show_split_time_0x13`, u1(obj.showSplitTime0x13))
    
    PUSH_EVENT_IMPORT(0xC5_23_0B_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__offline_event__checkpoint_info;
}
// event_switcher
//

const BUILD_event_base = (offsetName: string, obj: CleanKStruct<EVT.EventBase>) => {
    
    const builderFn = (autoTestCheckpointArrName: string, customChevronPtrArrayName: string, _parent?: StructType) => {
        if (!_parent) PtrPath.push(offsetName);

        const event_base = Struct('event_base');

        (_parent ?? event_base)
            .field(`base_object`, BUILD_genesys_object(obj.baseObject))
            .field(`autotest_checkpoints_0xc`, NullableP32(obj.uniqueIdArray, autoTestCheckpointArrName))
            .field(`cinematic_name_0x10`, u4(obj.cinematicName0x10))
            .field(`description_0x14`, u4(obj.description0x14))
            .field(`game_changer_id_0x18`, u4(obj.gameChangerId0x18, Endian.Big))
            .field(`game_mode_0x1c`, u4(obj.gameMode0x1c, Endian.Big))
            .field(`game_pack_0x20`, u4(obj.gamePack0x20))
            .field(`unique_id_0x24`, u4(obj.uniqueId0x24))
            .field(`cycle_time_of_day_0x28`, f4(obj.cycleTimeOfDay0x28))
            .field(`finish_time_of_day_0x2c`, f4(obj.finishTimeOfDay0x2c))
            .field(`sun_direction_0x30`, f4(obj.sunDirection0x30))
            .field(`time_of_day_0x34`, f4(obj.timeOfDay0x34))
            .field(`float_0x38`, f4(obj.float0x38))
            .field(`chevron_list_0x3c`, NullableP32(obj.customChevronPtrArray, customChevronPtrArrayName))
            .field(`road_surface_conditions`, u2(obj.roadSurfaceConditions))
            .field(`array_count_for_0xc`, u2(obj.uniqueIdArray?.length ?? 0))
            .field(`is_alternative_weather_0x44`, u1(obj.isAlternativeWeather0x44))
            .field(`is_rain_active_0x45`, u1(obj.isRainActive0x45))
            .field(`is_thunder_active_0x46`, u1(obj.isThunderActive0x46))
            .field(`override_sun_direction_0x47`, u1(obj.overrideSunDirection0x47))
            .field(`bool_0x48`, u1(obj.bool0x48))
            .field(`array_count_for_0x3c`, u1(obj.customChevronPtrArray?.length ?? 0))
            .field(`uint8_0x4a`, u1(obj.uint80x4a))
            .field(`padding-ebase`, U8s([0]))
        
        const autotestCheckpointsArray = Struct('autotestCheckpointsArray');
    
        if (obj.uniqueIdArray) {
            for (const [idx, val] of (obj.uniqueIdArray as number[]).entries()) {
                autotestCheckpointsArray
                    .field(`autotest_checkpoint_${idx}`, u4(val));
            }
        }
    
        const customChevronPtrTableData = BUILD_ptr_ptr_table(customChevronPtrArrayName, customChevronPtrArrayName, BUILD_genesys__gen__custom_chevron, obj.customChevronPtrArray as EVT.Ptr[]);
        if (!_parent) {
            event_base
                .field(customChevronPtrArrayName, customChevronPtrTableData.ptrArray)
                .field(customChevronPtrArrayName + 'Data', customChevronPtrTableData.data)
            PtrPath.pop();
        }

        return {
            event_base,
            autotestCheckpointsArray,
            customChevronPtrTableData
        }
    }

    return builderFn;
}

const BUILD_online_event = (offsetName: string, obj: CleanKStruct<EVT.OnlineEvent>) => {
    
    const builderFn = (oevt_uniqIdArrName: string, _parent?: StructType, autotestCheckpointsArrName?: string, baseCustomChevronName?: string) => {
        if (!_parent) PtrPath.push(offsetName);

        const online_event = Struct('online_event');
        
        const { 
            event_base,
            autotestCheckpointsArray, 
            customChevronPtrTableData 
        } = BUILD_event_base('base_object', obj.baseObject)
            (autotestCheckpointsArrName ?? 'b_autotestCheckpointsArr', baseCustomChevronName ?? 'b_customChevronArr', (_parent ?? online_event));
    
        (_parent ?? online_event)
            .field(`float_arr_0x4c`, f4(obj.floatArr0x4c))
            .field(`float_arr_entry_maybe_0x50`, f4(obj.floatArrEntryMaybe0x50))
            .field(`arena_0x54`, u4(obj.arena0x54))
            .field(`unique_id_0x58`, u4(obj.uniqueId0x58))
            .field(`unique_id_0x5c`, u4(obj.uniqueId0x5c))
            .field(`unique_id_arr_0x60`, NullableP32(obj.uniqueIdArray, oevt_uniqIdArrName))
            .field(`route_0x64`, u4(obj.route0x64))
            .field(`array_count_for_0x4c`, u2(2)) // always 2
            .field(`array_count_for_0x60`, u2(obj.uniqueIdArray?.length ?? 0))
            .field(`requires_airport_0x6c`, u1(obj.requiresAirport0x6c))
            .field(`padding-oevent`, U8s([0, 0, 0]))
    
        const oevent_uniqueIdArray = Struct('oevent_uniqueIdArray')
        if (obj.uniqueIdArray) {
            for (const [idx, id] of (obj.uniqueIdArray as number[]).entries()) {
                oevent_uniqueIdArray
                    .field(`entry_${idx}`, u4(id));
            }
        }

        if (!_parent) {
            online_event
                .field('b_uniqIdArr', autotestCheckpointsArray)
                .field('b_customChevronArr', customChevronPtrTableData.ptrArray)
                .field('b_customChevronArrData', customChevronPtrTableData.data)
                .field(oevt_uniqIdArrName, oevent_uniqueIdArray)

            PtrPath.pop();
        }
        
        return {
            oevent_online_event: online_event,
            autotestCheckpointsArray,
            customChevronPtrTableData,
            oevent_uniqueIdArray
        }
    }

    return builderFn;
}

const BUILD_online_challenge = (offsetName: string, obj: CleanKStruct<EVT.OnlineChallenge>) => {
    PtrPath.push(offsetName);
    const online_challenge = Struct('online_challenge');

    const {
        oevent_online_event,
        autotestCheckpointsArray,
        customChevronPtrTableData,
        oevent_uniqueIdArray
    } = BUILD_online_event('base_object', obj.baseObject)
        ('oevt_uniqIdArr', online_challenge, 'b_autotestCheckpointArr', 'b_customChevronArr');

    online_challenge
        .field(`intro_0x70`, u4(obj.intro0x70))
        .field(`unique_id_0x74`, u4(obj.uniqueId0x74))
        .field(`challenge_part_ptr_ptr_table_0x78`, NullableP32(obj.challengePartPtrTable, 'challengePartPtrArray'))
        .field(`elimination_type`, u2(obj.eliminationType))
        .field(`type_val`, u2(obj.typeVal))
        .field(`array_count_for_0x78`, u1(obj.challengePartPtrTable?.length ?? 0))
        .field(`padding-ochallenge`, U8s([0, 0, 0]))

    online_challenge
        .field('b_autotestCheckpointArr', autotestCheckpointsArray)
        .field('b_customChevronArr', customChevronPtrTableData.ptrArray)
        .field('b_customChevronArrData', customChevronPtrTableData.data)
        .field('oevt_uniqIdArr', oevent_uniqueIdArray);

    const challengePartArray = Struct('challengeParts')
    const challengePartPtrArray = Struct('challengePartPtrTable')

    for (const [idx, part] of (obj.challengePartPtrTable as EVT.Ptr[]).map(v => v.data.data as EVT.GenesysGenChallengeChallengePart).entries()) {
        challengePartArray
            .field(`entry_${idx}`, BUILD_genesys__gen__challenge__challenge_part(`challengePartArray.entry_${idx}`, part));

        challengePartPtrArray
            .field(`ptr_entry_${idx}`, P32(`challengePartArray.entry_${idx}`));
    }

    online_challenge
        .field('challengePartPtrArray', challengePartPtrArray)
        .field('challengePartArray', challengePartArray)

    PtrPath.pop();
    return online_challenge;
}

const BUILD_genesys__gen__challenge_action__accumulate_distance = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionAccumulateDistance>) => {
    PtrPath.push(offsetName);
    
    const genesys__gen__challenge_action__accumulate_distance = Struct('genesys__gen__challenge_action__accumulate_distance')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__accumulate_distance, obj.baseObject)
    
    if (accumulation_data_obj) {
        genesys__gen__challenge_action__accumulate_distance
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }
    
    PUSH_EVENT_IMPORT(0xB2_39_11_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__challenge_action__accumulate_distance;
}

const BUILD_genesys__gen__challenge_action__accumulate_near_misses = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionAccumulateNearMisses>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__accumulate_near_misses = Struct('genesys__gen__challenge_action__accumulate_near_misses')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__accumulate_near_misses, obj.baseObject)
        
    genesys__gen__challenge_action__accumulate_near_misses
        .field(`min_speed_0x48`, f4(obj.minSpeed0x48))
        .field(`challenge_location_ptr_0x4c`, NullableP32(obj.challengeLocationPtr0x4c.offset, 'challenge_location'))
        .field(`in_air_0x50`, u1(obj.inAir0x50))
        .field(`padding`, U8s([0, 0, 0]))
    
    if (accumulation_data_obj) {
        genesys__gen__challenge_action__accumulate_near_misses
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }
    
    if (obj.challengeLocationPtr0x4c.offset) {
        const loc = BUILD_genesys__gen__challenge__location('challenge_location', obj.challengeLocationPtr0x4c.data.data as EVT.GenesysGenChallengeLocation);
        
        genesys__gen__challenge_action__accumulate_near_misses
            .field('challenge_location', loc);
    }

    // 0x02_29_90
    PUSH_EVENT_IMPORT(0x7D_39_11_00, P32(`base_object`));            

    PtrPath.pop();
    return genesys__gen__challenge_action__accumulate_near_misses;
}

const BUILD_genesys__gen__challenge_action__accumulate_takedowns = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionAccumulateTakedowns>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__accumulate_takedowns = Struct('genesys__gen__challenge_action__accumulate_takedowns')    
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__accumulate_takedowns, obj.baseObject)
    
    if (accumulation_data_obj) {
        genesys__gen__challenge_action__accumulate_takedowns
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    PUSH_EVENT_IMPORT(0x05_39_11_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__challenge_action__accumulate_takedowns;
}

const BUILD_genesys__gen__challenge_action__accumulate_time = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionAccumulateTime>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__accumulate_time = Struct('genesys__gen__challenge_action__accumulate_time')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__accumulate_time, obj.baseObject)
    
    if (accumulation_data_obj) {
        genesys__gen__challenge_action__accumulate_time
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    PUSH_EVENT_IMPORT(0xB1_39_11_00, P32(`base_object`));            

    PtrPath.pop();
    return genesys__gen__challenge_action__accumulate_time;
}

const BUILD_genesys__gen__challenge_action__car_state = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionCarState>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__car_state = Struct('genesys__gen__challenge_action__car_state')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__car_state, obj.baseObject)
    
    genesys__gen__challenge_action__car_state
        .field(`car_category_0x48`, u4(obj.carCategory0x48))
        .field(`float_0x4c`, f4(obj.float0x4c))
        .field(`float_0x50`, f4(obj.float0x50))
        .field(`max_speed_0x54`, u2(obj.maxSpeed0x54))
        .field(`min_speed_0x56`, u2(obj.minSpeed0x56))
        .field(`bool_0x58`, u1(obj.bool0x58))
        .field(`bool_0x59`, u1(obj.bool0x59))
        .field(`bool_0x5a`, u1(obj.bool0x5a))
        .field(`donutting_0x5b`, u1(obj.donutting0x5b))
        .field(`drifting_0x5c`, u1(obj.drifting0x5c))
        .field(`in_air_0x5d`, u1(obj.inAir0x5d))
        .field(`nitrous_0x5e`, u1(obj.nitrous0x5e))
        .field(`bool_0x5f`, u1(obj.bool0x5f))
        .field(`reversing_0x60`, u1(obj.reversing0x60))
        .field(`slipstreaming_0x61`, u1(obj.slipstreaming0x61))
        .field(`padding`, U8s([0, 0]))

    if (accumulation_data_obj) {
        genesys__gen__challenge_action__car_state
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }
    
    PUSH_EVENT_IMPORT(0xB0_39_11_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__challenge_action__car_state;
}

const BUILD_genesys__gen__challenge_action__coop_accumulate_distance = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionCoopAccumulateDistance>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__coop_accumulate_distance = Struct('genesys__gen__challenge_action__coop_accumulate_distance')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__coop_accumulate_distance, obj.baseObject)
    
    if (accumulation_data_obj) {
        genesys__gen__challenge_action__coop_accumulate_distance
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    PUSH_EVENT_IMPORT(0xA6_A0_19_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__challenge_action__coop_accumulate_distance;
}

const BUILD_genesys__gen__challenge_action__do_jump = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionDoJump>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__do_jump = Struct('genesys__gen__challenge_action__do_jump')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__do_jump, obj.baseObject)
        
    genesys__gen__challenge_action__do_jump
        .field(`challenge_location_ptr_0x48`, NullableP32(obj.challengeLocationPtr0x48.offset, 'challenge_location'))
        .field(`accumulate_0x4c`, u1(obj.accumulate0x4c))
        .field(`padding`, U8s([0, 0, 0]))

    if (accumulation_data_obj) {
        genesys__gen__challenge_action__do_jump
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    if (obj.challengeLocationPtr0x48.offset) {
        const loc = BUILD_genesys__gen__challenge__location('challenge_location', obj.challengeLocationPtr0x48.data.data as EVT.GenesysGenChallengeLocation);
        
        genesys__gen__challenge_action__do_jump
            .field('challenge_location', loc);
    }

    PUSH_EVENT_IMPORT(0xD8_39_11_00, P32(`base_object`));            

    PtrPath.pop();
    return genesys__gen__challenge_action__do_jump;
}

const BUILD_genesys__gen__challenge_action__get_to_location = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionGetToLocation>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__get_to_location = Struct('genesys__gen__challenge_action__get_to_location')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__get_to_location, obj.baseObject)
        
    genesys__gen__challenge_action__get_to_location
        .field(`challenge_location_ptr_0x48`, NullableP32(obj.challengeLocationPtr0x48.offset, 'challenge_location'))
        .field(`route_location_0x4c`, u1(obj.routeLocation0x4c))
        .field(`bool_0x4d`, u1(obj.bool0x4d))
        .field(`padding`, U8s([0, 0]))

    if (accumulation_data_obj) {
        genesys__gen__challenge_action__get_to_location
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    if (obj.challengeLocationPtr0x48.offset) {
        const loc = BUILD_genesys__gen__challenge__location('challenge_location', obj.challengeLocationPtr0x48.data.data as EVT.GenesysGenChallengeLocation);
        
        genesys__gen__challenge_action__get_to_location
            .field('challenge_location', loc);
    }

    PUSH_EVENT_IMPORT(0xCD_36_11_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__challenge_action__get_to_location;
}

const BUILD_genesys__gen__challenge_action__hit_trigger = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionHitTrigger>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__hit_trigger = Struct('genesys__gen__challenge_action__hit_trigger')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__hit_trigger, obj.baseObject)
    
    genesys__gen__challenge_action__hit_trigger
        .field(`trigger_0x48`, u4(obj.trigger0x48))

    if (accumulation_data_obj) {
        genesys__gen__challenge_action__hit_trigger
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    PUSH_EVENT_IMPORT(0xD9_39_11_00, P32(`base_object`));            
   
    PtrPath.pop();
    return genesys__gen__challenge_action__hit_trigger;
}

const BUILD_genesys__gen__challenge_action__jump_over_players = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionJumpOverPlayers>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__jump_over_players = Struct('genesys__gen__challenge_action__jump_over_players')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__jump_over_players, obj.baseObject)

    genesys__gen__challenge_action__jump_over_players
        .field(`challenge_location_ptr_0x48`, NullableP32(obj.challengeLocationPtr0x48.offset, 'challenge_location'))
        .field(`bool_0x4c`, u1(obj.bool0x4c))
        .field(`padding`, U8s([0, 0, 0]))
        
    if (accumulation_data_obj) {
        genesys__gen__challenge_action__jump_over_players
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    if (obj.challengeLocationPtr0x48.offset) {
        const loc = BUILD_genesys__gen__challenge__location('challenge_location', obj.challengeLocationPtr0x48.data.data as EVT.GenesysGenChallengeLocation);
        
        genesys__gen__challenge_action__jump_over_players
            .field('challenge_location', loc);
    }

    PUSH_EVENT_IMPORT(0xD3_39_11_00, P32(`base_object`));            

    PtrPath.pop();
    return genesys__gen__challenge_action__jump_over_players;
}

const BUILD_genesys__gen__challenge_action__jump_stats = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionJumpStats>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__jump_stats = Struct('genesys__gen__challenge_action__jump_stats')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__jump_stats, obj.baseObject)
    
    genesys__gen__challenge_action__jump_stats
        .field(`challenge_location_ptr_0x48`, NullableP32(obj.challengeLocationPtr0x48.offset, 'challenge_location'))

    if (accumulation_data_obj) {
        genesys__gen__challenge_action__jump_stats
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    if (obj.challengeLocationPtr0x48.offset) {
        const loc = BUILD_genesys__gen__challenge__location('challenge_location', obj.challengeLocationPtr0x48.data.data as EVT.GenesysGenChallengeLocation);
        
        genesys__gen__challenge_action__jump_stats
            .field('challenge_location', loc);
    }

    PUSH_EVENT_IMPORT(0x5C_37_11_00, P32(`base_object`));            
    
    PtrPath.pop();
    return genesys__gen__challenge_action__jump_stats;
}

const BUILD_genesys__gen__challenge_action__speed_camera_action = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionSpeedCameraAction>) => {
    PtrPath.push(offsetName);
    // console.log((obj as any).constructor.name);
    // console.log((obj.baseObject as any).constructor.name);
    
    const genesys__gen__challenge_action__speed_camera_action = Struct('genesys__gen__challenge_action__speed_camera_action')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__speed_camera_action, obj.baseObject)
    
    genesys__gen__challenge_action__speed_camera_action
        .field(`unique_id_0x48`, u4(obj.uniqueId0x48))
        .field(`on_hit_sequence_0x4c`, u4(obj.onHitSequence0x4c))
        .field(`challenge_location_ptr_0x50`, NullableP32(obj.challengeLocationPtr0x50.offset, 'challenge_location'))
        
    if (accumulation_data_obj) {
        genesys__gen__challenge_action__speed_camera_action
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    if (obj.challengeLocationPtr0x50.offset) {
        const loc = BUILD_genesys__gen__challenge__location('challenge_location', obj.challengeLocationPtr0x50.data.data as EVT.GenesysGenChallengeLocation);
        
        genesys__gen__challenge_action__speed_camera_action
            .field('challenge_location', loc);
    }


    PUSH_EVENT_IMPORT(0x4E_37_11_00, P32('base_object'));
    PtrPath.pop();
    return genesys__gen__challenge_action__speed_camera_action;
}

const BUILD_genesys__gen__challenge_action__speed_run = (offsetName: string, obj: CleanKStruct<EVT.GenesysGenChallengeActionSpeedRun>) => {
    PtrPath.push(offsetName);
    const genesys__gen__challenge_action__speed_run = Struct('genesys__gen__challenge_action__speed_run')
    const accumulation_data_obj = BUILD_genesys__gen__challenge_action__action_base('base_object', genesys__gen__challenge_action__speed_run, obj.baseObject)

    genesys__gen__challenge_action__speed_run
        .field(`challenge_location_ptr_0x48_0`, NullableP32(obj.routePtrArray0x48[0].offset, 'challenge_location_0'))
        .field(`challenge_location_ptr_0x48_1`, NullableP32(obj.routePtrArray0x48[1].offset, 'challenge_location_1'))
        .field(`array_count_for_0x48`, u1(2)) // always 2
        .field(`padding`, U8s([0, 0, 0]))
    
    if (accumulation_data_obj) {
        genesys__gen__challenge_action__speed_run
            .field('accumulation_data', BUILD_genesys__gen__challenge_action__accumulation_helper_data('accumulation_data', accumulation_data_obj));
    }

    if (obj.routePtrArray0x48[0].offset) {
        const loc = BUILD_genesys__gen__challenge__location('challenge_location_0', obj.routePtrArray0x48[0].data.data as EVT.GenesysGenChallengeLocation);
        
        genesys__gen__challenge_action__speed_run
            .field('challenge_location_0', loc);
    }

    if (obj.routePtrArray0x48[1].offset) {
        const loc = BUILD_genesys__gen__challenge__location('challenge_location_1', obj.routePtrArray0x48[1].data.data as EVT.GenesysGenChallengeLocation);
        
        genesys__gen__challenge_action__speed_run
            .field('challenge_location_1', loc);
    }
    
    PUSH_EVENT_IMPORT(0xFA_F8_17_00, P32('base_object'));
    
    PtrPath.pop();
    return genesys__gen__challenge_action__speed_run;
}

const BUILD_vote_event = (offsetName: string, obj: CleanKStruct<EVT.VoteEvent>) => {
    PtrPath.push(offsetName);
    const vote_event = Struct('vote_event')
    const {
        oevent_online_event,
        autotestCheckpointsArray,
        customChevronPtrTableData,
        oevent_uniqueIdArray
    } = BUILD_online_event('base_object', obj.baseObject)
        ('oevt_uniqIdArr', vote_event, 'b_autotestCheckpointArr', 'b_customChevronArr');

    vote_event
        .field(`unique_id_0x70`, u4(obj.uniqueId0x70))
        .field(`unique_id_0x74`, u4(obj.uniqueId0x74))
        .field(`unique_id_0x78`, u4(obj.uniqueId0x78))
        .field(`unique_id_0x7c`, u4(obj.uniqueId0x7c))

    vote_event
        .field("b_autotestCheckpointArr", autotestCheckpointsArray)
        .field("b_customChevronArr", customChevronPtrTableData.ptrArray)
        .field("b_customChevronArrData", customChevronPtrTableData.data)
        .field("oevt_uniqIdArr", oevent_uniqueIdArray)
    
    PtrPath.pop();
    return vote_event;
}

const BUILD_offline_event = (offsetName: string, obj: CleanKStruct<EVT.OfflineEvent>) => {
    PtrPath.push(offsetName);

    const offline_event = Struct('offline_event')
    const { 
        event_base,
        autotestCheckpointsArray, 
        customChevronPtrTableData: b_customChevronPtrTableData 
    } = BUILD_event_base('base_object', obj.baseObject)
        ('b_autotestCheckpointsArr', 'b_customChevronArr', offline_event);

    const _additionalAssets0x54 = Struct('oevt_additionalAssets0x54')
        .field('data', U32s(!obj.additionalAssets0x54 ? [] : Object.values(obj.additionalAssets0x54).map(v => v as number)));
    const _aiHints0x58 = Struct('oevt_aiHints0x58')
        .field('data', U32s(!obj.aiHints0x58 ? [] : Object.values(obj.aiHints0x58).map(v => v as number)));
    const _checkpoints0x64 = Struct('oevt_checkpoints0x64')
        .field('data', U32s(!obj.checkpoints0x64 ? [] : Object.values(obj.checkpoints0x64).map(v => v as number)));
    const _defaultHeatLevels0x6c = Struct('oevt_defaultHeatLevels0x6c')
        .field('data', U32s(!obj.defaultHeatLevels0x6c ? [] : Object.values(obj.defaultHeatLevels0x6c).map(v => v as number)));
    const _gameplayTriggers0x7c = Struct('oevt_gameplayTriggers0x7c')
        .field('data', U32s(!obj.gameplayTriggers0x7c ? [] : Object.values(obj.gameplayTriggers0x7c).map(v => v as number)));
    const _timeline0xa0 = Struct('oevt_timeline0xa0')
        .field('data', U32s(!obj.timeline0xa0 ? [] : Object.values(obj.timeline0xa0).map(v => v as number)));
    const _targetSpeed0xa8 = Struct('oevt_targetSpeed0xa8')
        .field('data', F32s(!obj.targetSpeed0xa8 ? [] : Object.values(obj.targetSpeed0xa8).map(v => v as number)));
    const _targetTime0xac = Struct('oevt_targetTime0xac')
        .field('data', F32s(!obj.targetTime0xac ? [] : Object.values(obj.targetTime0xac).map(v => v as number)));

    
    const aiPlayerInformationArray = BUILD_data_array('aiPlayerInformationArray', 'aiPlayerInformationArray', BUILD_genesys__gen__offline_event__ai_player_information, obj.aiPlayerInformationArray0xc0 as any[]);
    const alternateRoutesArray = BUILD_genesys__gen__offline_event__alternate_routes('alternateRoutesArray', obj.alternateRoutes0xc4 as any[]);
    const checkpointInfoArray = BUILD_data_array('checkpointInfoArray', 'checkpointInfoArray', BUILD_genesys__gen__offline_event__checkpoint_info, obj.checkpointInfoArray0xc8 as any[])

    const chevronPtrArray = BUILD_ptr_ptr_table('chevronPtrArray', 'chevron', BUILD_genesys__gen__chevron, obj.chevronPtrArray0xb4 as EVT.Ptr[])
    const customChevronPtrArray = BUILD_ptr_ptr_table('customChevronPtrArray', 'customChevron', BUILD_genesys__gen__custom_chevron, obj.customChevronPtrArray0xb8 as EVT.Ptr[])
    const gameplayConditionPtrArray = BUILD_ptr_ptr_table('gameplayConditionPtrArray', 'gameplayCondition', BUILD_genesys__gen__gameplay__condition, obj.gameplayConditionPtrArray0xbc as EVT.Ptr[]);
    
    offline_event
        .field(`traffic_overrides_0x4c`, U8s(Array.from(obj.trafficOverrides0x4c)))
        .field(`additional_assets_ptr_0x54`, NullableP32(obj.additionalAssets0x54, 'additionalAssets0x54'))
        .field(`ai_hints_ptr_0x58`, NullableP32(obj.aiHints0x58, 'aiHints0x58'))
        .field(`allowed_vehicle_list_0x5c`, u4(obj.allowedVehicleList0x5c))
        .field(`unique_id_0x60`, u4(obj.uniqueId0x60))
        .field(`checkpoints_ptr_0x64`, NullableP32(obj.checkpoints0x64, 'checkpoints0x64'))
        .field(`unique_id_0x68`, u4(obj.uniqueId0x68))
        .field(`default_heat_levels_ptr_0x6c`, NullableP32(obj.defaultHeatLevels0x6c, 'defaultHeatLevels0x6c'))
        .field(`event_intro_0x70`, u4(obj.eventIntro0x70))
        .field(`event_outro_0x74`, u4(obj.eventOutro0x74))
        .field(`feedback_message_group_0x78`, u4(obj.feedbackMessageGroup0x78))
        .field(`gameplay_triggers_ptr_0x7c`, NullableP32(obj.gameplayTriggers0x7c, 'gameplayTriggers0x7c'))
        .field(`unique_id_0x80`, u4(obj.uniqueId0x80))
        .field(`name_0x84`, u4(obj.name0x84))
        .field(`name_formatted_0x88`, u4(obj.nameFormatted0x88))
        .field(`next_story_event_0x8c`, u4(obj.nextStoryEvent0x8c))
        .field(`unique_id_0x90`, u4(obj.uniqueId0x90))
        .field(`race_balancing_data_0x94`, u4(obj.raceBalancingData0x94))
        .field(`race_balancing_profile_0x98`, u4(obj.raceBalancingProfile0x98))
        .field(`spawn_position_0x9c`, u4(obj.spawnPosition0x9c))
        .field(`timeline_ptr_0xa0`, NullableP32(obj.timeline0xa0, 'timeline0xa0'))
        .field(`type_name_0xa4`, u4(obj.typeName0xa4))
        .field(`target_speed_ptr_0xa8`, NullableP32(obj.targetSpeed0xa8, 'targetSpeed0xa8'))
        .field(`target_time_ptr_0xac`, NullableP32(obj.targetTime0xac, 'targetTime0xac'))
        .field(`traffic_density_0xb0`, f4(obj.trafficDensity0xb0))
        .field(`chevron_ptr_ptr_table_0xb4`, NullableP32(obj.chevronPtrArray0xb4, 'chevronPtrArray'))
        .field(`custom_chevron_ptr_ptr_table_0xb8`, NullableP32(obj.customChevronPtrArray0xb8, 'customChevronPtrArray'))
        .field(`gameplay_condition_ptr_ptr_table_0xbc`, NullableP32(obj.gameplayConditionPtrArray0xbc, 'gameplayConditionPtrArray'))
        .field(`ai_player_information_ptr_array_0xc0`, NullableP32(obj.aiPlayerInformationArray0xc0, 'aiPlayerInformationArray'))
        .field(`alternate_routes_ptr_array_0xc4`, NullableP32(obj.alternateRoutes0xc4, 'alternateRoutesArray'))
        .field(`checkpoint_info_ptr_array_0xc8`, NullableP32(obj.checkpointInfoArray0xc8, 'checkpointInfoArray'))
        .field(`target_score_0xcc`, u4(obj.targetScore0xcc))
        .field(`demo_mode`, u2(obj.demoMode))
        .field(`array_count_for_0x54`, u2(obj.additionalAssets0x54?.length ?? 0))
        .field(`array_count_for_0x58`, u2(obj.aiHints0x58?.length ?? 0))
        .field(`array_count_for_0xc0`, u2(obj.aiPlayerInformationArray0xc0?.length ?? 0))
        .field(`array_count_for_0xc4`, u2(obj.alternateRoutes0xc4?.length ?? 0))
        .field(`array_count_for_0xc8`, u2(obj.checkpointInfoArray0xc8?.length ?? 0))
        .field(`array_count_for_0x64`, u2(obj.checkpoints0x64?.length ?? 0))
        .field(`array_count_for_0x6c`, u2(obj.defaultHeatLevels0x6c?.length ?? 0))
        .field(`array_count_for_0xb4`, u2(obj.chevronPtrArray0xb4?.length ?? 0))
        .field(`array_count_for_0xa8`, u2(obj.targetSpeed0xa8?.length ?? 0))
        .field(`array_count_for_0xac`, u2(obj.targetTime0xac?.length ?? 0))
        .field(`array_count_for_0xa0`, u2(obj.timeline0xa0?.length ?? 0))
        .field(`cop_spawning_0xe8`, u1(obj.copSpawning0xe8))
        .field(`bool_0xe9`, u1(obj.bool0xe9))
        .field(`bool_0xea`, u1(obj.bool0xea))
        .field(`bool_0xeb`, u1(obj.bool0xeb))
        .field(`nitrous_allowed_0xec`, u1(obj.nitrousAllowed0xec))
        .field(`no_racing_line_traffic_0xed`, u1(obj.noRacingLineTraffic0xed))
        .field(`bool_0xee`, u1(obj.bool0xee))
        .field(`start_with_engine_on_0xef`, u1(obj.startWithEngineOn0xef))
        .field(`traffic_enabled_0xf0`, u1(obj.trafficEnabled0xf0))
        .field(`bool_0xf1`, u1(obj.bool0xf1))
        .field(`weapons_allowed_0xf2`, u1(obj.weaponsAllowed0xf2))
        .field(`array_count_for_0xb8`, u1(obj.customChevronPtrArray0xb8?.length ?? 0))
        .field(`array_count_for_0xbc`, u1(obj.gameplayConditionPtrArray0xbc?.length ?? 0))
        .field(`array_count_for_0x7c`, u1(obj.gameplayTriggers0x7c?.length ?? 0))
        .field(`laps_0xf6`, u1(obj.laps0xf6))
        .field(`padding`, U8s([0]))

    offline_event
        .field("b_autotestCheckpointsArr", autotestCheckpointsArray)
        .field("b_customChevronArr", b_customChevronPtrTableData.ptrArray)
        .field("b_customChevronArrData", b_customChevronPtrTableData.data)

    offline_event
        .field('additionalAssets0x54', _additionalAssets0x54)
        .field('aiHints0x58', _aiHints0x58)
        .field('checkpoints0x64', _checkpoints0x64)
        .field('defaultHeatLevels0x6c', _defaultHeatLevels0x6c)
        .field('gameplayTriggers0x7c', _gameplayTriggers0x7c)
        .field('timeline0xa0', _timeline0xa0)
        .field('targetSpeed0xa8', _targetSpeed0xa8)
        .field('targetTime0xac', _targetTime0xac)
        .field('chevronPtrArray', chevronPtrArray.ptrArray)
        .field('chevronPtrArrayData', chevronPtrArray.data)
        .field('customChevronPtrArray', customChevronPtrArray.ptrArray)
        .field('customChevronPtrArrayData', customChevronPtrArray.data)
        .field('gameplayConditionPtrArray', gameplayConditionPtrArray.ptrArray)
        .field('gameplayConditionPtrArrayData', gameplayConditionPtrArray.data)
        .field('aiPlayerInformationArray', aiPlayerInformationArray)
        .field('alternateRoutesArray', alternateRoutesArray)
        .field('checkpointInfoArray', checkpointInfoArray)

    if (PtrPath.includes('event_array.event_4')) {
        console.log(customChevronPtrArray);
    }

    PtrPath.pop();
    return offline_event;
}

export const BUILD_event_file = (obj: CleanKStruct<EVT>) => {
    EVENT_IMPORT_ARRAY.splice(0, EVENT_IMPORT_ARRAY.length)
    
    const event_file = Struct('event_file')
        .field(`header`, BUILD_genesys_object(obj.header))
        .field(`unknown_id`, u4(obj.unknownId));

    MAIN_EVENT_DATA = event_file;

    PUSH_EVENT_IMPORT(0xF8_FF_FF_FF, P32('header'));

    event_file
        .field(`event_start_offset`, P32('event_pointers'))
        .field(`event_count`, u4(obj.allEvents.length));
    
    const eventPointers = Struct('EventPointers');
    const allEvents = Struct('ALL_EVENTS');

    for (const [idx, switcher] of (obj.allEvents as EVT.Ptr[]).map(v => (v.data.data as EVT.EventSwitcher)).entries()) {
        if (switcher.offlineEvent) {
            PUSH_EVENT_IMPORT(0xF3_F3_05_00, P32(`event_array.event_${idx}`));            
            allEvents.field(`event_${idx}`, BUILD_offline_event(`event_array.event_${idx}`, switcher.offlineEvent));
         
        } else if (switcher.onlineEvent) {
            PUSH_EVENT_IMPORT(0x55_5D_04_00, P32(`event_array.event_${idx}`));
            allEvents.field(`event_${idx}`, BUILD_online_event(`event_array.event_${idx}`, switcher.onlineEvent)('oevt_uniqIdArr').oevent_online_event);

        } else if (switcher.onlineChallenge) { 
            PUSH_EVENT_IMPORT(0xC7_36_11_00, P32(`event_array.event_${idx}`));
            allEvents.field(`event_${idx}`, BUILD_online_challenge(`event_array.event_${idx}`, switcher.onlineChallenge));
         
        } else if (switcher.voteEvent) {
            PUSH_EVENT_IMPORT(0xC6_B2_17_00, P32(`event_array.event_${idx}`));
            allEvents.field(`event_${idx}`, BUILD_vote_event(`event_array.event_${idx}`, switcher.voteEvent));
         
        }

        
        eventPointers.field(`event_${idx}_ptr`, P32(`event_array.event_${idx}`));
    }

    event_file.field('event_pointers', eventPointers);
    event_file.field('event_array', allEvents);

    const currentSize = event_file.computeBufferSize();
    const bytesToPad = 0x10 - (currentSize % 0x10);

    if (bytesToPad > 0) {
        event_file.field('PRE_IMPORT_PADDING', U8s(new Array(bytesToPad)));
    }
    

    EVENT_IMPORT_ARRAY.sort((a, b) => {
        return (a.get('offset') as BaseField).get() - (b.get('offset') as BaseField).get()
    });
    for (const [idx, imp] of EVENT_IMPORT_ARRAY.entries()) {
        // console.log((imp.get('offset') as BaseField).get());
        
        const offsetField = (imp.get('offset') as BaseField);
        // offsetField.set(offsetField.get() | 0x80_00_00_00);

        const event_import = Struct('event_import')
            .field('ID', imp.get('ID'))
            .field('always-1', imp.get('always-1'))
            .field('offset', U32((offsetField.get() | 0x80_00_00_00) >>> 0, Endian.Little))
            .field('padding', U8s([0, 0, 0, 0]));

        event_file.field(`IMPORT_${idx}`, event_import);
    }

    return event_file.toUint8Array();
}
