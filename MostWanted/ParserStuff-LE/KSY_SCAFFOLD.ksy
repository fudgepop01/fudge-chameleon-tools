meta:
  id: $$NAME$$
  endian: le
  encoding: ascii
  # 146165144147145160157160060061o
# $$DATA$$
  
  string_base:
    seq:
      - id: save_ofs
        size: 0
        if: buf_ofs < 0
      - id: ofs_arr_buffer_0x0
        type: u4
      - id: array_count_for_0x0
        type: u4
        doc: '"Capacity"'
    instances:
      buf_ofs:
        value: _io.pos
      inst_buffer_0x0:
        pos: buf_ofs + ofs_arr_buffer_0x0
        type: str
        size: array_count_for_0x0
      size:
        value: 12
      mu_version_hash:
        value: 0x95_fb_ea_be

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
            # $$SWITCHER_TYPES$$
            '"string_base"': string_base

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