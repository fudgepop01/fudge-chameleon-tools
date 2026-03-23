meta:
  id: generic_gen_object
  endian: be
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
        0x09_97_15_d1: genesys__gen__behaviour
        0x95_fb_ea_be: string_base
        0x9c_cd_d1_68: genesys__gen__physical_definition__rigid_body__box_volume
        0x01_12_fc_16: genesys__gen__physical_definition__rigid_body__cylinder_volume
        0x63_33_d3_31: genesys__gen__physical_definition__rigid_body__convex_hull_volume
        0xf9_19_5e_af: genesys__gen__physical_definition__rigid_body__sphere_volume
        0x8c_ca_12_b3: genesys__gen__physical_definition__rigid_body
        0x92_bf_42_33: genesys__gen__physical_definition
        0xa5_f5_99_f3: rw_math_vpu__vector3
        0xb6_8b_60_0e: rw_math_vpu__matrix44affine
        0xc2_29_a8_2f: rw_math_vpu__vector4
        0xf8_19_e6_79: genesys__gen__corona
        0xfb_72_73_f3: genesys__gen__wcplay_sound_behaviour
        0x01_f2_27_ad: genesys__gen__wcvfx_behaviour
        0xb9_30_1e_9c: genesys__gen__corona__glow
        0xa2_b1_30_07: genesys__gen__corona__env_map_glow
        0xb5_9a_5e_dc: genesys__gen__corona__beam
        0xad_a5_0d_dc: genesys__gen__corona__flare
        0xdf_e3_19_75: genesys__gen__wcvfx_behaviour__coronas
        0xec_16_af_6a: genesys__gen__wcvfx_behaviour__spot_effects
        0xcb_b3_7b_5b: genesys__gen__wcvfx_behaviour__lights
        0xb9_ac_70_67: genesys__gen__wcplay_sound_behaviour__prop_surface_sound
        0x1c_72_63_08: genesys__gen__make_physical_behaviour
        0x3e_e2_74_05: genesys__gen__wcremove_world_entity_behaviour
        0x43_d3_4f_71: genesys__gen__game_mode
        0x69_06_e8_a3: genesys__gen__event
        0xa1_9a_e6_e7: genesys__gen__online_event
        0x97_bb_27_7e: genesys__gen__event_arena
        0xae_f6_41_5c: genesys__gen__event_arena_data
        0xd3_97_39_6c: genesys__gen__score_view_model
        0x24_2c_b4_ca: genesys__gen__score_view_model__score_data
        0xe0_51_7c_e1: genesys__gen__game_mode__score_override
        0x32_ac_e7_1b: genesys__gen__chevron
        0x1e_06_6a_b1: genesys__gen__offline_event
        0xa5_6a_24_27: genesys__gen__aiplayer_instance
        0x66_9e_7a_1d: genesys__gen__offline_event__custom_chevrons
        0xac_a9_15_3e: genesys__gen__custom_chevron
        0xbc_85_5d_7f: genesys_obj_collection
        0xee_73_7c_02: genesys__gen__car_select_data
        0x98_9c_04_d1: genesys__gen__entitlement
        0x3a_7e_79_74: genesys__gen__event_list
        0xe9_6b_72_79: genesys__gen__event_location
        0xd4_53_06_9d: genesys__gen__game_pack
        0x83_b0_e4_19: genesys__gen__gameplay_milestone
        0x70_1e_13_71: genesys__gen__game_rank
        0x97_40_43_c6: genesys__gen__game_unlock
        0x52_00_dc_f4: genesys__gen__game_unlock__event
        0x48_7f_29_ad: genesys__gen__game_unlock__milestone
        0x2c_04_42_9d: genesys__gen__game_unlock_list
        0x48_46_99_8b: genesys__gen__nucleus_entitlement_tag
        0xba_a5_64_08: genesys__gen__nucleus_entitlement_tags
        0x3a_26_00_0e: genesys__gen__nucleus_grant_mappings_list
        0xb0_09_2b_8e: genesys__gen__road_block_definition
        0x65_03_e6_7a: genesys__gen__road_block_layer
        0xaf_b3_ae_aa: genesys__gen__store_item
        0xb7_10_a2_08: genesys__gen__store_pack
        0xd4_f9_60_f2: genesys__gen__store_pack_list
        0x63_9c_ba_fd: genesys__gen__thankyou_mapping
        0x99_b7_15_31: genesys__gen__thank_you_screen_item
        0xfe_41_d4_24: genesys__gen__uicamera
        0x63_78_a7_1f: genesys__gen__car_select_data__sequences
        0x6e_2f_b0_1d: genesys__gen__gameplay_milestone__entry
        0xfe_1c_ee_ea: genesys__gen__nucleus_grant_mappings_list__mapping
        0xa7_64_a6_e7: genesys__gen__road_block_layer__item
        0xd8_80_1e_64: genesys__gen__upgrade_package
        0xfd_42_7b_87: genesys__gen__device_grant_upgrade_package
        0x20_91_91_f5: genesys__gen__performance_upgrade_package
        0xdb_ad_40_b1: genesys__gen__rollout
        0x32_00_82_dd: genesys__gen__perk
        0x6d_ae_98_7f: genesys__gen__perk_level
        0x1d_72_6a_04: genesys__gen__game_rule
        0x8c_91_2b_55: genesys__gen__nitrous_earning_game_rule
        0xd0_c3_9c_8b: genesys__gen__nitrous_burning_game_rule
        0xee_0a_cb_16: genesys__gen__impact_protection_game_rule
        0x1a_0d_be_44: genesys__gen__impact_damage_game_rule
        0xc9_d9_31_4f: genesys__gen__rollout__weapon_data
        0x86_49_8f_4e: genesys__gen__scoring_action
        0x88_49_d6_4a: genesys__gen__heat_level
        0xbd_37_77_79: genesys__gen__gameplay_trigger__output__sequence_output
        0x80_52_29_7f: genesys__gen__aiplayer_type
        0x24_2c_7a_43: genesys__gen__gameplay_trigger
        0x37_ad_05_45: genesys__gen__gameplay_trigger__input
        0x56_b9_1f_bf: genesys__gen__gameplay_trigger__output
        0x7a_12_3c_69: genesys__gen__heat_level__cop_type
        0x7c_8e_25_02: genesys__gen__roadblock_instance
        0x8c_47_45_f7: genesys__gen__environment_keyframe
        0x64_56_94_63: genesys__gen__environment_keyframe__light_rig
        0x2f_1e_cb_20: genesys__gen__environment_keyframe__fog
        0xcd_a9_f5_19: genesys__gen__environment_keyframe__sky
        0x10_6b_36_d6: genesys__gen__environment_keyframe__clouds
        0x70_f6_15_8c: genesys__gen__environment_keyframe__camera
        0x44_8f_40_d6: genesys__gen__environment_keyframe__vfx
        0xdf_92_d1_a0: genesys__gen__environment_keyframe__mini__dof
        0xfd_e0_27_12: genesys__gen__environment_keyframe__heat_haze
        0xd9_97_08_86: genesys__gen__environment_keyframe__weather
        0x91_d5_29_ca: genesys__gen__environment_timeline
        0x00_42_3f_25: genesys__gen__environment_timeline__timeline_keyframe
        0xf1_2b_e6_48: genesys__gen__light__base
        0xed_c9_d7_11: genesys__gen__light__cone
        0xdd_aa_b8_6b: genesys__gen__mixer_channel
        0xf1_5e_68_36: genesys__gen__mixing_group
        0x5a_94_09_dc: genesys__gen__post_fx_keyframe
        0x24_b3_7b_28: genesys__gen__post_fxstate
        0x0a_5f_40_dc: genesys__gen__sound_distance_falloff
        0x13_80_30_74: genesys__gen__uielement_base__behaviour
        0x6e_fc_a2_93: genesys__gen__uielement_base__effect_constant
        0xf7_d7_ce_ca: genesys__gen__uielement_base__rendering_data
        0x26_3b_cd_cb: genesys__gen__uielement_base__timeline__behaviour
        0xae_66_27_c7: genesys__gen__uielement_base__timeline
        0xe1_90_0e_b0: genesys__gen__uielement_base
        0xf2_eb_70_5d: genesys__gen__uielement__element_stack
        0xbd_4d_ce_fb: genesys__gen__uielement__element_stack__template
        0x65_a4_3a_9b: genesys__gen__uielement__mini_map
        0x83_16_4a_5d: genesys__gen__uielement__main_map
        0x24_e9_85_66: genesys__gen__uielement__mask
        0xe6_5b_60_fd: genesys__gen__uielement__movie_player
        0x52_ab_e0_8b: genesys__gen__uielement__movie_player__dimensions
        0xba_7f_fb_d9: genesys__gen__uielement__prototype_image
        0x40_5b_b1_d7: genesys__gen__uielement__prototype_image__tint_properties
        0x5d_20_64_2f: genesys__gen__uielement__prototype_image__opacity
        0xda_04_88_b3: genesys__gen__uielement__prototype_label
        0xe2_6f_77_c4: genesys__gen__uielement__prototype_label__string
        0xc3_d4_63_2a: genesys__gen__uielement__prototype_label__text_properties
        0xcc_86_ec_f8: genesys__gen__uielement__prototype_scrolling_text
        0xdb_b3_6f_3d: genesys__gen__uielement__prototype_scrolling_text__string
        0xf8_79_f1_b0: genesys__gen__uielement__prototype_scrolling_text__text_properties
        0x17_83_63_05: genesys__gen__uielement__prototype_shape
        0x6e_ab_bc_51: genesys__gen__uielement__scrollable_label
        0x1e_16_9f_cb: genesys__gen__uielement__scrollable_label__string
        0x41_39_54_24: genesys__gen__uielement__scrollable_label__text_properties
        0xa6_74_11_68: genesys__gen__uilayout
        0xd3_a2_8a_a9: genesys__gen__uilayout_instance_params
        0x78_d6_fe_c0: genesys__gen__uimaterial
        0xd8_e0_f9_66: genesys__gen__uitechnique
        0x12_48_17_f4: genesys__gen__light__base__flash_pattern
        0xd6_1a_73_ed: genesys__gen__post_fx_keyframe__bloom
        0x2e_e7_6e_33: rw_math_vpu__vector2
        0xbd_8f_1f_f0: genesys__gen__post_fx_keyframe__vignette
        0xf3_88_bb_fd: genesys__gen__post_fx_keyframe__general
        0x5f_65_e8_33: genesys__gen__post_fx_keyframe__depth_of__field
        0x4e_ef_3c_c8: genesys__gen__post_fx_keyframe__stereo_3d
        0x77_93_f8_32: genesys__gen__post_fxstate__colour_cube_settings
        0xf5_9a_d1_ea: genesys__gen__post_fxstate__value_modifier
        0x6d_19_4c_19: genesys__gen__uilayout_instance_params__transform_components
        0x2f_72_e7_56: genesys__gen__uilayout_instance_params__timeline_parameters
        0x69_49_4f_68: genesys__gen__sequence_item
        0x35_84_25_6f: genesys__gen__wave_sequence_item
        0x88_89_de_f6: genesys__gen__animation_sequence_item
        0xcc_58_ca_7a: genesys__gen__wcsequence_behaviour
        0xb6_da_e6_71: genesys__gen__sequence_item__modulating_double_value
        0x8a_62_3f_1d: genesys__gen__wave_sequence_item__fade
        0xd1_65_21_59: genesys__gen__bus_mixer_channel_sequence_item
        0x02_74_d0_24: genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value
        0x5b_eb_4f_2f: genesys__gen__physics_sequence_item
        0xeb_cf_86_b0: genesys__gen__physics_sequence_item__physics_double_value
        0xf2_75_9c_88: genesys__gen__sequence_timeline_controller
        0xfc_f0_5f_e9: genesys__gen__sequence
        0x06_e6_a5_18: genesys__gen__jump_timeline_controller
        0xab_95_3f_0c: genesys__gen__layout_sequence_item
        0x99_cb_68_36: genesys__gen__post_fxsequence_item
        0x34_eb_fc_7e: genesys__gen__weapon_upgrade
        0x4c_93_b8_27: genesys__gen__silent_launch_weapon_upgrade
        0x62_e1_8b_c6: genesys__gen__extra_ammo_weapon_upgrade
        0xf3_e9_59_fe: genesys__gen__arc_light_cone_upgrade
        0x55_f0_51_e3: genesys__gen__spike_strip_body_blow_upgrade
        0x02_75_06_f3: genesys__gen__spike_strip_blowout_upgrade
        0x8a_c1_4c_bb: genesys__gen__dust_storm_minimap_upgrade
        0xe8_37_d4_2c: genesys__gen__hypox_particles_weapon_upgrade
        0xdb_46_7b_91: genesys__gen__vfx_spot_effect_sequence_item
        0xff_33_3d_e7: genesys__gen__add_behaviour_sequence_item
        0x08_37_f3_16: genesys__gen__hud_style_sequence_item
        0xb8_93_80_28: genesys__gen__apply_vehicle_kick_sequence_item
        0xd5_69_9b_70: genesys__gen__camera_gameplay_shake_effect
        0x48_b8_4c_b2: genesys__gen__camera_gameplay_shake_effect__rotation
        0x33_a1_3e_49: genesys__gen__camera_gameplay_shake_effect__translation
        0xd9_b1_e6_09: genesys__gen__camera_gameplay_shake_effect__rotation__axis_params
        0xd2_62_d8_63: genesys__gen__camera_gameplay_shake_effect__translation__axis_params
        0xdb_d6_17_c8: genesys__gen__weapon
        0x65_70_9e_b3: genesys__gen__weapon_list
        0x5e_bd_8a_23: genesys__gen__spike_strip_weapon
        0xc4_d9_ad_a2: genesys__gen__smoke_screen_weapon
        0xc9_40_c8_d7: genesys__gen__flash_headlights_weapon
        0x3f_0e_3e_55: genesys__gen__uicolour
        0x0b_10_18_a7: rw__rgba
        0x5c_d0_42_36: genesys__gen__camera_shake_sequence_item
        0x96_2d_e0_bf: genesys__gen__event_trigger_sequence_item
        0xdb_db_1a_8e: genesys__gen__weapon_recharge_data
        0x85_39_5f_b3: genesys__gen__mixer_channel__priority
        0x9e_30_79_c4: genesys__gen__vision_mode
        0x4d_bc_1e_69: genesys__gen__thermal_vision_mode
        0x88_b4_c0_6b: genesys__gen__environment_timeline_sequence_item
        0x5e_5f_4f_4f: genesys__gen__set_vision_mode_type_sequence_item
        0xa2_34_48_a0: genesys__gen__thermal_vision_mode_properties
        0xec_6f_ce_1d: genesys__gen__fast_launch_weapon_upgrade
        0xec_fa_af_14: genesys__gen__light__point
        0x98_74_e1_8d: genesys__gen__searchlight_behaviour
        0x77_94_0e_7d: genesys__gen__text_style
        0x16_9e_0b_3d: genesys__gen__text_style__text_style_locale
        0x5d_5a_65_e9: genesys__gen__wchide_behaviour
        0x20_01_b3_25: genesys__gen__wcpath_animation_behaviour
        0xf7_66_51_79: genesys__gen__wcpath_animation_behaviour__animation_path
        0xe7_1e_b5_01: genesys__gen__snap_to_world_behaviour
        0x37_71_e2_77: genesys__gen__physical_explosion__non_race_car_explosion
        0xc5_95_72_2d: genesys__gen__physical_explosion__race_car_on_ground_explosion
        0x78_d4_44_fd: genesys__gen__physical_explosion__race_car_in_air_explosion
        0x91_95_42_fe: genesys__gen__physical_explosion__gameplay_explosion
        0x51_3e_35_2b: genesys__gen__mine_weapon
        0x6c_78_4f_9c: genesys__gen__physical_explosion
        0x6e_d8_9d_70: genesys__gen__teflon_slick_weapon
        0xa0_2c_67_4c: genesys__gen__grenade_weapon
        0x84_75_cc_83: genesys__gen__flash_bang_weapon
        0xc5_3b_cf_df: genesys__gen__jammer_weapon
        0xd3_7f_ea_f5: genesys__gen__speedbreaker_weapon
        0x93_42_b9_84: genesys__gen__slow_mo_sequence_item
        0xc7_16_7c_f0: genesys__gen__helicopter_weapon
enums:
  e_00_00_2e_a1:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
    "5": ev5
  e_00_09_37_a3:
    "0": default
    "1": helicopter
  e_00_05_f7_0e:
    "0": time
    "1": score
  e_0c_96_6a_95:
    "0": ev0
    "1": ev1
    "2": both
    "3": ev3
    "4": online
  e_00_00_2f_c8:
    "0": ev0
    "1": dlc1
    "2": ev2
    "3": ev3
  e_00_00_2f_d0:
    "0": ev0
    "1": online
    "2": ev2
    "3": ev3
  e_00_04_5f_b1:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
  e_00_05_f3_93:
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
  e_00_05_f6_43:
    "0": default
    "1": waiting
    "2": patrolling
    "3": escaping
    "4": chasing
    "5": waiting__lights
    "6": idle__lights
    "7": rhino
  e_00_06_cc_72:
    "0": play__once
    "1": ev1
    "2": ev2
  e_00_06_cc_77:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
  e_00_06_fa_70:
    "0": none
  e_00_06_fa_71:
    "0": none
  e_00_06_fa_8a:
    "0": none
  e_00_09_37_93:
    "0": ev0
    "1": ev1
  e_34_26_5a_75:
    "0": none
    "1": random
    "2": ev2
    "3": ev3
  e_8e_7d_5f_21:
    "0": none
    "1": random
    "2": ev2
    "3": ev3
  e_c9_7e_aa_da:
    "0": ev0
    "1": ev1
    "2": ev2
  e_da_dc_9b_17:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
    "7": ev7
    "8": ev8
  e_35_d6_2d_64:
    "0": fade
    "1": move
    "2": ev2
    "3": ev3
    "4": scale
    "5": ev5
    "6": ev6
    "7": ev7
    "8": ev8
    "9": ev9
    "10": ev10
    "11": ev11
    "12": ev12
    "13": tint
    "14": ev14
    "15": ev15
    "16": ev16
    "17": ev17
    "18": ev18
  e_5b_33_21_f5:
    "0": none
    "1": ev1
    "2": ev2
    "3": ev3
  e_05_89_a9_77:
    "0": fade
    "1": move
    "2": ev2
    "3": ev3
    "4": scale
    "5": ev5
    "6": ev6
    "7": ev7
    "8": ev8
    "9": ev9
    "10": ev10
    "11": ev11
    "12": ev12
    "13": tint
    "14": ev14
    "15": ev15
    "16": ev16
    "17": ev17
    "18": ev18
  e_d0_00_70_01:
    "0": none
    "1": ev1
    "2": ev2
    "3": ev3
  e_06_a9_64_cd:
    "0": ev0
    "1": vertical
  e_70_f4_bb_e0:
    "0": left
    "1": ev1
    "2": ev2
    "3": full
  e_f7_ff_d1_f8:
    "0": left
    "1": ev1
    "2": ev2
    "3": full
  e_d7_b2_21_da:
    "0": ev0
    "1": ev1
    "2": ev2
  e_96_c1_53_69:
    "0": ev0
    "1": ev1
    "2": ev2
  e_40_99_f3_ac:
    "0": ev0
    "1": vertical
  e_35_a6_06_1e:
    "0": left
    "1": ev1
    "2": ev2
    "3": full
  e_00_00_2f_f0:
    "0": none
    "1": ev1
    "2": ev2
    "3": ev3
  e_00_00_30_1d:
    "0": near
    "1": mid
    "2": far
    "3": ev3
  e_00_00_30_22:
    "0": none
    "1": low
    "2": normal
    "3": extreme
  e_00_00_30_27:
    "0": none
    "1": engine
    "2": skid
    "3": player
    "4": competitor
    "5": traffic
    "6": ui
  e_00_00_30_35:
    "0": ev0
    "1": high_cost
  e_00_00_30_38:
    "0": invalid
    "1": match
    "2": linear
    "3": exponential
  e_00_00_30_3d:
    "0": none
    "1": power
    "2": multiply
  e_00_00_31_b6:
    "0": ev0
    "1": ev1
    "2": ev2
  e_00_00_31_ba:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
    "7": ev7
    "8": ev8
  e_00_00_31_c4:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
    "4": ev4
    "5": ev5
  e_00_00_31_ca:
    "0": ev0
    "1": translation
    "2": rotation
    "3": scale
  e_00_00_31_d2:
    "0": ev0
    "1": ev1
    "2": ev2
  e_00_03_f3_c4:
    "0": loaded
    "1": streamed
    "2": ev2
    "3": decay_exceptionally
    "4": ev4
  e_00_03_f6_5b:
    "0": multiply
    "1": offset
    "2": absolute
  e_00_03_f6_83:
    "0": time
    "1": binding
  e_00_03_f6_d5:
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
  e_00_03_f7_15:
    "0": nickname_violation
    "1": ev1
    "2": drag
    "3": engine__load
    "4": throttle
  e_00_03_f8_50:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
  e_00_04_5e_f1:
    "0": ev0
    "1": ev1
    "2": ev2
    "3": ev3
  e_00_04_5f_ad:
    "0": ev0
    "1": ev1
  e_00_04_63_4a:
    "0": deducted__shield
    "1": ev1
  e_00_05_ab_65:
    "0": ev0
    "1": default
    "2": ev2
    "3": ev3
    "4": xray
    "5": ev5
  e_00_06_cc_2f:
    "0": ev0
    "1": ev1
  e_00_07_33_ee:
    "0": source
    "1": ev1
    "2": perceives_several
    "3": ev3
    "4": ev4
    "5": ev5
    "6": ev6
  e_00_07_57_09:
    "0": ev0
    "1": ev1
  e_00_07_bc_8a:
    "0": none
    "1": ev1
  e_a7_6d_0e_28:
    "0": none
    "1": ev1
    "2": bold
    "3": ev3
    "4": ev4
    "5": ev5
    "6": glow
    "7": ev7
  e_95_95_0d_30:
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
types:
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
        if: ofs_arr_buffer_0x0 != 0
        size: array_count_for_0x0
      size:
        value: 8
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
  bool8_t:
    seq: []
    instances: {}
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
    instances:
      size:
        value: 100
      mu_version_hash:
        value: 0x9c_cd_d1_68
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
        value: 92
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
        value: 92
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
        value: 92
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
        value: 88
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
      - id: ptr_arr_convex_hull_volumes_0xb4
        type: u4
      - id: ptr_arr_cylinder_volumes_0xb8
        type: u4
      - id: ptr_arr_sphere_volumes_0xbc
        type: u4
      - id: array_count_for_0xac
        type: u2
        doc: '"BoxVolumesCount"'
      - id: array_count_for_0xb0
        type: u2
        doc: '"CapsuleVolumesCount"'
      - id: array_count_for_0xb4
        type: u2
        doc: '"ConvexHullVolumesCount"'
      - id: array_count_for_0xb8
        type: u2
        doc: '"CylinderVolumesCount"'
      - id: array_count_for_0xbc
        type: u2
        doc: '"SphereVolumesCount"'
      - id: array_count_for_0x90
        type: u2
        doc: '"SymmetricalInAxisCount"'
      - id: is_wheel_0xcc
        type: u1
      - id: padding
        size: 3
    instances:
      inst_symmetrical_in_axis_0x90:
        pos: ptr_arr_symmetrical_in_axis_0x90
        type: u1
        if: ptr_arr_symmetrical_in_axis_0x90 != 0
        repeat: expr
        repeat-expr: array_count_for_0x90
      inst_box_volumes_0xac:
        pos: ptr_arr_box_volumes_0xac
        type: genesys__gen__physical_definition__rigid_body__box_volume
        if: ptr_arr_box_volumes_0xac != 0
        repeat: expr
        repeat-expr: array_count_for_0xac
      inst_capsule_volumes_0xb0:
        pos: ptr_arr_capsule_volumes_0xb0
        type: genesys__gen__physical_definition__rigid_body__capsule_volume
        if: ptr_arr_capsule_volumes_0xb0 != 0
        repeat: expr
        repeat-expr: array_count_for_0xb0
      inst_convex_hull_volumes_0xb4:
        pos: ptr_arr_convex_hull_volumes_0xb4
        type: genesys__gen__physical_definition__rigid_body__convex_hull_volume
        if: ptr_arr_convex_hull_volumes_0xb4 != 0
        repeat: expr
        repeat-expr: array_count_for_0xb4
      inst_cylinder_volumes_0xb8:
        pos: ptr_arr_cylinder_volumes_0xb8
        type: genesys__gen__physical_definition__rigid_body__cylinder_volume
        if: ptr_arr_cylinder_volumes_0xb8 != 0
        repeat: expr
        repeat-expr: array_count_for_0xb8
      inst_sphere_volumes_0xbc:
        pos: ptr_arr_sphere_volumes_0xbc
        type: genesys__gen__physical_definition__rigid_body__sphere_volume
        if: ptr_arr_sphere_volumes_0xbc != 0
        repeat: expr
        repeat-expr: array_count_for_0xbc
      size:
        value: 208
      mu_version_hash:
        value: 0x8c_ca_12_b3
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
    instances:
      inst_rigid_bodies_names_0x38:
        pos: ptr_arr_rigid_bodies_names_0x38
        type: string_base
        if: ptr_arr_rigid_bodies_names_0x38 != 0
        repeat: expr
        repeat-expr: array_count_for_0x38
      inst_rigid_bodies_0x40:
        pos: ptr_arr_rigid_bodies_0x40
        type: genesys__gen__physical_definition__rigid_body
        if: ptr_arr_rigid_bodies_0x40 != 0
        repeat: expr
        repeat-expr: array_count_for_0x40
      size:
        value: 80
      mu_version_hash:
        value: 0x92_bf_42_33
  rw_math_vpu__vector3:
    seq:
      - id: arr_inline_elements_0x0
        type: f4
        repeat: expr
        repeat-expr: 3
    instances:
      size:
        value: 4
      mu_version_hash:
        value: 0xa5_f5_99_f3
  float32_t:
    seq: []
    instances: {}
  cgs_resource__handle:
    seq: []
    instances: {}
  rw_math_vpu__matrix44affine:
    seq:
      - id: arr_inline_elements_0x0
        type: rw_math_vpu__vector4
        repeat: expr
        repeat-expr: 4
    instances:
      size:
        value: 4
      mu_version_hash:
        value: 0xb6_8b_60_0e
  rw_math_vpu__vector4:
    seq:
      - id: arr_inline_elements_0x0
        type: f4
        repeat: expr
        repeat-expr: 4
    instances:
      size:
        value: 4
      mu_version_hash:
        value: 0xc2_29_a8_2f
  uint16_t:
    seq: []
    instances: {}
  int32_t:
    seq: []
    instances: {}
  genesys__gen__corona:
    seq:
      - id: base_object
        type: gen_obj
      - id: arr_inline_float32_t_0xc
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: arr_inline_float32_t_0x24
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: arr_inline_float32_t_0x3c
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: game_changer_id_0x54
        type: u4
      - id: max_visible_distance_0x58
        type: f4
      - id: visibility_test_depth_bias_0x5c
        type: f4
      - id: ptr_arr_beams_0x60
        type: u4
        doc: enum; 00_00_32_93_1
      - id: ptr_arr_flares_0x64
        type: u4
        doc: enum; 00_00_32_94_1
      - id: ptr_arr_env_map_glows_0x68
        type: u4
        doc: enum; 00_00_32_91_1
      - id: ptr_arr_glows_0x6c
        type: u4
        doc: enum; 00_00_32_91_1
      - id: ptr_arr_planar_reflection_glows_0x70
        type: u4
        doc: enum; 00_00_32_91_1
      - id: ptr_arr_rear_view_mirror_glows_0x74
        type: u4
        doc: enum; 00_00_32_91_1
      - id: array_count_for_0x60
        type: u2
        doc: '"BeamsCount"'
      - id: array_count_for_0x68
        type: u2
        doc: '"EnvMapGlowsCount"'
      - id: array_count_for_0x64
        type: u2
        doc: '"FlaresCount"'
      - id: array_count_for_0x6c
        type: u2
        doc: '"GlowsCount"'
      - id: array_count_for_0xc
        type: u2
      - id: array_count_for_0x24
        type: u2
      - id: array_count_for_0x70
        type: u2
        doc: '"PlanarReflectionGlowsCount"'
      - id: array_count_for_0x74
        type: u2
        doc: '"RearViewMirrorGlowsCount"'
      - id: array_count_for_0x3c
        type: u2
      - id: padding
        size: 2
    instances:
      inst_beams_0x60:
        pos: ptr_arr_beams_0x60
        type: u4
        if: ptr_arr_beams_0x60 != 0
        repeat: expr
        repeat-expr: array_count_for_0x60
      inst_flares_0x64:
        pos: ptr_arr_flares_0x64
        type: u4
        if: ptr_arr_flares_0x64 != 0
        repeat: expr
        repeat-expr: array_count_for_0x64
      inst_env_map_glows_0x68:
        pos: ptr_arr_env_map_glows_0x68
        type: u4
        if: ptr_arr_env_map_glows_0x68 != 0
        repeat: expr
        repeat-expr: array_count_for_0x68
      inst_glows_0x6c:
        pos: ptr_arr_glows_0x6c
        type: u4
        if: ptr_arr_glows_0x6c != 0
        repeat: expr
        repeat-expr: array_count_for_0x6c
      inst_planar_reflection_glows_0x70:
        pos: ptr_arr_planar_reflection_glows_0x70
        type: u4
        if: ptr_arr_planar_reflection_glows_0x70 != 0
        repeat: expr
        repeat-expr: array_count_for_0x70
      inst_rear_view_mirror_glows_0x74:
        pos: ptr_arr_rear_view_mirror_glows_0x74
        type: u4
        if: ptr_arr_rear_view_mirror_glows_0x74 != 0
        repeat: expr
        repeat-expr: array_count_for_0x74
      size:
        value: 140
      mu_version_hash:
        value: 0xf8_19_e6_79
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
        doc: enum; 00_04_22_99_1
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
        if: ptr_arr_cgs_resource__handle_0x38 != 0
        repeat: expr
        repeat-expr: array_count_for_0x38
      inst_cgs_resource__handle_0x3c:
        pos: ptr_arr_cgs_resource__handle_0x3c
        type: cgs_resource__handle
        if: ptr_arr_cgs_resource__handle_0x3c != 0
        repeat: expr
        repeat-expr: array_count_for_0x3c
      inst_surface__collisions_0x40:
        pos: ptr_arr_surface__collisions_0x40
        type: u4
        if: ptr_arr_surface__collisions_0x40 != 0
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
        doc: enum; 00_00_33_92_1
      - id: ptr_arr_lights_0x44
        type: u4
        doc: enum; 00_00_33_94_1
      - id: unk_enum_0x48
        type: u4
        doc: enum; 00_00_33_93_1
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
      - id: padding
        size: 2
    instances:
      inst_coronas_0x40:
        pos: ptr_arr_coronas_0x40
        type: u4
        if: ptr_arr_coronas_0x40 != 0
        repeat: expr
        repeat-expr: array_count_for_0x40
      inst_lights_0x44:
        pos: ptr_arr_lights_0x44
        type: u4
        if: ptr_arr_lights_0x44 != 0
        repeat: expr
        repeat-expr: array_count_for_0x44
      inst_00_00_33_93_1_0x48:
        pos: unk_enum_0x48
        type: u4
        if: unk_enum_0x48 != 0
        repeat: expr
        repeat-expr: array_count_for_0x48
      size:
        value: 108
      mu_version_hash:
        value: 0x01_f2_27_ad
  t_00_00_2e__a1:
    seq: []
    instances: {}
  genesys__gen__corona__glow:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: arr_inline_float32_t_0x20
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: arr_inline_float32_t_0x38
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: material_0x50
        size: 8
      - id: game_changer_id_0x58
        type: u4
      - id: brightness_0x5c
        type: f4
      - id: depth_bias_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: float32_t_0x68
        type: f4
      - id: rotation_offset_0x6c
        type: f4
      - id: array_count_for_0x20
        type: u2
      - id: array_count_for_0x38
        type: u2
    instances:
      size:
        value: 116
      mu_version_hash:
        value: 0xb9_30_1e_9c
  genesys__gen__corona__env_map_glow:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: arr_inline_float32_t_0x20
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: arr_inline_float32_t_0x38
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: material_0x50
        size: 8
      - id: game_changer_id_0x58
        type: u4
      - id: depth_bias_0x5c
        type: f4
      - id: float32_t_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: rotation_offset_0x68
        type: f4
      - id: array_count_for_0x20
        type: u2
      - id: array_count_for_0x38
        type: u2
    instances:
      size:
        value: 112
      mu_version_hash:
        value: 0xa2_b1_30_07
  genesys__gen__corona__beam:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: arr_inline_float32_t_0x20
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: arr_inline_float32_t_0x38
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: material_0x50
        size: 8
      - id: game_changer_id_0x58
        type: u4
      - id: brightness_0x5c
        type: f4
      - id: depth_bias_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: end_radius_0x68
        type: f4
      - id: float32_t_0x6c
        type: f4
      - id: start_radius_0x70
        type: f4
      - id: array_count_for_0x20
        type: u2
      - id: array_count_for_0x38
        type: u2
    instances:
      size:
        value: 120
      mu_version_hash:
        value: 0xb5_9a_5e_dc
  genesys__gen__corona__flare:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: arr_inline_float32_t_0x20
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: arr_inline_float32_t_0x38
        type: f4
        repeat: expr
        repeat-expr: 6
      - id: material_0x50
        size: 8
      - id: game_changer_id_0x58
        type: u4
      - id: brightness_0x5c
        type: f4
      - id: position_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: float32_t_0x68
        type: f4
      - id: rotation_offset_0x6c
        type: f4
      - id: array_count_for_0x20
        type: u2
      - id: array_count_for_0x38
        type: u2
      - id: bool8_t_0x74
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 120
      mu_version_hash:
        value: 0xad_a5_0d_dc
  genesys__gen__wcvfx_behaviour__coronas:
    seq:
      - id: base_object
        type: gen_obj
      - id: corona_definition_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: locator_group_0x18
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xdf_e3_19_75
  genesys__gen__wcvfx_behaviour__spot_effects:
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
        value: 28
      mu_version_hash:
        value: 0xec_16_af_6a
  genesys__gen__wcvfx_behaviour__lights:
    seq:
      - id: base_object
        type: gen_obj
      - id: light_definition_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: locator_group_0x18
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xcb_b3_7b_5b
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
        if: ptr_arr_rolling__waves_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_scraping__waves_0x18:
        pos: ptr_arr_scraping__waves_0x18
        type: cgs_resource__handle
        if: ptr_arr_scraping__waves_0x18 != 0
        repeat: expr
        repeat-expr: array_count_for_0x18
      inst_waves_0x1c:
        pos: ptr_arr_waves_0x1c
        type: cgs_resource__handle
        if: ptr_arr_waves_0x1c != 0
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 40
      mu_version_hash:
        value: 0xb9_ac_70_67
  genesys__gen__make_physical_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: unk_enum_0x1c
        type: u2
        doc: enum; 00_09_37_a3_1
      - id: collidable_0x1e
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x1c_72_63_08
  genesys__gen__wcremove_world_entity_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x3e_e2_74_05
  genesys__object:
    seq: []
    instances: {}
  int16_t:
    seq: []
    instances: {}
  t_00_09_37__a3:
    seq: []
    instances: {}
  genesys__gen__game_mode:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: hud__hsm_0x14
        size: 8
      - id: description_0x1c
        type: u4
      - id: game_changer_id_0x20
        type: u4
      - id: hsm_0x24
        type: u4
      - id: cgs_core__unique_id_0x28
        type: u4
      - id: mix_snap_shot_0x2c
        type: u4
      - id: name_0x30
        type: u4
      - id: score_view_model_0x34
        type: u4
      - id: weapon_list_0x38
        type: u4
      - id: mode_intro_time_limit_0x3c
        type: f4
      - id: mode_time_limit_0x40
        type: f4
      - id: float32_t_0x44
        type: f4
      - id: unk_enum_0x48
        type: u4
        doc: enum; 00_04_61_35_1
      - id: intercepting_cop_frequency_0x4c
        type: s4
      - id: minimap_distance_0x50
        type: s4
      - id: mode_score_limit_0x54
        type: s4
      - id: oncoming_cop_frequency_0x58
        type: s4
      - id: int32_t_0x5c
        type: s4
      - id: trailing_cop_frequency_0x60
        type: s4
      - id: ranking_type_0x64
        type: u2
        doc: enum; 00_05_f7_0e_1
      - id: array_count_for_0x48
        type: u2
      - id: allow_airacer_damage_from_world_0x68
        type: u1
      - id: allow_friendly_fire_0x69
        type: u1
      - id: host_can_end_game_0x6a
        type: u1
      - id: bool8_t_0x6b
        type: u1
      - id: online_0x6c
        type: u1
      - id: bool8_t_0x6d
        type: u1
      - id: retry_enabled_0x6e
        type: u1
      - id: bool8_t_0x6f
        type: u1
      - id: spawn_towards_ai_0x70
        type: u1
      - id: team_game_0x71
        type: u1
      - id: padding
        size: 2
    instances:
      inst_00_04_61_35_1_0x48:
        pos: unk_enum_0x48
        type: u4
        if: unk_enum_0x48 != 0
        repeat: expr
        repeat-expr: array_count_for_0x48
      size:
        value: 116
      mu_version_hash:
        value: 0x43_d3_4f_71
  genesys__gen__event:
    seq:
      - id: base_object
        type: gen_obj
      - id: ptr_arr_autotest_checkpoints_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: game_mode_0x14
        type: u4
      - id: cycle_time_of_day_0x18
        type: f4
      - id: finish_time_of_day_0x1c
        type: f4
      - id: sun_direction_0x20
        type: f4
      - id: time_of_day_0x24
        type: f4
      - id: array_count_for_0xc
        type: u2
        doc: '"AutotestCheckpointsCount"'
      - id: is_alternative_weather_0x2a
        type: u1
      - id: is_rain_active_0x2b
        type: u1
      - id: is_thunder_active_0x2c
        type: u1
      - id: bool8_t_0x2d
        type: u1
      - id: override_sun_direction_0x2e
        type: u1
      - id: padding
        size: 1
    instances:
      inst_autotest_checkpoints_0xc:
        pos: ptr_arr_autotest_checkpoints_0xc
        type: u4
        if: ptr_arr_autotest_checkpoints_0xc != 0
        repeat: expr
        repeat-expr: array_count_for_0xc
      size:
        value: 48
      mu_version_hash:
        value: 0x69_06_e8_a3
  genesys__gen__online_event:
    seq:
      - id: base_object
        type: genesys__gen__event
      - id: arena_0x30
        type: u4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0xa1_9a_e6_e7
  genesys__gen__event_arena:
    seq:
      - id: base_object
        type: gen_obj
      - id: arena_data_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: image_0x14
        type: u4
      - id: map_0x18
        type: u4
      - id: name_0x1c
        type: u4
      - id: world_0x20
        type: u4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x97_bb_27_7e
  genesys__gen__event_arena_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: loading__point__location_0x10
        type: u4
      - id: ptr_arr_spawn__locations_0x14
        type: u4
      - id: ptr_arr_ptr_chevrons_0x18
        type: u4
        doc: enum; 00_04_62_44_1
      - id: ptr_arr_ptr_custom_chevron_list_0x1c
        type: u4
        doc: enum; 00_06_fa_9f_1
      - id: array_count_for_0x18
        type: u2
        doc: '"ChevronsCount"'
      - id: array_count_for_0x14
        type: u2
        doc: '"Spawn_LocationsCount"'
      - id: array_count_for_0x1c
        type: u1
        doc: '"CustomChevronListCount"'
      - id: padding
        size: 3
    instances:
      inst_spawn__locations_0x14:
        pos: ptr_arr_spawn__locations_0x14
        type: u4
        if: ptr_arr_spawn__locations_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_chevrons_0x18:
        pos: ptr_arr_ptr_chevrons_0x18
        type: ptr('u4')
        if: ptr_arr_ptr_chevrons_0x18 != 0
        repeat: expr
        repeat-expr: array_count_for_0x18
      inst_custom_chevron_list_0x1c:
        pos: ptr_arr_ptr_custom_chevron_list_0x1c
        type: ptr('u4')
        if: ptr_arr_ptr_custom_chevron_list_0x1c != 0
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 40
      mu_version_hash:
        value: 0xae_f6_41_5c
  uint8_t:
    seq: []
    instances: {}
  genesys__gen__score_view_model:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_score_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
        doc: '"ScoreCount"'
      - id: padding
        size: 2
    instances:
      inst_score_0x10:
        pos: ptr_arr_score_0x10
        type: u4
        if: ptr_arr_score_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xd3_97_39_6c
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
        value: 28
      mu_version_hash:
        value: 0x24_2c_b4_ca
  genesys__gen__game_mode__score_override:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: score_0x14
        type: s4
      - id: int32_t_0x18
        type: s4
      - id: xp_0x1c
        type: s4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xe0_51_7c_e1
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
  genesys__gen__offline_event:
    seq:
      - id: base_object
        type: genesys__gen__event
      - id: cgs_core__unique_id_0x30
        type: u4
      - id: cgs_core__unique_id_0x34
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x38
        type: u4
      - id: ptr_arr_checkpoints_0x3c
        type: u4
      - id: ptr_arr_gameplay_triggers_0x40
        type: u4
      - id: intro_0x44
        type: u4
      - id: name_0x48
        type: u4
      - id: next_story_event_0x4c
        type: u4
      - id: deallocated_nodule_0x50
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x54
        type: u4
      - id: cgs_core__unique_id_0x58
        type: u4
      - id: timeline_0x5c
        type: u4
      - id: ptr_arr_float32_t_0x60
        type: u4
      - id: ptr_arr_target_time_0x64
        type: u4
      - id: traffic_density_0x68
        type: f4
      - id: ptr_arr_ptr_aiplayers_0x6c
        type: u4
        doc: enum; 00_06_fa_75_1
      - id: ptr_arr_ptr_chevron_list_0x70
        type: u4
        doc: enum; 00_04_62_44_1
      - id: ptr_arr_ptr_custom_chevron_list_0x74
        type: u4
        doc: enum; 00_06_fa_9f_1
      - id: target_score_0x78
        type: u4
      - id: array_count_for_0x38
        type: u2
      - id: array_count_for_0x3c
        type: u2
        doc: '"CheckpointsCount"'
      - id: array_count_for_0x70
        type: u2
        doc: '"ChevronListCount"'
      - id: array_count_for_0x54
        type: u2
      - id: array_count_for_0x60
        type: u2
      - id: array_count_for_0x64
        type: u2
        doc: '"TargetTimeCount"'
      - id: cop_spawning_0x88
        type: u1
      - id: start_with_engine_on_0x89
        type: u1
      - id: traffic_enabled_0x8a
        type: u1
      - id: array_count_for_0x6c
        type: u1
        doc: '"AIPlayersCount"'
      - id: array_count_for_0x74
        type: u1
        doc: '"CustomChevronListCount"'
      - id: array_count_for_0x40
        type: u1
        doc: '"GameplayTriggersCount"'
      - id: padding
        size: 2
    instances:
      inst_cgs_core__unique_id_0x38:
        pos: ptr_arr_cgs_core__unique_id_0x38
        type: u4
        if: ptr_arr_cgs_core__unique_id_0x38 != 0
        repeat: expr
        repeat-expr: array_count_for_0x38
      inst_checkpoints_0x3c:
        pos: ptr_arr_checkpoints_0x3c
        type: u4
        if: ptr_arr_checkpoints_0x3c != 0
        repeat: expr
        repeat-expr: array_count_for_0x3c
      inst_gameplay_triggers_0x40:
        pos: ptr_arr_gameplay_triggers_0x40
        type: u4
        if: ptr_arr_gameplay_triggers_0x40 != 0
        repeat: expr
        repeat-expr: array_count_for_0x40
      inst_cgs_core__unique_id_0x54:
        pos: ptr_arr_cgs_core__unique_id_0x54
        type: u4
        if: ptr_arr_cgs_core__unique_id_0x54 != 0
        repeat: expr
        repeat-expr: array_count_for_0x54
      inst_float32_t_0x60:
        pos: ptr_arr_float32_t_0x60
        type: f4
        if: ptr_arr_float32_t_0x60 != 0
        repeat: expr
        repeat-expr: array_count_for_0x60
      inst_target_time_0x64:
        pos: ptr_arr_target_time_0x64
        type: f4
        if: ptr_arr_target_time_0x64 != 0
        repeat: expr
        repeat-expr: array_count_for_0x64
      inst_aiplayers_0x6c:
        pos: ptr_arr_ptr_aiplayers_0x6c
        type: ptr('u4')
        if: ptr_arr_ptr_aiplayers_0x6c != 0
        repeat: expr
        repeat-expr: array_count_for_0x6c
      inst_chevron_list_0x70:
        pos: ptr_arr_ptr_chevron_list_0x70
        type: ptr('u4')
        if: ptr_arr_ptr_chevron_list_0x70 != 0
        repeat: expr
        repeat-expr: array_count_for_0x70
      inst_custom_chevron_list_0x74:
        pos: ptr_arr_ptr_custom_chevron_list_0x74
        type: ptr('u4')
        if: ptr_arr_ptr_custom_chevron_list_0x74 != 0
        repeat: expr
        repeat-expr: array_count_for_0x74
      size:
        value: 144
      mu_version_hash:
        value: 0x1e_06_6a_b1
  t_00_05__f7_0e:
    seq: []
    instances: {}
  genesys__gen__aiplayer_instance:
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
        value: 24
      mu_version_hash:
        value: 0xa5_6a_24_27
  genesys__gen__offline_event__custom_chevrons:
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
      - id: padding
        size: 2
    instances:
      inst_float32_t_0x10:
        pos: ptr_arr_float32_t_0x10
        type: f4
        if: ptr_arr_float32_t_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_float32_t_0x14:
        pos: ptr_arr_float32_t_0x14
        type: f4
        if: ptr_arr_float32_t_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_float32_t_0x18:
        pos: ptr_arr_float32_t_0x18
        type: f4
        if: ptr_arr_float32_t_0x18 != 0
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 36
      mu_version_hash:
        value: 0x66_9e_7a_1d
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
        if: ptr_arr_float32_t_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      inst_float32_t_0x14:
        pos: ptr_arr_float32_t_0x14
        type: f4
        if: ptr_arr_float32_t_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      inst_float32_t_0x18:
        pos: ptr_arr_float32_t_0x18
        type: f4
        if: ptr_arr_float32_t_0x18 != 0
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 36
      mu_version_hash:
        value: 0xac_a9_15_3e
  gen_obj:
    seq:
      - id: dynamic_gamedata
        size: 8
      - id: mu_type_version
        type: u4le
    instances: {}
  ff__ff__ff__f8:
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
        type: ptr('generic_gen_object')
        if: ptr_arr_ptr_item_0x10 != 0
        doc: "'instance of Genesys.Object'"
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xbc_85_5d_7f
  genesys__gen__car_select_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: cop_idle_sequences_0xc
        type: u1
        doc: enum; 00_00_32_82_1
      - id: cop_sequences_0x28
        type: u1
        doc: enum; 00_00_32_82_1
      - id: racer_idle_sequences_0x44
        type: u1
        doc: enum; 00_00_32_82_1
      - id: racer_sequences_0x60
        type: u1
        doc: enum; 00_00_32_82_1
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
        if: ptr_arr_cop_placements_0x7c != 0
        repeat: expr
        repeat-expr: array_count_for_0x7c
      inst_racer_placements_0x84:
        pos: ptr_arr_racer_placements_0x84
        type: u4
        if: ptr_arr_racer_placements_0x84 != 0
        repeat: expr
        repeat-expr: array_count_for_0x84
      size:
        value: 152
      mu_version_hash:
        value: 0xee_73_7c_02
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
        if: ptr_arr_ordered_list_0x10 != 0
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
      - id: arr_inline_position_0xc
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
        value: 68
      mu_version_hash:
        value: 0xe9_6b_72_79
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
      - id: show_pack_on_entitlement_0x20
        type: u4
      - id: release_0x24
        type: u4
        doc: enum; 00_00_2f_c8_1
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xd4_53_06_9d
  genesys__gen__gameplay_milestone:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: message_0x10
        type: u4
      - id: ptr_arr_entries_0x14
        type: u4
        doc: enum; 00_00_32_cf_1
      - id: type_0x18
        type: u2
        doc: enum; 00_00_2f_d0_1
      - id: array_count_for_0x14
        type: u2
        doc: '"EntriesCount"'
      - id: bool8_t_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      inst_entries_0x14:
        pos: ptr_arr_entries_0x14
        type: u4
        if: ptr_arr_entries_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 32
      mu_version_hash:
        value: 0x83_b0_e4_19
  genesys__gen__game_rank:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: rank__name_0x10
        type: u4
      - id: cgs_core__unique_id_0x14
        type: u4
      - id: rank__number_0x18
        type: s4
      - id: bool8_t_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x70_1e_13_71
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
      - id: cgs_core__unique_id_0x20
        type: u4
      - id: game_changer_id_0x24
        type: u4
      - id: ptr_arr_image_0x28
        type: u4
      - id: unk_enum_0x2c
        type: u4
        doc: enum; 00_00_28_21_1_1
      - id: unk_enum_0x30
        type: u4
        doc: enum; 00_00_28_21_1_2
      - id: bounty__required_0x34
        type: s4
      - id: progression__type_0x38
        type: u2
        doc: enum; 0c_96_6a_95
      - id: array_count_for_0x2c
        type: u2
      - id: array_count_for_0x28
        type: u2
      - id: array_count_for_0x30
        type: u2
      - id: is_enabled_0x40
        type: u1
      - id: padding
        size: 3
    instances:
      inst_image_0x28:
        pos: ptr_arr_image_0x28
        type: u4
        if: ptr_arr_image_0x28 != 0
        repeat: expr
        repeat-expr: array_count_for_0x28
      inst_00_00_28_21_1_1_0x2c:
        pos: unk_enum_0x2c
        type: u4
        if: unk_enum_0x2c != 0
        repeat: expr
        repeat-expr: array_count_for_0x2c
      inst_00_00_28_21_1_2_0x30:
        pos: unk_enum_0x30
        type: u4
        if: unk_enum_0x30 != 0
        repeat: expr
        repeat-expr: array_count_for_0x30
      size:
        value: 68
      mu_version_hash:
        value: 0x97_40_43_c6
  t_0c_96_6a_95:
    seq: []
    instances: {}
  genesys__gen__game_unlock__event:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0x52_00_dc_f4
  genesys__gen__game_unlock__milestone:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: int32_t_0x14
        type: s4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x48_7f_29_ad
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
        type: ptr('generic_gen_object')
        if: ptr_arr_ptr_item_0x10 != 0
        doc: "'instance of Genesys.Object'"
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x2c_04_42_9d
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
        value: 24
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
        if: ptr_arr_nucleus_tag_0x10 != 0
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
        doc: enum; 00_00_33_09_1
      - id: array_count_for_0x10
        type: u2
        doc: '"ItemsCount"'
      - id: padding
        size: 2
    instances:
      inst_items_0x10:
        pos: ptr_arr_items_0x10
        type: u4
        if: ptr_arr_items_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x3a_26_00_0e
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
      - id: primary_layer_0x18
        type: u4
      - id: layer_distance_0x1c
        type: f4
      - id: array_count_for_0xc
        type: u2
        doc: '"BackLayersCount"'
      - id: array_count_for_0x10
        type: u2
        doc: '"FrontLayersCount"'
    instances:
      inst_back_layers_0xc:
        pos: ptr_arr_back_layers_0xc
        type: u4
        if: ptr_arr_back_layers_0xc != 0
        repeat: expr
        repeat-expr: array_count_for_0xc
      inst_front_layers_0x10:
        pos: ptr_arr_front_layers_0x10
        type: u4
        if: ptr_arr_front_layers_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 36
      mu_version_hash:
        value: 0xb0_09_2b_8e
  genesys__gen__road_block_layer:
    seq:
      - id: base_object
        type: gen_obj
      - id: middle_item_0xc
        type: u1
        doc: enum; 00_00_33_2a_1
      - id: game_changer_id_0x24
        type: u4
      - id: distance_0x28
        type: f4
      - id: first_distance_0x2c
        type: f4
      - id: ptr_arr_left_items_0x30
        type: u4
        doc: enum; 00_00_33_2a_1
      - id: ptr_arr_right_items_0x34
        type: u4
        doc: enum; 00_00_33_2a_1
      - id: array_count_for_0x30
        type: u2
      - id: array_count_for_0x34
        type: u2
    instances:
      inst_left_items_0x30:
        pos: ptr_arr_left_items_0x30
        type: u4
        if: ptr_arr_left_items_0x30 != 0
        repeat: expr
        repeat-expr: array_count_for_0x30
      inst_right_items_0x34:
        pos: ptr_arr_right_items_0x34
        type: u4
        if: ptr_arr_right_items_0x34 != 0
        repeat: expr
        repeat-expr: array_count_for_0x34
      size:
        value: 60
      mu_version_hash:
        value: 0x65_03_e6_7a
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
        type: s4
      - id: x360offer_id_0x44
        type: s4
      - id: array_count_for_0x3c
        type: u2
        doc: '"EntitlementsCount"'
      - id: array_count_for_0x28
        type: u2
        doc: '"Long_DescriptionCount"'
      - id: show__in__store_0x4c
        type: u1
      - id: padding
        size: 3
    instances:
      inst_long__description_0x28:
        pos: ptr_arr_long__description_0x28
        type: u4
        if: ptr_arr_long__description_0x28 != 0
        repeat: expr
        repeat-expr: array_count_for_0x28
      inst_entitlements_0x3c:
        pos: ptr_arr_entitlements_0x3c
        type: cgs_resource__handle
        if: ptr_arr_entitlements_0x3c != 0
        repeat: expr
        repeat-expr: array_count_for_0x3c
      size:
        value: 80
      mu_version_hash:
        value: 0xaf_b3_ae_aa
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
        if: ptr_arr_content_items_0x18 != 0
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
        if: ptr_arr_store_packs_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xd4_f9_60_f2
  genesys__gen__thankyou_mapping:
    seq:
      - id: base_object
        type: gen_obj
      - id: nucleus_entitlement_0xc
        size: 8
      - id: thankyou_item_0x14
        size: 8
      - id: game_changer_id_0x1c
        type: u4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x63_9c_ba_fd
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
        value: 28
      mu_version_hash:
        value: 0x99_b7_15_31
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
  t_00_00_2f__c8:
    seq: []
    instances: {}
  t_00_00_2f__d0:
    seq: []
    instances: {}
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
        if: ptr_arr_sequences_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 28
      mu_version_hash:
        value: 0x63_78_a7_1f
  genesys__gen__gameplay_milestone__entry:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: int32_t_0x10
        type: s4
      - id: value_0x14
        type: s4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x6e_2f_b0_1d
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
        if: ptr_arr_entitlement_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 28
      mu_version_hash:
        value: 0xfe_1c_ee_ea
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
        value: 24
      mu_version_hash:
        value: 0xa7_64_a6_e7
  genesys__gen__upgrade_package:
    seq:
      - id: base_object
        type: gen_obj
      - id: description_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: image_0x14
        type: u4
      - id: name_0x18
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xd8_80_1e_64
  genesys__gen__device_grant_upgrade_package:
    seq:
      - id: base_object
        type: genesys__gen__upgrade_package
      - id: cgs_core__unique_id_0x1c
        type: u4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xfd_42_7b_87
  genesys__gen__performance_upgrade_package:
    seq:
      - id: base_object
        type: genesys__gen__upgrade_package
      - id: cgs_core__unique_id_0x1c
        type: u4
      - id: float32_t_0x20
        type: f4
      - id: unk_enum_0x24
        type: u4
        doc: enum; 00_04_5f_b1_1
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x20_91_91_f5
  t_00_04_5f__b1:
    seq: []
    instances: {}
  genesys__gen__rollout:
    seq:
      - id: base_object
        type: gen_obj
      - id: arr_inline_weapon_data_0xc
        type: u1
        repeat: expr
        repeat-expr: 2
        doc: enum; 00_04_64_5e_1
      - id: game_changer_id_0x44
        type: u4
      - id: name_0x48
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x4c
        type: u4
      - id: cgs_core__unique_id_0x50
        type: u4
      - id: vehicle_0x54
        type: u4
      - id: array_count_for_0x4c
        type: u2
      - id: array_count_for_0xc
        type: u2
      - id: is_online_rollout_0x5c
        type: u1
      - id: is_player_rollout_0x5d
        type: u1
      - id: padding
        size: 2
    instances:
      inst_cgs_core__unique_id_0x4c:
        pos: ptr_arr_cgs_core__unique_id_0x4c
        type: u4
        if: ptr_arr_cgs_core__unique_id_0x4c != 0
        repeat: expr
        repeat-expr: array_count_for_0x4c
      size:
        value: 96
      mu_version_hash:
        value: 0xdb_ad_40_b1
  genesys__gen__perk:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x10
        type: u4
      - id: array_count_for_0x10
        type: u1
      - id: padding
        size: 3
    instances:
      inst_cgs_resource__handle_0x10:
        pos: ptr_arr_cgs_resource__handle_0x10
        type: cgs_resource__handle
        if: ptr_arr_cgs_resource__handle_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x32_00_82_dd
  genesys__gen__perk_level:
    seq:
      - id: base_object
        type: gen_obj
      - id: description_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: image_0x14
        type: u4
      - id: name_0x18
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x1c
        type: u4
      - id: array_count_for_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      inst_cgs_resource__handle_0x1c:
        pos: ptr_arr_cgs_resource__handle_0x1c
        type: cgs_resource__handle
        if: ptr_arr_cgs_resource__handle_0x1c != 0
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 36
      mu_version_hash:
        value: 0x6d_ae_98_7f
  genesys__gen__game_rule:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
    instances:
      size:
        value: 16
      mu_version_hash:
        value: 0x1d_72_6a_04
  genesys__gen__nitrous_earning_game_rule:
    seq:
      - id: base_object
        type: genesys__gen__game_rule
      - id: float32_t_0x10
        type: f4
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0x8c_91_2b_55
  genesys__gen__nitrous_burning_game_rule:
    seq:
      - id: base_object
        type: genesys__gen__game_rule
      - id: float32_t_0x10
        type: f4
    instances:
      size:
        value: 20
      mu_version_hash:
        value: 0xd0_c3_9c_8b
  genesys__gen__impact_protection_game_rule:
    seq:
      - id: base_object
        type: genesys__gen__game_rule
      - id: back_0x10
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
      - id: left_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
    instances:
      size:
        value: 56
      mu_version_hash:
        value: 0xee_0a_cb_16
  genesys__gen__impact_damage_game_rule:
    seq:
      - id: base_object
        type: genesys__gen__game_rule
      - id: back_0x10
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
      - id: left_0x2c
        type: f4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
    instances:
      size:
        value: 56
      mu_version_hash:
        value: 0x1a_0d_be_44
  genesys__gen__rollout__weapon_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: weapon_0x10
        type: u4
      - id: ptr_arr_weapon_upgrades_0x14
        type: u4
      - id: array_count_for_0x14
        type: u2
        doc: '"WeaponUpgradesCount"'
      - id: padding
        size: 2
    instances:
      inst_weapon_upgrades_0x14:
        pos: ptr_arr_weapon_upgrades_0x14
        type: u4
        if: ptr_arr_weapon_upgrades_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 28
      mu_version_hash:
        value: 0xc9_d9_31_4f
  genesys__gen__scoring_action:
    seq:
      - id: base_object
        type: gen_obj
      - id: predicate_0xc
        type: string_base
      - id: ptr_arr_cgs_core__unique_id_0x14
        type: u4
      - id: description_0x18
        type: u4
      - id: game_changer_id_0x1c
        type: u4
      - id: gameplay_trigger_0x20
        type: u4
      - id: cgs_core__unique_id_0x24
        type: u4
      - id: sequence_0x28
        type: u4
      - id: cgs_core__unique_id_0x2c
        type: u4
      - id: title_0x30
        type: u4
      - id: int32_t_0x34
        type: s4
      - id: heat_0x38
        type: s4
      - id: priority_0x3c
        type: s4
      - id: score_0x40
        type: s4
      - id: xp_0x44
        type: s4
      - id: queue_0x48
        type: u2
        doc: enum; 00_09_37_93_1
      - id: array_count_for_0x14
        type: u2
      - id: feedback_deferrable_0x4c
        type: u1
      - id: online_0x4d
        type: u1
      - id: padding
        size: 2
    instances:
      inst_cgs_core__unique_id_0x14:
        pos: ptr_arr_cgs_core__unique_id_0x14
        type: u4
        if: ptr_arr_cgs_core__unique_id_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 80
      mu_version_hash:
        value: 0x86_49_8f_4e
  t_00_05__f3_93:
    seq: []
    instances: {}
  genesys__gen__heat_level:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: aim_for_payload_time_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: cop_hearing_range_for_idle_player_0x1c
        type: f4
      - id: cop_hearing_range_for_moving_player_0x20
        type: f4
      - id: cop_sight_cone_angle_when_alert_0x24
        type: f4
      - id: cop_sight_cone_angle_when_idle_0x28
        type: f4
      - id: cop_sight_range_when_alert_0x2c
        type: f4
      - id: cop_sight_range_when_chasing_0x30
        type: f4
      - id: cop_sight_range_when_idle_0x34
        type: f4
      - id: float32_t_0x38
        type: f4
      - id: unk_enum_0x3c
        type: u4
        doc: enum; 00_06_fc_f9_1
      - id: threshold_0x40
        type: u4
      - id: ptr_arr_formation_ahead_0x44
        type: u4
      - id: ptr_arr_formation_behind_0x48
        type: u4
      - id: array_count_for_0x3c
        type: u2
      - id: array_count_for_0x44
        type: u2
        doc: '"FormationAheadCount"'
      - id: array_count_for_0x48
        type: u2
        doc: '"FormationBehindCount"'
      - id: allow_cooldown_0x52
        type: u1
      - id: force_cooldown_0x53
        type: u1
      - id: aim_for_payload_angle_0x54
        type: u1
      - id: display_number_0x55
        type: u1
      - id: uint8_t_0x56
        type: u1
      - id: uint8_t_0x57
        type: u1
      - id: uint8_t_0x58
        type: u1
      - id: uint8_t_0x59
        type: u1
      - id: uint8_t_0x5a
        type: u1
      - id: uint8_t_0x5b
        type: u1
    instances:
      inst_00_06_fc_f9_1_0x3c:
        pos: unk_enum_0x3c
        type: u4
        if: unk_enum_0x3c != 0
        repeat: expr
        repeat-expr: array_count_for_0x3c
      inst_formation_ahead_0x44:
        pos: ptr_arr_formation_ahead_0x44
        type: u1
        if: ptr_arr_formation_ahead_0x44 != 0
        repeat: expr
        repeat-expr: array_count_for_0x44
      inst_formation_behind_0x48:
        pos: ptr_arr_formation_behind_0x48
        type: u1
        if: ptr_arr_formation_behind_0x48 != 0
        repeat: expr
        repeat-expr: array_count_for_0x48
      size:
        value: 92
      mu_version_hash:
        value: 0x88_49_d6_4a
  t_00_05__f6_43:
    seq: []
    instances: {}
  t_00_06__cc_72:
    seq: []
    instances: {}
  genesys__gen__gameplay_trigger__output__sequence_output:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: sequence_0x10
        type: u4
      - id: sequence_type_0x14
        type: u4
        doc: enum; 00_06_cc_77_1
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xbd_37_77_79
  t_00_06__cc_77:
    seq: []
    instances: {}
  genesys__gen__aiplayer_type:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: rollout_0x10
        type: u4
      - id: aggression_delay_0x14
        type: f4
      - id: aggression_frequency_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: escaping_speed_0x20
        type: f4
      - id: fail_jump_daze_time_0x24
        type: f4
      - id: flat_out_initial_time_0x28
        type: f4
      - id: flat_out_time_0x2c
        type: f4
      - id: hit_damage_percentage_to_daze_0x30
        type: f4
      - id: hit_daze_time_0x34
        type: f4
      - id: max_damage_for_speed_effect_0x38
        type: f4
      - id: max_event_balancing_distance_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: min_damage_for_speed_effect_0x44
        type: f4
      - id: min_event_balancing_distance_0x48
        type: f4
      - id: min_shortcut_time_0x4c
        type: f4
      - id: min_throttle_damage_percent_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: shortcut_taking_percentage_0x58
        type: f4
      - id: speed_0x5c
        type: f4
      - id: speed_matching_max_distance_0x60
        type: f4
      - id: speed_matching_max_speed_0x64
        type: f4
      - id: speed_matching_min_speed_0x68
        type: f4
      - id: speed_matching_speed_difference_0x6c
        type: f4
      - id: toughness_0x70
        type: f4
      - id: turn_at_junction_percentage_0x74
        type: f4
      - id: uturn_min_time_0x78
        type: f4
      - id: weapon_avoidance_percentage_0x7c
        type: f4
      - id: weaving_duration_0x80
        type: f4
      - id: weaving_frequency_0x84
        type: f4
      - id: aggression_type_0x88
        type: u2
        doc: enum; 00_06_fa_71_1
      - id: behaviour_0x8a
        type: u2
        doc: enum; 00_05_f6_43_1
      - id: nitrous_usage_0x8c
        type: u2
        doc: enum; 00_06_fa_8a_1
      - id: weaving_type_0x8e
        type: u2
        doc: enum; 00_06_fa_70_1
      - id: can_rhino_0x90
        type: u1
      - id: do_uturns_0x91
        type: u1
      - id: is_cop_0x92
        type: u1
      - id: padding
        size: 1
    instances:
      size:
        value: 148
      mu_version_hash:
        value: 0x80_52_29_7f
  t_00_06__fa_70:
    seq: []
    instances: {}
  t_00_06__fa_71:
    seq: []
    instances: {}
  t_00_06__fa_8a:
    seq: []
    instances: {}
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
        doc: enum; 00_06_fb_3b_1
      - id: ptr_arr_output_0x20
        type: u4
        doc: enum; 00_06_fb_3c_1
      - id: trigger_lifetime_0x24
        type: u2
        doc: enum; 00_06_cc_72_1
      - id: array_count_for_0x1c
        type: u2
        doc: '"InputCount"'
      - id: array_count_for_0x20
        type: u2
        doc: '"OutputCount"'
      - id: add_to_mini_map_0x2a
        type: u1
      - id: padding
        size: 1
    instances:
      inst_input_0x1c:
        pos: ptr_arr_input_0x1c
        type: u4
        if: ptr_arr_input_0x1c != 0
        repeat: expr
        repeat-expr: array_count_for_0x1c
      inst_output_0x20:
        pos: ptr_arr_output_0x20
        type: u4
        if: ptr_arr_output_0x20 != 0
        repeat: expr
        repeat-expr: array_count_for_0x20
      size:
        value: 44
      mu_version_hash:
        value: 0x24_2c_7a_43
  genesys__gen__gameplay_trigger__input:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_trigger_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_trigger_0x10:
        pos: ptr_arr_trigger_0x10
        type: u4
        if: ptr_arr_trigger_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x37_ad_05_45
  genesys__gen__gameplay_trigger__output:
    seq:
      - id: base_object
        type: gen_obj
      - id: predicate_0xc
        type: string_base
      - id: cgs_resource__handle_0x14
        size: 8
      - id: game_changer_id_0x1c
        type: u4
      - id: ptr_arr_ptr_aiplayer_instance_0x20
        type: u4
        doc: enum; 00_06_fa_75_1
      - id: ptr_arr_sequence_0x24
        type: u4
        doc: enum; 00_06_cc_76_1
      - id: ptr_arr_ptr_roadblock_instance_0x28
        type: u4
        doc: enum; 00_09_37_62_1
      - id: array_count_for_0x24
        type: u2
        doc: '"SequenceCount"'
      - id: array_count_for_0x20
        type: u1
      - id: array_count_for_0x28
        type: u1
        doc: '"RoadblockInstanceCount"'
    instances:
      inst_aiplayer_instance_0x20:
        pos: ptr_arr_ptr_aiplayer_instance_0x20
        type: ptr('u4')
        if: ptr_arr_ptr_aiplayer_instance_0x20 != 0
        repeat: expr
        repeat-expr: array_count_for_0x20
      inst_sequence_0x24:
        pos: ptr_arr_sequence_0x24
        type: u4
        if: ptr_arr_sequence_0x24 != 0
        repeat: expr
        repeat-expr: array_count_for_0x24
      inst_roadblock_instance_0x28:
        pos: ptr_arr_ptr_roadblock_instance_0x28
        type: ptr('u4')
        if: ptr_arr_ptr_roadblock_instance_0x28 != 0
        repeat: expr
        repeat-expr: array_count_for_0x28
      size:
        value: 48
      mu_version_hash:
        value: 0x56_b9_1f_bf
  genesys__gen__heat_level__cop_type:
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
      - id: uint8_t_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x7a_12_3c_69
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
        value: 24
      mu_version_hash:
        value: 0x7c_8e_25_02
  t_00_09_37_93:
    seq: []
    instances: {}
  genesys__gen__environment_keyframe:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: colour_cube_0x14
        size: 8
      - id: game_changer_id_0x1c
        type: u4
      - id: unk_enum_0x20
        type: u4
        doc: enum; 00_00_27_dd_1_5
      - id: unk_enum_0x24
        type: u4
        doc: enum; 00_00_27_dd_1_4
      - id: unk_enum_0x28
        type: u4
        doc: enum; 00_00_27_dd_1_2
      - id: unk_enum_0x2c
        type: u4
        doc: enum; 00_00_27_dd_1_8
      - id: unk_enum_0x30
        type: u4
        doc: enum; 00_00_27_dd_1_1
      - id: unk_enum_0x34
        type: u4
        doc: enum; 00_00_27_dd_1_7
      - id: unk_enum_0x38
        type: u4
        doc: enum; 00_00_27_dd_1_3
      - id: unk_enum_0x3c
        type: u4
        doc: enum; 00_00_27_dd_1_6
      - id: unk_enum_0x40
        type: u4
        doc: enum; 00_00_27_dd_1_9
    instances:
      inst_00_00_27_dd_1_5_0x20:
        pos: unk_enum_0x20
        type: u4
        if: unk_enum_0x20 != 0
      inst_00_00_27_dd_1_4_0x24:
        pos: unk_enum_0x24
        type: u4
        if: unk_enum_0x24 != 0
      inst_00_00_27_dd_1_2_0x28:
        pos: unk_enum_0x28
        type: u4
        if: unk_enum_0x28 != 0
      inst_00_00_27_dd_1_8_0x2c:
        pos: unk_enum_0x2c
        type: u4
        if: unk_enum_0x2c != 0
      inst_00_00_27_dd_1_1_0x30:
        pos: unk_enum_0x30
        type: u4
        if: unk_enum_0x30 != 0
      inst_00_00_27_dd_1_7_0x34:
        pos: unk_enum_0x34
        type: u4
        if: unk_enum_0x34 != 0
      inst_00_00_27_dd_1_3_0x38:
        pos: unk_enum_0x38
        type: u4
        if: unk_enum_0x38 != 0
      inst_00_00_27_dd_1_6_0x3c:
        pos: unk_enum_0x3c
        type: u4
        if: unk_enum_0x3c != 0
      inst_00_00_27_dd_1_9_0x40:
        pos: unk_enum_0x40
        type: u4
        if: unk_enum_0x40 != 0
      size:
        value: 68
      mu_version_hash:
        value: 0x8c_47_45_f7
  genesys__gen__environment_keyframe__light_rig:
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
      - id: rw_math_vpu__vector4_0x70
        type: rw_math_vpu__vector4
      - id: game_changer_id_0x80
        type: u4
      - id: float32_t_0x84
        type: f4
    instances:
      size:
        value: 136
      mu_version_hash:
        value: 0x64_56_94_63
  genesys__gen__environment_keyframe__fog:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: game_changer_id_0x20
        type: u4
      - id: float32_t_0x24
        type: f4
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: arr_inline_float32_t_0x30
        type: f4
        repeat: expr
        repeat-expr: 5
      - id: far_distance_0x44
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
      - id: near_distance_0x5c
        type: f4
      - id: power_0x60
        type: f4
      - id: float32_t_0x64
        type: f4
      - id: array_count_for_0x30
        type: u2
      - id: padding
        size: 2
    instances:
      size:
        value: 108
      mu_version_hash:
        value: 0x2f_1e_cb_20
  genesys__gen__environment_keyframe__sky:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector4_0x10
        type: rw_math_vpu__vector4
      - id: game_changer_id_0x20
        type: u4
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
      - id: ptr_arr_float32_t_0x48
        type: u4
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
      - id: array_count_for_0x48
        type: u2
      - id: padding
        size: 2
    instances:
      inst_float32_t_0x48:
        pos: ptr_arr_float32_t_0x48
        type: f4
        if: ptr_arr_float32_t_0x48 != 0
        repeat: expr
        repeat-expr: array_count_for_0x48
      size:
        value: 108
      mu_version_hash:
        value: 0xcd_a9_f5_19
  genesys__gen__environment_keyframe__clouds:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector4_0x10
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x20
        type: rw_math_vpu__vector4
      - id: cgs_core__unique_id_0x30
        type: u4
      - id: game_changer_id_0x34
        type: u4
      - id: density_0x38
        type: f4
      - id: float32_t_0x3c
        type: f4
      - id: float32_t_0x40
        type: f4
      - id: scale_0x44
        type: f4
      - id: float32_t_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: speed_0x54
        type: f4
    instances:
      size:
        value: 88
      mu_version_hash:
        value: 0x10_6b_36_d6
  genesys__gen__environment_keyframe__camera:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector4_0x10
        type: rw_math_vpu__vector4
      - id: game_changer_id_0x20
        type: u4
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
      - id: dark_bloom_weight_0x44
        type: f4
      - id: dark_bloom_white_point_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: arr_inline_float32_t_0x58
        type: f4
        repeat: expr
        repeat-expr: 5
      - id: arr_inline_float32_t_0x6c
        type: f4
        repeat: expr
        repeat-expr: 4
      - id: float32_t_0x7c
        type: f4
      - id: array_count_for_0x58
        type: u2
      - id: array_count_for_0x6c
        type: u2
    instances:
      size:
        value: 132
      mu_version_hash:
        value: 0x70_f6_15_8c
  genesys__gen__environment_keyframe__vfx:
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
        value: 24
      mu_version_hash:
        value: 0x44_8f_40_d6
  genesys__gen__environment_keyframe__mini__dof:
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
        value: 28
      mu_version_hash:
        value: 0xdf_92_d1_a0
  genesys__gen__environment_keyframe__heat_haze:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: amplitude_0x10
        type: f4
      - id: float32_t_0x14
        type: f4
      - id: float32_t_0x18
        type: f4
      - id: frequency_0x1c
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
        value: 48
      mu_version_hash:
        value: 0xfd_e0_27_12
  genesys__gen__environment_keyframe__weather:
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
        value: 44
      mu_version_hash:
        value: 0xd9_97_08_86
  genesys__gen__environment_timeline:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: unk_enum_0x10
        type: u4
        doc: enum; 00_00_27_df_1_1
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_00_00_27_df_1_1_0x10:
        pos: unk_enum_0x10
        type: u4
        if: unk_enum_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x91_d5_29_ca
  genesys__gen__environment_timeline__timeline_keyframe:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: time_of_day_0x18
        type: f4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x00_42_3f_25
  genesys__gen__light__base:
    seq:
      - id: base_object
        type: gen_obj
      - id: colour_0x10
        type: rw_math_vpu__vector4
      - id: unk_enum_0x20
        type: u1
        doc: enum; 00_00_32_f1_1
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
        value: 100
      mu_version_hash:
        value: 0xed_c9_d7_11
  genesys__gen__mixer_channel:
    seq:
      - id: base_object
        type: gen_obj
      - id: distance_falloff_0xc
        size: 8
      - id: mixing_group_0x14
        size: 8
      - id: plug_in__chain_0x1c
        size: 8
      - id: voice_group_0x24
        size: 8
      - id: game_changer_id_0x2c
        type: u4
      - id: emitter_response_0x30
        type: f4
      - id: focus_0x34
        type: f4
      - id: gain_0x38
        type: f4
      - id: lfe_send_0x3c
        type: f4
      - id: panning__cosine_0x40
        type: f4
      - id: panning__divergence_0x44
        type: f4
      - id: panning__sine_0x48
        type: f4
      - id: reverb_send_a_0x4c
        type: f4
      - id: reverb_send_b_0x50
        type: f4
      - id: ptr_arr_priority_0x54
        type: u4
        doc: enum; 00_07_6b_0e_1
      - id: doppler_model_0x58
        type: u2
        doc: enum; 00_00_30_22_1
      - id: array_count_for_0x54
        type: u2
        doc: '"PriorityCount"'
      - id: cull_playing_voices_0x5c
        type: u1
      - id: panning__override_0x5d
        type: u1
      - id: instance_limit_0x5e
        type: u1
      - id: padding
        size: 1
    instances:
      inst_priority_0x54:
        pos: ptr_arr_priority_0x54
        type: u4
        if: ptr_arr_priority_0x54 != 0
        repeat: expr
        repeat-expr: array_count_for_0x54
      size:
        value: 96
      mu_version_hash:
        value: 0xdd_aa_b8_6b
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
        value: 20
      mu_version_hash:
        value: 0xf1_5e_68_36
  genesys__gen__post_fx_keyframe:
    seq:
      - id: base_object
        type: gen_obj
      - id: vignette_0x10
        type: u1
        doc: enum; 00_00_33_12_1
      - id: bloom_0x80
        type: u1
        doc: enum; 00_00_33_11_1
      - id: general_0xd0
        type: u1
        doc: enum; 00_00_33_13_1
      - id: unk_enum_0xf4
        type: u1
        doc: enum; 00_00_33_14_1
      - id: unk_enum_0x110
        type: u1
        doc: enum; 00_00_33_15_1
      - id: game_changer_id_0x128
        type: u4
    instances:
      size:
        value: 300
      mu_version_hash:
        value: 0x5a_94_09_dc
  genesys__gen__post_fxstate:
    seq:
      - id: base_object
        type: gen_obj
      - id: arr_inline_colour_cubes_0xc
        type: u1
        repeat: expr
        repeat-expr: 2
        doc: enum; 00_00_33_16_1
      - id: bloom__value__modification_0x44
        type: u1
        doc: enum; 00_00_33_17_1
      - id: colour__cube__value__modification_0x5c
        type: u1
        doc: enum; 00_00_33_17_1
      - id: dof__value__modification_0x74
        type: u1
        doc: enum; 00_00_33_17_1
      - id: general__value__modification_0x8c
        type: u1
        doc: enum; 00_00_33_17_1
      - id: vignette__value__modification_0xa4
        type: u1
        doc: enum; 00_00_33_17_1
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
        doc: enum; 00_00_30_38_1
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
        value: 248
      mu_version_hash:
        value: 0x24_b3_7b_28
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
      - id: float32_t_0x28
        type: f4
      - id: float32_t_0x2c
        type: f4
      - id: max_distance_0x30
        type: f4
      - id: max_distance_divergence_0x34
        type: f4
      - id: max_distance_reverb_0x38
        type: f4
      - id: min_distance_0x3c
        type: f4
      - id: min_distance_divergence_0x40
        type: f4
      - id: min_distance_reverb_0x44
        type: f4
      - id: bool8_t_0x48
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 76
      mu_version_hash:
        value: 0x0a_5f_40_dc
  t_34_26_5a_75:
    seq: []
    instances: {}
  genesys__gen__uielement_base__behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: float32_t_0x1c
        type: f4
      - id: duration_0x20
        type: f4
      - id: type_0x24
        type: u2
        doc: enum; 35_d6_2d_64
      - id: ease_0x26
        type: u2
        doc: enum; 5b_33_21_f5
      - id: unk_enum_0x28
        type: u4
        doc: enum; 34_26_5a_75
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x13_80_30_74
  genesys__gen__uielement_base__effect_constant:
    seq:
      - id: base_object
        type: gen_obj
      - id: values_0x10
        type: rw_math_vpu__vector4
      - id: binding_0x20
        type: string_base
      - id: cgs_core__string_base_0x28
        type: string_base
      - id: game_changer_id_0x30
        type: u4
      - id: int32_t_0x34
        type: s4
      - id: offset_0x38
        type: s4
      - id: int32_t_0x3c
        type: s4
      - id: int32_t_0x40
        type: s4
    instances:
      size:
        value: 68
      mu_version_hash:
        value: 0x6e_fc_a2_93
  genesys__gen__uielement_base__rendering_data:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_resource__handle_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x1c
        type: u4
      - id: array_count_for_0x1c
        type: u2
      - id: padding
        size: 2
    instances:
      inst_cgs_resource__handle_0x1c:
        pos: ptr_arr_cgs_resource__handle_0x1c
        type: cgs_resource__handle
        if: ptr_arr_cgs_resource__handle_0x1c != 0
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 36
      mu_version_hash:
        value: 0xf7_d7_ce_ca
  t_8e_7d_5f_21:
    seq: []
    instances: {}
  genesys__gen__uielement_base__timeline__behaviour:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: float32_t_0x1c
        type: f4
      - id: duration_0x20
        type: f4
      - id: type_0x24
        type: u2
        doc: enum; 05_89_a9_77
      - id: ease_0x26
        type: u2
        doc: enum; d0_00_70_01
      - id: unk_enum_0x28
        type: u4
        doc: enum; 8e_7d_5f_21
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x26_3b_cd_cb
  c9_7e__aa__da:
    seq: []
    instances: {}
  genesys__gen__uielement_base__timeline:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: cgs_core__string_base_0x14
        type: string_base
      - id: game_changer_id_0x1c
        type: u4
      - id: ptr_arr_genesys__gen__uielement_base__timeline__behaviour_0x20
        type: u4
      - id: ptr_arr_genesys__gen__uielement_base__timeline__behaviour_0x24
        type: u4
      - id: ptr_arr_genesys__gen__uielement_base__timeline__behaviour_0x28
        type: u4
      - id: int32_t_0x2c
        type: s4
      - id: unk_enum_0x30
        type: u2
        doc: enum; c9_7e_aa_da
      - id: array_count_for_0x20
        type: u2
      - id: array_count_for_0x24
        type: u2
      - id: array_count_for_0x28
        type: u2
    instances:
      inst_genesys__gen__uielement_base__timeline__behaviour_0x20:
        pos: ptr_arr_genesys__gen__uielement_base__timeline__behaviour_0x20
        type: genesys__gen__uielement_base__timeline__behaviour
        if: ptr_arr_genesys__gen__uielement_base__timeline__behaviour_0x20 != 0
        repeat: expr
        repeat-expr: array_count_for_0x20
      inst_genesys__gen__uielement_base__timeline__behaviour_0x24:
        pos: ptr_arr_genesys__gen__uielement_base__timeline__behaviour_0x24
        type: genesys__gen__uielement_base__timeline__behaviour
        if: ptr_arr_genesys__gen__uielement_base__timeline__behaviour_0x24 != 0
        repeat: expr
        repeat-expr: array_count_for_0x24
      inst_genesys__gen__uielement_base__timeline__behaviour_0x28:
        pos: ptr_arr_genesys__gen__uielement_base__timeline__behaviour_0x28
        type: genesys__gen__uielement_base__timeline__behaviour
        if: ptr_arr_genesys__gen__uielement_base__timeline__behaviour_0x28 != 0
        repeat: expr
        repeat-expr: array_count_for_0x28
      size:
        value: 56
      mu_version_hash:
        value: 0xae_66_27_c7
  da__dc_9b_17:
    seq: []
    instances: {}
  genesys__gen__uielement_base:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: cgs_core__string_base_0x14
        type: string_base
      - id: cgs_core__string_base_0x1c
        type: string_base
      - id: cgs_core__string_base_0x24
        type: string_base
      - id: cgs_core__string_base_0x2c
        type: string_base
      - id: cgs_core__string_base_0x34
        type: string_base
      - id: cgs_core__string_base_0x3c
        type: string_base
      - id: cgs_core__string_base_0x44
        type: string_base
      - id: material_0x4c
        size: 8
      - id: game_changer_id_0x54
        type: u4
      - id: ptr_arr_cgs_core__unique_id_0x58
        type: u4
      - id: cgs_core__unique_id_0x5c
        type: u4
      - id: cgs_core__unique_id_0x60
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x64
        type: u4
      - id: ptr_arr_genesys__gen__uielement_base__behaviour_0x68
        type: u4
      - id: ptr_arr_genesys__gen__uielement_base__behaviour_0x6c
        type: u4
      - id: ptr_arr_genesys__gen__uielement_base__behaviour_0x70
        type: u4
      - id: ptr_arr_genesys__gen__uielement_base__effect_constant_0x74
        type: u4
      - id: ptr_genesys__gen__uielement_base__rendering_data_0x78
        type: u4
      - id: ptr_arr_genesys__gen__uielement_base__timeline_0x7c
        type: u4
      - id: int32_t_0x80
        type: s4
      - id: position_x_0x84
        type: s4
      - id: position_y_0x88
        type: s4
      - id: rotation_0x8c
        type: s4
      - id: int32_t_0x90
        type: s4
      - id: int32_t_0x94
        type: s4
      - id: int32_t_0x98
        type: s4
      - id: int32_t_0x9c
        type: s4
      - id: unk_enum_0xa0
        type: u2
        doc: enum; da_dc_9b_17
      - id: array_count_for_0x74
        type: u2
      - id: array_count_for_0x64
        type: u2
      - id: array_count_for_0x68
        type: u2
      - id: array_count_for_0x58
        type: u2
      - id: array_count_for_0x7c
        type: u2
      - id: array_count_for_0x6c
        type: u2
      - id: array_count_for_0x70
        type: u2
    instances:
      inst_cgs_core__unique_id_0x58:
        pos: ptr_arr_cgs_core__unique_id_0x58
        type: u4
        if: ptr_arr_cgs_core__unique_id_0x58 != 0
        repeat: expr
        repeat-expr: array_count_for_0x58
      inst_cgs_resource__handle_0x64:
        pos: ptr_arr_cgs_resource__handle_0x64
        type: cgs_resource__handle
        if: ptr_arr_cgs_resource__handle_0x64 != 0
        repeat: expr
        repeat-expr: array_count_for_0x64
      inst_genesys__gen__uielement_base__behaviour_0x68:
        pos: ptr_arr_genesys__gen__uielement_base__behaviour_0x68
        type: genesys__gen__uielement_base__behaviour
        if: ptr_arr_genesys__gen__uielement_base__behaviour_0x68 != 0
        repeat: expr
        repeat-expr: array_count_for_0x68
      inst_genesys__gen__uielement_base__behaviour_0x6c:
        pos: ptr_arr_genesys__gen__uielement_base__behaviour_0x6c
        type: genesys__gen__uielement_base__behaviour
        if: ptr_arr_genesys__gen__uielement_base__behaviour_0x6c != 0
        repeat: expr
        repeat-expr: array_count_for_0x6c
      inst_genesys__gen__uielement_base__behaviour_0x70:
        pos: ptr_arr_genesys__gen__uielement_base__behaviour_0x70
        type: genesys__gen__uielement_base__behaviour
        if: ptr_arr_genesys__gen__uielement_base__behaviour_0x70 != 0
        repeat: expr
        repeat-expr: array_count_for_0x70
      inst_genesys__gen__uielement_base__effect_constant_0x74:
        pos: ptr_arr_genesys__gen__uielement_base__effect_constant_0x74
        type: genesys__gen__uielement_base__effect_constant
        if: ptr_arr_genesys__gen__uielement_base__effect_constant_0x74 != 0
        repeat: expr
        repeat-expr: array_count_for_0x74
      inst_genesys__gen__uielement_base__rendering_data_0x78:
        pos: ptr_genesys__gen__uielement_base__rendering_data_0x78
        type: genesys__gen__uielement_base__rendering_data
        if: ptr_genesys__gen__uielement_base__rendering_data_0x78 != 0
      inst_genesys__gen__uielement_base__timeline_0x7c:
        pos: ptr_arr_genesys__gen__uielement_base__timeline_0x7c
        type: genesys__gen__uielement_base__timeline
        if: ptr_arr_genesys__gen__uielement_base__timeline_0x7c != 0
        repeat: expr
        repeat-expr: array_count_for_0x7c
      size:
        value: 176
      mu_version_hash:
        value: 0xe1_90_0e_b0
  t_35__d6_2d_64:
    seq: []
    instances: {}
  t_5b_33_21__f5:
    seq: []
    instances: {}
  d0_00_70_01:
    seq: []
    instances: {}
  t_05_89__a9_77:
    seq: []
    instances: {}
  t_06__a9_64__cd:
    seq: []
    instances: {}
  genesys__gen__uielement__element_stack:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: cgs_core__string_base_0x14
        type: string_base
      - id: cgs_core__string_base_0x1c
        type: string_base
      - id: cgs_core__string_base_0x24
        type: string_base
      - id: cgs_resource__handle_0x2c
        size: 8
      - id: cgs_resource__handle_0x34
        size: 8
      - id: cgs_resource__handle_0x3c
        size: 8
      - id: game_changer_id_0x44
        type: u4
      - id: unk_enum_0x48
        type: u4
        doc: enum; 00_00_2a_7c_1_1
      - id: ptr_genesys__gen__uielement_base_0x4c
        type: u4
      - id: int32_t_0x50
        type: s4
      - id: int32_t_0x54
        type: s4
      - id: int32_t_0x58
        type: s4
      - id: int32_t_0x5c
        type: s4
      - id: int32_t_0x60
        type: s4
      - id: unk_enum_0x64
        type: u2
        doc: enum; 06_a9_64_cd
      - id: array_count_for_0x48
        type: u2
    instances:
      inst_00_00_2a_7c_1_1_0x48:
        pos: unk_enum_0x48
        type: u4
        if: unk_enum_0x48 != 0
        repeat: expr
        repeat-expr: array_count_for_0x48
      inst_genesys__gen__uielement_base_0x4c:
        pos: ptr_genesys__gen__uielement_base_0x4c
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x4c != 0
      size:
        value: 104
      mu_version_hash:
        value: 0xf2_eb_70_5d
  genesys__gen__uielement__element_stack__template:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_0xc
        type: string_base
      - id: cgs_resource__handle_0x14
        size: 8
      - id: game_changer_id_0x1c
        type: u4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0xbd_4d_ce_fb
  genesys__gen__uielement__mini_map:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector3_0x10
        type: rw_math_vpu__vector3
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
      - id: rw_math_vpu__vector4_0x70
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x80
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x90
        type: rw_math_vpu__vector4
      - id: cgs_core__string_base_0xa0
        type: string_base
      - id: cgs_core__string_base_0xa8
        type: string_base
      - id: cgs_core__string_base_0xb0
        type: string_base
      - id: cgs_core__string_base_0xb8
        type: string_base
      - id: cgs_core__string_base_0xc0
        type: string_base
      - id: cgs_core__string_base_0xc8
        type: string_base
      - id: cgs_core__string_base_0xd0
        type: string_base
      - id: game_changer_id_0xd8
        type: u4
      - id: float32_t_0xdc
        type: f4
      - id: float32_t_0xe0
        type: f4
      - id: float32_t_0xe4
        type: f4
      - id: float32_t_0xe8
        type: f4
      - id: float32_t_0xec
        type: f4
      - id: float32_t_0xf0
        type: f4
      - id: float32_t_0xf4
        type: f4
      - id: minimum_speed_0xf8
        type: f4
      - id: float32_t_0xfc
        type: f4
      - id: float32_t_0x100
        type: f4
      - id: float32_t_0x104
        type: f4
      - id: float32_t_0x108
        type: f4
      - id: ptr_genesys__gen__uielement_base_0x10c
        type: u4
      - id: ptr_genesys__object_0x110
        type: u4
      - id: ptr_genesys__object_0x114
        type: u4
      - id: ptr_arr_ptr_genesys__object_0x118
        type: u4
      - id: ptr_mask_0x11c
        type: u4
      - id: ptr_genesys__object_0x120
        type: u4
      - id: array_count_for_0x118
        type: u2
      - id: bool8_t_0x126
        type: u1
      - id: padding
        size: 1
    instances:
      inst_genesys__gen__uielement_base_0x10c:
        pos: ptr_genesys__gen__uielement_base_0x10c
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x10c != 0
      inst_genesys__object_0x110:
        pos: ptr_genesys__object_0x110
        type: generic_gen_object
        if: ptr_genesys__object_0x110 != 0
        doc: "'instance of Genesys.Object'"
      inst_genesys__object_0x114:
        pos: ptr_genesys__object_0x114
        type: generic_gen_object
        if: ptr_genesys__object_0x114 != 0
        doc: "'instance of Genesys.Object'"
      inst_genesys__object_0x118:
        pos: ptr_arr_ptr_genesys__object_0x118
        type: ptr('generic_gen_object')
        if: ptr_arr_ptr_genesys__object_0x118 != 0
        doc: "'instance of Genesys.Object'"
        repeat: expr
        repeat-expr: array_count_for_0x118
      inst_mask_0x11c:
        pos: ptr_mask_0x11c
        type: generic_gen_object
        if: ptr_mask_0x11c != 0
        doc: "'instance of Genesys.Object'"
      inst_genesys__object_0x120:
        pos: ptr_genesys__object_0x120
        type: generic_gen_object
        if: ptr_genesys__object_0x120 != 0
        doc: "'instance of Genesys.Object'"
      size:
        value: 296
      mu_version_hash:
        value: 0x65_a4_3a_9b
  genesys__gen__uielement__main_map:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector3_0x10
        type: rw_math_vpu__vector3
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
      - id: rw_math_vpu__vector4_0x70
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x80
        type: rw_math_vpu__vector4
      - id: rw_math_vpu__vector4_0x90
        type: rw_math_vpu__vector4
      - id: cgs_core__string_base_0xa0
        type: string_base
      - id: cgs_core__string_base_0xa8
        type: string_base
      - id: cgs_core__string_base_0xb0
        type: string_base
      - id: cgs_core__string_base_0xb8
        type: string_base
      - id: cgs_core__string_base_0xc0
        type: string_base
      - id: cgs_core__string_base_0xc8
        type: string_base
      - id: cgs_core__string_base_0xd0
        type: string_base
      - id: game_changer_id_0xd8
        type: u4
      - id: float32_t_0xdc
        type: f4
      - id: float32_t_0xe0
        type: f4
      - id: float32_t_0xe4
        type: f4
      - id: float32_t_0xe8
        type: f4
      - id: float32_t_0xec
        type: f4
      - id: float32_t_0xf0
        type: f4
      - id: float32_t_0xf4
        type: f4
      - id: minimum_speed_0xf8
        type: f4
      - id: float32_t_0xfc
        type: f4
      - id: float32_t_0x100
        type: f4
      - id: float32_t_0x104
        type: f4
      - id: float32_t_0x108
        type: f4
      - id: ptr_genesys__gen__uielement_base_0x10c
        type: u4
      - id: ptr_genesys__object_0x110
        type: u4
      - id: ptr_genesys__object_0x114
        type: u4
      - id: ptr_arr_ptr_genesys__object_0x118
        type: u4
      - id: ptr_mask_0x11c
        type: u4
      - id: ptr_genesys__object_0x120
        type: u4
      - id: array_count_for_0x118
        type: u2
      - id: bool8_t_0x126
        type: u1
      - id: padding
        size: 1
    instances:
      inst_genesys__gen__uielement_base_0x10c:
        pos: ptr_genesys__gen__uielement_base_0x10c
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x10c != 0
      inst_genesys__object_0x110:
        pos: ptr_genesys__object_0x110
        type: generic_gen_object
        if: ptr_genesys__object_0x110 != 0
        doc: "'instance of Genesys.Object'"
      inst_genesys__object_0x114:
        pos: ptr_genesys__object_0x114
        type: generic_gen_object
        if: ptr_genesys__object_0x114 != 0
        doc: "'instance of Genesys.Object'"
      inst_genesys__object_0x118:
        pos: ptr_arr_ptr_genesys__object_0x118
        type: ptr('generic_gen_object')
        if: ptr_arr_ptr_genesys__object_0x118 != 0
        doc: "'instance of Genesys.Object'"
        repeat: expr
        repeat-expr: array_count_for_0x118
      inst_mask_0x11c:
        pos: ptr_mask_0x11c
        type: generic_gen_object
        if: ptr_mask_0x11c != 0
        doc: "'instance of Genesys.Object'"
      inst_genesys__object_0x120:
        pos: ptr_genesys__object_0x120
        type: generic_gen_object
        if: ptr_genesys__object_0x120 != 0
        doc: "'instance of Genesys.Object'"
      size:
        value: 296
      mu_version_hash:
        value: 0x83_16_4a_5d
  genesys__gen__uielement__mask:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: ptr_genesys__gen__uielement_base_0x14
        type: u4
      - id: bool8_t_0x18
        type: u1
      - id: padding
        size: 3
    instances:
      inst_genesys__gen__uielement_base_0x14:
        pos: ptr_genesys__gen__uielement_base_0x14
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x14 != 0
      size:
        value: 28
      mu_version_hash:
        value: 0x24_e9_85_66
  genesys__gen__uielement__movie_player:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_size_0x10
        type: u4
        doc: enum; 00_00_2a_81_1_1
      - id: ptr_genesys__gen__uielement_base_0x14
        type: u4
    instances:
      inst_size_0x10:
        pos: ptr_size_0x10
        type: u4
        if: ptr_size_0x10 != 0
      inst_genesys__gen__uielement_base_0x14:
        pos: ptr_genesys__gen__uielement_base_0x14
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x14 != 0
      size:
        value: 24
      mu_version_hash:
        value: 0xe6_5b_60_fd
  genesys__gen__uielement__movie_player__dimensions:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: int32_t_0x10
        type: s4
      - id: int32_t_0x14
        type: s4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x52_ab_e0_8b
  genesys__gen__uielement__prototype_image:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: unk_enum_0x1c
        type: u4
        doc: enum; 00_00_2a_83_1_2
      - id: ptr_tint_0x20
        type: u4
        doc: enum; 00_00_2a_83_1_1
      - id: ptr_genesys__gen__uielement_base_0x24
        type: u4
      - id: bool8_t_0x28
        type: u1
      - id: bool8_t_0x29
        type: u1
      - id: padding
        size: 2
    instances:
      inst_00_00_2a_83_1_2_0x1c:
        pos: unk_enum_0x1c
        type: u4
        if: unk_enum_0x1c != 0
      inst_tint_0x20:
        pos: ptr_tint_0x20
        type: u4
        if: ptr_tint_0x20 != 0
      inst_genesys__gen__uielement_base_0x24:
        pos: ptr_genesys__gen__uielement_base_0x24
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x24 != 0
      size:
        value: 44
      mu_version_hash:
        value: 0xba_7f_fb_d9
  genesys__gen__uielement__prototype_image__tint_properties:
    seq:
      - id: base_object
        type: gen_obj
      - id: value_0x10
        type: rw_math_vpu__vector4
      - id: binding_0x20
        type: string_base
      - id: cgs_core__string_base_0x28
        type: string_base
      - id: game_changer_id_0x30
        type: u4
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0x40_5b_b1_d7
  genesys__gen__uielement__prototype_image__opacity:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: value_0x18
        type: s4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x5d_20_64_2f
  genesys__gen__uielement__prototype_label:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: unk_enum_0x10
        type: u4
        doc: enum; 00_00_2a_84_1_1
      - id: unk_enum_0x14
        type: u4
        doc: enum; 00_00_2a_84_1_2
      - id: ptr_genesys__gen__uielement_base_0x18
        type: u4
      - id: int32_t_0x1c
        type: s4
      - id: bool8_t_0x20
        type: u1
      - id: padding
        size: 3
    instances:
      inst_00_00_2a_84_1_1_0x10:
        pos: unk_enum_0x10
        type: u4
        if: unk_enum_0x10 != 0
      inst_00_00_2a_84_1_2_0x14:
        pos: unk_enum_0x14
        type: u4
        if: unk_enum_0x14 != 0
      inst_genesys__gen__uielement_base_0x18:
        pos: ptr_genesys__gen__uielement_base_0x18
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x18 != 0
      size:
        value: 36
      mu_version_hash:
        value: 0xda_04_88_b3
  genesys__gen__uielement__prototype_label__string:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xe2_6f_77_c4
  genesys__gen__uielement__prototype_label__text_properties:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector4_0x10
        type: rw_math_vpu__vector4
      - id: cgs_core__string_base_0x20
        type: string_base
      - id: cgs_resource__handle_0x28
        size: 8
      - id: game_changer_id_0x30
        type: u4
      - id: uno_o_0x34
        type: u2
        doc: enum; 70_f4_bb_e0
      - id: bool8_t_0x36
        type: u1
      - id: bool8_t_0x37
        type: u1
    instances:
      size:
        value: 56
      mu_version_hash:
        value: 0xc3_d4_63_2a
  t_70__f4__bb__e0:
    seq: []
    instances: {}
  genesys__gen__uielement__prototype_scrolling_text:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: unk_enum_0x18
        type: u4
        doc: enum; 00_00_2a_85_1_1
      - id: unk_enum_0x1c
        type: u4
        doc: enum; 00_00_2a_85_1_2
      - id: ptr_genesys__gen__uielement_base_0x20
        type: u4
      - id: int32_t_0x24
        type: s4
      - id: int32_t_0x28
        type: s4
      - id: array_count_for_0x18
        type: u2
      - id: padding
        size: 2
    instances:
      inst_00_00_2a_85_1_1_0x18:
        pos: unk_enum_0x18
        type: u4
        if: unk_enum_0x18 != 0
        repeat: expr
        repeat-expr: array_count_for_0x18
      inst_00_00_2a_85_1_2_0x1c:
        pos: unk_enum_0x1c
        type: u4
        if: unk_enum_0x1c != 0
      inst_genesys__gen__uielement_base_0x20:
        pos: ptr_genesys__gen__uielement_base_0x20
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x20 != 0
      size:
        value: 48
      mu_version_hash:
        value: 0xcc_86_ec_f8
  genesys__gen__uielement__prototype_scrolling_text__string:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xdb_b3_6f_3d
  genesys__gen__uielement__prototype_scrolling_text__text_properties:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector4_0x10
        type: rw_math_vpu__vector4
      - id: cgs_core__string_base_0x20
        type: string_base
      - id: cgs_resource__handle_0x28
        size: 8
      - id: game_changer_id_0x30
        type: u4
      - id: uno_o_0x34
        type: u2
        doc: enum; f7_ff_d1_f8
      - id: bool8_t_0x36
        type: u1
      - id: bool8_t_0x37
        type: u1
    instances:
      size:
        value: 56
      mu_version_hash:
        value: 0xf8_79_f1_b0
  f7__ff__d1__f8:
    seq: []
    instances: {}
  d7__b2_21__da:
    seq: []
    instances: {}
  genesys__gen__uielement__prototype_shape:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector4_0x10
        type: rw_math_vpu__vector4
      - id: game_changer_id_0x20
        type: u4
      - id: ptr_genesys__gen__uielement_base_0x24
        type: u4
      - id: int32_t_0x28
        type: s4
      - id: unk_enum_0x2c
        type: u4
        doc: enum; d7_b2_21_da
    instances:
      inst_genesys__gen__uielement_base_0x24:
        pos: ptr_genesys__gen__uielement_base_0x24
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x24 != 0
      size:
        value: 48
      mu_version_hash:
        value: 0x17_83_63_05
  t_96__c1_53_69:
    seq: []
    instances: {}
  genesys__gen__uielement__scrollable_label:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: cgs_core__string_base_0x14
        type: string_base
      - id: u1u9_0x1c
        type: string_base
      - id: game_changer_id_0x24
        type: u4
      - id: cgs_core__unique_id_0x28
        type: u4
      - id: float32_t_0x2c
        type: f4
      - id: unk_enum_0x30
        type: u4
        doc: enum; 00_00_2a_87_1_1
      - id: unk_enum_0x34
        type: u4
        doc: enum; 00_00_2a_87_1_2
      - id: ptr_genesys__gen__uielement_base_0x38
        type: u4
      - id: ptr_genesys__object_0x3c
        type: u4
      - id: int32_t_0x40
        type: s4
      - id: unk_enum_0x44
        type: u2
        doc: enum; 96_c1_53_69
      - id: id_6afs_0x46
        type: u2
        doc: enum; 40_99_f3_ac
      - id: bool8_t_0x48
        type: u1
      - id: bool8_t_0x49
        type: u1
      - id: padding
        size: 2
    instances:
      inst_00_00_2a_87_1_1_0x30:
        pos: unk_enum_0x30
        type: u4
        if: unk_enum_0x30 != 0
      inst_00_00_2a_87_1_2_0x34:
        pos: unk_enum_0x34
        type: u4
        if: unk_enum_0x34 != 0
      inst_genesys__gen__uielement_base_0x38:
        pos: ptr_genesys__gen__uielement_base_0x38
        type: genesys__gen__uielement_base
        if: ptr_genesys__gen__uielement_base_0x38 != 0
      inst_genesys__object_0x3c:
        pos: ptr_genesys__object_0x3c
        type: generic_gen_object
        if: ptr_genesys__object_0x3c != 0
        doc: "'instance of Genesys.Object'"
      size:
        value: 76
      mu_version_hash:
        value: 0x6e_ab_bc_51
  t_40_99__f3__ac:
    seq: []
    instances: {}
  genesys__gen__uielement__scrollable_label__string:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x1e_16_9f_cb
  genesys__gen__uielement__scrollable_label__text_properties:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector4_0x10
        type: rw_math_vpu__vector4
      - id: cgs_core__string_base_0x20
        type: string_base
      - id: cgs_resource__handle_0x28
        size: 8
      - id: game_changer_id_0x30
        type: u4
      - id: uno_o_0x34
        type: u2
        doc: enum; 35_a6_06_1e
      - id: bool8_t_0x36
        type: u1
      - id: bool8_t_0x37
        type: u1
    instances:
      size:
        value: 56
      mu_version_hash:
        value: 0x41_39_54_24
  t_35__a6_06_1e:
    seq: []
    instances: {}
  genesys__gen__uilayout:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_ptr_elements_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_elements_0x10:
        pos: ptr_arr_ptr_elements_0x10
        type: ptr('generic_gen_object')
        if: ptr_arr_ptr_elements_0x10 != 0
        doc: "'instance of Genesys.Object'"
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0xa6_74_11_68
  genesys__gen__uilayout_instance_params:
    seq:
      - id: base_object
        type: gen_obj
      - id: unk_enum_0xc
        type: u1
        doc: enum; 00_00_33_78_1
      - id: rotation_0x4c
        type: u1
        doc: enum; 00_00_33_77_1
      - id: scale_0x74
        type: u1
        doc: enum; 00_00_33_77_1
      - id: translation_0x9c
        type: u1
        doc: enum; 00_00_33_77_1
      - id: cgs_core__string_base_0xc4
        type: string_base
      - id: cgs_core__string_base_0xcc
        type: string_base
      - id: game_changer_id_0xd4
        type: u4
      - id: unk_enum_0xd8
        type: u4
        doc: enum; 00_00_33_78_1
      - id: unk_enum_0xdc
        type: u4
        doc: enum; 00_00_33_77_1
      - id: int32_t_0xe0
        type: s4
      - id: unk_enum_0xe4
        type: u2
        doc: enum; 00_00_31_ba_1
      - id: unk_enum_0xe6
        type: u2
        doc: enum; 00_00_31_c4_1
      - id: array_count_for_0xdc
        type: u2
      - id: array_count_for_0xd8
        type: u2
    instances:
      inst_00_00_33_78_1_0xd8:
        pos: unk_enum_0xd8
        type: u4
        if: unk_enum_0xd8 != 0
        repeat: expr
        repeat-expr: array_count_for_0xd8
      inst_00_00_33_77_1_0xdc:
        pos: unk_enum_0xdc
        type: u4
        if: unk_enum_0xdc != 0
        repeat: expr
        repeat-expr: array_count_for_0xdc
      size:
        value: 236
      mu_version_hash:
        value: 0xd3_a2_8a_a9
  genesys__gen__uimaterial:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: material_0x10
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x14
        type: u4
      - id: int32_t_0x18
        type: s4
      - id: unk_enum_0x1c
        type: u2
        doc: enum; 00_06_cc_2f_1
      - id: array_count_for_0x14
        type: u2
    instances:
      inst_cgs_resource__handle_0x14:
        pos: ptr_arr_cgs_resource__handle_0x14
        type: cgs_resource__handle
        if: ptr_arr_cgs_resource__handle_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      size:
        value: 32
      mu_version_hash:
        value: 0x78_d6_fe_c0
  genesys__gen__uitechnique:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x18
        type: u4
      - id: unk_enum_0x1c
        type: u2
        doc: enum; 00_00_31_d2_1
      - id: array_count_for_0x18
        type: u2
    instances:
      inst_cgs_resource__handle_0x18:
        pos: ptr_arr_cgs_resource__handle_0x18
        type: cgs_resource__handle
        if: ptr_arr_cgs_resource__handle_0x18 != 0
        repeat: expr
        repeat-expr: array_count_for_0x18
      size:
        value: 32
      mu_version_hash:
        value: 0xd8_e0_f9_66
  t_00_00_2f__f0:
    seq: []
    instances: {}
  t_00_00_30_1d:
    seq: []
    instances: {}
  t_00_00_30_22:
    seq: []
    instances: {}
  t_00_00_30_27:
    seq: []
    instances: {}
  t_00_00_30_35:
    seq: []
    instances: {}
  t_00_00_30_38:
    seq: []
    instances: {}
  t_00_00_30_3d:
    seq: []
    instances: {}
  t_00_00_31__b6:
    seq: []
    instances: {}
  t_00_00_31__ba:
    seq: []
    instances: {}
  t_00_00_31__c4:
    seq: []
    instances: {}
  t_00_00_31__ca:
    seq: []
    instances: {}
  t_00_00_31__d2:
    seq: []
    instances: {}
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
        doc: enum; 00_00_2f_f0_1
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x12_48_17_f4
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
        value: 76
      mu_version_hash:
        value: 0xd6_1a_73_ed
  rw_math_vpu__vector2:
    seq:
      - id: arr_inline_elements_0x0
        type: f4
        repeat: expr
        repeat-expr: 2
    instances:
      size:
        value: 4
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
        value: 104
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
        doc: enum; 00_00_30_35_1
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xf3_88_bb_fd
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
        value: 28
      mu_version_hash:
        value: 0x5f_65_e8_33
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
        value: 24
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
        doc: enum; 00_00_30_3d_1
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0xf5_9a_d1_ea
  genesys__gen__uilayout_instance_params__transform_components:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: x_0x18
        type: f4
      - id: y_0x1c
        type: f4
      - id: z_0x20
        type: f4
      - id: type_0x24
        type: u4
        doc: enum; 00_00_31_ca_1
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x6d_19_4c_19
  genesys__gen__uilayout_instance_params__timeline_parameters:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: cgs_core__string_base_0x14
        type: string_base
      - id: cgs_core__string_base_0x1c
        type: string_base
      - id: cgs_core__string_base_0x24
        type: string_base
      - id: cgs_core__string_base_0x2c
        type: string_base
      - id: game_changer_id_0x34
        type: u4
      - id: int32_t_0x38
        type: s4
      - id: trigger_type_0x3c
        type: u4
        doc: enum; 00_00_31_b6_1
    instances:
      size:
        value: 64
      mu_version_hash:
        value: 0x2f_72_e7_56
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
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x69_49_4f_68
  genesys__gen__wave_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: fade__in_0x20
        type: u1
        doc: enum; 00_03_f6_87_1
      - id: fade__out_0x38
        type: u1
        doc: enum; 00_03_f6_87_1
      - id: snapshot__property_0x50
        type: string_base
      - id: transform__override__binding_0x58
        type: string_base
      - id: mixer__channel_0x60
        size: 8
      - id: ptr_arr_waves_0x68
        type: u4
      - id: ptr_gain_0x6c
        type: u4
        doc: enum; 00_03_f6_5a_1
      - id: ptr_pitch_0x70
        type: u4
        doc: enum; 00_03_f6_5a_1
      - id: type_0x74
        type: u2
        doc: enum; 00_03_f3_c4_1
      - id: array_count_for_0x68
        type: u2
        doc: '"WavesCount"'
      - id: auto__pitch_0x78
        type: u1
      - id: padding
        size: 3
    instances:
      inst_waves_0x68:
        pos: ptr_arr_waves_0x68
        type: cgs_resource__handle
        if: ptr_arr_waves_0x68 != 0
        repeat: expr
        repeat-expr: array_count_for_0x68
      inst_gain_0x6c:
        pos: ptr_gain_0x6c
        type: u4
        if: ptr_gain_0x6c != 0
      inst_pitch_0x70:
        pos: ptr_pitch_0x70
        type: u4
        if: ptr_pitch_0x70 != 0
      size:
        value: 124
      mu_version_hash:
        value: 0x35_84_25_6f
  t_00_03__f3__c4:
    seq: []
    instances: {}
  genesys__gen__animation_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: cgs_resource__handle_0x20
        size: 8
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x88_89_de_f6
  genesys__gen__wcsequence_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: sequence_0x1c
        size: 8
      - id: bool8_t_0x24
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xcc_58_ca_7a
  genesys__gen__sequence_item__modulating_double_value:
    seq:
      - id: base_object
        type: gen_obj
      - id: binding_0xc
        type: string_base
      - id: cgs_resource__handle_0x14
        size: 8
      - id: game_changer_id_0x1c
        type: u4
      - id: bias_0x20
        type: f4
      - id: binding__exponent_0x24
        type: f4
      - id: binding__range__max_0x28
        type: f4
      - id: binding__range__min_0x2c
        type: f4
      - id: output__value__max_0x30
        type: f4
      - id: output__value__min_0x34
        type: f4
      - id: value_0x38
        type: f4
      - id: animation__modulation__type_0x3c
        type: u2
        doc: enum; 00_03_f6_5b_1
      - id: binding__modulation__type_0x3e
        type: u2
        doc: enum; 00_03_f6_5b_1
      - id: binding__invert_0x40
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 68
      mu_version_hash:
        value: 0xb6_da_e6_71
  t_00_03__f6_5b:
    seq: []
    instances: {}
  t_00_03__f6_83:
    seq: []
    instances: {}
  genesys__gen__wave_sequence_item__fade:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: curve_0x10
        type: f4
      - id: time_0x14
        type: f4
    instances:
      size:
        value: 24
      mu_version_hash:
        value: 0x8a_62_3f_1d
  genesys__gen__bus_mixer_channel_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: bus_0x20
        type: u4
      - id: ptr_arr_automated__values_0x24
        type: u4
        doc: enum; 00_03_f6_d4_1
      - id: array_count_for_0x24
        type: u2
        doc: '"Automated_ValuesCount"'
      - id: padding
        size: 2
    instances:
      inst_automated__values_0x24:
        pos: ptr_arr_automated__values_0x24
        type: u4
        if: ptr_arr_automated__values_0x24 != 0
        repeat: expr
        repeat-expr: array_count_for_0x24
      size:
        value: 44
      mu_version_hash:
        value: 0xd1_65_21_59
  genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_modulating_value_0x10
        type: u4
        doc: enum; 00_03_f6_5a_1
      - id: bus_mixer_channel_property_0x14
        type: u4
        doc: enum; 00_03_f6_d5_1
    instances:
      inst_modulating_value_0x10:
        pos: ptr_modulating_value_0x10
        type: u4
        if: ptr_modulating_value_0x10 != 0
      size:
        value: 24
      mu_version_hash:
        value: 0x02_74_d0_24
  t_00_03__f6__d5:
    seq: []
    instances: {}
  genesys__gen__physics_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: ptr_arr_automated__values_0x20
        type: u4
        doc: enum; 00_03_f7_14_1
      - id: array_count_for_0x20
        type: u2
        doc: '"Automated_ValuesCount"'
      - id: padding
        size: 2
    instances:
      inst_automated__values_0x20:
        pos: ptr_arr_automated__values_0x20
        type: u4
        if: ptr_arr_automated__values_0x20 != 0
        repeat: expr
        repeat-expr: array_count_for_0x20
      size:
        value: 40
      mu_version_hash:
        value: 0x5b_eb_4f_2f
  genesys__gen__physics_sequence_item__physics_double_value:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_modulating_value_0x10
        type: u4
        doc: enum; 00_03_f6_5a_1
      - id: automated__property_0x14
        type: u4
        doc: enum; 00_03_f7_15_1
    instances:
      inst_modulating_value_0x10:
        pos: ptr_modulating_value_0x10
        type: u4
        if: ptr_modulating_value_0x10 != 0
      size:
        value: 24
      mu_version_hash:
        value: 0xeb_cf_86_b0
  t_00_03__f7_15:
    seq: []
    instances: {}
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
        doc: enum; 00_04_63_4a_1
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
      - id: ptr_arr_sequence_items_0x18
        type: u4
      - id: ptr_arr_timeline_controllers_0x1c
        type: u4
      - id: binding__max_0x20
        type: f4
      - id: binding__min_0x24
        type: f4
      - id: default__progression__controller_0x28
        type: u2
        doc: enum; 00_03_f6_83_1
      - id: array_count_for_0x18
        type: u2
        doc: '"SequenceItemsCount"'
      - id: array_count_for_0x1c
        type: u2
        doc: '"TimelineControllersCount"'
      - id: padding
        size: 2
    instances:
      inst_sequence_items_0x18:
        pos: ptr_arr_sequence_items_0x18
        type: cgs_resource__handle
        if: ptr_arr_sequence_items_0x18 != 0
        repeat: expr
        repeat-expr: array_count_for_0x18
      inst_timeline_controllers_0x1c:
        pos: ptr_arr_timeline_controllers_0x1c
        type: cgs_resource__handle
        if: ptr_arr_timeline_controllers_0x1c != 0
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 48
      mu_version_hash:
        value: 0xfc_f0_5f_e9
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
        value: 36
      mu_version_hash:
        value: 0x06_e6_a5_18
  genesys__gen__layout_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: cgs_resource__handle_0x20
        size: 8
      - id: cgs_resource__handle_0x28
        size: 8
      - id: unk_enum_0x30
        type: u4
        doc: enum; 00_03_f8_50_1
    instances:
      size:
        value: 52
      mu_version_hash:
        value: 0xab_95_3f_0c
  t_00_03__f8_50:
    seq: []
    instances: {}
  genesys__gen__post_fxsequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: post_fxstate_0x20
        size: 8
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x99_cb_68_36
  t_00_04_5e__f1:
    seq: []
    instances: {}
  t_00_04_5f__ad:
    seq: []
    instances: {}
  t_00_04_63_4a:
    seq: []
    instances: {}
  genesys__gen__weapon_upgrade:
    seq:
      - id: base_object
        type: gen_obj
      - id: description_0xc
        type: u4
      - id: game_changer_id_0x10
        type: u4
      - id: image_0x14
        type: u4
      - id: name_0x18
        type: u4
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x34_eb_fc_7e
  genesys__gen__silent_launch_weapon_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__weapon_upgrade
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x4c_93_b8_27
  genesys__gen__extra_ammo_weapon_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__weapon_upgrade
      - id: uint8_t_0x1c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x62_e1_8b_c6
  genesys__gen__arc_light_cone_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__weapon_upgrade
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: float32_t_0x24
        type: f4
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0xf3_e9_59_fe
  genesys__gen__spike_strip_body_blow_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__weapon_upgrade
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x55_f0_51_e3
  genesys__gen__spike_strip_blowout_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__weapon_upgrade
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x02_75_06_f3
  genesys__gen__dust_storm_minimap_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__weapon_upgrade
      - id: float32_t_0x1c
        type: f4
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x8a_c1_4c_bb
  genesys__gen__hypox_particles_weapon_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__weapon_upgrade
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xe8_37_d4_2c
  genesys__gen__vfx_spot_effect_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: rw_math_vpu__vector3_0x20
        type: rw_math_vpu__vector3
      - id: cgs_core__string_base_0x30
        type: string_base
      - id: cgs_resource__handle_0x38
        size: 8
    instances:
      size:
        value: 60
      mu_version_hash:
        value: 0xdb_46_7b_91
  genesys__gen__add_behaviour_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: behaviour_0x20
        size: 8
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xff_33_3d_e7
  genesys__gen__hud_style_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: unk_enum_0x20
        type: u4
        doc: enum; 00_05_ab_65_1
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x08_37_f3_16
  t_00_05__ab_65:
    seq: []
    instances: {}
  genesys__gen__apply_vehicle_kick_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: strength_0x20
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xb8_93_80_28
  genesys__gen__camera_gameplay_shake_effect:
    seq:
      - id: base_object
        type: gen_obj
      - id: translation_0xc
        type: u1
        doc: enum; 00_06_8f_da_1
      - id: rotation_0xa4
        type: u1
        doc: enum; 00_06_8f_d9_1
      - id: game_changer_id_0x130
        type: u4
    instances:
      size:
        value: 308
      mu_version_hash:
        value: 0xd5_69_9b_70
  genesys__gen__camera_gameplay_shake_effect__rotation:
    seq:
      - id: base_object
        type: gen_obj
      - id: pitch_0xc
        type: u1
        doc: enum; 00_06_8f_db_1
      - id: roll_0x34
        type: u1
        doc: enum; 00_06_8f_db_1
      - id: yaw_0x5c
        type: u1
        doc: enum; 00_06_8f_db_1
      - id: game_changer_id_0x84
        type: u4
      - id: amplitude_0x88
        type: f4
    instances:
      size:
        value: 140
      mu_version_hash:
        value: 0x48_b8_4c_b2
  genesys__gen__camera_gameplay_shake_effect__translation:
    seq:
      - id: base_object
        type: gen_obj
      - id: x_0xc
        type: u1
        doc: enum; 00_06_8f_dc_1
      - id: y_0x38
        type: u1
        doc: enum; 00_06_8f_dc_1
      - id: z_0x64
        type: u1
        doc: enum; 00_06_8f_dc_1
      - id: game_changer_id_0x90
        type: u4
      - id: amplitude_0x94
        type: f4
    instances:
      size:
        value: 152
      mu_version_hash:
        value: 0x33_a1_3e_49
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
  genesys__gen__weapon:
    seq:
      - id: base_object
        type: gen_obj
      - id: rw_math_vpu__vector3_0x10
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0x20
        type: rw_math_vpu__vector3
      - id: cgs_resource__handle_0x30
        size: 8
      - id: cgs_resource__handle_0x38
        size: 8
      - id: cgs_resource__handle_0x40
        size: 8
      - id: cgs_resource__handle_0x48
        size: 8
      - id: cgs_resource__handle_0x50
        size: 8
      - id: cgs_resource__handle_0x58
        size: 8
      - id: game_changer_id_0x60
        type: u4
      - id: image_0x64
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
      - id: cgs_core__unique_id_0x7c
        type: u4
      - id: short_name_0x80
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x84
        type: u4
      - id: float32_t_0x88
        type: f4
      - id: recharge_time_0x8c
        type: f4
      - id: float32_t_0x90
        type: f4
      - id: unk_enum_0x94
        type: u4
        doc: enum; 00_07_2a_be_1
      - id: unk_enum_0x98
        type: u4
        doc: enum; 00_07_2a_be_1
      - id: unk_enum_0x9c
        type: u4
        doc: enum; 00_07_2a_be_1
      - id: unk_enum_0xa0
        type: u2
        doc: enum; 00_04_5f_ad_1
      - id: slot_0xa2
        type: u2
        doc: enum; 00_04_5e_f1_1
      - id: bool8_t_0xa4
        type: u1
      - id: uint8_t_0xa5
        type: u1
      - id: array_count_for_0x84
        type: u1
      - id: padding
        size: 1
    instances:
      inst_cgs_resource__handle_0x84:
        pos: ptr_arr_cgs_resource__handle_0x84
        type: cgs_resource__handle
        if: ptr_arr_cgs_resource__handle_0x84 != 0
        repeat: expr
        repeat-expr: array_count_for_0x84
      inst_00_07_2a_be_1_0x94:
        pos: unk_enum_0x94
        type: u4
        if: unk_enum_0x94 != 0
      inst_00_07_2a_be_1_0x98:
        pos: unk_enum_0x98
        type: u4
        if: unk_enum_0x98 != 0
      inst_00_07_2a_be_1_0x9c:
        pos: unk_enum_0x9c
        type: u4
        if: unk_enum_0x9c != 0
      size:
        value: 168
      mu_version_hash:
        value: 0xdb_d6_17_c8
  genesys__gen__weapon_list:
    seq:
      - id: base_object
        type: gen_obj
      - id: game_changer_id_0xc
        type: u4
      - id: ptr_arr_cgs_resource__handle_0x10
        type: u4
      - id: array_count_for_0x10
        type: u2
      - id: padding
        size: 2
    instances:
      inst_cgs_resource__handle_0x10:
        pos: ptr_arr_cgs_resource__handle_0x10
        type: cgs_resource__handle
        if: ptr_arr_cgs_resource__handle_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      size:
        value: 24
      mu_version_hash:
        value: 0x65_70_9e_b3
  genesys__gen__spike_strip_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
      - id: rw_math_vpu__vector3_0xb0
        type: rw_math_vpu__vector3
      - id: rw_math_vpu__vector3_0xc0
        type: rw_math_vpu__vector3
      - id: surface_0xd0
        type: u4
      - id: float32_t_0xd4
        type: f4
      - id: float32_t_0xd8
        type: f4
      - id: float32_t_0xdc
        type: f4
      - id: float32_t_0xe0
        type: f4
      - id: float32_t_0xe4
        type: f4
      - id: float32_t_0xe8
        type: f4
      - id: bool8_t_0xec
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 240
      mu_version_hash:
        value: 0x5e_bd_8a_23
  genesys__gen__smoke_screen_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
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
    instances:
      size:
        value: 220
      mu_version_hash:
        value: 0xc4_d9_ad_a2
  genesys__gen__flash_headlights_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
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
      - id: float32_t_0xdc
        type: f4
      - id: float32_t_0xe0
        type: f4
      - id: float32_t_0xe4
        type: f4
      - id: float32_t_0xe8
        type: f4
      - id: float32_t_0xec
        type: f4
    instances:
      size:
        value: 240
      mu_version_hash:
        value: 0xc9_40_c8_d7
  t_00_06__cc_2f:
    seq: []
    instances: {}
  genesys__gen__uicolour:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__string_base_0xc
        type: string_base
      - id: game_changer_id_0x14
        type: u4
      - id: colour_0x18
        type: rw__rgba
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0x3f_0e_3e_55
  rw__rgba:
    seq:
      - id: arr_inline_uint8_t_0x0
        type: u1
        repeat: expr
        repeat-expr: 4
      - id: padding
        size: 3
    instances:
      size:
        value: 4
      mu_version_hash:
        value: 0x0b_10_18_a7
  t_00_07_33__ee:
    seq: []
    instances: {}
  genesys__gen__camera_shake_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: unk_enum_0x20
        type: u4
        doc: enum; 00_06_8f_d8_1
    instances:
      inst_00_06_8f_d8_1_0x20:
        pos: unk_enum_0x20
        type: u4
        if: unk_enum_0x20 != 0
      size:
        value: 36
      mu_version_hash:
        value: 0x5c_d0_42_36
  genesys__gen__event_trigger_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x96_2d_e0_bf
  t_00_07_57_09:
    seq: []
    instances: {}
  genesys__gen__weapon_recharge_data:
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
      - id: type_0x20
        type: u4
        doc: enum; 00_07_57_09_1
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xdb_db_1a_8e
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
  genesys__gen__vision_mode:
    seq:
      - id: base_object
        type: genesys__gen__weapon
      - id: padding
        size: 2
    instances:
      size:
        value: 172
      mu_version_hash:
        value: 0x9e_30_79_c4
  genesys__gen__thermal_vision_mode:
    seq:
      - id: base_object
        type: genesys__gen__vision_mode
      - id: padding
        size: 2
    instances:
      size:
        value: 172
      mu_version_hash:
        value: 0x4d_bc_1e_69
  genesys__gen__environment_timeline_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: cgs_resource__handle_0x20
        size: 8
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0x88_b4_c0_6b
  genesys__gen__set_vision_mode_type_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: cgs_resource__handle_0x20
        size: 8
      - id: unk_enum_0x28
        type: u4
        doc: enum; 00_07_bc_8a_1
    instances:
      size:
        value: 44
      mu_version_hash:
        value: 0x5e_5f_4f_4f
  t_00_07__bc_8a:
    seq: []
    instances: {}
  genesys__gen__thermal_vision_mode_properties:
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
        value: 64
      mu_version_hash:
        value: 0xa2_34_48_a0
  genesys__gen__fast_launch_weapon_upgrade:
    seq:
      - id: base_object
        type: genesys__gen__weapon_upgrade
    instances:
      size:
        value: 28
      mu_version_hash:
        value: 0xec_6f_ce_1d
  genesys__gen__light__point:
    seq:
      - id: base_object
        type: genesys__gen__light__base
    instances:
      size:
        value: 88
      mu_version_hash:
        value: 0xec_fa_af_14
  genesys__gen__searchlight_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: cgs_resource__handle_0x1c
        size: 8
      - id: cgs_resource__handle_0x24
        size: 8
      - id: light_definition_0x2c
        size: 8
      - id: locator_group_0x34
        type: u4
    instances:
      size:
        value: 56
      mu_version_hash:
        value: 0x98_74_e1_8d
  a7_6d_0e_28:
    seq: []
    instances: {}
  genesys__gen__text_style:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: cgs_core__unique_id_0x18
        type: u4
      - id: float32_t_0x1c
        type: f4
      - id: arr_inline_float32_t_0x20
        type: f4
        repeat: expr
        repeat-expr: 4
      - id: float32_t_0x30
        type: f4
      - id: float32_t_0x34
        type: f4
      - id: arr_inline_float32_t_0x38
        type: f4
        repeat: expr
        repeat-expr: 4
      - id: float32_t_0x48
        type: f4
      - id: float32_t_0x4c
        type: f4
      - id: float32_t_0x50
        type: f4
      - id: float32_t_0x54
        type: f4
      - id: unk_enum_0x58
        type: u4
        doc: enum; 00_00_2a_58_1_1
      - id: unk_enum_0x5c
        type: u2
        doc: enum; a7_6d_0e_28
      - id: array_count_for_0x20
        type: u2
      - id: array_count_for_0x38
        type: u2
      - id: array_count_for_0x58
        type: u2
      - id: bool8_t_0x64
        type: u1
      - id: bool8_t_0x65
        type: u1
      - id: padding
        size: 2
    instances:
      inst_00_00_2a_58_1_1_0x58:
        pos: unk_enum_0x58
        type: u4
        if: unk_enum_0x58 != 0
        repeat: expr
        repeat-expr: array_count_for_0x58
      size:
        value: 104
      mu_version_hash:
        value: 0x77_94_0e_7d
  t_95_95_0d_30:
    seq: []
    instances: {}
  genesys__gen__text_style__text_style_locale:
    seq:
      - id: base_object
        type: gen_obj
      - id: cgs_core__unique_id_0xc
        type: u4
      - id: cgs_core__unique_id_0x10
        type: u4
      - id: game_changer_id_0x14
        type: u4
      - id: float32_t_0x18
        type: f4
      - id: float32_t_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
      - id: unk_enum_0x24
        type: u4
        doc: enum; 95_95_0d_30
    instances:
      size:
        value: 40
      mu_version_hash:
        value: 0x16_9e_0b_3d
  genesys__gen__wchide_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: padding
        size: 2
    instances:
      size:
        value: 32
      mu_version_hash:
        value: 0x5d_5a_65_e9
  genesys__gen__wcpath_animation_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: unk_enum_0x1c
        type: u4
        doc: enum; 00_00_33_91_1
      - id: array_count_for_0x1c
        type: u2
      - id: padding
        size: 2
    instances:
      inst_00_00_33_91_1_0x1c:
        pos: unk_enum_0x1c
        type: u4
        if: unk_enum_0x1c != 0
        repeat: expr
        repeat-expr: array_count_for_0x1c
      size:
        value: 36
      mu_version_hash:
        value: 0x20_01_b3_25
  genesys__gen__wcpath_animation_behaviour__animation_path:
    seq:
      - id: base_object
        type: gen_obj
      - id: path_0xc
        size: 8
      - id: game_changer_id_0x14
        type: u4
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
      - id: bool8_t_0x38
        type: u1
      - id: bool8_t_0x39
        type: u1
      - id: bool8_t_0x3a
        type: u1
      - id: bool8_t_0x3b
        type: u1
      - id: bool8_t_0x3c
        type: u1
      - id: padding
        size: 3
    instances:
      size:
        value: 64
      mu_version_hash:
        value: 0xf7_66_51_79
  genesys__gen__snap_to_world_behaviour:
    seq:
      - id: base_object
        type: genesys__gen__behaviour
      - id: distance_0x1c
        type: f4
      - id: float32_t_0x20
        type: f4
    instances:
      size:
        value: 36
      mu_version_hash:
        value: 0xe7_1e_b5_01
  genesys__gen__physical_explosion__non_race_car_explosion:
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
        value: 36
      mu_version_hash:
        value: 0x37_71_e2_77
  genesys__gen__physical_explosion__race_car_on_ground_explosion:
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
        value: 24
      mu_version_hash:
        value: 0xc5_95_72_2d
  genesys__gen__physical_explosion__race_car_in_air_explosion:
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
        value: 24
      mu_version_hash:
        value: 0x78_d4_44_fd
  genesys__gen__physical_explosion__gameplay_explosion:
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
        value: 24
      mu_version_hash:
        value: 0x91_95_42_fe
  genesys__gen__mine_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
      - id: cgs_resource__handle_0xb0
        size: 8
      - id: float32_t_0xb8
        type: f4
      - id: float32_t_0xbc
        type: f4
      - id: float32_t_0xc0
        type: f4
    instances:
      size:
        value: 196
      mu_version_hash:
        value: 0x51_3e_35_2b
  genesys__gen__physical_explosion:
    seq:
      - id: base_object
        type: gen_obj
      - id: unk_enum_0xc
        type: u1
        doc: enum; 00_05_d7_a4_1
      - id: unk_enum_0x30
        type: u1
        doc: enum; 00_05_d7_a7_1
      - id: unk_enum_0x48
        type: u1
        doc: enum; 00_05_d7_a6_1
      - id: unk_enum_0x60
        type: u1
        doc: enum; 00_05_d7_a5_1
      - id: game_changer_id_0x78
        type: u4
    instances:
      size:
        value: 124
      mu_version_hash:
        value: 0x6c_78_4f_9c
  genesys__gen__teflon_slick_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
      - id: cgs_core__unique_id_0xb0
        type: u4
      - id: cgs_core__unique_id_0xb4
        type: u4
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
      - id: radius_0xcc
        type: f4
      - id: float32_t_0xd0
        type: f4
      - id: float32_t_0xd4
        type: f4
      - id: int32_t_0xd8
        type: s4
    instances:
      size:
        value: 220
      mu_version_hash:
        value: 0x6e_d8_9d_70
  genesys__gen__grenade_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
      - id: cgs_resource__handle_0xb0
        size: 8
      - id: float32_t_0xb8
        type: f4
      - id: float32_t_0xbc
        type: f4
    instances:
      size:
        value: 192
      mu_version_hash:
        value: 0xa0_2c_67_4c
  genesys__gen__flash_bang_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
      - id: cgs_resource__handle_0xb0
        size: 8
      - id: float32_t_0xb8
        type: f4
      - id: float32_t_0xbc
        type: f4
      - id: float32_t_0xc0
        type: f4
    instances:
      size:
        value: 196
      mu_version_hash:
        value: 0x84_75_cc_83
  genesys__gen__jammer_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
      - id: effect_duration_0xb0
        type: f4
      - id: float32_t_0xb4
        type: f4
    instances:
      size:
        value: 184
      mu_version_hash:
        value: 0xc5_3b_cf_df
  genesys__gen__speedbreaker_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
      - id: float32_t_0xb0
        type: f4
      - id: float32_t_0xb4
        type: f4
      - id: float32_t_0xb8
        type: f4
      - id: float32_t_0xbc
        type: f4
    instances:
      size:
        value: 192
      mu_version_hash:
        value: 0xd3_7f_ea_f5
  genesys__gen__slow_mo_sequence_item:
    seq:
      - id: base_object
        type: genesys__gen__sequence_item
      - id: unk_enum_0x20
        type: u4
        doc: enum; 00_03_f6_5a_1
    instances:
      inst_00_03_f6_5a_1_0x20:
        pos: unk_enum_0x20
        type: u4
        if: unk_enum_0x20 != 0
      size:
        value: 36
      mu_version_hash:
        value: 0x93_42_b9_84
  genesys__gen__helicopter_weapon:
    seq:
      - id: base_object
        type: genesys__gen__weapon
      - id: padding
        size: 2
    instances:
      size:
        value: 172
      mu_version_hash:
        value: 0xc7_16_7c_f0
  genesys_obj_collection:
    seq:
      - id: base_object
        type: gen_obj
      - id: unk_id
        type: u4
      - id: collection_start_offset
        type: u4
      - id: collection_count
        type: u2
      - id: padding
        size: 0x2
    instances:
      obj_collection:
        pos: collection_start_offset
        type: ptr('generic_gen_object')
        repeat: expr
        repeat-expr: collection_count

  
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
            '"genesys__gen__behaviour"': genesys__gen__behaviour
            '"cgs_core__string_base"': cgs_core__string_base
            '"char"': char
            '"uint32_t"': uint32_t
            '"cgs_core__unique_id"': cgs_core__unique_id
            '"bool8_t"': bool8_t
            '"genesys__gen__physical_definition__rigid_body__box_volume"': genesys__gen__physical_definition__rigid_body__box_volume
            '"genesys__gen__physical_definition__rigid_body__capsule_volume"': genesys__gen__physical_definition__rigid_body__capsule_volume
            '"genesys__gen__physical_definition__rigid_body__convex_hull_volume"': genesys__gen__physical_definition__rigid_body__convex_hull_volume
            '"genesys__gen__physical_definition__rigid_body__cylinder_volume"': genesys__gen__physical_definition__rigid_body__cylinder_volume
            '"genesys__gen__physical_definition__rigid_body__sphere_volume"': genesys__gen__physical_definition__rigid_body__sphere_volume
            '"genesys__gen__physical_definition__rigid_body"': genesys__gen__physical_definition__rigid_body
            '"genesys__gen__physical_definition"': genesys__gen__physical_definition
            '"rw_math_vpu__vector3"': rw_math_vpu__vector3
            '"float32_t"': float32_t
            '"cgs_resource__handle"': cgs_resource__handle
            '"rw_math_vpu__matrix44affine"': rw_math_vpu__matrix44affine
            '"rw_math_vpu__vector4"': rw_math_vpu__vector4
            '"uint16_t"': uint16_t
            '"int32_t"': int32_t
            '"genesys__gen__corona"': genesys__gen__corona
            '"genesys__gen__wcplay_sound_behaviour"': genesys__gen__wcplay_sound_behaviour
            '"genesys__gen__wcvfx_behaviour"': genesys__gen__wcvfx_behaviour
            '"t_00_00_2e__a1"': t_00_00_2e__a1
            '"genesys__gen__corona__glow"': genesys__gen__corona__glow
            '"genesys__gen__corona__env_map_glow"': genesys__gen__corona__env_map_glow
            '"genesys__gen__corona__beam"': genesys__gen__corona__beam
            '"genesys__gen__corona__flare"': genesys__gen__corona__flare
            '"genesys__gen__wcvfx_behaviour__coronas"': genesys__gen__wcvfx_behaviour__coronas
            '"genesys__gen__wcvfx_behaviour__spot_effects"': genesys__gen__wcvfx_behaviour__spot_effects
            '"genesys__gen__wcvfx_behaviour__lights"': genesys__gen__wcvfx_behaviour__lights
            '"genesys__gen__wcplay_sound_behaviour__prop_surface_sound"': genesys__gen__wcplay_sound_behaviour__prop_surface_sound
            '"genesys__gen__make_physical_behaviour"': genesys__gen__make_physical_behaviour
            '"genesys__gen__wcremove_world_entity_behaviour"': genesys__gen__wcremove_world_entity_behaviour
            '"genesys__object"': genesys__object
            '"int16_t"': int16_t
            '"t_00_09_37__a3"': t_00_09_37__a3
            '"genesys__gen__game_mode"': genesys__gen__game_mode
            '"genesys__gen__event"': genesys__gen__event
            '"genesys__gen__online_event"': genesys__gen__online_event
            '"genesys__gen__event_arena"': genesys__gen__event_arena
            '"genesys__gen__event_arena_data"': genesys__gen__event_arena_data
            '"uint8_t"': uint8_t
            '"genesys__gen__score_view_model"': genesys__gen__score_view_model
            '"genesys__gen__score_view_model__score_data"': genesys__gen__score_view_model__score_data
            '"genesys__gen__game_mode__score_override"': genesys__gen__game_mode__score_override
            '"genesys__gen__chevron"': genesys__gen__chevron
            '"genesys__gen__offline_event"': genesys__gen__offline_event
            '"t_00_05__f7_0e"': t_00_05__f7_0e
            '"genesys__gen__aiplayer_instance"': genesys__gen__aiplayer_instance
            '"genesys__gen__offline_event__custom_chevrons"': genesys__gen__offline_event__custom_chevrons
            '"genesys__gen__custom_chevron"': genesys__gen__custom_chevron
            '"gen_obj"': gen_obj
            '"ff__ff__ff__f8"': ff__ff__ff__f8
            '"genesys__gen__car_select_data"': genesys__gen__car_select_data
            '"genesys__gen__entitlement"': genesys__gen__entitlement
            '"genesys__gen__event_list"': genesys__gen__event_list
            '"genesys__gen__event_location"': genesys__gen__event_location
            '"genesys__gen__game_pack"': genesys__gen__game_pack
            '"genesys__gen__gameplay_milestone"': genesys__gen__gameplay_milestone
            '"genesys__gen__game_rank"': genesys__gen__game_rank
            '"genesys__gen__game_unlock"': genesys__gen__game_unlock
            '"t_0c_96_6a_95"': t_0c_96_6a_95
            '"genesys__gen__game_unlock__event"': genesys__gen__game_unlock__event
            '"genesys__gen__game_unlock__milestone"': genesys__gen__game_unlock__milestone
            '"genesys__gen__game_unlock_list"': genesys__gen__game_unlock_list
            '"genesys__gen__nucleus_entitlement_tag"': genesys__gen__nucleus_entitlement_tag
            '"genesys__gen__nucleus_entitlement_tags"': genesys__gen__nucleus_entitlement_tags
            '"genesys__gen__nucleus_grant_mappings_list"': genesys__gen__nucleus_grant_mappings_list
            '"genesys__gen__road_block_definition"': genesys__gen__road_block_definition
            '"genesys__gen__road_block_layer"': genesys__gen__road_block_layer
            '"genesys__gen__store_item"': genesys__gen__store_item
            '"genesys__gen__store_pack"': genesys__gen__store_pack
            '"genesys__gen__store_pack_list"': genesys__gen__store_pack_list
            '"genesys__gen__thankyou_mapping"': genesys__gen__thankyou_mapping
            '"genesys__gen__thank_you_screen_item"': genesys__gen__thank_you_screen_item
            '"genesys__gen__uicamera"': genesys__gen__uicamera
            '"t_00_00_2f__c8"': t_00_00_2f__c8
            '"t_00_00_2f__d0"': t_00_00_2f__d0
            '"genesys__gen__car_select_data__sequences"': genesys__gen__car_select_data__sequences
            '"genesys__gen__gameplay_milestone__entry"': genesys__gen__gameplay_milestone__entry
            '"genesys__gen__nucleus_grant_mappings_list__mapping"': genesys__gen__nucleus_grant_mappings_list__mapping
            '"genesys__gen__road_block_layer__item"': genesys__gen__road_block_layer__item
            '"genesys__gen__upgrade_package"': genesys__gen__upgrade_package
            '"genesys__gen__device_grant_upgrade_package"': genesys__gen__device_grant_upgrade_package
            '"genesys__gen__performance_upgrade_package"': genesys__gen__performance_upgrade_package
            '"t_00_04_5f__b1"': t_00_04_5f__b1
            '"genesys__gen__rollout"': genesys__gen__rollout
            '"genesys__gen__perk"': genesys__gen__perk
            '"genesys__gen__perk_level"': genesys__gen__perk_level
            '"genesys__gen__game_rule"': genesys__gen__game_rule
            '"genesys__gen__nitrous_earning_game_rule"': genesys__gen__nitrous_earning_game_rule
            '"genesys__gen__nitrous_burning_game_rule"': genesys__gen__nitrous_burning_game_rule
            '"genesys__gen__impact_protection_game_rule"': genesys__gen__impact_protection_game_rule
            '"genesys__gen__impact_damage_game_rule"': genesys__gen__impact_damage_game_rule
            '"genesys__gen__rollout__weapon_data"': genesys__gen__rollout__weapon_data
            '"genesys__gen__scoring_action"': genesys__gen__scoring_action
            '"t_00_05__f3_93"': t_00_05__f3_93
            '"genesys__gen__heat_level"': genesys__gen__heat_level
            '"t_00_05__f6_43"': t_00_05__f6_43
            '"t_00_06__cc_72"': t_00_06__cc_72
            '"genesys__gen__gameplay_trigger__output__sequence_output"': genesys__gen__gameplay_trigger__output__sequence_output
            '"t_00_06__cc_77"': t_00_06__cc_77
            '"genesys__gen__aiplayer_type"': genesys__gen__aiplayer_type
            '"t_00_06__fa_70"': t_00_06__fa_70
            '"t_00_06__fa_71"': t_00_06__fa_71
            '"t_00_06__fa_8a"': t_00_06__fa_8a
            '"genesys__gen__gameplay_trigger"': genesys__gen__gameplay_trigger
            '"genesys__gen__gameplay_trigger__input"': genesys__gen__gameplay_trigger__input
            '"genesys__gen__gameplay_trigger__output"': genesys__gen__gameplay_trigger__output
            '"genesys__gen__heat_level__cop_type"': genesys__gen__heat_level__cop_type
            '"genesys__gen__roadblock_instance"': genesys__gen__roadblock_instance
            '"t_00_09_37_93"': t_00_09_37_93
            '"genesys__gen__environment_keyframe"': genesys__gen__environment_keyframe
            '"genesys__gen__environment_keyframe__light_rig"': genesys__gen__environment_keyframe__light_rig
            '"genesys__gen__environment_keyframe__fog"': genesys__gen__environment_keyframe__fog
            '"genesys__gen__environment_keyframe__sky"': genesys__gen__environment_keyframe__sky
            '"genesys__gen__environment_keyframe__clouds"': genesys__gen__environment_keyframe__clouds
            '"genesys__gen__environment_keyframe__camera"': genesys__gen__environment_keyframe__camera
            '"genesys__gen__environment_keyframe__vfx"': genesys__gen__environment_keyframe__vfx
            '"genesys__gen__environment_keyframe__mini__dof"': genesys__gen__environment_keyframe__mini__dof
            '"genesys__gen__environment_keyframe__heat_haze"': genesys__gen__environment_keyframe__heat_haze
            '"genesys__gen__environment_keyframe__weather"': genesys__gen__environment_keyframe__weather
            '"genesys__gen__environment_timeline"': genesys__gen__environment_timeline
            '"genesys__gen__environment_timeline__timeline_keyframe"': genesys__gen__environment_timeline__timeline_keyframe
            '"genesys__gen__light__base"': genesys__gen__light__base
            '"genesys__gen__light__cone"': genesys__gen__light__cone
            '"genesys__gen__mixer_channel"': genesys__gen__mixer_channel
            '"genesys__gen__mixing_group"': genesys__gen__mixing_group
            '"genesys__gen__post_fx_keyframe"': genesys__gen__post_fx_keyframe
            '"genesys__gen__post_fxstate"': genesys__gen__post_fxstate
            '"genesys__gen__sound_distance_falloff"': genesys__gen__sound_distance_falloff
            '"t_34_26_5a_75"': t_34_26_5a_75
            '"genesys__gen__uielement_base__behaviour"': genesys__gen__uielement_base__behaviour
            '"genesys__gen__uielement_base__effect_constant"': genesys__gen__uielement_base__effect_constant
            '"genesys__gen__uielement_base__rendering_data"': genesys__gen__uielement_base__rendering_data
            '"t_8e_7d_5f_21"': t_8e_7d_5f_21
            '"genesys__gen__uielement_base__timeline__behaviour"': genesys__gen__uielement_base__timeline__behaviour
            '"c9_7e__aa__da"': c9_7e__aa__da
            '"genesys__gen__uielement_base__timeline"': genesys__gen__uielement_base__timeline
            '"da__dc_9b_17"': da__dc_9b_17
            '"genesys__gen__uielement_base"': genesys__gen__uielement_base
            '"t_35__d6_2d_64"': t_35__d6_2d_64
            '"t_5b_33_21__f5"': t_5b_33_21__f5
            '"d0_00_70_01"': d0_00_70_01
            '"t_05_89__a9_77"': t_05_89__a9_77
            '"t_06__a9_64__cd"': t_06__a9_64__cd
            '"genesys__gen__uielement__element_stack"': genesys__gen__uielement__element_stack
            '"genesys__gen__uielement__element_stack__template"': genesys__gen__uielement__element_stack__template
            '"genesys__gen__uielement__mini_map"': genesys__gen__uielement__mini_map
            '"genesys__gen__uielement__main_map"': genesys__gen__uielement__main_map
            '"genesys__gen__uielement__mask"': genesys__gen__uielement__mask
            '"genesys__gen__uielement__movie_player"': genesys__gen__uielement__movie_player
            '"genesys__gen__uielement__movie_player__dimensions"': genesys__gen__uielement__movie_player__dimensions
            '"genesys__gen__uielement__prototype_image"': genesys__gen__uielement__prototype_image
            '"genesys__gen__uielement__prototype_image__tint_properties"': genesys__gen__uielement__prototype_image__tint_properties
            '"genesys__gen__uielement__prototype_image__opacity"': genesys__gen__uielement__prototype_image__opacity
            '"genesys__gen__uielement__prototype_label"': genesys__gen__uielement__prototype_label
            '"genesys__gen__uielement__prototype_label__string"': genesys__gen__uielement__prototype_label__string
            '"genesys__gen__uielement__prototype_label__text_properties"': genesys__gen__uielement__prototype_label__text_properties
            '"t_70__f4__bb__e0"': t_70__f4__bb__e0
            '"genesys__gen__uielement__prototype_scrolling_text"': genesys__gen__uielement__prototype_scrolling_text
            '"genesys__gen__uielement__prototype_scrolling_text__string"': genesys__gen__uielement__prototype_scrolling_text__string
            '"genesys__gen__uielement__prototype_scrolling_text__text_properties"': genesys__gen__uielement__prototype_scrolling_text__text_properties
            '"f7__ff__d1__f8"': f7__ff__d1__f8
            '"d7__b2_21__da"': d7__b2_21__da
            '"genesys__gen__uielement__prototype_shape"': genesys__gen__uielement__prototype_shape
            '"t_96__c1_53_69"': t_96__c1_53_69
            '"genesys__gen__uielement__scrollable_label"': genesys__gen__uielement__scrollable_label
            '"t_40_99__f3__ac"': t_40_99__f3__ac
            '"genesys__gen__uielement__scrollable_label__string"': genesys__gen__uielement__scrollable_label__string
            '"genesys__gen__uielement__scrollable_label__text_properties"': genesys__gen__uielement__scrollable_label__text_properties
            '"t_35__a6_06_1e"': t_35__a6_06_1e
            '"genesys__gen__uilayout"': genesys__gen__uilayout
            '"genesys__gen__uilayout_instance_params"': genesys__gen__uilayout_instance_params
            '"genesys__gen__uimaterial"': genesys__gen__uimaterial
            '"genesys__gen__uitechnique"': genesys__gen__uitechnique
            '"t_00_00_2f__f0"': t_00_00_2f__f0
            '"t_00_00_30_1d"': t_00_00_30_1d
            '"t_00_00_30_22"': t_00_00_30_22
            '"t_00_00_30_27"': t_00_00_30_27
            '"t_00_00_30_35"': t_00_00_30_35
            '"t_00_00_30_38"': t_00_00_30_38
            '"t_00_00_30_3d"': t_00_00_30_3d
            '"t_00_00_31__b6"': t_00_00_31__b6
            '"t_00_00_31__ba"': t_00_00_31__ba
            '"t_00_00_31__c4"': t_00_00_31__c4
            '"t_00_00_31__ca"': t_00_00_31__ca
            '"t_00_00_31__d2"': t_00_00_31__d2
            '"genesys__gen__light__base__flash_pattern"': genesys__gen__light__base__flash_pattern
            '"genesys__gen__post_fx_keyframe__bloom"': genesys__gen__post_fx_keyframe__bloom
            '"rw_math_vpu__vector2"': rw_math_vpu__vector2
            '"genesys__gen__post_fx_keyframe__vignette"': genesys__gen__post_fx_keyframe__vignette
            '"genesys__gen__post_fx_keyframe__general"': genesys__gen__post_fx_keyframe__general
            '"genesys__gen__post_fx_keyframe__depth_of__field"': genesys__gen__post_fx_keyframe__depth_of__field
            '"genesys__gen__post_fx_keyframe__stereo_3d"': genesys__gen__post_fx_keyframe__stereo_3d
            '"genesys__gen__post_fxstate__colour_cube_settings"': genesys__gen__post_fxstate__colour_cube_settings
            '"genesys__gen__post_fxstate__value_modifier"': genesys__gen__post_fxstate__value_modifier
            '"genesys__gen__uilayout_instance_params__transform_components"': genesys__gen__uilayout_instance_params__transform_components
            '"genesys__gen__uilayout_instance_params__timeline_parameters"': genesys__gen__uilayout_instance_params__timeline_parameters
            '"genesys__gen__sequence_item"': genesys__gen__sequence_item
            '"genesys__gen__wave_sequence_item"': genesys__gen__wave_sequence_item
            '"t_00_03__f3__c4"': t_00_03__f3__c4
            '"genesys__gen__animation_sequence_item"': genesys__gen__animation_sequence_item
            '"genesys__gen__wcsequence_behaviour"': genesys__gen__wcsequence_behaviour
            '"genesys__gen__sequence_item__modulating_double_value"': genesys__gen__sequence_item__modulating_double_value
            '"t_00_03__f6_5b"': t_00_03__f6_5b
            '"t_00_03__f6_83"': t_00_03__f6_83
            '"genesys__gen__wave_sequence_item__fade"': genesys__gen__wave_sequence_item__fade
            '"genesys__gen__bus_mixer_channel_sequence_item"': genesys__gen__bus_mixer_channel_sequence_item
            '"genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value"': genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value
            '"t_00_03__f6__d5"': t_00_03__f6__d5
            '"genesys__gen__physics_sequence_item"': genesys__gen__physics_sequence_item
            '"genesys__gen__physics_sequence_item__physics_double_value"': genesys__gen__physics_sequence_item__physics_double_value
            '"t_00_03__f7_15"': t_00_03__f7_15
            '"genesys__gen__sequence_timeline_controller"': genesys__gen__sequence_timeline_controller
            '"genesys__gen__sequence"': genesys__gen__sequence
            '"genesys__gen__jump_timeline_controller"': genesys__gen__jump_timeline_controller
            '"genesys__gen__layout_sequence_item"': genesys__gen__layout_sequence_item
            '"t_00_03__f8_50"': t_00_03__f8_50
            '"genesys__gen__post_fxsequence_item"': genesys__gen__post_fxsequence_item
            '"t_00_04_5e__f1"': t_00_04_5e__f1
            '"t_00_04_5f__ad"': t_00_04_5f__ad
            '"t_00_04_63_4a"': t_00_04_63_4a
            '"genesys__gen__weapon_upgrade"': genesys__gen__weapon_upgrade
            '"genesys__gen__silent_launch_weapon_upgrade"': genesys__gen__silent_launch_weapon_upgrade
            '"genesys__gen__extra_ammo_weapon_upgrade"': genesys__gen__extra_ammo_weapon_upgrade
            '"genesys__gen__arc_light_cone_upgrade"': genesys__gen__arc_light_cone_upgrade
            '"genesys__gen__spike_strip_body_blow_upgrade"': genesys__gen__spike_strip_body_blow_upgrade
            '"genesys__gen__spike_strip_blowout_upgrade"': genesys__gen__spike_strip_blowout_upgrade
            '"genesys__gen__dust_storm_minimap_upgrade"': genesys__gen__dust_storm_minimap_upgrade
            '"genesys__gen__hypox_particles_weapon_upgrade"': genesys__gen__hypox_particles_weapon_upgrade
            '"genesys__gen__vfx_spot_effect_sequence_item"': genesys__gen__vfx_spot_effect_sequence_item
            '"genesys__gen__add_behaviour_sequence_item"': genesys__gen__add_behaviour_sequence_item
            '"genesys__gen__hud_style_sequence_item"': genesys__gen__hud_style_sequence_item
            '"t_00_05__ab_65"': t_00_05__ab_65
            '"genesys__gen__apply_vehicle_kick_sequence_item"': genesys__gen__apply_vehicle_kick_sequence_item
            '"genesys__gen__camera_gameplay_shake_effect"': genesys__gen__camera_gameplay_shake_effect
            '"genesys__gen__camera_gameplay_shake_effect__rotation"': genesys__gen__camera_gameplay_shake_effect__rotation
            '"genesys__gen__camera_gameplay_shake_effect__translation"': genesys__gen__camera_gameplay_shake_effect__translation
            '"genesys__gen__camera_gameplay_shake_effect__rotation__axis_params"': genesys__gen__camera_gameplay_shake_effect__rotation__axis_params
            '"genesys__gen__camera_gameplay_shake_effect__translation__axis_params"': genesys__gen__camera_gameplay_shake_effect__translation__axis_params
            '"genesys__gen__weapon"': genesys__gen__weapon
            '"genesys__gen__weapon_list"': genesys__gen__weapon_list
            '"genesys__gen__spike_strip_weapon"': genesys__gen__spike_strip_weapon
            '"genesys__gen__smoke_screen_weapon"': genesys__gen__smoke_screen_weapon
            '"genesys__gen__flash_headlights_weapon"': genesys__gen__flash_headlights_weapon
            '"t_00_06__cc_2f"': t_00_06__cc_2f
            '"genesys__gen__uicolour"': genesys__gen__uicolour
            '"rw__rgba"': rw__rgba
            '"t_00_07_33__ee"': t_00_07_33__ee
            '"genesys__gen__camera_shake_sequence_item"': genesys__gen__camera_shake_sequence_item
            '"genesys__gen__event_trigger_sequence_item"': genesys__gen__event_trigger_sequence_item
            '"t_00_07_57_09"': t_00_07_57_09
            '"genesys__gen__weapon_recharge_data"': genesys__gen__weapon_recharge_data
            '"genesys__gen__mixer_channel__priority"': genesys__gen__mixer_channel__priority
            '"genesys__gen__vision_mode"': genesys__gen__vision_mode
            '"genesys__gen__thermal_vision_mode"': genesys__gen__thermal_vision_mode
            '"genesys__gen__environment_timeline_sequence_item"': genesys__gen__environment_timeline_sequence_item
            '"genesys__gen__set_vision_mode_type_sequence_item"': genesys__gen__set_vision_mode_type_sequence_item
            '"t_00_07__bc_8a"': t_00_07__bc_8a
            '"genesys__gen__thermal_vision_mode_properties"': genesys__gen__thermal_vision_mode_properties
            '"genesys__gen__fast_launch_weapon_upgrade"': genesys__gen__fast_launch_weapon_upgrade
            '"genesys__gen__light__point"': genesys__gen__light__point
            '"genesys__gen__searchlight_behaviour"': genesys__gen__searchlight_behaviour
            '"a7_6d_0e_28"': a7_6d_0e_28
            '"genesys__gen__text_style"': genesys__gen__text_style
            '"t_95_95_0d_30"': t_95_95_0d_30
            '"genesys__gen__text_style__text_style_locale"': genesys__gen__text_style__text_style_locale
            '"genesys__gen__wchide_behaviour"': genesys__gen__wchide_behaviour
            '"genesys__gen__wcpath_animation_behaviour"': genesys__gen__wcpath_animation_behaviour
            '"genesys__gen__wcpath_animation_behaviour__animation_path"': genesys__gen__wcpath_animation_behaviour__animation_path
            '"genesys__gen__snap_to_world_behaviour"': genesys__gen__snap_to_world_behaviour
            '"genesys__gen__physical_explosion__non_race_car_explosion"': genesys__gen__physical_explosion__non_race_car_explosion
            '"genesys__gen__physical_explosion__race_car_on_ground_explosion"': genesys__gen__physical_explosion__race_car_on_ground_explosion
            '"genesys__gen__physical_explosion__race_car_in_air_explosion"': genesys__gen__physical_explosion__race_car_in_air_explosion
            '"genesys__gen__physical_explosion__gameplay_explosion"': genesys__gen__physical_explosion__gameplay_explosion
            '"genesys__gen__mine_weapon"': genesys__gen__mine_weapon
            '"genesys__gen__physical_explosion"': genesys__gen__physical_explosion
            '"genesys__gen__teflon_slick_weapon"': genesys__gen__teflon_slick_weapon
            '"genesys__gen__grenade_weapon"': genesys__gen__grenade_weapon
            '"genesys__gen__flash_bang_weapon"': genesys__gen__flash_bang_weapon
            '"genesys__gen__jammer_weapon"': genesys__gen__jammer_weapon
            '"genesys__gen__speedbreaker_weapon"': genesys__gen__speedbreaker_weapon
            '"genesys__gen__slow_mo_sequence_item"': genesys__gen__slow_mo_sequence_item
            '"genesys__gen__helicopter_weapon"': genesys__gen__helicopter_weapon
            '"genesys_obj_collection"': genesys_obj_collection
            '"generic_gen_object"': generic_gen_object
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