meta:
  id: genesys_type
  endian: le
  encoding: ascii
  # 146165144147145160157160060061o
enums:
  e_native_type:
    0: {id: e_nativetype_integer}
    1: {id: e_nativetype_unsigned_integer}
    2: {id: e_nativetype_float}
    3: {id: e_nativetype_boolean}
    4: {id: e_nativetype_char}
    5: {id: e_nativetype_enumeration}
    6: {id: e_nativetype_object}
    7: {id: e_nativetype_genesysobject}
    8: {id: e_nativetype_resource_handle}
    9: {id: e_nativetype_resource_id}
    10: {id: e_nativetype_count}
  e_valuetype:
    0: {id: e_valuetype_value}
    1: {id: e_valuetype_pointer}
    2: {id: e_valuetype_array}
    3: {id: e_valuetype_offset}
    4: {id: e_valuetype_count}
seq:
  - {id: mu_genesys_version, type: u1}
  - {id: me_native_type, type: u1}
  - {id: mu_property_count, type: u2}
  - id: type_data
    type: 
      switch-on: me_native_type
      cases:
        5: genesys_nativetype_enumeration_data
        6: genesys_nativetype_object_data
        7: genesys_nativetype_object_data
        _: genesys_nativetype_object_data
instances:
  sizes:
    type: type_size_collection   
  native_type:
    type: 
      switch-on: me_native_type
      cases:
        0: "display_type('e_nativetype_integer')"
        1: "display_type('e_nativetype_unsigned_integer')"
        2: "display_type('e_nativetype_float')"
        3: "display_type('e_nativetype_boolean')"
        4: "display_type('e_nativetype_char')"
        5: "display_type('e_nativetype_enumeration')"
        6: "display_type('e_nativetype_object')"
        7: "display_type('e_nativetype_genesysobject')"
        8: "display_type('e_nativetype_resource_handle')"
        9: "display_type('e_nativetype_resource_id')"
        10: "display_type('e_nativetype_count')"
        _: "display_type('undocumented')"
types:
  type_size_collection:
    instances:
      genesys_type_hash:
        value: sizeof<genesys_type_hash>
      genesys_value_type:
        value: sizeof<genesys_value_type>
      genesys_property:
        value: sizeof<genesys_property>
      genesys_type_information:
        value: sizeof<genesys_type_information>
      genesys_type_entry:
        value: sizeof<genesys_type_entry>
      genesys_nativetype_object_data:
        value: sizeof<genesys_nativetype_object_data>
      genesys_nativetype_enumeration_data:
        value: sizeof<genesys_nativetype_object_data>

  genesys_type_hash:
    seq:
    - {id: hash, type: u4}
    - {id: padding, type: u4}
    - {id: value, type: f4}

    instances:
      name:
        type: 
          switch-on: hash
          cases: 
            0x0b3fe48a: "display_type('CgsResource.Handle')"
            0x0e2af381: "display_type('uint32_t')"
            0x12d46c62: "display_type('int32_t')"
            0x2edb25e7: "display_type('Genesys.Object')"
            0x40404301: "display_type('CgsCore.StringBase')"
            0x5246d78c: "display_type('bool8_t')"
            0x530a6d87: "display_type('float32_t')"
            0x8cfe579f: "display_type('char')"
            0x8eabc011: "display_type('uint8_t')"
            0xa32a93d6: "display_type('uint16_t')"
            0xb92285f2: "display_type('CgsCore.UniqueId')"
            0xbfd40c35: "display_type('int16_t')"
            _: "display_type('unknown')"       
  genesys_value_type:
    seq:
      - {id: value_flags, type: u1}
    instances:
      e_value_type_p1:
        value: (value_flags & 0b00000011)
      e_value_type_p2:
        value: (value_flags & 0b00001100) >> 2
      e_value_type_p3:
        value: (value_flags & 0b00110000) >> 4
      e_value_type_p4:
        value: (value_flags & 0b11000000) >> 6
  genesys_property:
    seq:
      - {id: mp_type_ptr, type: "ptr('genesys_type')"}
      - {id: mu_type_version, type: u4}
      - {id: mp_array_count_property_ptr, type: u4}
      - {id: mu_id, type: u4}
      - {id: mu_type_size, type: u4, doc: "size of each element in bytes"}
      - {id: mu_offset, type: u4, doc: "location of the property relative to type start"}
      - {id: mu_count, type: u2, doc: "number of elements"}
      - {id: mu_type_alignment, type: u1}
      - {id: m_value_type, type: genesys_value_type}
  genesys_type_information:
    seq:
      - {id: mp_name_ptr, type: ptr('strz')}
      - {id: mpa_property_names_ptr, type: ptr('strz')}
  genesys_type_entry:
    seq:
      - {id: type_hash_id, size: 0x8}
      - {id: position, type: u4}
      - {id: padding, size: 0x4}
  genesys_nativetype_object_data:
    seq:
      - {id: mp_base_type_ptr, type: u4}
      - {id: mu_base_type_version, type: u4}
      - {id: mpa_properties_ptr, type: "ptr_array('genesys_property', _parent.mu_property_count)"}
      - {id: mu_version, type: u4}
      - {id: mu_id, type: u4}
      - {id: mu_size, type: u4}
      - {id: ma_reserved, type: u1, repeat: expr, repeat-expr: 3}
      - {id: mu_alignment, type: u1}
      - {id: mu_type_info_ptr, type: "ptr('genesys_type_information')"}

  genesys_nativetype_enumeration_data:
    seq:
      - {id: mp_base_type_ptr, type: u4}
      - {id: mu_base_type_version, type: u4}
      - {id: mpa_properties_ptr, type: "ptr_array('genesys_property', _parent.mu_property_count)"}
      - {id: mu_version, type: u4}
      - {id: mu_id, type: u4}
      - {id: mu_size, type: u4}
      - {id: ma_reserved, type: u1, repeat: expr, repeat-expr: 3}
      - {id: mu_alignment, type: u1}
  

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
            '"genesys_type"': genesys_type
            '"genesys_property"': genesys_property
            '"genesys_type_information"': genesys_type_information
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