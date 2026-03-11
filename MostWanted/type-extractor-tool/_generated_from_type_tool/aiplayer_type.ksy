meta:
  id: aiplayer_type
  endian: le
  encoding: ascii
  # 146165144147145160157160060061o
  imports:
    - genesys_object
seq:
  - id: base_object
    type: genesys_object
  - id: cgs_core__unique_id_0xc
    type: u4
  - id: game_changer_id_0x10
    type: u4
  - id: rollout_0x14
    type: u4
  - id: ptr_arr_target_placement_0x18
    type: u4
  - id: aggression_delay_0x1c
    type: f4
  - id: aggression_frequency_0x20
    type: f4
  - id: blinded_time_scale_0x24
    type: f4
  - id: escaping_speed_0x28
    type: f4
  - id: fail_jump_daze_time_0x2c
    type: f4
  - id: flat_out_initial_time_0x30
    type: f4
  - id: flat_out_time_0x34
    type: f4
  - id: hit_damage_percentage_to_daze_0x38
    type: f4
  - id: hit_daze_time_0x3c
    type: f4
  - id: max_damage_for_speed_effect_0x40
    type: f4
  - id: max_event_balancing_distance_0x44
    type: f4
  - id: max_speed_for_distance_0x48
    type: f4
  - id: min_damage_for_speed_effect_0x4c
    type: f4
  - id: min_event_balancing_distance_0x50
    type: f4
  - id: min_shortcut_time_0x54
    type: f4
  - id: min_speed_for_distance_0x58
    type: f4
  - id: min_throttle_damage_percent_0x5c
    type: f4
  - id: min_time_between_weapon_uses_0x60
    type: f4
  - id: respawn_time_0x64
    type: f4
  - id: shortcut_taking_percentage_0x68
    type: f4
  - id: spawn_speed_0x6c
    type: f4
  - id: speed_0x70
    type: f4
  - id: speed_matching_max_distance_0x74
    type: f4
  - id: speed_matching_max_speed_0x78
    type: f4
  - id: float32_t_0x7c
    type: f4
  - id: speed_matching_min_speed_0x80
    type: f4
  - id: speed_matching_speed_difference_0x84
    type: f4
  - id: toughness_0x88
    type: f4
  - id: turn_at_junction_percentage_0x8c
    type: f4
  - id: uturn_min_time_0x90
    type: f4
  - id: weapon_avoidance_percentage_0x94
    type: f4
  - id: weapon_use_delay_at_event_start_0x98
    type: f4
  - id: weaving_duration_0x9c
    type: f4
  - id: weaving_frequency_0xa0
    type: f4
  - id: aggression_type_0xa4
    type: u2
    doc: enum; 71_fa_06_00
  - id: behaviour_0xa6
    type: u2
    doc: enum; 43_f6_05_00
  - id: unk_enum_0xa8
    type: u2
    doc: enum; 43_f6_05_00
  - id: nitrous_usage_0xaa
    type: u2
    doc: enum; 8a_fa_06_00
  - id: weaving_type_0xac
    type: u2
    doc: enum; 70_fa_06_00
  - id: array_count_for_0x18
    type: u2
  - id: allowed_to_respawn_0xb0
    type: u1
  - id: can_rhino_0xb1
    type: u1
  - id: do_uturns_0xb2
    type: u1
  - id: is_aggressor_0xb3
    type: u1
  - id: is_blacklist_0xb4
    type: u1
  - id: is_cop_0xb5
    type: u1
  - id: bool8_t_0xb6
    type: u1
  - id: uint8_t_0xb7
    type: u1
  - id: weapon_use_chance_0xb8
    type: u1
  - id: padding
    size: 3
instances:
  inst_target_placement_0x18:
    pos: ptr_arr_target_placement_0x18
    type: u4
    repeat: expr
    repeat-expr: array_count_for_0x18
  size:
    value: 188
enums:
  e_43_f6_05_00:
    "0": default
    "1": waiting
    "2": patrolling
    "3": escaping
    "4": chasing
    "5": waiting__lights
    "6": idle__lights
    "7": rhino
    "8": racing
    "9": free__roam
    "10": idle
    "11": ev11
    "12": chasing__interceptor
    "13": cop__racing
    "14": ev14
    "15": ev15
types:
  cgs_core__unique_id:
    seq: []
    instances: {}


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