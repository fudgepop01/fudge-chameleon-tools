import { Endian, Pointer32, Struct, StructType, U16, U32, U32s, U8, U8s } from "construct-js";
import { Event as NfsEvent } from "../event";
import { GenesysObject } from "../genesys-object";
import { F32, F32s } from "../helpers/floatfield";

const buildGenesysObjectHeader = (obj: GenesysObject) => {
    return Struct('GenesysObjectHeader')
        .field('irrelevant', U32s([0, 0]))
        .field('muTypeVersion', U32(obj.muTypeVersion, Endian.Big));
}

// vpu_vector3
// weather_conditions
// temp_event_type
// multiplayer_race_type
// multiplayer_challenge_type
// genesys__gen__challenge_action__action_base__feedback_data
// genesys__gen__challenge_action__accumulation_helper_data
// type_finder_for_genesys__gen__challenge_action__action_base
// genesys__gen__challenge_action__action_base
// genesys__gen__challenge__challenge_part
// genesys__gen__challenge__location
// genesys__gen__chevron
const ChevronFactory = (obj: NfsEvent.GenesysGenChevron) => {
    const chevron = Struct('Chevron')
        .field("baseObject", buildGenesysObjectHeader(obj.baseObject))
        .field("gameChangerId_0xc", U32(obj.gameChangerId0xc))
        .field("roadSection_0x10", U32(obj.roadSection0x10))
        .field("shouldBlockStart_0x14", U8(obj.shouldBlockStart0x14))
        .field("padding", U8s([0, 0, 0]));

    return chevron;
}
// genesys__gen__custom_chevron
const CustomChevronFactory = (EventObj: StructType, prefix: string, obj: NfsEvent.GenesysGenCustomChevron) => {
    const floatArrayPtr0x10Ref = prefix + 'ccFloatArray1';
    const floatArrayPtr0x14Ref = prefix + 'ccFloatArray1';
    const floatArrayPtr0x18Ref = prefix + 'ccFloatArray1';

    const mainObj = Struct('CustomChevron')
        .field('baseObject', buildGenesysObjectHeader(obj.baseObject))
        .field('gameChangerId0xc', U32(obj.gameChangerId0xc))
        .field('floatArrayPtr0x10', Pointer32(EventObj, prefix + 'ccFloatArray1'))
        .field('floatArrayPtr0x14', Pointer32(EventObj, prefix + 'ccFloatArray2'))
        .field('floatArrayPtr0x18', Pointer32(EventObj, prefix + 'ccFloatArray3'))
        .field('arrayCountFor0x10', U16(obj.floatArray0x10.length))
        .field('arrayCountFor0x14', U16(obj.floatArray0x14.length))
        .field('arrayCountFor0x18', U16(obj.floatArray0x18.length))
        .field('invertNormal0x22', U8(obj.invertNormal0x22))
        .field('padding', U8s([0]))

    const floatArray1 = F32s(obj.floatArray0x10);
    const floatArray2 = F32s(obj.floatArray0x14);
    const floatArray3 = F32s(obj.floatArray0x18);

    return {
        CustomChevron: mainObj,
        [floatArrayPtr0x10Ref]: floatArray1,
        [floatArrayPtr0x14Ref]: floatArray2,
        [floatArrayPtr0x18Ref]: floatArray3 
    };
}
// genesys__gen__gameplay__condition
const GameplayConditionFactory = (usingObject: StructType, prefix: string, obj: NfsEvent.GenesysGenGameplayCondition) => {
    const stringsArrayID = prefix + "StringArray";
    const stringsArray = U32s(obj.stringStringsArray0xc);
    const referenceArrayID = prefix + "ReferenceArray";
    const referenceArray = U32s(obj.referenceArray0x14);
    const valuesArrayID = prefix + "ValuesArray";
    const valuesArray = U32s(obj.valuesArray0x18);
    
    const gameplayCondition = Struct('GameplayCondition')
        .field("base_object", buildGenesysObjectHeader(obj.baseObject))
        .field("strings_ptr_array_0xc", Pointer32(usingObject, stringsArrayID))
        .field("game_changer_id_0x10", U32(obj.gameChangerId0x10))
        .field("reference_ptr_array_0x14", Pointer32(usingObject, referenceArrayID))
        .field("values_ptr_array_0x18", Pointer32(usingObject, valuesArrayID))
        .field("test_type_val", U16(obj.testTypeVal)) // enum_55_31_0f_00
        .field("type_val", U16(obj.typeVal)) // enum_68_f1_0e_00
        .field("array_count_for_0x14", U16(obj.stringStringsArray0xc.length))
        .field("array_count_for_0xc", U16(obj.referenceArray0x14.length))
        .field("array_count_for_0x18", U16(obj.valuesArray0x18.length))
        .field("padding", U8s([0, 0]));

    return {
        [stringsArrayID]: stringsArray,
        [referenceArrayID]: referenceArray,
        [valuesArrayID]: valuesArray,
        gameplayCondition: gameplayCondition
    };
}
// genesys__gen__offline_event__ai_player_information
const AiPlayerInformationFactory = (obj: NfsEvent.GenesysGenOfflineEventAiPlayerInformation) => {
    const aiPlayerInformation = Struct('AiPlayerInformation')
        .field("base_object", buildGenesysObjectHeader(obj.baseObject))
        .field("ai_player_type_0xc", U32(obj.aiPlayerType0xc))
        .field("back_up_colour_0x10", U32(obj.backUpColour0x10))
        .field("placement_0x14", U32(obj.placement0x14))
        .field("primary_colour_0x18", U32(obj.primaryColour0x18))

    return aiPlayerInformation;
}
// genesys__gen__offline_event__alternate_routes
const AlternateRoutesFactory = (EventObj: StructType, prefix: string, obj: NfsEvent.GenesysGenOfflineEventAlternateRoutes) => {
    const routeMarkerArrayID = ;


    const alternateRoutes = Struct('AlternateRoute')
}
// genesys__gen__offline_event__checkpoint_info
// event_switcher
// event_base
const EventBaseFactory = (EventObj: StructType, obj: NfsEvent.EventBase) => {
    const customChevrons = [];
    for (let i = 0; i < obj.customChevronPtrArray.length; i++) {
        customChevrons.push(CustomChevronFactory(EventObj, `eb${i}`, obj.customChevronPtrArray[i].data.data as NfsEvent.GenesysGenCustomChevron));
    }
    
    // uniqueIdArray for now
    const ATCheckpointsID = 'autotestCheckpoints';
    const chevronListID = 'chevronList';
    const EventBase = Struct('EventBase')
        .field('baseObject', buildGenesysObjectHeader(obj.baseObject)) 
        .field('autotestCheckpoints0xc', obj.uniqueIdArray.length ? Pointer32(EventObj, ATCheckpointsID) : U32(0)) 
        .field('cinematicName0x10', U32(obj.cinematicName0x10)) 
        .field('description0x14', U32(obj.description0x14)) 
        .field('gameChangerId0x18', U32(obj.gameChangerId0x18, Endian.Big)) 
        .field('gameMode0x1c', U32(obj.gameMode0x1c, Endian.Big)) 
        .field('gamePack0x20', U32(obj.gamePack0x20)) 
        .field('uniqueId0x24', U32(obj.uniqueId0x24)) 
        .field('cycleTimeOfDay0x28', F32(obj.cycleTimeOfDay0x28)) 
        .field('finishTimeOfDay0x2c', F32(obj.finishTimeOfDay0x2c)) 
        .field('sunDirection0x30', F32(obj.sunDirection0x30)) 
        .field('timeOfDay0x34', F32(obj.timeOfDay0x34)) 
        .field('float0x38', F32(obj.float0x38)) 
        .field('chevronList0x3c', customChevrons.length ? Pointer32(EventObj, chevronListID) : U32(0)) 
        .field('roadSurfaceConditions', U16(obj.roadSurfaceConditions)) 
        .field('arrayCountFor0xc', U16(obj.uniqueIdArray.length)) 
        .field('isAlternativeWeather0x44', U8(obj.isAlternativeWeather0x44)) 
        .field('isRainActive0x45', U8(obj.isRainActive0x45)) 
        .field('isThunderActive0x46', U8(obj.isThunderActive0x46)) 
        .field('overrideSunDirection0x47', U8(obj.overrideSunDirection0x47)) 
        .field('bool0x48', U8(obj.bool0x48))
        .field('arrayCountFor0x3c', U8(customChevrons.length)) 
        .field('uint8_0x4a', U8(obj.uint80x4a)) 
        .field('padding', U8s([0]));

    return {
        [ATCheckpointsID]: obj.uniqueIdArray,
        [chevronListID]: customChevrons,
        eventBase: EventBase
    };
}

// online_event
// online_challenge
// genesys__gen__challenge_action__accumulate_distance
// genesys__gen__challenge_action__accumulate_near_misses
// genesys__gen__challenge_action__accumulate_takedowns
// genesys__gen__challenge_action__accumulate_time
// genesys__gen__challenge_action__car_state
// genesys__gen__challenge_action__coop_accumulate_distance
// genesys__gen__challenge_action__do_jump
// genesys__gen__challenge_action__get_to_location
// genesys__gen__challenge_action__hit_trigger
// genesys__gen__challenge_action__jump_over_players
// genesys__gen__challenge_action__jump_stats
// genesys__gen__challenge_action__speed_camera_action
// genesys__gen__challenge_action__speed_run
// vote_event
// offline_event
const OfflineEventFactory = (obj: NfsEvent.OfflineEvent) => {
    const overallEventData = Struct('OverallEventData');
    
    const EventBaseData = EventBaseFactory(overallEventData, obj.baseObject);
    
    const additionalAssets = U32s(obj.additionalAssets0x54);
    const aiHints = U32s(obj.aiHints0x58);
    const checkpoints = U32s(obj.checkpoints0x64);
    const defaultHeatLevels = U32s(obj.defaultHeatLevels0x6c);
    const gameplayTriggers = U32s(obj.gameplayTriggers0x7c);
    const timeline = U32s(obj.timeline0xa0);
    const targetSpeed = F32s(obj.targetSpeed0xa8);
    const targetTime = F32s(obj.targetTime0xac);
    
    const chevronData = [];
    for (let i = 0; i < obj.chevronPtrArray0xb4.length; i++) {
        chevronData.push(ChevronFactory(obj.chevronPtrArray0xb4[i].data.data as NfsEvent.GenesysGenChevron));
    }

    const customChevrons = [];
    for (let i = 0; i < obj.customChevronPtrArray0xb8.length; i++) {
        chevronData.push(CustomChevronFactory(overallEventData, `${i}`, obj.customChevronPtrArray0xb8[i].data.data as NfsEvent.GenesysGenCustomChevron));
    }

    const gameplayConditions = [];
    for (let i = 0; i < obj.gameplayConditionPtrArray0xbc.length; i++) {
        gameplayConditions.push(GameplayConditionFactory(overallEventData, `${i}`, obj.gameplayConditionPtrArray0xbc[i].data.data as NfsEvent.GenesysGenGameplayCondition));
    }

    const aiPlayerInformation = [];
    for (let i = 0; i < obj.aiPlayerInformationArray0xc0.length; i++) {
        aiPlayerInformation.push(AiPlayerInformationFactory(obj.aiPlayerInformationArray0xc0[i]));
    }

    const alternateRoutes = [];
    for (let i = 0; i < obj.alternateRoutes0xc4.length; i++) {
        aiPlayerInformation.push();
    }

    const output = Struct('OfflineEvent')
        .field()
    
        
}

const buildEventsFile = (obj: NfsEvent) => {
    const top = Struct('EventFile')
        .field('header', buildGenesysObjectHeader(obj.header))
        .field('unknownId', U32(obj.unknownId))
        .field('eventStartOffset', U32(obj.eventStartOffset))
        .field('eventCount', U32(obj.eventCount))



    
    const events = [];
    for (const [idx, switcher] of obj.allEvents.map(v => (v.data.data as NfsEvent.EventSwitcher)).entries()) {
        if (switcher.voteEvent) {
            const voteEvent = switcher.voteEvent;
        }
        else if (switcher.offlineEvent) {
            const offlineEvent = switcher.offlineEvent;
        }
        else if (switcher.onlineEvent) {
            const onlineEvent = switcher.onlineEvent;
        } 
        else if (switcher.onlineChallenge) {
            const onlineChallenge = switcher.onlineChallenge;
        }
    }

    
}