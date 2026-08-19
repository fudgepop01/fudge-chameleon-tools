import { Endian, Pointer32 as _Pointer32, Struct, StructType, U16, U32, U8, U8s, I8, I16, I32, U32s, U16s, I16s, I32s, I8s, BaseField } from "construct-js";
import { F32, F32s } from "./floatfield";
import { CleanKStruct } from "./recursiveOmit";
import { GenericGenObject } from "../generic-gen-object";

export const FLIP_DEFAULT_ENDIANNESS = () => {
    const _temp = Endian['Little'];
    (Endian as any)['Little'] = Endian['Big'];
    (Endian as any)['Big'] = _temp;
}


export const IMPORT_ARRAY: StructType[] = [];
export let MAIN_STRUCT: StructType[] = [undefined];
export let PtrPath: string[] = [];

const u2le = (val) => U16(val, Endian.Little);
const u4le = (val) => U32(val, Endian.Little);
const s2le = (val) => I16(val, Endian.Little);
const s4le = (val) => I32(val, Endian.Little);
const f4le = (val) => F32(val, Endian.Little);
const s16sle = (vals) => I16s(vals, Endian.Little);
const s32sle = (vals) => I32s(vals, Endian.Little);
const u16sle = (vals) => U16s(vals, Endian.Little);
const u32sle = (vals) => U32s(vals, Endian.Little);
const f32sle = (vals) => F32s(vals, Endian.Little);

const u2be = (val) => U16(val, Endian.Big);
const u4be = (val) => U32(val, Endian.Big);
const s2be = (val) => I16(val, Endian.Big);
const s4be = (val) => I32(val, Endian.Big);
const f4be = (val) => F32(val, Endian.Big);
const s16sbe = (vals) => I16s(vals, Endian.Big);
const s32sbe = (vals) => I32s(vals, Endian.Big);
const u16sbe = (vals) => U16s(vals, Endian.Big);
const u32sbe = (vals) => U32s(vals, Endian.Big);
const f32sbe = (vals) => F32s(vals, Endian.Big);

export const Endianness = {
    primary: Endian.Little,
    secondary: Endian.Big
}

export const u1 = (val: number) => U8(val);
export const u2 = (val: number) => U16(val, Endianness.primary);
export const u4 = (val: number) => U32(val, Endianness.primary);
export const s1 = (val: number) => I8(val);
export const s2 = (val: number) => I16(val, Endianness.primary);
export const s4 = (val: number) => I32(val, Endianness.primary);
export const f4 = (val: number) => F32(val, Endianness.primary);
export const u1s = (val: number[]) => U8s(val);
export const u2s = (val: number[]) => U16s(val, Endianness.primary);
export const u4s = (val: number[]) => U32s(val, Endianness.primary);
export const s1s = (val: number[]) => I8s(val);
export const s2s = (val: number[]) => I16s(val, Endianness.primary);
export const s4s = (val: number[]) => I32s(val, Endianness.primary);
export const f4s = (val: number[]) => F32s(val, Endianness.primary);

PtrPath.toString = () => {
    return PtrPath.join('.');
}

export const flattenPtrPath = () => {
    return PtrPath.toString().replace(/\./g, '__');
}

export const P32 = (offsetName: string, pathOffset?: number, pathReplacement?: string) => {
    if (PtrPath.length === 0 || PtrPath.slice(0, pathOffset).length === 0) {
        return _Pointer32(MAIN_STRUCT[0], offsetName, Endianness.primary);
    }
    let pPath = PtrPath.slice(0, pathOffset).join('.').replace(/\.\./g, '.');
    if (pathReplacement) {
        pPath += '.' + pathReplacement;
    }
    pPath += '.' + offsetName;
    return _Pointer32(MAIN_STRUCT[0], pPath, Endianness.primary);
}

export const NullableP32 = (isDefined: number | object | undefined, name: string, pathOffset?: number) => {
    return isDefined ? P32(name, pathOffset) : u4(0);
}

export const PUSH_IMPORT = (ImportID: number, _P32: ReturnType<typeof _Pointer32>) => {
    const event_import = Struct('event_import_base')
        .field('ID', U32(ImportID, Endianness.secondary))
        .field('always-1', U32(0x1, Endianness.secondary))
        .field('offset', _P32)
        .field('padding', U8s([0, 0, 0, 0]));

    IMPORT_ARRAY.push(event_import);
}

export const APPEND_genesys_object = (builder: StructType, obj: CleanKStruct<GenericGenObject.GenObj>, id?: number, pathOffset?: number, newPath?: string) => {
    // if (newPath) PtrPath.push(newPath);

    builder
        .field('dynamicData', U8s(new Array(8).fill(0)))
        .field('muID', U32(obj.muTypeVersion, Endianness.secondary));
    
    if (id) {
        if (pathOffset && newPath) {
            PUSH_IMPORT(id, P32('dynamicData', pathOffset ?? 0, newPath ?? undefined))
        } else {
            PUSH_IMPORT(id, P32('dynamicData'))
        }
    }
    
    // if (newPath) PtrPath.pop();
}

export const AppendImportsToFile = () => {
    IMPORT_ARRAY.sort((a, b) => {
        return (a.get('offset') as BaseField).get() - (b.get('offset') as BaseField).get()
    });
    for (const [idx, imp] of IMPORT_ARRAY.entries()) {
        const offsetField = (imp.get('offset') as BaseField);

        const aip_import = Struct('aip_import')

        if (Endianness.primary === Endian.Big) {
            aip_import
                .field('always-1', imp.get('always-1'))
                .field('ID', imp.get('ID'))
        } else {
            aip_import
                .field('ID', imp.get('ID'))
                .field('always-1', imp.get('always-1'))
        }
        aip_import
            .field('offset', U32((offsetField.get() | 0x80_00_00_00) >>> 0, Endianness.primary))
            .field('padding', U8s([0, 0, 0, 0]));

        MAIN_STRUCT[0].field(`IMPORT_${idx}`, aip_import);
    }
}