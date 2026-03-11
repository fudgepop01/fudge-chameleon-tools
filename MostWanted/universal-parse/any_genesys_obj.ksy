meta:
  id: any_genesys_obj
  endian: le
  encoding: ascii
  # 146165144147145160157160060061o
seq:
  - id: save_ofs
    size: 0
    if: ofs < 0
  - id: obj
    type: gen_obj
instances:
  ofs:
    value: _io.pos
  data:
    pos: ofs
    type:
      switch-on: obj.mu_type_version
      cases:
        0x95_fb_ea_be: string_base
        0xf3_fe_77_3a: genesys__gen__challenge_action__accumulation_helper_data
        0xeb_54_ae_33: genesys__gen__challenge_action__action_base
        0xd7_89_93_d1: genesys__gen__challenge_action__accumulate_takedowns
        0x4d_23_4a_77: genesys__gen__challenge_action__action_base__feedback_data
        0x0c_17_6b_d6: genesys__gen__online_route
        0x4b_e5_cb_0b: genesys__gen__race_balancing_data__opponent_balancing_data
        0xf3_d1_75_e0: genesys__gen__event_arena_data__spawn_point_collection
        0x32_ac_e7_1b: genesys__gen__chevron
        0x38_4f_76_67: genesys__gen__challenge__location
        0xe3_e6_76_a8: genesys__gen__challenge_action__speed_camera_action
        0x9e_7a_d5_e2: genesys__gen__game_mode
        0xac_a9_15_3e: genesys__gen__custom_chevron
        0xb8_25_62_0e: genesys__gen__event
        0x17_73_05_4a: genesys__gen__online_event
        0x87_56_5a_00: genesys__gen__event_arena_data
        0xf4_84_79_01: genesys__gen__event_arena
        0xc8_ac_8f_6a: genesys__gen__challenge_action__jump_stats
        0x1b_33_ec_c5: genesys__gen__offline_event__alternate_routes
        0x71_52_42_99: genesys__gen__gameplay__condition
        0x7b_fb_67_04: genesys__gen__score_view_model__score
        0x45_d1_c4_27: genesys__gen__score_view_model
        0x24_2c_b4_ca: genesys__gen__score_view_model__score_data
        0x2b_a8_0e_31: genesys__gen__challenge_action__accumulate_near_misses
        0x99_45_25_4c: genesys__gen__event__checkpoint_info
        0x24_b9_40_8f: genesys__gen__offline_event__aiplayer_information
        0x20_55_7e_9d: genesys__gen__offline_event__custom_chevrons
        0x79_8b_78_5d: genesys__gen__challenge_action__coop_accumulate_distance
        0x0a_5f_28_ef: genesys__gen__challenge_action__car_state
        0x47_de_09_5b: genesys__gen__challenge_action__accumulate_time
        0xe3_70_b2_cc: genesys__gen__challenge_action__accumulate_distance
        0x99_ef_67_0a: genesys__gen__offline_event__checkpoint_info
        0xba_f7_b2_c9: genesys__gen__online__vote_event
        0xd6_0e_28_e0: genesys__gen__challenge__challenge_part
        0x7e_70_16_62: genesys__gen__challenge__online_challenge
        0xb3_b4_2a_12: genesys__gen__challenge_action__get_to_location
        0xb6_1c_c0_be: genesys__gen__race_balancing_data
        0x3f_12_39_21: genesys__gen__challenge_action__jump_over_players
        0xa5_81_c6_d9: genesys__gen__race_balancing_profile
        0x63_66_35_21: genesys__gen__challenge_action__do_jump
        0xc0_99_71_a8: genesys__gen__challenge_action__hit_trigger
        0x90_3b_cc_47: genesys__gen__offline_event
        0xd7_8c_a2_95: genesys__gen__challenge_action__speed_run
        0xc2_29_a8_2f: rw_math_vpu__vector4
        0x09_97_15_d1: genesys__gen__behaviour
        0x3e_e2_74_05: genesys__gen__wcremove_world_entity_behaviour
        0xb5_41_c3_e9: genesys__gen__corona__glow
        0x1c_74_fd_f8: genesys__gen__wcvfx_behaviour__coronas
        0xc9_34_b7_bf: genesys__gen__corona__beam
        0x83_9e_a4_f9: genesys__gen__wcvfx_behaviour__spot_effects
        0xc8_1a_ca_2a: genesys__gen__corona__flare
        0xc0_7e_ea_42: genesys__gen__wcvfx_behaviour__lights
        0xb9_ac_70_67: genesys__gen__wcplay_sound_behaviour__prop_surface_sound
        0x28_77_c8_41: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume
        0x01_12_fc_16: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume
        0x63_33_d3_31: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume
        0xf9_19_5e_af: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume
        0x5d_6d_83_cc: genesys__gen__race_car_physical_definition__physical_definition__rigid_body
        0x96_2d_8d_39: genesys__gen__race_car_physical_definition__physical_definition
        0xa5_f5_99_f3: rw_math_vpu__vector3
        0xb6_8b_60_0e: rw_math_vpu__matrix44affine
        0xe1_d5_78_1c: genesys__gen__make_physical_behaviour
        0x49_97_64_c1: genesys__gen__corona
        0xfb_72_73_f3: genesys__gen__wcplay_sound_behaviour
        0xce_85_d4_17: genesys__gen__wcvfx_behaviour
        0x50_e0_3c_00: genesys__gen__dsp_plug_in
        0xe5_fe_f6_15: genesys__gen__pan2ddsp_plug_in
        0x58_c7_6e_0d: genesys__gen__sequence_item__modulating_double_value
        0x75_40_01_39: genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value
        0x62_b3_c0_62: genesys__gen__voice_group
        0x85_39_5f_b3: genesys__gen__mixer_channel__priority
        0xd6_1a_73_ed: genesys__gen__post_fx_keyframe__bloom
        0x2e_e7_6e_33: rw_math_vpu__vector2
        0xbd_8f_1f_f0: genesys__gen__post_fx_keyframe__vignette
        0xf3_88_bb_fd: genesys__gen__post_fx_keyframe__general
        0x6c_a8_bb_26: genesys__gen__sequence_item
        0x6e_64_d0_2d: genesys__gen__race_car_effect_sequence_item__effect_double_value
        0x09_ea_9b_a3: genesys__gen__race_car_effect_sequence_item
        0x5f_65_e8_33: genesys__gen__post_fx_keyframe__depth_of__field
        0xc2_89_6d_d9: genesys__gen__peaking_dsp_plug_in
        0x4e_ef_3c_c8: genesys__gen__post_fx_keyframe__stereo_3d
        0x77_93_f8_32: genesys__gen__post_fxstate__colour_cube_settings
        0xf5_9a_d1_ea: genesys__gen__post_fxstate__value_modifier
        0x1b_30_82_d5: genesys__gen__heat_level_sound_set
        0x23_47_36_54: genesys__gen__sound_distance_falloff
        0xf0_56_15_02: genesys__gen__post_fxsequence_item
        0x6b_f6_a4_ca: genesys__gen__wave_sequence_item__fade
        0xda_65_11_74: genesys__gen__sequence_items__post_fx_override_sequence_item
        0x61_e7_01_04: genesys__gen__sequence_items__post_fx_override_sequence_item__effect_double_value
        0xb1_24_9c_3f: genesys__gen__mixer_channel
        0xf1_5e_68_36: genesys__gen__mixing_group
        0x42_35_4e_9f: genesys__gen__high_pass_butterworth_dsp_plug_in
        0xf2_75_9c_88: genesys__gen__sequence_timeline_controller
        0xe9_14_f8_53: genesys__gen__sequence
        0x06_e6_a5_18: genesys__gen__jump_timeline_controller
        0x1d_2d_63_cb: genesys__gen__sub_harmoniser_dsp_plug_in
        0xd8_3b_9e_56: genesys__gen__delay_dsp_plug_in
        0x67_21_89_d6: genesys__gen__quit_sequence_timeline_controller
        0x66_b0_22_3a: genesys__gen__wave_sequence_item
        0x17_88_5d_2b: genesys__gen__send_dsp_plug_in
        0x5a_94_09_dc: genesys__gen__post_fx_keyframe
        0x24_b3_7b_28: genesys__gen__post_fxstate
        0xe4_0e_7e_5d: genesys__gen__dsp_plug_in_chain
        0xcf_a1_b2_a2: genesys__gen__submix_dsp_plug_in
        0xd8_23_6b_f4: genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value
        0x47_69_2d_2c: genesys__gen__bus_mixer_channel_sequence_item
        0xbd_89_97_d6: genesys__gen__general_trigger_sequence_item
        0x93_74_3c_35: genesys__gen__snd_player_dsp_plug_in
        0xbd_76_cd_b7: genesys__gen__heat_level_sound_set__nitrous
        0x3f_11_a9_be: genesys__gen__heat_level_sound_set__sirens
        0xbd_a5_43_73: genesys__gen__distortion_dsp_plug_in
        0xa1_4d_af_26: genesys__gen__mixer_channel_sequence_item
        0x06_09_2e_f5: genesys__gen__uilist_items__item
        0x9c_8e_21_a8: genesys__gen__uilist_items
        0x20_54_d5_2b: genesys__gen__damage_bar_profiles__profile__segment_data
        0x7d_20_49_39: genesys__gen__damage_bar_profiles__profile
        0x69_1f_92_ad: genesys__gen__collision_effects
        0x03_b1_56_8c: genesys__gen__collision_effects__battling_effect__skid_effects
        0xca_6e_93_04: genesys__gen__collision_effects__battling_effect__extra_roll_params
        0xf9_d8_34_ca: genesys__gen__collision_effects__battling_effect
        0x6b_b6_93_5e: genesys__gen__collision_effects__traffic_effect__extra_roll_params
        0x7b_2c_02_f9: genesys__gen__collision_effects__traffic_effect
        0xa8_65_71_c1: genesys__gen__collision_effects__world_effect
        0x58_72_c2_4c: genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal
        0x47_a5_6c_dc: genesys__gen__physics__crashing_rules__impact_rules
        0x71_fa_84_e7: genesys__gen__physics__crashing_rules
        0x0a_68_e0_18: genesys__gen__collision_responses__world__traffic
        0x4c_31_8b_b0: genesys__gen__collision_responses__world__player__flip_state
        0x5e_f3_27_2f: genesys__gen__collision_responses__world__crashed_player__constraint_data
        0x4f_05_f9_19: genesys__gen__collision_responses__world__crashed_player
        0x2b_35_23_d4: genesys__gen__race_car_handling_disruption_effect
        0x9b_67_75_03: genesys__gen__physics__landing_damage
        0x5a_6e_77_e3: genesys__gen__physics__landing_damage__pitch
        0xd8_b3_b0_ad: genesys__gen__physics__landing_damage__roll
        0xa7_f2_15_0b: genesys__gen__physics__damage_bar_profile__impact_location_damage_scale
        0x95_1d_ad_be: genesys__gen__collision_info__world_effect
        0x8a_ff_20_36: genesys__gen__collision_info_damage_profile
        0x2d_10_2a_d7: genesys__gen__collision_info__world_damage
        0xd5_dc_12_ea: genesys__gen__collision_info__battling_damage
        0x1b_31_97_bc: genesys__gen__collision_info__payload_damage
        0x48_96_f9_8c: genesys__gen__collision_responses__global
        0xc8_38_aa_88: genesys__gen__collision_responses__global__race_car_vs_race_car
        0x2a_b6_e9_bc: genesys__gen__collision_responses__global__race_car_vs_race_car__params
        0x49_67_5a_53: genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params
        0x9c_87_62_e4: genesys__gen__collision_responses__global__crashing_race_car_vs_traffic
        0xb7_9f_5b_47: genesys__gen__collision_responses__global__traffic_vs_dynamic
        0x46_b5_cc_d9: genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car
        0x39_72_6c_a5: genesys__gen__collision_responses__global__traffic_vs_traffic
        0xe8_ed_b4_b8: genesys__gen__collision_responses__global__dynamic_vs_dynamic
        0x1f_47_19_c7: genesys__gen__collision_responses__race_car
        0x64_29_af_ec: genesys__gen__collision_responses__race_car__player_vs_traffic
        0x81_4a_38_40: genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params
        0x7f_d3_92_c3: genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params
        0x8e_8a_90_a4: genesys__gen__collision_responses__race_car__player_vs_ai
        0xb0_39_af_62: genesys__gen__collision_responses__race_car__player_vs_ai__damage_params
        0x1c_ad_98_de: genesys__gen__collision_responses__race_car__player_vs_ai__basic_params
        0xe2_81_00_5d: genesys__gen__collision_responses__race_car__aivs_traffic
        0xba_d9_5a_cc: genesys__gen__collision_responses__race_car__aivs_traffic__damage_params
        0x74_54_51_c9: genesys__gen__collision_responses__race_car__aivs_traffic__basic_params
        0xc2_12_dd_ec: genesys__gen__collision_responses__race_car__player_vs_crashing_race_car
        0xf0_8c_ae_fc: genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile
        0xb9_2f_86_f9: genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params
        0x2b_14_62_e5: genesys__gen__collision_responses__race_car__aivs_crashing_race_car
        0xb0_4e_5d_28: genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params
        0xaf_f7_71_da: genesys__gen__collision_responses__race_car__race_car_vs_dynamic
        0xe7_62_87_7e: genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params
        0x8a_ce_69_15: genesys__gen__collision_responses__world__in_air_player
        0x34_7d_09_0a: genesys__gen__physics__damage_bar_profile__segment
        0xd9_8e_ba_cd: genesys__gen__physics__damage_bar_profile
        0x57_c7_4f_cf: genesys__gen__collision_info
        0x70_6d_b6_32: genesys__gen__collision_info__battling_effect
        0xdc_0a_f1_b1: genesys__gen__collision_info__battling_effect__extra_roll_params
        0x87_af_e3_6c: genesys__gen__collision_info__traffic_effect
        0xd5_69_9b_70: genesys__gen__camera_gameplay_shake_effect
        0x33_a1_3e_49: genesys__gen__camera_gameplay_shake_effect__translation
        0xd2_62_d8_63: genesys__gen__camera_gameplay_shake_effect__translation__axis_params
        0x48_b8_4c_b2: genesys__gen__camera_gameplay_shake_effect__rotation
        0xd9_b1_e6_09: genesys__gen__camera_gameplay_shake_effect__rotation__axis_params
        0x0b_b1_a0_97: genesys__gen__impact_damage_graphs
        0x65_8d_7d_4d: genesys__gen__impact_damage_graphs__graph
        0x40_62_ed_a3: genesys__gen__collision_responses__world
        0xfd_ed_9d_18: genesys__gen__collision_responses__world__player
        0xe2_46_a1_af: genesys__gen__damage_bar_profiles
        0x8c_43_2d_e1: genesys__gen__traffic_flow_type__traffic_flow_type
        0xaf_cd_40_4e: genesys__gen__traffic_flow
        0x1b_e2_b3_77: genesys__gen__traffic_flow_type
        0xca_5d_4e_b1: genesys__gen__traffic_vehicle
        0x9a_9b_0b_91: genesys__gen__traffic_vehicle_traits
        0xaf_e3_6e_f3: genesys__gen__dynamic_additional_info
        0xec_02_6f_0f: genesys__gen__compound_additional_info
        0x12_48_17_f4: genesys__gen__light__base__flash_pattern
        0xf1_2b_e6_48: genesys__gen__light__base
        0xed_c9_d7_11: genesys__gen__light__cone
        0xec_fa_af_14: genesys__gen__light__point
        0xb7_e8_37_c2: genesys__gen__smash_proxy_behaviour
        0x82_86_ce_b2: genesys__gen__light__spot
        0xd6_15_d6_f9: genesys__gen__enable_compound_behaviour
        0x51_5d_57_d0: genesys__gen__easy_guide__page
        0xfd_b5_bb_33: genesys__gen__nitrous_parameters__traffic_near_miss
        0xdf_4b_ff_06: genesys__gen__nitrous_strength__jump
        0x9a_fc_ff_c1: genesys__gen__nitrous_parameters__traffic_oncoming
        0x94_06_6a_3d: genesys__gen__nitrous_parameters__nitrous_power
        0x9e_5a_13_c6: genesys__gen__nitrous_parameters__hitting_another_competitor
        0x9a_fd_9b_d9: genesys__gen__nitrous_parameters__high_speed
        0x7b_b2_02_23: genesys__gen__nitrous_parameters__catching_air
        0xf3_3f_75_b9: genesys__gen__nitrous_parameters__balancing
        0x40_73_c3_54: genesys__gen__nitrous_parameters__slipstreaming
        0xe1_a3_2e_6f: genesys__gen__nitrous_parameters__fatal_hit
        0xb5_0e_b2_7a: genesys__gen__aerodynamic_behaviour
        0x2e_17_bf_4f: genesys__gen__ginsu_sequence_item
        0xc0_fd_f0_90: genesys__gen__ginsu_sequence_item__fade
        0xd7_10_9a_3b: genesys__gen__gearbox__gear
        0xde_7a_ff_f6: genesys__gen__gearbox
        0x4b_17_85_2d: genesys__gen__colour_group
        0x5c_b8_53_e2: genesys__gen__performance_modification_item
        0xb2_dc_d5_bf: genesys__gen__performance_modifier
        0xee_89_cc_78: genesys__gen__handbrake_ability
        0xea_26_7c_d5: genesys__gen__nitrous_parameters__donutting
        0xcc_ae_ef_0e: genesys__gen__vehicle__gameplay__mod_effect
        0xcb_0b_5c_17: genesys__gen__aligning_torque
        0x43_4f_43_96: genesys__gen__body_movement_behaviour__take_off_behaviour
        0x06_56_e7_e5: genesys__gen__body_movement_behaviour
        0x86_49_78_e9: genesys__gen__brake_behaviour
        0xf8_3a_19_d6: genesys__gen__donut_ability__donut_grip_values
        0x3c_7f_c8_b0: genesys__gen__donut_ability__donut_scale
        0x53_21_53_f7: genesys__gen__donut_ability
        0xfd_98_90_57: genesys__gen__drift_behaviour__other
        0xd3_77_a1_da: genesys__gen__drift_behaviour__yaw_torque
        0x81_49_c3_b1: genesys__gen__drift_behaviour__side_force
        0x9e_41_c9_f7: genesys__gen__drift_behaviour__drift_scale
        0xf0_be_de_aa: genesys__gen__drift_behaviour__drift_exit
        0x5e_ba_96_68: genesys__gen__drift_behaviour__drift_trigger
        0xfe_ca_6d_4d: genesys__gen__drift_behaviour
        0xcc_71_ba_d5: genesys__gen__point2d
        0x64_de_27_ed: genesys__gen__point2dwith_tangents
        0xbe_73_7b_b9: genesys__gen__engine__power_curve
        0xd9_0a_66_25: genesys__gen__engine__sound
        0x2a_44_41_c3: genesys__gen__engine__differentials
        0xa9_bc_ff_78: genesys__gen__engine__normal_quality_engine
        0xe4_41_04_8a: genesys__gen__engine__transmission
        0x47_a2_87_66: genesys__gen__nitrous_strength
        0x31_c0_27_33: genesys__gen__engine
        0x3c_df_a1_41: genesys__gen__hard_driving_behaviour__gas_effect
        0x64_75_9f_45: genesys__gen__hard_driving_behaviour__steering_effect
        0xd0_a7_30_12: genesys__gen__hard_driving_behaviour
        0x9b_b2_c8_08: genesys__gen__steering_behaviour
        0x4f_42_3b_2c: genesys__gen__steering_wheel_physics
        0x52_ba_0c_65: genesys__gen__suspension
        0x09_e5_f2_87: genesys__gen__tyre__lateral__slip__factors
        0x93_d1_1d_75: genesys__gen__tyre__lateral__grip__curve
        0x05_0d_26_67: genesys__gen__tyre__long__grip__curve
        0x1c_da_7e_d7: genesys__gen__tyre__long__slip__factors
        0x01_4d_7f_4a: genesys__gen__tyre
        0x15_f8_5f_84: genesys__gen__tyres__tyres
        0x10_e5_5d_05: genesys__gen__vehicle_surface_profile__surface_link
        0xb5_c9_84_4c: genesys__gen__vehicle_surface_profile
        0x5b_3c_50_7d: genesys__gen__tyres__surface_effects
        0x21_9f_da_00: genesys__gen__tyre_sound_params__lateral
        0x33_43_76_65: genesys__gen__tyre_sound_params__lat_slip
        0xb2_61_5d_31: genesys__gen__tyre_sound_params__longitudinal
        0xbe_23_b7_07: genesys__gen__tyre_sound_params__long_spin_braking
        0x7c_10_b4_65: genesys__gen__tyre_sound_params__long_spin
        0xb6_0a_56_be: genesys__gen__tyre_sound_params
        0x54_fe_2c_d0: genesys__gen__tyres
        0xe3_29_45_b6: genesys__gen__handling_behaviour
        0xf3_73_fe_06: genesys__gen__nitrous_strength__punch
        0x0a_60_0d_4a: genesys__gen__engine_sound2__dsp_param
        0x93_b1_ae_2d: genesys__gen__engine_sound2__dsp_param_wrapper
        0xfb_c0_ba_e4: genesys__gen__engine_sound2__gain_param
        0x48_9a_b4_65: genesys__gen__engine_sound2__gain_param_wrapper
        0x6d_f4_bf_f4: genesys__gen__engine_sound2
        0xd3_2c_dc_8a: genesys__gen__vehicle__driver_setup__seat_belt_bone_offset
        0xd5_a7_20_62: genesys__gen__vehicle__driver_setup
        0xba_3e_b8_57: genesys__gen__steering_wheel_behaviour
        0xea_90_bc_d0: genesys__gen__steering_behaviour__steering_angle_curve
        0x1f_e8_ef_c0: genesys__gen__vehicle__sound
        0x4c_3e_7d_35: genesys__gen__suspension_wheel
        0x7b_c0_7d_85: genesys__gen__wheel_suspension_constraint
        0x2b_eb_51_e8: genesys__gen__wheel_suspension_spring_constraint
        0x0d_a8_4d_eb: genesys__gen__light__projected_texture
        0x02_dc_ac_cf: genesys__gen__pidcontroller
        0xb4_39_c9_0b: genesys__gen__body_movement_behaviour__angle_control
        0x42_23_79_c9: genesys__gen__vehicle_damage_behaviour__damage_sequence
        0x22_3a_4d_f2: genesys__gen__vfx_locator_group_vehicle_spot_effect_sequence_item
        0xc3_33_10_aa: genesys__gen__camera_gameplay_bonnet__wind_sound
        0x79_b5_42_d5: genesys__gen__camera_gameplay_external__acceleration_movement
        0x30_87_ee_63: genesys__gen__camera_gameplay_external__yaw_spring_modification
        0xb9_46_0d_d9: genesys__gen__camera_gameplay_external__speed_based_height_change
        0x85_41_2c_35: genesys__gen__camera_gameplay_external_globals__impact_shake
        0xf7_54_09_1e: genesys__gen__high_shelf_dsp_plug_in
        0xc7_38_ed_50: genesys__gen__camera_gameplay_bonnet
        0x3a_9d_63_ee: genesys__gen__camera_gameplay_bumper
        0x57_fb_ae_22: genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold
        0x1e_65_59_e2: genesys__gen__vehicle_damage_behaviour__bodypart
        0xe2_01_2c_06: genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake
        0x75_04_48_a2: genesys__gen__camera_gameplay_external__speed_based_movement
        0xd1_22_20_3a: genesys__gen__camera_gameplay_external__camera__roll
        0x2f_d3_1d_aa: genesys__gen__camera_gameplay_external__deceleration__pitch__change
        0x8f_25_9b_de: genesys__gen__camera_gameplay_external_globals__lens_properties
        0xdb_89_19_ba: genesys__gen__camera_gameplay_external_globals
        0x17_ab_8a_15: genesys__gen__camera_gameplay_gradient_adjustments__params
        0x3a_76_eb_32: genesys__gen__camera_gameplay_gradient_adjustments
        0xbb_ad_ac_a9: genesys__gen__camera_gameplay_external
        0xf5_70_25_85: genesys__gen__vehicle_damage_behaviour__spot_effect
        0xac_a5_6f_a5: genesys__gen__vehicle_paint__material_properties
        0x0f_78_2d_29: genesys__gen__camera_rear_view_globals
        0x3b_7e_06_ec: genesys__gen__camera_rear_view
        0x40_7f_fb_f1: genesys__gen__vehicle_paint__structure2
        0xcd_60_4e_4a: genesys__gen__vehicle_vfx_behaviour__corona
        0x07_5e_e9_62: genesys__gen__vehicle_vfx_behaviour__light
        0x81_56_a6_f2: genesys__gen__vehicle_vfx_behaviour__spot_effect
        0xb7_ee_51_b2: genesys__gen__passby_sequence_behaviour
        0x3b_b7_85_6a: genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face
        0x56_27_d2_53: genesys__gen__race_car_physical_definition__convex_hull_conectivity_data
        0x4e_75_f6_26: genesys__gen__race_car_physical_definition
        0x57_35_1a_22: genesys__gen__nitrous_parameters__crash_escape
        0x05_28_73_c0: genesys__gen__vehicle_camera_container
        0xf2_1d_49_9c: genesys__gen__vehicle_colour_palette
        0x17_ee_4b_7d: genesys__gen__nitrous_parameters_usage
        0x96_5c_07_2b: genesys__gen__nitrous_parameters__speedbreaker_usage
        0x33_03_a1_b4: genesys__gen__nitrous_parameters
        0x83_90_1a_a6: genesys__gen__nitrous_parameters__drifting
        0xcf_6c_14_50: genesys__gen__nitrous_parameters__punch_usage
        0xe1_d8_d1_1f: genesys__gen__nitrous_parameters__min_speed
        0x04_cb_c8_7c: genesys__gen__nitrous_parameters__nitrous_usage
        0x64_9a_22_d4: genesys__gen__nitrous_parameters__taking_shortcut
        0x37_c9_32_bd: genesys__gen__nitrous_parameters__jump_usage
        0x52_20_55_c0: genesys__gen__nitrous_parameters__restrictions
        0x99_f8_6b_c8: genesys__gen__vehicle_component__wheel
        0xcb_99_ba_be: genesys__gen__vehicle_component
        0x70_1a_f0_04: genesys__gen__vehicle_damage_behaviour
        0xcd_13_11_72: genesys__gen__vehicle_info__axle
        0xd5_e6_e4_bf: genesys__gen__vehicle_info__extra_axle
        0xeb_bc_65_68: genesys__gen__vehicle_info
        0x35_09_ba_49: genesys__gen__vehicles__upgrade_base
        0x27_84_3e_3f: genesys__gen__vehicles__performance_upgrades
        0x84_f7_48_25: genesys__gen__vehicles__performance_upgrades__category
        0x27_e6_c8_ac: genesys__gen__vehicle_paint
        0xa5_fd_f5_ad: genesys__gen__vehicles__tyre_upgrade
        0xde_2c_b2_60: genesys__gen__engine__reverse_whine
        0xc4_d0_8e_8d: genesys__gen__vehicle_vfx_behaviour
        0x8c_c5_f9_3b: genesys__gen__engine__mixer__channel__gain__modification
        0x71_55_0f_54: genesys__gen__engine__mix
        0x76_07_7e_51: genesys__gen__control_mesh
        0x00_0b_99_13: genesys__gen__vehicles__vehicle_category_info
        0xe2_28_a5_39: genesys__gen__band_pass_dsp_plug_in
        0x0c_8b_da_7d: genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params
        0x95_43_43_fd: genesys__gen__wheel_damage
        0x0d_ca_11_27: genesys__gen__ginsu_dsp_plug_in
        0xee_6e_71_b1: genesys__gen__low_pass_butterworth_dsp_plug_in
        0x16_36_fd_42: genesys__gen__vehicle__gameplay__damage_stats
        0x8a_58_4e_a2: genesys__gen__wheel_sizes
        0x0f_ec_e6_a9: genesys__gen__timeline_controllers__race_car_entity_timeline_controller
        0x53_ed_c3_28: genesys__gen__handbrake_ability__handbrake_grip_values
        0xb4_bd_b3_92: genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params
        0xd2_6b_77_23: genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params
        0x66_08_56_1f: genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params
        0x28_a7_81_2a: genesys__gen__tyre_vfx_behaviour__front_rear_params
        0xf2_d7_7d_83: genesys__gen__tyre_vfx_behaviour
        0x24_e3_36_a6: genesys__gen__vehicles__sound__transmission_whine
        0x55_f8_05_97: genesys__gen__tyre_vfx_behaviour__long_lat_params
        0xd9_24_92_fb: genesys__gen__tyre_vfx_behaviour__smoke_params
        0xf7_e9_b7_09: genesys__gen__tyre_vfx_behaviour__skid_mark_params
        0xf5_6b_04_27: genesys__gen__vehicles__modifier_upgrade
        0x3a_6b_3d_40: genesys__gen__vehicles__nitrous_upgrade
        0x93_79_b7_14: genesys__gen__lfo_sequence_item
        0xf4_35_c7_65: genesys__gen__lfo_sequence_item__lfo_double_value
        0xf4_65_85_a8: genesys__gen__vehicle__gameplay__tyre_trails
        0x1f_07_17_67: genesys__gen__vehicle__gameplay
        0x68_a3_6b_fe: genesys__gen__online__driving_test_list
        0xf9_51_68_6b: genesys__gen__online__driving_test_list_group
        0x06_b8_ea_f5: genesys__gen__gameplay__offline_upgrade
        0xfe_1c_ee_ea: genesys__gen__nucleus_grant_mappings_list__mapping
        0xfc_d7_ca_e6: genesys__gen__online__driving_test_list_groups
        0x41_14_5c_97: genesys__gen__heat_level
        0x02_1b_2e_66: genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour
        0x5c_e2_18_46: genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour
        0x70_40_a2_8b: genesys__gen__heat_level__behaviour_coordination
        0x2f_4f_a7_04: genesys__gen__game_pack
        0xbc_4b_89_fb: genesys__gen__game_rank
        0xd5_95_86_1f: genesys__gen__game_unlock
        0x2c_04_42_9d: genesys__gen__game_unlock_list
        0x5b_fa_1e_2e: genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control
        0xde_b9_4e_40: genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold
        0xa7_64_a6_e7: genesys__gen__road_block_layer__item
        0x9d_0d_72_73: genesys__gen__gameplay_trigger__input
        0xdc_05_24_d5: genesys__gen__aiplayer_instance
        0x4c_f9_0b_22: genesys__gen__gameplay_trigger__aiplayer_information
        0x84_75_5b_d2: genesys__gen__gameplay_trigger__output__sequence_output
        0x7c_8e_25_02: genesys__gen__roadblock_instance
        0x31_d3_0a_05: genesys__gen__gameplay_trigger__output
        0x01_6a_bd_31: genesys__gen__gameplay_trigger
        0x7b_e0_ac_61: genesys__gen__online_challenge_target
        0xe0_a1_81_08: genesys__gen__online_challenge
        0x13_67_e2_c7: genesys__gen__store_item
        0xb7_10_a2_08: genesys__gen__store_pack
        0xd4_f9_60_f2: genesys__gen__store_pack_list
        0x6a_32_d4_f4: genesys__gen__scoring_action__online_scoring_feedback
        0x1a_e7_17_9a: genesys__gen__thankyou_mapping
        0x7a_ff_66_76: genesys__gen__rollout__weapon_data
        0x99_b7_15_31: genesys__gen__thank_you_screen_item
        0xd2_97_1c_1d: genesys__gen__aiplayer_type
        0xfe_41_d4_24: genesys__gen__uicamera
        0x63_78_a7_1f: genesys__gen__car_select_data__sequences
        0xce_cf_4d_c9: genesys__gen__safehouse
        0x31_cc_82_44: genesys__gen__gameplay__drift_marker
        0x6d_7e_04_b3: genesys__gen__rollout
        0x9c_df_6b_53: genesys__gen__scoring_action
        0xee_73_7c_02: genesys__gen__car_select_data
        0xae_20_16_93: genesys__gen__gameplay__milestone__entry
        0x4e_bb_d9_43: genesys__gen__gameplay__milestone
        0x48_46_99_8b: genesys__gen__nucleus_entitlement_tag
        0xba_a5_64_08: genesys__gen__nucleus_entitlement_tags
        0x3a_26_00_0e: genesys__gen__nucleus_grant_mappings_list
        0x39_07_3e_a4: genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods
        0x31_9a_5f_9c: genesys__gen__paint_pack
        0x72_08_5b_1b: genesys__gen__paint_pack_group
        0x60_0c_5f_24: genesys__gen__car_swap_spot
        0x41_ef_27_eb: genesys__gen__online__license_plate
        0x98_9c_04_d1: genesys__gen__entitlement
        0x65_c6_8f_55: genesys__gen__gameplay__revenge_bonus
        0x3a_7e_79_74: genesys__gen__event_list
        0xe9_6b_72_79: genesys__gen__event_location
        0x94_58_ff_cf: genesys__gen__road_block_definition
        0x65_03_e6_7a: genesys__gen__road_block_layer
        0x86_d7_15_26: genesys__gen__gameplay__blacklist_shutdown_data
        0xed_fc_c0_52: genesys__gen__gameplay__allowed_vehicle_list
        0x68_d5_c1_d3: genesys__gen__gameplay__cop_type
        0xee_33_86_8e: genesys__gen__cloud_compete_award
        0xbc_85_5d_7f: genesys_obj_collection
enums:
  e_e6_39_11_00:
    "0": allow_fail
    "1": ev1
  e_13_37_11_00:
    "0": none
    "1": raw
    "2": tick
    "3": speed
    "4": time
    "5": position
    "6": distance
  e_0f_39_11_00:
    "0": longest
    "1": shortest
    "2": most
    "3": least
    "4": closest
    "5": ev5
  e_2d_39_11_00:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": simultaneous
    "4": ev4
  e_28_37_11_00:
    "0": none
    "1": ev1
    "2": on__finish
  e_24_37_11_00:
    "0": individual
    "1": team
    "2": everyone
  e_0e_f7_05_00:
    "0": time
    "1": score
  e_13_94_0e_00:
    "0": no_retry
    "1": ev1
    "2": ev2
  e_2b_77_0f_00:
    "0": ev0
    "1": ev1
    "2": sector_start
    "3": lap_start
    "4": ev4
  e_42_f3_0e_00:
    "0": ev0
    "1": timeout
  e_53_37_11_00:
    "0": move_on
    "1": fail
  e_55_31_0f_00:
    "0": ev0
    "1": racers_finished
    "2": drift
    "3": racers_wrecked
    "4": cops_wrecked
    "5": binding
    "6": ev6
    "7": player_wrecked
    "8": beat_time
    "9": top_speed
    "10": starting_score
    "11": ev11
    "12": air_time
  e_8b_38_09_00:
    "0": dry
    "1": wet
    "2": standing_water
  e_58_39_11_00:
    "0": current_action
    "1": last_action
  e_68_f1_0e_00:
    "0": win
    "1": lose
    "2": special
  e_c3_38_11_00:
    "0": speed_test
    "1": team
    "2": social
  e_ff_f8_17_00:
    "0": none
    "1": ev1
    "2": ev2
    "3": ev3
    "4": random
  e_f7_f2_0e_00:
    "0": none
    "1": ev1
    "2": ev2
    "3": ev3
  e_2a_be_07_00:
    "0": high_quality
    "1": low_quality
  e_a3_37_09_00:
    "0": default
    "1": helicopter
  e_a1_2e_00_00:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
    "5": ev5
  e_b3_27_00_00_0_2:
    "0": none
    "1": camera_aligned
  e_e4_33_07_00:
    "0": mono
    "1": stereo
    "2": ev2
  e_5b_f6_03_00:
    "0": multiply
    "1": offset
    "2": absolute
  e_29_f7_03_00:
    "0": gain
    "1": panning__angle
    "2": panning__divergence
    "3": ev3
    "4": ev4
    "5": ev5
    "6": pitch
    "7": focus
    "8": emitter
    "9": ev9
    "10": instance_limit
    "11": ev11
  e_0f_34_07_00:
    "0": ev0
    "1": ev1
    "2": clip
    "3": off
  e_35_30_00_00:
    "0": ev0
    "1": high_cost
  e_d0_39_0b_00:
    "0": constantly
    "1": periodically
    "2": on__entry
    "3": once
  e_15_f7_03_00:
    "0": nickname_violation
    "1": ev1
    "2": drag
    "3": engine__load
    "4": ev4
    "5": throttle
    "6": engine__on
    "7": ev7
    "8": ev8
    "9": chassis__heat
    "10": alarm__on
    "11": ev11
    "12": ev12
  e_3d_30_00_00:
    "0": none
    "1": power
    "2": multiply
  e_1d_30_00_00:
    "0": near
    "1": mid
    "2": far
    "3": ev3
  e_22_30_00_00:
    "0": none
    "1": low
    "2": normal
    "3": extreme
  e_27_30_00_00:
    "0": none
    "1": engine
    "2": skid
    "3": player
    "4": competitor
    "5": traffic
    "6": ui
  e_2a_6b_07_00:
    "0": stop
    "1": restart
  e_38_30_00_00:
    "0": invalid
    "1": match
    "2": linear
    "3": exponential
  e_4a_63_04_00:
    "0": deducted__shield
    "1": ev1
  e_55_21_0a_00:
    "0": none
    "1": channel_animation
    "2": ev2
  e_83_f6_03_00:
    "0": time
    "1": binding
    "2": none
  e_85_8d_10_00:
    "0": once
    "1": random
    "2": periodic
    "3": ev3
    "4": ev4
    "5": ev5
  e_8f_7d_0f_00:
    "0": brightness
    "1": contrast
    "2": motion__blur
  e_b2_35_07_00:
    "0": default
    "1": reverb
    "2": ev2
    "3": ev3
    "4": buffering__percents
  e_c4_f3_03_00:
    "0": loaded
    "1": streamed
    "2": ev2
    "3": decay_exceptionally
    "4": ev4
    "5": speech__stream
    "6": ev6
    "7": ev7
  e_d5_f6_03_00:
    "0": gain
    "1": ev1
    "2": ev2
    "3": ev3
    "4": peak__frequency
    "5": peak__gain
    "6": peak__q
    "7": ev7
    "8": low__shelf__gain
    "9": ev9
    "10": ev10
    "11": ev11
    "12": ev12
    "13": ev13
    "14": ev14
    "15": ev15
    "16": ev16
    "17": ev17
    "18": compressor__ratio
    "19": compressor__threshold
    "20": vocally_impose
    "21": compressor__release
    "22": ev22
    "23": distortion__amount
  e_ee_33_07_00:
    "0": source
    "1": ev1
    "2": perceives_several
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
  e_de_30_00_00:
    "0": invalid
    "1": small
    "2": medium
    "3": large
  e_f0_2f_00_00:
    "0": none
    "1": ev1
    "2": ev2
    "3": ev3
  e_00_0f_16_00:
    "0": ev0
    "1": ev1
    "2": ev2
  e_02_5e_0f_00:
    "0": engine_torque
    "1": ev1
    "2": front_drag
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
    "7": ev7
    "8": toughness_vs_race_car
    "9": ev9
    "10": toughness_vs_traffic
    "11": ev11
    "12": toughness_vs_world
    "13": toughness_vs_dynamic
    "14": ev14
    "15": ev15
    "16": ev16
    "17": ev17
    "18": mass
    "19": strength
    "20": ev20
    "21": ev21
    "22": fu_r7
    "23": ev23
    "24": ev24
    "25": ev25
    "26": ev26
    "27": roll_angle_limit
    "28": ev28
    "29": ev29
    "30": ev30
    "31": gravity_multiplier
    "32": ev32
    "33": transmission_whine
    "34": ev34
    "35": ev35
    "36": ev36
    "37": ev37
    "38": ev38
    "39": ev39
    "40": ev40
    "41": ev41
    "42": ev42
    "43": ev43
    "44": ev44
    "45": ev45
    "46": pitying_gun
    "47": ev47
    "48": ev48
    "49": ev49
    "50": ev50
    "51": ev51
    "52": ev52
    "53": ev53
    "54": ev54
  e_04_32_00_00:
    "0": ev0
    "1": ev1
    "2": reversing
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
    "7": ev7
    "8": ev8
    "9": ev9
    "10": ev10
    "11": ev11
    "12": ev12
    "13": slip_streaming
    "14": ev14
    "15": ev15
    "16": ev16
    "17": ev17
    "18": idle
    "19": ev19
    "20": ev20
  e_09_5e_0f_00:
    "0": scalar
    "1": addition
    "2": override
  e_18_32_00_00:
    "0": ev0
    "1": ev1
    "2": ev2
  e_2b_55_19_00:
    "0": acceleration
    "1": top_speed
    "2": ev2
    "3": ev3
    "4": toughness
    "5": ev5
    "6": nitrous
  e_32_67_0d_00:
    "0": ev0
    "1": shunt
    "2": ev2
    "3": skid
  e_bc_35_07_00:
    "0": gain
    "1": frequency
    "2": q
    "3": time
    "4": feedback
    "5": ev5
    "6": ev6
    "7": ev7
    "8": ev8
  e_d9_31_00_00:
    "0": ev0
    "1": ev1
    "2": rear
    "3": left
    "4": ev4
    "5": ev5
    "6": ev6
    "7": ev7
    "8": ev8
  e_f3_0d_06_00:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
  e_a4_5d_0f_00:
    "0": ev0
    "1": ev1
    "2": stock
    "3": track
    "4": ev4
    "5": ev5
  e_f6_31_00_00:
    "0": ev0
    "1": ev1
    "2": grey
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
    "7": blue
    "8": ev8
  e_f0_31_00_00:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": traffic
  e_d9_65_15_00:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
    "7": ev7
    "8": ev8
  e_f4_5f_0f_00:
    "0": ev0
    "1": ev1
    "2": road
    "3": ev3
    "4": track
  e_f7_34_07_00:
    "0": rate
    "1": ev1
    "2": ev2
  e_e3_31_0f_00:
    "0": standard
    "1": pro
  e_d7_31_0f_00:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
    "7": ev7
    "8": ev8
    "9": ev9
    "10": ev10
    "11": ev11
    "12": ev12
    "13": ev13
  e_83_1d_10_00:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
  e_69_32_11_00:
    "0": chasing
    "1": blocking
    "2": bruising
    "3": rhino
    "4": ev4
    "5": idle
    "6": default
  e_c8_2f_00_00:
    "0": ev0
    "1": dlc1
    "2": dlc2
    "3": dlc3
    "4": dlc4
  e_95_6a_96_0c:
    "0": ev0
    "1": online
  e_8e_4e_49_12:
    "0": rank
    "1": game_mode
    "2": weapon
    "3": ev3
    "4": car
    "5": weapon_upgrade
    "6": ev6
    "7": license_plate
    "8": driving_test_list
    "9": feature
    "10": paint_pack
    "11": count
    "12": unknown
  e_77_cc_06_00:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
    "7": ev7
  e_72_cc_06_00:
    "0": play__once
    "1": ev1
    "2": ev2
  e_a8_60_04_00:
    "0": none
    "1": ev1
    "2": drifting
    "3": tbone
    "4": shunt
    "5": slam
    "6": vertical
    "7": into_traffic
    "8": into_water
    "9": ev9
    "10": using_nitrous
    "11": top_speed
    "12": ev12
    "13": ev13
    "14": ev14
    "15": after_spotting
    "16": ev16
    "17": all_events
    "18": ev18
    "19": license_plates
    "20": over_speed
    "21": billboards
    "22": speed_traps
    "23": in_air
    "24": over_player
    "25": traffic_vehicle
    "26": player_vehicle
    "27": ev27
    "28": paint_pack
  e_a7_d8_19_00:
    "0": equals
    "1": ev1
  e_43_5f_04_00:
    "0": drive
    "1": takedown
    "2": fall
    "3": jump
    "4": unlock
    "5": near_miss
    "6": complete_event
    "7": wreck
    "8": repair
    "9": ev9
    "10": ev10
    "11": perfect_nitrous
    "12": spot_opponent
    "13": spot_bonus
    "14": ev14
    "15": eliminate_opponent
    "16": last_standing
    "17": ticket
    "18": fuel_portrait
    "19": be
    "20": be_eliminated
    "21": false_start
    "22": score_first
    "23": collect
    "24": ev24
    "25": jack_car
    "26": air_time
    "27": accumulate_time
    "28": ev28
  e_d7_e3_10_00:
    "0": none
    "1": finish_first
    "2": ev2
    "3": not_overtaken
    "4": ev4
    "5": not_spotted
    "6": not_wrecked
    "7": ev7
    "8": ev8
    "9": distinct
    "10": on_rims
    "11": last_second
    "12": ev12
    "13": ev13
    "14": most_wanted
    "15": finish_last
    "16": no_score
  e_3e_5f_04_00:
    "0": seconds
    "1": chain
    "2": lives
    "3": events
    "4": speed_lists
    "5": all__time
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
  e_53_bc_16_00:
    "0": none
    "1": individual
    "2": social
    "3": team
  e_71_fa_06_00:
    "0": none
  e_8a_fa_06_00:
    "0": none
  e_70_fa_06_00:
    "0": none
  e_76_f5_0e_00:
    "0": ev0
    "1": imagen_rewarding
    "2": live_feed
    "3": photo_gallery
  e_86_f4_0e_00:
    "0": multi_player
    "1": single_player
    "2": social
    "3": ev3
    "4": ev4
    "5": disallowed__currently
    "6": ev6
  e_b9_b2_17_00:
    "0": ev0
    "1": online_only
    "2": ev2
  e_93_37_09_00:
    "0": ev0
    "1": ev1
    "2": ev2
  e_d9_f0_0e_00:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": pursuits__evaded
    "5": time__played
    "6": distance__driven
    "7": bounty__earned
    "8": times__busted
    "9": ev9
    "10": ev5lw_l
    "11": ev11
    "12": times__wrecked
    "13": ev13
    "14": ev14
    "15": ev15
    "16": ev16
    "17": ev17
    "18": ev18
    "19": jumps__found
    "20": ev20
    "21": ev21
    "22": billboards__hit
    "23": ev23
    "24": ev24
    "25": crash__escapes
    "26": ev26
    "27": ev27
    "28": ev28
    "29": ev29
    "30": ev30
    "31": ev31
    "32": ev32
    "33": ev33
    "34": ev34
    "35": ev35
    "36": ev36
    "37": ev37
    "38": ev38
    "39": ev39
    "40": ev40
    "41": ev41
    "42": ev42
    "43": ev43
    "44": ev44
    "45": ev45
    "46": ev46
    "47": ev47
  e_93_f3_05_00:
    "0": takedown
    "1": assist
    "2": suicide
    "3": teamkill
    "4": revenge
    "5": first_blood
    "6": afterlife
    "7": double_takedown
    "8": triple_takedown
    "9": takedown_frenzy
    "10": reverse
    "11": ev11
    "12": ev12
    "13": comeback
    "14": takendown
    "15": speeding
    "16": weapon_used
    "17": cop_hit
    "18": ev18
    "19": ev19
    "20": ev20
    "21": enter_cooldown
    "22": prop_damaged
    "23": prop_destroyed
    "24": traffic_hit
    "25": traffic_immobilised
    "26": ev26
    "27": hit_jump
    "28": jump_takedown
    "29": hit_blackspot
    "30": blackspot_takedown
    "31": hit_stack
    "32": stack_takedown
    "33": ev33
    "34": keeping_dry
    "35": ev35
    "36": high_speed
    "37": on_rims
    "38": on_rims2
    "39": on_rims3
    "40": on_rims4
    "41": boost_punch
    "42": slam_offline
    "43": shunt_offline
    "44": tbone_offline
    "45": slam_online
    "46": shunt_online
    "47": ev47
    "48": ev48
    "49": fight_bonus
    "50": weapon_hit
    "51": head_on_offline
    "52": ev52
    "53": avenger
    "54": rescuer
    "55": payload_takedown
    "56": ev56
    "57": payload_spilled
    "58": cop_hit_payload
    "59": into_city
    "60": blinded
    "61": smoked
  e_e2_b2_17_00:
    "0": ev0
  e_e1_bc_16_00:
    "0": off
    "1": standard
    "2": pro
  e_e8_bc_16_00:
    "0": stock
    "1": track
    "2": ev2
types:
  cgs_core__string_base:
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
      mu_version_hash:
        value: 0x95_fb_ea_be
  char:
    seq: []
    instances: {}
  uint32_t:
    seq: []
    instances: {}
  cgs_core__unique_id:
    seq: []
    instances: {}
  genesys__gen__challenge_action__accumulation_helper_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: target_0x10
        type: u4
      - id: operator_0x14
        type: u2
        doc: enum; 0f_39_11_00
      - id: bool8_t_0x16
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xf3_fe_77_3a
  genesys__gen__challenge_action__action_base:
    seq:
      - id: base_object
        type: gen_obj
      - id: feedback_data_0xc
        type: genesys__gen__challenge_action__action_base__feedback_data
      - id: cgs_core__unique_id_0x30
        type: u4
      - id: cgs_core__unique_id_0x34
        type: u4
      - id: game_changer_id_0x38
        type: u4
      - id: ptr_accumulation_data_0x3c
        type: u4
      - id: builtin_evoke_0x40
        type: u2
        doc: enum; 2d_39_11_00
      - id: scoring_method_0x42
        type: u2
        doc: enum; 28_37_11_00
      - id: unk_enum_0x44
        type: u2
        doc: enum; e6_39_11_00
      - id: who_0x46
        type: u2
        doc: enum; 24_37_11_00
    instances:
      inst_accumulation_data_0x3c:
        pos: ptr_accumulation_data_0x3c
        type: genesys__gen__challenge_action__accumulation_helper_data
      size:
        value: 76
      mu_version_hash:
        value: 0xeb_54_ae_33
  genesys__gen__challenge_action__accumulate_takedowns:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: padding
        size: 2
    instances:
      size:
        value: 76
      mu_version_hash:
        value: 0xd7_89_93_d1
  genesys__gen__challenge_action__action_base__feedback_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: instruction_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: cgs_core__unique_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: cgs_core__unique_id_0x1c
        type: u4
      - id: unk_enum_0x20
        type: u2
        doc: enum; 13_37_11_00
      - id: bool8_t_0x22
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x4d_23_4a_77
  bool8_t:
    seq: []
    instances: {}
  uint8_t:
    seq: []
    instances: {}
  genesys__gen__online_route:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_arr_checkpoints_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: array_count_for_0xc
        type: u2
        doc: '"CheckpointsCount"'
      - id: padding
        size: 2
    instances:
      inst_checkpoints_0xc:
        pos: ptr_arr_checkpoints_0xc
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0xc
      size:
        value: 24
      mu_version_hash:
        value: 0x0c_17_6b_d6
  uint16_t:
    seq: []
    instances: {}
  genesys__gen__race_balancing_data__opponent_balancing_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ahead_distance_0x10
        type: f4
      - id: behind_distance_0x14
        type: f4
      - id: end_cutoff_ratio_0x18
        type: f4
      - id: end_speed_value_ahead_0x1c
        type: f4
      - id: end_speed_value_behind_0x20
        type: f4
      - id: start_cutoff_ratio_0x24
        type: f4
      - id: start_speed_value_ahead_0x28
        type: f4
      - id: start_speed_value_behind_0x2c
        type: f4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0x4b_e5_cb_0b
  float32_t:
    seq: []
    instances: {}
  genesys__gen__event_arena_data__spawn_point_collection:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_spawn_points_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"SpawnPointsCount"'
      - id: padding
        size: 2
    instances:
      inst_spawn_points_0x10:
        pos: ptr_arr_spawn_points_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xf3_d1_75_e0
  int16_t:
    seq: []
    instances: {}
  genesys__gen__chevron:
    seq:
      - id: base_object
        type: gen_obj
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
      mu_version_hash:
        value: 0x32_ac_e7_1b
  genesys__gen__challenge__location:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: ptr_arr_display_trigger_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: ptr_arr_triggers_0x18
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: array_count_for_0x18
        type: u2
        doc: '"TriggersCount"'
    instances:
      inst_display_trigger_0x10:
        pos: ptr_arr_display_trigger_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_triggers_0x18:
        pos: ptr_arr_triggers_0x18
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 36
      mu_version_hash:
        value: 0x38_4f_76_67
  genesys__gen__challenge_action__speed_camera_action:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: on_hit_sequence_0x4c
        type: u4
      - id: ptr_genesys__gen__challenge__location_0x50
        type: u4
    instances:
      inst_genesys__gen__challenge__location_0x50:
        pos: ptr_genesys__gen__challenge__location_0x50
        type: genesys__gen__challenge__location
      size:
        value: 88
      mu_version_hash:
        value: 0xe3_e6_76_a8
  genesys__gen__game_mode:
    seq:
      - id: base_object
        type: gen_obj
      - id: maps_acceptors_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: description_0x14
        type: u4
      - id: game_changer_id_0x18
        type: u4
      - id: hsm_0x1c
        type: u4
      - id: hud__hsm_0x20
        type: u4
      - id: intro_0x24
        type: u4
      - id: mix_snap_shot_0x28
        type: u4
      - id: cgs_core__unique_id_0x2c
        type: u4
      - id: name_0x30
        type: u4
      - id: results_sequence_0x34
        type: u4
      - id: score_view_model_0x38
        type: u4
      - id: cgs_core__unique_id_0x3c
        type: u4
      - id: weapon_list_0x40
        type: u4
      - id: float32_t_0x44
        type: f4
      - id: mode_intro_time_limit_0x48
        type: f4
      - id: mode_time_limit_0x4c
        type: f4
      - id: timeout_time_0x50
        type: f4
      - id: on_bust_0x54
        type: u2
        doc: enum; 13_94_0e_00
      - id: ranking_type_0x56
        type: u2
        doc: enum; 0e_f7_05_00
      - id: unk_enum_0x58
        type: u2
        doc: enum; 42_f3_0e_00
      - id: intercepting_cop_frequency_0x5a
        type: u2
      - id: minimap_distance_0x5c
        type: u2
      - id: mode_score_limit_0x5e
        type: u2
      - id: oncoming_cop_frequency_0x60
        type: u2
      - id: trailing_cop_frequency_0x62
        type: u2
      - id: uint16_t_0x64
        type: u2
      - id: allow_airacer_damage_from_world_0x66
        type: u1
      - id: allow_friendly_fire_0x67
        type: u1
      - id: bool8_t_0x68
        type: u1
      - id: bool8_t_0x69
        type: u1
      - id: host_can_end_game_0x6a
        type: u1
      - id: online_0x6b
        type: u1
      - id: retry_enabled_0x6c
        type: u1
      - id: bool8_t_0x6d
        type: u1
      - id: show_checkpoints_0x6e
        type: u1
      - id: bool8_t_0x6f
        type: u1
      - id: spawn_towards_ai_0x70
        type: u1
      - id: team_game_0x71
        type: u1
      - id: timer_counts_up_0x72
        type: u1
      - id: bool8_t_0x73
        type: u1
      - id: bool8_t_0x74
        type: u1
      - id: feedback_group_id_0x75
        type: u1
      - id: padding
        size: 2
    instances:
      size:
        value: 120
      mu_version_hash:
        value: 0x9e_7a_d5_e2
  genesys__gen__custom_chevron:
    seq:
      - id: base_object
        type: gen_obj
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
      mu_version_hash:
        value: 0xac_a9_15_3e
  genesys__gen__event:
    seq:
      - id: base_object
        type: gen_obj
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
      mu_version_hash:
        value: 0xb8_25_62_0e
  genesys__gen__online_event:
    seq:
      - id: base_object
        type: genesys__gen__event
      - id: inline_arr_float32_t_0x4c
        type: f4
        repeat: expr
        repeat-expr: 2
      - id: arena_0x54
        type: u4
      - id: cgs_core__unique_id_0x58
        type: u4
      - id: cgs_core__unique_id_0x5c
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x60
        type: u4
      - id: route_0x64
        type: u4
      - id: array_count_for_0x4c
        type: u2
      - id: array_count_for_0x60
        type: u2
      - id: requires_airport_0x6c
        type: u1
      - id: padding
        size: 3
    instances:
      inst_cgs_core__unique_id_0x60:
        pos: ptr_arr_cgs_core__unique_id_0x60
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x60
      size:
        value: 112
      mu_version_hash:
        value: 0x17_73_05_4a
  genesys__gen__event_arena_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: loading__point__location_0x10
        type: u4
      - id: ptr_arr_lockdown_points_0x14
        type: u4
      - id: ptr_arr_point_to_point_checkpoints_0x18
        type: u4
      - id: ptr_arr_repair_points_0x1c
        type: u4
      - id: ptr_arr_spawn__locations_0x20
        type: u4
      - id: vista_camera_location_0x24
        type: u4
      - id: ptr_arr_ptr_chevrons_0x28
        type: u4
      - id: ptr_arr_ptr_custom_chevron_list_0x2c
        type: u4
      - id: ptr_arr_team_spawn_locations_0x30
        type: u4
      - id: array_count_for_0x28
        type: u2
        doc: '"ChevronsCount"'
      - id: array_count_for_0x14
        type: u2
        doc: '"LockdownPointsCount"'
      - id: array_count_for_0x18
        type: u2
        doc: '"PointToPointCheckpointsCount"'
      - id: array_count_for_0x1c
        type: u2
        doc: '"RepairPointsCount"'
      - id: array_count_for_0x20
        type: u2
        doc: '"Spawn_LocationsCount"'
      - id: array_count_for_0x30
        type: u2
        doc: '"TeamSpawnLocationsCount"'
      - id: array_count_for_0x2c
        type: u1
        doc: '"CustomChevronListCount"'
      - id: padding
        size: 3
    instances:
      inst_lockdown_points_0x14:
        pos: ptr_arr_lockdown_points_0x14
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_point_to_point_checkpoints_0x18:
        pos: ptr_arr_point_to_point_checkpoints_0x18
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x18
      inst_repair_points_0x1c:
        pos: ptr_arr_repair_points_0x1c
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x1c
      inst_spawn__locations_0x20:
        pos: ptr_arr_spawn__locations_0x20
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x20
      inst_chevrons_0x28:
        pos: ptr_arr_ptr_chevrons_0x28
        type: ptr('genesys__gen__chevron')
        repeat: expr
        repeat-expr: array_count_for_0x28
      inst_custom_chevron_list_0x2c:
        pos: ptr_arr_ptr_custom_chevron_list_0x2c
        type: ptr('genesys__gen__custom_chevron')
        repeat: expr
        repeat-expr: array_count_for_0x2c
      inst_team_spawn_locations_0x30:
        pos: ptr_arr_team_spawn_locations_0x30
        type: genesys__gen__event_arena_data__spawn_point_collection
        repeat: expr
        repeat-expr: array_count_for_0x30
      size:
        value: 68
      mu_version_hash:
        value: 0x87_56_5a_00
  genesys__gen__event_arena:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: image_0x10
        type: u4
      - id: map_0x14
        type: u4
      - id: name_0x18
        type: u4
      - id: world_0x1c
        type: u4
      - id: ptr_arena_data_0x20
        type: u4
    instances:
      inst_arena_data_0x20:
        pos: ptr_arena_data_0x20
        type: genesys__gen__event_arena_data
      size:
        value: 40
      mu_version_hash:
        value: 0xf4_84_79_01
  genesys__gen__challenge_action__jump_stats:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
    instances:
      size:
        value: 80
      mu_version_hash:
        value: 0xc8_ac_8f_6a
  int32_t:
    seq: []
    instances: {}
  genesys__gen__offline_event__alternate_routes:
    seq:
      - id: base_object
        type: gen_obj
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
      mu_version_hash:
        value: 0x1b_33_ec_c5
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
      mu_version_hash:
        value: 0x95_fb_ea_be
  genesys__gen__gameplay__condition:
    seq:
      - id: base_object
        type: gen_obj
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
      mu_version_hash:
        value: 0x71_52_42_99
  genesys__gen__score_view_model__score:
    seq:
      - id: base_object
        type: gen_obj
      - id: action_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: string_0x14
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x7b_fb_67_04
  genesys__gen__score_view_model:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_scores_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"ScoresCount"'
      - id: padding
        size: 2
    instances:
      inst_scores_0x10:
        pos: ptr_arr_scores_0x10
        type: genesys__gen__score_view_model__score
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x45_d1_c4_27
  genesys__gen__score_view_model__score_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_path_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: rank_0x18
        type: s4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x24_2c_b4_ca
  genesys__gen__challenge_action__accumulate_near_misses:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: ptr_location_0x4c
        type: u4
      - id: in_air_0x50
        type: u1
      - id: padding
        size: 3
    instances:
      inst_location_0x4c:
        pos: ptr_location_0x4c
        type: genesys__gen__challenge__location
      size:
        value: 84
      mu_version_hash:
        value: 0x2b_a8_0e_31
  genesys__gen__event__checkpoint_info:
    seq:
      - id: base_object
        type: gen_obj
      - id: sequence_0xc
        type: u4
      - id: show_split_time_0x10
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0x99_45_25_4c
  cgs_resource__handle:
    seq: []
    instances: {}
  genesys__gen__offline_event__aiplayer_information:
    seq:
      - id: base_object
        type: gen_obj
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
      mu_version_hash:
        value: 0x24_b9_40_8f
  genesys__gen__offline_event__custom_chevrons:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_arr_float32_t_0xc
        type: u4
      - id: ptr_arr_float32_t_0x10
        type: u4
      - id: ptr_arr_float32_t_0x14
        type: u4
      - id: array_count_for_0xc
        type: u2
      - id: array_count_for_0x10
        type: u2
      - id: array_count_for_0x14
        type: u2
      - id: padding
        size: 2
    instances:
      inst_float32_t_0xc:
        pos: ptr_arr_float32_t_0xc
        type: f4
        repeat: expr
        repeat-expr: array_count_for_0xc
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
      size:
        value: 32
      mu_version_hash:
        value: 0x20_55_7e_9d
  genesys__gen__challenge_action__coop_accumulate_distance:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: padding
        size: 2
    instances:
      size:
        value: 76
      mu_version_hash:
        value: 0x79_8b_78_5d
  genesys__gen__challenge_action__car_state:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: max_speed_0x54
        type: u2
      - id: min_speed_0x56
        type: u2
      - id: bool8_t_0x58
        type: u1
      - id: bool8_t_0x59
        type: u1
      - id: bool8_t_0x5a
        type: u1
      - id: donutting_0x5b
        type: u1
      - id: drifting_0x5c
        type: u1
      - id: in_air_0x5d
        type: u1
      - id: nitrous_0x5e
        type: u1
      - id: bool8_t_0x5f
        type: u1
      - id: reversing_0x60
        type: u1
      - id: slipstreaming_0x61
        type: u1
      - id: padding
        size: 2
    instances:
      size:
        value: 100
      mu_version_hash:
        value: 0x0a_5f_28_ef
  genesys__gen__challenge_action__accumulate_time:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: padding
        size: 2
    instances:
      size:
        value: 76
      mu_version_hash:
        value: 0x47_de_09_5b
  genesys__gen__challenge_action__accumulate_distance:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: padding
        size: 2
    instances:
      size:
        value: 76
      mu_version_hash:
        value: 0xe3_70_b2_cc
  genesys__gen__offline_event__checkpoint_info:
    seq:
      - id: base_object
        type: gen_obj
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
      mu_version_hash:
        value: 0x99_ef_67_0a
  genesys__gen__online__vote_event:
    seq:
      - id: base_object
        type: genesys__gen__online_event
      - id: cgs_core__unique_id_0x70
        type: u4
      - id: cgs_core__unique_id_0x74
        type: u4
      - id: cgs_core__unique_id_0x78
        type: u4
      - id: cgs_core__unique_id_0x7c
        type: u4
    instances:
      size:
        value: 132
      mu_version_hash:
        value: 0xba_f7_b2_c9
  genesys__gen__challenge__challenge_part:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: instruction_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: short_instruction_0x1c
        type: u4
      - id: ptr_arr_ptr_actions_0x20
        type: u4
      - id: unk_enum_0x24
        type: u2
        doc: enum; 53_37_11_00
      - id: unk_enum_0x26
        type: u2
        doc: enum; 58_39_11_00
      - id: uint16_t_0x28
        type: u2
      - id: bool8_t_0x2a
        type: u1
      - id: array_count_for_0x20
        type: u1
        doc: '"ActionsCount"'
    instances:
      inst_actions_0x20:
        pos: ptr_arr_ptr_actions_0x20
        type: ptr('genesys__gen__challenge_action__action_base')
        repeat: expr
        repeat-expr: array_count_for_0x20
      size:
        value: 48
      mu_version_hash:
        value: 0xd6_0e_28_e0
  genesys__gen__challenge__online_challenge:
    seq:
      - id: base_object
        type: genesys__gen__online_event
      - id: intro_0x70
        type: u4
      - id: deallocated_nodule_0x74
        type: u4
      - id: ptr_arr_ptr_parts_0x78
        type: u4
      - id: elimination_type_0x7c
        type: u2
        doc: enum; ff_f8_17_00
      - id: type_0x7e
        type: u2
        doc: enum; c3_38_11_00
      - id: array_count_for_0x78
        type: u1
        doc: '"PartsCount"'
      - id: padding
        size: 3
    instances:
      inst_parts_0x78:
        pos: ptr_arr_ptr_parts_0x78
        type: ptr('genesys__gen__challenge__challenge_part')
        repeat: expr
        repeat-expr: array_count_for_0x78
      size:
        value: 132
      mu_version_hash:
        value: 0x7e_70_16_62
  genesys__gen__challenge_action__get_to_location:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: route_location_0x4c
        type: u1
      - id: bool8_t_0x4d
        type: u1
      - id: padding
        size: 2
    instances:
      size:
        value: 80
      mu_version_hash:
        value: 0xb3_b4_2a_12
  genesys__gen__race_balancing_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: extra_crash_schedule_time_0x10
        type: f4
      - id: extra_schedule_time_0x14
        type: f4
      - id: ptr_arr_opponent_data_0x18
        type: u4
      - id: array_count_for_0x18
        type: u2
        doc: '"OpponentDataCount"'
      - id: padding
        size: 2
    instances:
      inst_opponent_data_0x18:
        pos: ptr_arr_opponent_data_0x18
        type: genesys__gen__race_balancing_data__opponent_balancing_data
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 32
      mu_version_hash:
        value: 0xb6_1c_c0_be
  genesys__gen__challenge_action__jump_over_players:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: bool8_t_0x4c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 80
      mu_version_hash:
        value: 0x3f_12_39_21
  genesys__gen__race_balancing_profile:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: max_speed_0x10
        type: f4
      - id: min_speed_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xa5_81_c6_d9
  genesys__gen__challenge_action__do_jump:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: accumulate_0x4c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 80
      mu_version_hash:
        value: 0x63_66_35_21
  genesys__gen__challenge_action__hit_trigger:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
    instances:
      size:
        value: 80
      mu_version_hash:
        value: 0xc0_99_71_a8
  genesys__object:
    seq: []
    instances: {}
  genesys__gen__offline_event:
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
      mu_version_hash:
        value: 0x90_3b_cc_47
  gen_obj:
    seq:
      - id: dynamic_gamedata
        size: 8
      - id: mu_type_version
        type: u4be
    instances: {}
  genesys__gen__challenge_action__speed_run:
    seq:
      - id: base_object
        type: genesys__gen__challenge_action__action_base
      - id: route_count_0x50
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 84
      mu_version_hash:
        value: 0xd7_8c_a2_95
  rw_math_vpu__vector4:
    seq:
      - id: inline_arr_elements_0x0
        type: f4
        repeat: expr
        repeat-expr: 4
    instances:
      size:
        value: 8
      mu_version_hash:
        value: 0xc2_29_a8_2f
  genesys__gen__behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: label_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: activate_on_hit_0x18
        type: u1
      - id: deactivate_on_hit_0x19
        type: u1
      - id: initially_on_0x1a
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x09_97_15_d1
  genesys__gen__wcremove_world_entity_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x3e_e2_74_05
  genesys__gen__corona__glow:
    seq:
      - id: base_object
        type: gen_obj
      - id: unk_enum_0x10
        type: u1
        doc: enum; 93_32_00_00_0_1
      - id: colour_0xa0
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0xb0
        type: rw_math_vpu__vector4
      - id: material_0xc0
        size: 8
      - id: depth_bias_0xc8
        type: f4
      - id: rotation_offset_0xcc
        type: f4
      - id: render_buffer_0xd0
        type: u4
        doc: enum; 2a_be_07_00
    instances:
      size:
        value: 216
      mu_version_hash:
        value: 0xb5_41_c3_e9
  genesys__gen__wcvfx_behaviour__coronas:
    seq:
      - id: base_object
        type: gen_obj
      - id: corona_definition_0xc
        size: 8
      - id: locator_group_0x14
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x1c_74_fd_f8
  genesys__gen__corona__beam:
    seq:
      - id: base_object
        type: gen_obj
      - id: unk_enum_0x10
        type: u1
        doc: enum; 93_32_00_00_0_1
      - id: colour_0xa0
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0xb0
        type: rw_math_vpu__vector4
      - id: material_0xc0
        size: 8
      - id: end_radius_0xc8
        type: f4
      - id: start_radius_0xcc
        type: f4
      - id: render_buffer_0xd0
        type: u4
        doc: enum; 2a_be_07_00
    instances:
      size:
        value: 216
      mu_version_hash:
        value: 0xc9_34_b7_bf
  genesys__gen__wcvfx_behaviour__spot_effects:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: locator_group_0x14
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x83_9e_a4_f9
  genesys__gen__corona__flare:
    seq:
      - id: base_object
        type: gen_obj
      - id: unk_enum_0x10
        type: u1
        doc: enum; 93_32_00_00_0_1
      - id: colour_0xa0
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0xb0
        type: rw_math_vpu__vector4
      - id: material_0xc0
        size: 8
      - id: position_0xc8
        type: f4
      - id: rotation_offset_0xcc
        type: f4
      - id: render_buffer_0xd0
        type: u4
        doc: enum; 2a_be_07_00
    instances:
      size:
        value: 216
      mu_version_hash:
        value: 0xc8_1a_ca_2a
  genesys__gen__wcvfx_behaviour__lights:
    seq:
      - id: base_object
        type: gen_obj
      - id: light_definition_0xc
        size: 8
      - id: locator_group_0x14
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xc0_7e_ea_42
  genesys__gen__wcplay_sound_behaviour__prop_surface_sound:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: surface_0x10
        type: u4
      - id: ptr_arr_rolling__waves_0x14
        type: u4
      - id: ptr_arr_scraping__waves_0x18
        type: u4
      - id: ptr_arr_waves_0x1c
        type: u4
      - id: array_count_for_0x14
        type: u2
      - id: array_count_for_0x18
        type: u2
      - id: array_count_for_0x1c
        type: u2
        doc: '"WavesCount"'
      - id: padding
        size: 2
    instances:
      inst_rolling__waves_0x14:
        pos: ptr_arr_rolling__waves_0x14
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_scraping__waves_0x18:
        pos: ptr_arr_scraping__waves_0x18
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x18
      inst_waves_0x1c:
        pos: ptr_arr_waves_0x1c
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 40
      mu_version_hash:
        value: 0xb9_ac_70_67
  genesys__gen__physical_definition__rigid_body__box_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: halfsize_0x50
        type: rw_math_vpu__vector3
      - id: game_changer_id_0x60
        type: u4
      - id: i6je_0x64
        type: s4
    instances:
      size:
        value: 108
      mu_version_hash:
        value: 0x28_77_c8_41
  genesys__gen__physical_definition__rigid_body__capsule_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: game_changer_id_0x50
        type: u4
      - id: half_length_0x54
        type: f4
      - id: radius_0x58
        type: f4
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0x01_12_fc_16
  genesys__gen__physical_definition__rigid_body__convex_hull_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: convex_hull_0x50
        size: 8
      - id: game_changer_id_0x58
        type: u4
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0x63_33_d3_31
  genesys__gen__physical_definition__rigid_body__cylinder_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: game_changer_id_0x50
        type: u4
      - id: half_length_0x54
        type: f4
      - id: radius_0x58
        type: f4
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0x01_12_fc_16
  genesys__gen__physical_definition__rigid_body__sphere_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: game_changer_id_0x50
        type: u4
      - id: radius_0x54
        type: f4
    instances:
      size:
        value: 92
      mu_version_hash:
        value: 0xf9_19_5e_af
  genesys__gen__physical_definition__rigid_body:
    seq:
      - id: base_object
        type: gen_obj
      - id: body_to_object_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: com_offset_0x50
        type: rw_math_vpu__vector3
      - id: inertia__scale_0x60
        type: rw_math_vpu__vector3
      - id: local_aabbcenter_0x70
        type: rw_math_vpu__vector3
      - id: local_aabbhalf_diagonal_0x80
        type: rw_math_vpu__vector3
      - id: ptr_arr_symmetrical_in_axis_0x90
        type: u4
      - id: game_changer_id_0x94
        type: u4
      - id: angular_drag_0x98
        type: f4
      - id: bounciness_0x9c
        type: f4
      - id: friction_0xa0
        type: f4
      - id: linear_drag_0xa4
        type: f4
      - id: mass_0xa8
        type: f4
      - id: ptr_arr_box_volumes_0xac
        type: u4
      - id: ptr_arr_capsule_volumes_0xb0
        type: u4
      - id: ptr_bounding_convex_hull_0xb4
        type: u4
      - id: ptr_arr_convex_hull_volumes_0xb8
        type: u4
      - id: ptr_arr_cylinder_volumes_0xbc
        type: u4
      - id: ptr_arr_sphere_volumes_0xc0
        type: u4
      - id: array_count_for_0xac
        type: u2
        doc: '"BoxVolumesCount"'
      - id: array_count_for_0xb0
        type: u2
        doc: '"CapsuleVolumesCount"'
      - id: array_count_for_0xb8
        type: u2
        doc: '"ConvexHullVolumesCount"'
      - id: array_count_for_0xbc
        type: u2
        doc: '"CylinderVolumesCount"'
      - id: array_count_for_0xc0
        type: u2
        doc: '"SphereVolumesCount"'
      - id: array_count_for_0x90
        type: u2
        doc: '"SymmetricalInAxisCount"'
      - id: is_wheel_0xd0
        type: u1
      - id: padding
        size: 3
    instances:
      inst_symmetrical_in_axis_0x90:
        pos: ptr_arr_symmetrical_in_axis_0x90
        type: u1
        repeat: expr
        repeat-expr: array_count_for_0x90
      inst_box_volumes_0xac:
        pos: ptr_arr_box_volumes_0xac
        type: genesys__gen__physical_definition__rigid_body__box_volume
        repeat: expr
        repeat-expr: array_count_for_0xac
      inst_capsule_volumes_0xb0:
        pos: ptr_arr_capsule_volumes_0xb0
        type: genesys__gen__physical_definition__rigid_body__capsule_volume
        repeat: expr
        repeat-expr: array_count_for_0xb0
      inst_bounding_convex_hull_0xb4:
        pos: ptr_bounding_convex_hull_0xb4
        type: genesys__gen__physical_definition__rigid_body__convex_hull_volume
      inst_convex_hull_volumes_0xb8:
        pos: ptr_arr_convex_hull_volumes_0xb8
        type: genesys__gen__physical_definition__rigid_body__convex_hull_volume
        repeat: expr
        repeat-expr: array_count_for_0xb8
      inst_cylinder_volumes_0xbc:
        pos: ptr_arr_cylinder_volumes_0xbc
        type: genesys__gen__physical_definition__rigid_body__cylinder_volume
        repeat: expr
        repeat-expr: array_count_for_0xbc
      inst_sphere_volumes_0xc0:
        pos: ptr_arr_sphere_volumes_0xc0
        type: genesys__gen__physical_definition__rigid_body__sphere_volume
        repeat: expr
        repeat-expr: array_count_for_0xc0
      size:
        value: 212
      mu_version_hash:
        value: 0x5d_6d_83_cc
  genesys__gen__physical_definition:
    seq:
      - id: base_object
        type: gen_obj
      - id: local_aabbcenter_0x10
        type: rw_math_vpu__vector3
      - id: local_aabbhalf_diagonal_0x20
        type: rw_math_vpu__vector3
      - id: additional_info_0x30
        size: 8
      - id: ptr_arr_rigid_bodies_names_0x38
        type: u4
      - id: game_changer_id_0x3c
        type: u4
      - id: ptr_arr_rigid_bodies_0x40
        type: u4
      - id: game_changer_id_0x44
        type: s4
      - id: main_rigid_body_index_0x48
        type: s4
      - id: array_count_for_0x40
        type: u2
        doc: '"RigidBodiesCount"'
      - id: array_count_for_0x38
        type: u2
        doc: '"RigidBodiesNamesCount"'
      - id: bool8_t_0x50
        type: u1
      - id: bool8_t_0x51
        type: u1
      - id: padding
        size: 2
    instances:
      inst_rigid_bodies_names_0x38:
        pos: ptr_arr_rigid_bodies_names_0x38
        type: string_base
        repeat: expr
        repeat-expr: array_count_for_0x38
      inst_rigid_bodies_0x40:
        pos: ptr_arr_rigid_bodies_0x40
        type: genesys__gen__physical_definition__rigid_body
        repeat: expr
        repeat-expr: array_count_for_0x40
      size:
        value: 84
      mu_version_hash:
        value: 0x96_2d_8d_39
  rw_math_vpu__vector3:
    seq:
      - id: inline_arr_elements_0x0
        type: f4
        repeat: expr
        repeat-expr: 3
    instances:
      size:
        value: 8
      mu_version_hash:
        value: 0xa5_f5_99_f3
  rw_math_vpu__matrix44affine:
    seq:
      - id: inline_arr_elements_0x0
        type: rw_math_vpu__vector4
        repeat: expr
        repeat-expr: 4
    instances:
      size:
        value: 8
      mu_version_hash:
        value: 0xb6_8b_60_0e
  genesys__gen__make_physical_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: unk_enum_0x1c
        type: u2
        doc: enum; a3_37_09_00
      - id: collidable_0x1e
        type: u1
      - id: initially_frozen_0x1f
        type: u1
      - id: bool8_t_0x20
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xe1_d5_78_1c
  genesys__gen__corona:
    seq:
      - id: base_object
        type: gen_obj
      - id: unk_enum_0x10
        type: u1
        doc: enum; 93_32_00_00_0_1
      - id: game_changer_id_0xa0
        type: u4
      - id: float32_t_0xa4
        type: f4
      - id: max_visible_distance_0xa8
        type: f4
      - id: visibility_test_depth_bias_0xac
        type: f4
      - id: ptr_arr_beams_0xb0
        type: u4
      - id: ptr_arr_flares_0xb4
        type: u4
      - id: ptr_arr_env_map_glows_0xb8
        type: u4
      - id: ptr_arr_glows_0xbc
        type: u4
      - id: ptr_arr_planar_reflection_glows_0xc0
        type: u4
      - id: ptr_arr_rear_view_mirror_glows_0xc4
        type: u4
      - id: flags_0xc8
        type: u2
        doc: enum; b3_27_00_00_0_2
      - id: array_count_for_0xb0
        type: u2
        doc: '"BeamsCount"'
      - id: array_count_for_0xb8
        type: u2
        doc: '"EnvMapGlowsCount"'
      - id: array_count_for_0xb4
        type: u2
        doc: '"FlaresCount"'
      - id: array_count_for_0xbc
        type: u2
        doc: '"GlowsCount"'
      - id: array_count_for_0xc0
        type: u2
        doc: '"PlanarReflectionGlowsCount"'
      - id: array_count_for_0xc4
        type: u2
        doc: '"RearViewMirrorGlowsCount"'
      - id: padding
        size: 2
    instances:
      inst_beams_0xb0:
        pos: ptr_arr_beams_0xb0
        type: genesys__gen__corona__beam
        repeat: expr
        repeat-expr: array_count_for_0xb0
      inst_flares_0xb4:
        pos: ptr_arr_flares_0xb4
        type: genesys__gen__corona__flare
        repeat: expr
        repeat-expr: array_count_for_0xb4
      inst_env_map_glows_0xb8:
        pos: ptr_arr_env_map_glows_0xb8
        type: genesys__gen__corona__glow
        repeat: expr
        repeat-expr: array_count_for_0xb8
      inst_glows_0xbc:
        pos: ptr_arr_glows_0xbc
        type: genesys__gen__corona__glow
        repeat: expr
        repeat-expr: array_count_for_0xbc
      inst_planar_reflection_glows_0xc0:
        pos: ptr_arr_planar_reflection_glows_0xc0
        type: genesys__gen__corona__glow
        repeat: expr
        repeat-expr: array_count_for_0xc0
      inst_rear_view_mirror_glows_0xc4:
        pos: ptr_arr_rear_view_mirror_glows_0xc4
        type: genesys__gen__corona__glow
        repeat: expr
        repeat-expr: array_count_for_0xc4
      size:
        value: 216
      mu_version_hash:
        value: 0x49_97_64_c1
  genesys__gen__wcplay_sound_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: offset_0x20
        type: rw_math_vpu__vector3
      - id: mixer_channel_0x30
        size: 8
      - id: ptr_arr_cgs_resource__handle_0x38
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x3c
        type: u4
      - id: ptr_arr_surface__collisions_0x40
        type: u4
      - id: array_count_for_0x38
        type: u2
      - id: array_count_for_0x3c
        type: u2
      - id: array_count_for_0x40
        type: u2
      - id: padding
        size: 2
    instances:
      inst_cgs_resource__handle_0x38:
        pos: ptr_arr_cgs_resource__handle_0x38
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x38
      inst_cgs_resource__handle_0x3c:
        pos: ptr_arr_cgs_resource__handle_0x3c
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x3c
      inst_surface__collisions_0x40:
        pos: ptr_arr_surface__collisions_0x40
        type: genesys__gen__wcplay_sound_behaviour__prop_surface_sound
        repeat: expr
        repeat-expr: array_count_for_0x40
      size:
        value: 76
      mu_version_hash:
        value: 0xfb_72_73_f3
  genesys__gen__wcvfx_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: impact_effect_0x1c
        size: 8
      - id: cgs_resource__handle_0x24
        size: 8
      - id: flash_frequency_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: nonprocedurally_slocum_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: ptr_arr_coronas_0x40
        type: u4
      - id: ptr_arr_lights_0x44
        type: u4
      - id: ptr_arr_genesys__gen__wcvfx_behaviour__spot_effects_0x48
        type: u4
      - id: int32_t_0x4c
        type: s4
      - id: int32_t_0x50
        type: s4
      - id: array_count_for_0x40
        type: u2
        doc: '"CoronasCount"'
      - id: array_count_for_0x44
        type: u2
        doc: '"LightsCount"'
      - id: array_count_for_0x48
        type: u2
      - id: bool8_t_0x5a
        type: u1
      - id: bool8_t_0x5b
        type: u1
      - id: bool8_t_0x5c
        type: u1
      - id: bool8_t_0x5d
        type: u1
      - id: bool8_t_0x5e
        type: u1
      - id: bool8_t_0x5f
        type: u1
      - id: bool8_t_0x60
        type: u1
      - id: bool8_t_0x61
        type: u1
      - id: bool8_t_0x62
        type: u1
      - id: bool8_t_0x63
        type: u1
      - id: bool8_t_0x64
        type: u1
      - id: bool8_t_0x65
        type: u1
      - id: bool8_t_0x66
        type: u1
      - id: bool8_t_0x67
        type: u1
      - id: bool8_t_0x68
        type: u1
      - id: bool8_t_0x69
        type: u1
      - id: bool8_t_0x6a
        type: u1
      - id: bool8_t_0x6b
        type: u1
    instances:
      inst_coronas_0x40:
        pos: ptr_arr_coronas_0x40
        type: genesys__gen__wcvfx_behaviour__coronas
        repeat: expr
        repeat-expr: array_count_for_0x40
      inst_lights_0x44:
        pos: ptr_arr_lights_0x44
        type: genesys__gen__wcvfx_behaviour__lights
        repeat: expr
        repeat-expr: array_count_for_0x44
      inst_genesys__gen__wcvfx_behaviour__spot_effects_0x48:
        pos: ptr_arr_genesys__gen__wcvfx_behaviour__spot_effects_0x48
        type: genesys__gen__wcvfx_behaviour__spot_effects
        repeat: expr
        repeat-expr: array_count_for_0x48
      size:
        value: 112
      mu_version_hash:
        value: 0xce_85_d4_17
  genesys__gen__dsp_plug_in:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: output__channels_0x10
        type: u4
        doc: enum; e4_33_07_00
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x50_e0_3c_00
  genesys__gen__pan2ddsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xe5_fe_f6_15
  genesys__gen__sequence_item__modulating_double_value:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_0xc
        type: string_base
      - id: binding__exponent_0x14
        type: f4
      - id: binding__range__max_0x18
        type: f4
      - id: binding__range__min_0x1c
        type: f4
      - id: output__value__max_0x20
        type: f4
      - id: output__value__min_0x24
        type: f4
      - id: value_0x28
        type: f4
      - id: unk_enum_0x2c
        type: u4
        doc: enum; 5a_f6_03_00_0_1
      - id: animation__modulation__type_0x30
        type: u2
        doc: enum; 5b_f6_03_00
      - id: binding__modulation__type_0x32
        type: u2
        doc: enum; 5b_f6_03_00
      - id: array_count_for_0x2c
        type: u2
      - id: bool8_t_0x36
        type: u1
      - id: binding__invert_0x37
        type: u1
    instances:
      inst_5a__f6_03_00_0_1_0x2c:
        pos: unk_enum_0x2c
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x2c
      size:
        value: 60
      mu_version_hash:
        value: 0x58_c7_6e_0d
  genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value:
    seq:
      - id: base_object
        type: gen_obj
      - id: plug_in_0xc
        type: u4
      - id: plug_in__type_0x10
        type: u4
      - id: ptr_arr_sound_distance_falloff_0x14
        type: u4
      - id: ptr_value_0x18
        type: u4
      - id: parameter__name_0x1c
        type: u4
      - id: automated__property_0x20
        type: u2
        doc: enum; 29_f7_03_00
      - id: array_count_for_0x14
        type: u1
      - id: padding
        size: 1
    instances:
      inst_sound_distance_falloff_0x14:
        pos: ptr_arr_sound_distance_falloff_0x14
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_value_0x18:
        pos: ptr_value_0x18
        type: genesys__gen__sequence_item__modulating_double_value
      size:
        value: 36
      mu_version_hash:
        value: 0x75_40_01_39
  genesys__gen__voice_group:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: instance_limit_0x10
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0x62_b3_c0_62
  genesys__gen__mixer_channel__priority:
    seq:
      - id: base_object
        type: gen_obj
      - id: priority_0xc
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 16
      mu_version_hash:
        value: 0x85_39_5f_b3
  genesys__gen__post_fx_keyframe__bloom:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: game_changer_id_0x20
        type: u4
      - id: dark_bloom_weight_0x24
        type: f4
      - id: dark_bloom_white_point_0x28
        type: f4
      - id: large_weight_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: medium_weight_0x34
        type: f4
      - id: saturation_0x38
        type: f4
      - id: small_weight_0x3c
        type: f4
      - id: threshold_0x40
        type: f4
      - id: threshold_large_0x44
        type: f4
      - id: threshold_medium_0x48
        type: f4
    instances:
      size:
        value: 80
      mu_version_hash:
        value: 0xd6_1a_73_ed
  rw_math_vpu__vector2:
    seq:
      - id: inline_arr_elements_0x0
        type: f4
        repeat: expr
        repeat-expr: 2
    instances:
      size:
        value: 8
      mu_version_hash:
        value: 0x2e_e7_6e_33
  genesys__gen__post_fx_keyframe__vignette:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector2_0x10
        type: rw_math_vpu__vector2
      - id: scale_0x20
        type: rw_math_vpu__vector2
      - id: rw_math_vpu__vector4_0x30
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x40
        type: rw_math_vpu__vector4
      - id: game_changer_id_0x50
        type: u4
      - id: float32_t_0x54
        type: f4
      - id: fisheye_power_0x58
        type: f4
      - id: fisheye_scale_0x5c
        type: f4
      - id: fisheye_warp_0x60
        type: f4
      - id: sharpness_0x64
        type: f4
    instances:
      size:
        value: 108
      mu_version_hash:
        value: 0xbd_8f_1f_f0
  genesys__gen__post_fx_keyframe__general:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: car_motion_blur_0x10
        type: f4
      - id: world_colour_cube_weight_0x14
        type: f4
      - id: world_motion_blur_0x18
        type: f4
      - id: world_saturation_0x1c
        type: f4
      - id: unk_enum_0x20
        type: u4
        doc: enum; 35_30_00_00
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xf3_88_bb_fd
  genesys__gen__sequence_item:
    seq:
      - id: base_object
        type: gen_obj
      - id: enabled_binding_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: end_time_0x18
        type: f4
      - id: start_time_0x1c
        type: f4
      - id: unk_enum_0x20
        type: u4
        doc: enum; d0_39_0b_00
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x6c_a8_bb_26
  genesys__gen__race_car_effect_sequence_item__effect_double_value:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_modulating_value_0xc
        type: u4
      - id: automated__property_0x10
        type: u4
        doc: enum; 15_f7_03_00
    instances:
      inst_modulating_value_0xc:
        pos: ptr_modulating_value_0xc
        type: genesys__gen__sequence_item__modulating_double_value
      size:
        value: 24
      mu_version_hash:
        value: 0x6e_64_d0_2d
  genesys__gen__race_car_effect_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: ptr_arr_automated__values_0x2c
        type: u4
      - id: array_count_for_0x2c
        type: u2
        doc: '"Automated_ValuesCount"'
      - id: padding
        size: 2
    instances:
      inst_automated__values_0x2c:
        pos: ptr_arr_automated__values_0x2c
        type: genesys__gen__race_car_effect_sequence_item__effect_double_value
        repeat: expr
        repeat-expr: array_count_for_0x2c
      size:
        value: 52
      mu_version_hash:
        value: 0x09_ea_9b_a3
  genesys__gen__post_fx_keyframe__depth_of__field:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x5f_65_e8_33
  genesys__gen__peaking_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
      - id: gain_0x18
        type: f4
      - id: q_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xc2_89_6d_d9
  genesys__gen__post_fx_keyframe__stereo_3d:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: focus__distance_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x4e_ef_3c_c8
  genesys__gen__post_fxstate__colour_cube_settings:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_cube_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: zero__if__not__set_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x77_93_f8_32
  genesys__gen__post_fxstate__value_modifier:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: modification__value_0x10
        type: f4
      - id: modification__type_0x14
        type: u4
        doc: enum; 3d_30_00_00
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xf5_9a_d1_ea
  genesys__gen__heat_level_sound_set:
    seq:
      - id: base_object
        type: gen_obj
      - id: nitrous_dump_0xc
        size: 8
      - id: nitrous_local_0x14
        size: 8
      - id: game_changer_id_0x1c
        type: u4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x1b_30_82_d5
  genesys__gen__sound_distance_falloff:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: curve_type_0x10
        type: f4
      - id: curve_type_reverb_0x14
        type: f4
      - id: divergence_at_max_distance_0x18
        type: f4
      - id: divergence_at_min_distance_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: initial_gain_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: arrays_motioned_0x30
        type: f4
      - id: max_distance_0x34
        type: f4
      - id: max_distance_divergence_0x38
        type: f4
      - id: max_distance_reverb_0x3c
        type: f4
      - id: min_distance_0x40
        type: f4
      - id: min_distance_divergence_0x44
        type: f4
      - id: min_distance_reverb_0x48
        type: f4
      - id: occlusion_multiplier_0x4c
        type: f4
      - id: peak_gain_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: float32_t_0x58
        type: f4
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0x23_47_36_54
  genesys__gen__post_fxsequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: genesys__gen__sequence_item__modulating_double_value_0x5c
        type: genesys__gen__sequence_item__modulating_double_value
      - id: genesys__gen__sequence_item__modulating_double_value_0x94
        type: genesys__gen__sequence_item__modulating_double_value
      - id: genesys__gen__sequence_item__modulating_double_value_0xcc
        type: genesys__gen__sequence_item__modulating_double_value
      - id: cgs_core__string_base_0x104
        type: string_base
      - id: post_fxstate_0x10c
        size: 8
      - id: unk_enum_0x114
        type: u2
        doc: enum; 55_21_0a_00
      - id: override_intensity_0x116
        type: u1
      - id: endless__environment_0x117
        type: u1
    instances:
      size:
        value: 284
      mu_version_hash:
        value: 0xf0_56_15_02
  genesys__gen__wave_sequence_item__fade:
    seq:
      - id: base_object
        type: gen_obj
      - id: curve_0xc
        type: f4
      - id: time_0x10
        type: f4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x6b_f6_a4_ca
  genesys__gen__sequence_items__post_fx_override_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: automated__values_count_0x28
        type: u2
      - id: padding
        size: 2
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xda_65_11_74
  genesys__gen__sequence_items__post_fx_override_sequence_item__effect_double_value:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_modulating_value_0xc
        type: u4
      - id: automated__property_0x10
        type: u4
        doc: enum; 8f_7d_0f_00
    instances:
      inst_modulating_value_0xc:
        pos: ptr_modulating_value_0xc
        type: genesys__gen__sequence_item__modulating_double_value
      size:
        value: 24
      mu_version_hash:
        value: 0x61_e7_01_04
  genesys__gen__mixer_channel:
    seq:
      - id: base_object
        type: gen_obj
      - id: distance_falloff_0xc
        size: 8
      - id: plug_in__chain_0x14
        size: 8
      - id: game_changer_id_0x1c
        type: u4
      - id: mixing_group_0x20
        type: u4
      - id: centre_level_0x24
        type: f4
      - id: emitter_response_0x28
        type: f4
      - id: focus_0x2c
        type: f4
      - id: gain_0x30
        type: f4
      - id: lfe_send_0x34
        type: f4
      - id: panning__cosine_0x38
        type: f4
      - id: panning__divergence_0x3c
        type: f4
      - id: panning__sine_0x40
        type: f4
      - id: reverb_send_a_0x44
        type: f4
      - id: reverb_send_b_0x48
        type: f4
      - id: ptr_arr_priority_0x4c
        type: u4
      - id: ptr_voice_group_0x50
        type: u4
      - id: doppler_model_0x54
        type: u2
        doc: enum; 22_30_00_00
      - id: virtual_voice_behaviour_0x56
        type: u2
        doc: enum; 2a_6b_07_00
      - id: array_count_for_0x4c
        type: u2
        doc: '"PriorityCount"'
      - id: cull_playing_voices_0x5a
        type: u1
      - id: panning__override_0x5b
        type: u1
      - id: instance_limit_0x5c
        type: u1
      - id: padding
        size: 3
    instances:
      inst_priority_0x4c:
        pos: ptr_arr_priority_0x4c
        type: genesys__gen__mixer_channel__priority
        repeat: expr
        repeat-expr: array_count_for_0x4c
      inst_voice_group_0x50:
        pos: ptr_voice_group_0x50
        type: genesys__gen__voice_group
      size:
        value: 96
      mu_version_hash:
        value: 0xb1_24_9c_3f
  genesys__gen__mixing_group:
    seq:
      - id: base_object
        type: gen_obj
      - id: bus_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xf1_5e_68_36
  genesys__gen__high_pass_butterworth_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
      - id: order_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x42_35_4e_9f
  genesys__gen__sequence_timeline_controller:
    seq:
      - id: base_object
        type: gen_obj
      - id: enabled_binding_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: trigger_type_0x18
        type: u2
        doc: enum; 4a_63_04_00
      - id: test_continuously_0x1a
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xf2_75_9c_88
  genesys__gen__sequence:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: binding__max_0x18
        type: f4
      - id: binding__min_0x1c
        type: f4
      - id: ptr_arr_ptr_sequence_items_0x20
        type: u4
      - id: ptr_arr_ptr_timeline_controllers_0x24
        type: u4
      - id: default__progression__controller_0x28
        type: u2
        doc: enum; 83_f6_03_00
      - id: array_count_for_0x20
        type: u1
        doc: '"SequenceItemsCount"'
      - id: array_count_for_0x24
        type: u1
        doc: '"TimelineControllersCount"'
    instances:
      inst_sequence_items_0x20:
        pos: ptr_arr_ptr_sequence_items_0x20
        type: ptr('genesys__gen__sequence_item')
        repeat: expr
        repeat-expr: array_count_for_0x20
      inst_timeline_controllers_0x24:
        pos: ptr_arr_ptr_timeline_controllers_0x24
        type: ptr('genesys__gen__sequence_timeline_controller')
        repeat: expr
        repeat-expr: array_count_for_0x24
      size:
        value: 48
      mu_version_hash:
        value: 0xe9_14_f8_53
  genesys__gen__jump_timeline_controller:
    seq:
      - id: base_object
        type: genesys__gen__sequence_timeline_controller
      - id: destination_time_0x1c
        type: f4
      - id: trigger_time_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x06_e6_a5_18
  genesys__gen__sub_harmoniser_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x1d_2d_63_cb
  genesys__gen__delay_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
      - id: time_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xd8_3b_9e_56
  genesys__gen__quit_sequence_timeline_controller:
    seq:
      - id: base_object
        type: genesys__gen__jump_timeline_controller
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x67_21_89_d6
  genesys__gen__wave_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: pitch_0x5c
        type: genesys__gen__sequence_item__modulating_double_value
      - id: fade__in_0x94
        type: genesys__gen__wave_sequence_item__fade
      - id: fade__out_0xa8
        type: genesys__gen__wave_sequence_item__fade
      - id: snapshot__property_0xbc
        type: string_base
      - id: transform__override__binding_0xc4
        type: string_base
      - id: mixer__channel_0xcc
        size: 8
      - id: ptr_arr_waves_0xd4
        type: u4
      - id: ptr_arr_trigger__probability_0xd8
        type: u4
      - id: re_trigger_0xdc
        type: u2
        doc: enum; 85_8d_10_00
      - id: type_0xde
        type: u2
        doc: enum; c4_f3_03_00
      - id: auto__pitch_0xe0
        type: u1
      - id: array_count_for_0xd8
        type: u1
      - id: array_count_for_0xd4
        type: u1
        doc: '"WavesCount"'
      - id: padding
        size: 1
    instances:
      inst_waves_0xd4:
        pos: ptr_arr_waves_0xd4
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0xd4
      inst_trigger__probability_0xd8:
        pos: ptr_arr_trigger__probability_0xd8
        type: genesys__gen__sequence_item__modulating_double_value
        repeat: expr
        repeat-expr: array_count_for_0xd8
      size:
        value: 228
      mu_version_hash:
        value: 0x66_b0_22_3a
  genesys__gen__send_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
      - id: voice__routing_0x1c
        size: 8
      - id: gain_0x24
        type: f4
      - id: bus__routing_0x28
        type: u4
        doc: enum; b2_35_07_00
    instances:
      size:
        value: 48
      mu_version_hash:
        value: 0x17_88_5d_2b
  genesys__gen__post_fx_keyframe:
    seq:
      - id: base_object
        type: gen_obj
      - id: vignette_0x10
        type: genesys__gen__post_fx_keyframe__vignette
      - id: bloom_0x80
        type: genesys__gen__post_fx_keyframe__bloom
      - id: general_0xd0
        type: genesys__gen__post_fx_keyframe__general
      - id: genesys__gen__post_fx_keyframe__depth_of__field_0xf4
        type: genesys__gen__post_fx_keyframe__depth_of__field
      - id: stereo_3d_0x110
        type: genesys__gen__post_fx_keyframe__stereo_3d
      - id: game_changer_id_0x128
        type: u4
    instances:
      size:
        value: 304
      mu_version_hash:
        value: 0x5a_94_09_dc
  genesys__gen__post_fxstate:
    seq:
      - id: base_object
        type: gen_obj
      - id: inline_arr_colour_cubes_0xc
        type: genesys__gen__post_fxstate__colour_cube_settings
        repeat: expr
        repeat-expr: 2
      - id: bloom__value__modification_0x44
        type: genesys__gen__post_fxstate__value_modifier
      - id: colour__cube__value__modification_0x5c
        type: genesys__gen__post_fxstate__value_modifier
      - id: dof__value__modification_0x74
        type: genesys__gen__post_fxstate__value_modifier
      - id: general__value__modification_0x8c
        type: genesys__gen__post_fxstate__value_modifier
      - id: vignette__value__modification_0xa4
        type: genesys__gen__post_fxstate__value_modifier
      - id: activity_binding_0xbc
        type: string_base
      - id: keyframe_blend_binding_0xc4
        type: string_base
      - id: value_binding_0xcc
        type: string_base
      - id: key_frame1_0xd4
        size: 8
      - id: key_frame2_0xdc
        size: 8
      - id: game_changer_id_0xe4
        type: u4
      - id: rate_of_change_0xe8
        type: f4
      - id: value_0xec
        type: f4
      - id: change_behaviour_0xf0
        type: u2
        doc: enum; 38_30_00_00
      - id: array_count_for_0xc
        type: u2
        doc: '"ColourCubesCount"'
      - id: use__bloom_0xf4
        type: u1
      - id: use__dof_0xf5
        type: u1
      - id: use__general__fx_0xf6
        type: u1
      - id: use__vignette_0xf7
        type: u1
    instances:
      size:
        value: 252
      mu_version_hash:
        value: 0x24_b3_7b_28
  genesys__gen__dsp_plug_in_chain:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_plug_ins_0x10
        type: u4
      - id: array_count_for_0x10
        type: u1
        doc: '"PlugInsCount"'
      - id: padding
        size: 3
    instances:
      inst_plug_ins_0x10:
        pos: ptr_arr_plug_ins_0x10
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xe4_0e_7e_5d
  genesys__gen__submix_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
      - id: uint16_t_0x18
        type: u2
      - id: padding
        size: 2
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xcf_a1_b2_a2
  genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_modulating_value_0xc
        type: u4
      - id: bus_mixer_channel_property_0x10
        type: u4
        doc: enum; d5_f6_03_00
    instances:
      inst_modulating_value_0xc:
        pos: ptr_modulating_value_0xc
        type: genesys__gen__sequence_item__modulating_double_value
      size:
        value: 24
      mu_version_hash:
        value: 0xd8_23_6b_f4
  genesys__gen__bus_mixer_channel_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: ptr_arr_automated__values_0x28
        type: u4
      - id: array_count_for_0x28
        type: u2
        doc: '"Automated_ValuesCount"'
      - id: padding
        size: 2
    instances:
      inst_automated__values_0x28:
        pos: ptr_arr_automated__values_0x28
        type: genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value
        repeat: expr
        repeat-expr: array_count_for_0x28
      size:
        value: 48
      mu_version_hash:
        value: 0x47_69_2d_2c
  genesys__gen__general_trigger_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: trigger_0x28
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xbd_89_97_d6
  genesys__gen__snd_player_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x93_74_3c_35
  genesys__gen__heat_level_sound_set__nitrous:
    seq:
      - id: base_object
        type: gen_obj
      - id: compressor__override_0xc
        type: u4
      - id: cop__on_0x10
        type: u4
      - id: ptr_arr_mix__snapshot__set_0x14
        type: u4
      - id: racer__off_0x18
        type: u4
      - id: racer__on_0x1c
        type: u4
      - id: array_count_for_0x14
        type: u2
      - id: padding
        size: 2
    instances:
      inst_mix__snapshot__set_0x14:
        pos: ptr_arr_mix__snapshot__set_0x14
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 36
      mu_version_hash:
        value: 0xbd_76_cd_b7
  genesys__gen__heat_level_sound_set__sirens:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_arr_blip__waves_0xc
        type: u4
      - id: ptr_arr_extra__waves_0x10
        type: u4
      - id: ptr_arr_rumbler__waves_0x14
        type: u4
      - id: standard__wave_0x18
        type: u4
      - id: array_count_for_0xc
        type: u2
        doc: '"Blip_WavesCount"'
      - id: array_count_for_0x10
        type: u2
        doc: '"Extra_WavesCount"'
      - id: array_count_for_0x14
        type: u2
        doc: '"Rumbler_WavesCount"'
      - id: padding
        size: 2
    instances:
      inst_blip__waves_0xc:
        pos: ptr_arr_blip__waves_0xc
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0xc
      inst_extra__waves_0x10:
        pos: ptr_arr_extra__waves_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_rumbler__waves_0x14:
        pos: ptr_arr_rumbler__waves_0x14
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 36
      mu_version_hash:
        value: 0x3f_11_a9_be
  genesys__gen__distortion_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
      - id: model_0x18
        type: u4
        doc: enum; 0f_34_07_00
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xbd_a5_43_73
  genesys__gen__mixer_channel_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: mixer__channel_0x2c
        size: 8
      - id: ptr_arr_double__params_0x34
        type: u4
      - id: array_count_for_0x34
        type: u2
        doc: '"Double_ParamsCount"'
      - id: padding
        size: 2
    instances:
      inst_double__params_0x34:
        pos: ptr_arr_double__params_0x34
        type: genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value
        repeat: expr
        repeat-expr: array_count_for_0x34
      size:
        value: 60
      mu_version_hash:
        value: 0xa1_4d_af_26
  genesys__gen__uilist_items__item:
    seq:
      - id: base_object
        type: gen_obj
      - id: value_0xc
        type: string_base
      - id: display_string_0x14
        type: u4
      - id: game_changer_id_0x18
        type: u4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x06_09_2e_f5
  genesys__gen__uilist_items:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_items_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"ItemsCount"'
      - id: padding
        size: 2
    instances:
      inst_items_0x10:
        pos: ptr_arr_items_0x10
        type: genesys__gen__uilist_items__item
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x9c_8e_21_a8
  genesys__gen__damage_bar_profiles__profile__segment_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: damage_to_leave_segment_0x10
        type: f4
      - id: segment_0x14
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x20_54_d5_2b
  genesys__gen__damage_bar_profiles__profile:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: segment_recharge_time_0x10
        type: f4
      - id: segment_recharge_wait_0x14
        type: f4
      - id: ptr_arr_segment_limits_0x18
        type: u4
      - id: ptr_arr_world_segment_limits_0x1c
        type: u4
      - id: array_count_for_0x18
        type: u2
        doc: '"SegmentLimitsCount"'
      - id: array_count_for_0x1c
        type: u2
        doc: '"WorldSegmentLimitsCount"'
    instances:
      inst_segment_limits_0x18:
        pos: ptr_arr_segment_limits_0x18
        type: genesys__gen__damage_bar_profiles__profile__segment_data
        repeat: expr
        repeat-expr: array_count_for_0x18
      inst_world_segment_limits_0x1c:
        pos: ptr_arr_world_segment_limits_0x1c
        type: genesys__gen__damage_bar_profiles__profile__segment_data
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 40
      mu_version_hash:
        value: 0x7d_20_49_39
  genesys__gen__collision_effects:
    seq:
      - id: base_object
        type: gen_obj
      - id: battling__collision__effect_0xc
        type: genesys__gen__collision_effects__battling_effect
      - id: traffic__collision__effect_0xd0
        type: genesys__gen__collision_effects__traffic_effect
      - id: world__collision__effect_0x140
        type: genesys__gen__collision_effects__world_effect
      - id: game_changer_id_0x168
        type: u4
    instances:
      size:
        value: 368
      mu_version_hash:
        value: 0x69_1f_92_ad
  genesys__gen__collision_effects__battling_effect__skid_effects:
    seq:
      - id: base_object
        type: gen_obj
      - id: high_damage_skid_effect_0xc
        size: 8
      - id: low_damage_skid_effect_0x14
        size: 8
      - id: high_damage_for_skid_effect_0x1c
        type: f4
      - id: low_damage_for_skid_effect_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x03_b1_56_8c
  genesys__gen__collision_effects__battling_effect__extra_roll_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xca_6e_93_04
  genesys__gen__collision_effects__battling_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__collision_effects__battling_effect__skid_effects_0xc
        type: genesys__gen__collision_effects__battling_effect__skid_effects
      - id: looser_shrinks_0x30
        type: genesys__gen__collision_effects__battling_effect__skid_effects
      - id: genesys__gen__collision_effects__battling_effect__skid_effects_0x54
        type: genesys__gen__collision_effects__battling_effect__skid_effects
      - id: genesys__gen__collision_effects__battling_effect__extra_roll_params_0x78
        type: genesys__gen__collision_effects__battling_effect__extra_roll_params
      - id: genesys__gen__collision_effects__battling_effect__extra_roll_params_0x90
        type: genesys__gen__collision_effects__battling_effect__extra_roll_params
      - id: cam__effect__stable_0xa8
        size: 8
      - id: cam__effect__unstable_0xb0
        size: 8
      - id: cam__effect__scale_0xb8
        type: f4
      - id: stable__camera__threshold_0xbc
        type: f4
      - id: unstable__camera__threshold_0xc0
        type: f4
    instances:
      size:
        value: 200
      mu_version_hash:
        value: 0xf9_d8_34_ca
  genesys__gen__collision_effects__traffic_effect__extra_roll_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x6b_b6_93_5e
  genesys__gen__collision_effects__traffic_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__collision_effects__traffic_effect__extra_roll_params_0xc
        type: genesys__gen__collision_effects__traffic_effect__extra_roll_params
      - id: genesys__gen__collision_effects__traffic_effect__extra_roll_params_0x24
        type: genesys__gen__collision_effects__traffic_effect__extra_roll_params
      - id: genesys__gen__collision_effects__traffic_effect__extra_roll_params_0x3c
        type: genesys__gen__collision_effects__traffic_effect__extra_roll_params
      - id: cam__effect_0x54
        size: 8
      - id: cam__effect__unstable_0x5c
        size: 8
      - id: cam__effect__scale_0x64
        type: f4
      - id: stable__camera__threshold_0x68
        type: f4
      - id: unstable__camera__threshold_0x6c
        type: f4
    instances:
      size:
        value: 116
      mu_version_hash:
        value: 0x7b_2c_02_f9
  genesys__gen__collision_effects__world_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: cam__effect_0xc
        size: 8
      - id: cam__effect__unstable_0x14
        size: 8
      - id: cam__effect__scale_0x1c
        type: f4
      - id: stable__camera__threshold_0x20
        type: f4
      - id: unstable__camera__threshold_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xa8_65_71_c1
  genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal:
    seq:
      - id: base_object
        type: gen_obj
      - id: damage_to_deal_0xc
        type: f4
      - id: should_wreck_0x10
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0x58_72_c2_4c
  genesys__gen__physics__crashing_rules__impact_rules:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_arr_float32_t_0xc
        type: u4
      - id: ptr_arr_float32_t_0x10
        type: u4
      - id: ptr_arr_float32_t_0x14
        type: u4
      - id: ptr_arr_damage_override_0x18
        type: u4
      - id: array_count_for_0xc
        type: u2
      - id: array_count_for_0x10
        type: u2
      - id: array_count_for_0x18
        type: u2
      - id: array_count_for_0x14
        type: u2
    instances:
      inst_float32_t_0xc:
        pos: ptr_arr_float32_t_0xc
        type: f4
        repeat: expr
        repeat-expr: array_count_for_0xc
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
      inst_damage_override_0x18:
        pos: ptr_arr_damage_override_0x18
        type: genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 40
      mu_version_hash:
        value: 0x47_a5_6c_dc
  genesys__gen__physics__crashing_rules:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x10
        type: u4
      - id: ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x14
        type: u4
      - id: ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x18
        type: u4
      - id: ptr_arr_landing_rules_0x1c
        type: u4
      - id: ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x20
        type: u4
      - id: ptr_arr_player_rules_0x24
        type: u4
      - id: ptr_arr_props_rules_0x28
        type: u4
      - id: ptr_arr_roadblock_rules_0x2c
        type: u4
      - id: ptr_arr_traffic_rules_0x30
        type: u4
      - id: ptr_arr_world_rules_0x34
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: array_count_for_0x14
        type: u2
      - id: array_count_for_0x18
        type: u2
      - id: array_count_for_0x1c
        type: u2
      - id: array_count_for_0x20
        type: u2
      - id: array_count_for_0x24
        type: u2
      - id: array_count_for_0x28
        type: u2
      - id: array_count_for_0x2c
        type: u2
      - id: array_count_for_0x30
        type: u2
      - id: array_count_for_0x34
        type: u2
    instances:
      inst_genesys__gen__physics__crashing_rules__impact_rules_0x10:
        pos: ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x10
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_genesys__gen__physics__crashing_rules__impact_rules_0x14:
        pos: ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x14
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_genesys__gen__physics__crashing_rules__impact_rules_0x18:
        pos: ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x18
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x18
      inst_landing_rules_0x1c:
        pos: ptr_arr_landing_rules_0x1c
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x1c
      inst_genesys__gen__physics__crashing_rules__impact_rules_0x20:
        pos: ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x20
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x20
      inst_player_rules_0x24:
        pos: ptr_arr_player_rules_0x24
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x24
      inst_props_rules_0x28:
        pos: ptr_arr_props_rules_0x28
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x28
      inst_roadblock_rules_0x2c:
        pos: ptr_arr_roadblock_rules_0x2c
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x2c
      inst_traffic_rules_0x30:
        pos: ptr_arr_traffic_rules_0x30
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x30
      inst_world_rules_0x34:
        pos: ptr_arr_world_rules_0x34
        type: genesys__gen__physics__crashing_rules__impact_rules
        repeat: expr
        repeat-expr: array_count_for_0x34
      size:
        value: 80
      mu_version_hash:
        value: 0x71_fa_84_e7
  genesys__gen__collision_responses__world__traffic:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: friction_0x10
        type: f4
      - id: restitution_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x0a_68_e0_18
  genesys__gen__collision_responses__world__player__flip_state:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: flip_graph_power_0x10
        type: f4
      - id: flip_min_threshold_0x14
        type: f4
      - id: flip_scale_0x18
        type: f4
      - id: player_speed_mph_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x4c_31_8b_b0
  genesys__gen__collision_responses__world__crashed_player__constraint_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: friction_0x10
        type: f4
      - id: restitution_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x5e_f3_27_2f
  genesys__gen__collision_responses__world__crashed_player:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__collision_responses__world__crashed_player__constraint_data_0xc
        type: genesys__gen__collision_responses__world__crashed_player__constraint_data
      - id: dodge_ginger_0x24
        type: genesys__gen__collision_responses__world__crashed_player__constraint_data
      - id: game_changer_id_0x3c
        type: u4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
    instances:
      size:
        value: 76
      mu_version_hash:
        value: 0x4f_05_f9_19
  genesys__gen__race_car_handling_disruption_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: effect_duration_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: high_speed_front_lat_grip_0x18
        type: f4
      - id: high_speed_front_long_grip_0x1c
        type: f4
      - id: high_speed_rear_lat_grip_0x20
        type: f4
      - id: high_speed_rear_long_grip_0x24
        type: f4
      - id: high_speed_steer_amount_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: high_speed_threshold_0x30
        type: f4
      - id: low_speed_front_lat_grip_0x34
        type: f4
      - id: low_speed_front_long_grip_0x38
        type: f4
      - id: low_speed_rear_lat_grip_0x3c
        type: f4
      - id: low_speed_rear_long_grip_0x40
        type: f4
      - id: low_speed_steer_amount_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: low_speed_threshold_0x4c
        type: f4
      - id: affects_all_wheels_0x50
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 84
      mu_version_hash:
        value: 0x2b_35_23_d4
  genesys__gen__physics__landing_damage:
    seq:
      - id: base_object
        type: gen_obj
      - id: pitch_0xc
        type: genesys__gen__physics__landing_damage__pitch
      - id: roll_0x30
        type: genesys__gen__physics__landing_damage__roll
      - id: game_changer_id_0x50
        type: u4
      - id: float32_t_0x54
        type: f4
    instances:
      size:
        value: 92
      mu_version_hash:
        value: 0x9b_67_75_03
  genesys__gen__physics__landing_damage__pitch:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: max_damage_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x5a_6e_77_e3
  genesys__gen__physics__landing_damage__roll:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xd8_b3_b0_ad
  genesys__gen__physics__damage_bar_profile__impact_location_damage_scale:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xa7_f2_15_0b
  genesys__gen__collision_info__world_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: cam__effect_0xc
        size: 8
      - id: cam__effect__scale_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x95_1d_ad_be
  genesys__gen__collision_info_damage_profile:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: minimum__damage_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x8a_ff_20_36
  genesys__gen__collision_info__world_damage:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_aggressive_0xc
        type: u4
      - id: ptr_self__inflicted_0x10
        type: u4
    instances:
      inst_aggressive_0xc:
        pos: ptr_aggressive_0xc
        type: genesys__gen__collision_info_damage_profile
      inst_self__inflicted_0x10:
        pos: ptr_self__inflicted_0x10
        type: genesys__gen__collision_info_damage_profile
      size:
        value: 24
      mu_version_hash:
        value: 0x2d_10_2a_d7
  genesys__gen__collision_info__battling_damage:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xd5_dc_12_ea
  genesys__gen__collision_info__payload_damage:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_genesys__gen__collision_info_damage_profile_0xc
        type: u4
      - id: ptr_self_inflicted_0x10
        type: u4
    instances:
      inst_genesys__gen__collision_info_damage_profile_0xc:
        pos: ptr_genesys__gen__collision_info_damage_profile_0xc
        type: genesys__gen__collision_info_damage_profile
      inst_self_inflicted_0x10:
        pos: ptr_self_inflicted_0x10
        type: genesys__gen__collision_info_damage_profile
      size:
        value: 24
      mu_version_hash:
        value: 0x1b_31_97_bc
  genesys__gen__collision_responses__global:
    seq:
      - id: base_object
        type: gen_obj
      - id: race__car__vs__race__car_0xc
        type: genesys__gen__collision_responses__global__race_car_vs_race_car
      - id: crashing__race__car__vs__traffic_0x74
        type: genesys__gen__collision_responses__global__crashing_race_car_vs_traffic
      - id: traffic__vs__dynamic_0x9c
        type: genesys__gen__collision_responses__global__traffic_vs_dynamic
      - id: crashing__race__car__vs__crashing__race__car_0xc0
        type: genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car
      - id: traffic__vs__traffic_0xe0
        type: genesys__gen__collision_responses__global__traffic_vs_traffic
      - id: dynamic__vs__dynamic_0x100
        type: genesys__gen__collision_responses__global__dynamic_vs_dynamic
      - id: game_changer_id_0x11c
        type: u4
    instances:
      size:
        value: 292
      mu_version_hash:
        value: 0x48_96_f9_8c
  genesys__gen__collision_responses__global__race_car_vs_race_car:
    seq:
      - id: base_object
        type: gen_obj
      - id: stable_0xc
        type: genesys__gen__collision_responses__global__race_car_vs_race_car__params
      - id: unstable_0x28
        type: genesys__gen__collision_responses__global__race_car_vs_race_car__params
      - id: crashed_0x44
        type: genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params
      - id: game_changer_id_0x5c
        type: u4
      - id: friction_0x60
        type: f4
      - id: restitution_0x64
        type: f4
    instances:
      size:
        value: 108
      mu_version_hash:
        value: 0xc8_38_aa_88
  genesys__gen__collision_responses__global__race_car_vs_race_car__params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: damage_0x14
        type: f4
      - id: linear__solve_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x2a_b6_e9_bc
  genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: linear__solve_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x49_67_5a_53
  genesys__gen__collision_responses__global__crashing_race_car_vs_traffic:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: crashing__race__car__angular__solve_0x10
        type: f4
      - id: crashing__race__car__linear__solve_0x14
        type: f4
      - id: friction_0x18
        type: f4
      - id: restitution_0x1c
        type: f4
      - id: traffic__angular__solve_0x20
        type: f4
      - id: traffic__linear__solve_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x9c_87_62_e4
  genesys__gen__collision_responses__global__traffic_vs_dynamic:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: dynamic__angular__solve_0x10
        type: f4
      - id: dynamic__linear__solve_0x14
        type: f4
      - id: restitution_0x18
        type: f4
      - id: traffic__angular__solve_0x1c
        type: f4
      - id: traffic__linear__solve_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xb7_9f_5b_47
  genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: friction_0x14
        type: f4
      - id: linear__solve_0x18
        type: f4
      - id: restitution_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x46_b5_cc_d9
  genesys__gen__collision_responses__global__traffic_vs_traffic:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: friction_0x14
        type: f4
      - id: linear__solve_0x18
        type: f4
      - id: restitution_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x39_72_6c_a5
  genesys__gen__collision_responses__global__dynamic_vs_dynamic:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: linear__solve_0x14
        type: f4
      - id: restitution_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xe8_ed_b4_b8
  genesys__gen__collision_responses__race_car:
    seq:
      - id: base_object
        type: gen_obj
      - id: player__vs__traffic_0xc
        type: genesys__gen__collision_responses__race_car__player_vs_traffic
      - id: player__vs__ai_0x100
        type: genesys__gen__collision_responses__race_car__player_vs_ai
      - id: ai__vs__traffic_0x1e8
        type: genesys__gen__collision_responses__race_car__aivs_traffic
      - id: player__vs__crashing__race__car_0x2c0
        type: genesys__gen__collision_responses__race_car__player_vs_crashing_race_car
      - id: ai__vs__crashing__race__car_0x368
        type: genesys__gen__collision_responses__race_car__aivs_crashing_race_car
      - id: ai__car__vs__dynamic_0x3d0
        type: genesys__gen__collision_responses__race_car__race_car_vs_dynamic
      - id: player_or__network_car__vs__dynamic_0x40c
        type: genesys__gen__collision_responses__race_car__race_car_vs_dynamic
      - id: game_changer_id_0x448
        type: u4
    instances:
      size:
        value: 1104
      mu_version_hash:
        value: 0x1f_47_19_c7
  genesys__gen__collision_responses__race_car__player_vs_traffic:
    seq:
      - id: base_object
        type: gen_obj
      - id: player__stable_0xc
        type: genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params
      - id: player__unstable_0x28
        type: genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params
      - id: traffic__stable_0x44
        type: genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params
      - id: traffic__unstable_0x60
        type: genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params
      - id: player__crashed_0x7c
        type: genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params
      - id: player__invulnerable_0x94
        type: genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params
      - id: player__low__speed_0xac
        type: genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params
      - id: traffic__low__speed_0xc4
        type: genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params
      - id: game_changer_id_0xdc
        type: u4
      - id: float32_t_0xe0
        type: f4
      - id: friction_0xe4
        type: f4
      - id: full__high__speed__mph_0xe8
        type: f4
      - id: full__low__speed__mph_0xec
        type: f4
      - id: restitution_0xf0
        type: f4
    instances:
      size:
        value: 248
      mu_version_hash:
        value: 0x64_29_af_ec
  genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: damage_0x14
        type: f4
      - id: linear__solve_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x81_4a_38_40
  genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: linear__solve_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x7f_d3_92_c3
  genesys__gen__collision_responses__race_car__player_vs_ai:
    seq:
      - id: base_object
        type: gen_obj
      - id: ai__stable_0xc
        type: genesys__gen__collision_responses__race_car__player_vs_ai__damage_params
      - id: ai__unstable_0x28
        type: genesys__gen__collision_responses__race_car__player_vs_ai__damage_params
      - id: player__stable_0x44
        type: genesys__gen__collision_responses__race_car__player_vs_ai__damage_params
      - id: player__unstable_0x60
        type: genesys__gen__collision_responses__race_car__player_vs_ai__damage_params
      - id: ai__crashed_0x7c
        type: genesys__gen__collision_responses__race_car__player_vs_ai__basic_params
      - id: player__crashed_0x94
        type: genesys__gen__collision_responses__race_car__player_vs_ai__basic_params
      - id: player__invulnerable_0xac
        type: genesys__gen__collision_responses__race_car__player_vs_ai__basic_params
      - id: player__when__ai__crashed_0xc4
        type: genesys__gen__collision_responses__race_car__player_vs_ai__basic_params
      - id: game_changer_id_0xdc
        type: u4
      - id: friction_0xe0
        type: f4
      - id: restitution_0xe4
        type: f4
    instances:
      size:
        value: 236
      mu_version_hash:
        value: 0x8e_8a_90_a4
  genesys__gen__collision_responses__race_car__player_vs_ai__damage_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: damage_0x14
        type: f4
      - id: linear__solve_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xb0_39_af_62
  genesys__gen__collision_responses__race_car__player_vs_ai__basic_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: linear__solve_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x1c_ad_98_de
  genesys__gen__collision_responses__race_car__aivs_traffic:
    seq:
      - id: base_object
        type: gen_obj
      - id: ai__stable_0xc
        type: genesys__gen__collision_responses__race_car__aivs_traffic__damage_params
      - id: ai__unstable_0x28
        type: genesys__gen__collision_responses__race_car__aivs_traffic__damage_params
      - id: traffic__stable_0x44
        type: genesys__gen__collision_responses__race_car__aivs_traffic__damage_params
      - id: traffic__unstable_0x60
        type: genesys__gen__collision_responses__race_car__aivs_traffic__damage_params
      - id: ai__crashed_0x7c
        type: genesys__gen__collision_responses__race_car__aivs_traffic__basic_params
      - id: ai__low__speed_0x94
        type: genesys__gen__collision_responses__race_car__aivs_traffic__basic_params
      - id: traffic__low__speed_0xac
        type: genesys__gen__collision_responses__race_car__aivs_traffic__basic_params
      - id: game_changer_id_0xc4
        type: u4
      - id: friction_0xc8
        type: f4
      - id: full__high__speed__mph_0xcc
        type: f4
      - id: full__low__speed__mph_0xd0
        type: f4
      - id: restitution_0xd4
        type: f4
    instances:
      size:
        value: 220
      mu_version_hash:
        value: 0xe2_81_00_5d
  genesys__gen__collision_responses__race_car__aivs_traffic__damage_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: damage_0x14
        type: f4
      - id: linear__solve_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xba_d9_5a_cc
  genesys__gen__collision_responses__race_car__aivs_traffic__basic_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: linear__solve_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x74_54_51_c9
  genesys__gen__collision_responses__race_car__player_vs_crashing_race_car:
    seq:
      - id: base_object
        type: gen_obj
      - id: first__frame_0xc
        type: genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile
      - id: low__speed_0x34
        type: genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile
      - id: subsequent__frames_0x5c
        type: genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile
      - id: player__invulnerable_0x84
        type: genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params
      - id: game_changer_id_0x9c
        type: u4
      - id: full__high__speed__mph_0xa0
        type: f4
      - id: full__low__speed__mph_0xa4
        type: f4
    instances:
      size:
        value: 172
      mu_version_hash:
        value: 0xc2_12_dd_ec
  genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: crashing__race__car__angular__solve_0x10
        type: f4
      - id: crashing__race__car__linear__solve_0x14
        type: f4
      - id: friction_0x18
        type: f4
      - id: player__angular__solve_0x1c
        type: f4
      - id: player__linear__solve_0x20
        type: f4
      - id: restitution_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xf0_8c_ae_fc
  genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: linear__solve_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xb9_2f_86_f9
  genesys__gen__collision_responses__race_car__aivs_crashing_race_car:
    seq:
      - id: base_object
        type: gen_obj
      - id: high__speed_0xc
        type: genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params
      - id: low__speed_0x34
        type: genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params
      - id: game_changer_id_0x5c
        type: u4
      - id: full__high__speed__mph_0x60
        type: f4
      - id: full__low__speed__mph_0x64
        type: f4
    instances:
      size:
        value: 108
      mu_version_hash:
        value: 0x2b_14_62_e5
  genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ai__angular__solve_0x10
        type: f4
      - id: ai__linear__solve_0x14
        type: f4
      - id: crashing__race__car__angular__solve_0x18
        type: f4
      - id: crashing__race__car__linear__solve_0x1c
        type: f4
      - id: friction_0x20
        type: f4
      - id: restitution_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xb0_4e_5d_28
  genesys__gen__collision_responses__race_car__race_car_vs_dynamic:
    seq:
      - id: base_object
        type: gen_obj
      - id: race__car__invulnerable_0xc
        type: genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params
      - id: game_changer_id_0x24
        type: u4
      - id: dynamic__angular__solve_0x28
        type: f4
      - id: dynamic__linear__solve_0x2c
        type: f4
      - id: race__car__angular__solve_0x30
        type: f4
      - id: race__car__linear__solve_0x34
        type: f4
      - id: restitution_0x38
        type: f4
    instances:
      size:
        value: 64
      mu_version_hash:
        value: 0xaf_f7_71_da
  genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angular__solve_0x10
        type: f4
      - id: linear__solve_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xe7_62_87_7e
  genesys__gen__collision_responses__world__in_air_player:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: dynamic_friction_0x10
        type: f4
      - id: restitution_0x14
        type: f4
      - id: solve_position_angular_scale_0x18
        type: f4
      - id: solve_velocity_angular_scale_0x1c
        type: f4
      - id: static_friction_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x8a_ce_69_15
  genesys__gen__physics__damage_bar_profile__segment:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: lamps_corked_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: recharge_time_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: size_0x24
        type: f4
      - id: bool8_t_0x28
        type: u1
      - id: recharges_0x29
        type: u1
      - id: adapter_wales_0x2a
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x34_7d_09_0a
  genesys__gen__physics__damage_bar_profile:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__physics__damage_bar_profile__impact_location_damage_scale_0xc
        type: genesys__gen__physics__damage_bar_profile__impact_location_damage_scale
      - id: crashing_rules_0x34
        size: 8
      - id: game_changer_id_0x3c
        type: u4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: ejected_rubbish_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: float32_t_0x58
        type: f4
      - id: float32_t_0x5c
        type: f4
      - id: float32_t_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: float32_t_0x68
        type: f4
      - id: float32_t_0x6c
        type: f4
      - id: ptr_arr_segments_0x70
        type: u4
      - id: array_count_for_0x70
        type: u2
        doc: '"SegmentsCount"'
      - id: padding
        size: 2
    instances:
      inst_segments_0x70:
        pos: ptr_arr_segments_0x70
        type: genesys__gen__physics__damage_bar_profile__segment
        repeat: expr
        repeat-expr: array_count_for_0x70
      size:
        value: 120
      mu_version_hash:
        value: 0xd9_8e_ba_cd
  genesys__gen__collision_info:
    seq:
      - id: base_object
        type: gen_obj
      - id: collision__effects_0xc
        size: 8
      - id: damage__bars_0x14
        size: 8
      - id: damage__graphs_0x1c
        size: 8
      - id: global__collision__responses_0x24
        size: 8
      - id: race__car__collision__responses_0x2c
        size: 8
      - id: world__collision__responses_0x34
        size: 8
      - id: game_changer_id_0x3c
        type: u4
      - id: average__world__strength_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: bloodstained_ends_0x54
        type: f4
      - id: ptr_landing__damage_0x58
        type: u4
    instances:
      inst_landing__damage_0x58:
        pos: ptr_landing__damage_0x58
        type: genesys__gen__physics__landing_damage
      size:
        value: 96
      mu_version_hash:
        value: 0x57_c7_4f_cf
  genesys__gen__collision_info__battling_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: ai__extra__roll_0xc
        type: genesys__gen__collision_info__battling_effect__extra_roll_params
      - id: player__extra__roll_0x24
        type: genesys__gen__collision_info__battling_effect__extra_roll_params
      - id: cam__effect_0x3c
        size: 8
      - id: cam__effect__scale_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
    instances:
      size:
        value: 80
      mu_version_hash:
        value: 0x70_6d_b6_32
  genesys__gen__collision_info__battling_effect__extra_roll_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: damage__for__full__extra__roll_0xc
        type: f4
      - id: damage__for__no__extra__roll_0x10
        type: f4
      - id: extra__limit__duration_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xdc_0a_f1_b1
  genesys__gen__collision_info__traffic_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: cam__effect_0xc
        size: 8
      - id: cam__effect__scale_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x87_af_e3_6c
  genesys__gen__camera_gameplay_shake_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: translation_0xc
        type: genesys__gen__camera_gameplay_shake_effect__translation
      - id: rotation_0xa4
        type: genesys__gen__camera_gameplay_shake_effect__rotation
      - id: game_changer_id_0x130
        type: u4
    instances:
      size:
        value: 312
      mu_version_hash:
        value: 0xd5_69_9b_70
  genesys__gen__camera_gameplay_shake_effect__translation:
    seq:
      - id: base_object
        type: gen_obj
      - id: x_0xc
        type: genesys__gen__camera_gameplay_shake_effect__translation__axis_params
      - id: y_0x38
        type: genesys__gen__camera_gameplay_shake_effect__translation__axis_params
      - id: z_0x64
        type: genesys__gen__camera_gameplay_shake_effect__translation__axis_params
      - id: game_changer_id_0x90
        type: u4
      - id: amplitude_0x94
        type: f4
    instances:
      size:
        value: 156
      mu_version_hash:
        value: 0x33_a1_3e_49
  genesys__gen__camera_gameplay_shake_effect__translation__axis_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: amplitude_0x10
        type: f4
      - id: inwards__damping_0x14
        type: f4
      - id: lower__translation__limit_0x18
        type: f4
      - id: outwards__damping_0x1c
        type: f4
      - id: spring__coefficient_0x20
        type: f4
      - id: upper__translation__limit_0x24
        type: f4
      - id: invert__force__direction_0x28
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xd2_62_d8_63
  genesys__gen__camera_gameplay_shake_effect__rotation:
    seq:
      - id: base_object
        type: gen_obj
      - id: pitch_0xc
        type: genesys__gen__camera_gameplay_shake_effect__rotation__axis_params
      - id: roll_0x34
        type: genesys__gen__camera_gameplay_shake_effect__rotation__axis_params
      - id: yaw_0x5c
        type: genesys__gen__camera_gameplay_shake_effect__rotation__axis_params
      - id: game_changer_id_0x84
        type: u4
      - id: amplitude_0x88
        type: f4
    instances:
      size:
        value: 144
      mu_version_hash:
        value: 0x48_b8_4c_b2
  genesys__gen__camera_gameplay_shake_effect__rotation__axis_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: amplitude_0x10
        type: f4
      - id: damping_0x14
        type: f4
      - id: maximum__angle_0x18
        type: f4
      - id: minimum__angle_0x1c
        type: f4
      - id: spring__coefficient_0x20
        type: f4
      - id: invert__force__direction_0x24
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xd9_b1_e6_09
  genesys__gen__impact_damage_graphs:
    seq:
      - id: base_object
        type: gen_obj
      - id: general_damage_graph_0xc
        type: genesys__gen__impact_damage_graphs__graph
      - id: race_car_vs_race_car_damage_graph_0x30
        type: genesys__gen__impact_damage_graphs__graph
      - id: game_changer_id_0x54
        type: u4
      - id: velocity_for_full_damage_mph_0x58
        type: f4
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0x0b_b1_a0_97
  genesys__gen__impact_damage_graphs__graph:
    seq:
      - id: base_object
        type: gen_obj
      - id: maximum_closing_velocity_mph_0xc
        type: f4
      - id: maximum_velocity_damage_0x10
        type: f4
      - id: medium_closing_velocity_mph_0x14
        type: f4
      - id: medium_velocity_damage_0x18
        type: f4
      - id: minimum_closing_velocity_mph_0x1c
        type: f4
      - id: minimum_velocity_damage_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x65_8d_7d_4d
  genesys__gen__collision_responses__world:
    seq:
      - id: base_object
        type: gen_obj
      - id: player_0xc
        type: genesys__gen__collision_responses__world__player
      - id: crashed_player_0x70
        type: genesys__gen__collision_responses__world__crashed_player
      - id: in_air_player_0xb8
        type: genesys__gen__collision_responses__world__in_air_player
      - id: crashed_traffic_0xdc
        type: genesys__gen__collision_responses__world__traffic
      - id: traffic_0xf4
        type: genesys__gen__collision_responses__world__traffic
      - id: game_changer_id_0x10c
        type: u4
    instances:
      size:
        value: 276
      mu_version_hash:
        value: 0x40_62_ed_a3
  genesys__gen__collision_responses__world__player:
    seq:
      - id: base_object
        type: gen_obj
      - id: high_speed_flip_state_0xc
        type: genesys__gen__collision_responses__world__player__flip_state
      - id: low_speed_flip_state_0x2c
        type: genesys__gen__collision_responses__world__player__flip_state
      - id: game_changer_id_0x4c
        type: u4
      - id: dynamic_friction_0x50
        type: f4
      - id: restitution_0x54
        type: f4
      - id: solve_position_angular_scale_0x58
        type: f4
      - id: solve_velocity_angular_scale_0x5c
        type: f4
      - id: static_friction_0x60
        type: f4
    instances:
      size:
        value: 104
      mu_version_hash:
        value: 0xfd_ed_9d_18
  genesys__gen__damage_bar_profiles:
    seq:
      - id: base_object
        type: gen_obj
      - id: ai_0xc
        size: 8
      - id: impactor_sustaining_0x14
        size: 8
      - id: player_online_0x1c
        size: 8
      - id: traffic_0x24
        size: 8
      - id: game_changer_id_0x2c
        type: u4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0xe2_46_a1_af
  genesys__gen__traffic_flow_type__traffic_flow_type:
    seq:
      - id: base_object
        type: gen_obj
      - id: traffic_vehicle_type_0xc
        size: 8
      - id: colour_0x14
        type: u4
      - id: game_changer_id_0x18
        type: u4
      - id: proportion_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x8c_43_2d_e1
  genesys__gen__traffic_flow:
    seq:
      - id: base_object
        type: gen_obj
      - id: flow_type_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: density_0x20
        type: f4
      - id: speed_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0xaf_cd_40_4e
  genesys__gen__traffic_flow_type:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_flow_type_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"FlowTypeCount"'
      - id: padding
        size: 2
    instances:
      inst_flow_type_0x10:
        pos: ptr_arr_flow_type_0x10
        type: genesys__gen__traffic_flow_type__traffic_flow_type
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x1b_e2_b3_77
  genesys__gen__traffic_vehicle:
    seq:
      - id: base_object
        type: gen_obj
      - id: positive_pitch__negative_pitch__yaw__roll_0x10
        type: rw_math_vpu__vector4
      - id: trailer_0x20
        size: 8
      - id: traits_0x28
        size: 8
      - id: game_changer_id_0x30
        type: u4
      - id: vehicle_component_0x34
        type: u4
      - id: score_0x38
        type: u4
      - id: bool8_t_0x3c
        type: u1
      - id: use_thick_wheel_smoke_0x3d
        type: u1
      - id: padding
        size: 2
    instances:
      size:
        value: 64
      mu_version_hash:
        value: 0xca_5d_4e_b1
  genesys__gen__traffic_vehicle_traits:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: acceleration_0x10
        type: f4
      - id: scale_0x14
        type: u4
        doc: enum; de_30_00_00
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x9a_9b_0b_91
  genesys__gen__dynamic_additional_info:
    seq:
      - id: base_object
        type: gen_obj
      - id: sequence_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: strength_0x20
        type: f4
      - id: score_0x24
        type: u2
      - id: bool8_t_0x26
        type: u1
      - id: bool8_t_0x27
        type: u1
      - id: bool8_t_0x28
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xaf_e3_6e_f3
  genesys__gen__compound_additional_info:
    seq:
      - id: base_object
        type: genesys__gen__dynamic_additional_info
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
    instances:
      size:
        value: 60
      mu_version_hash:
        value: 0xec_02_6f_0f
  genesys__gen__light__base__flash_pattern:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: duration_0x10
        type: f4
      - id: frequency_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: offset_0x1c
        type: f4
      - id: type_0x20
        type: u4
        doc: enum; f0_2f_00_00
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x12_48_17_f4
  genesys__gen__light__base:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: genesys__gen__light__base__flash_pattern_0x20
        type: genesys__gen__light__base__flash_pattern
      - id: game_changer_id_0x44
        type: u4
      - id: float32_t_0x48
        type: f4
      - id: intensity_0x4c
        type: f4
      - id: bool8_t_0x50
        type: u1
      - id: bool8_t_0x51
        type: u1
      - id: bool8_t_0x52
        type: u1
      - id: bool8_t_0x53
        type: u1
      - id: bool8_t_0x54
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 88
      mu_version_hash:
        value: 0xf1_2b_e6_48
  genesys__gen__light__cone:
    seq:
      - id: base_object
        type: genesys__gen__light__base
      - id: float32_t_0x60
        type: f4
    instances:
      size:
        value: 104
      mu_version_hash:
        value: 0xed_c9_d7_11
  genesys__gen__light__point:
    seq:
      - id: base_object
        type: genesys__gen__light__base
    instances:
      size:
        value: 92
      mu_version_hash:
        value: 0xec_fa_af_14
  genesys__gen__smash_proxy_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xb7_e8_37_c2
  genesys__gen__light__spot:
    seq:
      - id: base_object
        type: genesys__gen__light__cone
      - id: float32_t_0x70
        type: f4
    instances:
      size:
        value: 120
      mu_version_hash:
        value: 0x82_86_ce_b2
  genesys__gen__enable_compound_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: padding
        size: 2
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xd6_15_d6_f9
  genesys__gen__easy_guide__page:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x14
        type: u4
      - id: sequence_0x18
        type: u4
      - id: ptr_arr_text_0x1c
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x20
        type: u4
      - id: unk_enum_0x24
        type: u2
        doc: enum; 00_0f_16_00
      - id: array_count_for_0x1c
        type: u2
      - id: array_count_for_0x20
        type: u1
      - id: array_count_for_0x14
        type: u1
      - id: padding
        size: 2
    instances:
      inst_cgs_core__unique_id_0x14:
        pos: ptr_arr_cgs_core__unique_id_0x14
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_text_0x1c:
        pos: ptr_arr_text_0x1c
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x1c
      inst_cgs_resource__handle_0x20:
        pos: ptr_arr_cgs_resource__handle_0x20
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x20
      size:
        value: 44
      mu_version_hash:
        value: 0x51_5d_57_d0
  genesys__gen__nitrous_parameters__traffic_near_miss:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: minimum_speed_0x14
        type: f4
      - id: nitrous_reward_0x18
        type: f4
      - id: is_enabled_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xfd_b5_bb_33
  genesys__gen__nitrous_strength__jump:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xdf_4b_ff_06
  genesys__gen__nitrous_parameters__traffic_oncoming:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: minimum_speed_0x14
        type: f4
      - id: minimum_time_0x18
        type: f4
      - id: nitrous_reward_0x1c
        type: f4
      - id: oncoming_timeout_0x20
        type: f4
      - id: is_enabled_0x24
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x9a_fc_ff_c1
  genesys__gen__nitrous_parameters__nitrous_power:
    seq:
      - id: base_object
        type: gen_obj
      - id: time_to_full_nitrous_0xc
        type: f4
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0x94_06_6a_3d
  genesys__gen__nitrous_parameters__hitting_another_competitor:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: minimum_speed_0x14
        type: f4
      - id: minimum_time_0x18
        type: f4
      - id: nitrous_reward_0x1c
        type: f4
      - id: is_enabled_0x20
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x9e_5a_13_c6
  genesys__gen__nitrous_parameters__high_speed:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: nitrous_reward_0x14
        type: f4
      - id: speed_percentage_0x18
        type: f4
      - id: is_enabled_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x9a_fd_9b_d9
  genesys__gen__nitrous_parameters__catching_air:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: nitrous_reward_0x14
        type: f4
      - id: time_in_air_0x18
        type: f4
      - id: is_enabled_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x7b_b2_02_23
  genesys__gen__nitrous_parameters__balancing:
    seq:
      - id: base_object
        type: gen_obj
      - id: close_burn_rate_0xc
        type: f4
      - id: close_multiplier_0x10
        type: f4
      - id: far_burn_rate_0x14
        type: f4
      - id: far_multiplier_0x18
        type: f4
      - id: max_distance_0x1c
        type: f4
      - id: slipstream_distance_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xf3_3f_75_b9
  genesys__gen__nitrous_parameters__slipstreaming:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: minimum_speed_0x14
        type: f4
      - id: min_slip_streaming_0x18
        type: f4
      - id: nitrous_reward_0x1c
        type: f4
      - id: is_enabled_0x20
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x40_73_c3_54
  genesys__gen__nitrous_parameters__fatal_hit:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: nitrous_reward_0x14
        type: f4
      - id: is_enabled_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xe1_a3_2e_6f
  genesys__gen__aerodynamic_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: float32_t_0x58
        type: f4
      - id: float32_t_0x5c
        type: f4
      - id: float32_t_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: bool8_t_0x68
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 108
      mu_version_hash:
        value: 0xb5_0e_b2_7a
  genesys__gen__ginsu_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: fade__out_0x38
        type: genesys__gen__ginsu_sequence_item__fade
      - id: cgs_resource__handle_0x4c
        size: 8
      - id: mixer__channel_0x54
        size: 8
    instances:
      size:
        value: 92
      mu_version_hash:
        value: 0x2e_17_bf_4f
  genesys__gen__ginsu_sequence_item__fade:
    seq:
      - id: base_object
        type: gen_obj
      - id: curve_0xc
        type: f4
      - id: time_0x10
        type: f4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xc0_fd_f0_90
  genesys__gen__gearbox__gear:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xd7_10_9a_3b
  genesys__gen__gearbox:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__gearbox__gear_0xc
        type: genesys__gen__gearbox__gear
      - id: game_changer_id_0x28
        type: u4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: ptr_arr_genesys__gen__gearbox__gear_0x4c
        type: u4
      - id: array_count_for_0x4c
        type: u2
      - id: bool8_t_0x52
        type: u1
      - id: bool8_t_0x53
        type: u1
      - id: bool8_t_0x54
        type: u1
      - id: padding
        size: 3
    instances:
      inst_genesys__gen__gearbox__gear_0x4c:
        pos: ptr_arr_genesys__gen__gearbox__gear_0x4c
        type: genesys__gen__gearbox__gear
        repeat: expr
        repeat-expr: array_count_for_0x4c
      size:
        value: 88
      mu_version_hash:
        value: 0xde_7a_ff_f6
  genesys__gen__colour_group:
    seq:
      - id: base_object
        type: gen_obj
      - id: primary_colour_0xc
        size: 8
      - id: cgs_resource__handle_0x14
        size: 8
      - id: cgs_resource__handle_0x1c
        size: 8
      - id: game_changer_id_0x24
        type: u4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x4b_17_85_2d
  genesys__gen__performance_modification_item:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: value_0x10
        type: f4
      - id: unk_enum_0x14
        type: u2
        doc: enum; 02_5e_0f_00
      - id: modification_type_0x16
        type: u2
        doc: enum; 09_5e_0f_00
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x5c_b8_53_e2
  genesys__gen__performance_modifier:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_ptr_modifications_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"ModificationsCount"'
      - id: padding
        size: 2
    instances:
      inst_modifications_0x10:
        pos: ptr_arr_ptr_modifications_0x10
        type: ptr('genesys__gen__performance_modification_item')
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xb2_dc_d5_bf
  genesys__gen__handbrake_ability:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
    instances:
      size:
        value: 48
      mu_version_hash:
        value: 0xee_89_cc_78
  genesys__gen__nitrous_parameters__donutting:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: max_speed_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: nitrous_reward_0x1c
        type: f4
      - id: is_enabled_0x20
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xea_26_7c_d5
  genesys__gen__vehicle__gameplay__mod_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: value_0xc
        type: f4
      - id: stat_0x10
        type: u4
        doc: enum; 2b_55_19_00
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xcc_ae_ef_0e
  genesys__gen__aligning_torque:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xcb_0b_5c_17
  genesys__gen__body_movement_behaviour__take_off_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
    instances:
      size:
        value: 72
      mu_version_hash:
        value: 0x43_4f_43_96
  genesys__gen__body_movement_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__body_movement_behaviour__take_off_behaviour_0xc
        type: genesys__gen__body_movement_behaviour__take_off_behaviour
      - id: game_changer_id_0x50
        type: u4
      - id: float32_t_0x54
        type: f4
      - id: float32_t_0x58
        type: f4
      - id: float32_t_0x5c
        type: f4
      - id: float32_t_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: float32_t_0x68
        type: f4
      - id: float32_t_0x6c
        type: f4
      - id: float32_t_0x70
        type: f4
      - id: float32_t_0x74
        type: f4
      - id: float32_t_0x78
        type: f4
      - id: float32_t_0x7c
        type: f4
      - id: float32_t_0x80
        type: f4
      - id: float32_t_0x84
        type: f4
      - id: float32_t_0x88
        type: f4
      - id: float32_t_0x8c
        type: f4
      - id: float32_t_0x90
        type: f4
    instances:
      size:
        value: 152
      mu_version_hash:
        value: 0x06_56_e7_e5
  genesys__gen__brake_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x86_49_78_e9
  genesys__gen__donut_ability__donut_grip_values:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0xf8_3a_19_d6
  genesys__gen__donut_ability__donut_scale:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x3c_7f_c8_b0
  genesys__gen__donut_ability:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__donut_ability__donut_grip_values_0xc
        type: genesys__gen__donut_ability__donut_grip_values
      - id: genesys__gen__donut_ability__donut_scale_0x3c
        type: genesys__gen__donut_ability__donut_scale
      - id: game_changer_id_0x5c
        type: u4
    instances:
      size:
        value: 100
      mu_version_hash:
        value: 0x53_21_53_f7
  genesys__gen__drift_behaviour__other:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
    instances:
      size:
        value: 76
      mu_version_hash:
        value: 0xfd_98_90_57
  genesys__gen__drift_behaviour__yaw_torque:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
    instances:
      size:
        value: 68
      mu_version_hash:
        value: 0xd3_77_a1_da
  genesys__gen__drift_behaviour__side_force:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
    instances:
      size:
        value: 60
      mu_version_hash:
        value: 0x81_49_c3_b1
  genesys__gen__drift_behaviour__drift_scale:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
    instances:
      size:
        value: 56
      mu_version_hash:
        value: 0x9e_41_c9_f7
  genesys__gen__drift_behaviour__drift_exit:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xf0_be_de_aa
  genesys__gen__drift_behaviour__drift_trigger:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x5e_ba_96_68
  genesys__gen__drift_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__drift_behaviour__other_0xc
        type: genesys__gen__drift_behaviour__other
      - id: genesys__gen__drift_behaviour__yaw_torque_0x54
        type: genesys__gen__drift_behaviour__yaw_torque
      - id: genesys__gen__drift_behaviour__side_force_0x94
        type: genesys__gen__drift_behaviour__side_force
      - id: genesys__gen__drift_behaviour__drift_scale_0xcc
        type: genesys__gen__drift_behaviour__drift_scale
      - id: genesys__gen__drift_behaviour__drift_exit_0x100
        type: genesys__gen__drift_behaviour__drift_exit
      - id: genesys__gen__drift_behaviour__drift_trigger_0x128
        type: genesys__gen__drift_behaviour__drift_trigger
      - id: game_changer_id_0x14c
        type: u4
    instances:
      size:
        value: 340
      mu_version_hash:
        value: 0xfe_ca_6d_4d
  genesys__gen__point2d:
    seq:
      - id: base_object
        type: gen_obj
      - id: inline_arr_float32_t_0xc
        type: f4
        repeat: expr
        repeat-expr: 2
      - id: array_count_for_0xc
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xcc_71_ba_d5
  genesys__gen__point2dwith_tangents:
    seq:
      - id: base_object
        type: genesys__gen__point2d
      - id: genesys__gen__point2d_0x18
        type: genesys__gen__point2d
      - id: genesys__gen__point2d_0x30
        type: genesys__gen__point2d
    instances:
      size:
        value: 56
      mu_version_hash:
        value: 0x64_de_27_ed
  genesys__gen__engine__power_curve:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: ptr_arr_ptr_genesys__gen__point2dwith_tangents_0x4c
        type: u4
      - id: array_count_for_0x4c
        type: u1
      - id: padding
        size: 3
    instances:
      inst_genesys__gen__point2dwith_tangents_0x4c:
        pos: ptr_arr_ptr_genesys__gen__point2dwith_tangents_0x4c
        type: ptr('genesys__gen__point2dwith_tangents')
        repeat: expr
        repeat-expr: array_count_for_0x4c
      size:
        value: 84
      mu_version_hash:
        value: 0xbe_73_7b_b9
  genesys__gen__engine__sound:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: idle_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
    instances:
      size:
        value: 64
      mu_version_hash:
        value: 0xd9_0a_66_25
  genesys__gen__engine__differentials:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x2a_44_41_c3
  genesys__gen__engine__normal_quality_engine:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xa9_bc_ff_78
  genesys__gen__engine__transmission:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0xe4_41_04_8a
  genesys__gen__nitrous_strength:
    seq:
      - id: base_object
        type: gen_obj
      - id: jump_0xc
        type: genesys__gen__nitrous_strength__jump
      - id: punch_0x24
        type: genesys__gen__nitrous_strength__punch
      - id: game_changer_id_0x38
        type: u4
      - id: float32_t_0x3c
        type: f4
    instances:
      size:
        value: 68
      mu_version_hash:
        value: 0x47_a2_87_66
  genesys__gen__engine:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__engine__power_curve_0xc
        type: genesys__gen__engine__power_curve
      - id: genesys__gen__engine__sound_0x60
        type: genesys__gen__engine__sound
      - id: genesys__gen__engine__differentials_0x9c
        type: genesys__gen__engine__differentials
      - id: genesys__gen__engine__normal_quality_engine_0xb8
        type: genesys__gen__engine__normal_quality_engine
      - id: genesys__gen__engine__transmission_0xcc
        type: genesys__gen__engine__transmission
      - id: cgs_resource__handle_0xdc
        size: 8
      - id: cgs_resource__handle_0xe4
        size: 8
      - id: game_changer_id_0xec
        type: u4
      - id: float32_t_0xf0
        type: f4
      - id: float32_t_0xf4
        type: f4
      - id: float32_t_0xf8
        type: f4
      - id: float32_t_0xfc
        type: f4
      - id: float32_t_0x100
        type: f4
      - id: float32_t_0x104
        type: f4
      - id: float32_t_0x108
        type: f4
      - id: float32_t_0x10c
        type: f4
      - id: ptr_genesys__gen__gearbox_0x110
        type: u4
      - id: ptr_genesys__gen__gearbox_0x114
        type: u4
      - id: ptr_genesys__gen__nitrous_strength_0x118
        type: u4
    instances:
      inst_genesys__gen__gearbox_0x110:
        pos: ptr_genesys__gen__gearbox_0x110
        type: genesys__gen__gearbox
      inst_genesys__gen__gearbox_0x114:
        pos: ptr_genesys__gen__gearbox_0x114
        type: genesys__gen__gearbox
      inst_genesys__gen__nitrous_strength_0x118:
        pos: ptr_genesys__gen__nitrous_strength_0x118
        type: genesys__gen__nitrous_strength
      size:
        value: 288
      mu_version_hash:
        value: 0x31_c0_27_33
  genesys__gen__hard_driving_behaviour__gas_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
    instances:
      size:
        value: 68
      mu_version_hash:
        value: 0x3c_df_a1_41
  genesys__gen__hard_driving_behaviour__steering_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x64_75_9f_45
  genesys__gen__hard_driving_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__hard_driving_behaviour__gas_effect_0xc
        type: genesys__gen__hard_driving_behaviour__gas_effect
      - id: genesys__gen__hard_driving_behaviour__steering_effect_0x4c
        type: genesys__gen__hard_driving_behaviour__steering_effect
      - id: game_changer_id_0x60
        type: u4
    instances:
      size:
        value: 104
      mu_version_hash:
        value: 0xd0_a7_30_12
  genesys__gen__steering_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: float32_t_0x58
        type: f4
      - id: float32_t_0x5c
        type: f4
      - id: float32_t_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: float32_t_0x68
        type: f4
      - id: float32_t_0x6c
        type: f4
      - id: float32_t_0x70
        type: f4
    instances:
      size:
        value: 120
      mu_version_hash:
        value: 0x9b_b2_c8_08
  genesys__gen__steering_wheel_physics:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
    instances:
      size:
        value: 48
      mu_version_hash:
        value: 0x4f_42_3b_2c
  genesys__gen__suspension:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x52_ba_0c_65
  genesys__gen__tyre__lateral__slip__factors:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x09_e5_f2_87
  genesys__gen__tyre__lateral__grip__curve:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x93_d1_1d_75
  genesys__gen__tyre__long__grip__curve:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: fgow_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x05_0d_26_67
  genesys__gen__tyre__long__slip__factors:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x1c_da_7e_d7
  genesys__gen__tyre:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__tyre__lateral__slip__factors_0xc
        type: genesys__gen__tyre__lateral__slip__factors
      - id: genesys__gen__tyre__lateral__slip__factors_0x30
        type: genesys__gen__tyre__lateral__slip__factors
      - id: genesys__gen__tyre__lateral__grip__curve_0x54
        type: genesys__gen__tyre__lateral__grip__curve
      - id: genesys__gen__tyre__lateral__grip__curve_0x74
        type: genesys__gen__tyre__lateral__grip__curve
      - id: genesys__gen__tyre__lateral__grip__curve_0x94
        type: genesys__gen__tyre__lateral__grip__curve
      - id: genesys__gen__tyre__long__grip__curve_0xb4
        type: genesys__gen__tyre__long__grip__curve
      - id: genesys__gen__tyre__long__grip__curve_0xd4
        type: genesys__gen__tyre__long__grip__curve
      - id: genesys__gen__tyre__long__grip__curve_0xf4
        type: genesys__gen__tyre__long__grip__curve
      - id: genesys__gen__tyre__long__grip__curve_0x114
        type: genesys__gen__tyre__long__grip__curve
      - id: genesys__gen__tyre__long__slip__factors_0x134
        type: genesys__gen__tyre__long__slip__factors
      - id: genesys__gen__tyre__long__slip__factors_0x154
        type: genesys__gen__tyre__long__slip__factors
      - id: game_changer_id_0x174
        type: u4
      - id: float32_t_0x178
        type: f4
      - id: float32_t_0x17c
        type: f4
      - id: float32_t_0x180
        type: f4
      - id: float32_t_0x184
        type: f4
      - id: float32_t_0x188
        type: f4
      - id: float32_t_0x18c
        type: f4
      - id: float32_t_0x190
        type: f4
      - id: float32_t_0x194
        type: f4
      - id: float32_t_0x198
        type: f4
      - id: float32_t_0x19c
        type: f4
    instances:
      size:
        value: 420
      mu_version_hash:
        value: 0x01_4d_7f_4a
  genesys__gen__tyres__tyres:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_genesys__gen__tyre_0x10
        type: u4
      - id: ptr_genesys__gen__tyre_0x14
        type: u4
    instances:
      inst_genesys__gen__tyre_0x10:
        pos: ptr_genesys__gen__tyre_0x10
        type: genesys__gen__tyre
      inst_genesys__gen__tyre_0x14:
        pos: ptr_genesys__gen__tyre_0x14
        type: genesys__gen__tyre
      size:
        value: 28
      mu_version_hash:
        value: 0x15_f8_5f_84
  genesys__gen__vehicle_surface_profile__surface_link:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x10
        type: u4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_cgs_core__unique_id_0x10:
        pos: ptr_arr_cgs_core__unique_id_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 60
      mu_version_hash:
        value: 0x10_e5_5d_05
  genesys__gen__vehicle_surface_profile:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_genesys__gen__vehicle_surface_profile__surface_link_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_genesys__gen__vehicle_surface_profile__surface_link_0x10:
        pos: ptr_arr_genesys__gen__vehicle_surface_profile__surface_link_0x10
        type: genesys__gen__vehicle_surface_profile__surface_link
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xb5_c9_84_4c
  genesys__gen__tyres__surface_effects:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_genesys__gen__vehicle_surface_profile_0x10
        type: u4
    instances:
      inst_genesys__gen__vehicle_surface_profile_0x10:
        pos: ptr_genesys__gen__vehicle_surface_profile_0x10
        type: genesys__gen__vehicle_surface_profile
      size:
        value: 24
      mu_version_hash:
        value: 0x5b_3c_50_7d
  genesys__gen__tyre_sound_params__lateral:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0x21_9f_da_00
  genesys__gen__tyre_sound_params__lat_slip:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: ya_am_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x33_43_76_65
  genesys__gen__tyre_sound_params__longitudinal:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xb2_61_5d_31
  genesys__gen__tyre_sound_params__long_spin_braking:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: ya_am_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xbe_23_b7_07
  genesys__gen__tyre_sound_params__long_spin:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: ya_am_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x7c_10_b4_65
  genesys__gen__tyre_sound_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__tyre_sound_params__lateral_0xc
        type: genesys__gen__tyre_sound_params__lateral
      - id: genesys__gen__tyre_sound_params__lat_slip_0x3c
        type: genesys__gen__tyre_sound_params__lat_slip
      - id: genesys__gen__tyre_sound_params__longitudinal_0x64
        type: genesys__gen__tyre_sound_params__longitudinal
      - id: genesys__gen__tyre_sound_params__long_spin_braking_0x8c
        type: genesys__gen__tyre_sound_params__long_spin_braking
      - id: genesys__gen__tyre_sound_params__long_spin_0xb4
        type: genesys__gen__tyre_sound_params__long_spin
      - id: game_changer_id_0xd8
        type: u4
    instances:
      size:
        value: 224
      mu_version_hash:
        value: 0xb6_0a_56_be
  genesys__gen__tyres:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__tyres__tyres_0xc
        type: genesys__gen__tyres__tyres
      - id: genesys__gen__tyres__surface_effects_0x24
        type: genesys__gen__tyres__surface_effects
      - id: game_changer_id_0x38
        type: u4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: float32_t_0x58
        type: f4
      - id: float32_t_0x5c
        type: f4
      - id: float32_t_0x60
        type: f4
      - id: ptr_genesys__gen__tyre_sound_params_0x64
        type: u4
    instances:
      inst_genesys__gen__tyre_sound_params_0x64:
        pos: ptr_genesys__gen__tyre_sound_params_0x64
        type: genesys__gen__tyre_sound_params
      size:
        value: 108
      mu_version_hash:
        value: 0x54_fe_2c_d0
  genesys__gen__handling_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_genesys__gen__aerodynamic_behaviour_0x10
        type: u4
      - id: ptr_genesys__gen__aligning_torque_0x14
        type: u4
      - id: ptr_genesys__gen__body_movement_behaviour_0x18
        type: u4
      - id: ptr_genesys__gen__brake_behaviour_0x1c
        type: u4
      - id: ptr_genesys__gen__donut_ability_0x20
        type: u4
      - id: ptr_drift_0x24
        type: u4
      - id: ptr_engine_0x28
        type: u4
      - id: ptr_genesys__gen__handbrake_ability_0x2c
        type: u4
      - id: ptr_genesys__gen__hard_driving_behaviour_0x30
        type: u4
      - id: ptr_genesys__gen__steering_behaviour_0x34
        type: u4
      - id: ptr_genesys__gen__steering_wheel_physics_0x38
        type: u4
      - id: ptr_genesys__gen__suspension_0x3c
        type: u4
      - id: ptr_genesys__gen__tyres_0x40
        type: u4
    instances:
      inst_genesys__gen__aerodynamic_behaviour_0x10:
        pos: ptr_genesys__gen__aerodynamic_behaviour_0x10
        type: genesys__gen__aerodynamic_behaviour
      inst_genesys__gen__aligning_torque_0x14:
        pos: ptr_genesys__gen__aligning_torque_0x14
        type: genesys__gen__aligning_torque
      inst_genesys__gen__body_movement_behaviour_0x18:
        pos: ptr_genesys__gen__body_movement_behaviour_0x18
        type: genesys__gen__body_movement_behaviour
      inst_genesys__gen__brake_behaviour_0x1c:
        pos: ptr_genesys__gen__brake_behaviour_0x1c
        type: genesys__gen__brake_behaviour
      inst_genesys__gen__donut_ability_0x20:
        pos: ptr_genesys__gen__donut_ability_0x20
        type: genesys__gen__donut_ability
      inst_drift_0x24:
        pos: ptr_drift_0x24
        type: genesys__gen__drift_behaviour
      inst_engine_0x28:
        pos: ptr_engine_0x28
        type: genesys__gen__engine
      inst_genesys__gen__handbrake_ability_0x2c:
        pos: ptr_genesys__gen__handbrake_ability_0x2c
        type: genesys__gen__handbrake_ability
      inst_genesys__gen__hard_driving_behaviour_0x30:
        pos: ptr_genesys__gen__hard_driving_behaviour_0x30
        type: genesys__gen__hard_driving_behaviour
      inst_genesys__gen__steering_behaviour_0x34:
        pos: ptr_genesys__gen__steering_behaviour_0x34
        type: genesys__gen__steering_behaviour
      inst_genesys__gen__steering_wheel_physics_0x38:
        pos: ptr_genesys__gen__steering_wheel_physics_0x38
        type: genesys__gen__steering_wheel_physics
      inst_genesys__gen__suspension_0x3c:
        pos: ptr_genesys__gen__suspension_0x3c
        type: genesys__gen__suspension
      inst_genesys__gen__tyres_0x40:
        pos: ptr_genesys__gen__tyres_0x40
        type: genesys__gen__tyres
      size:
        value: 72
      mu_version_hash:
        value: 0xe3_29_45_b6
  genesys__gen__nitrous_strength__punch:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xf3_73_fe_06
  genesys__gen__engine_sound2__dsp_param:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: plug_in_0x14
        type: u4
      - id: value_0x18
        type: f4
      - id: unk_enum_0x1c
        type: u4
        doc: enum; bc_35_07_00
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x0a_60_0d_4a
  genesys__gen__engine_sound2__dsp_param_wrapper:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_genesys__gen__engine_sound2__dsp_param_0xc
        type: u4
    instances:
      inst_genesys__gen__engine_sound2__dsp_param_0xc:
        pos: ptr_genesys__gen__engine_sound2__dsp_param_0xc
        type: genesys__gen__engine_sound2__dsp_param
      size:
        value: 20
      mu_version_hash:
        value: 0x93_b1_ae_2d
  genesys__gen__engine_sound2__gain_param:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: gain_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xfb_c0_ba_e4
  genesys__gen__engine_sound2__gain_param_wrapper:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_gain_0xc
        type: u4
    instances:
      inst_gain_0xc:
        pos: ptr_gain_0xc
        type: genesys__gen__engine_sound2__gain_param
      size:
        value: 20
      mu_version_hash:
        value: 0x48_9a_b4_65
  genesys__gen__engine_sound2:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: cgs_resource__handle_0x14
        size: 8
      - id: cgs_resource__handle_0x1c
        size: 8
      - id: cgs_resource__handle_0x24
        size: 8
      - id: cgs_resource__handle_0x2c
        size: 8
      - id: cgs_resource__handle_0x34
        size: 8
      - id: game_changer_id_0x3c
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x40
        type: u4
      - id: ptr_arr_drift_0x44
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x48
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x4c
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x50
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x54
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x58
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x5c
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x60
        type: u4
      - id: ptr_arr_reversing_0x64
        type: u4
      - id: ptr_arr_sequences_0x68
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x6c
        type: u4
      - id: float32_t_0x70
        type: f4
      - id: float32_t_0x74
        type: f4
      - id: float32_t_0x78
        type: f4
      - id: float32_t_0x7c
        type: f4
      - id: float32_t_0x80
        type: f4
      - id: float32_t_0x84
        type: f4
      - id: float32_t_0x88
        type: f4
      - id: float32_t_0x8c
        type: f4
      - id: float32_t_0x90
        type: f4
      - id: float32_t_0x94
        type: f4
      - id: float32_t_0x98
        type: f4
      - id: float32_t_0x9c
        type: f4
      - id: float32_t_0xa0
        type: f4
      - id: float32_t_0xa4
        type: f4
      - id: float32_t_0xa8
        type: f4
      - id: float32_t_0xac
        type: f4
      - id: float32_t_0xb0
        type: f4
      - id: float32_t_0xb4
        type: f4
      - id: float32_t_0xb8
        type: f4
      - id: float32_t_0xbc
        type: f4
      - id: float32_t_0xc0
        type: f4
      - id: float32_t_0xc4
        type: f4
      - id: float32_t_0xc8
        type: f4
      - id: float32_t_0xcc
        type: f4
      - id: float32_t_0xd0
        type: f4
      - id: float32_t_0xd4
        type: f4
      - id: ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8
        type: u4
      - id: ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc
        type: u4
      - id: ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0
        type: u4
      - id: ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4
        type: u4
      - id: ptr_arr_genesys__gen__engine_sound2__gain_param_wrapper_0xe8
        type: u4
      - id: array_count_for_0xd8
        type: u2
      - id: array_count_for_0xdc
        type: u2
      - id: array_count_for_0xe8
        type: u2
      - id: array_count_for_0xe0
        type: u2
      - id: array_count_for_0xe4
        type: u2
      - id: bool8_t_0xf6
        type: u1
      - id: array_count_for_0x40
        type: u1
      - id: array_count_for_0x44
        type: u1
      - id: array_count_for_0x4c
        type: u1
      - id: array_count_for_0x48
        type: u1
      - id: array_count_for_0x54
        type: u1
      - id: array_count_for_0x50
        type: u1
      - id: array_count_for_0x58
        type: u1
      - id: array_count_for_0x5c
        type: u1
      - id: array_count_for_0x60
        type: u1
      - id: uint8_t_0x100
        type: u1
      - id: array_count_for_0x64
        type: u1
      - id: array_count_for_0x68
        type: u1
        doc: '"SequencesCount"'
      - id: array_count_for_0x6c
        type: u1
    instances:
      inst_cgs_resource__handle_0x40:
        pos: ptr_arr_cgs_resource__handle_0x40
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x40
      inst_drift_0x44:
        pos: ptr_arr_drift_0x44
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x44
      inst_cgs_resource__handle_0x48:
        pos: ptr_arr_cgs_resource__handle_0x48
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x48
      inst_cgs_resource__handle_0x4c:
        pos: ptr_arr_cgs_resource__handle_0x4c
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x4c
      inst_cgs_resource__handle_0x50:
        pos: ptr_arr_cgs_resource__handle_0x50
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x50
      inst_cgs_resource__handle_0x54:
        pos: ptr_arr_cgs_resource__handle_0x54
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x54
      inst_cgs_resource__handle_0x58:
        pos: ptr_arr_cgs_resource__handle_0x58
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x58
      inst_cgs_resource__handle_0x5c:
        pos: ptr_arr_cgs_resource__handle_0x5c
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x5c
      inst_cgs_resource__handle_0x60:
        pos: ptr_arr_cgs_resource__handle_0x60
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x60
      inst_reversing_0x64:
        pos: ptr_arr_reversing_0x64
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x64
      inst_sequences_0x68:
        pos: ptr_arr_sequences_0x68
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x68
      inst_cgs_resource__handle_0x6c:
        pos: ptr_arr_cgs_resource__handle_0x6c
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x6c
      inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8:
        pos: ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8
        type: genesys__gen__engine_sound2__dsp_param_wrapper
        repeat: expr
        repeat-expr: array_count_for_0xd8
      inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc:
        pos: ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc
        type: genesys__gen__engine_sound2__dsp_param_wrapper
        repeat: expr
        repeat-expr: array_count_for_0xdc
      inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0:
        pos: ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0
        type: genesys__gen__engine_sound2__dsp_param_wrapper
        repeat: expr
        repeat-expr: array_count_for_0xe0
      inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4:
        pos: ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4
        type: genesys__gen__engine_sound2__dsp_param_wrapper
        repeat: expr
        repeat-expr: array_count_for_0xe4
      inst_genesys__gen__engine_sound2__gain_param_wrapper_0xe8:
        pos: ptr_arr_genesys__gen__engine_sound2__gain_param_wrapper_0xe8
        type: genesys__gen__engine_sound2__gain_param_wrapper
        repeat: expr
        repeat-expr: array_count_for_0xe8
      size:
        value: 264
      mu_version_hash:
        value: 0x6d_f4_bf_f4
  genesys__gen__vehicle__driver_setup__seat_belt_bone_offset:
    seq:
      - id: base_object
        type: gen_obj
      - id: position_0x10
        type: rw_math_vpu__vector3
      - id: rotation_0x20
        type: rw_math_vpu__vector3
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xd3_2c_dc_8a
  genesys__gen__vehicle__driver_setup:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector3_0x10
        type: rw_math_vpu__vector3
      - id: ptr_arr_cgs_core__unique_id_0x20
        type: u4
      - id: cgs_core__unique_id_0x24
        type: u4
      - id: game_changer_id_0x28
        type: u4
      - id: cgs_core__unique_id_0x2c
        type: u4
      - id: cgs_core__unique_id_0x30
        type: u4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: ptr_arr_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c
        type: u4
      - id: array_count_for_0x20
        type: u2
      - id: array_count_for_0x3c
        type: u2
      - id: bool8_t_0x44
        type: u1
      - id: bool8_t_0x45
        type: u1
      - id: bool8_t_0x46
        type: u1
      - id: bool8_t_0x47
        type: u1
    instances:
      inst_cgs_core__unique_id_0x20:
        pos: ptr_arr_cgs_core__unique_id_0x20
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x20
      inst_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c:
        pos: ptr_arr_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c
        type: genesys__gen__vehicle__driver_setup__seat_belt_bone_offset
        repeat: expr
        repeat-expr: array_count_for_0x3c
      size:
        value: 76
      mu_version_hash:
        value: 0xd5_a7_20_62
  genesys__gen__steering_wheel_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: cgs_resource__handle_0x1c
        size: 8
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xba_3e_b8_57
  genesys__gen__steering_behaviour__steering_angle_curve:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0xea_90_bc_d0
  genesys__gen__vehicle__sound:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: horn_0x18
        type: u4
      - id: cgs_core__unique_id_0x1c
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x20
        type: u4
      - id: array_count_for_0x20
        type: u2
      - id: padding
        size: 2
    instances:
      inst_cgs_core__unique_id_0x20:
        pos: ptr_arr_cgs_core__unique_id_0x20
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x20
      size:
        value: 40
      mu_version_hash:
        value: 0x1f_e8_ef_c0
  genesys__gen__suspension_wheel:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: cgs_core__string_base_0x14
        type: string_base
      - id: damage_0x1c
        size: 8
      - id: cgs_resource__handle_0x24
        size: 8
      - id: cgs_resource__handle_0x2c
        size: 8
      - id: game_changer_id_0x34
        type: u4
      - id: float32_t_0x38
        type: f4
    instances:
      size:
        value: 64
      mu_version_hash:
        value: 0x4c_3e_7d_35
  genesys__gen__wheel_suspension_constraint:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: angle_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: bool8_t_0x28
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x7b_c0_7d_85
  genesys__gen__wheel_suspension_spring_constraint:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: bool8_t_0x24
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x2b_eb_51_e8
  genesys__gen__light__projected_texture:
    seq:
      - id: base_object
        type: genesys__gen__light__base
      - id: rw_math_vpu__vector2_0x60
        type: rw_math_vpu__vector2
      - id: rw_math_vpu__vector3_0x70
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector4_0x80
        type: rw_math_vpu__vector4
      - id: material_0x90
        size: 8
    instances:
      size:
        value: 152
      mu_version_hash:
        value: 0x0d_a8_4d_eb
  genesys__gen__pidcontroller:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x02_dc_ac_cf
  genesys__gen__body_movement_behaviour__angle_control:
    seq:
      - id: base_object
        type: gen_obj
      - id: damping_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xb4_39_c9_0b
  genesys__gen__vehicle_damage_behaviour__damage_sequence:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x42_23_79_c9
  genesys__gen__vfx_locator_group_vehicle_spot_effect_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: rw_math_vpu__vector3_0x30
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x40
        type: rw_math_vpu__vector3
      - id: intensity_0x50
        type: genesys__gen__sequence_item__modulating_double_value
      - id: cgs_core__string_base_0x88
        type: string_base
      - id: cgs_resource__handle_0x90
        size: 8
      - id: locator_group_0x98
        type: u4
    instances:
      size:
        value: 160
      mu_version_hash:
        value: 0x22_3a_4d_f2
  genesys__gen__camera_gameplay_bonnet__wind_sound:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xc3_33_10_aa
  genesys__gen__camera_gameplay_external__acceleration_movement:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
    instances:
      size:
        value: 64
      mu_version_hash:
        value: 0x79_b5_42_d5
  genesys__gen__camera_gameplay_external__yaw_spring_modification:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: x_ryd_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
    instances:
      size:
        value: 48
      mu_version_hash:
        value: 0x30_87_ee_63
  genesys__gen__camera_gameplay_external__speed_based_height_change:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xb9_46_0d_d9
  genesys__gen__camera_gameplay_external_globals__impact_shake:
    seq:
      - id: base_object
        type: gen_obj
      - id: inline_arr_float32_t_0xc
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: inline_arr_float32_t_0x18
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: inline_arr_float32_t_0x24
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: game_changer_id_0x30
        type: u4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: array_count_for_0xc
        type: u2
      - id: array_count_for_0x18
        type: u2
      - id: array_count_for_0x24
        type: u2
      - id: padding
        size: 2
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0x85_41_2c_35
  genesys__gen__high_shelf_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
      - id: gain_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xf7_54_09_1e
  genesys__gen__camera_gameplay_bonnet:
    seq:
      - id: base_object
        type: gen_obj
      - id: inline_arr_float32_t_0xc
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: inline_arr_float32_t_0x18
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: inline_arr_float32_t_0x24
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: game_changer_id_0x30
        type: u4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: float32_t_0x58
        type: f4
      - id: float32_t_0x5c
        type: f4
      - id: float32_t_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: float32_t_0x68
        type: f4
      - id: float32_t_0x6c
        type: f4
      - id: int32_t_0x70
        type: s4
      - id: int32_t_0x74
        type: s4
      - id: array_count_for_0xc
        type: u2
      - id: array_count_for_0x18
        type: u2
      - id: array_count_for_0x24
        type: u2
        doc: '"P0KR"'
      - id: padding
        size: 2
    instances:
      size:
        value: 128
      mu_version_hash:
        value: 0xc7_38_ed_50
  genesys__gen__camera_gameplay_bumper:
    seq:
      - id: base_object
        type: genesys__gen__camera_gameplay_bonnet
    instances:
      size:
        value: 132
      mu_version_hash:
        value: 0x3a_9d_63_ee
  genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: damage_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x57_fb_ae_22
  genesys__gen__vehicle_damage_behaviour__bodypart:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector2_0x10
        type: rw_math_vpu__vector2
      - id: rw_math_vpu__vector2_0x20
        type: rw_math_vpu__vector2
      - id: rw_math_vpu__vector2_0x30
        type: rw_math_vpu__vector2
      - id: rw_math_vpu__vector3_0x40
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x50
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x60
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x70
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector4_0x80
        type: rw_math_vpu__vector4
      - id: cgs_core__string_base_0x90
        type: string_base
      - id: cgs_resource__handle_0x98
        size: 8
      - id: game_changer_id_0xa0
        type: u4
      - id: locator_group_0xa4
        type: u4
      - id: mass_0xa8
        type: f4
      - id: ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac
        type: u4
      - id: unk_enum_0xb0
        type: u2
        doc: enum; d9_31_00_00
      - id: array_count_for_0xac
        type: u2
      - id: bool8_t_0xb4
        type: u1
      - id: padding
        size: 3
    instances:
      inst_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac:
        pos: ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac
        type: genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold
        repeat: expr
        repeat-expr: array_count_for_0xac
      size:
        value: 184
      mu_version_hash:
        value: 0x1e_65_59_e2
  genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: amplitude_0x10
        type: f4
      - id: frequency_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: power_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xe2_01_2c_06
  genesys__gen__camera_gameplay_external__speed_based_movement:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake_0xc
        type: genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake
      - id: game_changer_id_0x30
        type: u4
      - id: float32_t_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
    instances:
      size:
        value: 76
      mu_version_hash:
        value: 0x75_04_48_a2
  genesys__gen__camera_gameplay_external__camera__roll:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
    instances:
      size:
        value: 48
      mu_version_hash:
        value: 0xd1_22_20_3a
  genesys__gen__camera_gameplay_external__deceleration__pitch__change:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x2f_d3_1d_aa
  genesys__gen__camera_gameplay_external_globals__lens_properties:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: bool8_t_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x8f_25_9b_de
  genesys__gen__camera_gameplay_external_globals:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__camera_gameplay_external_globals__impact_shake_0xc
        type: genesys__gen__camera_gameplay_external_globals__impact_shake
      - id: genesys__gen__camera_gameplay_external_globals__lens_properties_0x6c
        type: genesys__gen__camera_gameplay_external_globals__lens_properties
      - id: game_changer_id_0x88
        type: u4
      - id: ptr_genesys__gen__camera_gameplay_shake_effect_0x8c
        type: u4
    instances:
      inst_genesys__gen__camera_gameplay_shake_effect_0x8c:
        pos: ptr_genesys__gen__camera_gameplay_shake_effect_0x8c
        type: genesys__gen__camera_gameplay_shake_effect
      size:
        value: 148
      mu_version_hash:
        value: 0xdb_89_19_ba
  genesys__gen__camera_gameplay_gradient_adjustments__params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x17_ab_8a_15
  genesys__gen__camera_gameplay_gradient_adjustments:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__camera_gameplay_gradient_adjustments__params_0xc
        type: genesys__gen__camera_gameplay_gradient_adjustments__params
      - id: genesys__gen__camera_gameplay_gradient_adjustments__params_0x24
        type: genesys__gen__camera_gameplay_gradient_adjustments__params
      - id: game_changer_id_0x3c
        type: u4
      - id: float32_t_0x40
        type: f4
    instances:
      size:
        value: 72
      mu_version_hash:
        value: 0x3a_76_eb_32
  genesys__gen__camera_gameplay_external:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__camera_gameplay_external__speed_based_movement_0xc
        type: genesys__gen__camera_gameplay_external__speed_based_movement
      - id: genesys__gen__camera_gameplay_external__acceleration_movement_0x54
        type: genesys__gen__camera_gameplay_external__acceleration_movement
      - id: genesys__gen__camera_gameplay_external__camera__roll_0x90
        type: genesys__gen__camera_gameplay_external__camera__roll
      - id: genesys__gen__camera_gameplay_external__yaw_spring_modification_0xbc
        type: genesys__gen__camera_gameplay_external__yaw_spring_modification
      - id: genesys__gen__camera_gameplay_external__deceleration__pitch__change_0xe8
        type: genesys__gen__camera_gameplay_external__deceleration__pitch__change
      - id: genesys__gen__camera_gameplay_external__speed_based_height_change_0x10c
        type: genesys__gen__camera_gameplay_external__speed_based_height_change
      - id: inline_arr_float32_t_0x124
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: inline_arr_float32_t_0x130
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: inline_arr_float32_t_0x13c
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: inline_arr_float32_t_0x148
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: cgs_resource__handle_0x154
        size: 8
      - id: game_changer_id_0x15c
        type: u4
      - id: float32_t_0x160
        type: f4
      - id: float32_t_0x164
        type: f4
      - id: float32_t_0x168
        type: f4
      - id: float32_t_0x16c
        type: f4
      - id: float32_t_0x170
        type: f4
      - id: ptr_genesys__gen__camera_gameplay_external_globals_0x174
        type: u4
      - id: ptr_genesys__gen__camera_gameplay_gradient_adjustments_0x178
        type: u4
      - id: array_count_for_0x124
        type: u2
      - id: array_count_for_0x130
        type: u2
      - id: array_count_for_0x13c
        type: u2
      - id: array_count_for_0x148
        type: u2
        doc: '"P0KR"'
      - id: uint8_t_0x184
        type: u1
      - id: uint8_t_0x185
        type: u1
      - id: padding
        size: 2
    instances:
      inst_genesys__gen__camera_gameplay_external_globals_0x174:
        pos: ptr_genesys__gen__camera_gameplay_external_globals_0x174
        type: genesys__gen__camera_gameplay_external_globals
      inst_genesys__gen__camera_gameplay_gradient_adjustments_0x178:
        pos: ptr_genesys__gen__camera_gameplay_gradient_adjustments_0x178
        type: genesys__gen__camera_gameplay_gradient_adjustments
      size:
        value: 392
      mu_version_hash:
        value: 0xbb_ad_ac_a9
  genesys__gen__vehicle_damage_behaviour__spot_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: locator_group_0x18
        type: u4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xf5_70_25_85
  genesys__gen__vehicle_paint__material_properties:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector3_0x10
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x20
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector4_0x30
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x40
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x50
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x60
        type: rw_math_vpu__vector4
      - id: game_changer_id_0x70
        type: u4
      - id: float32_t_0x74
        type: f4
      - id: float32_t_0x78
        type: f4
    instances:
      size:
        value: 128
      mu_version_hash:
        value: 0xac_a5_6f_a5
  genesys__gen__camera_rear_view_globals:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x0f_78_2d_29
  genesys__gen__camera_rear_view:
    seq:
      - id: base_object
        type: gen_obj
      - id: inline_arr_float32_t_0xc
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: game_changer_id_0x18
        type: u4
      - id: float32_t_0x1c
        type: f4
      - id: ptr_genesys__gen__camera_rear_view_globals_0x20
        type: u4
      - id: array_count_for_0xc
        type: u2
      - id: padding
        size: 2
    instances:
      inst_genesys__gen__camera_rear_view_globals_0x20:
        pos: ptr_genesys__gen__camera_rear_view_globals_0x20
        type: genesys__gen__camera_rear_view_globals
      size:
        value: 40
      mu_version_hash:
        value: 0x3b_7e_06_ec
  genesys__gen__vehicle_paint__structure2:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0x40_7f_fb_f1
  genesys__gen__vehicle_vfx_behaviour__corona:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: cgs_resource__handle_0x20
        size: 8
      - id: corona_definition_0x28
        size: 8
      - id: locator_group_0x30
        type: u4
      - id: brightness_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: unk_enum_0x40
        type: u2
        doc: enum; 04_32_00_00
      - id: time_of_day_0x42
        type: u2
        doc: enum; 18_32_00_00
      - id: bool8_t_0x44
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 72
      mu_version_hash:
        value: 0xcd_60_4e_4a
  genesys__gen__vehicle_vfx_behaviour__light:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: cgs_resource__handle_0x20
        size: 8
      - id: light_definition_0x28
        size: 8
      - id: locator_group_0x30
        type: u4
      - id: float32_t_0x34
        type: f4
      - id: unk_enum_0x38
        type: u2
        doc: enum; 04_32_00_00
      - id: time_of_day_0x3a
        type: u2
        doc: enum; 18_32_00_00
    instances:
      size:
        value: 64
      mu_version_hash:
        value: 0x07_5e_e9_62
  genesys__gen__vehicle_vfx_behaviour__spot_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: locator_group_0x14
        type: u4
      - id: unk_enum_0x18
        type: u2
        doc: enum; 04_32_00_00
      - id: time_of_day_0x1a
        type: u2
        doc: enum; 18_32_00_00
      - id: bool8_t_0x1c
        type: u1
      - id: bool8_t_0x1d
        type: u1
      - id: padding
        size: 2
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x81_56_a6_f2
  genesys__gen__passby_sequence_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: cgs_resource__handle_0x1c
        size: 8
      - id: cgs_resource__handle_0x24
        size: 8
      - id: cgs_resource__handle_0x2c
        size: 8
      - id: cgs_resource__handle_0x34
        size: 8
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: float32_t_0x58
        type: f4
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0xb7_ee_51_b2
  genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector3_0x10
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x20
        type: rw_math_vpu__vector3
      - id: game_changer_id_0x30
        type: u4
    instances:
      size:
        value: 56
      mu_version_hash:
        value: 0x3b_b7_85_6a
  genesys__gen__race_car_physical_definition__convex_hull_conectivity_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10:
        pos: ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10
        type: genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x56_27_d2_53
  genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: halfsize_0x50
        type: rw_math_vpu__vector3
      - id: game_changer_id_0x60
        type: u4
      - id: i6je_0x64
        type: s4
    instances:
      size:
        value: 108
      mu_version_hash:
        value: 0x28_77_c8_41
  genesys__gen__race_car_physical_definition__physical_definition__rigid_body__capsule_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: game_changer_id_0x50
        type: u4
      - id: half_length_0x54
        type: f4
      - id: radius_0x58
        type: f4
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0x01_12_fc_16
  genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: convex_hull_0x50
        size: 8
      - id: game_changer_id_0x58
        type: u4
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0x63_33_d3_31
  genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: game_changer_id_0x50
        type: u4
      - id: half_length_0x54
        type: f4
      - id: radius_0x58
        type: f4
    instances:
      size:
        value: 96
      mu_version_hash:
        value: 0x01_12_fc_16
  genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume:
    seq:
      - id: base_object
        type: gen_obj
      - id: volume_to_body_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: game_changer_id_0x50
        type: u4
      - id: radius_0x54
        type: f4
    instances:
      size:
        value: 92
      mu_version_hash:
        value: 0xf9_19_5e_af
  genesys__gen__race_car_physical_definition__physical_definition__rigid_body:
    seq:
      - id: base_object
        type: gen_obj
      - id: body_to_object_transform_0x10
        type: rw_math_vpu__matrix44affine
      - id: com_offset_0x50
        type: rw_math_vpu__vector3
      - id: inertia__scale_0x60
        type: rw_math_vpu__vector3
      - id: local_aabbcenter_0x70
        type: rw_math_vpu__vector3
      - id: local_aabbhalf_diagonal_0x80
        type: rw_math_vpu__vector3
      - id: ptr_arr_symmetrical_in_axis_0x90
        type: u4
      - id: game_changer_id_0x94
        type: u4
      - id: angular_drag_0x98
        type: f4
      - id: bounciness_0x9c
        type: f4
      - id: friction_0xa0
        type: f4
      - id: linear_drag_0xa4
        type: f4
      - id: mass_0xa8
        type: f4
      - id: ptr_arr_box_volumes_0xac
        type: u4
      - id: ptr_arr_capsule_volumes_0xb0
        type: u4
      - id: ptr_bounding_convex_hull_0xb4
        type: u4
      - id: ptr_arr_convex_hull_volumes_0xb8
        type: u4
      - id: ptr_arr_cylinder_volumes_0xbc
        type: u4
      - id: ptr_arr_sphere_volumes_0xc0
        type: u4
      - id: array_count_for_0xac
        type: u2
        doc: '"BoxVolumesCount"'
      - id: array_count_for_0xb0
        type: u2
        doc: '"CapsuleVolumesCount"'
      - id: array_count_for_0xb8
        type: u2
        doc: '"ConvexHullVolumesCount"'
      - id: array_count_for_0xbc
        type: u2
        doc: '"CylinderVolumesCount"'
      - id: array_count_for_0xc0
        type: u2
        doc: '"SphereVolumesCount"'
      - id: array_count_for_0x90
        type: u2
        doc: '"SymmetricalInAxisCount"'
      - id: is_wheel_0xd0
        type: u1
      - id: padding
        size: 3
    instances:
      inst_symmetrical_in_axis_0x90:
        pos: ptr_arr_symmetrical_in_axis_0x90
        type: u1
        repeat: expr
        repeat-expr: array_count_for_0x90
      inst_box_volumes_0xac:
        pos: ptr_arr_box_volumes_0xac
        type: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume
        repeat: expr
        repeat-expr: array_count_for_0xac
      inst_capsule_volumes_0xb0:
        pos: ptr_arr_capsule_volumes_0xb0
        type: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__capsule_volume
        repeat: expr
        repeat-expr: array_count_for_0xb0
      inst_bounding_convex_hull_0xb4:
        pos: ptr_bounding_convex_hull_0xb4
        type: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume
      inst_convex_hull_volumes_0xb8:
        pos: ptr_arr_convex_hull_volumes_0xb8
        type: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume
        repeat: expr
        repeat-expr: array_count_for_0xb8
      inst_cylinder_volumes_0xbc:
        pos: ptr_arr_cylinder_volumes_0xbc
        type: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume
        repeat: expr
        repeat-expr: array_count_for_0xbc
      inst_sphere_volumes_0xc0:
        pos: ptr_arr_sphere_volumes_0xc0
        type: genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume
        repeat: expr
        repeat-expr: array_count_for_0xc0
      size:
        value: 212
      mu_version_hash:
        value: 0x5d_6d_83_cc
  genesys__gen__race_car_physical_definition__physical_definition:
    seq:
      - id: base_object
        type: gen_obj
      - id: local_aabbcenter_0x10
        type: rw_math_vpu__vector3
      - id: local_aabbhalf_diagonal_0x20
        type: rw_math_vpu__vector3
      - id: additional_info_0x30
        size: 8
      - id: ptr_arr_rigid_bodies_names_0x38
        type: u4
      - id: game_changer_id_0x3c
        type: u4
      - id: ptr_arr_rigid_bodies_0x40
        type: u4
      - id: game_changer_id_0x44
        type: s4
      - id: main_rigid_body_index_0x48
        type: s4
      - id: array_count_for_0x40
        type: u2
        doc: '"RigidBodiesCount"'
      - id: array_count_for_0x38
        type: u2
        doc: '"RigidBodiesNamesCount"'
      - id: bool8_t_0x50
        type: u1
      - id: bool8_t_0x51
        type: u1
      - id: padding
        size: 2
    instances:
      inst_rigid_bodies_names_0x38:
        pos: ptr_arr_rigid_bodies_names_0x38
        type: string_base
        repeat: expr
        repeat-expr: array_count_for_0x38
      inst_rigid_bodies_0x40:
        pos: ptr_arr_rigid_bodies_0x40
        type: genesys__gen__race_car_physical_definition__physical_definition__rigid_body
        repeat: expr
        repeat-expr: array_count_for_0x40
      size:
        value: 84
      mu_version_hash:
        value: 0x96_2d_8d_39
  genesys__gen__race_car_physical_definition:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10
        type: u4
      - id: ptr_genesys__gen__race_car_physical_definition__physical_definition_0x14
        type: u4
      - id: int32_t_0x18
        type: s4
      - id: int32_t_0x1c
        type: s4
      - id: int32_t_0x20
        type: s4
      - id: int32_t_0x24
        type: s4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10:
        pos: ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10
        type: genesys__gen__race_car_physical_definition__convex_hull_conectivity_data
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_genesys__gen__race_car_physical_definition__physical_definition_0x14:
        pos: ptr_genesys__gen__race_car_physical_definition__physical_definition_0x14
        type: genesys__gen__race_car_physical_definition__physical_definition
      size:
        value: 44
      mu_version_hash:
        value: 0x4e_75_f6_26
  genesys__gen__nitrous_parameters__crash_escape:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: minimum_speed_0x14
        type: f4
      - id: nitrous_reward_0x18
        type: f4
      - id: is_enabled_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x57_35_1a_22
  genesys__gen__vehicle_camera_container:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_genesys__gen__camera_gameplay_bonnet_0x10
        type: u4
      - id: ptr_genesys__gen__camera_gameplay_bumper_0x14
        type: u4
      - id: ptr_genesys__gen__camera_gameplay_external_0x18
        type: u4
      - id: ptr_genesys__gen__camera_rear_view_0x1c
        type: u4
    instances:
      inst_genesys__gen__camera_gameplay_bonnet_0x10:
        pos: ptr_genesys__gen__camera_gameplay_bonnet_0x10
        type: genesys__gen__camera_gameplay_bonnet
      inst_genesys__gen__camera_gameplay_bumper_0x14:
        pos: ptr_genesys__gen__camera_gameplay_bumper_0x14
        type: genesys__gen__camera_gameplay_bumper
      inst_genesys__gen__camera_gameplay_external_0x18:
        pos: ptr_genesys__gen__camera_gameplay_external_0x18
        type: genesys__gen__camera_gameplay_external
      inst_genesys__gen__camera_rear_view_0x1c:
        pos: ptr_genesys__gen__camera_rear_view_0x1c
        type: genesys__gen__camera_rear_view
      size:
        value: 36
      mu_version_hash:
        value: 0x05_28_73_c0
  genesys__gen__vehicle_colour_palette:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x10
        type: u4
      - id: ptr_arr_ptr_genesys__gen__colour_group_0x14
        type: u4
      - id: array_count_for_0x14
        type: u1
      - id: array_count_for_0x10
        type: u1
      - id: padding
        size: 2
    instances:
      inst_cgs_resource__handle_0x10:
        pos: ptr_arr_cgs_resource__handle_0x10
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_genesys__gen__colour_group_0x14:
        pos: ptr_arr_ptr_genesys__gen__colour_group_0x14
        type: ptr('genesys__gen__colour_group')
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 28
      mu_version_hash:
        value: 0xf2_1d_49_9c
  genesys__gen__nitrous_parameters_usage:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: decrease_nitrous_0x10
        type: f4
      - id: time_to_full_nitrous_0x14
        type: f4
      - id: enabled_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x17_ee_4b_7d
  genesys__gen__nitrous_parameters__speedbreaker_usage:
    seq:
      - id: base_object
        type: genesys__gen__nitrous_parameters_usage
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x96_5c_07_2b
  genesys__gen__nitrous_parameters:
    seq:
      - id: base_object
        type: gen_obj
      - id: traffic_oncoming_0xc
        type: genesys__gen__nitrous_parameters__traffic_oncoming
      - id: balancing_0x34
        type: genesys__gen__nitrous_parameters__balancing
      - id: donutting_0x58
        type: genesys__gen__nitrous_parameters__donutting
      - id: drifting_0x7c
        type: genesys__gen__nitrous_parameters__drifting
      - id: hitting_another_competitor_0xa0
        type: genesys__gen__nitrous_parameters__hitting_another_competitor
      - id: punch_0xc4
        type: genesys__gen__nitrous_parameters__punch_usage
      - id: slip_streaming_0xe8
        type: genesys__gen__nitrous_parameters__slipstreaming
      - id: catching_air_0x10c
        type: genesys__gen__nitrous_parameters__catching_air
      - id: crash_escape_0x12c
        type: genesys__gen__nitrous_parameters__crash_escape
      - id: driving_at_high_speed_0x14c
        type: genesys__gen__nitrous_parameters__high_speed
      - id: driving_at_speed_0x16c
        type: genesys__gen__nitrous_parameters__min_speed
      - id: nitrous_0x18c
        type: genesys__gen__nitrous_parameters__nitrous_usage
      - id: taking_shortcut_0x1ac
        type: genesys__gen__nitrous_parameters__taking_shortcut
      - id: traffic_near_miss_0x1cc
        type: genesys__gen__nitrous_parameters__traffic_near_miss
      - id: traffic_near_miss_oncoming_0x1ec
        type: genesys__gen__nitrous_parameters__traffic_near_miss
      - id: fatal_hit_0x20c
        type: genesys__gen__nitrous_parameters__fatal_hit
      - id: jump_0x228
        type: genesys__gen__nitrous_parameters__jump_usage
      - id: shared_0x244
        type: genesys__gen__nitrous_parameters__restrictions
      - id: genesys__gen__nitrous_parameters__speedbreaker_usage_0x260
        type: genesys__gen__nitrous_parameters__speedbreaker_usage
      - id: game_changer_id_0x27c
        type: u4
    instances:
      size:
        value: 644
      mu_version_hash:
        value: 0x33_03_a1_b4
  genesys__gen__nitrous_parameters__drifting:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: minimum_speed_0x14
        type: f4
      - id: nitrous_reward_0x18
        type: f4
      - id: time_drifting_0x1c
        type: f4
      - id: is_enabled_0x20
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x83_90_1a_a6
  genesys__gen__nitrous_parameters__punch_usage:
    seq:
      - id: base_object
        type: genesys__gen__nitrous_parameters_usage
      - id: punch_burn_percent_0x1c
        type: f4
      - id: punch_delay_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xcf_6c_14_50
  genesys__gen__nitrous_parameters__min_speed:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: minimum_speed_0x14
        type: f4
      - id: nitrous_reward_0x18
        type: f4
      - id: is_enabled_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xe1_d8_d1_1f
  genesys__gen__nitrous_parameters__nitrous_usage:
    seq:
      - id: base_object
        type: genesys__gen__nitrous_parameters_usage
      - id: min_nitrous_time_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x04_cb_c8_7c
  genesys__gen__nitrous_parameters__taking_shortcut:
    seq:
      - id: base_object
        type: gen_obj
      - id: message_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: minimum_speed_0x14
        type: f4
      - id: nitrous_reward_0x18
        type: f4
      - id: is_enabled_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x64_9a_22_d4
  genesys__gen__nitrous_parameters__jump_usage:
    seq:
      - id: base_object
        type: genesys__gen__nitrous_parameters_usage
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x37_c9_32_bd
  genesys__gen__nitrous_parameters__restrictions:
    seq:
      - id: base_object
        type: gen_obj
      - id: nitrous_ready_message_0xc
        type: u4
      - id: min_nitrous_amount_0x10
        type: f4
      - id: min_nitrous_punch_0x14
        type: f4
      - id: min_nitrous_speed_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x52_20_55_c0
  genesys__gen__vehicle_component__wheel:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: type_0x10
        type: u4
        doc: enum; f3_0d_06_00
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x99_f8_6b_c8
  genesys__gen__vehicle_component:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: category_0x14
        size: 8
      - id: cgs_resource__handle_0x1c
        size: 8
      - id: cgs_resource__handle_0x24
        size: 8
      - id: cgs_resource__handle_0x2c
        size: 8
      - id: cgs_resource__handle_0x34
        size: 8
      - id: cgs_resource__handle_0x3c
        size: 8
      - id: cgs_resource__handle_0x44
        size: 8
      - id: cgs_resource__handle_0x4c
        size: 8
      - id: cgs_resource__handle_0x54
        size: 8
      - id: game_changer_id_0x5c
        type: u4
      - id: cgs_core__unique_id_0x60
        type: u4
      - id: manufacturer_0x64
        type: u4
      - id: name_0x68
        type: u4
      - id: cgs_core__unique_id_0x6c
        type: u4
      - id: cgs_core__unique_id_0x70
        type: u4
      - id: cgs_core__unique_id_0x74
        type: u4
      - id: cgs_core__unique_id_0x78
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x7c
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x80
        type: u4
      - id: ptr_arr_genesys__gen__vehicle_component__wheel_0x84
        type: u4
      - id: array_count_for_0x7c
        type: u2
      - id: array_count_for_0x84
        type: u2
      - id: bool8_t_0x8c
        type: u1
      - id: bool8_t_0x8d
        type: u1
      - id: bool8_t_0x8e
        type: u1
      - id: bool8_t_0x8f
        type: u1
      - id: bool8_t_0x90
        type: u1
      - id: bool8_t_0x91
        type: u1
      - id: bool8_t_0x92
        type: u1
      - id: bool8_t_0x93
        type: u1
      - id: array_count_for_0x80
        type: u1
      - id: uint8_t_0x95
        type: u1
      - id: padding
        size: 2
    instances:
      inst_cgs_core__unique_id_0x7c:
        pos: ptr_arr_cgs_core__unique_id_0x7c
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x7c
      inst_cgs_resource__handle_0x80:
        pos: ptr_arr_cgs_resource__handle_0x80
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x80
      inst_genesys__gen__vehicle_component__wheel_0x84:
        pos: ptr_arr_genesys__gen__vehicle_component__wheel_0x84
        type: genesys__gen__vehicle_component__wheel
        repeat: expr
        repeat-expr: array_count_for_0x84
      size:
        value: 152
      mu_version_hash:
        value: 0xcb_99_ba_be
  genesys__gen__vehicle_damage_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: cgs_resource__handle_0x1c
        size: 8
      - id: ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart_0x24
        type: u4
      - id: ptr_arr_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28
        type: u4
      - id: ptr_arr_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c
        type: u4
      - id: array_count_for_0x24
        type: u2
      - id: array_count_for_0x28
        type: u2
      - id: array_count_for_0x2c
        type: u2
      - id: padding
        size: 2
    instances:
      inst_genesys__gen__vehicle_damage_behaviour__bodypart_0x24:
        pos: ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart_0x24
        type: genesys__gen__vehicle_damage_behaviour__bodypart
        repeat: expr
        repeat-expr: array_count_for_0x24
      inst_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28:
        pos: ptr_arr_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28
        type: genesys__gen__vehicle_damage_behaviour__damage_sequence
        repeat: expr
        repeat-expr: array_count_for_0x28
      inst_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c:
        pos: ptr_arr_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c
        type: genesys__gen__vehicle_damage_behaviour__spot_effect
        repeat: expr
        repeat-expr: array_count_for_0x2c
      size:
        value: 56
      mu_version_hash:
        value: 0x70_1a_f0_04
  genesys__gen__vehicle_info__axle:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x18
        type: u4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: array_count_for_0x18
        type: u2
      - id: padding
        size: 2
    instances:
      inst_cgs_resource__handle_0x18:
        pos: ptr_arr_cgs_resource__handle_0x18
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 40
      mu_version_hash:
        value: 0xcd_13_11_72
  genesys__gen__vehicle_info__extra_axle:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: int32_t_0x14
        type: s4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xd5_e6_e4_bf
  genesys__gen__vehicle_info:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__matrix44affine_0x10
        type: rw_math_vpu__matrix44affine
      - id: rw_math_vpu__vector3_0x50
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x60
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x70
        type: rw_math_vpu__vector3
      - id: game_changer_id_0x80
        type: u4
      - id: float32_t_0x84
        type: f4
      - id: float32_t_0x88
        type: f4
      - id: float32_t_0x8c
        type: f4
      - id: float32_t_0x90
        type: f4
      - id: float32_t_0x94
        type: f4
      - id: ptr_arr_genesys__gen__vehicle_info__axle_0x98
        type: u4
      - id: ptr_arr_genesys__gen__vehicle_info__extra_axle_0x9c
        type: u4
      - id: array_count_for_0x98
        type: u2
      - id: array_count_for_0x9c
        type: u2
      - id: bool8_t_0xa4
        type: u1
      - id: bool8_t_0xa5
        type: u1
      - id: bool8_t_0xa6
        type: u1
      - id: padding
        size: 1
    instances:
      inst_genesys__gen__vehicle_info__axle_0x98:
        pos: ptr_arr_genesys__gen__vehicle_info__axle_0x98
        type: genesys__gen__vehicle_info__axle
        repeat: expr
        repeat-expr: array_count_for_0x98
      inst_genesys__gen__vehicle_info__extra_axle_0x9c:
        pos: ptr_arr_genesys__gen__vehicle_info__extra_axle_0x9c
        type: genesys__gen__vehicle_info__extra_axle
        repeat: expr
        repeat-expr: array_count_for_0x9c
      size:
        value: 168
      mu_version_hash:
        value: 0xeb_bc_65_68
  genesys__gen__vehicles__upgrade_base:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: icon_0x10
        type: u4
      - id: name_0x14
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x35_09_ba_49
  genesys__gen__vehicles__performance_upgrades:
    seq:
      - id: base_object
        type: gen_obj
      - id: pro_0xc
        type: genesys__gen__vehicles__performance_upgrades__category
      - id: standard_0x60
        type: genesys__gen__vehicles__performance_upgrades__category
      - id: game_changer_id_0xb4
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0xb8
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0xbc
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0xc0
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0xc4
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0xc8
        type: u4
    instances:
      inst_genesys__gen__vehicles__upgrade_base_0xb8:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0xb8
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0xbc:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0xbc
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0xc0:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0xc0
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0xc4:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0xc4
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0xc8:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0xc8
        type: genesys__gen__vehicles__upgrade_base
      size:
        value: 208
      mu_version_hash:
        value: 0x27_84_3e_3f
  genesys__gen__vehicles__performance_upgrades__category:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x10
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x14
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x18
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x1c
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x20
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x24
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x28
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x2c
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x30
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x34
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x38
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x3c
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x40
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x44
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x48
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x4c
        type: u4
      - id: ptr_genesys__gen__vehicles__upgrade_base_0x50
        type: u4
    instances:
      inst_genesys__gen__vehicles__upgrade_base_0x10:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x10
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x14:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x14
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x18:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x18
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x1c:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x1c
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x20:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x20
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x24:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x24
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x28:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x28
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x2c:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x2c
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x30:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x30
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x34:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x34
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x38:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x38
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x3c:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x3c
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x40:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x40
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x44:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x44
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x48:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x48
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x4c:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x4c
        type: genesys__gen__vehicles__upgrade_base
      inst_genesys__gen__vehicles__upgrade_base_0x50:
        pos: ptr_genesys__gen__vehicles__upgrade_base_0x50
        type: genesys__gen__vehicles__upgrade_base
      size:
        value: 88
      mu_version_hash:
        value: 0x84_f7_48_25
  genesys__gen__vehicle_paint:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector4_0x10
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x20
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x30
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x40
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x50
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x60
        type: rw_math_vpu__vector4
      - id: cgs_core__unique_id_0x70
        type: u4
      - id: game_changer_id_0x74
        type: u4
      - id: name_0x78
        type: u4
      - id: float32_t_0x7c
        type: f4
      - id: float32_t_0x80
        type: f4
      - id: float32_t_0x84
        type: f4
      - id: float32_t_0x88
        type: f4
      - id: float32_t_0x8c
        type: f4
      - id: float32_t_0x90
        type: f4
      - id: float32_t_0x94
        type: f4
      - id: float32_t_0x98
        type: f4
      - id: unk_enum_0x9c
        type: u2
        doc: enum; f6_31_00_00
      - id: type_0x9e
        type: u2
        doc: enum; f0_31_00_00
      - id: bool8_t_0xa0
        type: u1
      - id: bool8_t_0xa1
        type: u1
      - id: padding
        size: 2
    instances:
      size:
        value: 164
      mu_version_hash:
        value: 0x27_e6_c8_ac
  genesys__gen__vehicles__tyre_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__vehicles__upgrade_base
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xa5_fd_f5_ad
  genesys__gen__engine__reverse_whine:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0xde_2c_b2_60
  genesys__gen__vehicle_vfx_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: ptr_arr_coronas_0x1c
        type: u4
      - id: ptr_arr_lights_0x20
        type: u4
      - id: ptr_arr_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24
        type: u4
      - id: array_count_for_0x1c
        type: u2
        doc: '"CoronasCount"'
      - id: array_count_for_0x20
        type: u2
        doc: '"LightsCount"'
      - id: array_count_for_0x24
        type: u2
      - id: padding
        size: 2
    instances:
      inst_coronas_0x1c:
        pos: ptr_arr_coronas_0x1c
        type: genesys__gen__vehicle_vfx_behaviour__corona
        repeat: expr
        repeat-expr: array_count_for_0x1c
      inst_lights_0x20:
        pos: ptr_arr_lights_0x20
        type: genesys__gen__vehicle_vfx_behaviour__light
        repeat: expr
        repeat-expr: array_count_for_0x20
      inst_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24:
        pos: ptr_arr_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24
        type: genesys__gen__vehicle_vfx_behaviour__spot_effect
        repeat: expr
        repeat-expr: array_count_for_0x24
      size:
        value: 48
      mu_version_hash:
        value: 0xc4_d0_8e_8d
  genesys__gen__engine__mixer__channel__gain__modification:
    seq:
      - id: base_object
        type: gen_obj
      - id: mixer__channel_0xc
        size: 8
      - id: gain_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x8c_c5_f9_3b
  genesys__gen__engine__mix:
    seq:
      - id: base_object
        type: gen_obj
      - id: float32_t_0xc
        type: f4
      - id: float32_t_0x10
        type: f4
      - id: engine_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: pops_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0x71_55_0f_54
  genesys__gen__control_mesh:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector2_0x10
        type: rw_math_vpu__vector2
      - id: rw_math_vpu__vector3_0x20
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x30
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector4_0x40
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x50
        type: rw_math_vpu__vector4
      - id: game_changer_id_0x60
        type: u4
    instances:
      size:
        value: 104
      mu_version_hash:
        value: 0x76_07_7e_51
  genesys__gen__vehicles__vehicle_category_info:
    seq:
      - id: base_object
        type: gen_obj
      - id: description_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: name_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x00_0b_99_13
  genesys__gen__band_pass_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
      - id: frequency_0x18
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xe2_28_a5_39
  genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0x0c_8b_da_7d
  genesys__gen__wheel_damage:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0x95_43_43_fd
  genesys__gen__ginsu_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x0d_ca_11_27
  genesys__gen__low_pass_butterworth_dsp_plug_in:
    seq:
      - id: base_object
        type: genesys__gen__dsp_plug_in
      - id: order_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xee_6e_71_b1
  genesys__gen__vehicle__gameplay__damage_stats:
    seq:
      - id: base_object
        type: gen_obj
      - id: uint16_t_0xc
        type: u2
      - id: uint16_t_0xe
        type: u2
      - id: uint16_t_0x10
        type: u2
      - id: uint16_t_0x12
        type: u2
      - id: uint16_t_0x14
        type: u2
      - id: uint16_t_0x16
        type: u2
      - id: strength_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x16_36_fd_42
  genesys__gen__wheel_sizes:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x8a_58_4e_a2
  genesys__gen__timeline_controllers__race_car_entity_timeline_controller:
    seq:
      - id: base_object
        type: genesys__gen__sequence_timeline_controller
      - id: unk_enum_0x1c
        type: u4
        doc: enum; d9_65_15_00
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x0f_ec_e6_a9
  genesys__gen__handbrake_ability__handbrake_grip_values:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0x53_ed_c3_28
  genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xb4_bd_b3_92
  genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params_0xc
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x3c
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x64
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params
      - id: game_changer_id_0x8c
        type: u4
    instances:
      size:
        value: 148
      mu_version_hash:
        value: 0xd2_6b_77_23
  genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params_0xc
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x3c
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x64
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params
      - id: game_changer_id_0x8c
        type: u4
    instances:
      size:
        value: 148
      mu_version_hash:
        value: 0x66_08_56_1f
  genesys__gen__tyre_vfx_behaviour__front_rear_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params_0xc
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params_0x9c
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params
      - id: game_changer_id_0x12c
        type: u4
    instances:
      size:
        value: 308
      mu_version_hash:
        value: 0x28_a7_81_2a
  genesys__gen__tyre_vfx_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params_0xc
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params
      - id: genesys__gen__tyre_vfx_behaviour__front_rear_params_0x13c
        type: genesys__gen__tyre_vfx_behaviour__front_rear_params
      - id: game_changer_id_0x26c
        type: u4
    instances:
      size:
        value: 628
      mu_version_hash:
        value: 0xf2_d7_7d_83
  genesys__gen__vehicles__sound__transmission_whine:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_sequences_0x10
        type: u4
      - id: array_count_for_0x10
        type: u1
        doc: '"SequencesCount"'
      - id: padding
        size: 3
    instances:
      inst_sequences_0x10:
        pos: ptr_arr_sequences_0x10
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x24_e3_36_a6
  genesys__gen__tyre_vfx_behaviour__long_lat_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x55_f8_05_97
  genesys__gen__tyre_vfx_behaviour__smoke_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__tyre_vfx_behaviour__long_lat_params_0xc
        type: genesys__gen__tyre_vfx_behaviour__long_lat_params
      - id: genesys__gen__tyre_vfx_behaviour__long_lat_params_0x30
        type: genesys__gen__tyre_vfx_behaviour__long_lat_params
      - id: game_changer_id_0x54
        type: u4
    instances:
      size:
        value: 92
      mu_version_hash:
        value: 0xd9_24_92_fb
  genesys__gen__tyre_vfx_behaviour__skid_mark_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__tyre_vfx_behaviour__long_lat_params_0xc
        type: genesys__gen__tyre_vfx_behaviour__long_lat_params
      - id: genesys__gen__tyre_vfx_behaviour__long_lat_params_0x30
        type: genesys__gen__tyre_vfx_behaviour__long_lat_params
      - id: game_changer_id_0x54
        type: u4
    instances:
      size:
        value: 92
      mu_version_hash:
        value: 0xf7_e9_b7_09
  genesys__gen__vehicles__modifier_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__vehicles__upgrade_base
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xf5_6b_04_27
  genesys__gen__vehicles__nitrous_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__vehicles__upgrade_base
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x3a_6b_3d_40
  genesys__gen__lfo_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: unit_0x28
        type: u2
        doc: enum; 32_67_0d_00
      - id: automated__values_count_0x2a
        type: u2
    instances:
      size:
        value: 48
      mu_version_hash:
        value: 0x93_79_b7_14
  genesys__gen__lfo_sequence_item__lfo_double_value:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_value_0xc
        type: u4
      - id: automated__property_0x10
        type: u4
        doc: enum; f7_34_07_00
    instances:
      inst_value_0xc:
        pos: ptr_value_0xc
        type: genesys__gen__sequence_item__modulating_double_value
      size:
        value: 24
      mu_version_hash:
        value: 0xf4_35_c7_65
  genesys__gen__vehicle__gameplay__tyre_trails:
    seq:
      - id: base_object
        type: gen_obj
      - id: unk_enum_0xc
        type: u2
        doc: enum; f4_5f_0f_00
      - id: stock_0xe
        type: u2
        doc: enum; f4_5f_0f_00
      - id: track_0x10
        type: u4
        doc: enum; f4_5f_0f_00
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xf4_65_85_a8
  genesys__gen__vehicle__gameplay:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__vehicle__gameplay__damage_stats_0xc
        type: genesys__gen__vehicle__gameplay__damage_stats
      - id: genesys__gen__vehicle__gameplay__damage_stats_0x28
        type: genesys__gen__vehicle__gameplay__damage_stats
      - id: id_0nkx_0x44
        type: genesys__gen__vehicle__gameplay__damage_stats
      - id: genesys__gen__vehicle__gameplay__tyre_trails_0x60
        type: genesys__gen__vehicle__gameplay__tyre_trails
      - id: cgs_resource__handle_0x74
        size: 8
      - id: cgs_resource__handle_0x7c
        size: 8
      - id: cgs_resource__handle_0x84
        size: 8
      - id: cgs_core__unique_id_0x8c
        type: u4
      - id: game_changer_id_0x90
        type: u4
      - id: cgs_core__unique_id_0x94
        type: u4
      - id: cgs_core__unique_id_0x98
        type: u4
      - id: cgs_core__unique_id_0x9c
        type: u4
      - id: cgs_core__unique_id_0xa0
        type: u4
      - id: cgs_core__unique_id_0xa4
        type: u4
      - id: cgs_core__unique_id_0xa8
        type: u4
      - id: float32_t_0xac
        type: f4
      - id: ptr_genesys__gen__pidcontroller_0xb0
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb4
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb8
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xbc
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc0
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc4
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc8
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xcc
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd0
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd4
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd8
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xdc
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe0
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe4
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe8
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xec
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf0
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf4
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf8
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xfc
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x100
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x104
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x108
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x10c
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x110
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x114
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x118
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x11c
        type: u4
      - id: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x120
        type: u4
      - id: array_count_for_0xb4
        type: u1
      - id: array_count_for_0xb8
        type: u1
      - id: array_count_for_0xbc
        type: u1
      - id: array_count_for_0xc0
        type: u1
      - id: array_count_for_0xc4
        type: u1
      - id: array_count_for_0xc8
        type: u1
      - id: array_count_for_0xcc
        type: u1
      - id: array_count_for_0xd0
        type: u1
      - id: array_count_for_0xd4
        type: u1
      - id: array_count_for_0xd8
        type: u1
      - id: array_count_for_0xdc
        type: u1
      - id: array_count_for_0xe0
        type: u1
      - id: array_count_for_0xe4
        type: u1
      - id: array_count_for_0xe8
        type: u1
      - id: array_count_for_0xec
        type: u1
      - id: array_count_for_0xf0
        type: u1
      - id: array_count_for_0xf4
        type: u1
      - id: array_count_for_0xf8
        type: u1
      - id: array_count_for_0xfc
        type: u1
      - id: array_count_for_0x100
        type: u1
      - id: array_count_for_0x104
        type: u1
      - id: array_count_for_0x108
        type: u1
      - id: array_count_for_0x10c
        type: u1
      - id: array_count_for_0x110
        type: u1
      - id: array_count_for_0x114
        type: u1
      - id: array_count_for_0x118
        type: u1
      - id: array_count_for_0x11c
        type: u1
      - id: array_count_for_0x120
        type: u1
      - id: uint8_t_0x140
        type: u1
      - id: padding
        size: 3
    instances:
      inst_genesys__gen__pidcontroller_0xb0:
        pos: ptr_genesys__gen__pidcontroller_0xb0
        type: genesys__gen__pidcontroller
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xb4:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb4
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xb4
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xb8:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb8
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xb8
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xbc:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xbc
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xbc
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xc0:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc0
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xc0
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xc4:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc4
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xc4
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xc8:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc8
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xc8
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xcc:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xcc
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xcc
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xd0:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd0
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xd0
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xd4:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd4
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xd4
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xd8:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd8
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xd8
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xdc:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xdc
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xdc
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xe0:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe0
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xe0
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xe4:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe4
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xe4
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xe8:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe8
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xe8
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xec:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xec
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xec
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xf0:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf0
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xf0
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xf4:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf4
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xf4
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xf8:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf8
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xf8
      inst_genesys__gen__vehicle__gameplay__mod_effect_0xfc:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xfc
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0xfc
      inst_genesys__gen__vehicle__gameplay__mod_effect_0x100:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x100
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0x100
      inst_genesys__gen__vehicle__gameplay__mod_effect_0x104:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x104
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0x104
      inst_genesys__gen__vehicle__gameplay__mod_effect_0x108:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x108
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0x108
      inst_genesys__gen__vehicle__gameplay__mod_effect_0x10c:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x10c
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0x10c
      inst_genesys__gen__vehicle__gameplay__mod_effect_0x110:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x110
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0x110
      inst_genesys__gen__vehicle__gameplay__mod_effect_0x114:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x114
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0x114
      inst_genesys__gen__vehicle__gameplay__mod_effect_0x118:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x118
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0x118
      inst_genesys__gen__vehicle__gameplay__mod_effect_0x11c:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x11c
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0x11c
      inst_genesys__gen__vehicle__gameplay__mod_effect_0x120:
        pos: ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x120
        type: genesys__gen__vehicle__gameplay__mod_effect
        repeat: expr
        repeat-expr: array_count_for_0x120
      size:
        value: 324
      mu_version_hash:
        value: 0x1f_07_17_67
  genesys__gen__online__driving_test_list:
    seq:
      - id: base_object
        type: gen_obj
      - id: description_0xc
        type: u4
      - id: ptr_arr_driving_tests_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: name_0x18
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_driving_tests_0x10:
        pos: ptr_arr_driving_tests_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 32
      mu_version_hash:
        value: 0x68_a3_6b_fe
  genesys__gen__online__driving_test_list_group:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: name_0x14
        type: u4
      - id: ptr_arr_ptr_driving_test_list_0x18
        type: u4
      - id: array_count_for_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      inst_driving_test_list_0x18:
        pos: ptr_arr_ptr_driving_test_list_0x18
        type: ptr('genesys__gen__online__driving_test_list')
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 32
      mu_version_hash:
        value: 0xf9_51_68_6b
  genesys__gen__gameplay__offline_upgrade:
    seq:
      - id: base_object
        type: gen_obj
      - id: apply_sequence_0xc
        type: u4
      - id: description_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: image_0x18
        type: u4
      - id: milestone_required_0x1c
        type: u4
      - id: name_0x20
        type: u4
      - id: short_name_0x24
        type: u4
      - id: category_0x28
        type: u2
        doc: enum; e3_31_0f_00
      - id: type_0x2a
        type: u2
        doc: enum; d7_31_0f_00
    instances:
      size:
        value: 48
      mu_version_hash:
        value: 0x06_b8_ea_f5
  genesys__gen__nucleus_grant_mappings_list__mapping:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: nucleus_tag_0x10
        type: u4
      - id: ptr_arr_entitlement_0x14
        type: u4
      - id: array_count_for_0x14
        type: u2
      - id: padding
        size: 2
    instances:
      inst_entitlement_0x14:
        pos: ptr_arr_entitlement_0x14
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 28
      mu_version_hash:
        value: 0xfe_1c_ee_ea
  genesys__gen__online__driving_test_list_groups:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_ptr_driving_test_list_groups_0x10
        type: u4
      - id: array_count_for_0x10
        type: u1
      - id: padding
        size: 3
    instances:
      inst_driving_test_list_groups_0x10:
        pos: ptr_arr_ptr_driving_test_list_groups_0x10
        type: ptr('genesys__gen__online__driving_test_list_group')
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xfc_d7_ca_e6
  genesys__gen__heat_level:
    seq:
      - id: base_object
        type: gen_obj
      - id: coordination_0xc
        type: genesys__gen__heat_level__behaviour_coordination
      - id: cgs_core__unique_id_0x6c
        type: u4
      - id: game_changer_id_0x70
        type: u4
      - id: helicopter_0x74
        type: u4
      - id: aim_for_payload_time_0x78
        type: f4
      - id: float32_t_0x7c
        type: f4
      - id: float32_t_0x80
        type: f4
      - id: float32_t_0x84
        type: f4
      - id: float32_t_0x88
        type: f4
      - id: float32_t_0x8c
        type: f4
      - id: cop_hearing_range_for_idle_player_0x90
        type: f4
      - id: cop_hearing_range_for_moving_player_0x94
        type: f4
      - id: cop_sight_cone_angle_when_alert_0x98
        type: f4
      - id: cop_sight_cone_angle_when_idle_0x9c
        type: f4
      - id: cop_sight_range_when_alert_0xa0
        type: f4
      - id: cop_sight_range_when_chasing_0xa4
        type: f4
      - id: cop_sight_range_when_idle_0xa8
        type: f4
      - id: float32_t_0xac
        type: f4
      - id: float32_t_0xb0
        type: f4
      - id: float32_t_0xb4
        type: f4
      - id: float32_t_0xb8
        type: f4
      - id: float32_t_0xbc
        type: f4
      - id: float32_t_0xc0
        type: f4
      - id: float32_t_0xc4
        type: f4
      - id: float32_t_0xc8
        type: f4
      - id: float32_t_0xcc
        type: f4
      - id: float32_t_0xd0
        type: f4
      - id: float32_t_0xd4
        type: f4
      - id: float32_t_0xd8
        type: f4
      - id: pursuit_radius_0xdc
        type: f4
      - id: search_radius_0xe0
        type: f4
      - id: float32_t_0xe4
        type: f4
      - id: float32_t_0xe8
        type: f4
      - id: unk_enum_0xec
        type: u4
        doc: enum; 83_1d_10_00
      - id: ptr_arr_formation_ahead_0xf0
        type: u4
      - id: ptr_arr_uint8_t_0xf4
        type: u4
      - id: ptr_arr_formation_behind_0xf8
        type: u4
      - id: ptr_arr_uint8_t_0xfc
        type: u4
      - id: int16_t_0x100
        type: s2
      - id: array_count_for_0xec
        type: u2
        doc: '"DirectingReopening"'
      - id: uint16_t_0x104
        type: u2
      - id: array_count_for_0xf0
        type: u2
        doc: '"FormationAheadCount"'
      - id: array_count_for_0xf4
        type: u2
      - id: array_count_for_0xf8
        type: u2
        doc: '"FormationBehindCount"'
      - id: array_count_for_0xfc
        type: u2
      - id: threshold_0x10e
        type: u2
      - id: allow_cooldown_0x110
        type: u1
      - id: bool8_t_0x111
        type: u1
      - id: force_cooldown_0x112
        type: u1
      - id: bool8_t_0x113
        type: u1
      - id: helicopter_permanent_0x114
        type: u1
      - id: aim_for_payload_angle_0x115
        type: u1
      - id: display_number_0x116
        type: u1
      - id: padding
        size: 1
    instances:
      inst_83_1d_10_00_0xec:
        pos: unk_enum_0xec
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0xec
      inst_formation_ahead_0xf0:
        pos: ptr_arr_formation_ahead_0xf0
        type: u1
        repeat: expr
        repeat-expr: array_count_for_0xf0
      inst_uint8_t_0xf4:
        pos: ptr_arr_uint8_t_0xf4
        type: u1
        repeat: expr
        repeat-expr: array_count_for_0xf4
      inst_formation_behind_0xf8:
        pos: ptr_arr_formation_behind_0xf8
        type: u1
        repeat: expr
        repeat-expr: array_count_for_0xf8
      inst_uint8_t_0xfc:
        pos: ptr_arr_uint8_t_0xfc
        type: u1
        repeat: expr
        repeat-expr: array_count_for_0xfc
      size:
        value: 280
      mu_version_hash:
        value: 0x41_14_5c_97
  genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: cop_behaviour_0x14
        type: u2
        doc: enum; 69_32_11_00
      - id: positioning_0x16
        type: s1
      - id: padding
        size: 1
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x02_1b_2e_66
  genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: roadblock_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c
        type: u4
      - id: array_count_for_0x1c
        type: u2
      - id: spawn_cops_0x22
        type: u1
      - id: middleton_datagram_0x23
        type: u1
    instances:
      inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c:
        pos: ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c
        type: genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 40
      mu_version_hash:
        value: 0x5c_e2_18_46
  genesys__gen__heat_level__behaviour_coordination:
    seq:
      - id: base_object
        type: gen_obj
      - id: genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0xc
        type: genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour
      - id: genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x30
        type: genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour
      - id: float32_t_0x54
        type: f4
      - id: ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58
        type: u4
      - id: array_count_for_0x58
        type: u2
      - id: padding
        size: 2
    instances:
      inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58:
        pos: ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58
        type: genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour
        repeat: expr
        repeat-expr: array_count_for_0x58
      size:
        value: 96
      mu_version_hash:
        value: 0x70_40_a2_8b
  int8_t:
    seq: []
    instances: {}
  genesys__gen__game_pack:
    seq:
      - id: base_object
        type: gen_obj
      - id: name_0xc
        type: string_base
      - id: car_pack_image_0x14
        type: u4
      - id: display_name_0x18
        type: u4
      - id: game_changer_id_0x1c
        type: u4
      - id: cgs_core__unique_id_0x20
        type: u4
      - id: show_pack_on_entitlement_0x24
        type: u4
      - id: release_0x28
        type: u2
        doc: enum; c8_2f_00_00
      - id: display_purchase_0x2a
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x2f_4f_a7_04
  genesys__gen__game_rank:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: rank__image_0x10
        type: u4
      - id: rank__name_0x14
        type: u4
      - id: rank__number_0x18
        type: s4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xbc_4b_89_fb
  genesys__gen__game_unlock:
    seq:
      - id: base_object
        type: gen_obj
      - id: entitlement__required_0xc
        size: 8
      - id: asset__to__unlock_0x14
        type: u4
      - id: associated_asset_0x18
        type: u4
      - id: challenge__target__required_0x1c
        type: u4
      - id: game_changer_id_0x20
        type: u4
      - id: ptr_arr_required_assets_0x24
        type: u4
      - id: sequence_0x28
        type: u4
      - id: text_0x2c
        type: u4
      - id: bounty__required_0x30
        type: s4
      - id: int32_t_0x34
        type: s4
      - id: int32_t_0x38
        type: s4
      - id: int32_t_0x3c
        type: s4
      - id: progression__type_0x40
        type: u2
        doc: enum; 95_6a_96_0c
      - id: unlock_asset_type_0x42
        type: u2
        doc: enum; 8e_4e_49_12
      - id: array_count_for_0x24
        type: u2
      - id: is_enabled_0x46
        type: u1
      - id: is_silent_0x47
        type: u1
      - id: bool8_t_0x48
        type: u1
      - id: padding
        size: 3
    instances:
      inst_required_assets_0x24:
        pos: ptr_arr_required_assets_0x24
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x24
      size:
        value: 76
      mu_version_hash:
        value: 0xd5_95_86_1f
  genesys__gen__game_unlock_list:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_ptr_item_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"ItemCount"'
      - id: padding
        size: 2
    instances:
      inst_item_0x10:
        pos: ptr_arr_ptr_item_0x10
        type: ptr('any_genesys_obj')
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x2c_04_42_9d
  genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control:
    seq:
      - id: base_object
        type: gen_obj
      - id: far_distance_0xc
        type: f4
      - id: near_distance_0x10
        type: f4
      - id: rewarding_highlighting_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x5b_fa_1e_2e
  genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold:
    seq:
      - id: base_object
        type: gen_obj
      - id: damage_value_0xc
        type: f4
      - id: ptr_arr_speed_control_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_speed_control_0x10:
        pos: ptr_arr_speed_control_0x10
        type: genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xde_b9_4e_40
  genesys__gen__road_block_layer__item:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: angle_0x14
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xa7_64_a6_e7
  genesys__gen__gameplay_trigger__input:
    seq:
      - id: base_object
        type: gen_obj
      - id: trigger_0xc
        type: u4
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0x9d_0d_72_73
  genesys__gen__aiplayer_instance:
    seq:
      - id: base_object
        type: gen_obj
      - id: back_up_colour_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: primary_colour_0x14
        type: u4
      - id: type_0x18
        type: u4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xdc_05_24_d5
  genesys__gen__gameplay_trigger__aiplayer_information:
    seq:
      - id: base_object
        type: gen_obj
      - id: placement_0xc
        type: u4
      - id: ptr_aiplayer_instance_0x10
        type: u4
    instances:
      inst_aiplayer_instance_0x10:
        pos: ptr_aiplayer_instance_0x10
        type: genesys__gen__aiplayer_instance
      size:
        value: 24
      mu_version_hash:
        value: 0x4c_f9_0b_22
  genesys__gen__gameplay_trigger__output__sequence_output:
    seq:
      - id: base_object
        type: gen_obj
      - id: sequence_0xc
        type: u4
      - id: sequence_type_0x10
        type: u2
        doc: enum; 77_cc_06_00
      - id: bool8_t_0x12
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0x84_75_5b_d2
  genesys__gen__roadblock_instance:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: placement_0x10
        type: u4
      - id: type_0x14
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x7c_8e_25_02
  genesys__gen__gameplay_trigger__output:
    seq:
      - id: base_object
        type: gen_obj
      - id: predicate_0xc
        type: string_base
      - id: ptr_arr_speech__events_0x14
        type: u4
      - id: ptr_arr_ptr_aiplayers_0x18
        type: u4
      - id: ptr_arr_sequence_0x1c
        type: u4
      - id: ptr_arr_ptr_roadblock_instance_0x20
        type: u4
      - id: array_count_for_0x18
        type: u2
        doc: '"AIPlayersCount"'
      - id: array_count_for_0x1c
        type: u2
        doc: '"SequenceCount"'
      - id: array_count_for_0x20
        type: u1
        doc: '"RoadblockInstanceCount"'
      - id: array_count_for_0x14
        type: u1
        doc: '"Players_An"'
      - id: padding
        size: 2
    instances:
      inst_speech__events_0x14:
        pos: ptr_arr_speech__events_0x14
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_aiplayers_0x18:
        pos: ptr_arr_ptr_aiplayers_0x18
        type: ptr('genesys__gen__gameplay_trigger__aiplayer_information')
        repeat: expr
        repeat-expr: array_count_for_0x18
      inst_sequence_0x1c:
        pos: ptr_arr_sequence_0x1c
        type: genesys__gen__gameplay_trigger__output__sequence_output
        repeat: expr
        repeat-expr: array_count_for_0x1c
      inst_roadblock_instance_0x20:
        pos: ptr_arr_ptr_roadblock_instance_0x20
        type: ptr('genesys__gen__roadblock_instance')
        repeat: expr
        repeat-expr: array_count_for_0x20
      size:
        value: 44
      mu_version_hash:
        value: 0x31_d3_0a_05
  genesys__gen__gameplay_trigger:
    seq:
      - id: base_object
        type: gen_obj
      - id: predicate_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: time_to_wait_0x18
        type: f4
      - id: ptr_arr_input_0x1c
        type: u4
      - id: ptr_arr_output_0x20
        type: u4
      - id: trigger_lifetime_0x24
        type: u2
        doc: enum; 72_cc_06_00
      - id: array_count_for_0x1c
        type: u2
        doc: '"InputCount"'
      - id: array_count_for_0x20
        type: u2
        doc: '"OutputCount"'
      - id: add_to_mini_map_0x2a
        type: u1
      - id: bool8_t_0x2b
        type: u1
      - id: bool8_t_0x2c
        type: u1
      - id: padding
        size: 3
    instances:
      inst_input_0x1c:
        pos: ptr_arr_input_0x1c
        type: genesys__gen__gameplay_trigger__input
        repeat: expr
        repeat-expr: array_count_for_0x1c
      inst_output_0x20:
        pos: ptr_arr_output_0x20
        type: genesys__gen__gameplay_trigger__output
        repeat: expr
        repeat-expr: array_count_for_0x20
      size:
        value: 48
      mu_version_hash:
        value: 0x01_6a_bd_31
  genesys__gen__online_challenge_target:
    seq:
      - id: base_object
        type: gen_obj
      - id: award_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: uint32_t_0x14
        type: u4
      - id: xp_0x18
        type: u2
      - id: padding
        size: 2
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x7b_e0_ac_61
  genesys__gen__online_challenge:
    seq:
      - id: base_object
        type: gen_obj
      - id: description_0xc
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x10
        type: u4
      - id: equipment__vehicle_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: game_changer_id_0x1c
        type: u4
      - id: ptr_arr_game_mode_0x20
        type: u4
      - id: ptr_arr_license_plates_0x24
        type: u4
      - id: manufacturer_0x28
        type: u4
      - id: cgs_core__unique_id_0x2c
        type: u4
      - id: name_0x30
        type: u4
      - id: revenge_bonus_0x34
        type: u4
      - id: att0_0x38
        type: u4
      - id: screen_description_0x3c
        type: u4
      - id: ticket_0x40
        type: u4
      - id: title_0x44
        type: u4
      - id: trigger_0x48
        type: u4
      - id: vehicle_category_0x4c
        type: u4
      - id: cgs_core__unique_id_0x50
        type: u4
      - id: vehicle_nationality_0x54
        type: u4
      - id: cgs_core__unique_id_0x58
        type: u4
      - id: cgs_core__unique_id_0x5c
        type: u4
      - id: ptr_arr_ptr_target_0x60
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: array_count_for_0x20
        type: u2
      - id: array_count_for_0x24
        type: u2
      - id: scope_actions_0x6a
        type: u2
      - id: bool8_t_0x6c
        type: u1
      - id: most_wanted_0x6d
        type: u1
      - id: not_eliminated_0x6e
        type: u1
      - id: not_wrecked_0x6f
        type: u1
      - id: on_rims_0x70
        type: u1
      - id: same_victim_0x71
        type: u1
      - id: bool8_t_0x72
        type: u1
      - id: bool8_t_0x73
        type: u1
      - id: bool8_t_0x74
        type: u1
      - id: unk_enum_0x75
        type: u1
        doc: enum; a8_60_04_00
      - id: action__type_0x76
        type: u1
        doc: enum; 43_5f_04_00
      - id: condition_0x77
        type: u1
        doc: enum; d7_e3_10_00
      - id: unk_enum_0x78
        type: u1
        doc: enum; a7_d8_19_00
      - id: time__period_0x79
        type: u1
        doc: enum; 3e_5f_04_00
      - id: array_count_for_0x60
        type: u1
        doc: '"TargetCount"'
      - id: padding
        size: 1
    instances:
      inst_cgs_core__unique_id_0x10:
        pos: ptr_arr_cgs_core__unique_id_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_game_mode_0x20:
        pos: ptr_arr_game_mode_0x20
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x20
      inst_license_plates_0x24:
        pos: ptr_arr_license_plates_0x24
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x24
      inst_target_0x60:
        pos: ptr_arr_ptr_target_0x60
        type: ptr('genesys__gen__online_challenge_target')
        repeat: expr
        repeat-expr: array_count_for_0x60
      size:
        value: 124
      mu_version_hash:
        value: 0xe0_a1_81_08
  genesys__gen__store_item:
    seq:
      - id: base_object
        type: gen_obj
      - id: name_0xc
        type: string_base
      - id: psnpackage_name_0x14
        type: string_base
      - id: nucleus_ent_tag_0x1c
        size: 8
      - id: game_changer_id_0x24
        type: u4
      - id: ptr_arr_long__description_0x28
        type: u4
      - id: main_image_0x2c
        type: u4
      - id: sub_image1_0x30
        type: u4
      - id: sub_image2_0x34
        type: u4
      - id: title_0x38
        type: u4
      - id: ptr_arr_entitlements_0x3c
        type: u4
      - id: x360license_mask_0x40
        type: u4
      - id: x360offer_id_0x44
        type: u4
      - id: array_count_for_0x28
        type: u2
        doc: '"Long_DescriptionCount"'
      - id: show__in__store_0x4a
        type: u1
      - id: array_count_for_0x3c
        type: u1
        doc: '"EntitlementsCount"'
    instances:
      inst_long__description_0x28:
        pos: ptr_arr_long__description_0x28
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x28
      inst_entitlements_0x3c:
        pos: ptr_arr_entitlements_0x3c
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x3c
      size:
        value: 80
      mu_version_hash:
        value: 0x13_67_e2_c7
  genesys__gen__store_pack:
    seq:
      - id: base_object
        type: gen_obj
      - id: pack_item_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: ptr_arr_content_items_0x18
        type: u4
      - id: array_count_for_0x18
        type: u2
        doc: '"ContentItemsCount"'
      - id: padding
        size: 2
    instances:
      inst_content_items_0x18:
        pos: ptr_arr_content_items_0x18
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 32
      mu_version_hash:
        value: 0xb7_10_a2_08
  genesys__gen__store_pack_list:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_store_packs_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"StorePacksCount"'
      - id: padding
        size: 2
    instances:
      inst_store_packs_0x10:
        pos: ptr_arr_store_packs_0x10
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xd4_f9_60_f2
  genesys__gen__scoring_action__online_scoring_feedback:
    seq:
      - id: base_object
        type: gen_obj
      - id: description_0xc
        type: u4
      - id: sequence_0x10
        type: u4
      - id: cgs_core__unique_id_0x14
        type: u4
      - id: title_0x18
        type: u4
      - id: deferrable_0x1c
        type: u1
      - id: opposing__team_0x1d
        type: u1
      - id: scoring__player_0x1e
        type: u1
      - id: scoring__team_0x1f
        type: u1
      - id: bool8_t_0x20
        type: u1
      - id: victim__player_0x21
        type: u1
      - id: padding
        size: 2
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x6a_32_d4_f4
  genesys__gen__thankyou_mapping:
    seq:
      - id: base_object
        type: gen_obj
      - id: nucleus_entitlement_0xc
        size: 8
      - id: thankyou_item_0x14
        size: 8
      - id: entitlement_0x1c
        type: u4
      - id: game_changer_id_0x20
        type: u4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x1a_e7_17_9a
  genesys__gen__rollout__weapon_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: weapon_0xc
        type: u4
      - id: ptr_arr_weapon_upgrades_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"WeaponUpgradesCount"'
      - id: padding
        size: 2
    instances:
      inst_weapon_upgrades_0x10:
        pos: ptr_arr_weapon_upgrades_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x7a_ff_66_76
  genesys__gen__thank_you_screen_item:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: heading_0x10
        type: u4
      - id: message_0x14
        type: u4
      - id: bounty_reward_0x18
        type: s4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x99_b7_15_31
  genesys__gen__aiplayer_type:
    seq:
      - id: base_object
        type: gen_obj
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
      mu_version_hash:
        value: 0xd2_97_1c_1d
  genesys__gen__uicamera:
    seq:
      - id: base_object
        type: gen_obj
      - id: look_at_0x10
        type: rw_math_vpu__vector3
      - id: position_0x20
        type: rw_math_vpu__vector3
      - id: up_vector_0x30
        type: rw_math_vpu__vector3
      - id: game_changer_id_0x40
        type: u4
      - id: aspect_ratio_0x44
        type: f4
      - id: far_clip_0x48
        type: f4
      - id: field_of_view_0x4c
        type: f4
      - id: near_clip_0x50
        type: f4
      - id: aspect_correct_0x54
        type: u1
      - id: bool8_t_0x55
        type: u1
      - id: bool8_t_0x56
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 88
      mu_version_hash:
        value: 0xfe_41_d4_24
  genesys__gen__car_select_data__sequences:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_sequences_0x10
        type: u4
      - id: time_0x14
        type: s4
      - id: array_count_for_0x10
        type: u2
        doc: '"SequencesCount"'
      - id: padding
        size: 2
    instances:
      inst_sequences_0x10:
        pos: ptr_arr_sequences_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 28
      mu_version_hash:
        value: 0x63_78_a7_1f
  genesys__gen__safehouse:
    seq:
      - id: base_object
        type: gen_obj
      - id: discovery_trigger_0xc
        type: u4
      - id: entry_sequence_0x10
        type: u4
      - id: exit_sequence_0x14
        type: u4
      - id: exit_spawn_location_0x18
        type: u4
      - id: game_changer_id_0x1c
        type: u4
      - id: name_0x20
        type: u4
      - id: placement_0x24
        type: u4
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0xce_cf_4d_c9
  genesys__gen__gameplay__drift_marker:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: cgs_core__unique_id_0x14
        type: u4
      - id: safety_trigger_0x18
        type: u4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x31_cc_82_44
  genesys__gen__rollout:
    seq:
      - id: base_object
        type: gen_obj
      - id: weapon_data_0xc
        type: genesys__gen__rollout__weapon_data
      - id: body_upgrade_0x24
        type: u4
      - id: ptr_arr_characters_0x28
        type: u4
      - id: chassis_upgrade_0x2c
        type: u4
      - id: colour_0x30
        type: u4
      - id: damage_bar_profile_0x34
        type: u4
      - id: game_changer_id_0x38
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x3c
        type: u4
      - id: name_0x40
        type: u4
      - id: nitrous_upgrade_0x44
        type: u4
      - id: ptr_arr_number_plate_0x48
        type: u4
      - id: cgs_core__unique_id_0x4c
        type: u4
      - id: revenge_bonus_0x50
        type: u4
      - id: cgs_core__unique_id_0x54
        type: u4
      - id: vehicle_0x58
        type: u4
      - id: dirt_amount_0x5c
        type: f4
      - id: dust_amount_0x60
        type: f4
      - id: array_count_for_0x28
        type: u2
        doc: '"CharactersCount"'
      - id: array_count_for_0x3c
        type: u2
      - id: array_count_for_0x48
        type: u2
      - id: bool8_t_0x6a
        type: u1
      - id: is_online_rollout_0x6b
        type: u1
      - id: is_player_rollout_0x6c
        type: u1
      - id: padding
        size: 3
    instances:
      inst_characters_0x28:
        pos: ptr_arr_characters_0x28
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x28
      inst_cgs_core__unique_id_0x3c:
        pos: ptr_arr_cgs_core__unique_id_0x3c
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x3c
      inst_number_plate_0x48:
        pos: ptr_arr_number_plate_0x48
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x48
      size:
        value: 112
      mu_version_hash:
        value: 0x6d_7e_04_b3
  genesys__gen__scoring_action:
    seq:
      - id: base_object
        type: gen_obj
      - id: predicate_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: gameplay_trigger_0x18
        type: u4
      - id: sequence_0x1c
        type: u4
      - id: title_0x20
        type: u4
      - id: float32_t_0x24
        type: f4
      - id: ptr_arr_online_feedback_0x28
        type: u4
      - id: ptr_arr_uint32_t_0x2c
        type: u4
      - id: ptr_arr_score_0x30
        type: u4
      - id: ptr_arr_initiates_raids_0x34
        type: u4
      - id: scope_0x38
        type: u2
        doc: enum; b9_b2_17_00
      - id: queue_0x3a
        type: u2
        doc: enum; 93_37_09_00
      - id: array_count_for_0x2c
        type: u2
        doc: '"IntergroupVoiced"'
      - id: array_count_for_0x28
        type: u2
      - id: array_count_for_0x30
        type: u2
        doc: '"ScoreCount"'
      - id: array_count_for_0x34
        type: u2
      - id: bool8_t_0x44
        type: u1
      - id: feedback_deferrable_0x45
        type: u1
      - id: priority_0x46
        type: u1
      - id: padding
        size: 1
    instances:
      inst_online_feedback_0x28:
        pos: ptr_arr_online_feedback_0x28
        type: genesys__gen__scoring_action__online_scoring_feedback
        repeat: expr
        repeat-expr: array_count_for_0x28
      inst_uint32_t_0x2c:
        pos: ptr_arr_uint32_t_0x2c
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x2c
      inst_score_0x30:
        pos: ptr_arr_score_0x30
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x30
      inst_initiates_raids_0x34:
        pos: ptr_arr_initiates_raids_0x34
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x34
      size:
        value: 72
      mu_version_hash:
        value: 0x9c_df_6b_53
  genesys__gen__car_select_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: cop_idle_sequences_0xc
        type: genesys__gen__car_select_data__sequences
      - id: cop_sequences_0x28
        type: genesys__gen__car_select_data__sequences
      - id: racer_idle_sequences_0x44
        type: genesys__gen__car_select_data__sequences
      - id: racer_sequences_0x60
        type: genesys__gen__car_select_data__sequences
      - id: ptr_arr_cop_placements_0x7c
        type: u4
      - id: game_changer_id_0x80
        type: u4
      - id: ptr_arr_racer_placements_0x84
        type: u4
      - id: uimemory_limit_0x88
        type: f4
      - id: uiresource_limit_0x8c
        type: s4
      - id: array_count_for_0x7c
        type: u2
        doc: '"CopPlacementsCount"'
      - id: array_count_for_0x84
        type: u2
        doc: '"RacerPlacementsCount"'
      - id: loop_sequences_0x94
        type: u1
      - id: split_by_tier_0x95
        type: u1
      - id: padding
        size: 2
    instances:
      inst_cop_placements_0x7c:
        pos: ptr_arr_cop_placements_0x7c
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x7c
      inst_racer_placements_0x84:
        pos: ptr_arr_racer_placements_0x84
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x84
      size:
        value: 152
      mu_version_hash:
        value: 0xee_73_7c_02
  genesys__gen__gameplay__milestone__entry:
    seq:
      - id: base_object
        type: gen_obj
      - id: award_0xc
        type: u4
      - id: value_0x10
        type: f4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xae_20_16_93
  genesys__gen__gameplay__milestone:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: name_0x14
        type: u4
      - id: progress_0x18
        type: u4
      - id: ptr_arr_entries_0x1c
        type: u4
      - id: stat_0x20
        type: u2
        doc: enum; d9_f0_0e_00
      - id: array_count_for_0x1c
        type: u2
        doc: '"EntriesCount"'
    instances:
      inst_entries_0x1c:
        pos: ptr_arr_entries_0x1c
        type: genesys__gen__gameplay__milestone__entry
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 40
      mu_version_hash:
        value: 0x4e_bb_d9_43
  genesys__gen__nucleus_entitlement_tag:
    seq:
      - id: base_object
        type: gen_obj
      - id: tag_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x48_46_99_8b
  genesys__gen__nucleus_entitlement_tags:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_nucleus_tag_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"NucleusTagCount"'
      - id: padding
        size: 2
    instances:
      inst_nucleus_tag_0x10:
        pos: ptr_arr_nucleus_tag_0x10
        type: cgs_resource__handle
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xba_a5_64_08
  genesys__gen__nucleus_grant_mappings_list:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_items_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"ItemsCount"'
      - id: padding
        size: 2
    instances:
      inst_items_0x10:
        pos: ptr_arr_items_0x10
        type: genesys__gen__nucleus_grant_mappings_list__mapping
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x3a_26_00_0e
  genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods:
    seq:
      - id: base_object
        type: gen_obj
      - id: vehicle_0xc
        type: u4
      - id: float32_t_0x10
        type: f4
      - id: ptr_arr_mods_0x14
        type: u4
        doc: enum; d7_31_0f_00
      - id: inline_arr_target_scores_0x18
        type: s2
        repeat: expr
        repeat-expr: 3
      - id: inline_arr_target_speeds_0x1e
        type: s2
        repeat: expr
        repeat-expr: 3
      - id: array_count_for_0x14
        type: u2
      - id: array_count_for_0x18
        type: u2
      - id: array_count_for_0x1e
        type: u2
      - id: difficulty_0x2a
        type: u1
      - id: padding
        size: 1
    instances:
      inst_mods_0x14:
        pos: ptr_arr_mods_0x14
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 44
      mu_version_hash:
        value: 0x39_07_3e_a4
  genesys__gen__paint_pack:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: image_0x18
        type: u4
      - id: livery_0x1c
        type: u4
      - id: name_0x20
        type: u4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x31_9a_5f_9c
  genesys__gen__paint_pack_group:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_ptr_paint_packs_0x10
        type: u4
      - id: array_count_for_0x10
        type: u1
      - id: padding
        size: 3
    instances:
      inst_paint_packs_0x10:
        pos: ptr_arr_ptr_paint_packs_0x10
        type: ptr('genesys__gen__paint_pack')
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x72_08_5b_1b
  genesys__gen__car_swap_spot:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: colour_id_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: parking_placement_0x1c
        type: u4
      - id: placement_0x20
        type: u4
      - id: vehicle_id_0x24
        type: u4
      - id: vehicle_placement_0x28
        type: u4
    instances:
      size:
        value: 48
      mu_version_hash:
        value: 0x60_0c_5f_24
  genesys__gen__online__license_plate:
    seq:
      - id: base_object
        type: gen_obj
      - id: backing_image_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: name_0x14
        type: u4
      - id: release_0x18
        type: u4
      - id: bool8_t_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x41_ef_27_eb
  genesys__gen__entitlement:
    seq:
      - id: base_object
        type: gen_obj
      - id: description_0xc
        type: string_base
      - id: entitlement_tag_0x14
        type: string_base
      - id: name_0x1c
        type: string_base
      - id: game_changer_id_0x24
        type: u4
      - id: purchasable_0x28
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x98_9c_04_d1
  genesys__gen__gameplay__revenge_bonus:
    seq:
      - id: base_object
        type: gen_obj
      - id: bonus_score_0xc
        type: u4
      - id: description_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: icon_0x18
        type: u4
      - id: name_0x1c
        type: u4
      - id: duration_0x20
        type: f4
      - id: ptr_arr_ptr_genesys__gen__nitrous_parameters_0x24
        type: u4
      - id: ptr_arr_ptr_genesys__gen__performance_modifier_0x28
        type: u4
      - id: ptr_arr_feature_0x2c
        type: u4
        doc: enum; e2_b2_17_00
      - id: array_count_for_0x2c
        type: u2
        doc: '"FeatureCount"'
      - id: bool8_t_0x32
        type: u1
      - id: array_count_for_0x24
        type: u1
        doc: '"LyonOffset"'
      - id: array_count_for_0x28
        type: u1
      - id: wrecks_count_0x35
        type: u1
      - id: padding
        size: 2
    instances:
      inst_genesys__gen__nitrous_parameters_0x24:
        pos: ptr_arr_ptr_genesys__gen__nitrous_parameters_0x24
        type: ptr('genesys__gen__nitrous_parameters')
        repeat: expr
        repeat-expr: array_count_for_0x24
      inst_genesys__gen__performance_modifier_0x28:
        pos: ptr_arr_ptr_genesys__gen__performance_modifier_0x28
        type: ptr('genesys__gen__performance_modifier')
        repeat: expr
        repeat-expr: array_count_for_0x28
      inst_feature_0x2c:
        pos: ptr_arr_feature_0x2c
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x2c
      size:
        value: 56
      mu_version_hash:
        value: 0x65_c6_8f_55
  genesys__gen__event_list:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_ordered_list_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"OrderedListCount"'
      - id: padding
        size: 2
    instances:
      inst_ordered_list_0x10:
        pos: ptr_arr_ordered_list_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x3a_7e_79_74
  genesys__gen__event_location:
    seq:
      - id: base_object
        type: gen_obj
      - id: inline_arr_position_0xc
        type: f4
        repeat: expr
        repeat-expr: 3
      - id: event_list_0x18
        size: 8
      - id: main_map_camera_0x20
        size: 8
      - id: zoomed_map_camera_0x28
        size: 8
      - id: freedrive_event_0x30
        type: u4
      - id: game_changer_id_0x34
        type: u4
      - id: name_0x38
        type: u4
      - id: original_game_pack_0x3c
        type: u4
      - id: array_count_for_0xc
        type: u2
        doc: '"PositionCount"'
      - id: is_cop_location_0x42
        type: u1
      - id: is_online_0x43
        type: u1
    instances:
      size:
        value: 72
      mu_version_hash:
        value: 0xe9_6b_72_79
  genesys__gen__road_block_definition:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_arr_back_layers_0xc
        type: u4
      - id: ptr_arr_front_layers_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x18
        type: u4
      - id: primary_layer_0x1c
        type: u4
      - id: sequence_0x20
        type: u4
      - id: layer_distance_0x24
        type: f4
      - id: array_count_for_0xc
        type: u2
        doc: '"BackLayersCount"'
      - id: array_count_for_0x10
        type: u2
        doc: '"FrontLayersCount"'
      - id: array_count_for_0x18
        type: u2
      - id: padding
        size: 2
    instances:
      inst_back_layers_0xc:
        pos: ptr_arr_back_layers_0xc
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0xc
      inst_front_layers_0x10:
        pos: ptr_arr_front_layers_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_cgs_core__unique_id_0x18:
        pos: ptr_arr_cgs_core__unique_id_0x18
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 48
      mu_version_hash:
        value: 0x94_58_ff_cf
  genesys__gen__road_block_layer:
    seq:
      - id: base_object
        type: gen_obj
      - id: middle_item_0xc
        type: genesys__gen__road_block_layer__item
      - id: game_changer_id_0x24
        type: u4
      - id: distance_0x28
        type: f4
      - id: first_distance_0x2c
        type: f4
      - id: ptr_arr_left_items_0x30
        type: u4
      - id: ptr_arr_right_items_0x34
        type: u4
      - id: array_count_for_0x30
        type: u2
      - id: array_count_for_0x34
        type: u2
    instances:
      inst_left_items_0x30:
        pos: ptr_arr_left_items_0x30
        type: genesys__gen__road_block_layer__item
        repeat: expr
        repeat-expr: array_count_for_0x30
      inst_right_items_0x34:
        pos: ptr_arr_right_items_0x34
        type: genesys__gen__road_block_layer__item
        repeat: expr
        repeat-expr: array_count_for_0x34
      size:
        value: 64
      mu_version_hash:
        value: 0x65_03_e6_7a
  genesys__gen__gameplay__blacklist_shutdown_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: cloud_compete_award_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: cgs_core__unique_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: name_0x1c
        type: u4
      - id: ptr_aiplayer_instance_0x20
        type: u4
      - id: ptr_arr_damage_thresholds_0x24
        type: u4
      - id: array_count_for_0x24
        type: u2
      - id: blacklist_number_0x2a
        type: u1
      - id: padding
        size: 1
    instances:
      inst_aiplayer_instance_0x20:
        pos: ptr_aiplayer_instance_0x20
        type: genesys__gen__aiplayer_instance
      inst_damage_thresholds_0x24:
        pos: ptr_arr_damage_thresholds_0x24
        type: genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold
        repeat: expr
        repeat-expr: array_count_for_0x24
      size:
        value: 44
      mu_version_hash:
        value: 0x86_d7_15_26
  genesys__gen__gameplay__allowed_vehicle_list:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"PersonalizationBooster"'
      - id: padding
        size: 2
    instances:
      inst_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10:
        pos: ptr_arr_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10
        type: genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xed_fc_c0_52
  genesys__gen__gameplay__cop_type:
    seq:
      - id: base_object
        type: gen_obj
      - id: aiplayer_type_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: bool8_t_0x14
        type: u1
      - id: can_spawn_behind_0x15
        type: u1
      - id: can_spawn_head_on_0x16
        type: u1
      - id: can_spawn_intercepting_0x17
        type: u1
      - id: bool8_t_0x18
        type: u1
      - id: bool8_t_0x19
        type: u1
      - id: padding
        size: 2
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x68_d5_c1_d3
  genesys__gen__cloud_compete_award:
    seq:
      - id: base_object
        type: gen_obj
      - id: description_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: title_0x14
        type: u4
      - id: unlock_string_0x18
        type: u4
      - id: category_0x1c
        type: u2
        doc: enum; 86_f4_0e_00
      - id: action_destination_0x1e
        type: u2
        doc: enum; 76_f5_0e_00
      - id: uint16_t_0x20
        type: u2
      - id: bool8_t_0x22
        type: u1
      - id: uint8_t_0x23
        type: u1
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xee_33_86_8e
  genesys_obj_collection:
    seq:
      - id: base_object
        type: gen_obj
      - id: unk_id
        type: u4
      - id: collection_start_offset
        type: u4
      - id: collection_count
        type: u4
    instances:
      obj_collection:
        pos: collection_start_offset
        type: ptr('any_genesys_obj')
        repeat: expr
        repeat-expr: collection_count


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
            '"cgs_core__string_base"': cgs_core__string_base
            '"char"': char
            '"uint32_t"': uint32_t
            '"cgs_core__unique_id"': cgs_core__unique_id
            '"genesys__gen__challenge_action__accumulation_helper_data"': genesys__gen__challenge_action__accumulation_helper_data
            '"genesys__gen__challenge_action__action_base"': genesys__gen__challenge_action__action_base
            '"genesys__gen__challenge_action__accumulate_takedowns"': genesys__gen__challenge_action__accumulate_takedowns
            '"genesys__gen__challenge_action__action_base__feedback_data"': genesys__gen__challenge_action__action_base__feedback_data
            '"bool8_t"': bool8_t
            '"uint8_t"': uint8_t
            '"genesys__gen__online_route"': genesys__gen__online_route
            '"uint16_t"': uint16_t
            '"genesys__gen__race_balancing_data__opponent_balancing_data"': genesys__gen__race_balancing_data__opponent_balancing_data
            '"float32_t"': float32_t
            '"genesys__gen__event_arena_data__spawn_point_collection"': genesys__gen__event_arena_data__spawn_point_collection
            '"int16_t"': int16_t
            '"genesys__gen__chevron"': genesys__gen__chevron
            '"genesys__gen__challenge__location"': genesys__gen__challenge__location
            '"genesys__gen__challenge_action__speed_camera_action"': genesys__gen__challenge_action__speed_camera_action
            '"genesys__gen__game_mode"': genesys__gen__game_mode
            '"genesys__gen__custom_chevron"': genesys__gen__custom_chevron
            '"genesys__gen__event"': genesys__gen__event
            '"genesys__gen__online_event"': genesys__gen__online_event
            '"genesys__gen__event_arena_data"': genesys__gen__event_arena_data
            '"genesys__gen__event_arena"': genesys__gen__event_arena
            '"genesys__gen__challenge_action__jump_stats"': genesys__gen__challenge_action__jump_stats
            '"int32_t"': int32_t
            '"genesys__gen__offline_event__alternate_routes"': genesys__gen__offline_event__alternate_routes
            '"string_base"': string_base
            '"genesys__gen__gameplay__condition"': genesys__gen__gameplay__condition
            '"genesys__gen__score_view_model__score"': genesys__gen__score_view_model__score
            '"genesys__gen__score_view_model"': genesys__gen__score_view_model
            '"genesys__gen__score_view_model__score_data"': genesys__gen__score_view_model__score_data
            '"genesys__gen__challenge_action__accumulate_near_misses"': genesys__gen__challenge_action__accumulate_near_misses
            '"genesys__gen__event__checkpoint_info"': genesys__gen__event__checkpoint_info
            '"cgs_resource__handle"': cgs_resource__handle
            '"genesys__gen__offline_event__aiplayer_information"': genesys__gen__offline_event__aiplayer_information
            '"genesys__gen__offline_event__custom_chevrons"': genesys__gen__offline_event__custom_chevrons
            '"genesys__gen__challenge_action__coop_accumulate_distance"': genesys__gen__challenge_action__coop_accumulate_distance
            '"genesys__gen__challenge_action__car_state"': genesys__gen__challenge_action__car_state
            '"genesys__gen__challenge_action__accumulate_time"': genesys__gen__challenge_action__accumulate_time
            '"genesys__gen__challenge_action__accumulate_distance"': genesys__gen__challenge_action__accumulate_distance
            '"genesys__gen__offline_event__checkpoint_info"': genesys__gen__offline_event__checkpoint_info
            '"genesys__gen__online__vote_event"': genesys__gen__online__vote_event
            '"genesys__gen__challenge__challenge_part"': genesys__gen__challenge__challenge_part
            '"genesys__gen__challenge__online_challenge"': genesys__gen__challenge__online_challenge
            '"genesys__gen__challenge_action__get_to_location"': genesys__gen__challenge_action__get_to_location
            '"genesys__gen__race_balancing_data"': genesys__gen__race_balancing_data
            '"genesys__gen__challenge_action__jump_over_players"': genesys__gen__challenge_action__jump_over_players
            '"genesys__gen__race_balancing_profile"': genesys__gen__race_balancing_profile
            '"genesys__gen__challenge_action__do_jump"': genesys__gen__challenge_action__do_jump
            '"genesys__gen__challenge_action__hit_trigger"': genesys__gen__challenge_action__hit_trigger
            '"genesys__object"': genesys__object
            '"genesys__gen__offline_event"': genesys__gen__offline_event
            '"gen_obj"': gen_obj
            '"genesys__gen__challenge_action__speed_run"': genesys__gen__challenge_action__speed_run
            '"rw_math_vpu__vector4"': rw_math_vpu__vector4
            '"genesys__gen__behaviour"': genesys__gen__behaviour
            '"genesys__gen__wcremove_world_entity_behaviour"': genesys__gen__wcremove_world_entity_behaviour
            '"genesys__gen__corona__glow"': genesys__gen__corona__glow
            '"genesys__gen__wcvfx_behaviour__coronas"': genesys__gen__wcvfx_behaviour__coronas
            '"genesys__gen__corona__beam"': genesys__gen__corona__beam
            '"genesys__gen__wcvfx_behaviour__spot_effects"': genesys__gen__wcvfx_behaviour__spot_effects
            '"genesys__gen__corona__flare"': genesys__gen__corona__flare
            '"genesys__gen__wcvfx_behaviour__lights"': genesys__gen__wcvfx_behaviour__lights
            '"genesys__gen__wcplay_sound_behaviour__prop_surface_sound"': genesys__gen__wcplay_sound_behaviour__prop_surface_sound
            '"genesys__gen__physical_definition__rigid_body__box_volume"': genesys__gen__physical_definition__rigid_body__box_volume
            '"genesys__gen__physical_definition__rigid_body__capsule_volume"': genesys__gen__physical_definition__rigid_body__capsule_volume
            '"genesys__gen__physical_definition__rigid_body__convex_hull_volume"': genesys__gen__physical_definition__rigid_body__convex_hull_volume
            '"genesys__gen__physical_definition__rigid_body__cylinder_volume"': genesys__gen__physical_definition__rigid_body__cylinder_volume
            '"genesys__gen__physical_definition__rigid_body__sphere_volume"': genesys__gen__physical_definition__rigid_body__sphere_volume
            '"genesys__gen__physical_definition__rigid_body"': genesys__gen__physical_definition__rigid_body
            '"genesys__gen__physical_definition"': genesys__gen__physical_definition
            '"rw_math_vpu__vector3"': rw_math_vpu__vector3
            '"rw_math_vpu__matrix44affine"': rw_math_vpu__matrix44affine
            '"genesys__gen__make_physical_behaviour"': genesys__gen__make_physical_behaviour
            '"genesys__gen__corona"': genesys__gen__corona
            '"genesys__gen__wcplay_sound_behaviour"': genesys__gen__wcplay_sound_behaviour
            '"genesys__gen__wcvfx_behaviour"': genesys__gen__wcvfx_behaviour
            '"genesys__gen__dsp_plug_in"': genesys__gen__dsp_plug_in
            '"genesys__gen__pan2ddsp_plug_in"': genesys__gen__pan2ddsp_plug_in
            '"genesys__gen__sequence_item__modulating_double_value"': genesys__gen__sequence_item__modulating_double_value
            '"genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value"': genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value
            '"genesys__gen__voice_group"': genesys__gen__voice_group
            '"genesys__gen__mixer_channel__priority"': genesys__gen__mixer_channel__priority
            '"genesys__gen__post_fx_keyframe__bloom"': genesys__gen__post_fx_keyframe__bloom
            '"rw_math_vpu__vector2"': rw_math_vpu__vector2
            '"genesys__gen__post_fx_keyframe__vignette"': genesys__gen__post_fx_keyframe__vignette
            '"genesys__gen__post_fx_keyframe__general"': genesys__gen__post_fx_keyframe__general
            '"genesys__gen__sequence_item"': genesys__gen__sequence_item
            '"genesys__gen__race_car_effect_sequence_item__effect_double_value"': genesys__gen__race_car_effect_sequence_item__effect_double_value
            '"genesys__gen__race_car_effect_sequence_item"': genesys__gen__race_car_effect_sequence_item
            '"genesys__gen__post_fx_keyframe__depth_of__field"': genesys__gen__post_fx_keyframe__depth_of__field
            '"genesys__gen__peaking_dsp_plug_in"': genesys__gen__peaking_dsp_plug_in
            '"genesys__gen__post_fx_keyframe__stereo_3d"': genesys__gen__post_fx_keyframe__stereo_3d
            '"genesys__gen__post_fxstate__colour_cube_settings"': genesys__gen__post_fxstate__colour_cube_settings
            '"genesys__gen__post_fxstate__value_modifier"': genesys__gen__post_fxstate__value_modifier
            '"genesys__gen__heat_level_sound_set"': genesys__gen__heat_level_sound_set
            '"genesys__gen__sound_distance_falloff"': genesys__gen__sound_distance_falloff
            '"genesys__gen__post_fxsequence_item"': genesys__gen__post_fxsequence_item
            '"genesys__gen__wave_sequence_item__fade"': genesys__gen__wave_sequence_item__fade
            '"genesys__gen__sequence_items__post_fx_override_sequence_item"': genesys__gen__sequence_items__post_fx_override_sequence_item
            '"genesys__gen__sequence_items__post_fx_override_sequence_item__effect_double_value"': genesys__gen__sequence_items__post_fx_override_sequence_item__effect_double_value
            '"genesys__gen__mixer_channel"': genesys__gen__mixer_channel
            '"genesys__gen__mixing_group"': genesys__gen__mixing_group
            '"genesys__gen__high_pass_butterworth_dsp_plug_in"': genesys__gen__high_pass_butterworth_dsp_plug_in
            '"genesys__gen__sequence_timeline_controller"': genesys__gen__sequence_timeline_controller
            '"genesys__gen__sequence"': genesys__gen__sequence
            '"genesys__gen__jump_timeline_controller"': genesys__gen__jump_timeline_controller
            '"genesys__gen__sub_harmoniser_dsp_plug_in"': genesys__gen__sub_harmoniser_dsp_plug_in
            '"genesys__gen__delay_dsp_plug_in"': genesys__gen__delay_dsp_plug_in
            '"genesys__gen__quit_sequence_timeline_controller"': genesys__gen__quit_sequence_timeline_controller
            '"genesys__gen__wave_sequence_item"': genesys__gen__wave_sequence_item
            '"genesys__gen__send_dsp_plug_in"': genesys__gen__send_dsp_plug_in
            '"genesys__gen__post_fx_keyframe"': genesys__gen__post_fx_keyframe
            '"genesys__gen__post_fxstate"': genesys__gen__post_fxstate
            '"genesys__gen__dsp_plug_in_chain"': genesys__gen__dsp_plug_in_chain
            '"genesys__gen__submix_dsp_plug_in"': genesys__gen__submix_dsp_plug_in
            '"genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value"': genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value
            '"genesys__gen__bus_mixer_channel_sequence_item"': genesys__gen__bus_mixer_channel_sequence_item
            '"genesys__gen__general_trigger_sequence_item"': genesys__gen__general_trigger_sequence_item
            '"genesys__gen__snd_player_dsp_plug_in"': genesys__gen__snd_player_dsp_plug_in
            '"genesys__gen__heat_level_sound_set__nitrous"': genesys__gen__heat_level_sound_set__nitrous
            '"genesys__gen__heat_level_sound_set__sirens"': genesys__gen__heat_level_sound_set__sirens
            '"genesys__gen__distortion_dsp_plug_in"': genesys__gen__distortion_dsp_plug_in
            '"genesys__gen__mixer_channel_sequence_item"': genesys__gen__mixer_channel_sequence_item
            '"genesys__gen__uilist_items__item"': genesys__gen__uilist_items__item
            '"genesys__gen__uilist_items"': genesys__gen__uilist_items
            '"genesys__gen__damage_bar_profiles__profile__segment_data"': genesys__gen__damage_bar_profiles__profile__segment_data
            '"genesys__gen__damage_bar_profiles__profile"': genesys__gen__damage_bar_profiles__profile
            '"genesys__gen__collision_effects"': genesys__gen__collision_effects
            '"genesys__gen__collision_effects__battling_effect__skid_effects"': genesys__gen__collision_effects__battling_effect__skid_effects
            '"genesys__gen__collision_effects__battling_effect__extra_roll_params"': genesys__gen__collision_effects__battling_effect__extra_roll_params
            '"genesys__gen__collision_effects__battling_effect"': genesys__gen__collision_effects__battling_effect
            '"genesys__gen__collision_effects__traffic_effect__extra_roll_params"': genesys__gen__collision_effects__traffic_effect__extra_roll_params
            '"genesys__gen__collision_effects__traffic_effect"': genesys__gen__collision_effects__traffic_effect
            '"genesys__gen__collision_effects__world_effect"': genesys__gen__collision_effects__world_effect
            '"genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal"': genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal
            '"genesys__gen__physics__crashing_rules__impact_rules"': genesys__gen__physics__crashing_rules__impact_rules
            '"genesys__gen__physics__crashing_rules"': genesys__gen__physics__crashing_rules
            '"genesys__gen__collision_responses__world__traffic"': genesys__gen__collision_responses__world__traffic
            '"genesys__gen__collision_responses__world__player__flip_state"': genesys__gen__collision_responses__world__player__flip_state
            '"genesys__gen__collision_responses__world__crashed_player__constraint_data"': genesys__gen__collision_responses__world__crashed_player__constraint_data
            '"genesys__gen__collision_responses__world__crashed_player"': genesys__gen__collision_responses__world__crashed_player
            '"genesys__gen__race_car_handling_disruption_effect"': genesys__gen__race_car_handling_disruption_effect
            '"genesys__gen__physics__landing_damage"': genesys__gen__physics__landing_damage
            '"genesys__gen__physics__landing_damage__pitch"': genesys__gen__physics__landing_damage__pitch
            '"genesys__gen__physics__landing_damage__roll"': genesys__gen__physics__landing_damage__roll
            '"genesys__gen__physics__damage_bar_profile__impact_location_damage_scale"': genesys__gen__physics__damage_bar_profile__impact_location_damage_scale
            '"genesys__gen__collision_info__world_effect"': genesys__gen__collision_info__world_effect
            '"genesys__gen__collision_info_damage_profile"': genesys__gen__collision_info_damage_profile
            '"genesys__gen__collision_info__world_damage"': genesys__gen__collision_info__world_damage
            '"genesys__gen__collision_info__battling_damage"': genesys__gen__collision_info__battling_damage
            '"genesys__gen__collision_info__payload_damage"': genesys__gen__collision_info__payload_damage
            '"genesys__gen__collision_responses__global"': genesys__gen__collision_responses__global
            '"genesys__gen__collision_responses__global__race_car_vs_race_car"': genesys__gen__collision_responses__global__race_car_vs_race_car
            '"genesys__gen__collision_responses__global__race_car_vs_race_car__params"': genesys__gen__collision_responses__global__race_car_vs_race_car__params
            '"genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params"': genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params
            '"genesys__gen__collision_responses__global__crashing_race_car_vs_traffic"': genesys__gen__collision_responses__global__crashing_race_car_vs_traffic
            '"genesys__gen__collision_responses__global__traffic_vs_dynamic"': genesys__gen__collision_responses__global__traffic_vs_dynamic
            '"genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car"': genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car
            '"genesys__gen__collision_responses__global__traffic_vs_traffic"': genesys__gen__collision_responses__global__traffic_vs_traffic
            '"genesys__gen__collision_responses__global__dynamic_vs_dynamic"': genesys__gen__collision_responses__global__dynamic_vs_dynamic
            '"genesys__gen__collision_responses__race_car"': genesys__gen__collision_responses__race_car
            '"genesys__gen__collision_responses__race_car__player_vs_traffic"': genesys__gen__collision_responses__race_car__player_vs_traffic
            '"genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params"': genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params
            '"genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params"': genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params
            '"genesys__gen__collision_responses__race_car__player_vs_ai"': genesys__gen__collision_responses__race_car__player_vs_ai
            '"genesys__gen__collision_responses__race_car__player_vs_ai__damage_params"': genesys__gen__collision_responses__race_car__player_vs_ai__damage_params
            '"genesys__gen__collision_responses__race_car__player_vs_ai__basic_params"': genesys__gen__collision_responses__race_car__player_vs_ai__basic_params
            '"genesys__gen__collision_responses__race_car__aivs_traffic"': genesys__gen__collision_responses__race_car__aivs_traffic
            '"genesys__gen__collision_responses__race_car__aivs_traffic__damage_params"': genesys__gen__collision_responses__race_car__aivs_traffic__damage_params
            '"genesys__gen__collision_responses__race_car__aivs_traffic__basic_params"': genesys__gen__collision_responses__race_car__aivs_traffic__basic_params
            '"genesys__gen__collision_responses__race_car__player_vs_crashing_race_car"': genesys__gen__collision_responses__race_car__player_vs_crashing_race_car
            '"genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile"': genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile
            '"genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params"': genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params
            '"genesys__gen__collision_responses__race_car__aivs_crashing_race_car"': genesys__gen__collision_responses__race_car__aivs_crashing_race_car
            '"genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params"': genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params
            '"genesys__gen__collision_responses__race_car__race_car_vs_dynamic"': genesys__gen__collision_responses__race_car__race_car_vs_dynamic
            '"genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params"': genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params
            '"genesys__gen__collision_responses__world__in_air_player"': genesys__gen__collision_responses__world__in_air_player
            '"genesys__gen__physics__damage_bar_profile__segment"': genesys__gen__physics__damage_bar_profile__segment
            '"genesys__gen__physics__damage_bar_profile"': genesys__gen__physics__damage_bar_profile
            '"genesys__gen__collision_info"': genesys__gen__collision_info
            '"genesys__gen__collision_info__battling_effect"': genesys__gen__collision_info__battling_effect
            '"genesys__gen__collision_info__battling_effect__extra_roll_params"': genesys__gen__collision_info__battling_effect__extra_roll_params
            '"genesys__gen__collision_info__traffic_effect"': genesys__gen__collision_info__traffic_effect
            '"genesys__gen__camera_gameplay_shake_effect"': genesys__gen__camera_gameplay_shake_effect
            '"genesys__gen__camera_gameplay_shake_effect__translation"': genesys__gen__camera_gameplay_shake_effect__translation
            '"genesys__gen__camera_gameplay_shake_effect__translation__axis_params"': genesys__gen__camera_gameplay_shake_effect__translation__axis_params
            '"genesys__gen__camera_gameplay_shake_effect__rotation"': genesys__gen__camera_gameplay_shake_effect__rotation
            '"genesys__gen__camera_gameplay_shake_effect__rotation__axis_params"': genesys__gen__camera_gameplay_shake_effect__rotation__axis_params
            '"genesys__gen__impact_damage_graphs"': genesys__gen__impact_damage_graphs
            '"genesys__gen__impact_damage_graphs__graph"': genesys__gen__impact_damage_graphs__graph
            '"genesys__gen__collision_responses__world"': genesys__gen__collision_responses__world
            '"genesys__gen__collision_responses__world__player"': genesys__gen__collision_responses__world__player
            '"genesys__gen__damage_bar_profiles"': genesys__gen__damage_bar_profiles
            '"genesys__gen__traffic_flow_type__traffic_flow_type"': genesys__gen__traffic_flow_type__traffic_flow_type
            '"genesys__gen__traffic_flow"': genesys__gen__traffic_flow
            '"genesys__gen__traffic_flow_type"': genesys__gen__traffic_flow_type
            '"genesys__gen__traffic_vehicle"': genesys__gen__traffic_vehicle
            '"genesys__gen__traffic_vehicle_traits"': genesys__gen__traffic_vehicle_traits
            '"genesys__gen__dynamic_additional_info"': genesys__gen__dynamic_additional_info
            '"genesys__gen__compound_additional_info"': genesys__gen__compound_additional_info
            '"genesys__gen__light__base__flash_pattern"': genesys__gen__light__base__flash_pattern
            '"genesys__gen__light__base"': genesys__gen__light__base
            '"genesys__gen__light__cone"': genesys__gen__light__cone
            '"genesys__gen__light__point"': genesys__gen__light__point
            '"genesys__gen__smash_proxy_behaviour"': genesys__gen__smash_proxy_behaviour
            '"genesys__gen__light__spot"': genesys__gen__light__spot
            '"genesys__gen__enable_compound_behaviour"': genesys__gen__enable_compound_behaviour
            '"genesys__gen__easy_guide__page"': genesys__gen__easy_guide__page
            '"genesys__gen__nitrous_parameters__traffic_near_miss"': genesys__gen__nitrous_parameters__traffic_near_miss
            '"genesys__gen__nitrous_strength__jump"': genesys__gen__nitrous_strength__jump
            '"genesys__gen__nitrous_parameters__traffic_oncoming"': genesys__gen__nitrous_parameters__traffic_oncoming
            '"genesys__gen__nitrous_parameters__nitrous_power"': genesys__gen__nitrous_parameters__nitrous_power
            '"genesys__gen__nitrous_parameters__hitting_another_competitor"': genesys__gen__nitrous_parameters__hitting_another_competitor
            '"genesys__gen__nitrous_parameters__high_speed"': genesys__gen__nitrous_parameters__high_speed
            '"genesys__gen__nitrous_parameters__catching_air"': genesys__gen__nitrous_parameters__catching_air
            '"genesys__gen__nitrous_parameters__balancing"': genesys__gen__nitrous_parameters__balancing
            '"genesys__gen__nitrous_parameters__slipstreaming"': genesys__gen__nitrous_parameters__slipstreaming
            '"genesys__gen__nitrous_parameters__fatal_hit"': genesys__gen__nitrous_parameters__fatal_hit
            '"genesys__gen__aerodynamic_behaviour"': genesys__gen__aerodynamic_behaviour
            '"genesys__gen__ginsu_sequence_item"': genesys__gen__ginsu_sequence_item
            '"genesys__gen__ginsu_sequence_item__fade"': genesys__gen__ginsu_sequence_item__fade
            '"genesys__gen__gearbox__gear"': genesys__gen__gearbox__gear
            '"genesys__gen__gearbox"': genesys__gen__gearbox
            '"genesys__gen__colour_group"': genesys__gen__colour_group
            '"genesys__gen__performance_modification_item"': genesys__gen__performance_modification_item
            '"genesys__gen__performance_modifier"': genesys__gen__performance_modifier
            '"genesys__gen__handbrake_ability"': genesys__gen__handbrake_ability
            '"genesys__gen__nitrous_parameters__donutting"': genesys__gen__nitrous_parameters__donutting
            '"genesys__gen__vehicle__gameplay__mod_effect"': genesys__gen__vehicle__gameplay__mod_effect
            '"genesys__gen__aligning_torque"': genesys__gen__aligning_torque
            '"genesys__gen__body_movement_behaviour__take_off_behaviour"': genesys__gen__body_movement_behaviour__take_off_behaviour
            '"genesys__gen__body_movement_behaviour"': genesys__gen__body_movement_behaviour
            '"genesys__gen__brake_behaviour"': genesys__gen__brake_behaviour
            '"genesys__gen__donut_ability__donut_grip_values"': genesys__gen__donut_ability__donut_grip_values
            '"genesys__gen__donut_ability__donut_scale"': genesys__gen__donut_ability__donut_scale
            '"genesys__gen__donut_ability"': genesys__gen__donut_ability
            '"genesys__gen__drift_behaviour__other"': genesys__gen__drift_behaviour__other
            '"genesys__gen__drift_behaviour__yaw_torque"': genesys__gen__drift_behaviour__yaw_torque
            '"genesys__gen__drift_behaviour__side_force"': genesys__gen__drift_behaviour__side_force
            '"genesys__gen__drift_behaviour__drift_scale"': genesys__gen__drift_behaviour__drift_scale
            '"genesys__gen__drift_behaviour__drift_exit"': genesys__gen__drift_behaviour__drift_exit
            '"genesys__gen__drift_behaviour__drift_trigger"': genesys__gen__drift_behaviour__drift_trigger
            '"genesys__gen__drift_behaviour"': genesys__gen__drift_behaviour
            '"genesys__gen__point2d"': genesys__gen__point2d
            '"genesys__gen__point2dwith_tangents"': genesys__gen__point2dwith_tangents
            '"genesys__gen__engine__power_curve"': genesys__gen__engine__power_curve
            '"genesys__gen__engine__sound"': genesys__gen__engine__sound
            '"genesys__gen__engine__differentials"': genesys__gen__engine__differentials
            '"genesys__gen__engine__normal_quality_engine"': genesys__gen__engine__normal_quality_engine
            '"genesys__gen__engine__transmission"': genesys__gen__engine__transmission
            '"genesys__gen__nitrous_strength"': genesys__gen__nitrous_strength
            '"genesys__gen__engine"': genesys__gen__engine
            '"genesys__gen__hard_driving_behaviour__gas_effect"': genesys__gen__hard_driving_behaviour__gas_effect
            '"genesys__gen__hard_driving_behaviour__steering_effect"': genesys__gen__hard_driving_behaviour__steering_effect
            '"genesys__gen__hard_driving_behaviour"': genesys__gen__hard_driving_behaviour
            '"genesys__gen__steering_behaviour"': genesys__gen__steering_behaviour
            '"genesys__gen__steering_wheel_physics"': genesys__gen__steering_wheel_physics
            '"genesys__gen__suspension"': genesys__gen__suspension
            '"genesys__gen__tyre__lateral__slip__factors"': genesys__gen__tyre__lateral__slip__factors
            '"genesys__gen__tyre__lateral__grip__curve"': genesys__gen__tyre__lateral__grip__curve
            '"genesys__gen__tyre__long__grip__curve"': genesys__gen__tyre__long__grip__curve
            '"genesys__gen__tyre__long__slip__factors"': genesys__gen__tyre__long__slip__factors
            '"genesys__gen__tyre"': genesys__gen__tyre
            '"genesys__gen__tyres__tyres"': genesys__gen__tyres__tyres
            '"genesys__gen__vehicle_surface_profile__surface_link"': genesys__gen__vehicle_surface_profile__surface_link
            '"genesys__gen__vehicle_surface_profile"': genesys__gen__vehicle_surface_profile
            '"genesys__gen__tyres__surface_effects"': genesys__gen__tyres__surface_effects
            '"genesys__gen__tyre_sound_params__lateral"': genesys__gen__tyre_sound_params__lateral
            '"genesys__gen__tyre_sound_params__lat_slip"': genesys__gen__tyre_sound_params__lat_slip
            '"genesys__gen__tyre_sound_params__longitudinal"': genesys__gen__tyre_sound_params__longitudinal
            '"genesys__gen__tyre_sound_params__long_spin_braking"': genesys__gen__tyre_sound_params__long_spin_braking
            '"genesys__gen__tyre_sound_params__long_spin"': genesys__gen__tyre_sound_params__long_spin
            '"genesys__gen__tyre_sound_params"': genesys__gen__tyre_sound_params
            '"genesys__gen__tyres"': genesys__gen__tyres
            '"genesys__gen__handling_behaviour"': genesys__gen__handling_behaviour
            '"genesys__gen__nitrous_strength__punch"': genesys__gen__nitrous_strength__punch
            '"genesys__gen__engine_sound2__dsp_param"': genesys__gen__engine_sound2__dsp_param
            '"genesys__gen__engine_sound2__dsp_param_wrapper"': genesys__gen__engine_sound2__dsp_param_wrapper
            '"genesys__gen__engine_sound2__gain_param"': genesys__gen__engine_sound2__gain_param
            '"genesys__gen__engine_sound2__gain_param_wrapper"': genesys__gen__engine_sound2__gain_param_wrapper
            '"genesys__gen__engine_sound2"': genesys__gen__engine_sound2
            '"genesys__gen__vehicle__driver_setup__seat_belt_bone_offset"': genesys__gen__vehicle__driver_setup__seat_belt_bone_offset
            '"genesys__gen__vehicle__driver_setup"': genesys__gen__vehicle__driver_setup
            '"genesys__gen__steering_wheel_behaviour"': genesys__gen__steering_wheel_behaviour
            '"genesys__gen__steering_behaviour__steering_angle_curve"': genesys__gen__steering_behaviour__steering_angle_curve
            '"genesys__gen__vehicle__sound"': genesys__gen__vehicle__sound
            '"genesys__gen__suspension_wheel"': genesys__gen__suspension_wheel
            '"genesys__gen__wheel_suspension_constraint"': genesys__gen__wheel_suspension_constraint
            '"genesys__gen__wheel_suspension_spring_constraint"': genesys__gen__wheel_suspension_spring_constraint
            '"genesys__gen__light__projected_texture"': genesys__gen__light__projected_texture
            '"genesys__gen__pidcontroller"': genesys__gen__pidcontroller
            '"genesys__gen__body_movement_behaviour__angle_control"': genesys__gen__body_movement_behaviour__angle_control
            '"genesys__gen__vehicle_damage_behaviour__damage_sequence"': genesys__gen__vehicle_damage_behaviour__damage_sequence
            '"genesys__gen__vfx_locator_group_vehicle_spot_effect_sequence_item"': genesys__gen__vfx_locator_group_vehicle_spot_effect_sequence_item
            '"genesys__gen__camera_gameplay_bonnet__wind_sound"': genesys__gen__camera_gameplay_bonnet__wind_sound
            '"genesys__gen__camera_gameplay_external__acceleration_movement"': genesys__gen__camera_gameplay_external__acceleration_movement
            '"genesys__gen__camera_gameplay_external__yaw_spring_modification"': genesys__gen__camera_gameplay_external__yaw_spring_modification
            '"genesys__gen__camera_gameplay_external__speed_based_height_change"': genesys__gen__camera_gameplay_external__speed_based_height_change
            '"genesys__gen__camera_gameplay_external_globals__impact_shake"': genesys__gen__camera_gameplay_external_globals__impact_shake
            '"genesys__gen__high_shelf_dsp_plug_in"': genesys__gen__high_shelf_dsp_plug_in
            '"genesys__gen__camera_gameplay_bonnet"': genesys__gen__camera_gameplay_bonnet
            '"genesys__gen__camera_gameplay_bumper"': genesys__gen__camera_gameplay_bumper
            '"genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold"': genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold
            '"genesys__gen__vehicle_damage_behaviour__bodypart"': genesys__gen__vehicle_damage_behaviour__bodypart
            '"genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake"': genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake
            '"genesys__gen__camera_gameplay_external__speed_based_movement"': genesys__gen__camera_gameplay_external__speed_based_movement
            '"genesys__gen__camera_gameplay_external__camera__roll"': genesys__gen__camera_gameplay_external__camera__roll
            '"genesys__gen__camera_gameplay_external__deceleration__pitch__change"': genesys__gen__camera_gameplay_external__deceleration__pitch__change
            '"genesys__gen__camera_gameplay_external_globals__lens_properties"': genesys__gen__camera_gameplay_external_globals__lens_properties
            '"genesys__gen__camera_gameplay_external_globals"': genesys__gen__camera_gameplay_external_globals
            '"genesys__gen__camera_gameplay_gradient_adjustments__params"': genesys__gen__camera_gameplay_gradient_adjustments__params
            '"genesys__gen__camera_gameplay_gradient_adjustments"': genesys__gen__camera_gameplay_gradient_adjustments
            '"genesys__gen__camera_gameplay_external"': genesys__gen__camera_gameplay_external
            '"genesys__gen__vehicle_damage_behaviour__spot_effect"': genesys__gen__vehicle_damage_behaviour__spot_effect
            '"genesys__gen__vehicle_paint__material_properties"': genesys__gen__vehicle_paint__material_properties
            '"genesys__gen__camera_rear_view_globals"': genesys__gen__camera_rear_view_globals
            '"genesys__gen__camera_rear_view"': genesys__gen__camera_rear_view
            '"genesys__gen__vehicle_paint__structure2"': genesys__gen__vehicle_paint__structure2
            '"genesys__gen__vehicle_vfx_behaviour__corona"': genesys__gen__vehicle_vfx_behaviour__corona
            '"genesys__gen__vehicle_vfx_behaviour__light"': genesys__gen__vehicle_vfx_behaviour__light
            '"genesys__gen__vehicle_vfx_behaviour__spot_effect"': genesys__gen__vehicle_vfx_behaviour__spot_effect
            '"genesys__gen__passby_sequence_behaviour"': genesys__gen__passby_sequence_behaviour
            '"genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face"': genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face
            '"genesys__gen__race_car_physical_definition__convex_hull_conectivity_data"': genesys__gen__race_car_physical_definition__convex_hull_conectivity_data
            '"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume"': genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume
            '"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__capsule_volume"': genesys__gen__race_car_physical_definition__physical_definition__rigid_body__capsule_volume
            '"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume"': genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume
            '"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume"': genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume
            '"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume"': genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume
            '"genesys__gen__race_car_physical_definition__physical_definition__rigid_body"': genesys__gen__race_car_physical_definition__physical_definition__rigid_body
            '"genesys__gen__race_car_physical_definition__physical_definition"': genesys__gen__race_car_physical_definition__physical_definition
            '"genesys__gen__race_car_physical_definition"': genesys__gen__race_car_physical_definition
            '"genesys__gen__nitrous_parameters__crash_escape"': genesys__gen__nitrous_parameters__crash_escape
            '"genesys__gen__vehicle_camera_container"': genesys__gen__vehicle_camera_container
            '"genesys__gen__vehicle_colour_palette"': genesys__gen__vehicle_colour_palette
            '"genesys__gen__nitrous_parameters_usage"': genesys__gen__nitrous_parameters_usage
            '"genesys__gen__nitrous_parameters__speedbreaker_usage"': genesys__gen__nitrous_parameters__speedbreaker_usage
            '"genesys__gen__nitrous_parameters"': genesys__gen__nitrous_parameters
            '"genesys__gen__nitrous_parameters__drifting"': genesys__gen__nitrous_parameters__drifting
            '"genesys__gen__nitrous_parameters__punch_usage"': genesys__gen__nitrous_parameters__punch_usage
            '"genesys__gen__nitrous_parameters__min_speed"': genesys__gen__nitrous_parameters__min_speed
            '"genesys__gen__nitrous_parameters__nitrous_usage"': genesys__gen__nitrous_parameters__nitrous_usage
            '"genesys__gen__nitrous_parameters__taking_shortcut"': genesys__gen__nitrous_parameters__taking_shortcut
            '"genesys__gen__nitrous_parameters__jump_usage"': genesys__gen__nitrous_parameters__jump_usage
            '"genesys__gen__nitrous_parameters__restrictions"': genesys__gen__nitrous_parameters__restrictions
            '"genesys__gen__vehicle_component__wheel"': genesys__gen__vehicle_component__wheel
            '"genesys__gen__vehicle_component"': genesys__gen__vehicle_component
            '"genesys__gen__vehicle_damage_behaviour"': genesys__gen__vehicle_damage_behaviour
            '"genesys__gen__vehicle_info__axle"': genesys__gen__vehicle_info__axle
            '"genesys__gen__vehicle_info__extra_axle"': genesys__gen__vehicle_info__extra_axle
            '"genesys__gen__vehicle_info"': genesys__gen__vehicle_info
            '"genesys__gen__vehicles__upgrade_base"': genesys__gen__vehicles__upgrade_base
            '"genesys__gen__vehicles__performance_upgrades"': genesys__gen__vehicles__performance_upgrades
            '"genesys__gen__vehicles__performance_upgrades__category"': genesys__gen__vehicles__performance_upgrades__category
            '"genesys__gen__vehicle_paint"': genesys__gen__vehicle_paint
            '"genesys__gen__vehicles__tyre_upgrade"': genesys__gen__vehicles__tyre_upgrade
            '"genesys__gen__engine__reverse_whine"': genesys__gen__engine__reverse_whine
            '"genesys__gen__vehicle_vfx_behaviour"': genesys__gen__vehicle_vfx_behaviour
            '"genesys__gen__engine__mixer__channel__gain__modification"': genesys__gen__engine__mixer__channel__gain__modification
            '"genesys__gen__engine__mix"': genesys__gen__engine__mix
            '"genesys__gen__control_mesh"': genesys__gen__control_mesh
            '"genesys__gen__vehicles__vehicle_category_info"': genesys__gen__vehicles__vehicle_category_info
            '"genesys__gen__band_pass_dsp_plug_in"': genesys__gen__band_pass_dsp_plug_in
            '"genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params"': genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params
            '"genesys__gen__wheel_damage"': genesys__gen__wheel_damage
            '"genesys__gen__ginsu_dsp_plug_in"': genesys__gen__ginsu_dsp_plug_in
            '"genesys__gen__low_pass_butterworth_dsp_plug_in"': genesys__gen__low_pass_butterworth_dsp_plug_in
            '"genesys__gen__vehicle__gameplay__damage_stats"': genesys__gen__vehicle__gameplay__damage_stats
            '"genesys__gen__wheel_sizes"': genesys__gen__wheel_sizes
            '"genesys__gen__timeline_controllers__race_car_entity_timeline_controller"': genesys__gen__timeline_controllers__race_car_entity_timeline_controller
            '"genesys__gen__handbrake_ability__handbrake_grip_values"': genesys__gen__handbrake_ability__handbrake_grip_values
            '"genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params"': genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params
            '"genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params"': genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params
            '"genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params"': genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params
            '"genesys__gen__tyre_vfx_behaviour__front_rear_params"': genesys__gen__tyre_vfx_behaviour__front_rear_params
            '"genesys__gen__tyre_vfx_behaviour"': genesys__gen__tyre_vfx_behaviour
            '"genesys__gen__vehicles__sound__transmission_whine"': genesys__gen__vehicles__sound__transmission_whine
            '"genesys__gen__tyre_vfx_behaviour__long_lat_params"': genesys__gen__tyre_vfx_behaviour__long_lat_params
            '"genesys__gen__tyre_vfx_behaviour__smoke_params"': genesys__gen__tyre_vfx_behaviour__smoke_params
            '"genesys__gen__tyre_vfx_behaviour__skid_mark_params"': genesys__gen__tyre_vfx_behaviour__skid_mark_params
            '"genesys__gen__vehicles__modifier_upgrade"': genesys__gen__vehicles__modifier_upgrade
            '"genesys__gen__vehicles__nitrous_upgrade"': genesys__gen__vehicles__nitrous_upgrade
            '"genesys__gen__lfo_sequence_item"': genesys__gen__lfo_sequence_item
            '"genesys__gen__lfo_sequence_item__lfo_double_value"': genesys__gen__lfo_sequence_item__lfo_double_value
            '"genesys__gen__vehicle__gameplay__tyre_trails"': genesys__gen__vehicle__gameplay__tyre_trails
            '"genesys__gen__vehicle__gameplay"': genesys__gen__vehicle__gameplay
            '"genesys__gen__online__driving_test_list"': genesys__gen__online__driving_test_list
            '"genesys__gen__online__driving_test_list_group"': genesys__gen__online__driving_test_list_group
            '"genesys__gen__gameplay__offline_upgrade"': genesys__gen__gameplay__offline_upgrade
            '"genesys__gen__nucleus_grant_mappings_list__mapping"': genesys__gen__nucleus_grant_mappings_list__mapping
            '"genesys__gen__online__driving_test_list_groups"': genesys__gen__online__driving_test_list_groups
            '"genesys__gen__heat_level"': genesys__gen__heat_level
            '"genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour"': genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour
            '"genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour"': genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour
            '"genesys__gen__heat_level__behaviour_coordination"': genesys__gen__heat_level__behaviour_coordination
            '"int8_t"': int8_t
            '"genesys__gen__game_pack"': genesys__gen__game_pack
            '"genesys__gen__game_rank"': genesys__gen__game_rank
            '"genesys__gen__game_unlock"': genesys__gen__game_unlock
            '"genesys__gen__game_unlock_list"': genesys__gen__game_unlock_list
            '"genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control"': genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control
            '"genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold"': genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold
            '"genesys__gen__road_block_layer__item"': genesys__gen__road_block_layer__item
            '"genesys__gen__gameplay_trigger__input"': genesys__gen__gameplay_trigger__input
            '"genesys__gen__aiplayer_instance"': genesys__gen__aiplayer_instance
            '"genesys__gen__gameplay_trigger__aiplayer_information"': genesys__gen__gameplay_trigger__aiplayer_information
            '"genesys__gen__gameplay_trigger__output__sequence_output"': genesys__gen__gameplay_trigger__output__sequence_output
            '"genesys__gen__roadblock_instance"': genesys__gen__roadblock_instance
            '"genesys__gen__gameplay_trigger__output"': genesys__gen__gameplay_trigger__output
            '"genesys__gen__gameplay_trigger"': genesys__gen__gameplay_trigger
            '"genesys__gen__online_challenge_target"': genesys__gen__online_challenge_target
            '"genesys__gen__online_challenge"': genesys__gen__online_challenge
            '"genesys__gen__store_item"': genesys__gen__store_item
            '"genesys__gen__store_pack"': genesys__gen__store_pack
            '"genesys__gen__store_pack_list"': genesys__gen__store_pack_list
            '"genesys__gen__scoring_action__online_scoring_feedback"': genesys__gen__scoring_action__online_scoring_feedback
            '"genesys__gen__thankyou_mapping"': genesys__gen__thankyou_mapping
            '"genesys__gen__rollout__weapon_data"': genesys__gen__rollout__weapon_data
            '"genesys__gen__thank_you_screen_item"': genesys__gen__thank_you_screen_item
            '"genesys__gen__aiplayer_type"': genesys__gen__aiplayer_type
            '"genesys__gen__uicamera"': genesys__gen__uicamera
            '"genesys__gen__car_select_data__sequences"': genesys__gen__car_select_data__sequences
            '"genesys__gen__safehouse"': genesys__gen__safehouse
            '"genesys__gen__gameplay__drift_marker"': genesys__gen__gameplay__drift_marker
            '"genesys__gen__rollout"': genesys__gen__rollout
            '"genesys__gen__scoring_action"': genesys__gen__scoring_action
            '"genesys__gen__car_select_data"': genesys__gen__car_select_data
            '"genesys__gen__gameplay__milestone__entry"': genesys__gen__gameplay__milestone__entry
            '"genesys__gen__gameplay__milestone"': genesys__gen__gameplay__milestone
            '"genesys__gen__nucleus_entitlement_tag"': genesys__gen__nucleus_entitlement_tag
            '"genesys__gen__nucleus_entitlement_tags"': genesys__gen__nucleus_entitlement_tags
            '"genesys__gen__nucleus_grant_mappings_list"': genesys__gen__nucleus_grant_mappings_list
            '"genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods"': genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods
            '"genesys__gen__paint_pack"': genesys__gen__paint_pack
            '"genesys__gen__paint_pack_group"': genesys__gen__paint_pack_group
            '"genesys__gen__car_swap_spot"': genesys__gen__car_swap_spot
            '"genesys__gen__online__license_plate"': genesys__gen__online__license_plate
            '"genesys__gen__entitlement"': genesys__gen__entitlement
            '"genesys__gen__gameplay__revenge_bonus"': genesys__gen__gameplay__revenge_bonus
            '"genesys__gen__event_list"': genesys__gen__event_list
            '"genesys__gen__event_location"': genesys__gen__event_location
            '"genesys__gen__road_block_definition"': genesys__gen__road_block_definition
            '"genesys__gen__road_block_layer"': genesys__gen__road_block_layer
            '"genesys__gen__gameplay__blacklist_shutdown_data"': genesys__gen__gameplay__blacklist_shutdown_data
            '"genesys__gen__gameplay__allowed_vehicle_list"': genesys__gen__gameplay__allowed_vehicle_list
            '"genesys__gen__gameplay__cop_type"': genesys__gen__gameplay__cop_type
            '"genesys__gen__cloud_compete_award"': genesys__gen__cloud_compete_award
            '"genesys_obj_collection"': genesys_obj_collection
            '"any_genesys_obj"': any_genesys_obj

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