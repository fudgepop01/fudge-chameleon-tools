meta:
  id: offline_event
  endian: le
  encoding: ascii
  # 146165144147145160157160060061o
  imports:
    - genesys_object
seq:
  - id: base_object
    type: genesys__gen__event
  - id: traffic_overrides_0x4c
    size: 8
  - id: ptr_arr_additional_assets_0x54
    type: u4
  - id: ptr_arr_aihints_0x58
    type: u4
  - id: allowed_vehicle_list_0x5c
    type: u4
  - id: maps_acceptors_0x60
    type: u4
  - id: ptr_arr_checkpoints_0x64
    type: u4
  - id: cgs_core__unique_id_0x68
    type: u4
  - id: ptr_arr_default_heat_levels_0x6c
    type: u4
  - id: event_intro_0x70
    type: u4
  - id: event_outro_0x74
    type: u4
  - id: feedback_message_group_0x78
    type: u4
  - id: ptr_arr_gameplay_triggers_0x7c
    type: u4
  - id: cgs_core__unique_id_0x80
    type: u4
  - id: name_0x84
    type: u4
  - id: name_formatted_0x88
    type: u4
  - id: next_story_event_0x8c
    type: u4
  - id: cgs_core__unique_id_0x90
    type: u4
  - id: race_balancing_data_0x94
    type: u4
  - id: race_balancing_profile_0x98
    type: u4
  - id: spawn_position_0x9c
    type: u4
  - id: ptr_arr_timeline_0xa0
    type: u4
  - id: type_name_0xa4
    type: u4
  - id: ptr_arr_target_speed_0xa8
    type: u4
  - id: ptr_arr_target_time_0xac
    type: u4
  - id: traffic_density_0xb0
    type: f4
  - id: ptr_arr_ptr_genesys__gen__chevron_0xb4
    type: u4
  - id: ptr_arr_ptr_genesys__gen__custom_chevron_0xb8
    type: u4
  - id: ptr_arr_ptr_conditions_0xbc
    type: u4
  - id: ptr_arr_aiplayers_0xc0
    type: u4
  - id: ptr_arr_alternative_routes_0xc4
    type: u4
  - id: ptr_arr_checkpoint_info_0xc8
    type: u4
  - id: target_score_0xcc
    type: u4
  - id: demo_mode_0xd0
    type: u2
    doc: enum; f7_f2_0e_00
  - id: array_count_for_0x54
    type: u2
  - id: array_count_for_0x58
    type: u2
    doc: '"AIHintsCount"'
  - id: array_count_for_0xc0
    type: u2
    doc: '"AIPlayersCount"'
  - id: array_count_for_0xc4
    type: u2
  - id: array_count_for_0xc8
    type: u2
    doc: '"CheckpointInfoCount"'
  - id: array_count_for_0x64
    type: u2
    doc: '"CheckpointsCount"'
  - id: array_count_for_0x6c
    type: u2
    doc: '"DefaultHeatLevelsCount"'
  - id: array_count_for_0xb4
    type: u2
  - id: array_count_for_0xa8
    type: u2
  - id: array_count_for_0xac
    type: u2
    doc: '"TargetTimeCount"'
  - id: array_count_for_0xa0
    type: u2
  - id: cop_spawning_0xe8
    type: u1
  - id: bool8_t_0xe9
    type: u1
  - id: listens_pervade_0xea
    type: u1
  - id: bool8_t_0xeb
    type: u1
  - id: nitrous_allowed_0xec
    type: u1
  - id: no_racing_line_traffic_0xed
    type: u1
  - id: brightening_capsule_0xee
    type: u1
  - id: start_with_engine_on_0xef
    type: u1
  - id: traffic_enabled_0xf0
    type: u1
  - id: bool8_t_0xf1
    type: u1
  - id: weapons_allowed_0xf2
    type: u1
  - id: array_count_for_0xb8
    type: u1
  - id: array_count_for_0xbc
    type: u1
    doc: '"ConditionsCount"'
  - id: array_count_for_0x7c
    type: u1
    doc: '"GameplayTriggersCount"'
  - id: laps_0xf6
    type: u1
  - id: padding
    size: 1
instances:
  inst_additional_assets_0x54:
    pos: ptr_arr_additional_assets_0x54
    type: u4
    repeat: expr
    repeat-expr: array_count_for_0x54
  inst_aihints_0x58:
    pos: ptr_arr_aihints_0x58
    type: u4
    repeat: expr
    repeat-expr: array_count_for_0x58
  inst_checkpoints_0x64:
    pos: ptr_arr_checkpoints_0x64
    type: u4
    repeat: expr
    repeat-expr: array_count_for_0x64
  inst_default_heat_levels_0x6c:
    pos: ptr_arr_default_heat_levels_0x6c
    type: u4
    repeat: expr
    repeat-expr: array_count_for_0x6c
  inst_gameplay_triggers_0x7c:
    pos: ptr_arr_gameplay_triggers_0x7c
    type: u4
    repeat: expr
    repeat-expr: array_count_for_0x7c
  inst_timeline_0xa0:
    pos: ptr_arr_timeline_0xa0
    type: u4
    repeat: expr
    repeat-expr: array_count_for_0xa0
  inst_target_speed_0xa8:
    pos: ptr_arr_target_speed_0xa8
    type: f4
    repeat: expr
    repeat-expr: array_count_for_0xa8
  inst_target_time_0xac:
    pos: ptr_arr_target_time_0xac
    type: f4
    repeat: expr
    repeat-expr: array_count_for_0xac
  inst_genesys__gen__chevron_0xb4:
    pos: ptr_arr_ptr_genesys__gen__chevron_0xb4
    type: ptr('genesys__gen__chevron')
    repeat: expr
    repeat-expr: array_count_for_0xb4
  inst_genesys__gen__custom_chevron_0xb8:
    pos: ptr_arr_ptr_genesys__gen__custom_chevron_0xb8
    type: ptr('genesys__gen__custom_chevron')
    repeat: expr
    repeat-expr: array_count_for_0xb8
  inst_conditions_0xbc:
    pos: ptr_arr_ptr_conditions_0xbc
    type: ptr('genesys__gen__gameplay__condition')
    repeat: expr
    repeat-expr: array_count_for_0xbc
  inst_aiplayers_0xc0:
    pos: ptr_arr_aiplayers_0xc0
    type: genesys__gen__offline_event__aiplayer_information
    repeat: expr
    repeat-expr: array_count_for_0xc0
  inst_alternative_routes_0xc4:
    pos: ptr_arr_alternative_routes_0xc4
    type: genesys__gen__offline_event__alternate_routes
    repeat: expr
    repeat-expr: array_count_for_0xc4
  inst_checkpoint_info_0xc8:
    pos: ptr_arr_checkpoint_info_0xc8
    type: genesys__gen__offline_event__checkpoint_info
    repeat: expr
    repeat-expr: array_count_for_0xc8
  size:
    value: 248
types:
  cgs_core__unique_id:
    seq: []
    instances: {}
  genesys__gen__custom_chevron:
    seq:
      - id: base_object
        type: genesys_object
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_float32_t_0x10
        type: u4
      - id: ptr_arr_float32_t_0x14
        type: u4
      - id: ptr_arr_float32_t_0x18
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: array_count_for_0x14
        type: u2
      - id: array_count_for_0x18
        type: u2
      - id: invert_normal_0x22
        type: u1
      - id: padding
        size: 1
    instances:
      inst_float32_t_0x10:
        pos: ptr_arr_float32_t_0x10
        type: f4
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_float32_t_0x14:
        pos: ptr_arr_float32_t_0x14
        type: f4
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_float32_t_0x18:
        pos: ptr_arr_float32_t_0x18
        type: f4
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 36
  genesys__gen__event:
    seq:
      - id: base_object
        type: genesys_object
      - id: ptr_arr_autotest_checkpoints_0xc
        type: u4
      - id: cinematic_name_0x10
        type: u4
      - id: description_0x14
        type: u4
      - id: game_changer_id_0x18
        type: u4
      - id: game_mode_0x1c
        type: u4
      - id: game_pack_0x20
        type: u4
      - id: cgs_core__unique_id_0x24
        type: u4
      - id: cycle_time_of_day_0x28
        type: f4
      - id: finish_time_of_day_0x2c
        type: f4
      - id: sun_direction_0x30
        type: f4
      - id: time_of_day_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: ptr_arr_ptr_chevron_list_0x3c
        type: u4
      - id: road_surface_conditions_0x40
        type: u2
        doc: enum; 8b_38_09_00
      - id: array_count_for_0xc
        type: u2
        doc: '"AutotestCheckpointsCount"'
      - id: is_alternative_weather_0x44
        type: u1
      - id: is_rain_active_0x45
        type: u1
      - id: is_thunder_active_0x46
        type: u1
      - id: override_sun_direction_0x47
        type: u1
      - id: bool8_t_0x48
        type: u1
      - id: array_count_for_0x3c
        type: u1
        doc: '"ChevronListCount"'
      - id: uint8_t_0x4a
        type: u1
      - id: padding
        size: 1
    instances:
      inst_autotest_checkpoints_0xc:
        pos: ptr_arr_autotest_checkpoints_0xc
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0xc
      inst_chevron_list_0x3c:
        pos: ptr_arr_ptr_chevron_list_0x3c
        type: ptr('genesys__gen__custom_chevron')
        repeat: expr
        repeat-expr: array_count_for_0x3c
      size:
        value: 76
  genesys__gen__chevron:
    seq:
      - id: base_object
        type: genesys_object
      - id: game_changer_id_0xc
        type: u4
      - id: road_section_0x10
        type: u4
      - id: should_block_start_0x14
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 24
  string_base:
    seq:
      - id: ofs_arr_buffer_0x0
        type: u4
      - id: array_count_for_0x0
        type: u4
        doc: '"Capacity"'
    instances:
      inst_buffer_0x0:
        pos: ofs_arr_buffer_0x0
        type: str
        size: array_count_for_0x0
      size:
        value: 12
  genesys__gen__gameplay__condition:
    seq:
      - id: base_object
        type: genesys_object
      - id: ptr_arr_strings_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: ptr_arr_references_0x14
        type: u4
      - id: ptr_arr_values_0x18
        type: u4
      - id: test_0x1c
        type: u2
        doc: enum; 55_31_0f_00
      - id: type_0x1e
        type: u2
        doc: enum; 68_f1_0e_00
      - id: array_count_for_0x14
        type: u2
        doc: '"ReferencesCount"'
      - id: array_count_for_0xc
        type: u2
        doc: '"StringsCount"'
      - id: array_count_for_0x18
        type: u2
        doc: '"ValuesCount"'
      - id: padding
        size: 2
    instances:
      inst_strings_0xc:
        pos: ptr_arr_strings_0xc
        type: string_base
        repeat: expr
        repeat-expr: array_count_for_0xc
      inst_references_0x14:
        pos: ptr_arr_references_0x14
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_values_0x18:
        pos: ptr_arr_values_0x18
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 40
  genesys__gen__offline_event__aiplayer_information:
    seq:
      - id: base_object
        type: genesys_object
      - id: aiplayer_type_0xc
        type: u4
      - id: back_up_colour_0x10
        type: u4
      - id: placement_0x14
        type: u4
      - id: primary_colour_0x18
        type: u4
    instances:
      size:
        value: 32
  genesys__gen__offline_event__alternate_routes:
    seq:
      - id: base_object
        type: genesys_object
      - id: checkpoint_0xc
        type: u4
      - id: ptr_arr_route_markers_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_route_markers_0x10:
        pos: ptr_arr_route_markers_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
  genesys__gen__offline_event__checkpoint_info:
    seq:
      - id: base_object
        type: genesys_object
      - id: sequence_0xc
        type: u4
      - id: type_0x10
        type: u2
        doc: enum; 2b_77_0f_00
      - id: bool8_t_0x12
        type: u1
      - id: show_split_time_0x13
        type: u1
    instances:
      size:
        value: 24


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
            '"cgs_core__unique_id"': cgs_core__unique_id
            '"genesys__gen__custom_chevron"': genesys__gen__custom_chevron
            '"genesys__gen__event"': genesys__gen__event
            '"genesys__gen__chevron"': genesys__gen__chevron
            '"string_base"': string_base
            '"genesys__gen__gameplay__condition"': genesys__gen__gameplay__condition
            '"genesys__gen__offline_event__aiplayer_information"': genesys__gen__offline_event__aiplayer_information
            '"genesys__gen__offline_event__alternate_routes"': genesys__gen__offline_event__alternate_routes
            '"genesys__gen__offline_event__checkpoint_info"': genesys__gen__offline_event__checkpoint_info

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