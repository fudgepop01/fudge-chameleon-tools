meta:
  id: hsm
  endian: le
  encoding: ascii
  # 146165144147145160157160060061o
seq:
  - {id: mi_version_number0x0, type: s4, doc: "Version number _ 3"}
  - {id: ptr_ma_top_state_definitions0x4, type: u4, doc: "Top-level state definitions"}
  - {id: mi_num_top_state_definitions0x8, type: s4, doc: "Number of top-level state definitions"}
  - {id: ptr_ma_state_definitions0xc, type: u4, doc: "State definitions"}
  - {id: mi_num_state_definitions0x10, type: s4, doc: "Number of state definitions"}
  - {id: ptr_ma_data_definitions0x14, type: u4, doc: "Data definitions"}
  - {id: mi_num_data_definitions0x18, type: s4, doc: "Number of data definitions"}
  - {id: ptr_ma_behaviour_interfaces0x1c, type: u4, doc: "Behaviour interfaces"}
  - {id: mi_num_behaviour_interfaces0x20, type: s4, doc: "Number of behaviour interfaces"}
instances:
  top_state_definitions:
    pos: ptr_ma_top_state_definitions0x4
    type: game__game_logic__hsm_data__hsm_top_state_definition
    repeat: expr
    repeat-expr: mi_num_top_state_definitions0x8
  state_definitions:
    pos: ptr_ma_state_definitions0xc
    type: game__game_logic__hsm_data__hsm_state_definition
    repeat: expr
    repeat-expr: mi_num_state_definitions0x10
  data_definitions:
    pos: ptr_ma_data_definitions0x14
    type: game__game_logic__hsm_data__hsm_data_definition
    repeat: expr
    repeat-expr: mi_num_data_definitions0x18
  behaviour_interfaces:
    pos: ptr_ma_behaviour_interfaces0x1c
    type: game__game_logic__hsm_data__hsm_behaviour_interface
    repeat: expr
    repeat-expr: mi_num_behaviour_interfaces0x20

enums:
  e_fallback_behaviour:
    0: run_children
    1: exit
    2: assert_then_exit
    3: count

  e_hsm_action:
    0: nothing
    1: child
    2: exit
    3: hsm_action_count

  e_hsm_param_type:
    0: string
    1: int
    2: float
    3: id
    4: bool
    5: asset_reference
    6: structure
    7: invalid

types:
  game__game_logic__hsm_data__hsm_top_state_definition:
    seq:
    - {id: m_top_state_definition_id0x0, type: game__game_logic__state_definition_id, doc: "Definition ID" }
    - {id: m_top_state_behaviour_id0x4, type: game__game_logic__state_behaviour_id, doc: "Behaviour ID" }
    - {id: m_top_state_instance_id0x8, type: game__game_logic__state_instance_id, doc: "Instance ID" }

  game__game_logic__hsm_data__hsm_state_definition:
    seq:
    - {id: m_state_behaviour_id0x0, type: game__game_logic__state_behaviour_id, doc: "State behaviour ID" }
    - {id: m_state_definition_id0x4, type: game__game_logic__state_definition_id, doc: "State definition ID" }
    - {id: ptr_ma_state_entry_points0x8, type: u4, doc: "State entry points" }
    - {id: ptr_ma_child_exit_data0xc, type: u4, doc: "Child exit data" }
    - {id: ptr_ma_parameters0x10, type: u4, doc: "Parameters" }
    - {id: mp_data_definition0x14, type: ptr('game__game_logic__hsm_data__hsm_data_definition'), doc: "Data definition" }
    - {id: mpc_debug_state_definition_name0x18, type: ptr('strz'), doc: "Name" }
    - {id: mu_num_parameters0x1c, type: u1, doc: "Number of parameters" }
    - {id: mu_fallback_behaviour0x1d, type: u1, doc: "Fallback behaviour; See EFallbackBehaviour" }
    - {id: mu_num_state_entry_points0x1e, type: u1, doc: "Number of state entry points" }
    - {id: mu_num_children0x1f, type: u1, doc: "Number of children" }
    instances:
      state_entry_points:
        pos: ptr_ma_state_entry_points0x8
        type: game__game_logic__hsm_data__hsm_state_entry_point
        repeat: expr
        repeat-expr: mu_num_state_entry_points0x1e
      child_exit_data:
        pos: ptr_ma_child_exit_data0xc
        type: game__game_logic__hsm_data__hsm_child_exit_data
        repeat: expr
        repeat-expr: mu_num_children0x1f
      parameters:
        pos: ptr_ma_parameters0x10
        type: game__game_logic__hsm_data__hsm_parameter
        repeat: expr
        repeat-expr: mu_num_parameters0x1c

  game__game_logic__hsm_data__hsm_data_definition:
    seq:
    - {id: m_data_definition_id0x0, type: game__game_logic__data_definition_id, doc: "ID"}
    - {id: mpc_path0x4, type: ptr('strz'), doc: "Path"}
    - {id: mp_data0x8, type: ptr('strz'), doc: "Data"}
    - {id: mu_data_size0xc, type: u4, doc: "Data size"}
    - {id: mpc_debug_data_definition_name0x10, type: ptr('strz'), doc: "Name"}

  game__game_logic__hsm_data__hsm_behaviour_interface:
    seq:
    - { id: m_behaviour_interface_id0x0, type: cgs_id, doc: "Behaviour ID" }
    - { id: mpc_debug_name0x8, type: ptr('strz'), doc: "Name" }
    - { id: ptr_ma_entry_point_ids0xc, type: u4, doc: "Entry point IDs" }
    - { id: ptr_ma_exit_point_ids0x10, type: u4, doc: "Exit point IDs" }
    - { id: ptr_ma_parameters0x14, type: u4, doc: "Parameters" }
    - { id: mi_num_parameters0x18, type: s4, doc: "Number of parameters" }
    - { id: mi_num_entry_points0x1c, type: s2, doc: "Number of entry points" }
    - { id: mi_num_exit_points0x1e, type: s2, doc: "Number of exit points" }
    instances:
      entry_point_ids:
        pos: ptr_ma_entry_point_ids0xc
        type: cgs_id
        repeat: expr
        repeat-expr: mi_num_entry_points0x1c
      exit_point_ids: 
        pos: ptr_ma_exit_point_ids0x10
        type: cgs_id
        repeat: expr
        repeat-expr: mi_num_exit_points0x1e
      parameters:
        pos: ptr_ma_parameters0x14
        type: game__game_logic__hsm_data__hsm_parameter
        repeat: expr
        repeat-expr: mi_num_parameters0x18

  game__game_logic__hsm_data__hsm_state_entry_point:
    seq:
    - { id: m_entry_point_id0x0, type: game__game_logic__state_entry_point_id, doc: "Entry point ID" }
    - { id: mu_action0x8, type: u1, doc: "Action; See EHSMActio" }
    - { id: mu_num_children0x9, type: u1, doc: "Number of children" }
    - { id: padding, size: 2 }
    - { id: ptr_ma_child_spawn_data0xc, type: u4, doc: "Child state spawn data" }
    instances:
      child_spawn_data:
        pos: ptr_ma_child_spawn_data0xc
        type: game__game_logic__hsm_data__hsm_state_spawn_data
        repeat: expr
        repeat-expr: mu_num_children0x9

  game__game_logic__hsm_data__hsm_state_spawn_data:
    seq:
    - { id: m_entry_point_id0x0, type: game__game_logic__state_entry_point_id, doc: "Entry point ID" }
    - { id: m_state_definition_id0x8, type: game__game_logic__state_definition_id, doc: "State definition ID" }
    - { id: mpc_debug_state_definition_name0xc, type: ptr('strz'), doc: "State definition name" }

  game__game_logic__hsm_data__hsm_child_exit_data:
    seq:
    - { id: m_child_state_definition_id0x0, type: game__game_logic__state_definition_id, doc: "Child state definition ID" }
    - { id: ptr_ma_child_exit_point_data0x4, type: u4, doc: "Child exit points" }
    - { id: mi_num_child_exit_points0x8, type: s4, doc: "Number of child exit points" }
    - { id: mpc_debug_state_definition_name0xc, type: ptr('strz'), doc: "State definition name" }
    instances:
      child_exit_points:
        pos: ptr_ma_child_exit_point_data0x4
        type: game__game_logic__hsm_data__hsm_child_exit_point_data
        repeat: expr
        repeat-expr: mi_num_child_exit_points0x8
  
  game__game_logic__hsm_data__hsm_child_exit_point_data:
    seq:
    - { id: m_parent_exit_point_id0x0, type: game__game_logic__state_exit_point_id, doc: "Parent exit point ID" }
    - { id: m_child_exit_point_id0x8, type: game__game_logic__state_exit_point_id, doc: "Child exit point ID" }
    - { id: mu_action0x10, type: u1, doc: "Action; See EHSMAction" }
    - { id: mu_num_children0x11, type: u1, doc: "Number of children" }
    - { id: padding, size: 2 }
    - { id: ptr_ma_child_spawn_data0x14, type: u4, doc: "Child state spawn data" }
    instances: 
      child_spawn_data:
        pos: ptr_ma_child_spawn_data0x14
        type: game__game_logic__hsm_data__hsm_state_spawn_data
        repeat: expr
        repeat-expr: mu_num_children0x11

  game__game_logic__hsm_data__hsm_parameter:
    seq:
    - { id: m_param_id0x0, type: game__game_logic__hsm_data__parameter_id, doc: "Parameter ID" }
    - { id: union0x8, type: u4, doc: "Pointer to value or child parameter list" }
    - { id: me_param_type0xc, type: s2, enum: e_hsm_param_type, doc: "Parameter type; See EHSMParamTypes" }
    - { id: mi_num_values0xe, type: s2, doc: "Number of values" }    
    instances:
      parameter_values:
        pos: union0x8
        type: anonymous_param_union(me_param_type0xc)
        repeat: expr
        repeat-expr: mi_num_values0xe

  anonymous_param_union:
    params:
      - id: param_type
        enum: e_hsm_param_type
        type: s2
    seq:
    - id: param
      # type: s4
      type:
        switch-on: param_type
        cases:
          'e_hsm_param_type::string': ptr('strz')
          'e_hsm_param_type::int': ptr('u4')
          'e_hsm_param_type::float': ptr('f4')
          'e_hsm_param_type::id': u4
          'e_hsm_param_type::bool': ptr('strz')
          'e_hsm_param_type::asset_reference': ptr('strz')
          'e_hsm_param_type::structure': game__game_logic__hsm_data__hsm_structure_instance
          'e_hsm_param_type::invalid': u4

  game__game_logic__hsm_data__hsm_structure_instance:
    seq:
    - { id: ptr_ma_parameters0x0, type: u4, doc: "Parameters" }
    - { id: mi_num_parameters0x4, type: s2, doc: "Number of parameters" }
    - { id: padding, size: 2 }
    instances:
      parameters:
        pos: ptr_ma_parameters0x0
        type: game__game_logic__hsm_data__hsm_parameter
        repeat: expr
        repeat-expr: mi_num_parameters0x4

  # Typedefs

  game__game_logic__state_definition_id:
    seq:
    - id: state_definition_id
      type: s4
      doc: |
        Unique ID

  game__game_logic__state_behaviour_id:
    seq:
    - id: state_behaviour_id
      type: s4
      doc: | 
        JAMCRC hash of behaviour ID
        ID matches decoded HSMBehaviourInterface__mBehaviourInterfaceID

  game__game_logic__data_definition_id:
    seq:
    - id: data_definition_id
      type: s4
      doc: |
        Unique ID

  game__game_logic__state_instance_id:
    seq:
    - id: state_instance_id
      type: s4
      doc: |
        Unique ID

  game__game_logic__state_entry_point_id:
    seq:
    - id: state_entry_point_id
      type: cgs_id
      doc: |
        Little endian

  game__game_logic__state_exit_point_id:
    seq:
    - id: state_exit_point_id
      type: cgs_id
      doc: |
        Little endian

  game__game_logic__hsm_data__parameter_id:
    seq:
    - id: parameter_id
      type: cgs_id

  cgs_id:
    seq:
    - id: value
      size: 0x8

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
            '"game__game_logic__hsm_data__hsm_top_state_definition"': game__game_logic__hsm_data__hsm_top_state_definition
            '"game__game_logic__hsm_data__hsm_state_entry_point"': game__game_logic__hsm_data__hsm_state_entry_point
            '"game__game_logic__hsm_data__hsm_state_spawn_data"': game__game_logic__hsm_data__hsm_state_spawn_data
            '"game__game_logic__hsm_data__hsm_child_exit_data"': game__game_logic__hsm_data__hsm_child_exit_data
            '"game__game_logic__hsm_data__hsm_child_exit_point_data"': game__game_logic__hsm_data__hsm_child_exit_point_data
            '"game__game_logic__hsm_data__hsm_parameter"': game__game_logic__hsm_data__hsm_parameter
            '"game__game_logic__hsm_data__hsm_state_definition"': game__game_logic__hsm_data__hsm_state_definition
            '"game__game_logic__hsm_data__hsm_data_definition"': game__game_logic__hsm_data__hsm_data_definition
            '"game__game_logic__hsm_data__hsm_behaviour_interface"': game__game_logic__hsm_data__hsm_behaviour_interface
            '"game__game_logic__hsm_data__hsm_structure_instance"': game__game_logic__hsm_data__hsm_structure_instance
            '"cgs_id"': cgs_id

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