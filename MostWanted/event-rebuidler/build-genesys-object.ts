import { Endian, Pointer32, RawString, Struct, StructType, U16, U32, U32s, U8, U8s } from "construct-js";
import { GenesysObject } from "../parse-genesys-object";
import { CleanKStruct } from "../helpers/recursiveOmit";
//(.+)-.+type:(.+?)[,}]

// $1  # CTRLD-$2
// $0

const u1 = U8;
const u2 = U16;
const u4 = U32;

// const BUILD_cgs_resource_type_v2 = (obj: GenesysObject.CgsResourceTypeV2, ctx?: string) => {
//     // const vtable_ptr_field = Struct('vtable-ptr-field')

//     // if (obj.vtable.offset)
//     //     vtable_ptr_field
//     //         .field('vtable-from-ptr', obj.vtable.offset ?  );
    
//     const cgs_resource_type_v2 = Struct('cgs_resource_type_v2')
//         .field('vtable', U32(0)) // ptr('u4')
//         .field('mb_memory_overridden', U8(obj.mbMemoryOverridden)) // u1
//         .field('mac_debug_type_name', RawString(obj.macDebugTypeName.padEnd(31, '\0'))) // str
//         .field('mu_type_id', U32(obj.muTypeId)) // U32
//     for (const [idx, val] of obj.mauMemoryAlignment.entries()) {
//         cgs_resource_type_v2
//             .field(`mau_memory_alignment_${idx}`, U32(val)) // U32
//     }

//     return cgs_resource_type_v2;
// }

// const BUILD_cgs_mem_address = (obj: GenesysObject.CgsMemAddress, ctx?: string) => {
//     const cgs_mem_address = Struct('cgs_mem_address')
//         // .field('map_data', obj.mapData) // U32 ptr('u4')
//         .field('map_data', U32(0));

//     return cgs_mem_address;
// }

// const BUILD_cgs_mem_descriptor = (obj: GenesysObject.CgsMemDescriptor, ctx?: string) => {
//     const cgs_mem_descriptor = Struct('cgs_mem_descriptor');
//     for (const [idx, size] of obj.mauSizes.entries()) {
//         cgs_mem_descriptor
//             .field(`mau_sizes_${idx}`, u4(size)) // U32
//     }
//     for (const [idx, alignment] of obj.mauAlignments.entries()) {
//         cgs_mem_descriptor
//            .field(`mau_alignments_${idx}`, u4(alignment)) // U32
//     }

//     return cgs_mem_descriptor;
// }

// const BUILD_cgs_resource_id = (obj: GenesysObject.CgsResourceId, ctx?: string) => {
//     const cgs_resource_id = Struct('cgs_resource_id')
//         .field('m_hash', U8s(Array.from(obj.mHash))) // size 0x8

//     return cgs_resource_id;
// }

// const BUILD_cgs_resource_pool_entry = (obj: GenesysObject.CgsResourcePoolEntry, ctx?: string) => {
    
//     let resourceType: StructType = undefined;
//     const cgs_resource_pool_entry = Struct('cgs_resource_pool_entry')
//         .field('m_id', BUILD_cgs_resource_id(obj.mId, ctx)) // cgs_resource_id
//         .field('m_descriptor', BUILD_cgs_mem_descriptor(obj.mDescriptor, ctx)) // cgs_mem_descriptor
//         .field('m_address', BUILD_cgs_mem_address(obj.mAddress, ctx)) // cgs_mem_address
    
//     if (obj.mpResourceType.offset) {
//         resourceType = BUILD_cgs_resource_type_v2(obj.mpResourceType.data.data as GenesysObject.CgsResourceTypeV2, ctx);

//         cgs_resource_pool_entry
//             .field('mp_resource_type', Pointer32(cgs_resource_pool_entry, 'resource_type')) // U32 "ptr('cgs_resource_type_v2')"
//     }
//     cgs_resource_pool_entry
//         .field('mu_import_table_offset', u4(obj.muImportTableOffset)) // U32
    
//     for (const [idx, entry] of obj.mauHeapIndices.entries())
//         cgs_resource_pool_entry
//             .field(`entry_mau_heap_indices_${idx}`, u2(entry)) // U16

//     if (resourceType) {
//         cgs_resource_pool_entry
//             .field('resource_type', resourceType);
//     }
// }

// const BUILD_cgs_resource_handle = (obj: GenesysObject.CgsResourceHandle, ctx?: string) => {
//     const cgs_resource_handle = Struct('cgs_resource_handle')
//         .field('mp_entry', obj.mpEntry) // U32 "ptr('cgs_resource_pool_entry')"
//         .field('mu_offset', obj.muOffset) // U32

// }

// const BUILD_cgs_resource_thandle = (obj: GenesysObject.CgsResourceThandle, ctx?: string) => {
//     const cgs_resource_thandle = Struct('cgs_resource_thandle')
//         .field('handle', obj.handle) // cgs_resource_handle
// }

export const BUILD_genesys_object = (obj: CleanKStruct<GenesysObject>) => {
    // always 0 in the games
    const genesys_object = Struct('genesys_object')
        .field('mp_type_0', u4(0))
        .field('mp_type_1', u4(0))
        .field('mu_type_version', u4(obj.muTypeVersion, Endian.Big));

    return genesys_object;
}