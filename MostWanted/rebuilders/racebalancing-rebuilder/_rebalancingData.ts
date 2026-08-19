import { BaseField, Endian, Pointer32 as _Pointer32, Struct, U32,U8s, U32s } from "construct-js";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import { CleanKStruct } from "../../helpers/recursiveOmit";
import { APPEND_genesys_object, AppendImportsToFile, f4, flattenPtrPath, IMPORT_ARRAY, MAIN_STRUCT, NullableP32, P32, PtrPath, s1, s2, u1, u2, u4 } from "../../helpers/rebuilderAddins";

const BUILD_genesys__gen__balancing_data__opponent_balancing_data = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenRaceBalancingDataOpponentBalancingData>) => {
    PtrPath.push(offsetName)
    
    const out = Struct('opponent_data');
    APPEND_genesys_object(out, obj.baseObject, 0x1B_33_00_00);
    out
      .field('game_changer_id_0xc', u4(obj.gameChangerId0xc))
      .field('ahead_distance_0x10', f4(obj.aheadDistance0x10))
      .field('behind_distance_0x14', f4(obj.behindDistance0x14))
      .field('end_cutoff_ratio_0x18', f4(obj.endCutoffRatio0x18))
      .field('end_speed_value_ahead_0x1c', f4(obj.endSpeedValueAhead0x1c))
      .field('end_speed_value_behind_0x20', f4(obj.endSpeedValueBehind0x20))
      .field('start_cutoff_ratio_0x24', f4(obj.startCutoffRatio0x24))
      .field('start_speed_value_ahead_0x28', f4(obj.startSpeedValueAhead0x28))
      .field('start_speed_value_behind_0x2c', f4(obj.startSpeedValueBehind0x2c))

    PtrPath.pop()
    return out;
}

const BUILD_genesys__gen__balancing_data = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenRaceBalancingData>) => {
    PtrPath.push(offsetName)

    const instOpponentData0x18 = Struct('opponentData');
    if (obj.instOpponentData0x18) {
        PtrPath.push('instOpponentData0x18');
        for (const [idx, data] of obj.instOpponentData0x18.entries()) {
            instOpponentData0x18
                .field(`data_${idx}`, BUILD_genesys__gen__balancing_data__opponent_balancing_data(`data_${idx}`, data));
        }
        PtrPath.pop();
    }

    const out = Struct('balancing_data');
    APPEND_genesys_object(out, obj.baseObject, 0xD3_29_00_00);
    out
        .field('game_changer_id_0xc', u4(obj.gameChangerId0xc))
        .field('extra_crash_schedule_time_0x10', f4(obj.extraCrashScheduleTime0x10))
        .field('extra_schedule_time_0x14', f4(obj.extraScheduleTime0x14))
        .field('ptr_arr_opponent_data_0x18', u4(obj.ptrArrOpponentData0x18))
        // doc: '"OpponentDataCount"'
        .field('array_count_for_0x18', u2(obj.instOpponentData0x18?.length ?? 0))
        .field('padding', U8s(new Array(2).fill(0)))

    // instances
    out
        .field('instOpponentData0x18', instOpponentData0x18)

    PtrPath.pop()
    return out;
}

export const BUILD_FILE = (obj: CleanKStruct<GenObj.GenesysGenRaceBalancingData>) => {
    IMPORT_ARRAY.splice(0, IMPORT_ARRAY.length)

    const RaceBalancingFile = Struct('raceBalancingFile')
    MAIN_STRUCT[0] = RaceBalancingFile;

    RaceBalancingFile.field('data', BUILD_genesys__gen__balancing_data('data', obj));

    const currentSize = RaceBalancingFile.computeBufferSize();
    const bytesToPad = 0x10 - (currentSize % 0x10);

    if (bytesToPad > 0 && bytesToPad < 0x10) {
        RaceBalancingFile.field('PRE_IMPORT_PADDING', U8s(new Array(bytesToPad)));
    }

    AppendImportsToFile();

    return RaceBalancingFile.toUint8Array();
}
