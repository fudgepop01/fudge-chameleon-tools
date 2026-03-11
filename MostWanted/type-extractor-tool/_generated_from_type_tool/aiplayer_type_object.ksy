meta:
  id: aiplayer_type_object
  endian: le
  encoding: ascii
  # 146165144147145160157160060061o
  imports:
    - genesys_object
    - all
seq:
  - {id: header, type: genesys_object}
  - {id: unknown_id, type: u4}
  - {id: collection_start_offset, type: "u4"}
  - {id: collection_count, type: "u4"}
instances:
  all_player_types:
    pos: collection_start_offset
    type: ptr('all')
    repeat: expr
    repeat-expr: collection_count

types:
  dummy:
    instances:
      d:
        value: '"dummy"'
  display_type:
    params:
      - id: type_to_display
        type: str
    instances:
      type_name:
        value: type_to_display

  atype:
    params:
      - id: dtype
        type: str
    seq:
      - id: data
        type: 
          switch-on: dtype
          cases:
            '"all"': all

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

  # ptr:
  #   params:
  #     - id: dtype
  #       type: str
  #   seq:
  #     - id: offset
  #       type: s4
  #   instances:
  #     data:
  #       if: offset != 0
  #       pos: offset
  #       type: atype(dtype)
  
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