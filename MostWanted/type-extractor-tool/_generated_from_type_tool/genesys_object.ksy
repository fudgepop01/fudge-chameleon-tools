meta:
  id: genesys_object
  endian: le
  encoding: ascii
  # 146165144147145160157160060061o
seq:
    # CTRLD- cgs_resource_handle

  - {id: mp_type, type: cgs_resource_handle}
    # CTRLD- u4be

  - {id: mu_type_version, type: u4be}
types: 
  cgs_resource_type_v2:
    seq:
        # CTRLD- ptr('u4')

      - {id: vtable, type: ptr('u4')}
        # CTRLD- u1

      - {id: mb_memory_overridden, type: u1}
        # CTRLD- str

      - {id: mac_debug_type_name, type: str, size: 31}
        # CTRLD- u4

      - {id: mu_type_id, type: u4}
        # CTRLD- u4

      - {id: mau_memory_alignment, type: u4, repeat: expr, repeat-expr: 4}
  cgs_mem_address:
    seq:
        # CTRLD- ptr('u4')

      - {id: map_data, type: ptr('u4'), repeat: expr, repeat-expr: 4}
  cgs_mem_descriptor:
    seq:
        # CTRLD- u4

      - {id: mau_sizes, type: u4, repeat: expr, repeat-expr: 4}
        # CTRLD- u4

      - {id: mau_alignments, type: u4, repeat: expr, repeat-expr: 4}
  cgs_resource_id:
    seq:
      - {id: m_hash, size: 0x8}
  cgs_resource_pool_entry:
    seq:
        # CTRLD- cgs_resource_id

      - {id: m_id, type: cgs_resource_id}
        # CTRLD- cgs_mem_descriptor

      - {id: m_descriptor, type: cgs_mem_descriptor}
        # CTRLD- cgs_mem_address

      - {id: m_address, type: cgs_mem_address}
        # CTRLD- "ptr('cgs_resource_type_v2')"

      - {id: mp_resource_type, type: "ptr('cgs_resource_type_v2')"}
        # CTRLD- u4

      - {id: mu_import_table_offset, type: u4}
        # CTRLD- u2

      - {id: mau_heap_indices, type: u2, repeat: expr, repeat-expr: 4}
      
  cgs_resource_handle:
    seq:
        # CTRLD- "ptr('cgs_resource_pool_entry')"

      - {id: mp_entry, type: "ptr('cgs_resource_pool_entry')"}
        # CTRLD- u4

      - {id: mu_offset, type: u4}
  cgs_resource_thandle:
    seq:
        # CTRLD- cgs_resource_handle

      - {id: handle, type: cgs_resource_handle}

  dummy:
    instances:
      d:
        value: '"dummy"'
  atype:
    params:
      - id: dtype
        type: str
    seq:
      - id: data
        type: 
          switch-on: dtype
          cases:
            '"cgs_resource_pool_entry"': cgs_resource_pool_entry
            '"cgs_resource_type_v2"': cgs_resource_type_v2
            '"f4"': f4
            '"u1"': u1
            '"u2"': u2
            '"u4"': u4
            '"s1"': s1 
            '"s2"': s2 
            '"s4"': s4
            '"strz"': strz
            _: dummy
  ptr:
    params:
      - id: dtype
        type: str
    seq:
      - id: offset
        type: s4
    instances:
      data:
        if: offset != 0
        pos: offset
        type: atype(dtype)
  ptr_array:
    params:
      - id: dtype
        type: str
      - id: amt
        type: s4
    seq:
      - id: offset
        type: s4
    instances:
      entries:
        pos: offset
        repeat: expr
        repeat-expr: amt
        type: atype(dtype)
        
  ptr_table:
    params:
      - id: dtype
        type: str
      - id: amt
        type: s4
    seq:
      - id: entries
        repeat: expr
        repeat-expr: amt
        type: ptr(dtype)
        
  ptr_ptr:
    params:
      - id: dtype
        type: str
    seq:
      - id: offset
        type: s4
    instances:
      ptr:
        if: offset != 0
        pos: offset
        type: ptr(dtype)

  ptr_ptr_table:
    params:
      - id: dtype
        type: str
      - id: amt
        type: s4
    seq:
      - id: offset
        type: s4
      - id: count
        type: u4
        if: amt == 0
    instances:
      len:
        value: |
          amt == -1 ? 0 
          : amt == 0 ? count 
          : amt
      ptr_table:
        if: offset != 0
        pos: offset
        type: "ptr_table(dtype, len)"