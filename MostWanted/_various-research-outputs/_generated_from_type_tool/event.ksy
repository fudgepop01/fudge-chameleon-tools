meta:
  id: event
  endian: le
  encoding: ascii
  # 146165144147145160157160060061o
  imports:
    - genesys_object
    - offline_event
seq:
  - {id: header, type: genesys_object}
  - {id: unknown_id, type: u4}
  # 121 events in total
  - {id: event_start_offset, type: "u4"}
  - {id: event_count, type: "u4"}
  - {id: all_events, type: "ptr('event_switcher')", repeat: expr, repeat-expr: event_count}  
  # - {id: something_offsets, type: u4}
# instances: {
#   circuit:
#     type: circuit_collection
#   sprint:
#     type: sprint_collection
#   speedrun:
#     type: speedrun_collection
#   smash_n_grab:
#     type: smash_n_grab_collection
#   ambush:
#     type: ambush_collection
#   drift:
#     type: drift_collection
#   most_wanted:
#     type: most_wanted_collection
#   special:
#     type: special_colleciton
#   multiplayer_races:
#     type: multiplayer_race_collection
#   multiplayer_challenges:
#     type: multiplayer_challenge_collection
# }
enums:
  e_condition_type:
    0: win
    1: lose
    2: special
  e_condition_test_type:
    # 0: unknown
    1: racers_finished
    2: drift
    3: racers_wrecked
    4: cops_wrecked
    5: binding
    # 6: unknown
    7: player_wrecked
    8: beat_time
    9: top_speed
    10: starting_score
    # 11: unknown
    12: air_time
  e_online_challenge_involvement:
    0: individual
    1: team
    2: everyone
  e_online_challenge_fail:
    0: allow_fail
    1: no_fail_maybe
  e_online_elimination_type:
    0: none
    1: unk1
    2: unk2
    3: unk3
    4: random
  e_online_challenge_type:
    0: speed_test
    1: team
    2: social
  e_parent_event_type:
    0: mp_speedtest
    1: mp_challenge
types:
  # circuit_collection:
  #   instances:
  #     # continental_drift_c: { pos: 2616, type: event_type, size: 0xF0 }
  #     # stock_market_crash_c: { pos: 4360, type: event_type, size: 0xF0 }
  #     # crash_landing_c: { pos: 5152, type: event_type, size: 0xF0 }
  #     # turf_war_c: { pos: 5960, type: event_type, size: 0xF0 }
  #     # emmerson_beltway_c: { pos: 6828, type: event_type, size: 0xF0 }
  #     # off_the_grid_c: { pos: 8412, type: event_type, size: 0xF0 }
  #     # turbulence_c: { pos: 10584, type: event_type, size: 0xF0 }
  #     # power_struggle_c: { pos: 14916, type: event_type, size: 0xF0 }
  #     # red_shift_c: { pos: 17004, type: event_type, size: 0xF0 }
  #     # cold_burn_c: { pos: 18416, type: event_type, size: 0xF0 }
  #     # import_duty_c: { pos: 19976, type: event_type, size: 0xF0 }
  #     # cruise_control_c: { pos: 21060, type: event_type, size: 0xF0 }
  #     # mud_bath_c: { pos: 24060, type: event_type, size: 0xF0 }
  #     # stopping_power_c: { pos: 27740, type: event_type, size: 0xF0 }
  #     # crush_hour_c: { pos: 29564, type: event_type, size: 0xF0 }
  #     # jumping_jacks_c: { pos: 38208, type: event_type, size: 0xF0 }
  #     # collateral_damage_c: { pos: 50036, type: event_type, size: 0xF0 }
  #     # green_zone_c: { pos: 148932, type: event_type, size: 0xF0 }
  #     # around_the_world_c: { pos: 150680, type: event_type, size: 0xF0 }
  #     # mayhem_c: { pos: 170192, type: event_type, size: 0xF0 }
  #     # round_trip_c: { pos: 176016, type: event_type, size: 0xF0 }
  #     inner_city_pressure_c: { pos: 196984, type: offline_event }
  # ambush_collection:
  #   instances:
  #     liberty_park_a: { pos: 51136, type: event_type, size: 0xF0 }
  #     double_parked_a: { pos: 76356, type: event_type, size: 0xF0 }
  #     the_fugitive_a: { pos: 79636, type: event_type, size: 0xF0 }
  #     storehouse_stakeout_a: { pos: 82420, type: event_type, size: 0xF0 }
  #     bloody_nose_a: { pos: 83648, type: event_type, size: 0xF0 }
  #     the_hunted_a: { pos: 84652, type: event_type, size: 0xF0 }
  #     jailbird_a: { pos: 195152, type: event_type, size: 0xF0 }
  # sprint_collection:
  #   instances:
  #     rolling_stock_s: { pos: 3188, type: event_type, size: 0xF0 }
  #     harbor_run_s: { pos: 7684, type: event_type, size: 0xF0 }
  #     crashdown_s: { pos: 9460, type: event_type, size: 0xF0 }
  #     park_and_country_s: { pos: 11536, type: event_type, size: 0xF0 }
  #     park_and_ride_s: { pos: 12148, type: event_type, size: 0xF0 }
  #     cannonball_run_s: { pos: 12868, type: event_type, size: 0xF0 }
  #     pumping_iron_s: { pos: 13412, type: event_type, size: 0xF0 }
  #     straight_to_the_point_s: { pos: 15460, type: event_type, size: 0xF0 }
  #     arch_enemies_s: { pos: 16296, type: event_type, size: 0xF0 }
  #     power_play_s: { pos: 22120, type: event_type, size: 0xF0 }
  #     chain_reaction_s: { pos: 24752, type: event_type, size: 0xF0 }
  #     trail_blazer_s: { pos: 26388, type: event_type, size: 0xF0 }
  #     sports_sprint_s: { pos: 26992, type: event_type, size: 0xF0 }
  #     burning_rubber_s: { pos: 28440, type: event_type, size: 0xF0 }
  #     industrial_revolution_s: { pos: 36108, type: event_type, size: 0xF0 }
  #     running_the_gauntlet_s: { pos: 52396, type: event_type, size: 0xF0 }
  #     sprint_eastward_s: { pos: 53988, type: event_type, size: 0xF0 }
  #     keys_to_the_city_s: { pos: 143948, type: event_type, size: 0xF0 }
  #     downfall_s: { pos: 144872, type: event_type, size: 0xF0 }
  #     terminal_velocity_s: { pos: 145852, type: event_type, size: 0xF0 }
  #     steel_city_s: { pos: 146744, type: event_type, size: 0xF0 }
  #     drive_hard_s: { pos: 147688, type: event_type, size: 0xF0 }
  #     burning_bridges_s: { pos: 149784, type: event_type, size: 0xF0 }
  #     the_enforcer_s: { pos: 152232, type: event_type, size: 0xF0 }
  #     get_to_callahan_s: { pos: 162900, type: event_type, size: 0xF0 }
  #     license_to_thrill_s: { pos: 163708, type: event_type, size: 0xF0 }
  #     bootlegging_s: { pos: 164840, type: event_type, size: 0xF0 }
  #     sudden_impact_s: { pos: 168060, type: event_type, size: 0xF0 }
  #     bullet_train_s: { pos: 169124, type: event_type, size: 0xF0 }
  #     deadline_s: { pos: 171064, type: event_type, size: 0xF0 }
  #     live_and_let_drive_s: { pos: 171908, type: event_type, size: 0xF0 }
  #     pulp_friction_s: { pos: 172808, type: event_type, size: 0xF0 }
  #     braking_traction_s: { pos: 173604, type: event_type, size: 0xF0 }
  #     aerial_agression_s: { pos: 174416, type: event_type, size: 0xF0 }
  #     high_stakes_s: { pos: 192032, type: event_type, size: 0xF0 }
  #     bring_the_noise_s: { pos: 193184, type: event_type, size: 0xF0 }
  # speedrun_collection:
  #   instances:
  #     turbine_sr: { pos: 35452, type: event_type, size: 0xF0 }
  #     gravity_sr: { pos: 35740, type: event_type, size: 0xF0 }
  #     downtown_run_sr: { pos: 36884, type: event_type, size: 0xF0 }
  #     downgraded_sr: { pos: 37216, type: event_type, size: 0xF0 }
  #     needle_point_sr: { pos: 37560, type: event_type, size: 0xF0 }
  #     to_the_bridge_sr: { pos: 37900, type: event_type, size: 0xF0 }
  #     the_getaway_sr: { pos: 49152, type: event_type, size: 0xF0 }
  #     industiral_way_sr: { pos: 49508, type: event_type, size: 0xF0 }
  #     fast_track_sr: { pos: 53668, type: event_type, size: 0xF0 }
  #     get_to_the_chopper_sr: { pos: 82092, type: event_type, size: 0xF0 }
  #     critical_path_sr: { pos: 148344, type: event_type, size: 0xF0 }
  #     the_descent_sr: { pos: 151924, type: event_type, size: 0xF0 }
  #     life_for_speed_sr: { pos: 153092, type: event_type, size: 0xF0 }
  #     full_overdrive_sr: { pos: 153788, type: event_type, size: 0xF0 }
  #     full_throttle_sr: { pos: 154228, type: event_type, size: 0xF0 }
  #     running_wild_sr: { pos: 174024, type: event_type, size: 0xF0 }
  #     fuelled_sr: { pos: 192792, type: event_type, size: 0xF0 }
  #     speed_demon_sr: { pos: 193652, type: event_type, size: 0xF0 }
  # smash_n_grab_collection:
  #   instances:
  #     duty_free_sg: { pos: 178280, type: event_type, size: 0xF0 }
  #     air_raid_sg_0: { pos: 190072, type: event_type, size: 0xF0 }
  #     air_raid_sg_1: { pos: 190072, type: event_type, size: 0xF0 }
  #     green_belt_sg_0: { pos: 190608, type: event_type, size: 0xF0 }
  #     green_belt_sg_1: { pos: 190608, type: event_type, size: 0xF0 }
  #     green_belt_sg_2: { pos: 190608, type: event_type, size: 0xF0 }
  #     ship_to_shore_sg_0: { pos: 191068, type: event_type, size: 0xF0 }
  #     ship_to_shore_sg_1: { pos: 191068, type: event_type, size: 0xF0 }
  #     ship_to_shore_sg_2: { pos: 191068, type: event_type, size: 0xF0 }
  #     ship_to_shore_sg_3: { pos: 191068, type: event_type, size: 0xF0 }
  #     destruction_site_sg_0: { pos: 191524, type: event_type, size: 0xF0 }
  #     destruction_site_sg_1: { pos: 191524, type: event_type, size: 0xF0 }
  #     destruction_site_sg_2: { pos: 191524, type: event_type, size: 0xF0 }
  #     destruction_site_sg_3: { pos: 191524, type: event_type, size: 0xF0 }
  #     destruction_site_sg_4: { pos: 191524, type: event_type, size: 0xF0 } 
  # drift_collection:
  #   instances:
  #     sidewinder_d: { pos: 162012, type: event_type, size: 0xF0 }
  #     # easy_drifter_d: { pos: 162472, type: event_type, size: 0xF0 }
  #     # power_slide_d: { pos: 176924, type: event_type, size: 0xF0 }
  #     # drift_city_d: { pos: 188736, type: event_type, size: 0xF0 }
  #     # air_brake_d: { pos: 189376, type: event_type, size: 0xF0 }
  # most_wanted_collection:
  #   instances:
  #     ev41_most_wanted_6: { pos: 41124, type: event_type, size: 0xF0 }
  #     ev45_most_wanted_8: { pos: 50676, type: event_type, size: 0xF0 }
  #     ev47_most_wanted_5: { pos: 51492, type: event_type, size: 0xF0 }
  #     ev52_most_wanted_10: { pos: 76696, type: event_type, size: 0xF0 }
  #     ev53_most_wanted_9: { pos: 77352, type: event_type, size: 0xF0 }
  #     ev54_most_wanted_7: { pos: 78256, type: event_type, size: 0xF0 }
  #     ev56_most_wanted_1: { pos: 80032, type: event_type, size: 0xF0 }
  #     ev59_most_wanted_2: { pos: 82760, type: event_type, size: 0xF0 }
  #     ev61_most_wanted_3: { pos: 84016, type: event_type, size: 0xF0 }
  #     ev63_most_wanted_4: { pos: 102452, type: event_type, size: 0xF0 }
  #     ev74_most_wanted_venom: { pos: 151536, type: event_type, size: 0xF0 }
  #     ev85_most_wanted_gtr: { pos: 165840, type: event_type, size: 0xF0 }
  #     ev86_most_wanted_gt500: { pos: 167084, type: event_type, size: 0xF0 }
  #     ev99_most_wanted_spyder: { pos: 186256, type: event_type, size: 0xF0 }
  # special_colleciton:
  #   instances:
  #     ev1_freedrive: { pos: 1872, type: event_type, size: 0xF0 }
  #     ev2_freedrive: { pos: 2120, type: event_type, size: 0xF0 }
  #     ev3_freedrive: { pos: 2368, type: event_type, size: 0xF0 }
  #     ev64_welcome_to_fairhaven: { pos: 103096, type: event_type, size: 0xF0 }
  # multiplayer_race_collection:
  #   instances:
  #     multiplayer_evt0: {pos: 1712, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt1: {pos: 23836, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt2: {pos: 27628, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt3: {pos: 31924, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt4: {pos: 32236, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt5: {pos: 32728, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt6: {pos: 32888, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt7: {pos: 33112, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt8: {pos: 33604, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt9: {pos: 33892, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt10: {pos: 34204, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt11: {pos: 34556, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt12: {pos: 34716, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt13: {pos: 34876, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt14: {pos: 35164, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt15: {pos: 43196, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt16: {pos: 44192, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt17: {pos: 58972, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt18: {pos: 59260, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt19: {pos: 59612, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt20: {pos: 59772, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt21: {pos: 59932, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt22: {pos: 60156, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt23: {pos: 61212, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt24: {pos: 61500, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt25: {pos: 61788, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt26: {pos: 62076, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt27: {pos: 64280, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt28: {pos: 68316, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt29: {pos: 71820, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt30: {pos: 72044, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt31: {pos: 72268, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt32: {pos: 72492, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt33: {pos: 72716, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt34: {pos: 72876, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt35: {pos: 73036, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt36: {pos: 73196, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt37: {pos: 73356, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt38: {pos: 73516, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt39: {pos: 73676, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt40: {pos: 73836, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt41: {pos: 73996, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt42: {pos: 74156, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt43: {pos: 74316, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt44: {pos: 74476, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt45: {pos: 75012, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt46: {pos: 75172, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt47: {pos: 75332, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt48: {pos: 75556, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt49: {pos: 75780, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt50: {pos: 76068, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt51: {pos: 103492, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt52: {pos: 103604, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt53: {pos: 103716, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt54: {pos: 103876, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt55: {pos: 112420, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt56: {pos: 112580, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt57: {pos: 112740, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt58: {pos: 113156, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt59: {pos: 113572, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt60: {pos: 113796, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt61: {pos: 114020, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt62: {pos: 114256, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt63: {pos: 114492, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt64: {pos: 114792, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt65: {pos: 118972, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt66: {pos: 119132, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt67: {pos: 119292, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt68: {pos: 119452, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt69: {pos: 119612, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt70: {pos: 119772, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt71: {pos: 119932, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt72: {pos: 120360, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt73: {pos: 120788, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt74: {pos: 121204, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt75: {pos: 121620, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt76: {pos: 121908, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt77: {pos: 122196, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt78: {pos: 122484, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt79: {pos: 125256, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt80: {pos: 125416, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt81: {pos: 125528, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt82: {pos: 125816, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt83: {pos: 126104, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt84: {pos: 126328, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt85: {pos: 126552, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt86: {pos: 126840, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt87: {pos: 127128, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt88: {pos: 127480, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt89: {pos: 127832, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt90: {pos: 128120, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt91: {pos: 128408, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt92: {pos: 128632, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt93: {pos: 128856, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt94: {pos: 129296, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt95: {pos: 129736, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt96: {pos: 129896, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt97: {pos: 130056, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt98: {pos: 130280, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt99: {pos: 130504, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt100: {pos: 130792, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt101: {pos: 131080, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt102: {pos: 131240, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt103: {pos: 131400, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt104: {pos: 131624, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt105: {pos: 135048, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt106: {pos: 135208, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt107: {pos: 143628, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt108: {pos: 143788, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt109: {pos: 154600, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt110: {pos: 154888, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt111: {pos: 155176, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt112: {pos: 155464, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt113: {pos: 155752, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt114: {pos: 156040, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt115: {pos: 156328, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt116: {pos: 156616, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt117: {pos: 156904, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt118: {pos: 157128, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt119: {pos: 157352, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt120: {pos: 157576, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt121: {pos: 157800, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt122: {pos: 158216, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt123: {pos: 158632, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt124: {pos: 158856, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt125: {pos: 159080, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt126: {pos: 159304, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt127: {pos: 159528, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt128: {pos: 159752, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt129: {pos: 159976, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt130: {pos: 160200, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt131: {pos: 160424, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt132: {pos: 160648, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt133: {pos: 182204, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt134: {pos: 182428, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt135: {pos: 182652, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt136: {pos: 182876, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt137: {pos: 185808, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt138: {pos: 186032, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt139: {pos: 196344, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt140: {pos: 196504, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt141: {pos: 196664, type: multiplayer_race_type, size: 0xF0}
  #     multiplayer_evt142: {pos: 196824, type: multiplayer_race_type, size: 0xF0}
  # multiplayer_challenge_collection:
  #   instances:
  #     multiplayer_challenge_evt0: {pos: 31192, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt1: {pos: 31548, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt2: {pos: 39460, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt3: {pos: 39912, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt4: {pos: 40312, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt5: {pos: 40768, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt6: {pos: 41888, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt7: {pos: 42444, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt8: {pos: 42816, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt9: {pos: 43356, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt10: {pos: 43740, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt11: {pos: 44352, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt12: {pos: 44908, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt13: {pos: 45464, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt14: {pos: 46020, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt15: {pos: 46480, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt16: {pos: 47036, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt17: {pos: 47488, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt18: {pos: 47860, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt19: {pos: 48416, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt20: {pos: 55540, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt21: {pos: 55992, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt22: {pos: 56548, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt23: {pos: 56932, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt24: {pos: 57512, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt25: {pos: 57900, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt26: {pos: 58376, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt27: {pos: 60380, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt28: {pos: 60756, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt29: {pos: 62364, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt30: {pos: 62744, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt31: {pos: 63116, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt32: {pos: 63472, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt33: {pos: 63828, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt34: {pos: 64440, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt35: {pos: 64816, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt36: {pos: 65268, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt37: {pos: 65656, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt38: {pos: 66212, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt39: {pos: 66592, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt40: {pos: 66964, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt41: {pos: 67352, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt42: {pos: 67728, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt43: {pos: 68476, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt44: {pos: 68928, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt45: {pos: 69552, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt46: {pos: 70176, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt47: {pos: 70728, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt48: {pos: 71272, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt49: {pos: 74636, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt50: {pos: 85000, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt51: {pos: 85580, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt52: {pos: 85960, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt53: {pos: 86332, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt54: {pos: 86708, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt55: {pos: 87192, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt56: {pos: 87548, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt57: {pos: 88104, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt58: {pos: 88484, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt59: {pos: 88880, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt60: {pos: 89252, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt61: {pos: 89624, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt62: {pos: 90180, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt63: {pos: 90632, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt64: {pos: 91028, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt65: {pos: 91408, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt66: {pos: 91860, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt67: {pos: 92236, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt68: {pos: 92692, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt69: {pos: 93248, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt70: {pos: 93804, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt71: {pos: 94256, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt72: {pos: 94808, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt73: {pos: 95260, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt74: {pos: 95816, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt75: {pos: 96192, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt76: {pos: 96612, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt77: {pos: 97032, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt78: {pos: 97452, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt79: {pos: 97872, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt80: {pos: 98292, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt81: {pos: 98712, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt82: {pos: 99132, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt83: {pos: 99552, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt84: {pos: 99928, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt85: {pos: 100348, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt86: {pos: 100768, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt87: {pos: 101188, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt88: {pos: 101640, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt89: {pos: 104036, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt90: {pos: 104488, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt91: {pos: 104864, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt92: {pos: 105236, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt93: {pos: 105796, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt94: {pos: 106184, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt95: {pos: 106556, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt96: {pos: 106912, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt97: {pos: 107268, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt98: {pos: 107872, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt99: {pos: 108452, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt100: {pos: 109008, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt101: {pos: 109388, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt102: {pos: 109760, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt103: {pos: 110384, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt104: {pos: 110756, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt105: {pos: 111140, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt106: {pos: 111688, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt107: {pos: 112064, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt108: {pos: 115092, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt109: {pos: 115464, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt110: {pos: 115840, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt111: {pos: 116212, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt112: {pos: 116760, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt113: {pos: 117328, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt114: {pos: 117872, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt115: {pos: 118244, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt116: {pos: 118616, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt117: {pos: 122772, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt118: {pos: 123336, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt119: {pos: 123892, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt120: {pos: 124448, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt121: {pos: 124804, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt122: {pos: 131848, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt123: {pos: 132232, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt124: {pos: 132716, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt125: {pos: 133092, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt126: {pos: 133584, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt127: {pos: 134144, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt128: {pos: 134596, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt129: {pos: 135368, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt130: {pos: 135764, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt131: {pos: 136184, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt132: {pos: 136740, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt133: {pos: 137292, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt134: {pos: 137868, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt135: {pos: 138240, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt136: {pos: 138804, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt137: {pos: 139160, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt138: {pos: 139732, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt139: {pos: 140300, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt140: {pos: 140860, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt141: {pos: 141316, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt142: {pos: 141892, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt143: {pos: 142516, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt144: {pos: 143072, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt145: {pos: 160872, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt146: {pos: 161268, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt147: {pos: 161640, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt148: {pos: 178756, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt149: {pos: 179136, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt150: {pos: 179516, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt151: {pos: 179968, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt152: {pos: 180348, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt153: {pos: 180904, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt154: {pos: 181460, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt155: {pos: 181816, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt156: {pos: 183100, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt157: {pos: 183668, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt158: {pos: 184224, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt159: {pos: 184676, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt160: {pos: 185048, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt161: {pos: 185428, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt162: {pos: 195512, type: multiplayer_challenge_type, size: 0xF0}
  #     multiplayer_challenge_evt163: {pos: 195892, type: multiplayer_challenge_type, size: 0xF0}
  vpu_vector3:
    seq:
      - {id: x, type: f4}
      - {id: y, type: f4}
      - {id: z, type: f4}
      - {id: unused2, type: f4}
  weather_conditions:
    instances:
      wet_roads:
        pos: 0x8
        type: u1
      thunder:
        pos: 0xC
        type: u1
      cold_color_palette:
        pos: 0xD
        type: u1
      alternative:
        pos: 0xE
        type: u1
      rainy_weather:
        pos: 0xF
        type: u1

  temp_event_type:
    seq:
    - {id: race_header, size: 0xC}
    instances:
      evt_type_modifier:
        pos: 0xC
        size: 4
      evt_id:
        pos: 0x10
        type: u4
      event_type_hash:
        pos: 0x14
        type: u4be
      dlc_pack:
        pos: 0x18
        size: 4
      evt_name_id: 
        pos: 0x54
        type: u4be
      weather_config:
        pos: 0x20
        size: 0x30
        type: weather_conditions
      cutscene_id:
        pos: 0x68
        size: 0x4
      file_id:
        pos: 0x78
        size: 0x4
      easydrive_string_id:
        pos: 0x80
        size: 0x4
      number_of_checkpoints:
        pos: 0xD4
        type: u1
      cops_in_traffic:
        pos: 0xE0
        type: u1
      weapon_availability:
        pos: 0xEA
        type: u1
      cpu_count:
        pos: 0xED
        type: u1
      lap_count:
        pos: 0xEE
        type: u1
      float_maybe:
        pos: 0xF0
        type: u4
        repeat: expr
        repeat-expr: 0
      
      event_type_name:
        type:
          switch-on: event_type_hash
          cases:
            0x90230B00: "display_type('Sprint or Circuit')"
            0x51282100: "display_type('Drift')"
            0xD0B82100: "display_type('Smash n Grab')"
            0xB1940E00: "display_type('Speedrun')"
            0x29F40500: "display_type('Ambush')"
            0x01F40500: "display_type('Free Drive')"
            0x1ECF1700: "display_type('Intro')"
            _: "display_type('unknown')"
            
  multiplayer_race_type:
    seq:
    - {id: race_header, size: 0xC}

  multiplayer_challenge_type:
    seq:
    - {id: race_header, size: 0xC}

  genesys__gen__challenge_action__action_base__feedback_data:
    seq: 
      - {id: base_object, type: genesys_object}
      - {id: unique_id_0xc, type: u4}
      - {id: unique_id_0x10, type: u4}
      - {id: unique_id_0x14, type: u4}
      - {id: unique_id_0x18, type: u4}
      - {id: unique_id_0x1c, type: u4}
      - {id: enum_13_37_11_00, type: u2}
      - {id: bool_0x22, type: u1}
      - {id: padding, size: 0x1}

  genesys__gen__challenge_action__accumulation_helper_data:
    seq: 
      - {id: base_object, type: genesys_object}
      - {id: unique_id_0xc, type: u4}
      - {id: uint32_0x10, type: u4}
      - {id: enum_0f_39_11_00, type: u2}
      - {id: bool_0x16, type: u1}
      - {id: padding, size: 1}

  type_finder_for_genesys__gen__challenge_action__action_base:
    seq:
      - {id: obj, type: genesys_object}
    instances:
      action_type:
        pos: _parent._parent.offset
        type:
          switch-on: obj.mu_type_version
          cases:
            # E3_70_B2_CC
            0xE3_70_B2_CC: genesys__gen__challenge_action__accumulate_distance
            # 2B_A8_0E_31
            0x2B_A8_0E_31: genesys__gen__challenge_action__accumulate_near_misses
            # D7_89_93_D1
            0xD7_89_93_D1: genesys__gen__challenge_action__accumulate_takedowns
            # 47_DE_09_5B
            0x47_DE_09_5B: genesys__gen__challenge_action__accumulate_time
            # 0A_5F_28_EF
            0x0A_5F_28_EF: genesys__gen__challenge_action__car_state
            # 79_8B_78_5D
            0x79_8B_78_5D: genesys__gen__challenge_action__coop_accumulate_distance
            # 63_66_35_21
            0x63_66_35_21: genesys__gen__challenge_action__do_jump
            # B3_B4_2A_12
            0xB3_B4_2A_12: genesys__gen__challenge_action__get_to_location
            # C0_99_71_A8
            0xC0_99_71_A8: genesys__gen__challenge_action__hit_trigger
            # 3F_12_39_21
            0x3F_12_39_21: genesys__gen__challenge_action__jump_over_players
            # C8_AC_8F_6A
            0xC8_AC_8F_6A: genesys__gen__challenge_action__jump_stats
            # E3_E6_76_A8
            0xE3_E6_76_A8: genesys__gen__challenge_action__speed_camera_action
            # D7_8C_A2_95
            0xD7_8C_A2_95: genesys__gen__challenge_action__speed_run
            _: genesys__gen__challenge_action__action_base


  genesys__gen__challenge_action__action_base:
    seq: 
      - {id: base_object, type: genesys_object}
      - {id: feedback_data, type: genesys__gen__challenge_action__action_base__feedback_data}
      - {id: unique_id_0x30, type: u4}
      - {id: unique_id_0x34, type: u4}
      - {id: game_changer_id_0x38, type: u4}
      # - {id: unique_id_0x38, type: u4}
      - {id: accumulation_data_ptr_0x3c, type: u4}
      - {id: enum_2d_39_11_00, type: u2}
      - {id: scoring_method, type: u2, doc: enum_28_37_11_00}
      - {id: can_fail, type: u2, enum: e_online_challenge_fail, doc: enum_e6_39_11_00}
      - {id: who, type: u2, enum: e_online_challenge_involvement, doc: enum_24_37_11_00, }
    instances:
      accumulation_data:
        pos: accumulation_data_ptr_0x3c
        if: accumulation_data_ptr_0x3c != 0
        type: genesys__gen__challenge_action__accumulation_helper_data

  genesys__gen__challenge__challenge_part:
    seq:
      - {id: base_object, type: genesys_object}
      - {id: unique_id_0xc, type: u4}
      - {id: game_changer_id_0x10, type: u4}
      # - {id: unique_id_0x10, type: u4}
      - {id: instruction_0x14, type: u4}
      # - {id: unique_id_0x14, type: u4}
      - {id: unique_id_0x18, type: u4}
      - {id: short_instruction_0x1c, type: u4}
      # - {id: unique_id_0x1c, type: u4}
      - {id: action_base_ptr_ptr_table_0x20, type: u4}
      - {id: enum_53_37_11_00, type: u2, enum: e_parent_event_type}
      - {id: enum_58_39_11_00, type: u2, doc: "'always 1'"}
      - {id: uint16_0x28, type: u2, doc: "'90, 450, or 600'"}
      - { id: bool_0x2a, type: u1, doc: "'is speedtest?'"}
      - { id: array_count_for_0x20, type: u1}
    instances:
      action_base_ptr_table:
        pos: action_base_ptr_ptr_table_0x20
        type: ptr('type_finder_for_genesys__gen__challenge_action__action_base')
          # switch-on: action_base_ptr_ptr_table_0x20
          # cases: 
          #   E3_70_B2_CC: ptr('genesys__gen__challenge_action__accumulate_distance')
          #   2B_A8_0E_31: ptr('genesys__gen__challenge_action__accumulate_near_misses')
          #   D7_89_93_D1: ptr('genesys__gen__challenge_action__accumulate_takedowns')
          #   47_DE_09_5B: ptr('genesys__gen__challenge_action__accumulate_time')
          #   0A_5F_28_EF: ptr('genesys__gen__challenge_action__car_state')
          #   79_8B_78_5D: ptr('genesys__gen__challenge_action__coop_accumulate_distance')
          #   63_66_35_21: ptr('genesys__gen__challenge_action__do_jump')
          #   B3_B4_2A_12: ptr('genesys__gen__challenge_action__get_to_location')
          #   C0_99_71_A8: ptr('genesys__gen__challenge_action__hit_trigger')
          #   3F_12_39_21: ptr('genesys__gen__challenge_action__jump_over_players')
          #   C8_AC_8F_6A: ptr('genesys__gen__challenge_action__jump_stats')
          #   E3_E6_76_A8: ptr('genesys__gen__challenge_action__speed_camera_action')
          #   D7_8C_A2_95: ptr('genesys__gen__challenge_action__speed_run')
          #   _: ptr('genesys__gen__challenge_action__action_base')
        if: action_base_ptr_ptr_table_0x20 != 0
        repeat: expr
        repeat-expr: array_count_for_0x20

  genesys__gen__challenge__location:
    seq:
      - {id: base_object, type: genesys_object}
      - {id: unique_id_0xc, type: u4}
      - {id: display_trigger_ptr_array_0x10, type: u4}
      # - {id: display_trigger_ptr_array_0x10, type: u4}
      - {id: game_changer_id_0x14, type: u4}
      # - {id: unique_id_0x14, type: u4}
      - {id: trigger_ptr_array_0x18, type: u4}
      - {id: array_count_for_0x10, type: u2}
      - {id: array_count_for_0x18, type: u2}
    instances:
      display_trigger_arr_0x10:
        if: display_trigger_ptr_array_0x10 != 0
        pos: display_trigger_ptr_array_0x10
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x10
      trigger_arr_0x18:
        if: trigger_ptr_array_0x18 != 0
        pos: trigger_ptr_array_0x18
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x18
    
  genesys__gen__chevron:
    seq:
      - {id: base_object, type: genesys_object}
      - {id: game_changer_id_0xc, type: u4}
      # - {id: unique_id_0xc, type: u4}
      - {id: road_section_0x10, type: u4}
      # - {id: unique_id_0x10, type: u4}
      - {id: should_block_start_0x14, type: u1}
      # - {id: bool_0x14, type: u1}
      - {id: padding, size: 0x3}

  genesys__gen__custom_chevron:
    seq:
      - {id: base_object, type: genesys_object}
      - {id: game_changer_id_0xc, type: u4}
      # - {id: unique_id_0xc, type: u4}
      - {id: float_array_ptr_0x10, type: u4}
      - {id: float_array_ptr_0x14, type: u4}
      - {id: float_array_ptr_0x18, type: u4}
      - {id: array_count_for_0x10, type: u2}
      - {id: array_count_for_0x14, type: u2}
      - {id: array_count_for_0x18, type: u2}
      - {id: invert_normal_0x22, type: u1}
      # - {id: bool_0x22, type: u1}
      - {id: padding, size: 0x1}
    instances:
      float_array_0x10:
        type: f4
        pos: float_array_ptr_0x10
        if: float_array_ptr_0x10 != 0
        repeat: expr
        repeat-expr: array_count_for_0x10
      float_array_0x14:
        type: f4
        pos: float_array_ptr_0x14
        if: float_array_ptr_0x14 != 0
        repeat: expr
        repeat-expr: array_count_for_0x14
      float_array_0x18:
        type: f4
        pos: float_array_ptr_0x18
        if: float_array_ptr_0x18 != 0
        repeat: expr
        repeat-expr: array_count_for_0x18

  genesys__gen__gameplay__condition:
    seq:
      - {id: base_object, type: genesys_object}
      - {id: strings_ptr_array_0xc, type: u4}
      # - {id: string_base_ptr_array_0xc, type: u4}
      - {id: game_changer_id_0x10, type: u4}
      # - {id: unique_id_0x10, type: u4}
      - {id: reference_ptr_array_0x14, type: u4}
      # - {id: unique_id_ptr_array_0x14, type: u4}
      - {id: values_ptr_array_0x18, type: u4}
      # - {id: uint32_ptr_array_0x18, type: u4}
      - {id: test_type_val, type: u2, doc: enum_55_31_0f_00}
      - {id: type_val, type: u2, doc: enum_68_f1_0e_00}
      - {id: array_count_for_0x14, type: u2}
      - {id: array_count_for_0xc, type: u2}
      - {id: array_count_for_0x18, type: u2}
      - {id: padding, size: 0x2}
    instances:
      string_strings_array_0xc:
        if: strings_ptr_array_0xc != 0
        pos: strings_ptr_array_0xc
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0xc
      reference_array_0x14:
        if: reference_ptr_array_0x14 != 0
        pos: reference_ptr_array_0x14
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0xc
      values_array_0x18:
        if: values_ptr_array_0x18 != 0
        pos: values_ptr_array_0x18
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x18
      test_type:
        type:
          switch-on: test_type_val
          cases:
            # 0: "display_type('unknown')"
            1: "display_type('RacersFinished')"
            2: "display_type('Drift')"
            3: "display_type('RacersWrecked')"
            4: "display_type('CopsWrecked')"
            5: "display_type('Binding')"
            # 6: "display_type('unknown')"
            7: "display_type('PlayerWrecked')"
            8: "display_type('BeatTime')"
            9: "display_type('TopSpeed')"
            10: "display_type('StartingScore')"
            # 11: "display_type('unknown')"
            12: "display_type('AirTime')"
            _: "display_type('unknown')"
      kind:
        type:
          switch-on: type_val
          cases:
            0: "display_type('win')"
            1: "display_type('lose')"
            2: "display_type('special')"
            _: "display_type('unknown')"


  genesys__gen__offline_event__ai_player_information:
    seq:
      - {id: base_object, type: genesys_object}
      - {id: ai_player_type_0xc, type: u4}
      # - {id: unique_id_0xc, type: u4}
      - {id: back_up_colour_0x10, type: u4}
      # - {id: unique_id_0x10, type: u4}
      - {id: placement_0x14, type: u4}
      # - {id: unique_id_0x14, type: u4}
      - {id: primary_colour_0x18, type: u4}
      # - {id: unique_id_0x18, type: u4}

  genesys__gen__offline_event__alternate_routes:
    seq:
      - {id: base_object, type: genesys_object}
      - {id: checkpoint_0xc, type: u4}
      # - {id: unique_id_0xc, type: u4}
      - {id: route_marker_ptr_array_0x10, type: u4}
      # - {id: unique_id_ptr_array_0x10, type: u4}
      - {id: array_count_for_0x10, type: u2}
      - {id: padding, size: 0x2}
    instances:
      route_marker_array_0x10:
        type: u4
        if: route_marker_ptr_array_0x10 != 0
        pos: route_marker_ptr_array_0x10
        repeat: expr
        repeat-expr: array_count_for_0x10

  genesys__gen__offline_event__checkpoint_info:
    seq:
      - {id: base_object, type: genesys_object}
      - {id: sequence_0xc, type: u4}
      # - {id: unique_id_0xc, type: u4}
      - {id: type_val, type: u2, doc: enum_2b_77_0f_00}
      - {id: bool_0x12, type: u1}
      - {id: show_split_time_0x13, type: u1}
      # - {id: bool_0x13, type: u1}

  event_switcher:
    seq:
      - {id: base_object, type: genesys_object}
    instances:
      offline_event:
        if: base_object.mu_type_version == 0x903BCC47
        type: test_offline_event(_parent._parent.offset)
        pos: _parent._parent.offset
      online_event:
        if: base_object.mu_type_version == 0x1773054A
        type: online_event(_parent._parent.offset)
        pos: _parent._parent.offset
      online_challenge:        
        if: base_object.mu_type_version == 0x7E701662
        type: online_challenge(_parent._parent.offset)
        pos: _parent._parent.offset
      vote_event:
        if: base_object.mu_type_version == 0xBAF7B2C9
        type: vote_event(_parent._parent.offset)
        pos: _parent._parent.offset

  event_base:
    seq: 
      - {id: base_object, type: genesys_object}
      - {id: autotest_checkpoints_0xc, type: u4}
      # - {id: unique_id_array_ptr_0xc, type: u4}
      - {id: cinematic_name_0x10, type: u4}
      # - {id: unique_id_0x10, type: u4}
      - {id: description_0x14, type: u4}
      # - {id: unique_id_0x14, type: u4}
      - {id: game_changer_id_0x18, type: u4be}
      # - {id: event_name_id_0x18, type: u4be}
      - {id: game_mode_0x1c, type: u4be}
      # - {id: event_type_id_0x1c, type: u4be}
      - {id: game_pack_0x20, type: u4}
      # - {id: unique_id_0x20, type: u4}
      - {id: unique_id_0x24, type: u4}
      - {id: cycle_time_of_day_0x28, type: f4}
      # - {id: float_0x28, type: f4}
      - {id: finish_time_of_day_0x2c, type: f4}
      # - {id: float_0x2c, type: f4}
      - {id: sun_direction_0x30, type: f4}
      # - {id: float_0x30, type: f4}
      - {id: time_of_day_0x34, type: f4}
      # - {id: float_0x34, type: f4}
      - {id: float_0x38, type: f4}
      - {id: chevron_list_0x3c, type: u4}
      # - {id: custom_chevron_ptr_array_ptr_0x3c, type: u4}
      - {id: road_surface_conditions, type: u2, doc: enum_8b_38_09_00}
      - {id: array_count_for_0xc, type: u2}
      - {id: is_alternative_weather_0x44, type: u1}
      # - {id: bool_0x44, type: u1}
      - {id: is_rain_active_0x45, type: u1}
      # - {id: bool_0x45, type: u1}
      - {id: is_thunder_active_0x46, type: u1}
      # - {id: bool_0x46, type: u1}
      - {id: override_sun_direction_0x47, type: u1}
      # - {id: bool_0x47, type: u1}
      - {id: bool_0x48, type: u1}
      - {id: array_count_for_0x3c, type: u1}
      - {id: uint8_0x4a, type: u1}
      - {id: padding, size: 0x1}
    instances:
      kind:
        type: 
          switch-on: game_mode_0x1c
          cases:
            # SINGLEPLAYER
            0x90230B00: "display_type('Sprint or Circuit')"
            0x51282100: "display_type('Drift')"
            0xD0B82100: "display_type('Smash n Grab')"
            0xB1940E00: "display_type('Speedrun')"
            0x29F40500: "display_type('Ambush')"
            0x01F40500: "display_type('Free Drive')"
            0x1ECF1700: "display_type('Intro')"
            0x1E330400: "display_type('Cut/Unfinished')"
            # MULTIPLAYER
            0x818F0F00: "display_type('mp_RACE')"
            0x08040F00: "display_type('mp_TEAM_RACE')"
            0x1D940600: "display_type('mp_FREEDRIVE')"
            # ONLINE CHALLENGE
            0xAE381100: "display_type('mp_CHALLENGE')"
            0xD1361100: "display_type('mp_SPEEDTEST')"
            _: "display_type('unknown')"
      event_name:
        type: 
          switch-on: game_changer_id_0x18
          cases:
            0xBBC60800: "display_type('Rolling Stock')"
            0x90AF1100: "display_type('Industrial Revolution')"
            0xF59F0A00: "display_type('Stock Market Crash')"
            0x67160D00: "display_type('Turf War')"
            0xC3D30D00: "display_type('Off the Grid')"
            0x00AA0F00: "display_type('Import Duty')"
            0x5FE61000: "display_type('Mud Bath')"
            0x6C4B1300: "display_type('Jumping Jacks')"
            0x53DE1500: "display_type('Collateral Damage')"
            0x80491300: "display_type('To the Bridge')"
            0xA2D30D00: "display_type('Harbor Run')"
            0xC3010F00: "display_type('Crashdown')"
            0xDC020F00: "display_type('Park and Country')"
            0x8A030F00: "display_type('Park and Ride')"
            0xB9030F00: "display_type('Cannonball Run')"
            0xB4A80F00: "display_type('Pumping Iron')"
            0x45A90F00: "display_type('Straight to the Point')"
            0x65A90F00: "display_type('Arch Enemies')"
            0x1FB40F00: "display_type('Power Play')"
            0xE4E61000: "display_type('Chain Reaction')"
            0x23E71000: "display_type('Trail Blazer')"
            0xC2E71000: "display_type('Sports Sprint')"
            0x08041600: "display_type('Sprint Eastward')"
            0xF2211D00: "display_type('Keys to the City')"
            0xA6762100: "display_type('Aerial Agression')"
            0xC6131100: "display_type('Burning Rubber')"
            0xC7F81500: "display_type('Running the Gauntlet')"
            0x5E0D0700: "display_type('Continetal Drift')"
            0xB8140D00: "display_type('Crash Landing')"
            0x75160D00: "display_type('Emmerson Beltway')"
            0x7F020F00: "display_type('Turbulence')"
            0xECA80F00: "display_type('Power Struggle')"
            0x9FA90F00: "display_type('Red Shift')"
            0xD4A90F00: "display_type('Cold Burn')"
            0xB9B30F00: "display_type('Cruise Control')"
            0x9B131100: "display_type('Stopping Power')"
            0x23151100: "display_type('Crush Hour')"
            0xD2762100: "display_type('Round Trip')"
            0xA8A31100: "display_type('Turbine')"
            0x83A41100: "display_type('Gravity')"
            0xD31B1200: "display_type('Downtown Run')"
            0x861C1200: "display_type('Downgraded')"
            0x9F1C1200: "display_type('Needle Point')"
            0xE0DD1500: "display_type('The Getaway')"
            0xEDDD1500: "display_type('Industrial Way')"
            0xDBF81500: "display_type('Fast Track')"
            0x73D51600: "display_type('Get to the Chopper')"
            0x44672200: "display_type('High Stakes')"
            0x78672200: "display_type('Bring the Noise')"
            0x35702100: "display_type('Sudden Impact')"
            0x6D702100: "display_type('Bullet Train')"
            0xC1702100: "display_type('Deadline')"
            0xEA702100: "display_type('Live and let Drive')"
            0x23712100: "display_type('Pulp Friction')"
            0xE8712100: "display_type('Braking Traction')"
            0x9D6A2100: "display_type('Get to Callahan')"
            0xA86E2100: "display_type('License to Thrill')"
            0x436F2100: "display_type('Bootlegging')"
            0x11E41F00: "display_type('Downfall')"
            0x20E41F00: "display_type('Terminal Velocity')"
            0x2FE41F00: "display_type('Steel City')"
            0x3EE41F00: "display_type('Drive Hard')"
            0x7BE41F00: "display_type('Burning Bridges')"
            0x8C2E2000: "display_type('The Enforcer')"
            0x42D22200: "display_type('Inner City Pressure')"
            0x6CE41F00: "display_type('Green Zone')"
            0x93702100: "display_type('Mayhem')"
            0x8BE41F00: "display_type('Around the World')"
            0x74672200: "display_type('Fuelled')"
            0xAD672200: "display_type('Speed Demon')"
            0xFF712100: "display_type('Running Wild')"
            0xA8E41F00: "display_type('The Descent')"
            0x682F2000: "display_type('Live for Speed')"
            0x8B2F2000: "display_type('Full Overdrive')"
            0x8C2F2000: "display_type('Full Throttle')"
            0x4EE41F00: "display_type('Critical Path')"
            0x3ED51600: "display_type('Most Wanted 1')"
            0x6D2E1700: "display_type('Most Wanted 2')"
            0xCBAA1700: "display_type('Most Wanted 3')"
            0x35BF1700: "display_type('Most Wanted 4')"
            0x83E11500: "display_type('Most Wanted 5')"
            0x5E5C1500: "display_type('Most Wanted 6')"
            0xA7D41600: "display_type('Most Wanted 7')"
            0xEFE01500: "display_type('Most Wanted 8')"
            0x8E791600: "display_type('Most Wanted 9')"
            0x15791600: "display_type('Most Wanted 10')"
            0x686F2100: "display_type('Most Wanted GTR')"
            0xA56F2100: "display_type('Most Wanted GT500')"
            0x8DA12100: "display_type('Most Wanted Spyder')"
            0x99E41F00: "display_type('Most Wanted Venom')"
            0x12E11500: "display_type('Liberty Park')"
            0x25771600: "display_type('Double Parked')"
            0x07D51600: "display_type('The Fugitive')"
            0xE02D1700: "display_type('Storehouse Stakeout')"
            0x9FAA1700: "display_type('Bloody Nose')"
            0x6DAB1700: "display_type('The Hunted')"
            0x47682200: "display_type('Jailbird')"
            0x2B092100: "display_type('Sidewinder')"
            0x3C092100: "display_type('Easy Drifter')"
            0x45772100: "display_type('Power Slide')"
            0x40D02100: "display_type('Drift City')"
            0xC1D22100: "display_type('Air Brake')"
            0xFE772100: "display_type('Duty Free')"
            0x09652200: "display_type('Air Raid')"
            0x14652200: "display_type('Green Belt')"
            0xA1662200: "display_type('Ship to Shore')"
            0xFA662200: "display_type('Destruction Site')"
            0x2FF60500: "display_type('Freedrive')"
            0x1FF40500: "display_type('Freedrive')"
            0x26AB0500: "display_type('Freedrive')"
            0x22CF1700: "display_type('Welcome To Fairhaven')"
            0xC7B21700: "display_type('Bridges')"
            0xC8B21700: "display_type('PowerPlant')"
            0x91742200: "display_type('CLEAR FOR TAKEOFF')"
            0x67742200: "display_type('NOW BOARDING')"
            0x837B2100: "display_type('FLIGHTPLAN')"
            0x6D7B2100: "display_type('LAST CALL')"
            0xC47C2100: "display_type('KEYS TO THE CITY')"
            0xC09F2000: "display_type('CRUSH HOUR')"
            0x0AA02000: "display_type('TO THE BRIDGE')"
            0xDB9F2000: "display_type('MUD BATH')"
            0x20A02000: "display_type('CHAIN REACTION')"
            0xF59F2000: "display_type('TURBULENCE')"
            0xD29F2000: "display_type('IMPORT DUTY')"
            0x31A02000: "display_type('CRASHDOWN')"
            0x35A02000: "display_type('GET TO THE CHOPPER')"
            0x7F4C1800: "display_type('OUT OF THE LOOP')"
            0xF99F2000: "display_type('INDUSTRIAL WAY')"
            0x1BA02000: "display_type('ARCH ENEMIES')"
            0xC4330400: "display_type('POWER TRIP')"
            0xDC851100: "display_type('BLACKOUT')"
            0x0C861100: "display_type('PIER POWER')"
            0x0A861100: "display_type('CRITICAL PATH')"
            0xD8851100: "display_type('GOING UNDER')"
            0x0B861100: "display_type('DOWNFALL')"
            0x0D861100: "display_type('WHITE HEAT')"
            0x7B861100: "display_type('PIER PRESSURE')"
            0xC3861100: "display_type('DRIVE HARD')"
            0x4F551600: "display_type('HARBOR RUN')"
            0x28541600: "display_type('OFF THE GRID')"
            0x60541600: "display_type('EMMERSON BELTWAY')"
            0x6A541600: "display_type('GRAVITY')"
            0xB8541600: "display_type('STRAIGHT TO THE POINT')"
            0x27561600: "display_type('STEEL CITY')"
            0x2D561600: "display_type('KINGPIN')"
            0x35561600: "display_type('RED SHIFT')"
            0x3D561600: "display_type('ROLLING STOCK')"
            0x42561600: "display_type('WAVE LENGTH')"
            0x47561600: "display_type('INDUSTRIAL REVOLUTION')"
            0x60561600: "display_type('FAST TRACK')"
            0x6E561600: "display_type('SPORTS SPRINT')"
            0xAA561600: "display_type('CONTINENTAL DRIFT')"
            0xB0561600: "display_type('GREEN ZONE')"
            0xB6561600: "display_type('RUNNING THE GAUNTLET')"
            0xC14A1800: "display_type('DOWNGRADED')"
            0x274C1800: "display_type('PARK AND RIDE')"
            0x3D4C1800: "display_type('TERMINAL VELOCITY')"
            0x6D4C1800: "display_type('BURNING RUBBER')"
            # 0x7F4C1800: "display_type('OUT OF THE LOOP')"
            0x9E4C1800: "display_type('MEAN STREETS')"
            0x4D4D1800: "display_type('POWER PLAY')"
            0x5E4D1800: "display_type('TRAIL BLAZER')"
            0x6F4D1800: "display_type('DOWNTOWN RUN')"
            0x804D1800: "display_type('SECOND SIGHT')"
            0xA44D1800: "display_type('NARROW MARGIN')"
            0xC44D1800: "display_type('THE ENFORCER')"
            0x074E1800: "display_type('SUDDEN IMPACT')"
            0x0FE71800: "display_type('POWER LOOP')"
            0x1CE71800: "display_type('RAT RACE')"
            0x29E71800: "display_type('STOCK MARKET CRASH')"
            0x3CE71800: "display_type('STOPPING POWER')"
            0x4DE71800: "display_type('BORROWED TIME')"
            0x64E71800: "display_type('ZERO TOLERANCE')"
            0x89E71800: "display_type('ABSOLUTE POWER')"
            0x98E71800: "display_type('THE GETAWAY')"
            0xB1E71800: "display_type('CRASH LANDING')"
            0xBEE71800: "display_type('NEEDLE POINT')"
            0xD4E71800: "display_type('PUMPING IRON')"
            0xE2E71800: "display_type('CANNONBALL RUN')"
            0x0BE81800: "display_type('BURNING BRIDGES')"
            0xDEE81800: "display_type('COLD BURN')"
            0x21E91B00: "display_type('AROUND THE WORLD')"
            0xA79F2000: "display_type('COLLATERAL DAMAGE')"
            0xD69F2000: "display_type('JUMPING JACKS')"
            0x1CA02000: "display_type('ARCH ENEMIES')"
            0x32A02000: "display_type('CRASHDOWN')"
            0x36A02000: "display_type('GET TO THE CHOPPER')"
            0xD39F2000: "display_type('IMPORT DUTY')"
            0x5F9F2000: "display_type('TURBULENCE')"
            0x0BA02000: "display_type('TO THE BRIDGE')"
            0xC19F2000: "display_type('CRUSH HOUR')"
            0xC57C2100: "display_type('KEYS TO THE CITY')"
            0x6E7B2100: "display_type('LAST CALL')"
            0x847B2100: "display_type('FLIGHTPLAN')"
            0x68742200: "display_type('NOW BOARDING')"
            0x92742200: "display_type('CLEAR FOR TAKEOFF')"
            0xFA9F2000: "display_type('INDUSTRIAL WAY')"
            0xA89F2000: "display_type('COLLATERAL DAMAGE')"
            0xDC9F2000: "display_type('MUD BATH')"
            0x21A02000: "display_type('CHAIN REACTION')"
            0x5A2F1000: "display_type('BLACKOUT')"
            0x03851100: "display_type('CRITICAL PATH')"
            0xF1841100: "display_type('PIER POWER')"
            0xBF861100: "display_type('PIER PRESSURE')"
            0xC1861100: "display_type('DRIVE HARD')"
            0x08D51500: "display_type('HARBOR RUN')"
            0x28D51500: "display_type('STRAIGHT TO THE POINT')"
            0x23541600: "display_type('DOWNFALL')"
            0x24541600: "display_type('WHITE HEAT')"
            0x25541600: "display_type('POWER TRIP')"
            0x27541600: "display_type('GOING UNDER')"
            0x2F541600: "display_type('OFF THE GRID')"
            0x66541600: "display_type('EMMERSON BELTWAY')"
            0x71541600: "display_type('GRAVITY')"
            0x2C561600: "display_type('STEEL CITY')"
            0x2F561600: "display_type('KINGS STOP SPRINT')"
            0x3C561600: "display_type('RED SHIFT')"
            0x3E561600: "display_type('ROLLING STOCK')"
            0x41561600: "display_type('WAVE LENGTH')"
            0x48561600: "display_type('INDUSTRIAL REVOLUTION')"
            0x61561600: "display_type('FAST TRACK')"
            0x6F561600: "display_type('SPORTS SPRINT')"
            0xA9561600: "display_type('CONTINENTAL DRIFT')"
            0xAF561600: "display_type('GREEN ZONE')"
            0xB5561600: "display_type('RUNNING THE GAUNTLET')"
            0xC04A1800: "display_type('DOWNGRADED')"
            0x284C1800: "display_type('PARK AND RIDE')"
            0x3E4C1800: "display_type('TERMINAL VELOCITY')"
            0x6E4C1800: "display_type('BURNING RUBBER')"
            0x804C1800: "display_type('OUT OF THE LOOP')"
            0x9F4C1800: "display_type('MEAN STREETS')"
            0x4E4D1800: "display_type('POWER PLAY')"
            0x5F4D1800: "display_type('TRAIL BLAZER')"
            0x704D1800: "display_type('DOWNTOWN RUN')"
            0x814D1800: "display_type('SECOND SIGHT')"
            0xA54D1800: "display_type('NARROW MARGIN')"
            0xC54D1800: "display_type('THE ENFORCER')"
            0x084E1800: "display_type('SUDDEN IMPACT')"
            0x0EE71800: "display_type('POWER LOOP')"
            0x1BE71800: "display_type('RAT RACE')"
            0x28E71800: "display_type('STOCK MARKET CRASH')"
            0x3BE71800: "display_type('STOPPING POWER')"
            0x4CE71800: "display_type('BORROWED TIME')"
            0x65E71800: "display_type('ZERO TOLERANCE')"
            0x8AE71800: "display_type('ABSOLUTE POWER')"
            0x99E71800: "display_type('THE GETAWAY')"
            0xB2E71800: "display_type('CRASH LANDING')"
            0xBFE71800: "display_type('NEEDLE POINT')"
            0xD5E71800: "display_type('PUMPING IRON')"
            0xE3E71800: "display_type('CANNONBALL RUN')"
            0x0CE81800: "display_type('BURNING BRIDGES')"
            0xDFE81800: "display_type('COLD BURN')"
            0x22E91B00: "display_type('AROUND THE WORLD')"
            0xD79F2000: "display_type('JUMPING JACKS')"
            0xAFFE1000: "display_type('BRIDGES FREEDRIVE')"
            0xF7F91700: "display_type('BRIDGES FREEDRIVE')"
            0xF8F91700: "display_type('BRIDGES FREEDRIVE')"
            0x7BB01700: "display_type('MISSED BY THE BELL')"
            0x3BB01700: "display_type('TOWER DRIFT')"
            0x04B01700: "display_type('AIR PIPE')"
            0x3FEA1800: "display_type('FLIGHT DISTANCE')"
            0x16B01700: "display_type('WING WALKER')"
            0x4CB01700: "display_type('HANGAR ON')"
            0xC1411900: "display_type('AIR SPEED')"
            0x714B1800: "display_type('DRIFT THE LOOP')"
            0x174D1800: "display_type('AIR TRAFFIC CONTROL')"
            0xCB4A1800: "display_type('CONTAINER PARK')"
            0xAEAF1700: "display_type('AN AGGRESSIVE MANOR')"
            0x77411900: "display_type('ONE WAY TO PARADISE')"
            0xE7AF1700: "display_type('BELL TOWER TAKEDOWN')"
            0xC4EA1800: "display_type('DONT KILL THE CAR')"
            0x94AF1700: "display_type('LAKE LAUNCH')"
            0x85B01700: "display_type('KNOCKING OFF')"
            0xBBAF1700: "display_type('TO THE MANOR AIRBORNE')"
            0xC1AF1700: "display_type('MANSION MISSLES')"
            0xA8EA1800: "display_type('GREAT SCOTT!')"
            0x2DEA1800: "display_type('DOWNHILL STEPS')"
            0xD6411900: "display_type('MONUMENTAL DRIFT')"
            0xC8B11700: "display_type('PLANE JUMPER')"
            0xC9551600: "display_type('HIGH POWER')"
            0xBA551600: "display_type('STEEL JUMPER')"
            0xF4541600: "display_type('INTO THE STORM')"
            0x0A551600: "display_type('ALL OVER THE SHOP')"
            0x2BE81800: "display_type('BELL HOPPING')"
            0x11D51500: "display_type('BLOCK JUMPER')"
            0x47EA1800: "display_type('DRIFT UP A STORM')"
            0xD2AE1700: "display_type('STUNT WORKSHOP')"
            0xB3541600: "display_type('SHOCKING PARKING')"
            0x92B01700: "display_type('WORKSHOP DONUTS')"
            0x7F561600: "display_type('UNDER THE BRIDGE')"
            0x2ED51500: "display_type('DRIFT LIGHT')"
            0xAAD51500: "display_type('ABANDON SHIP!')"
            0xA9411900: "display_type('STANDARD SHIPPING')"
            0x20AF1700: "display_type('CLIFFTOP DRIFTERS')"
            0x914B1800: "display_type('TAKEDOWN TO THE BRIDGE')"
            0xA1531600: "display_type('OVER THE HIGHWAY')"
            0x6D4E1800: "display_type('POWER PARKING')"
            0x5CD51500: "display_type('TIGHT SHIPPING')"
            0xA3551600: "display_type('WORKSHOP TAKEDOWN')"
            0xD4E81800: "display_type('PLATFORM PARKING')"
            0x79541600: "display_type('MISSING BARGES')"
            0x3D541600: "display_type('COAL YARDAGE')"
            0x45411900: "display_type('COOL DRIFTING')"
            0x4D541600: "display_type('COOL TAKEDOWNS')"
            0x0CD51500: "display_type('POWER MISS')"
            0x31E81800: "display_type('DUNE JUMPER')"
            0x80E81800: "display_type('OVER THE EDGE')"
            0xBDB11700: "display_type('ROOFTOP PARKING')"
            0x91B11700: "display_type('MALL PARK')"
            0x91AE1700: "display_type('INTERLOCKING DRIFTS')"
            0x1EEA1800: "display_type('KRUGER SPEED')"
            0xBF4B1800: "display_type('PARADISE MISSED')"
            0xAAB01700: "display_type('HIGH HEELS')"
            0xC3541600: "display_type('PIER PARKING')"
            0x90D51500: "display_type('WITHIN THE LAW')"
            0xD6D51500: "display_type('STEP ON THE GRASS')"
            0xB2551600: "display_type('LIGHTHOUSE LEAPS')"
            0xDC521600: "display_type('PYRAMID PLATFORM')"
            0x084D1800: "display_type('WING AND A PRAYER')"
            0x97551600: "display_type('MARKET CRASH')"
            0xC9D41500: "display_type('DRIFT HARD')"
            0x244D1800: "display_type('RAIL JUMPER')"
            0x9A411900: "display_type('DRIVEN LOOPY')"
            0xD84B1800: "display_type('PIPE UP')"
            0xFFAE1700: "display_type('STUNT CRANE')"
            0x9C531600: "display_type('CONSTRUCTION TAKEDOWN')"
            0x8B531600: "display_type('DRIFT SITE')"
            0xE4D41500: "display_type('MISSING LOCKS')"
            0x98601400: "display_type('ARCH ANGELS')"
            0x87551600: "display_type('BRIDGE WRECKED')"
            0x90E81800: "display_type('CRANE PARKING')"
            0x9DD51500: "display_type('2ND FLOOR SQUEEZE')"
            0xA3621400: "display_type('BALANCE BEAM')"
            0x91531600: "display_type('KRUGER AIR')"
            0x66E81800: "display_type('STUNT SITE')"
            0x12AF1700: "display_type('PIPE MISSES')"
            0x277C2100: "display_type('EXCESS BAGGAGE')"
            0xA67A2100: "display_type('GLOBAL JUMPERS')"
            0x51742200: "display_type('TERMINAL LEAP')"
            0xC07A2100: "display_type('GROUND EFFECTS')"
            0x157B2100: "display_type('BUMPY LANDINGS')"
            0x907A2100: "display_type('NOW BOARDING')"
            0x5A742200: "display_type('TERMINAL PARKING')"
            0xD57A2100: "display_type('GLOBAL DRIFTERS')"
            0x434D1800: "display_type('PETERSON ST SPEED TRAP')"
            0x644B1800: "display_type('PETERSON LOOP DRIFT')"
            0x2CB01700: "display_type('AIRFIELD DRIFT')"
            0xE74C1800: "display_type('CARGO PLANE JUMP')"
            0x8BAF1700: "display_type('HUGHES PARK LAKE JUMP')"
            0xFCE81800: "display_type('PARK ARCHES SPEED RUN')"
            0x76AF1700: "display_type('MANSION JUMP')"
            0xA1AF1700: "display_type('BELL TOWER DRIFT')"
            0x63AF1700: "display_type('BELL TOWER JUMP')"
            0x69B11700: "display_type('PARK MANSION SPEED RUN')"
            0xC7B01700: "display_type('RAIL TRACK SPEED RUN')"
            0x95541600: "display_type('BLOCK RD SPEED TRAP')"
            0x334D1800: "display_type('CALLAHAN CONTAINERS JUMP')"
            0x3B4D1800: "display_type('CALLAHAN CONVEYOR JUMP')"
            0x83B11700: "display_type('STORM DRAIN SPEED RUN')"
            0xFF541600: "display_type('K&N WORKSHOP DRIFT')"
            0x8A541600: "display_type('SHOCKLEY RD SPEED TRAP')"
            0x40AF1700: "display_type('GANT ST SPEED TRAP')"
            0x81541600: "display_type('CALLAHAN OVERPASS JUMP')"
            0x7A4B1800: "display_type('HEFLIN BRIDGE JUMP')"
            0x294E1800: "display_type('STORM DRAIN DRIFT')"
            0xD3D51500: "display_type('LIGHTHOUSE DRIFT')"
            0x5CB11700: "display_type('I-92W DIRT TRACK SPEED RUN')"
            0x39E81800: "display_type('HARRIS RD JUMP')"
            0x204C1800: "display_type('BURKE ST SPEED TRAP')"
            0x76B11700: "display_type('POWER PLANT SPEED RUN')"
            0x4FD51500: "display_type('POWER PLANT DRIFT')"
            0x94B11700: "display_type('BARGES SPEED RUN')"
            0x454E1800: "display_type('TURBINE HALL DRIFT')"
            0xF34A1800: "display_type('COOLING TOWER DRIFT')"
            0xE44A1800: "display_type('COAL YARD JUMP')"
            0xEB4A1800: "display_type('HARRIS RD JUMP')"
            0xA2B11700: "display_type('COAL YARD SPEED RUN')"
            0xBD541600: "display_type('POWER PLANT ALLEY JUMP')"
            0x52EA1800: "display_type('CONNORS BRIDGE RD SPEED TRAP')"
            0x854B1800: "display_type('BELTWAY W JUMP')"
            0x5B4B1800: "display_type('INTERLOCKING LOOPS DRIFT')"
            0x27551600: "display_type('MARKET JUMP')"
            0x05B11700: "display_type('RAIL TRACK SPEED RUN')"
            0xA4621400: "display_type('LOWREY ST SPEED TRAP')"
            0x27B11700: "display_type('CONNORS BRIDGE RD SPEED RUN')"
            0x3E4E1800: "display_type('MARKET DRIFT')"
            0x1D551600: "display_type('ROSEWOOD PL JUMP')"
            0xFD4A1800: "display_type('FOLEY ST PARKING JUMP')"
            0x2B531600: "display_type('PYRAMID JUMP')"
            0x4F4E1800: "display_type('BELTWAY S SPEED TRAP')"
            0x194B1800: "display_type('LOWREY ST SPEED TRAP')"
            0x61E91800: "display_type('PIER DRIFT')"
            0xCC4C1800: "display_type('BELTWAY W HOOPS JUMP')"
            0xC54C1800: "display_type('GARBER ST JUMP')"
            0x0B4B1800: "display_type('MURPHY ST SPEED TRAP')"
            0x044B1800: "display_type('SOUTH STATION JUMP')"
            0x4B371100: "display_type('KRUGER AVE SPEED TRAP')"
            0xD9D41500: "display_type('MCCLANE CONVEYOR JUMP')"
            0x4EB11700: "display_type('MCCLANE BRIDGE SPEED RUN')"
            0x31551600: "display_type('LORENZO AVE BRIDGE JUMP')"
            0xA2621400: "display_type('ARCHES JUMP')"
            0x3C551600: "display_type('FOUR BRIDGES TOWER JUMP')"
            0x58371100: "display_type('MCCALE I-92 JUMP')"
            0xC0D51500: "display_type('CONSTRUCTION SITE DRIFT')"
            0xF4AE1700: "display_type('I-92E CRANE JUMP')"
            0xFC4B1800: "display_type('I-92E PIPE JUMP')"
            0x4F7C2100: "display_type('CAMERON DRIVE JUMPS')"
            0x65A02000: "display_type('CARGO SHIP JUMP')"
            0x4FA02000: "display_type('DAM JUMP')"
            0x40A02000: "display_type('INTERLOCKING LOOPS JUMP')"
            0xEC7A2100: "display_type('RUNWAY SPEED TRAP')"
            0x117C2100: "display_type('GLOBE RAMPS DRIFT')"
            0x7D7A2100: "display_type('RUNWAY PLANE JUMP')"
            0x537A2100: "display_type('TERMINAL PLANE JUMP')"
            0x617C2100: "display_type('CARGO PLANE JUMP')"
            0x1F7C2100: "display_type('AIRPORT SITE DRIFT')"
            0x2B7C2100: "display_type('AIRPORT BEACH JUMP')"
            _: "display_type('unknown')"
      unique_id_array:
        type: u4
        if: autotest_checkpoints_0xc != 0
        pos: autotest_checkpoints_0xc
        repeat: expr
        repeat-expr: array_count_for_0xc
      custom_chevron_ptr_array:
        type: ptr('genesys__gen__custom_chevron')
        if: chevron_list_0x3c != 0
        pos: chevron_list_0x3c
        repeat: expr
        repeat-expr: array_count_for_0x3c
      road_surface_condition:
        type:
          switch-on: road_surface_conditions
          cases:
            0x0: "display_type('Dry')"
            0x1: "display_type('Wet')"
            0x2: "display_type('StandingWater')"
  online_event:
    params:
      - id: evt_offset
        type: u4
    seq:
      - {id: base_object, type: event_base}
      - {id: float_arr_0x4c, type: f4}
      - {id: float_arr_entry_maybe_0x50, type: f4}
      - {id: arena_0x54, type: u4}
      # - {id: unique_id_0x54, type: u4}
      - {id: unique_id_0x58, type: u4}
      - {id: unique_id_0x5c, type: u4}
      - {id: unique_id_arr_0x60, type: u4}
      - {id: route_0x64, type: u4}
      # - {id: unique_id_0x64, type: u4}
      - {id: array_count_for_0x4c, type: u2}
      - {id: array_count_for_0x60, type: u2}
      - {id: requires_airport_0x6c, type: u1}
      # - {id: bool_0x6c, type: u1}
      - {id: padding, size: 0x3}
    instances:
      float_array_0x50:
        pos: evt_offset + 0x4c
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x4c
      unique_id_array:
        pos: unique_id_arr_0x60
        if: unique_id_arr_0x60 != 0
        type: u4
        repeat: expr
        repeat-expr: array_count_for_0x60

  online_challenge:
    params:
      - id: evt_offset
        type: u4
    seq:
      - {id: base_object, type: online_event(evt_offset)}
      - {id: intro_0x70, type: u4}
      # - {id: unique_id_0x70, type: u4}
      - {id: unique_id_0x74, type: u4}
      # - {id: deallocated_nodule_0x74, type: u4}
      - {id: challenge_part_ptr_ptr_table_0x78, type: u4}
      # - {id: challenge_part_ptr_ptr_table_0x78, type: u4}
      - {id: elimination_type, type: u2, enum: e_online_elimination_type, doc: enum_ff_f8_17_00}
      - {id: type_val, type: u2, enum: e_online_challenge_type, doc: enum_c3_38_11_00}
      # - {id: enum_c3_38_11_00, type: u2}
      - {id: array_count_for_0x78, type: u1}
      - {id: padding, size: 0x3}
    instances:
      challenge_part_ptr_table:
        type: ptr('genesys__gen__challenge__challenge_part')
        if: challenge_part_ptr_ptr_table_0x78 != 0
        pos: challenge_part_ptr_ptr_table_0x78
        repeat: expr
        repeat-expr: array_count_for_0x78

  genesys__gen__challenge_action__accumulate_distance:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
  
  genesys__gen__challenge_action__accumulate_near_misses:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
      - {id: min_speed_0x48, type: f4}
      # - {id: float_0x48, type: f4}
      - {id: challenge_location_ptr_0x4c, type: ptr('genesys__gen__challenge__location')}
      - {id: in_air_0x50, type: u1}
      # - {id: bool_0x50, type: u1}
      - {id: padding, size: 0x3}

  genesys__gen__challenge_action__accumulate_takedowns:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}

  genesys__gen__challenge_action__accumulate_time:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}

  genesys__gen__challenge_action__car_state:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
      - {id: car_category_0x48, type: u4}
      # - {id: unique_id_0x48, type: u4}
      - {id: float_0x4c, type: f4}
      - {id: float_0x50, type: f4}
      - {id: max_speed_0x54, type: u2}
      # - {id: uint16_0x54, type: u2}
      - {id: min_speed_0x56, type: u2}
      # - {id: uint16_0x56, type: u2}
      - {id: bool_0x58, type: u1}
      - {id: bool_0x59, type: u1}
      - {id: bool_0x5a, type: u1}
      - {id: donutting_0x5b, type: u1}
      # - {id: bool_0x5b, type: u1}
      - {id: drifting_0x5c, type: u1}
      # - {id: bool_0x5c, type: u1}
      - {id: in_air_0x5d, type: u1}
      # - {id: bool_0x5d, type: u1}
      - {id: nitrous_0x5e, type: u1}
      # - {id: bool_0x5e, type: u1}
      - {id: bool_0x5f, type: u1}
      - {id: reversing_0x60, type: u1}
      # - {id: bool_0x60, type: u1}
      - {id: slipstreaming_0x61, type: u1}
      # - {id: bool_0x61, type: u1}
      - {id: padding, size: 0x2}

  genesys__gen__challenge_action__coop_accumulate_distance:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}

  genesys__gen__challenge_action__do_jump:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
      - {id: challenge_location_ptr_0x48, type: ptr('genesys__gen__challenge__location')}
      - {id: accumulate_0x4c, type: u1}
      # - {id: bool_0x4c, type: u1}
      - {id: padding, size: 0x3}

  genesys__gen__challenge_action__get_to_location:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
      - {id: challenge_location_ptr_0x48, type: ptr('genesys__gen__challenge__location')}
      - {id: route_location_0x4c, type: u1}
      # - {id: bool_0x4c, type: u1}
      - {id: bool_0x4d, type: u1}
      - {id: padding, size: 0x2}
  
  genesys__gen__challenge_action__hit_trigger:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
      - {id: trigger_0x48, type: u4}
      # - {id: unique_id_0x48, type: u4}

  genesys__gen__challenge_action__jump_over_players:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
      - {id: challenge_location_ptr_0x48, type: ptr('genesys__gen__challenge__location')}
      - {id: bool_0x4c, type: u1}
      - {id: padding, size: 0x3}

  genesys__gen__challenge_action__jump_stats:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
      - {id: challenge_location_ptr_0x48, type: ptr('genesys__gen__challenge__location')}

  genesys__gen__challenge_action__speed_camera_action:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
      - {id: unique_id_0x48, type: u4}
      - {id: on_hit_sequence_0x4c, type: u4}
      # - {id: unique_id_0x4c, type: u4}
      - {id: challenge_location_ptr_0x50, type: ptr('genesys__gen__challenge__location')}

  genesys__gen__challenge_action__speed_run:
    seq: 
      - {id: base_object, type: genesys__gen__challenge_action__action_base}
      - {id: route_ptr_array_0x48, type: ptr('genesys__gen__challenge__location'), repeat: expr, repeat-expr: 2}
      # - {id: challenge_location_ptr_array_0x48, type: ptr('genesys__gen__challenge__location'), repeat: expr, repeat-expr: 2}
      - {id: array_count_for_0x48, type: u1, doc: "always 2"}
      - {id: padding, size: 0x3}

  vote_event:
    params:
    - id: evt_offset
      type: u4
    seq:
      - {id: base_object, type: online_event(evt_offset)}
      - {id: unique_id_0x70, type: u4}
      - {id: unique_id_0x74, type: u4}
      - {id: unique_id_0x78, type: u4}
      - {id: unique_id_0x7c, type: u4}


  test_offline_event:
    params:
      - id: evt_offset
        type: u4
    seq:
      - {id: test, type: offline_event }

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
            '"genesys__gen__challenge_action__accumulate_distance"': genesys__gen__challenge_action__accumulate_distance
            '"genesys__gen__challenge_action__accumulate_near_misses"': genesys__gen__challenge_action__accumulate_near_misses
            '"genesys__gen__challenge_action__accumulate_takedowns"': genesys__gen__challenge_action__accumulate_takedowns
            '"genesys__gen__challenge_action__accumulate_time"': genesys__gen__challenge_action__accumulate_time
            '"genesys__gen__challenge_action__car_state"': genesys__gen__challenge_action__car_state
            '"genesys__gen__challenge_action__coop_accumulate_distance"': genesys__gen__challenge_action__coop_accumulate_distance
            '"genesys__gen__challenge_action__do_jump"': genesys__gen__challenge_action__do_jump
            '"genesys__gen__challenge_action__get_to_location"': genesys__gen__challenge_action__get_to_location
            '"genesys__gen__challenge_action__hit_trigger"': genesys__gen__challenge_action__hit_trigger
            '"genesys__gen__challenge_action__jump_over_players"': genesys__gen__challenge_action__jump_over_players
            '"genesys__gen__challenge_action__jump_stats"': genesys__gen__challenge_action__jump_stats
            '"genesys__gen__challenge_action__speed_camera_action"': genesys__gen__challenge_action__speed_camera_action
            '"genesys__gen__challenge_action__speed_run"': genesys__gen__challenge_action__speed_run

            '"genesys__gen__challenge__location"': genesys__gen__challenge__location
            '"genesys__gen__challenge_action__action_base"': genesys__gen__challenge_action__action_base
            '"genesys__gen__challenge__challenge_part"': genesys__gen__challenge__challenge_part
            '"genesys__gen__chevron"': genesys__gen__chevron
            '"genesys__gen__custom_chevron"': genesys__gen__custom_chevron
            '"genesys__gen__gameplay__condition"': genesys__gen__gameplay__condition
            '"event_switcher"': event_switcher
            '"event_base"': event_base

            '"type_finder_for_genesys__gen__challenge_action__action_base"': type_finder_for_genesys__gen__challenge_action__action_base
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