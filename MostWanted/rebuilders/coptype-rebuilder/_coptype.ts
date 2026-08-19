import { BaseField, Endian, Pointer32 as _Pointer32, Struct, U32,U8s } from "construct-js";
import { GenericGenObject as GenObj } from "../../ParserStuff-LE/generic-gen-object";
import { CleanKStruct } from "../../helpers/recursiveOmit";
import { APPEND_genesys_object, AppendImportsToFile, f4, IMPORT_ARRAY, MAIN_STRUCT, NullableP32, P32, PtrPath, u1, u2, u4 } from "../../helpers/rebuilderAddins";

const BUILD_genesys__gen__gameplay__cop_type = (offsetName: string, obj: CleanKStruct<GenObj.GenesysGenGameplayCopType>) => {
    PtrPath.push(offsetName)

    const out = Struct('coptype')
    APPEND_genesys_object(out, obj.baseObject, 0xF9_FC_06_00)
    out
        .field("aiplayer_type_0xc", u4(obj.aiplayerType0xc))
        .field("game_changer_id_0x10", u4(obj.gameChangerId0x10))
        .field("can_spawn_ahead_0x14", u1(obj.canSpawnAhead0x14))
        .field("can_spawn_behind_0x15", u1(obj.canSpawnBehind0x15))
        .field("can_spawn_head_on_0x16", u1(obj.canSpawnHeadOn0x16))
        .field("can_spawn_intercepting_0x17", u1(obj.canSpawnIntercepting0x17))
        .field("bool8_t_0x18", u1(obj.bool8T0x18))
        .field("can_spawn_waiting_0x19", u1(obj.canSpawnWaiting0x19))
        .field("padding", U8s(new Array(2).fill(0)))

    PtrPath.pop()

    return out;
}

export const BUILD_FILE = (obj: CleanKStruct<GenObj.GenesysObjCollection>) => {
    IMPORT_ARRAY.splice(0, IMPORT_ARRAY.length)

    const coptypeFile = Struct('coptypesFile')
    MAIN_STRUCT[0] = coptypeFile;

    APPEND_genesys_object(coptypeFile, obj.baseObject, 0xF8_FF_FF_FF)

    coptypeFile
        .field('GameChangerID', u4(obj.unkId))
        .field('Item', P32('ctPtrs'))
        .field('ItemCount', u2(obj.objCollection?.length ?? 0))
        .field('padding', u2(0))


    const ctPtrs = Struct('ctPtrs');
    const allCopTypes = Struct('allCopTypes');

    if (obj.objCollection) {
        for (const [idx, itm] of obj.objCollection.entries()) {
            allCopTypes
                .field(`coptype_${idx}`, BUILD_genesys__gen__gameplay__cop_type(`coptypes.coptype_${idx}`, (itm.data.data as GenObj).data as GenObj.GenesysGenGameplayCopType));
            ctPtrs.field(`coptype_${idx}_ptr`, P32(`coptypes.coptype_${idx}`))
        }
    }

    coptypeFile.field('ctPtrs', ctPtrs);
    coptypeFile.field('coptypes', allCopTypes);

    const currentSize = coptypeFile.computeBufferSize();
    const bytesToPad = 0x10 - (currentSize % 0x10);

    if (bytesToPad > 0 && bytesToPad < 0x10) {
        coptypeFile.field('PRE_IMPORT_PADDING', U8s(new Array(bytesToPad)));
    }

    AppendImportsToFile();

    return coptypeFile.toUint8Array();
}
