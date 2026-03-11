from construct import *
from construct.lib import *
import enum

class any_genesys_obj__e_de_30_00_00(enum.IntEnum):
	invalid = 0
	small = 1
	medium = 2
	large = 3

class any_genesys_obj__e_b2_35_07_00(enum.IntEnum):
	default = 0
	reverb = 1
	ev2 = 2
	ev3 = 3
	buffering__percents = 4

class any_genesys_obj__e_e8_bc_16_00(enum.IntEnum):
	stock = 0
	track = 1
	ev2 = 2

class any_genesys_obj__e_53_37_11_00(enum.IntEnum):
	move_on = 0
	fail = 1

class any_genesys_obj__e_27_30_00_00(enum.IntEnum):
	none = 0
	engine = 1
	skid = 2
	player = 3
	competitor = 4
	traffic = 5
	ui = 6

class any_genesys_obj__e_29_f7_03_00(enum.IntEnum):
	gain = 0
	panning__angle = 1
	panning__divergence = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5
	pitch = 6
	focus = 7
	emitter = 8
	ev9 = 9
	instance_limit = 10
	ev11 = 11

class any_genesys_obj__e_69_32_11_00(enum.IntEnum):
	chasing = 0
	blocking = 1
	bruising = 2
	rhino = 3
	ev4 = 4
	idle = 5
	default = 6

class any_genesys_obj__e_a8_60_04_00(enum.IntEnum):
	none = 0
	ev1 = 1
	drifting = 2
	tbone = 3
	shunt = 4
	slam = 5
	vertical = 6
	into_traffic = 7
	into_water = 8
	ev9 = 9
	using_nitrous = 10
	top_speed = 11
	ev12 = 12
	ev13 = 13
	ev14 = 14
	after_spotting = 15
	ev16 = 16
	all_events = 17
	ev18 = 18
	license_plates = 19
	over_speed = 20
	billboards = 21
	speed_traps = 22
	in_air = 23
	over_player = 24
	traffic_vehicle = 25
	player_vehicle = 26
	ev27 = 27
	paint_pack = 28

class any_genesys_obj__e_2d_39_11_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2
	simultaneous = 3
	ev4 = 4

class any_genesys_obj__e_a1_2e_00_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5

class any_genesys_obj__e_8e_4e_49_12(enum.IntEnum):
	rank = 0
	game_mode = 1
	weapon = 2
	ev3 = 3
	car = 4
	weapon_upgrade = 5
	ev6 = 6
	license_plate = 7
	driving_test_list = 8
	feature = 9
	paint_pack = 10
	count = 11
	unknown = 12

class any_genesys_obj__e_77_cc_06_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5
	ev6 = 6
	ev7 = 7

class any_genesys_obj__e_15_f7_03_00(enum.IntEnum):
	nickname_violation = 0
	ev1 = 1
	drag = 2
	engine__load = 3
	ev4 = 4
	throttle = 5
	engine__on = 6
	ev7 = 7
	ev8 = 8
	chassis__heat = 9
	alarm__on = 10
	ev11 = 11
	ev12 = 12

class any_genesys_obj__e_ff_f8_17_00(enum.IntEnum):
	none = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3
	random = 4

class any_genesys_obj__e_76_f5_0e_00(enum.IntEnum):
	ev0 = 0
	imagen_rewarding = 1
	live_feed = 2
	photo_gallery = 3

class any_genesys_obj__e_13_37_11_00(enum.IntEnum):
	none = 0
	raw = 1
	tick = 2
	speed = 3
	time = 4
	position = 5
	distance = 6

class any_genesys_obj__e_0f_34_07_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	clip = 2
	off = 3

class any_genesys_obj__e_d9_65_15_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5
	ev6 = 6
	ev7 = 7
	ev8 = 8

class any_genesys_obj__e_f6_31_00_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	grey = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5
	ev6 = 6
	blue = 7
	ev8 = 8

class any_genesys_obj__e_86_f4_0e_00(enum.IntEnum):
	multi_player = 0
	single_player = 1
	social = 2
	ev3 = 3
	ev4 = 4
	disallowed__currently = 5
	ev6 = 6

class any_genesys_obj__e_8a_fa_06_00(enum.IntEnum):
	none = 0

class any_genesys_obj__e_28_37_11_00(enum.IntEnum):
	none = 0
	ev1 = 1
	on__finish = 2

class any_genesys_obj__e_e6_39_11_00(enum.IntEnum):
	allow_fail = 0
	ev1 = 1

class any_genesys_obj__e_5b_f6_03_00(enum.IntEnum):
	multiply = 0
	offset = 1
	absolute = 2

class any_genesys_obj__e_a3_37_09_00(enum.IntEnum):
	default = 0
	helicopter = 1

class any_genesys_obj__e_d5_f6_03_00(enum.IntEnum):
	gain = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3
	peak__frequency = 4
	peak__gain = 5
	peak__q = 6
	ev7 = 7
	low__shelf__gain = 8
	ev9 = 9
	ev10 = 10
	ev11 = 11
	ev12 = 12
	ev13 = 13
	ev14 = 14
	ev15 = 15
	ev16 = 16
	ev17 = 17
	compressor__ratio = 18
	compressor__threshold = 19
	vocally_impose = 20
	compressor__release = 21
	ev22 = 22
	distortion__amount = 23

class any_genesys_obj__e_3d_30_00_00(enum.IntEnum):
	none = 0
	power = 1
	multiply = 2

class any_genesys_obj__e_83_f6_03_00(enum.IntEnum):
	time = 0
	binding = 1
	none = 2

class any_genesys_obj__e_e3_31_0f_00(enum.IntEnum):
	standard = 0
	pro = 1

class any_genesys_obj__e_09_5e_0f_00(enum.IntEnum):
	scalar = 0
	addition = 1
	override = 2

class any_genesys_obj__e_b9_b2_17_00(enum.IntEnum):
	ev0 = 0
	online_only = 1
	ev2 = 2

class any_genesys_obj__e_c4_f3_03_00(enum.IntEnum):
	loaded = 0
	streamed = 1
	ev2 = 2
	decay_exceptionally = 3
	ev4 = 4
	speech__stream = 5
	ev6 = 6
	ev7 = 7

class any_genesys_obj__e_2b_77_0f_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	sector_start = 2
	lap_start = 3
	ev4 = 4

class any_genesys_obj__e_3e_5f_04_00(enum.IntEnum):
	seconds = 0
	chain = 1
	lives = 2
	events = 3
	speed_lists = 4
	all__time = 5

class any_genesys_obj__e_d7_31_0f_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5
	ev6 = 6
	ev7 = 7
	ev8 = 8
	ev9 = 9
	ev10 = 10
	ev11 = 11
	ev12 = 12
	ev13 = 13

class any_genesys_obj__e_f0_31_00_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3
	traffic = 4

class any_genesys_obj__e_53_bc_16_00(enum.IntEnum):
	none = 0
	individual = 1
	social = 2
	team = 3

class any_genesys_obj__e_32_67_0d_00(enum.IntEnum):
	ev0 = 0
	shunt = 1
	ev2 = 2
	skid = 3

class any_genesys_obj__e_bc_35_07_00(enum.IntEnum):
	gain = 0
	frequency = 1
	q = 2
	time = 3
	feedback = 4
	ev5 = 5
	ev6 = 6
	ev7 = 7
	ev8 = 8

class any_genesys_obj__e_e4_33_07_00(enum.IntEnum):
	mono = 0
	stereo = 1
	ev2 = 2

class any_genesys_obj__e_22_30_00_00(enum.IntEnum):
	none = 0
	low = 1
	normal = 2
	extreme = 3

class any_genesys_obj__e_d7_e3_10_00(enum.IntEnum):
	none = 0
	finish_first = 1
	ev2 = 2
	not_overtaken = 3
	ev4 = 4
	not_spotted = 5
	not_wrecked = 6
	ev7 = 7
	ev8 = 8
	distinct = 9
	on_rims = 10
	last_second = 11
	ev12 = 12
	ev13 = 13
	most_wanted = 14
	finish_last = 15
	no_score = 16

class any_genesys_obj__e_55_31_0f_00(enum.IntEnum):
	ev0 = 0
	racers_finished = 1
	drift = 2
	racers_wrecked = 3
	cops_wrecked = 4
	binding = 5
	ev6 = 6
	player_wrecked = 7
	beat_time = 8
	top_speed = 9
	starting_score = 10
	ev11 = 11
	air_time = 12

class any_genesys_obj__e_35_30_00_00(enum.IntEnum):
	ev0 = 0
	high_cost = 1

class any_genesys_obj__e_a7_d8_19_00(enum.IntEnum):
	equals = 0
	ev1 = 1

class any_genesys_obj__e_1d_30_00_00(enum.IntEnum):
	near = 0
	mid = 1
	far = 2
	ev3 = 3

class any_genesys_obj__e_38_30_00_00(enum.IntEnum):
	invalid = 0
	match = 1
	linear = 2
	exponential = 3

class any_genesys_obj__e_13_94_0e_00(enum.IntEnum):
	no_retry = 0
	ev1 = 1
	ev2 = 2

class any_genesys_obj__e_42_f3_0e_00(enum.IntEnum):
	ev0 = 0
	timeout = 1

class any_genesys_obj__e_18_32_00_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2

class any_genesys_obj__e_c8_2f_00_00(enum.IntEnum):
	ev0 = 0
	dlc1 = 1
	dlc2 = 2
	dlc3 = 3
	dlc4 = 4

class any_genesys_obj__e_2b_55_19_00(enum.IntEnum):
	acceleration = 0
	top_speed = 1
	ev2 = 2
	ev3 = 3
	toughness = 4
	ev5 = 5
	nitrous = 6

class any_genesys_obj__e_58_39_11_00(enum.IntEnum):
	current_action = 0
	last_action = 1

class any_genesys_obj__e_f7_f2_0e_00(enum.IntEnum):
	none = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3

class any_genesys_obj__e_93_37_09_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2

class any_genesys_obj__e_04_32_00_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	reversing = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5
	ev6 = 6
	ev7 = 7
	ev8 = 8
	ev9 = 9
	ev10 = 10
	ev11 = 11
	ev12 = 12
	slip_streaming = 13
	ev14 = 14
	ev15 = 15
	ev16 = 16
	ev17 = 17
	idle = 18
	ev19 = 19
	ev20 = 20

class any_genesys_obj__e_71_fa_06_00(enum.IntEnum):
	none = 0

class any_genesys_obj__e_b3_27_00_00_0_2(enum.IntEnum):
	none = 0
	camera_aligned = 1

class any_genesys_obj__e_d9_31_00_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	rear = 2
	left = 3
	ev4 = 4
	ev5 = 5
	ev6 = 6
	ev7 = 7
	ev8 = 8

class any_genesys_obj__e_68_f1_0e_00(enum.IntEnum):
	win = 0
	lose = 1
	special = 2

class any_genesys_obj__e_c3_38_11_00(enum.IntEnum):
	speed_test = 0
	team = 1
	social = 2

class any_genesys_obj__e_ee_33_07_00(enum.IntEnum):
	source = 0
	ev1 = 1
	perceives_several = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5
	ev6 = 6

class any_genesys_obj__e_4a_63_04_00(enum.IntEnum):
	deducted__shield = 0
	ev1 = 1

class any_genesys_obj__e_f3_0d_06_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3

class any_genesys_obj__e_d0_39_0b_00(enum.IntEnum):
	constantly = 0
	periodically = 1
	on__entry = 2
	once = 3

class any_genesys_obj__e_93_f3_05_00(enum.IntEnum):
	takedown = 0
	assist = 1
	suicide = 2
	teamkill = 3
	revenge = 4
	first_blood = 5
	afterlife = 6
	double_takedown = 7
	triple_takedown = 8
	takedown_frenzy = 9
	reverse = 10
	ev11 = 11
	ev12 = 12
	comeback = 13
	takendown = 14
	speeding = 15
	weapon_used = 16
	cop_hit = 17
	ev18 = 18
	ev19 = 19
	ev20 = 20
	enter_cooldown = 21
	prop_damaged = 22
	prop_destroyed = 23
	traffic_hit = 24
	traffic_immobilised = 25
	ev26 = 26
	hit_jump = 27
	jump_takedown = 28
	hit_blackspot = 29
	blackspot_takedown = 30
	hit_stack = 31
	stack_takedown = 32
	ev33 = 33
	keeping_dry = 34
	ev35 = 35
	high_speed = 36
	on_rims = 37
	on_rims2 = 38
	on_rims3 = 39
	on_rims4 = 40
	boost_punch = 41
	slam_offline = 42
	shunt_offline = 43
	tbone_offline = 44
	slam_online = 45
	shunt_online = 46
	ev47 = 47
	ev48 = 48
	fight_bonus = 49
	weapon_hit = 50
	head_on_offline = 51
	ev52 = 52
	avenger = 53
	rescuer = 54
	payload_takedown = 55
	ev56 = 56
	payload_spilled = 57
	cop_hit_payload = 58
	into_city = 59
	blinded = 60
	smoked = 61

class any_genesys_obj__e_83_1d_10_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5
	ev6 = 6

class any_genesys_obj__e_85_8d_10_00(enum.IntEnum):
	once = 0
	random = 1
	periodic = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5

class any_genesys_obj__e_d9_f0_0e_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3
	pursuits__evaded = 4
	time__played = 5
	distance__driven = 6
	bounty__earned = 7
	times__busted = 8
	ev9 = 9
	ev5lw_l = 10
	ev11 = 11
	times__wrecked = 12
	ev13 = 13
	ev14 = 14
	ev15 = 15
	ev16 = 16
	ev17 = 17
	ev18 = 18
	jumps__found = 19
	ev20 = 20
	ev21 = 21
	billboards__hit = 22
	ev23 = 23
	ev24 = 24
	crash__escapes = 25
	ev26 = 26
	ev27 = 27
	ev28 = 28
	ev29 = 29
	ev30 = 30
	ev31 = 31
	ev32 = 32
	ev33 = 33
	ev34 = 34
	ev35 = 35
	ev36 = 36
	ev37 = 37
	ev38 = 38
	ev39 = 39
	ev40 = 40
	ev41 = 41
	ev42 = 42
	ev43 = 43
	ev44 = 44
	ev45 = 45
	ev46 = 46
	ev47 = 47

class any_genesys_obj__e_f4_5f_0f_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	road = 2
	ev3 = 3
	track = 4

class any_genesys_obj__e_00_0f_16_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	ev2 = 2

class any_genesys_obj__e_95_6a_96_0c(enum.IntEnum):
	ev0 = 0
	online = 1

class any_genesys_obj__e_24_37_11_00(enum.IntEnum):
	individual = 0
	team = 1
	everyone = 2

class any_genesys_obj__e_f0_2f_00_00(enum.IntEnum):
	none = 0
	ev1 = 1
	ev2 = 2
	ev3 = 3

class any_genesys_obj__e_e1_bc_16_00(enum.IntEnum):
	off = 0
	standard = 1
	pro = 2

class any_genesys_obj__e_2a_be_07_00(enum.IntEnum):
	high_quality = 0
	low_quality = 1

class any_genesys_obj__e_8f_7d_0f_00(enum.IntEnum):
	brightness = 0
	contrast = 1
	motion__blur = 2

class any_genesys_obj__e_a4_5d_0f_00(enum.IntEnum):
	ev0 = 0
	ev1 = 1
	stock = 2
	track = 3
	ev4 = 4
	ev5 = 5

class any_genesys_obj__e_02_5e_0f_00(enum.IntEnum):
	engine_torque = 0
	ev1 = 1
	front_drag = 2
	ev3 = 3
	ev4 = 4
	ev5 = 5
	ev6 = 6
	ev7 = 7
	toughness_vs_race_car = 8
	ev9 = 9
	toughness_vs_traffic = 10
	ev11 = 11
	toughness_vs_world = 12
	toughness_vs_dynamic = 13
	ev14 = 14
	ev15 = 15
	ev16 = 16
	ev17 = 17
	mass = 18
	strength = 19
	ev20 = 20
	ev21 = 21
	fu_r7 = 22
	ev23 = 23
	ev24 = 24
	ev25 = 25
	ev26 = 26
	roll_angle_limit = 27
	ev28 = 28
	ev29 = 29
	ev30 = 30
	gravity_multiplier = 31
	ev32 = 32
	transmission_whine = 33
	ev34 = 34
	ev35 = 35
	ev36 = 36
	ev37 = 37
	ev38 = 38
	ev39 = 39
	ev40 = 40
	ev41 = 41
	ev42 = 42
	ev43 = 43
	ev44 = 44
	ev45 = 45
	pitying_gun = 46
	ev47 = 47
	ev48 = 48
	ev49 = 49
	ev50 = 50
	ev51 = 51
	ev52 = 52
	ev53 = 53
	ev54 = 54

class any_genesys_obj__e_55_21_0a_00(enum.IntEnum):
	none = 0
	channel_animation = 1
	ev2 = 2

class any_genesys_obj__e_43_5f_04_00(enum.IntEnum):
	drive = 0
	takedown = 1
	fall = 2
	jump = 3
	unlock = 4
	near_miss = 5
	complete_event = 6
	wreck = 7
	repair = 8
	ev9 = 9
	ev10 = 10
	perfect_nitrous = 11
	spot_opponent = 12
	spot_bonus = 13
	ev14 = 14
	eliminate_opponent = 15
	last_standing = 16
	ticket = 17
	fuel_portrait = 18
	be = 19
	be_eliminated = 20
	false_start = 21
	score_first = 22
	collect = 23
	ev24 = 24
	jack_car = 25
	air_time = 26
	accumulate_time = 27
	ev28 = 28

class any_genesys_obj__e_72_cc_06_00(enum.IntEnum):
	play__once = 0
	ev1 = 1
	ev2 = 2

class any_genesys_obj__e_0f_39_11_00(enum.IntEnum):
	longest = 0
	shortest = 1
	most = 2
	least = 3
	closest = 4
	ev5 = 5

class any_genesys_obj__e_e2_b2_17_00(enum.IntEnum):
	ev0 = 0

class any_genesys_obj__e_f7_34_07_00(enum.IntEnum):
	rate = 0
	ev1 = 1
	ev2 = 2

class any_genesys_obj__e_70_fa_06_00(enum.IntEnum):
	none = 0

class any_genesys_obj__e_8b_38_09_00(enum.IntEnum):
	dry = 0
	wet = 1
	standing_water = 2

class any_genesys_obj__e_43_f6_05_00(enum.IntEnum):
	default = 0
	waiting = 1
	patrolling = 2
	escaping = 3
	chasing = 4
	waiting__lights = 5
	idle__lights = 6
	rhino = 7
	racing = 8
	free__roam = 9
	idle = 10
	ev11 = 11
	chasing__interceptor = 12
	cop__racing = 13
	ev14 = 14
	ev15 = 15

class any_genesys_obj__e_0e_f7_05_00(enum.IntEnum):
	time = 0
	score = 1

class any_genesys_obj__e_2a_6b_07_00(enum.IntEnum):
	stop = 0
	restart = 1

any_genesys_obj__genesys__gen__tyre__long__slip__factors = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 484081367),
)

any_genesys_obj__genesys__gen__physics__damage_bar_profile = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__physics__damage_bar_profile__impact_location_damage_scale_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__physics__damage_bar_profile__impact_location_damage_scale),
	'crashing_rules_0x34' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x3c' / Int32ul,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'ejected_rubbish_0x48' / Float32l,
	'float32_t_0x4c' / Float32l,
	'float32_t_0x50' / Float32l,
	'float32_t_0x54' / Float32l,
	'float32_t_0x58' / Float32l,
	'float32_t_0x5c' / Float32l,
	'float32_t_0x60' / Float32l,
	'float32_t_0x64' / Float32l,
	'float32_t_0x68' / Float32l,
	'float32_t_0x6c' / Float32l,
	'ptr_arr_segments_0x70' / Int32ul,
	'array_count_for_0x70' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_segments_0x70' / Pointer(this.ptr_arr_segments_0x70, Array(this.array_count_for_0x70, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__damage_bar_profile__segment))),
	'size' / Computed(lambda this: 120),
	'mu_version_hash' / Computed(lambda this: 3650009805),
)

any_genesys_obj__genesys__gen__corona = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'unk_enum_0x10' / Int8ub,
	'game_changer_id_0xa0' / Int32ul,
	'float32_t_0xa4' / Float32l,
	'max_visible_distance_0xa8' / Float32l,
	'visibility_test_depth_bias_0xac' / Float32l,
	'ptr_arr_beams_0xb0' / Int32ul,
	'ptr_arr_flares_0xb4' / Int32ul,
	'ptr_arr_env_map_glows_0xb8' / Int32ul,
	'ptr_arr_glows_0xbc' / Int32ul,
	'ptr_arr_planar_reflection_glows_0xc0' / Int32ul,
	'ptr_arr_rear_view_mirror_glows_0xc4' / Int32ul,
	'flags_0xc8' / Int16ul,
	'array_count_for_0xb0' / Int16ul,
	'array_count_for_0xb8' / Int16ul,
	'array_count_for_0xb4' / Int16ul,
	'array_count_for_0xbc' / Int16ul,
	'array_count_for_0xc0' / Int16ul,
	'array_count_for_0xc4' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_planar_reflection_glows_0xc0' / Pointer(this.ptr_arr_planar_reflection_glows_0xc0, Array(this.array_count_for_0xc0, LazyBound(lambda: any_genesys_obj__genesys__gen__corona__glow))),
	'inst_beams_0xb0' / Pointer(this.ptr_arr_beams_0xb0, Array(this.array_count_for_0xb0, LazyBound(lambda: any_genesys_obj__genesys__gen__corona__beam))),
	'size' / Computed(lambda this: 216),
	'inst_flares_0xb4' / Pointer(this.ptr_arr_flares_0xb4, Array(this.array_count_for_0xb4, LazyBound(lambda: any_genesys_obj__genesys__gen__corona__flare))),
	'inst_glows_0xbc' / Pointer(this.ptr_arr_glows_0xbc, Array(this.array_count_for_0xbc, LazyBound(lambda: any_genesys_obj__genesys__gen__corona__glow))),
	'inst_env_map_glows_0xb8' / Pointer(this.ptr_arr_env_map_glows_0xb8, Array(this.array_count_for_0xb8, LazyBound(lambda: any_genesys_obj__genesys__gen__corona__glow))),
	'inst_rear_view_mirror_glows_0xc4' / Pointer(this.ptr_arr_rear_view_mirror_glows_0xc4, Array(this.array_count_for_0xc4, LazyBound(lambda: any_genesys_obj__genesys__gen__corona__glow))),
	'mu_version_hash' / Computed(lambda this: 1234658497),
)

any_genesys_obj__genesys__gen__nitrous_parameters = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'traffic_oncoming_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__traffic_oncoming),
	'balancing_0x34' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__balancing),
	'donutting_0x58' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__donutting),
	'drifting_0x7c' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__drifting),
	'hitting_another_competitor_0xa0' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__hitting_another_competitor),
	'punch_0xc4' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__punch_usage),
	'slip_streaming_0xe8' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__slipstreaming),
	'catching_air_0x10c' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__catching_air),
	'crash_escape_0x12c' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__crash_escape),
	'driving_at_high_speed_0x14c' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__high_speed),
	'driving_at_speed_0x16c' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__min_speed),
	'nitrous_0x18c' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__nitrous_usage),
	'taking_shortcut_0x1ac' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__taking_shortcut),
	'traffic_near_miss_0x1cc' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__traffic_near_miss),
	'traffic_near_miss_oncoming_0x1ec' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__traffic_near_miss),
	'fatal_hit_0x20c' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__fatal_hit),
	'jump_0x228' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__jump_usage),
	'shared_0x244' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__restrictions),
	'genesys__gen__nitrous_parameters__speedbreaker_usage_0x260' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__speedbreaker_usage),
	'game_changer_id_0x27c' / Int32ul,
	'size' / Computed(lambda this: 644),
	'mu_version_hash' / Computed(lambda this: 855876020),
)

any_genesys_obj__genesys__gen__nitrous_parameters__jump_usage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters_usage),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 935932605),
)

any_genesys_obj__genesys__gen__uilist_items = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_items_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_items_0x10' / Pointer(this.ptr_arr_items_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__uilist_items__item))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 2626560424),
)

any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'damage_value_0xc' / Float32l,
	'ptr_arr_speed_control_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_speed_control_0x10' / Pointer(this.ptr_arr_speed_control_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3736686144),
)

any_genesys_obj__genesys__gen__collision_info__payload_damage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_genesys__gen__collision_info_damage_profile_0xc' / Int32ul,
	'ptr_self_inflicted_0x10' / Int32ul,
	'inst_genesys__gen__collision_info_damage_profile_0xc' / Pointer(this.ptr_genesys__gen__collision_info_damage_profile_0xc, LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info_damage_profile)),
	'inst_self_inflicted_0x10' / Pointer(this.ptr_self_inflicted_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info_damage_profile)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 456234940),
)

any_genesys_obj__genesys__gen__light__cone = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__light__base),
	'float32_t_0x60' / Float32l,
	'size' / Computed(lambda this: 104),
	'mu_version_hash' / Computed(lambda this: 3989427985),
)

any_genesys_obj__rw_math_vpu__vector4 = Struct(
	'inline_arr_elements_0x0' / Array(4, Float32l),
	'size' / Computed(lambda this: 8),
	'mu_version_hash' / Computed(lambda this: 3257509935),
)

any_genesys_obj__genesys__gen__nitrous_parameters__min_speed = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'minimum_speed_0x14' / Float32l,
	'nitrous_reward_0x18' / Float32l,
	'is_enabled_0x1c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3789082911),
)

any_genesys_obj__genesys__gen__impact_damage_graphs__graph = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'maximum_closing_velocity_mph_0xc' / Float32l,
	'maximum_velocity_damage_0x10' / Float32l,
	'medium_closing_velocity_mph_0x14' / Float32l,
	'medium_velocity_damage_0x18' / Float32l,
	'minimum_closing_velocity_mph_0x1c' / Float32l,
	'minimum_velocity_damage_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 1703771469),
)

any_genesys_obj__genesys__gen__challenge__challenge_part = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__unique_id_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'instruction_0x14' / Int32ul,
	'cgs_core__unique_id_0x18' / Int32ul,
	'short_instruction_0x1c' / Int32ul,
	'ptr_arr_ptr_actions_0x20' / Int32ul,
	'unk_enum_0x24' / Int16ul,
	'unk_enum_0x26' / Int16ul,
	'uint16_t_0x28' / Int16ul,
	'bool8_t_0x2a' / Int8ub,
	'array_count_for_0x20' / Int8ub,
	'inst_actions_0x20' / Pointer(this.ptr_arr_ptr_actions_0x20, Array(this.array_count_for_0x20, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 3591252192),
)

any_genesys_obj__genesys__gen__online_route = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_arr_checkpoints_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'array_count_for_0xc' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_checkpoints_0xc' / Pointer(this.ptr_arr_checkpoints_0xc, Array(this.array_count_for_0xc, Int32ul)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 202861526),
)

any_genesys_obj__genesys__gen__nitrous_parameters__balancing = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'close_burn_rate_0xc' / Float32l,
	'close_multiplier_0x10' / Float32l,
	'far_burn_rate_0x14' / Float32l,
	'far_multiplier_0x18' / Float32l,
	'max_distance_0x1c' / Float32l,
	'slipstream_distance_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 4081022393),
)

any_genesys_obj__genesys__gen__band_pass_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'frequency_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3794314553),
)

any_genesys_obj__genesys__gen__challenge_action__accumulation_helper_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'target_0x10' / Int32ul,
	'operator_0x14' / Int16ul,
	'bool8_t_0x16' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 4093540154),
)

any_genesys_obj__genesys__gen__engine__mixer__channel__gain__modification = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'mixer__channel_0xc' / FixedSized(8, GreedyBytes),
	'gain_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2361784635),
)

any_genesys_obj__cgs_resource__handle = Struct(
)

any_genesys_obj__genesys__gen__collision_info__battling_effect__extra_roll_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'damage__for__full__extra__roll_0xc' / Float32l,
	'damage__for__no__extra__roll_0x10' / Float32l,
	'extra__limit__duration_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3691704753),
)

any_genesys_obj__genesys__gen__wheel_sizes = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2321043106),
)

any_genesys_obj__genesys__gen__challenge_action__get_to_location = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'route_location_0x4c' / Int8ub,
	'bool8_t_0x4d' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 80),
	'mu_version_hash' / Computed(lambda this: 3014928914),
)

any_genesys_obj__genesys__gen__hard_driving_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__hard_driving_behaviour__gas_effect_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__hard_driving_behaviour__gas_effect),
	'genesys__gen__hard_driving_behaviour__steering_effect_0x4c' / LazyBound(lambda: any_genesys_obj__genesys__gen__hard_driving_behaviour__steering_effect),
	'game_changer_id_0x60' / Int32ul,
	'size' / Computed(lambda this: 104),
	'mu_version_hash' / Computed(lambda this: 3500617746),
)

any_genesys_obj__genesys__gen__vehicle__gameplay = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__vehicle__gameplay__damage_stats_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__damage_stats),
	'genesys__gen__vehicle__gameplay__damage_stats_0x28' / LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__damage_stats),
	'id_0nkx_0x44' / LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__damage_stats),
	'genesys__gen__vehicle__gameplay__tyre_trails_0x60' / LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__tyre_trails),
	'cgs_resource__handle_0x74' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x7c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x84' / FixedSized(8, GreedyBytes),
	'cgs_core__unique_id_0x8c' / Int32ul,
	'game_changer_id_0x90' / Int32ul,
	'cgs_core__unique_id_0x94' / Int32ul,
	'cgs_core__unique_id_0x98' / Int32ul,
	'cgs_core__unique_id_0x9c' / Int32ul,
	'cgs_core__unique_id_0xa0' / Int32ul,
	'cgs_core__unique_id_0xa4' / Int32ul,
	'cgs_core__unique_id_0xa8' / Int32ul,
	'float32_t_0xac' / Float32l,
	'ptr_genesys__gen__pidcontroller_0xb0' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb4' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb8' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xbc' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc0' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc4' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc8' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xcc' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd0' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd4' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd8' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xdc' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe0' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe4' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe8' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xec' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf0' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf4' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf8' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xfc' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x100' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x104' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x108' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x10c' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x110' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x114' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x118' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x11c' / Int32ul,
	'ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x120' / Int32ul,
	'array_count_for_0xb4' / Int8ub,
	'array_count_for_0xb8' / Int8ub,
	'array_count_for_0xbc' / Int8ub,
	'array_count_for_0xc0' / Int8ub,
	'array_count_for_0xc4' / Int8ub,
	'array_count_for_0xc8' / Int8ub,
	'array_count_for_0xcc' / Int8ub,
	'array_count_for_0xd0' / Int8ub,
	'array_count_for_0xd4' / Int8ub,
	'array_count_for_0xd8' / Int8ub,
	'array_count_for_0xdc' / Int8ub,
	'array_count_for_0xe0' / Int8ub,
	'array_count_for_0xe4' / Int8ub,
	'array_count_for_0xe8' / Int8ub,
	'array_count_for_0xec' / Int8ub,
	'array_count_for_0xf0' / Int8ub,
	'array_count_for_0xf4' / Int8ub,
	'array_count_for_0xf8' / Int8ub,
	'array_count_for_0xfc' / Int8ub,
	'array_count_for_0x100' / Int8ub,
	'array_count_for_0x104' / Int8ub,
	'array_count_for_0x108' / Int8ub,
	'array_count_for_0x10c' / Int8ub,
	'array_count_for_0x110' / Int8ub,
	'array_count_for_0x114' / Int8ub,
	'array_count_for_0x118' / Int8ub,
	'array_count_for_0x11c' / Int8ub,
	'array_count_for_0x120' / Int8ub,
	'uint8_t_0x140' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xf8' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf8, Array(this.array_count_for_0xf8, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0x10c' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x10c, Array(this.array_count_for_0x10c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xf0' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf0, Array(this.array_count_for_0xf0, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xc4' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc4, Array(this.array_count_for_0xc4, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0x11c' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x11c, Array(this.array_count_for_0x11c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xf4' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf4, Array(this.array_count_for_0xf4, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xd4' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd4, Array(this.array_count_for_0xd4, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0x114' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x114, Array(this.array_count_for_0x114, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xcc' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xcc, Array(this.array_count_for_0xcc, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xdc' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xdc, Array(this.array_count_for_0xdc, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0x104' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x104, Array(this.array_count_for_0x104, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xc8' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc8, Array(this.array_count_for_0xc8, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'size' / Computed(lambda this: 324),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xb8' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb8, Array(this.array_count_for_0xb8, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0x108' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x108, Array(this.array_count_for_0x108, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__pidcontroller_0xb0' / Pointer(this.ptr_genesys__gen__pidcontroller_0xb0, LazyBound(lambda: any_genesys_obj__genesys__gen__pidcontroller)),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xd8' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd8, Array(this.array_count_for_0xd8, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0x118' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x118, Array(this.array_count_for_0x118, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0x110' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x110, Array(this.array_count_for_0x110, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xd0' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd0, Array(this.array_count_for_0xd0, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xec' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xec, Array(this.array_count_for_0xec, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xbc' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xbc, Array(this.array_count_for_0xbc, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0x120' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x120, Array(this.array_count_for_0x120, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xfc' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xfc, Array(this.array_count_for_0xfc, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xe4' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe4, Array(this.array_count_for_0xe4, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xc0' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc0, Array(this.array_count_for_0xc0, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0x100' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x100, Array(this.array_count_for_0x100, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xb4' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb4, Array(this.array_count_for_0xb4, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xe0' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe0, Array(this.array_count_for_0xe0, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
	'mu_version_hash' / Computed(lambda this: 520558439),
	'inst_genesys__gen__vehicle__gameplay__mod_effect_0xe8' / Pointer(this.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe8, Array(this.array_count_for_0xe8, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect))),
)

any_genesys_obj__genesys__gen__race_balancing_data__opponent_balancing_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ahead_distance_0x10' / Float32l,
	'behind_distance_0x14' / Float32l,
	'end_cutoff_ratio_0x18' / Float32l,
	'end_speed_value_ahead_0x1c' / Float32l,
	'end_speed_value_behind_0x20' / Float32l,
	'start_cutoff_ratio_0x24' / Float32l,
	'start_speed_value_ahead_0x28' / Float32l,
	'start_speed_value_behind_0x2c' / Float32l,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 1273350923),
)

any_genesys_obj__genesys__gen__camera_gameplay_gradient_adjustments__params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 397117973),
)

any_genesys_obj__genesys__gen__camera_gameplay_bonnet__wind_sound = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'cgs_core__unique_id_0x10' / Int32ul,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3274903722),
)

any_genesys_obj__genesys__gen__steering_behaviour__steering_angle_curve = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 3935354064),
)

any_genesys_obj__genesys__gen__high_pass_butterworth_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'order_0x18' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1110789791),
)

any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'convex_hull_0x50' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x58' / Int32ul,
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 1664340785),
)

any_genesys_obj__genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'damage_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1476111906),
)

any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'body_to_object_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'com_offset_0x50' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'inertia__scale_0x60' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'local_aabbcenter_0x70' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'local_aabbhalf_diagonal_0x80' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'ptr_arr_symmetrical_in_axis_0x90' / Int32ul,
	'game_changer_id_0x94' / Int32ul,
	'angular_drag_0x98' / Float32l,
	'bounciness_0x9c' / Float32l,
	'friction_0xa0' / Float32l,
	'linear_drag_0xa4' / Float32l,
	'mass_0xa8' / Float32l,
	'ptr_arr_box_volumes_0xac' / Int32ul,
	'ptr_arr_capsule_volumes_0xb0' / Int32ul,
	'ptr_bounding_convex_hull_0xb4' / Int32ul,
	'ptr_arr_convex_hull_volumes_0xb8' / Int32ul,
	'ptr_arr_cylinder_volumes_0xbc' / Int32ul,
	'ptr_arr_sphere_volumes_0xc0' / Int32ul,
	'array_count_for_0xac' / Int16ul,
	'array_count_for_0xb0' / Int16ul,
	'array_count_for_0xb8' / Int16ul,
	'array_count_for_0xbc' / Int16ul,
	'array_count_for_0xc0' / Int16ul,
	'array_count_for_0x90' / Int16ul,
	'is_wheel_0xd0' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_capsule_volumes_0xb0' / Pointer(this.ptr_arr_capsule_volumes_0xb0, Array(this.array_count_for_0xb0, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__capsule_volume))),
	'inst_box_volumes_0xac' / Pointer(this.ptr_arr_box_volumes_0xac, Array(this.array_count_for_0xac, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume))),
	'size' / Computed(lambda this: 212),
	'inst_bounding_convex_hull_0xb4' / Pointer(this.ptr_bounding_convex_hull_0xb4, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume)),
	'inst_sphere_volumes_0xc0' / Pointer(this.ptr_arr_sphere_volumes_0xc0, Array(this.array_count_for_0xc0, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume))),
	'inst_symmetrical_in_axis_0x90' / Pointer(this.ptr_arr_symmetrical_in_axis_0x90, Array(this.array_count_for_0x90, Int8ub)),
	'inst_cylinder_volumes_0xbc' / Pointer(this.ptr_arr_cylinder_volumes_0xbc, Array(this.array_count_for_0xbc, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume))),
	'inst_convex_hull_volumes_0xb8' / Pointer(this.ptr_arr_convex_hull_volumes_0xb8, Array(this.array_count_for_0xb8, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume))),
	'mu_version_hash' / Computed(lambda this: 1567458252),
)

any_genesys_obj__genesys__gen__challenge_action__do_jump = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'accumulate_0x4c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 80),
	'mu_version_hash' / Computed(lambda this: 1667642657),
)

any_genesys_obj__bool8_t = Struct(
)

any_genesys_obj__genesys__gen__physics__landing_damage__pitch = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'max_damage_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 1517189091),
)

any_genesys_obj__genesys__gen__physical_definition__rigid_body__cylinder_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'game_changer_id_0x50' / Int32ul,
	'half_length_0x54' / Float32l,
	'radius_0x58' / Float32l,
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 18021398),
)

any_genesys_obj__genesys__gen__nitrous_parameters__drifting = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'minimum_speed_0x14' / Float32l,
	'nitrous_reward_0x18' / Float32l,
	'time_drifting_0x1c' / Float32l,
	'is_enabled_0x20' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 2207259302),
)

any_genesys_obj__genesys__gen__low_pass_butterworth_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'order_0x18' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 4000215473),
)

any_genesys_obj__genesys__gen__post_fxstate__value_modifier = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'modification__value_0x10' / Float32l,
	'modification__type_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 4120564202),
)

any_genesys_obj__genesys__gen__vehicle_surface_profile = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_genesys__gen__vehicle_surface_profile__surface_link_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_genesys__gen__vehicle_surface_profile__surface_link_0x10' / Pointer(this.ptr_arr_genesys__gen__vehicle_surface_profile__surface_link_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_surface_profile__surface_link))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3049882700),
)

any_genesys_obj__genesys__gen__wcvfx_behaviour__coronas = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'corona_definition_0xc' / FixedSized(8, GreedyBytes),
	'locator_group_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 477429240),
)

any_genesys_obj__genesys__gen__race_car_effect_sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'ptr_arr_automated__values_0x2c' / Int32ul,
	'array_count_for_0x2c' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_automated__values_0x2c' / Pointer(this.ptr_arr_automated__values_0x2c, Array(this.array_count_for_0x2c, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_effect_sequence_item__effect_double_value))),
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 166370211),
)

any_genesys_obj__genesys__gen__game_mode = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'maps_acceptors_0xc' / Int32ul,
	'cgs_core__unique_id_0x10' / Int32ul,
	'description_0x14' / Int32ul,
	'game_changer_id_0x18' / Int32ul,
	'hsm_0x1c' / Int32ul,
	'hud__hsm_0x20' / Int32ul,
	'intro_0x24' / Int32ul,
	'mix_snap_shot_0x28' / Int32ul,
	'cgs_core__unique_id_0x2c' / Int32ul,
	'name_0x30' / Int32ul,
	'results_sequence_0x34' / Int32ul,
	'score_view_model_0x38' / Int32ul,
	'cgs_core__unique_id_0x3c' / Int32ul,
	'weapon_list_0x40' / Int32ul,
	'float32_t_0x44' / Float32l,
	'mode_intro_time_limit_0x48' / Float32l,
	'mode_time_limit_0x4c' / Float32l,
	'timeout_time_0x50' / Float32l,
	'on_bust_0x54' / Int16ul,
	'ranking_type_0x56' / Int16ul,
	'unk_enum_0x58' / Int16ul,
	'intercepting_cop_frequency_0x5a' / Int16ul,
	'minimap_distance_0x5c' / Int16ul,
	'mode_score_limit_0x5e' / Int16ul,
	'oncoming_cop_frequency_0x60' / Int16ul,
	'trailing_cop_frequency_0x62' / Int16ul,
	'uint16_t_0x64' / Int16ul,
	'allow_airacer_damage_from_world_0x66' / Int8ub,
	'allow_friendly_fire_0x67' / Int8ub,
	'bool8_t_0x68' / Int8ub,
	'bool8_t_0x69' / Int8ub,
	'host_can_end_game_0x6a' / Int8ub,
	'online_0x6b' / Int8ub,
	'retry_enabled_0x6c' / Int8ub,
	'bool8_t_0x6d' / Int8ub,
	'show_checkpoints_0x6e' / Int8ub,
	'bool8_t_0x6f' / Int8ub,
	'spawn_towards_ai_0x70' / Int8ub,
	'team_game_0x71' / Int8ub,
	'timer_counts_up_0x72' / Int8ub,
	'bool8_t_0x73' / Int8ub,
	'bool8_t_0x74' / Int8ub,
	'feedback_group_id_0x75' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 120),
	'mu_version_hash' / Computed(lambda this: 2658850274),
)

any_genesys_obj__genesys__gen__event_arena = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'image_0x10' / Int32ul,
	'map_0x14' / Int32ul,
	'name_0x18' / Int32ul,
	'world_0x1c' / Int32ul,
	'ptr_arena_data_0x20' / Int32ul,
	'inst_arena_data_0x20' / Pointer(this.ptr_arena_data_0x20, LazyBound(lambda: any_genesys_obj__genesys__gen__event_arena_data)),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 4102322433),
)

any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_height_change = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3108376025),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'damage_0x14' / Float32l,
	'linear__solve_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 2169124928),
)

any_genesys_obj__genesys__gen__nitrous_parameters__traffic_oncoming = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'minimum_speed_0x14' / Float32l,
	'minimum_time_0x18' / Float32l,
	'nitrous_reward_0x1c' / Float32l,
	'oncoming_timeout_0x20' / Float32l,
	'is_enabled_0x24' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 2600271809),
)

any_genesys_obj__genesys__gen__game_pack = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'name_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'car_pack_image_0x14' / Int32ul,
	'display_name_0x18' / Int32ul,
	'game_changer_id_0x1c' / Int32ul,
	'cgs_core__unique_id_0x20' / Int32ul,
	'show_pack_on_entitlement_0x24' / Int32ul,
	'release_0x28' / Int16ul,
	'display_purchase_0x2a' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 793749252),
)

any_genesys_obj__genesys__gen__body_movement_behaviour__take_off_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'size' / Computed(lambda this: 72),
	'mu_version_hash' / Computed(lambda this: 1129268118),
)

any_genesys_obj__genesys__gen__road_block_definition = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_arr_back_layers_0xc' / Int32ul,
	'ptr_arr_front_layers_0x10' / Int32ul,
	'game_changer_id_0x14' / Int32ul,
	'ptr_arr_cgs_core__unique_id_0x18' / Int32ul,
	'primary_layer_0x1c' / Int32ul,
	'sequence_0x20' / Int32ul,
	'layer_distance_0x24' / Float32l,
	'array_count_for_0xc' / Int16ul,
	'array_count_for_0x10' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_back_layers_0xc' / Pointer(this.ptr_arr_back_layers_0xc, Array(this.array_count_for_0xc, Int32ul)),
	'size' / Computed(lambda this: 48),
	'inst_cgs_core__unique_id_0x18' / Pointer(this.ptr_arr_cgs_core__unique_id_0x18, Array(this.array_count_for_0x18, Int32ul)),
	'inst_front_layers_0x10' / Pointer(this.ptr_arr_front_layers_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'mu_version_hash' / Computed(lambda this: 2488860623),
)

any_genesys_obj__genesys__gen__wheel_suspension_spring_constraint = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'bool8_t_0x24' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 736842216),
)

any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'roadblock_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c' / Int32ul,
	'array_count_for_0x1c' / Int16ul,
	'spawn_cops_0x22' / Int8ub,
	'middleton_datagram_0x23' / Int8ub,
	'inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c' / Pointer(this.ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c, Array(this.array_count_for_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour))),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 1558321222),
)

any_genesys_obj__genesys__gen__passby_sequence_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'cgs_resource__handle_0x1c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x24' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x2c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x34' / FixedSized(8, GreedyBytes),
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'float32_t_0x4c' / Float32l,
	'float32_t_0x50' / Float32l,
	'float32_t_0x54' / Float32l,
	'float32_t_0x58' / Float32l,
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 3085849010),
)

any_genesys_obj__genesys__gen__challenge_action__coop_accumulate_distance = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 2039183453),
)

any_genesys_obj__genesys__gen__ginsu_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 231346471),
)

any_genesys_obj__genesys__gen__collision_effects__traffic_effect__extra_roll_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1807127390),
)

any_genesys_obj__ptr_ptr = Struct(
	'offset' / Int32sl,
	'ptr' / Pointer(this.offset, If(this.offset != 0, LazyBound(lambda: any_genesys_obj__ptr))),
)

any_genesys_obj__genesys__gen__physical_definition__rigid_body = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'body_to_object_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'com_offset_0x50' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'inertia__scale_0x60' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'local_aabbcenter_0x70' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'local_aabbhalf_diagonal_0x80' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'ptr_arr_symmetrical_in_axis_0x90' / Int32ul,
	'game_changer_id_0x94' / Int32ul,
	'angular_drag_0x98' / Float32l,
	'bounciness_0x9c' / Float32l,
	'friction_0xa0' / Float32l,
	'linear_drag_0xa4' / Float32l,
	'mass_0xa8' / Float32l,
	'ptr_arr_box_volumes_0xac' / Int32ul,
	'ptr_arr_capsule_volumes_0xb0' / Int32ul,
	'ptr_bounding_convex_hull_0xb4' / Int32ul,
	'ptr_arr_convex_hull_volumes_0xb8' / Int32ul,
	'ptr_arr_cylinder_volumes_0xbc' / Int32ul,
	'ptr_arr_sphere_volumes_0xc0' / Int32ul,
	'array_count_for_0xac' / Int16ul,
	'array_count_for_0xb0' / Int16ul,
	'array_count_for_0xb8' / Int16ul,
	'array_count_for_0xbc' / Int16ul,
	'array_count_for_0xc0' / Int16ul,
	'array_count_for_0x90' / Int16ul,
	'is_wheel_0xd0' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_capsule_volumes_0xb0' / Pointer(this.ptr_arr_capsule_volumes_0xb0, Array(this.array_count_for_0xb0, LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__capsule_volume))),
	'inst_box_volumes_0xac' / Pointer(this.ptr_arr_box_volumes_0xac, Array(this.array_count_for_0xac, LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__box_volume))),
	'size' / Computed(lambda this: 212),
	'inst_bounding_convex_hull_0xb4' / Pointer(this.ptr_bounding_convex_hull_0xb4, LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__convex_hull_volume)),
	'inst_sphere_volumes_0xc0' / Pointer(this.ptr_arr_sphere_volumes_0xc0, Array(this.array_count_for_0xc0, LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__sphere_volume))),
	'inst_symmetrical_in_axis_0x90' / Pointer(this.ptr_arr_symmetrical_in_axis_0x90, Array(this.array_count_for_0x90, Int8ub)),
	'inst_cylinder_volumes_0xbc' / Pointer(this.ptr_arr_cylinder_volumes_0xbc, Array(this.array_count_for_0xbc, LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__cylinder_volume))),
	'inst_convex_hull_volumes_0xb8' / Pointer(this.ptr_arr_convex_hull_volumes_0xb8, Array(this.array_count_for_0xb8, LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__convex_hull_volume))),
	'mu_version_hash' / Computed(lambda this: 1567458252),
)

any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__light = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'colour_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'cgs_resource__handle_0x20' / FixedSized(8, GreedyBytes),
	'light_definition_0x28' / FixedSized(8, GreedyBytes),
	'locator_group_0x30' / Int32ul,
	'float32_t_0x34' / Float32l,
	'unk_enum_0x38' / Int16ul,
	'time_of_day_0x3a' / Int16ul,
	'size' / Computed(lambda this: 64),
	'mu_version_hash' / Computed(lambda this: 123660642),
)

any_genesys_obj__genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'vehicle_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'ptr_arr_mods_0x14' / Int32ul,
	'inline_arr_target_scores_0x18' / Array(3, Int16sl),
	'inline_arr_target_speeds_0x1e' / Array(3, Int16sl),
	'array_count_for_0x14' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'array_count_for_0x1e' / Int16ul,
	'difficulty_0x2a' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'inst_mods_0x14' / Pointer(this.ptr_arr_mods_0x14, Array(this.array_count_for_0x14, Int32ul)),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 956776100),
)

any_genesys_obj__int16_t = Struct(
)

any_genesys_obj__genesys__gen__dynamic_additional_info = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'sequence_0xc' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x14' / Int32ul,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'strength_0x20' / Float32l,
	'score_0x24' / Int16ul,
	'bool8_t_0x26' / Int8ub,
	'bool8_t_0x27' / Int8ub,
	'bool8_t_0x28' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 2950917875),
)

any_genesys_obj__genesys__gen__gameplay__milestone__entry = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'award_0xc' / Int32ul,
	'value_0x10' / Float32l,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 2921338515),
)

any_genesys_obj__genesys__gen__engine__differentials = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 709116355),
)

any_genesys_obj__genesys__gen__engine_sound2__dsp_param_wrapper = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_genesys__gen__engine_sound2__dsp_param_0xc' / Int32ul,
	'inst_genesys__gen__engine_sound2__dsp_param_0xc' / Pointer(this.ptr_genesys__gen__engine_sound2__dsp_param_0xc, LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__dsp_param)),
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 2477895213),
)

any_genesys_obj__genesys__gen__event_list = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_ordered_list_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_ordered_list_0x10' / Pointer(this.ptr_arr_ordered_list_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 981367156),
)

any_genesys_obj__genesys__gen__collision_info__battling_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ai__extra__roll_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__battling_effect__extra_roll_params),
	'player__extra__roll_0x24' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__battling_effect__extra_roll_params),
	'cam__effect_0x3c' / FixedSized(8, GreedyBytes),
	'cam__effect__scale_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'size' / Computed(lambda this: 80),
	'mu_version_hash' / Computed(lambda this: 1886238258),
)

any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x3c' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x64' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params),
	'game_changer_id_0x8c' / Int32ul,
	'size' / Computed(lambda this: 148),
	'mu_version_hash' / Computed(lambda this: 3530258211),
)

any_genesys_obj__genesys__gen__engine__mix = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'engine_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'pops_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 1901399892),
)

any_genesys_obj__genesys__gen__vehicles__sound__transmission_whine = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_sequences_0x10' / Int32ul,
	'array_count_for_0x10' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_sequences_0x10' / Pointer(this.ptr_arr_sequences_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 618870438),
)

any_genesys_obj__genesys__gen__nitrous_strength__punch = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 4084465158),
)

any_genesys_obj__genesys__gen__steering_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'float32_t_0x4c' / Float32l,
	'float32_t_0x50' / Float32l,
	'float32_t_0x54' / Float32l,
	'float32_t_0x58' / Float32l,
	'float32_t_0x5c' / Float32l,
	'float32_t_0x60' / Float32l,
	'float32_t_0x64' / Float32l,
	'float32_t_0x68' / Float32l,
	'float32_t_0x6c' / Float32l,
	'float32_t_0x70' / Float32l,
	'size' / Computed(lambda this: 120),
	'mu_version_hash' / Computed(lambda this: 2612185096),
)

any_genesys_obj__genesys__gen__ginsu_sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'fade__out_0x38' / LazyBound(lambda: any_genesys_obj__genesys__gen__ginsu_sequence_item__fade),
	'cgs_resource__handle_0x4c' / FixedSized(8, GreedyBytes),
	'mixer__channel_0x54' / FixedSized(8, GreedyBytes),
	'size' / Computed(lambda this: 92),
	'mu_version_hash' / Computed(lambda this: 773308239),
)

any_genesys_obj__genesys__gen__steering_wheel_physics = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 1329740588),
)

any_genesys_obj__genesys__gen__physics__damage_bar_profile__segment = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'lamps_corked_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'recharge_time_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'size_0x24' / Float32l,
	'bool8_t_0x28' / Int8ub,
	'recharges_0x29' / Int8ub,
	'adapter_wales_0x2a' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 880609546),
)

any_genesys_obj__genesys__gen__offline_event__alternate_routes = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'checkpoint_0xc' / Int32ul,
	'ptr_arr_route_markers_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_route_markers_0x10' / Pointer(this.ptr_arr_route_markers_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 456387781),
)

any_genesys_obj__genesys__gen__collision_responses__world__crashed_player = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__collision_responses__world__crashed_player__constraint_data_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__crashed_player__constraint_data),
	'dodge_ginger_0x24' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__crashed_player__constraint_data),
	'game_changer_id_0x3c' / Int32ul,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 1325791513),
)

any_genesys_obj__genesys__gen__delay_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'time_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3627785814),
)

any_genesys_obj__genesys__gen__donut_ability__donut_scale = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 1015007408),
)

any_genesys_obj__genesys__gen__gearbox = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__gearbox__gear_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__gearbox__gear),
	'game_changer_id_0x28' / Int32ul,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'ptr_arr_genesys__gen__gearbox__gear_0x4c' / Int32ul,
	'array_count_for_0x4c' / Int16ul,
	'bool8_t_0x52' / Int8ub,
	'bool8_t_0x53' / Int8ub,
	'bool8_t_0x54' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_genesys__gen__gearbox__gear_0x4c' / Pointer(this.ptr_arr_genesys__gen__gearbox__gear_0x4c, Array(this.array_count_for_0x4c, LazyBound(lambda: any_genesys_obj__genesys__gen__gearbox__gear))),
	'size' / Computed(lambda this: 88),
	'mu_version_hash' / Computed(lambda this: 3732602870),
)

any_genesys_obj__genesys__gen__physics__damage_bar_profile__impact_location_damage_scale = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 2817660171),
)

any_genesys_obj__genesys__gen__challenge__location = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__unique_id_0xc' / Int32ul,
	'ptr_arr_display_trigger_0x10' / Int32ul,
	'game_changer_id_0x14' / Int32ul,
	'ptr_arr_triggers_0x18' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'inst_display_trigger_0x10' / Pointer(this.ptr_arr_display_trigger_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'inst_triggers_0x18' / Pointer(this.ptr_arr_triggers_0x18, Array(this.array_count_for_0x18, Int32ul)),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 944731751),
)

any_genesys_obj__genesys__gen__cloud_compete_award = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'description_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'title_0x14' / Int32ul,
	'unlock_string_0x18' / Int32ul,
	'category_0x1c' / Int16ul,
	'action_destination_0x1e' / Int16ul,
	'uint16_t_0x20' / Int16ul,
	'bool8_t_0x22' / Int8ub,
	'uint8_t_0x23' / Int8ub,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 3996354190),
)

any_genesys_obj__genesys__gen__sequence_items__post_fx_override_sequence_item__effect_double_value = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_modulating_value_0xc' / Int32ul,
	'automated__property_0x10' / Int32ul,
	'inst_modulating_value_0xc' / Pointer(this.ptr_modulating_value_0xc, LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1642529028),
)

any_genesys_obj__ptr_array = Struct(
	'offset' / Int32sl,
	'entries' / Pointer(this.offset, Array(this.amt, LazyBound(lambda: any_genesys_obj__atype))),
)

any_genesys_obj__genesys__gen__engine__sound = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'idle_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'size' / Computed(lambda this: 64),
	'mu_version_hash' / Computed(lambda this: 3641337381),
)

any_genesys_obj__genesys__gen__nitrous_parameters__donutting = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'max_speed_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'nitrous_reward_0x1c' / Float32l,
	'is_enabled_0x20' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 3928390869),
)

any_genesys_obj__genesys__gen__vehicle_info__extra_axle = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'int32_t_0x14' / Int32sl,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3588678847),
)

any_genesys_obj__genesys__gen__tyre_sound_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__tyre_sound_params__lateral_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__lateral),
	'genesys__gen__tyre_sound_params__lat_slip_0x3c' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__lat_slip),
	'genesys__gen__tyre_sound_params__longitudinal_0x64' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__longitudinal),
	'genesys__gen__tyre_sound_params__long_spin_braking_0x8c' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__long_spin_braking),
	'genesys__gen__tyre_sound_params__long_spin_0xb4' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__long_spin),
	'game_changer_id_0xd8' / Int32ul,
	'size' / Computed(lambda this: 224),
	'mu_version_hash' / Computed(lambda this: 3054130878),
)

any_genesys_obj__genesys__gen__engine__reverse_whine = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__unique_id_0xc' / Int32ul,
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 3727471200),
)

any_genesys_obj__genesys__gen__tyres = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__tyres__tyres_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyres__tyres),
	'genesys__gen__tyres__surface_effects_0x24' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyres__surface_effects),
	'game_changer_id_0x38' / Int32ul,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'float32_t_0x4c' / Float32l,
	'float32_t_0x50' / Float32l,
	'float32_t_0x54' / Float32l,
	'float32_t_0x58' / Float32l,
	'float32_t_0x5c' / Float32l,
	'float32_t_0x60' / Float32l,
	'ptr_genesys__gen__tyre_sound_params_0x64' / Int32ul,
	'inst_genesys__gen__tyre_sound_params_0x64' / Pointer(this.ptr_genesys__gen__tyre_sound_params_0x64, LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params)),
	'size' / Computed(lambda this: 108),
	'mu_version_hash' / Computed(lambda this: 1425943760),
)

any_genesys_obj__genesys__gen__light__point = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__light__base),
	'size' / Computed(lambda this: 92),
	'mu_version_hash' / Computed(lambda this: 3975851796),
)

any_genesys_obj__genesys__gen__race_car_physical_definition = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10' / Int32ul,
	'ptr_genesys__gen__race_car_physical_definition__physical_definition_0x14' / Int32ul,
	'int32_t_0x18' / Int32sl,
	'int32_t_0x1c' / Int32sl,
	'int32_t_0x20' / Int32sl,
	'int32_t_0x24' / Int32sl,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10' / Pointer(this.ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__convex_hull_conectivity_data))),
	'inst_genesys__gen__race_car_physical_definition__physical_definition_0x14' / Pointer(this.ptr_genesys__gen__race_car_physical_definition__physical_definition_0x14, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition)),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 1316353574),
)

any_genesys_obj__genesys__gen__dsp_plug_in_chain = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_plug_ins_0x10' / Int32ul,
	'array_count_for_0x10' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_plug_ins_0x10' / Pointer(this.ptr_arr_plug_ins_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3826155101),
)

any_genesys_obj__genesys__gen__tyres__tyres = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_genesys__gen__tyre_0x10' / Int32ul,
	'ptr_genesys__gen__tyre_0x14' / Int32ul,
	'inst_genesys__gen__tyre_0x10' / Pointer(this.ptr_genesys__gen__tyre_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__tyre)),
	'inst_genesys__gen__tyre_0x14' / Pointer(this.ptr_genesys__gen__tyre_0x14, LazyBound(lambda: any_genesys_obj__genesys__gen__tyre)),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 368598916),
)

any_genesys_obj__genesys__gen__behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'label_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'game_changer_id_0x14' / Int32ul,
	'activate_on_hit_0x18' / Int8ub,
	'deactivate_on_hit_0x19' / Int8ub,
	'initially_on_0x1a' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 160896465),
)

any_genesys_obj__genesys__gen__thank_you_screen_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'heading_0x10' / Int32ul,
	'message_0x14' / Int32ul,
	'bounty_reward_0x18' / Int32sl,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 2578912561),
)

any_genesys_obj__genesys__gen__light__projected_texture = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__light__base),
	'rw_math_vpu__vector2_0x60' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector2),
	'rw_math_vpu__vector3_0x70' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector4_0x80' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'material_0x90' / FixedSized(8, GreedyBytes),
	'size' / Computed(lambda this: 152),
	'mu_version_hash' / Computed(lambda this: 229133803),
)

any_genesys_obj__genesys__gen__camera_gameplay_external__camera__roll = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 3508674618),
)

any_genesys_obj__genesys__gen__engine__normal_quality_engine = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 2847735672),
)

any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car__params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'damage_0x14' / Float32l,
	'linear__solve_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 716630460),
)

any_genesys_obj__genesys__gen__gameplay__offline_upgrade = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'apply_sequence_0xc' / Int32ul,
	'description_0x10' / Int32ul,
	'game_changer_id_0x14' / Int32ul,
	'image_0x18' / Int32ul,
	'milestone_required_0x1c' / Int32ul,
	'name_0x20' / Int32ul,
	'short_name_0x24' / Int32ul,
	'category_0x28' / Int16ul,
	'type_0x2a' / Int16ul,
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 112782069),
)

any_genesys_obj__genesys__gen__tyre_vfx_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params_0x13c' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params),
	'game_changer_id_0x26c' / Int32ul,
	'size' / Computed(lambda this: 628),
	'mu_version_hash' / Computed(lambda this: 4074208643),
)

any_genesys_obj__genesys__gen__light__base__flash_pattern = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'duration_0x10' / Float32l,
	'frequency_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'offset_0x1c' / Float32l,
	'type_0x20' / Int32ul,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 306714612),
)

any_genesys_obj__genesys__gen__gameplay_trigger__output = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'predicate_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'ptr_arr_speech__events_0x14' / Int32ul,
	'ptr_arr_ptr_aiplayers_0x18' / Int32ul,
	'ptr_arr_sequence_0x1c' / Int32ul,
	'ptr_arr_ptr_roadblock_instance_0x20' / Int32ul,
	'array_count_for_0x18' / Int16ul,
	'array_count_for_0x1c' / Int16ul,
	'array_count_for_0x20' / Int8ub,
	'array_count_for_0x14' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_aiplayers_0x18' / Pointer(this.ptr_arr_ptr_aiplayers_0x18, Array(this.array_count_for_0x18, LazyBound(lambda: any_genesys_obj__ptr))),
	'inst_roadblock_instance_0x20' / Pointer(this.ptr_arr_ptr_roadblock_instance_0x20, Array(this.array_count_for_0x20, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 44),
	'inst_sequence_0x1c' / Pointer(this.ptr_arr_sequence_0x1c, Array(this.array_count_for_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__output__sequence_output))),
	'inst_speech__events_0x14' / Pointer(this.ptr_arr_speech__events_0x14, Array(this.array_count_for_0x14, Int32ul)),
	'mu_version_hash' / Computed(lambda this: 835914245),
)

any_genesys_obj__genesys__gen__collision_effects__world_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cam__effect_0xc' / FixedSized(8, GreedyBytes),
	'cam__effect__unstable_0x14' / FixedSized(8, GreedyBytes),
	'cam__effect__scale_0x1c' / Float32l,
	'stable__camera__threshold_0x20' / Float32l,
	'unstable__camera__threshold_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 2825220545),
)

any_genesys_obj__genesys__gen__physical_definition__rigid_body__capsule_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'game_changer_id_0x50' / Int32ul,
	'half_length_0x54' / Float32l,
	'radius_0x58' / Float32l,
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 18021398),
)

any_genesys_obj__genesys__gen__engine__power_curve = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'ptr_arr_ptr_genesys__gen__point2dwith_tangents_0x4c' / Int32ul,
	'array_count_for_0x4c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_genesys__gen__point2dwith_tangents_0x4c' / Pointer(this.ptr_arr_ptr_genesys__gen__point2dwith_tangents_0x4c, Array(this.array_count_for_0x4c, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 84),
	'mu_version_hash' / Computed(lambda this: 3195239353),
)

any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'damage_to_deal_0xc' / Float32l,
	'should_wreck_0x10' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 1483915852),
)

any_genesys_obj__genesys__gen__collision_responses__race_car = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'player__vs__traffic_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic),
	'player__vs__ai_0x100' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai),
	'ai__vs__traffic_0x1e8' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic),
	'player__vs__crashing__race__car_0x2c0' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car),
	'ai__vs__crashing__race__car_0x368' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_crashing_race_car),
	'ai__car__vs__dynamic_0x3d0' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__race_car_vs_dynamic),
	'player_or__network_car__vs__dynamic_0x40c' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__race_car_vs_dynamic),
	'game_changer_id_0x448' / Int32ul,
	'size' / Computed(lambda this: 1104),
	'mu_version_hash' / Computed(lambda this: 524753351),
)

any_genesys_obj__genesys__gen__race_car_effect_sequence_item__effect_double_value = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_modulating_value_0xc' / Int32ul,
	'automated__property_0x10' / Int32ul,
	'inst_modulating_value_0xc' / Pointer(this.ptr_modulating_value_0xc, LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1852100653),
)

any_genesys_obj__genesys__gen__gameplay__cop_type = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'aiplayer_type_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'bool8_t_0x14' / Int8ub,
	'can_spawn_behind_0x15' / Int8ub,
	'can_spawn_head_on_0x16' / Int8ub,
	'can_spawn_intercepting_0x17' / Int8ub,
	'bool8_t_0x18' / Int8ub,
	'bool8_t_0x19' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1758839251),
)

any_genesys_obj__genesys__gen__nucleus_grant_mappings_list__mapping = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'nucleus_tag_0x10' / Int32ul,
	'ptr_arr_entitlement_0x14' / Int32ul,
	'array_count_for_0x14' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_entitlement_0x14' / Pointer(this.ptr_arr_entitlement_0x14, Array(this.array_count_for_0x14, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 4263309034),
)

any_genesys_obj__genesys__gen__challenge_action__action_base = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'feedback_data_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base__feedback_data),
	'cgs_core__unique_id_0x30' / Int32ul,
	'cgs_core__unique_id_0x34' / Int32ul,
	'game_changer_id_0x38' / Int32ul,
	'ptr_accumulation_data_0x3c' / Int32ul,
	'builtin_evoke_0x40' / Int16ul,
	'scoring_method_0x42' / Int16ul,
	'unk_enum_0x44' / Int16ul,
	'who_0x46' / Int16ul,
	'inst_accumulation_data_0x3c' / Pointer(this.ptr_accumulation_data_0x3c, LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulation_helper_data)),
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 3948195379),
)

any_genesys_obj__genesys__gen__online__driving_test_list = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'description_0xc' / Int32ul,
	'ptr_arr_driving_tests_0x10' / Int32ul,
	'game_changer_id_0x14' / Int32ul,
	'name_0x18' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_driving_tests_0x10' / Pointer(this.ptr_arr_driving_tests_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 1755540478),
)

any_genesys_obj__genesys__gen__lfo_sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'unit_0x28' / Int16ul,
	'automated__values_count_0x2a' / Int16ul,
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 2474227476),
)

any_genesys_obj__genesys__gen__drift_behaviour__drift_exit = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 4039040682),
)

any_genesys_obj__ptr_ptr_table = Struct(
	'offset' / Int32sl,
	'count' / If(this.amt == 0, Int32ul),
	'len' / Computed(lambda this: (0 if this.amt == -1 else (this.count if this.amt == 0 else this.amt))),
	'ptr_table' / Pointer(this.offset, If(this.offset != 0, LazyBound(lambda: any_genesys_obj__ptr_table))),
)

any_genesys_obj__genesys__gen__collision_effects__battling_effect__extra_roll_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3396244228),
)

any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_arr_float32_t_0xc' / Int32ul,
	'ptr_arr_float32_t_0x10' / Int32ul,
	'ptr_arr_float32_t_0x14' / Int32ul,
	'ptr_arr_damage_override_0x18' / Int32ul,
	'array_count_for_0xc' / Int16ul,
	'array_count_for_0x10' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'array_count_for_0x14' / Int16ul,
	'inst_float32_t_0x14' / Pointer(this.ptr_arr_float32_t_0x14, Array(this.array_count_for_0x14, Float32l)),
	'inst_float32_t_0xc' / Pointer(this.ptr_arr_float32_t_0xc, Array(this.array_count_for_0xc, Float32l)),
	'size' / Computed(lambda this: 40),
	'inst_float32_t_0x10' / Pointer(this.ptr_arr_float32_t_0x10, Array(this.array_count_for_0x10, Float32l)),
	'inst_damage_override_0x18' / Pointer(this.ptr_arr_damage_override_0x18, Array(this.array_count_for_0x18, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal))),
	'mu_version_hash' / Computed(lambda this: 1202023644),
)

any_genesys_obj__genesys__gen__vehicle_paint = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'rw_math_vpu__vector4_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x30' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x40' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x50' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x60' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'cgs_core__unique_id_0x70' / Int32ul,
	'game_changer_id_0x74' / Int32ul,
	'name_0x78' / Int32ul,
	'float32_t_0x7c' / Float32l,
	'float32_t_0x80' / Float32l,
	'float32_t_0x84' / Float32l,
	'float32_t_0x88' / Float32l,
	'float32_t_0x8c' / Float32l,
	'float32_t_0x90' / Float32l,
	'float32_t_0x94' / Float32l,
	'float32_t_0x98' / Float32l,
	'unk_enum_0x9c' / Int16ul,
	'type_0x9e' / Int16ul,
	'bool8_t_0xa0' / Int8ub,
	'bool8_t_0xa1' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 164),
	'mu_version_hash' / Computed(lambda this: 669436076),
)

any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'far_distance_0xc' / Float32l,
	'near_distance_0x10' / Float32l,
	'rewarding_highlighting_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 1543118382),
)

any_genesys_obj__genesys__gen__nitrous_parameters__fatal_hit = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'nitrous_reward_0x14' / Float32l,
	'is_enabled_0x18' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3785567855),
)

any_genesys_obj__genesys__gen__race_car_handling_disruption_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'effect_duration_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'high_speed_front_lat_grip_0x18' / Float32l,
	'high_speed_front_long_grip_0x1c' / Float32l,
	'high_speed_rear_lat_grip_0x20' / Float32l,
	'high_speed_rear_long_grip_0x24' / Float32l,
	'high_speed_steer_amount_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'high_speed_threshold_0x30' / Float32l,
	'low_speed_front_lat_grip_0x34' / Float32l,
	'low_speed_front_long_grip_0x38' / Float32l,
	'low_speed_rear_lat_grip_0x3c' / Float32l,
	'low_speed_rear_long_grip_0x40' / Float32l,
	'low_speed_steer_amount_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'low_speed_threshold_0x4c' / Float32l,
	'affects_all_wheels_0x50' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 84),
	'mu_version_hash' / Computed(lambda this: 724902868),
)

any_genesys_obj__genesys__gen__light__base = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'colour_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'genesys__gen__light__base__flash_pattern_0x20' / LazyBound(lambda: any_genesys_obj__genesys__gen__light__base__flash_pattern),
	'game_changer_id_0x44' / Int32ul,
	'float32_t_0x48' / Float32l,
	'intensity_0x4c' / Float32l,
	'bool8_t_0x50' / Int8ub,
	'bool8_t_0x51' / Int8ub,
	'bool8_t_0x52' / Int8ub,
	'bool8_t_0x53' / Int8ub,
	'bool8_t_0x54' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 88),
	'mu_version_hash' / Computed(lambda this: 4046186056),
)

any_genesys_obj__genesys__gen__score_view_model__score_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'binding_path_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'game_changer_id_0x14' / Int32ul,
	'rank_0x18' / Int32sl,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 606909642),
)

any_genesys_obj__genesys__gen__challenge_action__action_base__feedback_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'instruction_0xc' / Int32ul,
	'cgs_core__unique_id_0x10' / Int32ul,
	'cgs_core__unique_id_0x14' / Int32ul,
	'cgs_core__unique_id_0x18' / Int32ul,
	'cgs_core__unique_id_0x1c' / Int32ul,
	'unk_enum_0x20' / Int16ul,
	'bool8_t_0x22' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 1294158455),
)

any_genesys_obj__genesys__gen__sequence_item__modulating_double_value = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'binding_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'binding__exponent_0x14' / Float32l,
	'binding__range__max_0x18' / Float32l,
	'binding__range__min_0x1c' / Float32l,
	'output__value__max_0x20' / Float32l,
	'output__value__min_0x24' / Float32l,
	'value_0x28' / Float32l,
	'unk_enum_0x2c' / Int32ul,
	'animation__modulation__type_0x30' / Int16ul,
	'binding__modulation__type_0x32' / Int16ul,
	'array_count_for_0x2c' / Int16ul,
	'bool8_t_0x36' / Int8ub,
	'binding__invert_0x37' / Int8ub,
	'inst_5a__f6_03_00_0_1_0x2c' / Pointer(this.unk_enum_0x2c, Array(this.array_count_for_0x2c, Int32ul)),
	'size' / Computed(lambda this: 60),
	'mu_version_hash' / Computed(lambda this: 1489464845),
)

any_genesys_obj__genesys__gen__heat_level_sound_set__sirens = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_arr_blip__waves_0xc' / Int32ul,
	'ptr_arr_extra__waves_0x10' / Int32ul,
	'ptr_arr_rumbler__waves_0x14' / Int32ul,
	'standard__wave_0x18' / Int32ul,
	'array_count_for_0xc' / Int16ul,
	'array_count_for_0x10' / Int16ul,
	'array_count_for_0x14' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 36),
	'inst_rumbler__waves_0x14' / Pointer(this.ptr_arr_rumbler__waves_0x14, Array(this.array_count_for_0x14, Int32ul)),
	'inst_extra__waves_0x10' / Pointer(this.ptr_arr_extra__waves_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'inst_blip__waves_0xc' / Pointer(this.ptr_arr_blip__waves_0xc, Array(this.array_count_for_0xc, Int32ul)),
	'mu_version_hash' / Computed(lambda this: 1058122174),
)

any_genesys_obj__genesys__gen__gameplay_trigger__aiplayer_information = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'placement_0xc' / Int32ul,
	'ptr_aiplayer_instance_0x10' / Int32ul,
	'inst_aiplayer_instance_0x10' / Pointer(this.ptr_aiplayer_instance_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__aiplayer_instance)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1291389730),
)

any_genesys_obj__genesys__gen__vehicle__driver_setup = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'rw_math_vpu__vector3_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'ptr_arr_cgs_core__unique_id_0x20' / Int32ul,
	'cgs_core__unique_id_0x24' / Int32ul,
	'game_changer_id_0x28' / Int32ul,
	'cgs_core__unique_id_0x2c' / Int32ul,
	'cgs_core__unique_id_0x30' / Int32ul,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'ptr_arr_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c' / Int32ul,
	'array_count_for_0x20' / Int16ul,
	'array_count_for_0x3c' / Int16ul,
	'bool8_t_0x44' / Int8ub,
	'bool8_t_0x45' / Int8ub,
	'bool8_t_0x46' / Int8ub,
	'bool8_t_0x47' / Int8ub,
	'inst_cgs_core__unique_id_0x20' / Pointer(this.ptr_arr_cgs_core__unique_id_0x20, Array(this.array_count_for_0x20, Int32ul)),
	'inst_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c' / Pointer(this.ptr_arr_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c, Array(this.array_count_for_0x3c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__driver_setup__seat_belt_bone_offset))),
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 3584499810),
)

any_genesys_obj__genesys__gen__uilist_items__item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'value_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'display_string_0x14' / Int32ul,
	'game_changer_id_0x18' / Int32ul,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 101265141),
)

any_genesys_obj__genesys__gen__challenge_action__speed_camera_action = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'on_hit_sequence_0x4c' / Int32ul,
	'ptr_genesys__gen__challenge__location_0x50' / Int32ul,
	'inst_genesys__gen__challenge__location_0x50' / Pointer(this.ptr_genesys__gen__challenge__location_0x50, LazyBound(lambda: any_genesys_obj__genesys__gen__challenge__location)),
	'size' / Computed(lambda this: 88),
	'mu_version_hash' / Computed(lambda this: 3823531688),
)

any_genesys_obj__genesys__gen__camera_gameplay_external_globals__lens_properties = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'bool8_t_0x18' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2401606622),
)

any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'local_aabbcenter_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'local_aabbhalf_diagonal_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'additional_info_0x30' / FixedSized(8, GreedyBytes),
	'ptr_arr_rigid_bodies_names_0x38' / Int32ul,
	'game_changer_id_0x3c' / Int32ul,
	'ptr_arr_rigid_bodies_0x40' / Int32ul,
	'game_changer_id_0x44' / Int32sl,
	'main_rigid_body_index_0x48' / Int32sl,
	'array_count_for_0x40' / Int16ul,
	'array_count_for_0x38' / Int16ul,
	'bool8_t_0x50' / Int8ub,
	'bool8_t_0x51' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_rigid_bodies_names_0x38' / Pointer(this.ptr_arr_rigid_bodies_names_0x38, Array(this.array_count_for_0x38, LazyBound(lambda: any_genesys_obj__string_base))),
	'inst_rigid_bodies_0x40' / Pointer(this.ptr_arr_rigid_bodies_0x40, Array(this.array_count_for_0x40, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body))),
	'size' / Computed(lambda this: 84),
	'mu_version_hash' / Computed(lambda this: 2519567673),
)

any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'x_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation__axis_params),
	'y_0x38' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation__axis_params),
	'z_0x64' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation__axis_params),
	'game_changer_id_0x90' / Int32ul,
	'amplitude_0x94' / Float32l,
	'size' / Computed(lambda this: 156),
	'mu_version_hash' / Computed(lambda this: 866205257),
)

any_genesys_obj__genesys__gen__tyre_sound_params__longitudinal = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 2992725297),
)

any_genesys_obj__genesys__gen__challenge_action__accumulate_near_misses = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'ptr_location_0x4c' / Int32ul,
	'in_air_0x50' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_location_0x4c' / Pointer(this.ptr_location_0x4c, LazyBound(lambda: any_genesys_obj__genesys__gen__challenge__location)),
	'size' / Computed(lambda this: 84),
	'mu_version_hash' / Computed(lambda this: 732433969),
)

any_genesys_obj__genesys__gen__camera_gameplay_bumper = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_bonnet),
	'size' / Computed(lambda this: 132),
	'mu_version_hash' / Computed(lambda this: 983393262),
)

any_genesys_obj__genesys__gen__vehicles__tyre_upgrade = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 2784884141),
)

any_genesys_obj__genesys__gen__entitlement = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'description_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'entitlement_tag_0x14' / LazyBound(lambda: any_genesys_obj__string_base),
	'name_0x1c' / LazyBound(lambda: any_genesys_obj__string_base),
	'game_changer_id_0x24' / Int32ul,
	'purchasable_0x28' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 2560361681),
)

any_genesys_obj__genesys__gen__engine_sound2__dsp_param = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_resource__handle_0xc' / FixedSized(8, GreedyBytes),
	'plug_in_0x14' / Int32ul,
	'value_0x18' / Float32l,
	'unk_enum_0x1c' / Int32ul,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 174067018),
)

any_genesys_obj__genesys__gen__score_view_model__score = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'action_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'string_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2080073476),
)

any_genesys_obj__genesys__gen__wcvfx_behaviour__spot_effects = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_resource__handle_0xc' / FixedSized(8, GreedyBytes),
	'locator_group_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2208212217),
)

any_genesys_obj__genesys__gen__collision_responses__world__player = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'high_speed_flip_state_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__player__flip_state),
	'low_speed_flip_state_0x2c' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__player__flip_state),
	'game_changer_id_0x4c' / Int32ul,
	'dynamic_friction_0x50' / Float32l,
	'restitution_0x54' / Float32l,
	'solve_position_angular_scale_0x58' / Float32l,
	'solve_velocity_angular_scale_0x5c' / Float32l,
	'static_friction_0x60' / Float32l,
	'size' / Computed(lambda this: 104),
	'mu_version_hash' / Computed(lambda this: 4260207896),
)

any_genesys_obj__genesys__gen__online__vote_event = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__online_event),
	'cgs_core__unique_id_0x70' / Int32ul,
	'cgs_core__unique_id_0x74' / Int32ul,
	'cgs_core__unique_id_0x78' / Int32ul,
	'cgs_core__unique_id_0x7c' / Int32ul,
	'size' / Computed(lambda this: 132),
	'mu_version_hash' / Computed(lambda this: 3136795337),
)

any_genesys_obj__genesys__gen__tyre__lateral__slip__factors = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 166064775),
)

any_genesys_obj__genesys__gen__mixer_channel = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'distance_falloff_0xc' / FixedSized(8, GreedyBytes),
	'plug_in__chain_0x14' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x1c' / Int32ul,
	'mixing_group_0x20' / Int32ul,
	'centre_level_0x24' / Float32l,
	'emitter_response_0x28' / Float32l,
	'focus_0x2c' / Float32l,
	'gain_0x30' / Float32l,
	'lfe_send_0x34' / Float32l,
	'panning__cosine_0x38' / Float32l,
	'panning__divergence_0x3c' / Float32l,
	'panning__sine_0x40' / Float32l,
	'reverb_send_a_0x44' / Float32l,
	'reverb_send_b_0x48' / Float32l,
	'ptr_arr_priority_0x4c' / Int32ul,
	'ptr_voice_group_0x50' / Int32ul,
	'doppler_model_0x54' / Int16ul,
	'virtual_voice_behaviour_0x56' / Int16ul,
	'array_count_for_0x4c' / Int16ul,
	'cull_playing_voices_0x5a' / Int8ub,
	'panning__override_0x5b' / Int8ub,
	'instance_limit_0x5c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_priority_0x4c' / Pointer(this.ptr_arr_priority_0x4c, Array(this.array_count_for_0x4c, LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel__priority))),
	'inst_voice_group_0x50' / Pointer(this.ptr_voice_group_0x50, LazyBound(lambda: any_genesys_obj__genesys__gen__voice_group)),
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 2971966527),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__basic_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'linear__solve_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1951683017),
)

any_genesys_obj__genesys__gen__online__license_plate = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'backing_image_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'name_0x14' / Int32ul,
	'release_0x18' / Int32ul,
	'bool8_t_0x1c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 1106192363),
)

any_genesys_obj__uint8_t = Struct(
)

any_genesys_obj__genesys__gen__event_location = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'inline_arr_position_0xc' / Array(3, Float32l),
	'event_list_0x18' / FixedSized(8, GreedyBytes),
	'main_map_camera_0x20' / FixedSized(8, GreedyBytes),
	'zoomed_map_camera_0x28' / FixedSized(8, GreedyBytes),
	'freedrive_event_0x30' / Int32ul,
	'game_changer_id_0x34' / Int32ul,
	'name_0x38' / Int32ul,
	'original_game_pack_0x3c' / Int32ul,
	'array_count_for_0xc' / Int16ul,
	'is_cop_location_0x42' / Int8ub,
	'is_online_0x43' / Int8ub,
	'size' / Computed(lambda this: 72),
	'mu_version_hash' / Computed(lambda this: 3916132985),
)

any_genesys_obj__genesys__gen__vehicles__performance_upgrades__category = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x10' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x14' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x18' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x1c' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x20' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x24' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x28' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x2c' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x30' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x34' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x38' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x3c' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x40' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x44' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x48' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x4c' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0x50' / Int32ul,
	'inst_genesys__gen__vehicles__upgrade_base_0x24' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x24, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x18' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x18, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x38' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x38, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x10' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x14' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x14, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x3c' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x3c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x28' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x28, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x20' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x20, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'size' / Computed(lambda this: 88),
	'inst_genesys__gen__vehicles__upgrade_base_0x34' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x34, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x40' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x40, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x30' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x30, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x2c' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x2c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x50' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x50, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x1c' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x48' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x48, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0x44' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x44, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'mu_version_hash' / Computed(lambda this: 2230798373),
	'inst_genesys__gen__vehicles__upgrade_base_0x4c' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0x4c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
)

any_genesys_obj__genesys__gen__make_physical_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'unk_enum_0x1c' / Int16ul,
	'collidable_0x1e' / Int8ub,
	'initially_frozen_0x1f' / Int8ub,
	'bool8_t_0x20' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 3788863516),
)

any_genesys_obj__genesys__gen__smash_proxy_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 3085449154),
)

any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation__axis_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'amplitude_0x10' / Float32l,
	'inwards__damping_0x14' / Float32l,
	'lower__translation__limit_0x18' / Float32l,
	'outwards__damping_0x1c' / Float32l,
	'spring__coefficient_0x20' / Float32l,
	'upper__translation__limit_0x24' / Float32l,
	'invert__force__direction_0x28' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 3529693283),
)

any_genesys_obj__genesys__gen__vehicle_camera_container = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_genesys__gen__camera_gameplay_bonnet_0x10' / Int32ul,
	'ptr_genesys__gen__camera_gameplay_bumper_0x14' / Int32ul,
	'ptr_genesys__gen__camera_gameplay_external_0x18' / Int32ul,
	'ptr_genesys__gen__camera_rear_view_0x1c' / Int32ul,
	'inst_genesys__gen__camera_rear_view_0x1c' / Pointer(this.ptr_genesys__gen__camera_rear_view_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__camera_rear_view)),
	'inst_genesys__gen__camera_gameplay_external_0x18' / Pointer(this.ptr_genesys__gen__camera_gameplay_external_0x18, LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external)),
	'size' / Computed(lambda this: 36),
	'inst_genesys__gen__camera_gameplay_bonnet_0x10' / Pointer(this.ptr_genesys__gen__camera_gameplay_bonnet_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_bonnet)),
	'inst_genesys__gen__camera_gameplay_bumper_0x14' / Pointer(this.ptr_genesys__gen__camera_gameplay_bumper_0x14, LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_bumper)),
	'mu_version_hash' / Computed(lambda this: 86537152),
)

any_genesys_obj__genesys__gen__race_car_physical_definition__convex_hull_conectivity_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10' / Pointer(this.ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1445450323),
)

any_genesys_obj__genesys__gen__drift_behaviour__drift_trigger = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 1589286504),
)

any_genesys_obj__uint32_t = Struct(
)

any_genesys_obj__genesys__gen__corona__beam = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'unk_enum_0x10' / Int8ub,
	'colour_0xa0' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0xb0' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'material_0xc0' / FixedSized(8, GreedyBytes),
	'end_radius_0xc8' / Float32l,
	'start_radius_0xcc' / Float32l,
	'render_buffer_0xd0' / Int32ul,
	'size' / Computed(lambda this: 216),
	'mu_version_hash' / Computed(lambda this: 3375675327),
)

any_genesys_obj__genesys__gen__rollout = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'weapon_data_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__rollout__weapon_data),
	'body_upgrade_0x24' / Int32ul,
	'ptr_arr_characters_0x28' / Int32ul,
	'chassis_upgrade_0x2c' / Int32ul,
	'colour_0x30' / Int32ul,
	'damage_bar_profile_0x34' / Int32ul,
	'game_changer_id_0x38' / Int32ul,
	'ptr_arr_cgs_core__unique_id_0x3c' / Int32ul,
	'name_0x40' / Int32ul,
	'nitrous_upgrade_0x44' / Int32ul,
	'ptr_arr_number_plate_0x48' / Int32ul,
	'cgs_core__unique_id_0x4c' / Int32ul,
	'revenge_bonus_0x50' / Int32ul,
	'cgs_core__unique_id_0x54' / Int32ul,
	'vehicle_0x58' / Int32ul,
	'dirt_amount_0x5c' / Float32l,
	'dust_amount_0x60' / Float32l,
	'array_count_for_0x28' / Int16ul,
	'array_count_for_0x3c' / Int16ul,
	'array_count_for_0x48' / Int16ul,
	'bool8_t_0x6a' / Int8ub,
	'is_online_rollout_0x6b' / Int8ub,
	'is_player_rollout_0x6c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_cgs_core__unique_id_0x3c' / Pointer(this.ptr_arr_cgs_core__unique_id_0x3c, Array(this.array_count_for_0x3c, Int32ul)),
	'size' / Computed(lambda this: 112),
	'inst_number_plate_0x48' / Pointer(this.ptr_arr_number_plate_0x48, Array(this.array_count_for_0x48, Int32ul)),
	'inst_characters_0x28' / Pointer(this.ptr_arr_characters_0x28, Array(this.array_count_for_0x28, Int32ul)),
	'mu_version_hash' / Computed(lambda this: 1836975283),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__basic_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'linear__solve_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 481138910),
)

any_genesys_obj__genesys__gen__post_fx_keyframe__stereo_3d = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'focus__distance_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1324301512),
)

any_genesys_obj__genesys__gen__nucleus_entitlement_tag = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'tag_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'game_changer_id_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1212586379),
)

any_genesys_obj__genesys__gen__collision_responses__world__in_air_player = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'dynamic_friction_0x10' / Float32l,
	'restitution_0x14' / Float32l,
	'solve_position_angular_scale_0x18' / Float32l,
	'solve_velocity_angular_scale_0x1c' / Float32l,
	'static_friction_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 2328783125),
)

any_genesys_obj__genesys__gen__online_challenge = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'description_0xc' / Int32ul,
	'ptr_arr_cgs_core__unique_id_0x10' / Int32ul,
	'equipment__vehicle_0x14' / Int32ul,
	'cgs_core__unique_id_0x18' / Int32ul,
	'game_changer_id_0x1c' / Int32ul,
	'ptr_arr_game_mode_0x20' / Int32ul,
	'ptr_arr_license_plates_0x24' / Int32ul,
	'manufacturer_0x28' / Int32ul,
	'cgs_core__unique_id_0x2c' / Int32ul,
	'name_0x30' / Int32ul,
	'revenge_bonus_0x34' / Int32ul,
	'att0_0x38' / Int32ul,
	'screen_description_0x3c' / Int32ul,
	'ticket_0x40' / Int32ul,
	'title_0x44' / Int32ul,
	'trigger_0x48' / Int32ul,
	'vehicle_category_0x4c' / Int32ul,
	'cgs_core__unique_id_0x50' / Int32ul,
	'vehicle_nationality_0x54' / Int32ul,
	'cgs_core__unique_id_0x58' / Int32ul,
	'cgs_core__unique_id_0x5c' / Int32ul,
	'ptr_arr_ptr_target_0x60' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'array_count_for_0x20' / Int16ul,
	'array_count_for_0x24' / Int16ul,
	'scope_actions_0x6a' / Int16ul,
	'bool8_t_0x6c' / Int8ub,
	'most_wanted_0x6d' / Int8ub,
	'not_eliminated_0x6e' / Int8ub,
	'not_wrecked_0x6f' / Int8ub,
	'on_rims_0x70' / Int8ub,
	'same_victim_0x71' / Int8ub,
	'bool8_t_0x72' / Int8ub,
	'bool8_t_0x73' / Int8ub,
	'bool8_t_0x74' / Int8ub,
	'unk_enum_0x75' / Int8ub,
	'action__type_0x76' / Int8ub,
	'condition_0x77' / Int8ub,
	'unk_enum_0x78' / Int8ub,
	'time__period_0x79' / Int8ub,
	'array_count_for_0x60' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 124),
	'inst_license_plates_0x24' / Pointer(this.ptr_arr_license_plates_0x24, Array(this.array_count_for_0x24, Int32ul)),
	'inst_target_0x60' / Pointer(this.ptr_arr_ptr_target_0x60, Array(this.array_count_for_0x60, LazyBound(lambda: any_genesys_obj__ptr))),
	'inst_game_mode_0x20' / Pointer(this.ptr_arr_game_mode_0x20, Array(this.array_count_for_0x20, Int32ul)),
	'inst_cgs_core__unique_id_0x10' / Pointer(this.ptr_arr_cgs_core__unique_id_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'mu_version_hash' / Computed(lambda this: 3768680712),
)

any_genesys_obj__genesys__gen__custom_chevron = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_float32_t_0x10' / Int32ul,
	'ptr_arr_float32_t_0x14' / Int32ul,
	'ptr_arr_float32_t_0x18' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'array_count_for_0x14' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'invert_normal_0x22' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'inst_float32_t_0x14' / Pointer(this.ptr_arr_float32_t_0x14, Array(this.array_count_for_0x14, Float32l)),
	'size' / Computed(lambda this: 36),
	'inst_float32_t_0x10' / Pointer(this.ptr_arr_float32_t_0x10, Array(this.array_count_for_0x10, Float32l)),
	'inst_float32_t_0x18' / Pointer(this.ptr_arr_float32_t_0x18, Array(this.array_count_for_0x18, Float32l)),
	'mu_version_hash' / Computed(lambda this: 2896762174),
)

any_genesys_obj__genesys__gen__wave_sequence_item__fade = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'curve_0xc' / Float32l,
	'time_0x10' / Float32l,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1811326154),
)

any_genesys_obj__genesys__gen__collision_responses__world = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'player_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__player),
	'crashed_player_0x70' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__crashed_player),
	'in_air_player_0xb8' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__in_air_player),
	'crashed_traffic_0xdc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__traffic),
	'traffic_0xf4' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__traffic),
	'game_changer_id_0x10c' / Int32ul,
	'size' / Computed(lambda this: 276),
	'mu_version_hash' / Computed(lambda this: 1080225187),
)

any_genesys_obj__genesys__gen__drift_behaviour__side_force = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'size' / Computed(lambda this: 60),
	'mu_version_hash' / Computed(lambda this: 2169095089),
)

any_genesys_obj__genesys__gen__hard_driving_behaviour__steering_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1685430085),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ai__stable_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__damage_params),
	'ai__unstable_0x28' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__damage_params),
	'traffic__stable_0x44' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__damage_params),
	'traffic__unstable_0x60' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__damage_params),
	'ai__crashed_0x7c' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__basic_params),
	'ai__low__speed_0x94' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__basic_params),
	'traffic__low__speed_0xac' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__basic_params),
	'game_changer_id_0xc4' / Int32ul,
	'friction_0xc8' / Float32l,
	'full__high__speed__mph_0xcc' / Float32l,
	'full__low__speed__mph_0xd0' / Float32l,
	'restitution_0xd4' / Float32l,
	'size' / Computed(lambda this: 220),
	'mu_version_hash' / Computed(lambda this: 3800105053),
)

any_genesys_obj__genesys__gen__body_movement_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__body_movement_behaviour__take_off_behaviour_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__body_movement_behaviour__take_off_behaviour),
	'game_changer_id_0x50' / Int32ul,
	'float32_t_0x54' / Float32l,
	'float32_t_0x58' / Float32l,
	'float32_t_0x5c' / Float32l,
	'float32_t_0x60' / Float32l,
	'float32_t_0x64' / Float32l,
	'float32_t_0x68' / Float32l,
	'float32_t_0x6c' / Float32l,
	'float32_t_0x70' / Float32l,
	'float32_t_0x74' / Float32l,
	'float32_t_0x78' / Float32l,
	'float32_t_0x7c' / Float32l,
	'float32_t_0x80' / Float32l,
	'float32_t_0x84' / Float32l,
	'float32_t_0x88' / Float32l,
	'float32_t_0x8c' / Float32l,
	'float32_t_0x90' / Float32l,
	'size' / Computed(lambda this: 152),
	'mu_version_hash' / Computed(lambda this: 106358757),
)

any_genesys_obj__genesys__gen__nitrous_parameters__slipstreaming = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'minimum_speed_0x14' / Float32l,
	'min_slip_streaming_0x18' / Float32l,
	'nitrous_reward_0x1c' / Float32l,
	'is_enabled_0x20' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 1081328468),
)

any_genesys_obj__genesys__gen__mixing_group = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'bus_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 4049496118),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'linear__solve_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3106899705),
)

any_genesys_obj__genesys__gen__collision_responses__global__traffic_vs_dynamic = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'dynamic__angular__solve_0x10' / Float32l,
	'dynamic__linear__solve_0x14' / Float32l,
	'restitution_0x18' / Float32l,
	'traffic__angular__solve_0x1c' / Float32l,
	'traffic__linear__solve_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 3080674119),
)

any_genesys_obj__genesys__gen__nitrous_parameters__restrictions = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'nitrous_ready_message_0xc' / Int32ul,
	'min_nitrous_amount_0x10' / Float32l,
	'min_nitrous_punch_0x14' / Float32l,
	'min_nitrous_speed_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 1377850816),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_crashing_race_car = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'high__speed_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params),
	'low__speed_0x34' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params),
	'game_changer_id_0x5c' / Int32ul,
	'full__high__speed__mph_0x60' / Float32l,
	'full__low__speed__mph_0x64' / Float32l,
	'size' / Computed(lambda this: 108),
	'mu_version_hash' / Computed(lambda this: 722756325),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'crashing__race__car__angular__solve_0x10' / Float32l,
	'crashing__race__car__linear__solve_0x14' / Float32l,
	'friction_0x18' / Float32l,
	'player__angular__solve_0x1c' / Float32l,
	'player__linear__solve_0x20' / Float32l,
	'restitution_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 4035751676),
)

any_genesys_obj__genesys__gen__rollout__weapon_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'weapon_0xc' / Int32ul,
	'ptr_arr_weapon_upgrades_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_weapon_upgrades_0x10' / Pointer(this.ptr_arr_weapon_upgrades_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 2063558262),
)

any_genesys_obj__genesys__gen__wcplay_sound_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'offset_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'mixer_channel_0x30' / FixedSized(8, GreedyBytes),
	'ptr_arr_cgs_resource__handle_0x38' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x3c' / Int32ul,
	'ptr_arr_surface__collisions_0x40' / Int32ul,
	'array_count_for_0x38' / Int16ul,
	'array_count_for_0x3c' / Int16ul,
	'array_count_for_0x40' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_surface__collisions_0x40' / Pointer(this.ptr_arr_surface__collisions_0x40, Array(this.array_count_for_0x40, LazyBound(lambda: any_genesys_obj__genesys__gen__wcplay_sound_behaviour__prop_surface_sound))),
	'inst_cgs_resource__handle_0x38' / Pointer(this.ptr_arr_cgs_resource__handle_0x38, Array(this.array_count_for_0x38, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 76),
	'inst_cgs_resource__handle_0x3c' / Pointer(this.ptr_arr_cgs_resource__handle_0x3c, Array(this.array_count_for_0x3c, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'mu_version_hash' / Computed(lambda this: 4218582003),
)

any_genesys_obj__rw_math_vpu__vector3 = Struct(
	'inline_arr_elements_0x0' / Array(3, Float32l),
	'size' / Computed(lambda this: 8),
	'mu_version_hash' / Computed(lambda this: 2784336371),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__race_car_vs_dynamic = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'race__car__invulnerable_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params),
	'game_changer_id_0x24' / Int32ul,
	'dynamic__angular__solve_0x28' / Float32l,
	'dynamic__linear__solve_0x2c' / Float32l,
	'race__car__angular__solve_0x30' / Float32l,
	'race__car__linear__solve_0x34' / Float32l,
	'restitution_0x38' / Float32l,
	'size' / Computed(lambda this: 64),
	'mu_version_hash' / Computed(lambda this: 2952229338),
)

any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'game_changer_id_0x50' / Int32ul,
	'radius_0x54' / Float32l,
	'size' / Computed(lambda this: 92),
	'mu_version_hash' / Computed(lambda this: 4179189423),
)

any_genesys_obj__genesys__gen__collision_info = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'collision__effects_0xc' / FixedSized(8, GreedyBytes),
	'damage__bars_0x14' / FixedSized(8, GreedyBytes),
	'damage__graphs_0x1c' / FixedSized(8, GreedyBytes),
	'global__collision__responses_0x24' / FixedSized(8, GreedyBytes),
	'race__car__collision__responses_0x2c' / FixedSized(8, GreedyBytes),
	'world__collision__responses_0x34' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x3c' / Int32ul,
	'average__world__strength_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'float32_t_0x4c' / Float32l,
	'float32_t_0x50' / Float32l,
	'bloodstained_ends_0x54' / Float32l,
	'ptr_landing__damage_0x58' / Int32ul,
	'inst_landing__damage_0x58' / Pointer(this.ptr_landing__damage_0x58, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__landing_damage)),
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 1472679887),
)

any_genesys_obj__genesys__gen__camera_gameplay_external__yaw_spring_modification = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'x_ryd_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 814214755),
)

any_genesys_obj__genesys__gen__score_view_model = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_scores_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_scores_0x10' / Pointer(this.ptr_arr_scores_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__score_view_model__score))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1171375143),
)

any_genesys_obj__genesys__gen__vehicle__gameplay__damage_stats = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'uint16_t_0xc' / Int16ul,
	'uint16_t_0xe' / Int16ul,
	'uint16_t_0x10' / Int16ul,
	'uint16_t_0x12' / Int16ul,
	'uint16_t_0x14' / Int16ul,
	'uint16_t_0x16' / Int16ul,
	'strength_0x18' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 372702530),
)

any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params_0x9c' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params),
	'game_changer_id_0x12c' / Int32ul,
	'size' / Computed(lambda this: 308),
	'mu_version_hash' / Computed(lambda this: 682066218),
)

any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__capsule_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'game_changer_id_0x50' / Int32ul,
	'half_length_0x54' / Float32l,
	'radius_0x58' / Float32l,
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 18021398),
)

any_genesys_obj__genesys__gen__vehicle_component = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_resource__handle_0xc' / FixedSized(8, GreedyBytes),
	'category_0x14' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x1c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x24' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x2c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x34' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x3c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x44' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x4c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x54' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x5c' / Int32ul,
	'cgs_core__unique_id_0x60' / Int32ul,
	'manufacturer_0x64' / Int32ul,
	'name_0x68' / Int32ul,
	'cgs_core__unique_id_0x6c' / Int32ul,
	'cgs_core__unique_id_0x70' / Int32ul,
	'cgs_core__unique_id_0x74' / Int32ul,
	'cgs_core__unique_id_0x78' / Int32ul,
	'ptr_arr_cgs_core__unique_id_0x7c' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x80' / Int32ul,
	'ptr_arr_genesys__gen__vehicle_component__wheel_0x84' / Int32ul,
	'array_count_for_0x7c' / Int16ul,
	'array_count_for_0x84' / Int16ul,
	'bool8_t_0x8c' / Int8ub,
	'bool8_t_0x8d' / Int8ub,
	'bool8_t_0x8e' / Int8ub,
	'bool8_t_0x8f' / Int8ub,
	'bool8_t_0x90' / Int8ub,
	'bool8_t_0x91' / Int8ub,
	'bool8_t_0x92' / Int8ub,
	'bool8_t_0x93' / Int8ub,
	'array_count_for_0x80' / Int8ub,
	'uint8_t_0x95' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_genesys__gen__vehicle_component__wheel_0x84' / Pointer(this.ptr_arr_genesys__gen__vehicle_component__wheel_0x84, Array(this.array_count_for_0x84, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_component__wheel))),
	'size' / Computed(lambda this: 152),
	'inst_cgs_core__unique_id_0x7c' / Pointer(this.ptr_arr_cgs_core__unique_id_0x7c, Array(this.array_count_for_0x7c, Int32ul)),
	'inst_cgs_resource__handle_0x80' / Pointer(this.ptr_arr_cgs_resource__handle_0x80, Array(this.array_count_for_0x80, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'mu_version_hash' / Computed(lambda this: 3415849662),
)

any_genesys_obj__genesys__gen__point2dwith_tangents = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__point2d),
	'genesys__gen__point2d_0x18' / LazyBound(lambda: any_genesys_obj__genesys__gen__point2d),
	'genesys__gen__point2d_0x30' / LazyBound(lambda: any_genesys_obj__genesys__gen__point2d),
	'size' / Computed(lambda this: 56),
	'mu_version_hash' / Computed(lambda this: 1692280813),
)

any_genesys_obj__genesys__gen__post_fx_keyframe__depth_of__field = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 1600514099),
)

any_genesys_obj__ptr_table = Struct(
	'entries' / Array(this.amt, LazyBound(lambda: any_genesys_obj__ptr)),
)

any_genesys_obj__genesys__gen__post_fx_keyframe = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'vignette_0x10' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__vignette),
	'bloom_0x80' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__bloom),
	'general_0xd0' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__general),
	'genesys__gen__post_fx_keyframe__depth_of__field_0xf4' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__depth_of__field),
	'stereo_3d_0x110' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__stereo_3d),
	'game_changer_id_0x128' / Int32ul,
	'size' / Computed(lambda this: 304),
	'mu_version_hash' / Computed(lambda this: 1519651292),
)

any_genesys_obj__genesys__gen__submix_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'uint16_t_0x18' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3483480738),
)

any_genesys_obj__genesys__gen__camera_gameplay_external__deceleration__pitch__change = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 802364842),
)

any_genesys_obj__genesys__gen__gameplay_trigger__input = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'trigger_0xc' / Int32ul,
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 2634904179),
)

any_genesys_obj__rw_math_vpu__matrix44affine = Struct(
	'inline_arr_elements_0x0' / Array(4, LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4)),
	'size' / Computed(lambda this: 8),
	'mu_version_hash' / Computed(lambda this: 3062587406),
)

any_genesys_obj__genesys__gen__offline_event__custom_chevrons = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_arr_float32_t_0xc' / Int32ul,
	'ptr_arr_float32_t_0x10' / Int32ul,
	'ptr_arr_float32_t_0x14' / Int32ul,
	'array_count_for_0xc' / Int16ul,
	'array_count_for_0x10' / Int16ul,
	'array_count_for_0x14' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_float32_t_0x14' / Pointer(this.ptr_arr_float32_t_0x14, Array(this.array_count_for_0x14, Float32l)),
	'inst_float32_t_0xc' / Pointer(this.ptr_arr_float32_t_0xc, Array(this.array_count_for_0xc, Float32l)),
	'size' / Computed(lambda this: 32),
	'inst_float32_t_0x10' / Pointer(this.ptr_arr_float32_t_0x10, Array(this.array_count_for_0x10, Float32l)),
	'mu_version_hash' / Computed(lambda this: 542473885),
)

any_genesys_obj__float32_t = Struct(
)

any_genesys_obj__genesys__gen__bus_mixer_channel_sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'ptr_arr_automated__values_0x28' / Int32ul,
	'array_count_for_0x28' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_automated__values_0x28' / Pointer(this.ptr_arr_automated__values_0x28, Array(this.array_count_for_0x28, LazyBound(lambda: any_genesys_obj__genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value))),
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 1198075180),
)

any_genesys_obj__gen_obj = Struct(
	'dynamic_gamedata' / FixedSized(8, GreedyBytes),
	'mu_type_version' / Int32ub,
)

any_genesys_obj__genesys__gen__offline_event = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__event),
	'traffic_overrides_0x4c' / FixedSized(8, GreedyBytes),
	'ptr_arr_additional_assets_0x54' / Int32ul,
	'ptr_arr_aihints_0x58' / Int32ul,
	'allowed_vehicle_list_0x5c' / Int32ul,
	'maps_acceptors_0x60' / Int32ul,
	'ptr_arr_checkpoints_0x64' / Int32ul,
	'cgs_core__unique_id_0x68' / Int32ul,
	'ptr_arr_default_heat_levels_0x6c' / Int32ul,
	'event_intro_0x70' / Int32ul,
	'event_outro_0x74' / Int32ul,
	'feedback_message_group_0x78' / Int32ul,
	'ptr_arr_gameplay_triggers_0x7c' / Int32ul,
	'cgs_core__unique_id_0x80' / Int32ul,
	'name_0x84' / Int32ul,
	'name_formatted_0x88' / Int32ul,
	'next_story_event_0x8c' / Int32ul,
	'cgs_core__unique_id_0x90' / Int32ul,
	'race_balancing_data_0x94' / Int32ul,
	'race_balancing_profile_0x98' / Int32ul,
	'spawn_position_0x9c' / Int32ul,
	'ptr_arr_timeline_0xa0' / Int32ul,
	'type_name_0xa4' / Int32ul,
	'ptr_arr_target_speed_0xa8' / Int32ul,
	'ptr_arr_target_time_0xac' / Int32ul,
	'traffic_density_0xb0' / Float32l,
	'ptr_arr_ptr_genesys__gen__chevron_0xb4' / Int32ul,
	'ptr_arr_ptr_genesys__gen__custom_chevron_0xb8' / Int32ul,
	'ptr_arr_ptr_conditions_0xbc' / Int32ul,
	'ptr_arr_aiplayers_0xc0' / Int32ul,
	'ptr_arr_alternative_routes_0xc4' / Int32ul,
	'ptr_arr_checkpoint_info_0xc8' / Int32ul,
	'target_score_0xcc' / Int32ul,
	'demo_mode_0xd0' / Int16ul,
	'array_count_for_0x54' / Int16ul,
	'array_count_for_0x58' / Int16ul,
	'array_count_for_0xc0' / Int16ul,
	'array_count_for_0xc4' / Int16ul,
	'array_count_for_0xc8' / Int16ul,
	'array_count_for_0x64' / Int16ul,
	'array_count_for_0x6c' / Int16ul,
	'array_count_for_0xb4' / Int16ul,
	'array_count_for_0xa8' / Int16ul,
	'array_count_for_0xac' / Int16ul,
	'array_count_for_0xa0' / Int16ul,
	'cop_spawning_0xe8' / Int8ub,
	'bool8_t_0xe9' / Int8ub,
	'listens_pervade_0xea' / Int8ub,
	'bool8_t_0xeb' / Int8ub,
	'nitrous_allowed_0xec' / Int8ub,
	'no_racing_line_traffic_0xed' / Int8ub,
	'brightening_capsule_0xee' / Int8ub,
	'start_with_engine_on_0xef' / Int8ub,
	'traffic_enabled_0xf0' / Int8ub,
	'bool8_t_0xf1' / Int8ub,
	'weapons_allowed_0xf2' / Int8ub,
	'array_count_for_0xb8' / Int8ub,
	'array_count_for_0xbc' / Int8ub,
	'array_count_for_0x7c' / Int8ub,
	'laps_0xf6' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'inst_aihints_0x58' / Pointer(this.ptr_arr_aihints_0x58, Array(this.array_count_for_0x58, Int32ul)),
	'inst_alternative_routes_0xc4' / Pointer(this.ptr_arr_alternative_routes_0xc4, Array(this.array_count_for_0xc4, LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__alternate_routes))),
	'inst_checkpoint_info_0xc8' / Pointer(this.ptr_arr_checkpoint_info_0xc8, Array(this.array_count_for_0xc8, LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__checkpoint_info))),
	'inst_additional_assets_0x54' / Pointer(this.ptr_arr_additional_assets_0x54, Array(this.array_count_for_0x54, Int32ul)),
	'inst_timeline_0xa0' / Pointer(this.ptr_arr_timeline_0xa0, Array(this.array_count_for_0xa0, Int32ul)),
	'inst_gameplay_triggers_0x7c' / Pointer(this.ptr_arr_gameplay_triggers_0x7c, Array(this.array_count_for_0x7c, Int32ul)),
	'inst_default_heat_levels_0x6c' / Pointer(this.ptr_arr_default_heat_levels_0x6c, Array(this.array_count_for_0x6c, Int32ul)),
	'inst_genesys__gen__custom_chevron_0xb8' / Pointer(this.ptr_arr_ptr_genesys__gen__custom_chevron_0xb8, Array(this.array_count_for_0xb8, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 248),
	'inst_conditions_0xbc' / Pointer(this.ptr_arr_ptr_conditions_0xbc, Array(this.array_count_for_0xbc, LazyBound(lambda: any_genesys_obj__ptr))),
	'inst_aiplayers_0xc0' / Pointer(this.ptr_arr_aiplayers_0xc0, Array(this.array_count_for_0xc0, LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__aiplayer_information))),
	'inst_checkpoints_0x64' / Pointer(this.ptr_arr_checkpoints_0x64, Array(this.array_count_for_0x64, Int32ul)),
	'inst_target_time_0xac' / Pointer(this.ptr_arr_target_time_0xac, Array(this.array_count_for_0xac, Float32l)),
	'inst_target_speed_0xa8' / Pointer(this.ptr_arr_target_speed_0xa8, Array(this.array_count_for_0xa8, Float32l)),
	'inst_genesys__gen__chevron_0xb4' / Pointer(this.ptr_arr_ptr_genesys__gen__chevron_0xb4, Array(this.array_count_for_0xb4, LazyBound(lambda: any_genesys_obj__ptr))),
	'mu_version_hash' / Computed(lambda this: 2419838023),
)

any_genesys_obj__char = Struct(
)

any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'stable_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car__params),
	'unstable_0x28' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car__params),
	'crashed_0x44' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params),
	'game_changer_id_0x5c' / Int32ul,
	'friction_0x60' / Float32l,
	'restitution_0x64' / Float32l,
	'size' / Computed(lambda this: 108),
	'mu_version_hash' / Computed(lambda this: 3359156872),
)

any_genesys_obj__dummy = Struct(
	'd' / Computed(lambda this: u"dummy"),
)

any_genesys_obj__genesys__gen__quit_sequence_timeline_controller = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__jump_timeline_controller),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 1730251222),
)

any_genesys_obj__genesys__gen__donut_ability = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__donut_ability__donut_grip_values_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__donut_ability__donut_grip_values),
	'genesys__gen__donut_ability__donut_scale_0x3c' / LazyBound(lambda: any_genesys_obj__genesys__gen__donut_ability__donut_scale),
	'game_changer_id_0x5c' / Int32ul,
	'size' / Computed(lambda this: 100),
	'mu_version_hash' / Computed(lambda this: 1394693111),
)

any_genesys_obj__genesys__gen__camera_gameplay_external_globals__impact_shake = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'inline_arr_float32_t_0xc' / Array(3, Float32l),
	'inline_arr_float32_t_0x18' / Array(3, Float32l),
	'inline_arr_float32_t_0x24' / Array(3, Float32l),
	'game_changer_id_0x30' / Int32ul,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'float32_t_0x4c' / Float32l,
	'float32_t_0x50' / Float32l,
	'float32_t_0x54' / Float32l,
	'array_count_for_0xc' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'array_count_for_0x24' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 2235640885),
)

any_genesys_obj__genesys__gen__nitrous_parameters_usage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'decrease_nitrous_0x10' / Float32l,
	'time_to_full_nitrous_0x14' / Float32l,
	'enabled_0x18' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 401492861),
)

any_genesys_obj__genesys__gen__sequence = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'binding_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'game_changer_id_0x14' / Int32ul,
	'binding__max_0x18' / Float32l,
	'binding__min_0x1c' / Float32l,
	'ptr_arr_ptr_sequence_items_0x20' / Int32ul,
	'ptr_arr_ptr_timeline_controllers_0x24' / Int32ul,
	'default__progression__controller_0x28' / Int16ul,
	'array_count_for_0x20' / Int8ub,
	'array_count_for_0x24' / Int8ub,
	'inst_sequence_items_0x20' / Pointer(this.ptr_arr_ptr_sequence_items_0x20, Array(this.array_count_for_0x20, LazyBound(lambda: any_genesys_obj__ptr))),
	'inst_timeline_controllers_0x24' / Pointer(this.ptr_arr_ptr_timeline_controllers_0x24, Array(this.array_count_for_0x24, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 3910465619),
)

any_genesys_obj__genesys__gen__vehicles__modifier_upgrade = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 4117431335),
)

any_genesys_obj__genesys__gen__pidcontroller = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 48016591),
)

any_genesys_obj__genesys__gen__traffic_flow = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'flow_type_0xc' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x14' / Int32ul,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'density_0x20' / Float32l,
	'speed_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 2949464142),
)

any_genesys_obj__genesys__gen__post_fxstate = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'inline_arr_colour_cubes_0xc' / Array(2, LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__colour_cube_settings)),
	'bloom__value__modification_0x44' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__value_modifier),
	'colour__cube__value__modification_0x5c' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__value_modifier),
	'dof__value__modification_0x74' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__value_modifier),
	'general__value__modification_0x8c' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__value_modifier),
	'vignette__value__modification_0xa4' / LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__value_modifier),
	'activity_binding_0xbc' / LazyBound(lambda: any_genesys_obj__string_base),
	'keyframe_blend_binding_0xc4' / LazyBound(lambda: any_genesys_obj__string_base),
	'value_binding_0xcc' / LazyBound(lambda: any_genesys_obj__string_base),
	'key_frame1_0xd4' / FixedSized(8, GreedyBytes),
	'key_frame2_0xdc' / FixedSized(8, GreedyBytes),
	'game_changer_id_0xe4' / Int32ul,
	'rate_of_change_0xe8' / Float32l,
	'value_0xec' / Float32l,
	'change_behaviour_0xf0' / Int16ul,
	'array_count_for_0xc' / Int16ul,
	'use__bloom_0xf4' / Int8ub,
	'use__dof_0xf5' / Int8ub,
	'use__general__fx_0xf6' / Int8ub,
	'use__vignette_0xf7' / Int8ub,
	'size' / Computed(lambda this: 252),
	'mu_version_hash' / Computed(lambda this: 615742248),
)

any_genesys_obj__genesys__gen__collision_responses__global__traffic_vs_traffic = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'friction_0x14' / Float32l,
	'linear__solve_0x18' / Float32l,
	'restitution_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 963800229),
)

any_genesys_obj__genesys__gen__online__driving_test_list_group = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'cgs_core__unique_id_0x10' / Int32ul,
	'name_0x14' / Int32ul,
	'ptr_arr_ptr_driving_test_list_0x18' / Int32ul,
	'array_count_for_0x18' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_driving_test_list_0x18' / Pointer(this.ptr_arr_ptr_driving_test_list_0x18, Array(this.array_count_for_0x18, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 4182861931),
)

any_genesys_obj__genesys__gen__nitrous_strength__jump = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3746299654),
)

any_genesys_obj__genesys__gen__tyre_vfx_behaviour__skid_mark_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__tyre_vfx_behaviour__long_lat_params_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__long_lat_params),
	'genesys__gen__tyre_vfx_behaviour__long_lat_params_0x30' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__long_lat_params),
	'game_changer_id_0x54' / Int32ul,
	'size' / Computed(lambda this: 92),
	'mu_version_hash' / Computed(lambda this: 4159289097),
)

any_genesys_obj__genesys__gen__paint_pack_group = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_ptr_paint_packs_0x10' / Int32ul,
	'array_count_for_0x10' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_paint_packs_0x10' / Pointer(this.ptr_arr_ptr_paint_packs_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1913150235),
)

any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cloud_compete_award_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'cgs_core__unique_id_0x14' / Int32ul,
	'cgs_core__unique_id_0x18' / Int32ul,
	'name_0x1c' / Int32ul,
	'ptr_aiplayer_instance_0x20' / Int32ul,
	'ptr_arr_damage_thresholds_0x24' / Int32ul,
	'array_count_for_0x24' / Int16ul,
	'blacklist_number_0x2a' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'inst_aiplayer_instance_0x20' / Pointer(this.ptr_aiplayer_instance_0x20, LazyBound(lambda: any_genesys_obj__genesys__gen__aiplayer_instance)),
	'inst_damage_thresholds_0x24' / Pointer(this.ptr_arr_damage_thresholds_0x24, Array(this.array_count_for_0x24, LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold))),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 2262242598),
)

any_genesys_obj__genesys__gen__heat_level = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'coordination_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination),
	'cgs_core__unique_id_0x6c' / Int32ul,
	'game_changer_id_0x70' / Int32ul,
	'helicopter_0x74' / Int32ul,
	'aim_for_payload_time_0x78' / Float32l,
	'float32_t_0x7c' / Float32l,
	'float32_t_0x80' / Float32l,
	'float32_t_0x84' / Float32l,
	'float32_t_0x88' / Float32l,
	'float32_t_0x8c' / Float32l,
	'cop_hearing_range_for_idle_player_0x90' / Float32l,
	'cop_hearing_range_for_moving_player_0x94' / Float32l,
	'cop_sight_cone_angle_when_alert_0x98' / Float32l,
	'cop_sight_cone_angle_when_idle_0x9c' / Float32l,
	'cop_sight_range_when_alert_0xa0' / Float32l,
	'cop_sight_range_when_chasing_0xa4' / Float32l,
	'cop_sight_range_when_idle_0xa8' / Float32l,
	'float32_t_0xac' / Float32l,
	'float32_t_0xb0' / Float32l,
	'float32_t_0xb4' / Float32l,
	'float32_t_0xb8' / Float32l,
	'float32_t_0xbc' / Float32l,
	'float32_t_0xc0' / Float32l,
	'float32_t_0xc4' / Float32l,
	'float32_t_0xc8' / Float32l,
	'float32_t_0xcc' / Float32l,
	'float32_t_0xd0' / Float32l,
	'float32_t_0xd4' / Float32l,
	'float32_t_0xd8' / Float32l,
	'pursuit_radius_0xdc' / Float32l,
	'search_radius_0xe0' / Float32l,
	'float32_t_0xe4' / Float32l,
	'float32_t_0xe8' / Float32l,
	'unk_enum_0xec' / Int32ul,
	'ptr_arr_formation_ahead_0xf0' / Int32ul,
	'ptr_arr_uint8_t_0xf4' / Int32ul,
	'ptr_arr_formation_behind_0xf8' / Int32ul,
	'ptr_arr_uint8_t_0xfc' / Int32ul,
	'int16_t_0x100' / Int16sl,
	'array_count_for_0xec' / Int16ul,
	'uint16_t_0x104' / Int16ul,
	'array_count_for_0xf0' / Int16ul,
	'array_count_for_0xf4' / Int16ul,
	'array_count_for_0xf8' / Int16ul,
	'array_count_for_0xfc' / Int16ul,
	'threshold_0x10e' / Int16ul,
	'allow_cooldown_0x110' / Int8ub,
	'bool8_t_0x111' / Int8ub,
	'force_cooldown_0x112' / Int8ub,
	'bool8_t_0x113' / Int8ub,
	'helicopter_permanent_0x114' / Int8ub,
	'aim_for_payload_angle_0x115' / Int8ub,
	'display_number_0x116' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'inst_formation_behind_0xf8' / Pointer(this.ptr_arr_formation_behind_0xf8, Array(this.array_count_for_0xf8, Int8ub)),
	'inst_83_1d_10_00_0xec' / Pointer(this.unk_enum_0xec, Array(this.array_count_for_0xec, Int32ul)),
	'size' / Computed(lambda this: 280),
	'inst_formation_ahead_0xf0' / Pointer(this.ptr_arr_formation_ahead_0xf0, Array(this.array_count_for_0xf0, Int8ub)),
	'inst_uint8_t_0xfc' / Pointer(this.ptr_arr_uint8_t_0xfc, Array(this.array_count_for_0xfc, Int8ub)),
	'inst_uint8_t_0xf4' / Pointer(this.ptr_arr_uint8_t_0xf4, Array(this.array_count_for_0xf4, Int8ub)),
	'mu_version_hash' / Computed(lambda this: 1091853463),
)

any_genesys_obj__genesys__gen__store_pack_list = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_store_packs_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_store_packs_0x10' / Pointer(this.ptr_arr_store_packs_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3573113074),
)

any_genesys_obj__genesys__gen__online_event = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__event),
	'inline_arr_float32_t_0x4c' / Array(2, Float32l),
	'arena_0x54' / Int32ul,
	'cgs_core__unique_id_0x58' / Int32ul,
	'cgs_core__unique_id_0x5c' / Int32ul,
	'ptr_arr_cgs_core__unique_id_0x60' / Int32ul,
	'route_0x64' / Int32ul,
	'array_count_for_0x4c' / Int16ul,
	'array_count_for_0x60' / Int16ul,
	'requires_airport_0x6c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_cgs_core__unique_id_0x60' / Pointer(this.ptr_arr_cgs_core__unique_id_0x60, Array(this.array_count_for_0x60, Int32ul)),
	'size' / Computed(lambda this: 112),
	'mu_version_hash' / Computed(lambda this: 393413962),
)

any_genesys_obj__genesys__gen__game_unlock = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'entitlement__required_0xc' / FixedSized(8, GreedyBytes),
	'asset__to__unlock_0x14' / Int32ul,
	'associated_asset_0x18' / Int32ul,
	'challenge__target__required_0x1c' / Int32ul,
	'game_changer_id_0x20' / Int32ul,
	'ptr_arr_required_assets_0x24' / Int32ul,
	'sequence_0x28' / Int32ul,
	'text_0x2c' / Int32ul,
	'bounty__required_0x30' / Int32sl,
	'int32_t_0x34' / Int32sl,
	'int32_t_0x38' / Int32sl,
	'int32_t_0x3c' / Int32sl,
	'progression__type_0x40' / Int16ul,
	'unlock_asset_type_0x42' / Int16ul,
	'array_count_for_0x24' / Int16ul,
	'is_enabled_0x46' / Int8ub,
	'is_silent_0x47' / Int8ub,
	'bool8_t_0x48' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_required_assets_0x24' / Pointer(this.ptr_arr_required_assets_0x24, Array(this.array_count_for_0x24, Int32ul)),
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 3583346207),
)

any_genesys_obj__genesys__gen__drift_behaviour__yaw_torque = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'size' / Computed(lambda this: 68),
	'mu_version_hash' / Computed(lambda this: 3547832794),
)

any_genesys_obj__genesys__gen__camera_rear_view_globals = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 259534121),
)

any_genesys_obj__genesys__gen__post_fx_keyframe__vignette = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'rw_math_vpu__vector2_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector2),
	'scale_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector2),
	'rw_math_vpu__vector4_0x30' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x40' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'game_changer_id_0x50' / Int32ul,
	'float32_t_0x54' / Float32l,
	'fisheye_power_0x58' / Float32l,
	'fisheye_scale_0x5c' / Float32l,
	'fisheye_warp_0x60' / Float32l,
	'sharpness_0x64' / Float32l,
	'size' / Computed(lambda this: 108),
	'mu_version_hash' / Computed(lambda this: 3180273648),
)

any_genesys_obj__genesys__gen__physics__crashing_rules = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x10' / Int32ul,
	'ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x14' / Int32ul,
	'ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x18' / Int32ul,
	'ptr_arr_landing_rules_0x1c' / Int32ul,
	'ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x20' / Int32ul,
	'ptr_arr_player_rules_0x24' / Int32ul,
	'ptr_arr_props_rules_0x28' / Int32ul,
	'ptr_arr_roadblock_rules_0x2c' / Int32ul,
	'ptr_arr_traffic_rules_0x30' / Int32ul,
	'ptr_arr_world_rules_0x34' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'array_count_for_0x14' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'array_count_for_0x1c' / Int16ul,
	'array_count_for_0x20' / Int16ul,
	'array_count_for_0x24' / Int16ul,
	'array_count_for_0x28' / Int16ul,
	'array_count_for_0x2c' / Int16ul,
	'array_count_for_0x30' / Int16ul,
	'array_count_for_0x34' / Int16ul,
	'inst_genesys__gen__physics__crashing_rules__impact_rules_0x18' / Pointer(this.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x18, Array(this.array_count_for_0x18, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'inst_world_rules_0x34' / Pointer(this.ptr_arr_world_rules_0x34, Array(this.array_count_for_0x34, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'inst_genesys__gen__physics__crashing_rules__impact_rules_0x20' / Pointer(this.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x20, Array(this.array_count_for_0x20, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'inst_landing_rules_0x1c' / Pointer(this.ptr_arr_landing_rules_0x1c, Array(this.array_count_for_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'inst_traffic_rules_0x30' / Pointer(this.ptr_arr_traffic_rules_0x30, Array(this.array_count_for_0x30, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'size' / Computed(lambda this: 80),
	'inst_player_rules_0x24' / Pointer(this.ptr_arr_player_rules_0x24, Array(this.array_count_for_0x24, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'inst_genesys__gen__physics__crashing_rules__impact_rules_0x14' / Pointer(this.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x14, Array(this.array_count_for_0x14, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'inst_props_rules_0x28' / Pointer(this.ptr_arr_props_rules_0x28, Array(this.array_count_for_0x28, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'inst_roadblock_rules_0x2c' / Pointer(this.ptr_arr_roadblock_rules_0x2c, Array(this.array_count_for_0x2c, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'inst_genesys__gen__physics__crashing_rules__impact_rules_0x10' / Pointer(this.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules))),
	'mu_version_hash' / Computed(lambda this: 1912243431),
)

any_genesys_obj__genesys__gen__chevron = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'road_section_0x10' / Int32ul,
	'should_block_start_0x14' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 850192155),
)

any_genesys_obj__genesys__gen__vehicle_colour_palette = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x10' / Int32ul,
	'ptr_arr_ptr_genesys__gen__colour_group_0x14' / Int32ul,
	'array_count_for_0x14' / Int8ub,
	'array_count_for_0x10' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_cgs_resource__handle_0x10' / Pointer(this.ptr_arr_cgs_resource__handle_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_genesys__gen__colour_group_0x14' / Pointer(this.ptr_arr_ptr_genesys__gen__colour_group_0x14, Array(this.array_count_for_0x14, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 4062005660),
)

any_genesys_obj__genesys__gen__send_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'voice__routing_0x1c' / FixedSized(8, GreedyBytes),
	'gain_0x24' / Float32l,
	'bus__routing_0x28' / Int32ul,
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 394812715),
)

any_genesys_obj__genesys__gen__camera_gameplay_external_globals = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__camera_gameplay_external_globals__impact_shake_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external_globals__impact_shake),
	'genesys__gen__camera_gameplay_external_globals__lens_properties_0x6c' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external_globals__lens_properties),
	'game_changer_id_0x88' / Int32ul,
	'ptr_genesys__gen__camera_gameplay_shake_effect_0x8c' / Int32ul,
	'inst_genesys__gen__camera_gameplay_shake_effect_0x8c' / Pointer(this.ptr_genesys__gen__camera_gameplay_shake_effect_0x8c, LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect)),
	'size' / Computed(lambda this: 148),
	'mu_version_hash' / Computed(lambda this: 3683195322),
)

any_genesys_obj__genesys__gen__nitrous_parameters__high_speed = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'nitrous_reward_0x14' / Float32l,
	'speed_percentage_0x18' / Float32l,
	'is_enabled_0x1c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 2600311769),
)

any_genesys_obj__genesys__gen__tyre_sound_params__long_spin_braking = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'ya_am_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 3190011655),
)

any_genesys_obj__genesys__gen__gearbox__gear = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3608189499),
)

any_genesys_obj__genesys__gen__handbrake_ability__handbrake_grip_values = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 1408090920),
)

any_genesys_obj__genesys__gen__compound_additional_info = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dynamic_additional_info),
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'size' / Computed(lambda this: 60),
	'mu_version_hash' / Computed(lambda this: 3959582479),
)

any_genesys_obj__genesys__gen__engine_sound2 = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_resource__handle_0xc' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x14' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x1c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x24' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x2c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x34' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x3c' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x40' / Int32ul,
	'ptr_arr_drift_0x44' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x48' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x4c' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x50' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x54' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x58' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x5c' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x60' / Int32ul,
	'ptr_arr_reversing_0x64' / Int32ul,
	'ptr_arr_sequences_0x68' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x6c' / Int32ul,
	'float32_t_0x70' / Float32l,
	'float32_t_0x74' / Float32l,
	'float32_t_0x78' / Float32l,
	'float32_t_0x7c' / Float32l,
	'float32_t_0x80' / Float32l,
	'float32_t_0x84' / Float32l,
	'float32_t_0x88' / Float32l,
	'float32_t_0x8c' / Float32l,
	'float32_t_0x90' / Float32l,
	'float32_t_0x94' / Float32l,
	'float32_t_0x98' / Float32l,
	'float32_t_0x9c' / Float32l,
	'float32_t_0xa0' / Float32l,
	'float32_t_0xa4' / Float32l,
	'float32_t_0xa8' / Float32l,
	'float32_t_0xac' / Float32l,
	'float32_t_0xb0' / Float32l,
	'float32_t_0xb4' / Float32l,
	'float32_t_0xb8' / Float32l,
	'float32_t_0xbc' / Float32l,
	'float32_t_0xc0' / Float32l,
	'float32_t_0xc4' / Float32l,
	'float32_t_0xc8' / Float32l,
	'float32_t_0xcc' / Float32l,
	'float32_t_0xd0' / Float32l,
	'float32_t_0xd4' / Float32l,
	'ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8' / Int32ul,
	'ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc' / Int32ul,
	'ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0' / Int32ul,
	'ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4' / Int32ul,
	'ptr_arr_genesys__gen__engine_sound2__gain_param_wrapper_0xe8' / Int32ul,
	'array_count_for_0xd8' / Int16ul,
	'array_count_for_0xdc' / Int16ul,
	'array_count_for_0xe8' / Int16ul,
	'array_count_for_0xe0' / Int16ul,
	'array_count_for_0xe4' / Int16ul,
	'bool8_t_0xf6' / Int8ub,
	'array_count_for_0x40' / Int8ub,
	'array_count_for_0x44' / Int8ub,
	'array_count_for_0x4c' / Int8ub,
	'array_count_for_0x48' / Int8ub,
	'array_count_for_0x54' / Int8ub,
	'array_count_for_0x50' / Int8ub,
	'array_count_for_0x58' / Int8ub,
	'array_count_for_0x5c' / Int8ub,
	'array_count_for_0x60' / Int8ub,
	'uint8_t_0x100' / Int8ub,
	'array_count_for_0x64' / Int8ub,
	'array_count_for_0x68' / Int8ub,
	'array_count_for_0x6c' / Int8ub,
	'inst_cgs_resource__handle_0x54' / Pointer(this.ptr_arr_cgs_resource__handle_0x54, Array(this.array_count_for_0x54, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_cgs_resource__handle_0x40' / Pointer(this.ptr_arr_cgs_resource__handle_0x40, Array(this.array_count_for_0x40, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_cgs_resource__handle_0x4c' / Pointer(this.ptr_arr_cgs_resource__handle_0x4c, Array(this.array_count_for_0x4c, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4' / Pointer(this.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4, Array(this.array_count_for_0xe4, LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__dsp_param_wrapper))),
	'inst_genesys__gen__engine_sound2__gain_param_wrapper_0xe8' / Pointer(this.ptr_arr_genesys__gen__engine_sound2__gain_param_wrapper_0xe8, Array(this.array_count_for_0xe8, LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__gain_param_wrapper))),
	'inst_reversing_0x64' / Pointer(this.ptr_arr_reversing_0x64, Array(this.array_count_for_0x64, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8' / Pointer(this.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8, Array(this.array_count_for_0xd8, LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__dsp_param_wrapper))),
	'inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0' / Pointer(this.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0, Array(this.array_count_for_0xe0, LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__dsp_param_wrapper))),
	'size' / Computed(lambda this: 264),
	'inst_cgs_resource__handle_0x5c' / Pointer(this.ptr_arr_cgs_resource__handle_0x5c, Array(this.array_count_for_0x5c, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_cgs_resource__handle_0x58' / Pointer(this.ptr_arr_cgs_resource__handle_0x58, Array(this.array_count_for_0x58, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_drift_0x44' / Pointer(this.ptr_arr_drift_0x44, Array(this.array_count_for_0x44, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_cgs_resource__handle_0x60' / Pointer(this.ptr_arr_cgs_resource__handle_0x60, Array(this.array_count_for_0x60, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_sequences_0x68' / Pointer(this.ptr_arr_sequences_0x68, Array(this.array_count_for_0x68, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_cgs_resource__handle_0x6c' / Pointer(this.ptr_arr_cgs_resource__handle_0x6c, Array(this.array_count_for_0x6c, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc' / Pointer(this.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc, Array(this.array_count_for_0xdc, LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__dsp_param_wrapper))),
	'mu_version_hash' / Computed(lambda this: 1844756468),
	'inst_cgs_resource__handle_0x50' / Pointer(this.ptr_arr_cgs_resource__handle_0x50, Array(this.array_count_for_0x50, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_cgs_resource__handle_0x48' / Pointer(this.ptr_arr_cgs_resource__handle_0x48, Array(this.array_count_for_0x48, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
)

any_genesys_obj__genesys__gen__damage_bar_profiles = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ai_0xc' / FixedSized(8, GreedyBytes),
	'impactor_sustaining_0x14' / FixedSized(8, GreedyBytes),
	'player_online_0x1c' / FixedSized(8, GreedyBytes),
	'traffic_0x24' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x2c' / Int32ul,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 3796279727),
)

any_genesys_obj__genesys__gen__vehicles__upgrade_base = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'icon_0x10' / Int32ul,
	'name_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 889829961),
)

any_genesys_obj__genesys__gen__traffic_flow_type = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_flow_type_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_flow_type_0x10' / Pointer(this.ptr_arr_flow_type_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_flow_type__traffic_flow_type))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 467841911),
)

any_genesys_obj__genesys__gen__vehicle_info__axle = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_resource__handle_0xc' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x14' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x18' / Int32ul,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'array_count_for_0x18' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_cgs_resource__handle_0x18' / Pointer(this.ptr_arr_cgs_resource__handle_0x18, Array(this.array_count_for_0x18, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 3440578930),
)

any_genesys_obj__genesys__gen__nucleus_entitlement_tags = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_nucleus_tag_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_nucleus_tag_0x10' / Pointer(this.ptr_arr_nucleus_tag_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3131401224),
)

any_genesys_obj__genesys__gen__collision_effects__battling_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__collision_effects__battling_effect__skid_effects_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect__skid_effects),
	'looser_shrinks_0x30' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect__skid_effects),
	'genesys__gen__collision_effects__battling_effect__skid_effects_0x54' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect__skid_effects),
	'genesys__gen__collision_effects__battling_effect__extra_roll_params_0x78' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect__extra_roll_params),
	'genesys__gen__collision_effects__battling_effect__extra_roll_params_0x90' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect__extra_roll_params),
	'cam__effect__stable_0xa8' / FixedSized(8, GreedyBytes),
	'cam__effect__unstable_0xb0' / FixedSized(8, GreedyBytes),
	'cam__effect__scale_0xb8' / Float32l,
	'stable__camera__threshold_0xbc' / Float32l,
	'unstable__camera__threshold_0xc0' / Float32l,
	'size' / Computed(lambda this: 200),
	'mu_version_hash' / Computed(lambda this: 4191696074),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'player__stable_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params),
	'player__unstable_0x28' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params),
	'traffic__stable_0x44' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params),
	'traffic__unstable_0x60' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params),
	'player__crashed_0x7c' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params),
	'player__invulnerable_0x94' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params),
	'player__low__speed_0xac' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params),
	'traffic__low__speed_0xc4' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params),
	'game_changer_id_0xdc' / Int32ul,
	'float32_t_0xe0' / Float32l,
	'friction_0xe4' / Float32l,
	'full__high__speed__mph_0xe8' / Float32l,
	'full__low__speed__mph_0xec' / Float32l,
	'restitution_0xf0' / Float32l,
	'size' / Computed(lambda this: 248),
	'mu_version_hash' / Computed(lambda this: 1680453612),
)

any_genesys_obj__genesys__gen__vehicles__vehicle_category_info = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'description_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'name_0x14' / Int32ul,
	'cgs_core__unique_id_0x18' / Int32ul,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 760083),
)

any_genesys_obj__genesys__gen__nitrous_parameters__traffic_near_miss = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'minimum_speed_0x14' / Float32l,
	'nitrous_reward_0x18' / Float32l,
	'is_enabled_0x1c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 4256545587),
)

any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'pitch_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation__axis_params),
	'roll_0x34' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation__axis_params),
	'yaw_0x5c' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation__axis_params),
	'game_changer_id_0x84' / Int32ul,
	'amplitude_0x88' / Float32l,
	'size' / Computed(lambda this: 144),
	'mu_version_hash' / Computed(lambda this: 1220037810),
)

any_genesys_obj__genesys__gen__collision_effects__battling_effect__skid_effects = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'high_damage_skid_effect_0xc' / FixedSized(8, GreedyBytes),
	'low_damage_skid_effect_0x14' / FixedSized(8, GreedyBytes),
	'high_damage_for_skid_effect_0x1c' / Float32l,
	'low_damage_for_skid_effect_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 61953676),
)

any_genesys_obj__genesys__gen__gameplay__allowed_vehicle_list = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10' / Pointer(this.ptr_arr_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3992764498),
)

any_genesys_obj__genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'rw_math_vpu__vector3_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector3_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'game_changer_id_0x30' / Int32ul,
	'size' / Computed(lambda this: 56),
	'mu_version_hash' / Computed(lambda this: 1001882986),
)

any_genesys_obj__genesys__gen__sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'enabled_binding_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'game_changer_id_0x14' / Int32ul,
	'end_time_0x18' / Float32l,
	'start_time_0x1c' / Float32l,
	'unk_enum_0x20' / Int32ul,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 1822997286),
)

any_genesys_obj__genesys__gen__wcvfx_behaviour__lights = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'light_definition_0xc' / FixedSized(8, GreedyBytes),
	'locator_group_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3229542978),
)

any_genesys_obj__genesys__gen__voice_group = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'instance_limit_0x10' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 1655947362),
)

any_genesys_obj__genesys__gen__traffic_vehicle_traits = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'acceleration_0x10' / Float32l,
	'scale_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2593852305),
)

any_genesys_obj__genesys__gen__scoring_action = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'predicate_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'game_changer_id_0x14' / Int32ul,
	'gameplay_trigger_0x18' / Int32ul,
	'sequence_0x1c' / Int32ul,
	'title_0x20' / Int32ul,
	'float32_t_0x24' / Float32l,
	'ptr_arr_online_feedback_0x28' / Int32ul,
	'ptr_arr_uint32_t_0x2c' / Int32ul,
	'ptr_arr_score_0x30' / Int32ul,
	'ptr_arr_initiates_raids_0x34' / Int32ul,
	'scope_0x38' / Int16ul,
	'queue_0x3a' / Int16ul,
	'array_count_for_0x2c' / Int16ul,
	'array_count_for_0x28' / Int16ul,
	'array_count_for_0x30' / Int16ul,
	'array_count_for_0x34' / Int16ul,
	'bool8_t_0x44' / Int8ub,
	'feedback_deferrable_0x45' / Int8ub,
	'priority_0x46' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 72),
	'inst_online_feedback_0x28' / Pointer(this.ptr_arr_online_feedback_0x28, Array(this.array_count_for_0x28, LazyBound(lambda: any_genesys_obj__genesys__gen__scoring_action__online_scoring_feedback))),
	'inst_score_0x30' / Pointer(this.ptr_arr_score_0x30, Array(this.array_count_for_0x30, Int32ul)),
	'inst_uint32_t_0x2c' / Pointer(this.ptr_arr_uint32_t_0x2c, Array(this.array_count_for_0x2c, Int32ul)),
	'mu_version_hash' / Computed(lambda this: 2631887699),
	'inst_initiates_raids_0x34' / Pointer(this.ptr_arr_initiates_raids_0x34, Array(this.array_count_for_0x34, Int32ul)),
)

any_genesys_obj__genesys__gen__car_select_data__sequences = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_sequences_0x10' / Int32ul,
	'time_0x14' / Int32sl,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_sequences_0x10' / Pointer(this.ptr_arr_sequences_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1668851487),
)

any_genesys_obj__genesys__gen__sequence_items__post_fx_override_sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'automated__values_count_0x28' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 3664056692),
)

any_genesys_obj__genesys__gen__post_fxstate__colour_cube_settings = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'colour_cube_0xc' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x14' / Int32ul,
	'zero__if__not__set_0x18' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2006186034),
)

any_genesys_obj__genesys__gen__offline_event__aiplayer_information = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'aiplayer_type_0xc' / Int32ul,
	'back_up_colour_0x10' / Int32ul,
	'placement_0x14' / Int32ul,
	'primary_colour_0x18' / Int32ul,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 616120463),
)

any_genesys_obj__genesys__gen__collision_effects = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'battling__collision__effect_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect),
	'traffic__collision__effect_0xd0' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__traffic_effect),
	'world__collision__effect_0x140' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__world_effect),
	'game_changer_id_0x168' / Int32ul,
	'size' / Computed(lambda this: 368),
	'mu_version_hash' / Computed(lambda this: 1763676845),
)

any_genesys_obj__genesys__gen__online_challenge_target = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'award_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'uint32_t_0x14' / Int32ul,
	'xp_0x18' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2078321761),
)

any_genesys_obj__genesys__gen__traffic_vehicle = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'positive_pitch__negative_pitch__yaw__roll_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'trailer_0x20' / FixedSized(8, GreedyBytes),
	'traits_0x28' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x30' / Int32ul,
	'vehicle_component_0x34' / Int32ul,
	'score_0x38' / Int32ul,
	'bool8_t_0x3c' / Int8ub,
	'use_thick_wheel_smoke_0x3d' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 64),
	'mu_version_hash' / Computed(lambda this: 3395112625),
)

any_genesys_obj__genesys__gen__corona__flare = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'unk_enum_0x10' / Int8ub,
	'colour_0xa0' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0xb0' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'material_0xc0' / FixedSized(8, GreedyBytes),
	'position_0xc8' / Float32l,
	'rotation_offset_0xcc' / Float32l,
	'render_buffer_0xd0' / Int32ul,
	'size' / Computed(lambda this: 216),
	'mu_version_hash' / Computed(lambda this: 3357198890),
)

any_genesys_obj__genesys__gen__collision_info_damage_profile = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'minimum__damage_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 2331975734),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__damage_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'damage_0x14' / Float32l,
	'linear__solve_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 2956570466),
)

any_genesys_obj__genesys__gen__heat_level_sound_set = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'nitrous_dump_0xc' / FixedSized(8, GreedyBytes),
	'nitrous_local_0x14' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x1c' / Int32ul,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 456164053),
)

any_genesys_obj__genesys__gen__camera_gameplay_external__acceleration_movement = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'size' / Computed(lambda this: 64),
	'mu_version_hash' / Computed(lambda this: 2041922261),
)

any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_movement = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake),
	'game_changer_id_0x30' / Int32ul,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 1963215010),
)

any_genesys_obj__genesys__gen__collision_info__world_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cam__effect_0xc' / FixedSized(8, GreedyBytes),
	'cam__effect__scale_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2501750206),
)

any_genesys_obj__genesys__gen__challenge_action__accumulate_takedowns = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 3616117713),
)

any_genesys_obj__genesys__gen__tyre_vfx_behaviour__smoke_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__tyre_vfx_behaviour__long_lat_params_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__long_lat_params),
	'genesys__gen__tyre_vfx_behaviour__long_lat_params_0x30' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__long_lat_params),
	'game_changer_id_0x54' / Int32ul,
	'size' / Computed(lambda this: 92),
	'mu_version_hash' / Computed(lambda this: 3643052795),
)

any_genesys_obj__genesys__gen__collision_responses__global__dynamic_vs_dynamic = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'linear__solve_0x14' / Float32l,
	'restitution_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3907892408),
)

any_genesys_obj__genesys__gen__post_fx_keyframe__bloom = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'colour_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'game_changer_id_0x20' / Int32ul,
	'dark_bloom_weight_0x24' / Float32l,
	'dark_bloom_white_point_0x28' / Float32l,
	'large_weight_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'medium_weight_0x34' / Float32l,
	'saturation_0x38' / Float32l,
	'small_weight_0x3c' / Float32l,
	'threshold_0x40' / Float32l,
	'threshold_large_0x44' / Float32l,
	'threshold_medium_0x48' / Float32l,
	'size' / Computed(lambda this: 80),
	'mu_version_hash' / Computed(lambda this: 3592057837),
)

any_genesys_obj__genesys__gen__wcplay_sound_behaviour__prop_surface_sound = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'surface_0x10' / Int32ul,
	'ptr_arr_rolling__waves_0x14' / Int32ul,
	'ptr_arr_scraping__waves_0x18' / Int32ul,
	'ptr_arr_waves_0x1c' / Int32ul,
	'array_count_for_0x14' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'array_count_for_0x1c' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_waves_0x1c' / Pointer(this.ptr_arr_waves_0x1c, Array(this.array_count_for_0x1c, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_rolling__waves_0x14' / Pointer(this.ptr_arr_rolling__waves_0x14, Array(this.array_count_for_0x14, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 40),
	'inst_scraping__waves_0x18' / Pointer(this.ptr_arr_scraping__waves_0x18, Array(this.array_count_for_0x18, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'mu_version_hash' / Computed(lambda this: 3115085927),
)

any_genesys_obj__genesys__gen__gameplay__drift_marker = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'cgs_core__unique_id_0x10' / Int32ul,
	'cgs_core__unique_id_0x14' / Int32ul,
	'safety_trigger_0x18' / Int32ul,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 835486276),
)

any_genesys_obj__genesys__gen__vehicle_info = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'rw_math_vpu__matrix44affine_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'rw_math_vpu__vector3_0x50' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector3_0x60' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector3_0x70' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'game_changer_id_0x80' / Int32ul,
	'float32_t_0x84' / Float32l,
	'float32_t_0x88' / Float32l,
	'float32_t_0x8c' / Float32l,
	'float32_t_0x90' / Float32l,
	'float32_t_0x94' / Float32l,
	'ptr_arr_genesys__gen__vehicle_info__axle_0x98' / Int32ul,
	'ptr_arr_genesys__gen__vehicle_info__extra_axle_0x9c' / Int32ul,
	'array_count_for_0x98' / Int16ul,
	'array_count_for_0x9c' / Int16ul,
	'bool8_t_0xa4' / Int8ub,
	'bool8_t_0xa5' / Int8ub,
	'bool8_t_0xa6' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'inst_genesys__gen__vehicle_info__axle_0x98' / Pointer(this.ptr_arr_genesys__gen__vehicle_info__axle_0x98, Array(this.array_count_for_0x98, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_info__axle))),
	'inst_genesys__gen__vehicle_info__extra_axle_0x9c' / Pointer(this.ptr_arr_genesys__gen__vehicle_info__extra_axle_0x9c, Array(this.array_count_for_0x9c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_info__extra_axle))),
	'size' / Computed(lambda this: 168),
	'mu_version_hash' / Computed(lambda this: 3954992488),
)

any_genesys_obj__genesys__gen__camera_gameplay_shake_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'translation_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation),
	'rotation_0xa4' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation),
	'game_changer_id_0x130' / Int32ul,
	'size' / Computed(lambda this: 312),
	'mu_version_hash' / Computed(lambda this: 3580468080),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'linear__solve_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2144572099),
)

any_genesys_obj__genesys__gen__steering_wheel_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'cgs_resource__handle_0x1c' / FixedSized(8, GreedyBytes),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 3124672599),
)

any_genesys_obj__genesys__gen__nitrous_parameters__taking_shortcut = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'minimum_speed_0x14' / Float32l,
	'nitrous_reward_0x18' / Float32l,
	'is_enabled_0x1c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 1687823060),
)

any_genesys_obj__genesys__gen__vehicle_damage_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'cgs_resource__handle_0x1c' / FixedSized(8, GreedyBytes),
	'ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart_0x24' / Int32ul,
	'ptr_arr_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28' / Int32ul,
	'ptr_arr_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c' / Int32ul,
	'array_count_for_0x24' / Int16ul,
	'array_count_for_0x28' / Int16ul,
	'array_count_for_0x2c' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c' / Pointer(this.ptr_arr_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c, Array(this.array_count_for_0x2c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__spot_effect))),
	'inst_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28' / Pointer(this.ptr_arr_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28, Array(this.array_count_for_0x28, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__damage_sequence))),
	'size' / Computed(lambda this: 56),
	'inst_genesys__gen__vehicle_damage_behaviour__bodypart_0x24' / Pointer(this.ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart_0x24, Array(this.array_count_for_0x24, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__bodypart))),
	'mu_version_hash' / Computed(lambda this: 1880813572),
)

any_genesys_obj__genesys__gen__gameplay__milestone = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__unique_id_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'name_0x14' / Int32ul,
	'progress_0x18' / Int32ul,
	'ptr_arr_entries_0x1c' / Int32ul,
	'stat_0x20' / Int16ul,
	'array_count_for_0x1c' / Int16ul,
	'inst_entries_0x1c' / Pointer(this.ptr_arr_entries_0x1c, Array(this.array_count_for_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__milestone__entry))),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 1320933699),
)

any_genesys_obj__genesys__gen__lfo_sequence_item__lfo_double_value = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_value_0xc' / Int32ul,
	'automated__property_0x10' / Int32ul,
	'inst_value_0xc' / Pointer(this.ptr_value_0xc, LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 4097165157),
)

any_genesys_obj__string_base = Struct(
	'ofs_arr_buffer_0x0' / Int32ul,
	'array_count_for_0x0' / Int32ul,
	'inst_buffer_0x0' / Pointer(this.ofs_arr_buffer_0x0, FixedSized(this.array_count_for_0x0, GreedyString(encoding='ascii'))),
	'size' / Computed(lambda this: 12),
	'mu_version_hash' / Computed(lambda this: 2516314814),
)

any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation__axis_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'amplitude_0x10' / Float32l,
	'damping_0x14' / Float32l,
	'maximum__angle_0x18' / Float32l,
	'minimum__angle_0x1c' / Float32l,
	'spring__coefficient_0x20' / Float32l,
	'invert__force__direction_0x24' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 3652314633),
)

any_genesys_obj__genesys__gen__vehicle_damage_behaviour__bodypart = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'rw_math_vpu__vector2_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector2),
	'rw_math_vpu__vector2_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector2),
	'rw_math_vpu__vector2_0x30' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector2),
	'rw_math_vpu__vector3_0x40' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector3_0x50' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector3_0x60' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector3_0x70' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector4_0x80' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'cgs_core__string_base_0x90' / LazyBound(lambda: any_genesys_obj__string_base),
	'cgs_resource__handle_0x98' / FixedSized(8, GreedyBytes),
	'game_changer_id_0xa0' / Int32ul,
	'locator_group_0xa4' / Int32ul,
	'mass_0xa8' / Float32l,
	'ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac' / Int32ul,
	'unk_enum_0xb0' / Int16ul,
	'array_count_for_0xac' / Int16ul,
	'bool8_t_0xb4' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac' / Pointer(this.ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac, Array(this.array_count_for_0xac, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold))),
	'size' / Computed(lambda this: 184),
	'mu_version_hash' / Computed(lambda this: 509958626),
)

any_genesys_obj__genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'friction_0x14' / Float32l,
	'linear__solve_0x18' / Float32l,
	'restitution_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 1186319577),
)

any_genesys_obj__genesys__gen__camera_gameplay_external = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__camera_gameplay_external__speed_based_movement_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_movement),
	'genesys__gen__camera_gameplay_external__acceleration_movement_0x54' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__acceleration_movement),
	'genesys__gen__camera_gameplay_external__camera__roll_0x90' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__camera__roll),
	'genesys__gen__camera_gameplay_external__yaw_spring_modification_0xbc' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__yaw_spring_modification),
	'genesys__gen__camera_gameplay_external__deceleration__pitch__change_0xe8' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__deceleration__pitch__change),
	'genesys__gen__camera_gameplay_external__speed_based_height_change_0x10c' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_height_change),
	'inline_arr_float32_t_0x124' / Array(3, Float32l),
	'inline_arr_float32_t_0x130' / Array(3, Float32l),
	'inline_arr_float32_t_0x13c' / Array(3, Float32l),
	'inline_arr_float32_t_0x148' / Array(3, Float32l),
	'cgs_resource__handle_0x154' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x15c' / Int32ul,
	'float32_t_0x160' / Float32l,
	'float32_t_0x164' / Float32l,
	'float32_t_0x168' / Float32l,
	'float32_t_0x16c' / Float32l,
	'float32_t_0x170' / Float32l,
	'ptr_genesys__gen__camera_gameplay_external_globals_0x174' / Int32ul,
	'ptr_genesys__gen__camera_gameplay_gradient_adjustments_0x178' / Int32ul,
	'array_count_for_0x124' / Int16ul,
	'array_count_for_0x130' / Int16ul,
	'array_count_for_0x13c' / Int16ul,
	'array_count_for_0x148' / Int16ul,
	'uint8_t_0x184' / Int8ub,
	'uint8_t_0x185' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_genesys__gen__camera_gameplay_external_globals_0x174' / Pointer(this.ptr_genesys__gen__camera_gameplay_external_globals_0x174, LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external_globals)),
	'inst_genesys__gen__camera_gameplay_gradient_adjustments_0x178' / Pointer(this.ptr_genesys__gen__camera_gameplay_gradient_adjustments_0x178, LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_gradient_adjustments)),
	'size' / Computed(lambda this: 392),
	'mu_version_hash' / Computed(lambda this: 3148721321),
)

any_genesys_obj__genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_modulating_value_0xc' / Int32ul,
	'bus_mixer_channel_property_0x10' / Int32ul,
	'inst_modulating_value_0xc' / Pointer(this.ptr_modulating_value_0xc, LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3626200052),
)

any_genesys_obj__genesys__gen__tyres__surface_effects = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_genesys__gen__vehicle_surface_profile_0x10' / Int32ul,
	'inst_genesys__gen__vehicle_surface_profile_0x10' / Pointer(this.ptr_genesys__gen__vehicle_surface_profile_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_surface_profile)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1530679421),
)

any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'value_0xc' / Float32l,
	'stat_0x10' / Int32ul,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3434016526),
)

any_genesys_obj__genesys__gen__physics__landing_damage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'pitch_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__physics__landing_damage__pitch),
	'roll_0x30' / LazyBound(lambda: any_genesys_obj__genesys__gen__physics__landing_damage__roll),
	'game_changer_id_0x50' / Int32ul,
	'float32_t_0x54' / Float32l,
	'size' / Computed(lambda this: 92),
	'mu_version_hash' / Computed(lambda this: 2607248643),
)

any_genesys_obj__genesys__gen__vehicle_component__wheel = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__unique_id_0xc' / Int32ul,
	'type_0x10' / Int32ul,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 2583194568),
)

any_genesys_obj__genesys__gen__vehicle_vfx_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'ptr_arr_coronas_0x1c' / Int32ul,
	'ptr_arr_lights_0x20' / Int32ul,
	'ptr_arr_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24' / Int32ul,
	'array_count_for_0x1c' / Int16ul,
	'array_count_for_0x20' / Int16ul,
	'array_count_for_0x24' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_lights_0x20' / Pointer(this.ptr_arr_lights_0x20, Array(this.array_count_for_0x20, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__light))),
	'size' / Computed(lambda this: 48),
	'inst_coronas_0x1c' / Pointer(this.ptr_arr_coronas_0x1c, Array(this.array_count_for_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__corona))),
	'inst_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24' / Pointer(this.ptr_arr_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24, Array(this.array_count_for_0x24, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__spot_effect))),
	'mu_version_hash' / Computed(lambda this: 3302002317),
)

any_genesys_obj__genesys__gen__nucleus_grant_mappings_list = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_items_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_items_0x10' / Pointer(this.ptr_arr_items_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__nucleus_grant_mappings_list__mapping))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 975568910),
)

any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'amplitude_0x10' / Float32l,
	'frequency_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'power_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 3791727622),
)

any_genesys_obj__genesys__gen__roadblock_instance = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'placement_0x10' / Int32ul,
	'type_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2089690370),
)

any_genesys_obj__genesys__gen__paint_pack = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'colour_0xc' / Int32ul,
	'cgs_core__unique_id_0x10' / Int32ul,
	'game_changer_id_0x14' / Int32ul,
	'image_0x18' / Int32ul,
	'livery_0x1c' / Int32ul,
	'name_0x20' / Int32ul,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 832200604),
)

any_genesys_obj__genesys__gen__wcvfx_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'impact_effect_0x1c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x24' / FixedSized(8, GreedyBytes),
	'flash_frequency_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'nonprocedurally_slocum_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'ptr_arr_coronas_0x40' / Int32ul,
	'ptr_arr_lights_0x44' / Int32ul,
	'ptr_arr_genesys__gen__wcvfx_behaviour__spot_effects_0x48' / Int32ul,
	'int32_t_0x4c' / Int32sl,
	'int32_t_0x50' / Int32sl,
	'array_count_for_0x40' / Int16ul,
	'array_count_for_0x44' / Int16ul,
	'array_count_for_0x48' / Int16ul,
	'bool8_t_0x5a' / Int8ub,
	'bool8_t_0x5b' / Int8ub,
	'bool8_t_0x5c' / Int8ub,
	'bool8_t_0x5d' / Int8ub,
	'bool8_t_0x5e' / Int8ub,
	'bool8_t_0x5f' / Int8ub,
	'bool8_t_0x60' / Int8ub,
	'bool8_t_0x61' / Int8ub,
	'bool8_t_0x62' / Int8ub,
	'bool8_t_0x63' / Int8ub,
	'bool8_t_0x64' / Int8ub,
	'bool8_t_0x65' / Int8ub,
	'bool8_t_0x66' / Int8ub,
	'bool8_t_0x67' / Int8ub,
	'bool8_t_0x68' / Int8ub,
	'bool8_t_0x69' / Int8ub,
	'bool8_t_0x6a' / Int8ub,
	'bool8_t_0x6b' / Int8ub,
	'inst_lights_0x44' / Pointer(this.ptr_arr_lights_0x44, Array(this.array_count_for_0x44, LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour__lights))),
	'inst_genesys__gen__wcvfx_behaviour__spot_effects_0x48' / Pointer(this.ptr_arr_genesys__gen__wcvfx_behaviour__spot_effects_0x48, Array(this.array_count_for_0x48, LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour__spot_effects))),
	'size' / Computed(lambda this: 112),
	'inst_coronas_0x40' / Pointer(this.ptr_arr_coronas_0x40, Array(this.array_count_for_0x40, LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour__coronas))),
	'mu_version_hash' / Computed(lambda this: 3464877079),
)

any_genesys_obj__genesys__gen__peaking_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'gain_0x18' / Float32l,
	'q_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 3263786457),
)

any_genesys_obj__genesys__gen__collision_info__battling_damage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 3587969770),
)

any_genesys_obj__genesys__gen__body_movement_behaviour__angle_control = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'damping_0xc' / Float32l,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 3023685899),
)

any_genesys_obj__rw_math_vpu__vector2 = Struct(
	'inline_arr_elements_0x0' / Array(2, Float32l),
	'size' / Computed(lambda this: 8),
	'mu_version_hash' / Computed(lambda this: 786918963),
)

any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'linear__solve_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1231510099),
)

any_genesys_obj__genesys__gen__aiplayer_instance = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'back_up_colour_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'primary_colour_0x14' / Int32ul,
	'type_0x18' / Int32ul,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3691324629),
)

any_genesys_obj__genesys__gen__vehicle_damage_behaviour__spot_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_resource__handle_0xc' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x14' / Int32ul,
	'locator_group_0x18' / Int32ul,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 4117767557),
)

any_genesys_obj__genesys__gen__physical_definition = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'local_aabbcenter_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'local_aabbhalf_diagonal_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'additional_info_0x30' / FixedSized(8, GreedyBytes),
	'ptr_arr_rigid_bodies_names_0x38' / Int32ul,
	'game_changer_id_0x3c' / Int32ul,
	'ptr_arr_rigid_bodies_0x40' / Int32ul,
	'game_changer_id_0x44' / Int32sl,
	'main_rigid_body_index_0x48' / Int32sl,
	'array_count_for_0x40' / Int16ul,
	'array_count_for_0x38' / Int16ul,
	'bool8_t_0x50' / Int8ub,
	'bool8_t_0x51' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_rigid_bodies_names_0x38' / Pointer(this.ptr_arr_rigid_bodies_names_0x38, Array(this.array_count_for_0x38, LazyBound(lambda: any_genesys_obj__string_base))),
	'inst_rigid_bodies_0x40' / Pointer(this.ptr_arr_rigid_bodies_0x40, Array(this.array_count_for_0x40, LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body))),
	'size' / Computed(lambda this: 84),
	'mu_version_hash' / Computed(lambda this: 2519567673),
)

any_genesys_obj__genesys__gen__event__checkpoint_info = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'sequence_0xc' / Int32ul,
	'show_split_time_0x10' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 2571445580),
)

any_genesys_obj__genesys__gen__high_shelf_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'gain_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 4149479710),
)

any_genesys_obj__genesys__gen__damage_bar_profiles__profile__segment_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'damage_to_leave_segment_0x10' / Float32l,
	'segment_0x14' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 542430507),
)

any_genesys_obj__genesys__gen__drift_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__drift_behaviour__other_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__other),
	'genesys__gen__drift_behaviour__yaw_torque_0x54' / LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__yaw_torque),
	'genesys__gen__drift_behaviour__side_force_0x94' / LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__side_force),
	'genesys__gen__drift_behaviour__drift_scale_0xcc' / LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__drift_scale),
	'genesys__gen__drift_behaviour__drift_exit_0x100' / LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__drift_exit),
	'genesys__gen__drift_behaviour__drift_trigger_0x128' / LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__drift_trigger),
	'game_changer_id_0x14c' / Int32ul,
	'size' / Computed(lambda this: 340),
	'mu_version_hash' / Computed(lambda this: 4274679117),
)

any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 3032331154),
)

any_genesys_obj__genesys__gen__challenge_action__accumulate_distance = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 3815813836),
)

any_genesys_obj__genesys__gen__ginsu_sequence_item__fade = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'curve_0xc' / Float32l,
	'time_0x10' / Float32l,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3237867664),
)

any_genesys_obj__genesys__gen__sequence_timeline_controller = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'enabled_binding_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'game_changer_id_0x14' / Int32ul,
	'trigger_type_0x18' / Int16ul,
	'test_continuously_0x1a' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 4067794056),
)

any_genesys_obj__genesys__gen__thankyou_mapping = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'nucleus_entitlement_0xc' / FixedSized(8, GreedyBytes),
	'thankyou_item_0x14' / FixedSized(8, GreedyBytes),
	'entitlement_0x1c' / Int32ul,
	'game_changer_id_0x20' / Int32ul,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 451352474),
)

any_genesys_obj__genesys__gen__hard_driving_behaviour__gas_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'size' / Computed(lambda this: 68),
	'mu_version_hash' / Computed(lambda this: 1021288769),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ai__angular__solve_0x10' / Float32l,
	'ai__linear__solve_0x14' / Float32l,
	'crashing__race__car__angular__solve_0x18' / Float32l,
	'crashing__race__car__linear__solve_0x1c' / Float32l,
	'friction_0x20' / Float32l,
	'restitution_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 2957925672),
)

any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x3c' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params),
	'genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x64' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params),
	'game_changer_id_0x8c' / Int32ul,
	'size' / Computed(lambda this: 148),
	'mu_version_hash' / Computed(lambda this: 1711822367),
)

any_genesys_obj__genesys__gen__event_arena_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'loading__point__location_0x10' / Int32ul,
	'ptr_arr_lockdown_points_0x14' / Int32ul,
	'ptr_arr_point_to_point_checkpoints_0x18' / Int32ul,
	'ptr_arr_repair_points_0x1c' / Int32ul,
	'ptr_arr_spawn__locations_0x20' / Int32ul,
	'vista_camera_location_0x24' / Int32ul,
	'ptr_arr_ptr_chevrons_0x28' / Int32ul,
	'ptr_arr_ptr_custom_chevron_list_0x2c' / Int32ul,
	'ptr_arr_team_spawn_locations_0x30' / Int32ul,
	'array_count_for_0x28' / Int16ul,
	'array_count_for_0x14' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'array_count_for_0x1c' / Int16ul,
	'array_count_for_0x20' / Int16ul,
	'array_count_for_0x30' / Int16ul,
	'array_count_for_0x2c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_point_to_point_checkpoints_0x18' / Pointer(this.ptr_arr_point_to_point_checkpoints_0x18, Array(this.array_count_for_0x18, Int32ul)),
	'inst_repair_points_0x1c' / Pointer(this.ptr_arr_repair_points_0x1c, Array(this.array_count_for_0x1c, Int32ul)),
	'inst_chevrons_0x28' / Pointer(this.ptr_arr_ptr_chevrons_0x28, Array(this.array_count_for_0x28, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 68),
	'inst_lockdown_points_0x14' / Pointer(this.ptr_arr_lockdown_points_0x14, Array(this.array_count_for_0x14, Int32ul)),
	'inst_team_spawn_locations_0x30' / Pointer(this.ptr_arr_team_spawn_locations_0x30, Array(this.array_count_for_0x30, LazyBound(lambda: any_genesys_obj__genesys__gen__event_arena_data__spawn_point_collection))),
	'inst_custom_chevron_list_0x2c' / Pointer(this.ptr_arr_ptr_custom_chevron_list_0x2c, Array(this.array_count_for_0x2c, LazyBound(lambda: any_genesys_obj__ptr))),
	'mu_version_hash' / Computed(lambda this: 2270583296),
	'inst_spawn__locations_0x20' / Pointer(this.ptr_arr_spawn__locations_0x20, Array(this.array_count_for_0x20, Int32ul)),
)

any_genesys_obj__genesys__gen__challenge_action__car_state = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'float32_t_0x4c' / Float32l,
	'float32_t_0x50' / Float32l,
	'max_speed_0x54' / Int16ul,
	'min_speed_0x56' / Int16ul,
	'bool8_t_0x58' / Int8ub,
	'bool8_t_0x59' / Int8ub,
	'bool8_t_0x5a' / Int8ub,
	'donutting_0x5b' / Int8ub,
	'drifting_0x5c' / Int8ub,
	'in_air_0x5d' / Int8ub,
	'nitrous_0x5e' / Int8ub,
	'bool8_t_0x5f' / Int8ub,
	'reversing_0x60' / Int8ub,
	'slipstreaming_0x61' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 100),
	'mu_version_hash' / Computed(lambda this: 174008559),
)

any_genesys_obj__genesys__gen__wave_sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'pitch_0x5c' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value),
	'fade__in_0x94' / LazyBound(lambda: any_genesys_obj__genesys__gen__wave_sequence_item__fade),
	'fade__out_0xa8' / LazyBound(lambda: any_genesys_obj__genesys__gen__wave_sequence_item__fade),
	'snapshot__property_0xbc' / LazyBound(lambda: any_genesys_obj__string_base),
	'transform__override__binding_0xc4' / LazyBound(lambda: any_genesys_obj__string_base),
	'mixer__channel_0xcc' / FixedSized(8, GreedyBytes),
	'ptr_arr_waves_0xd4' / Int32ul,
	'ptr_arr_trigger__probability_0xd8' / Int32ul,
	're_trigger_0xdc' / Int16ul,
	'type_0xde' / Int16ul,
	'auto__pitch_0xe0' / Int8ub,
	'array_count_for_0xd8' / Int8ub,
	'array_count_for_0xd4' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'inst_waves_0xd4' / Pointer(this.ptr_arr_waves_0xd4, Array(this.array_count_for_0xd4, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_trigger__probability_0xd8' / Pointer(this.ptr_arr_trigger__probability_0xd8, Array(this.array_count_for_0xd8, LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value))),
	'size' / Computed(lambda this: 228),
	'mu_version_hash' / Computed(lambda this: 1722819130),
)

any_genesys_obj__genesys__gen__tyre_sound_params__lateral = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 564124160),
)

any_genesys_obj__genesys__gen__camera_gameplay_bonnet = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'inline_arr_float32_t_0xc' / Array(3, Float32l),
	'inline_arr_float32_t_0x18' / Array(3, Float32l),
	'inline_arr_float32_t_0x24' / Array(3, Float32l),
	'game_changer_id_0x30' / Int32ul,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'float32_t_0x4c' / Float32l,
	'float32_t_0x50' / Float32l,
	'float32_t_0x54' / Float32l,
	'float32_t_0x58' / Float32l,
	'float32_t_0x5c' / Float32l,
	'float32_t_0x60' / Float32l,
	'float32_t_0x64' / Float32l,
	'float32_t_0x68' / Float32l,
	'float32_t_0x6c' / Float32l,
	'int32_t_0x70' / Int32sl,
	'int32_t_0x74' / Int32sl,
	'array_count_for_0xc' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'array_count_for_0x24' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 128),
	'mu_version_hash' / Computed(lambda this: 3342396752),
)

any_genesys_obj__genesys__gen__tyre = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__tyre__lateral__slip__factors_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__lateral__slip__factors),
	'genesys__gen__tyre__lateral__slip__factors_0x30' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__lateral__slip__factors),
	'genesys__gen__tyre__lateral__grip__curve_0x54' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__lateral__grip__curve),
	'genesys__gen__tyre__lateral__grip__curve_0x74' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__lateral__grip__curve),
	'genesys__gen__tyre__lateral__grip__curve_0x94' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__lateral__grip__curve),
	'genesys__gen__tyre__long__grip__curve_0xb4' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__grip__curve),
	'genesys__gen__tyre__long__grip__curve_0xd4' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__grip__curve),
	'genesys__gen__tyre__long__grip__curve_0xf4' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__grip__curve),
	'genesys__gen__tyre__long__grip__curve_0x114' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__grip__curve),
	'genesys__gen__tyre__long__slip__factors_0x134' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__slip__factors),
	'genesys__gen__tyre__long__slip__factors_0x154' / LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__slip__factors),
	'game_changer_id_0x174' / Int32ul,
	'float32_t_0x178' / Float32l,
	'float32_t_0x17c' / Float32l,
	'float32_t_0x180' / Float32l,
	'float32_t_0x184' / Float32l,
	'float32_t_0x188' / Float32l,
	'float32_t_0x18c' / Float32l,
	'float32_t_0x190' / Float32l,
	'float32_t_0x194' / Float32l,
	'float32_t_0x198' / Float32l,
	'float32_t_0x19c' / Float32l,
	'size' / Computed(lambda this: 420),
	'mu_version_hash' / Computed(lambda this: 21856074),
)

any_genesys_obj__genesys__gen__race_balancing_profile = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'max_speed_0x10' / Float32l,
	'min_speed_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2776745689),
)

any_genesys_obj__genesys__gen__colour_group = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'primary_colour_0xc' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x14' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x1c' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x24' / Int32ul,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 1259832621),
)

any_genesys_obj__genesys__gen__distortion_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'model_0x18' / Int32ul,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3181724531),
)

any_genesys_obj__genesys__gen__vehicle_surface_profile__surface_link = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_cgs_core__unique_id_0x10' / Int32ul,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_cgs_core__unique_id_0x10' / Pointer(this.ptr_arr_cgs_core__unique_id_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'size' / Computed(lambda this: 60),
	'mu_version_hash' / Computed(lambda this: 283467013),
)

any_genesys_obj__genesys__gen__nitrous_parameters__speedbreaker_usage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters_usage),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 2522613547),
)

any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__spot_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_resource__handle_0xc' / FixedSized(8, GreedyBytes),
	'locator_group_0x14' / Int32ul,
	'unk_enum_0x18' / Int16ul,
	'time_of_day_0x1a' / Int16ul,
	'bool8_t_0x1c' / Int8ub,
	'bool8_t_0x1d' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 2169939698),
)

any_genesys_obj__genesys__gen__physical_definition__rigid_body__sphere_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'game_changer_id_0x50' / Int32ul,
	'radius_0x54' / Float32l,
	'size' / Computed(lambda this: 92),
	'mu_version_hash' / Computed(lambda this: 4179189423),
)

any_genesys_obj__genesys__gen__nitrous_parameters__nitrous_usage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters_usage),
	'min_nitrous_time_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 80463996),
)

any_genesys_obj__genesys__gen__physics__landing_damage__roll = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 3635654829),
)

any_genesys_obj__genesys__gen__store_pack = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'pack_item_0xc' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x14' / Int32ul,
	'ptr_arr_content_items_0x18' / Int32ul,
	'array_count_for_0x18' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_content_items_0x18' / Pointer(this.ptr_arr_content_items_0x18, Array(this.array_count_for_0x18, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3071320584),
)

any_genesys_obj__genesys__gen__handbrake_ability = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 4002008184),
)

any_genesys_obj__genesys__gen__performance_modifier = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_ptr_modifications_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_modifications_0x10' / Pointer(this.ptr_arr_ptr_modifications_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3000817087),
)

any_genesys_obj__genesys__gen__wheel_suspension_constraint = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angle_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'bool8_t_0x28' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 2076212613),
)

any_genesys_obj__genesys__gen__collision_responses__global = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'race__car__vs__race__car_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car),
	'crashing__race__car__vs__traffic_0x74' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__crashing_race_car_vs_traffic),
	'traffic__vs__dynamic_0x9c' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__traffic_vs_dynamic),
	'crashing__race__car__vs__crashing__race__car_0xc0' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car),
	'traffic__vs__traffic_0xe0' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__traffic_vs_traffic),
	'dynamic__vs__dynamic_0x100' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__dynamic_vs_dynamic),
	'game_changer_id_0x11c' / Int32ul,
	'size' / Computed(lambda this: 292),
	'mu_version_hash' / Computed(lambda this: 1217853836),
)

any_genesys_obj__genesys__gen__uicamera = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'look_at_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'position_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'up_vector_0x30' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'game_changer_id_0x40' / Int32ul,
	'aspect_ratio_0x44' / Float32l,
	'far_clip_0x48' / Float32l,
	'field_of_view_0x4c' / Float32l,
	'near_clip_0x50' / Float32l,
	'aspect_correct_0x54' / Int8ub,
	'bool8_t_0x55' / Int8ub,
	'bool8_t_0x56' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 88),
	'mu_version_hash' / Computed(lambda this: 4265727012),
)

any_genesys_obj__genesys__gen__road_block_layer = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'middle_item_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__road_block_layer__item),
	'game_changer_id_0x24' / Int32ul,
	'distance_0x28' / Float32l,
	'first_distance_0x2c' / Float32l,
	'ptr_arr_left_items_0x30' / Int32ul,
	'ptr_arr_right_items_0x34' / Int32ul,
	'array_count_for_0x30' / Int16ul,
	'array_count_for_0x34' / Int16ul,
	'inst_left_items_0x30' / Pointer(this.ptr_arr_left_items_0x30, Array(this.array_count_for_0x30, LazyBound(lambda: any_genesys_obj__genesys__gen__road_block_layer__item))),
	'inst_right_items_0x34' / Pointer(this.ptr_arr_right_items_0x34, Array(this.array_count_for_0x34, LazyBound(lambda: any_genesys_obj__genesys__gen__road_block_layer__item))),
	'size' / Computed(lambda this: 64),
	'mu_version_hash' / Computed(lambda this: 1694754426),
)

any_genesys_obj__genesys__gen__race_balancing_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'extra_crash_schedule_time_0x10' / Float32l,
	'extra_schedule_time_0x14' / Float32l,
	'ptr_arr_opponent_data_0x18' / Int32ul,
	'array_count_for_0x18' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_opponent_data_0x18' / Pointer(this.ptr_arr_opponent_data_0x18, Array(this.array_count_for_0x18, LazyBound(lambda: any_genesys_obj__genesys__gen__race_balancing_data__opponent_balancing_data))),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3055337662),
)

any_genesys_obj__genesys__gen__tyre_sound_params__long_spin = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'ya_am_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 2081469541),
)

any_genesys_obj__genesys__gen__nitrous_parameters__nitrous_power = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'time_to_full_nitrous_0xc' / Float32l,
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 2483448381),
)

any_genesys_obj__genesys__gen__tyre_sound_params__lat_slip = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'ya_am_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 860059237),
)

any_genesys_obj__genesys__gen__dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'output__channels_0x10' / Int32ul,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 1356872704),
)

any_genesys_obj__genesys__gen__post_fx_keyframe__general = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'car_motion_blur_0x10' / Float32l,
	'world_colour_cube_weight_0x14' / Float32l,
	'world_motion_blur_0x18' / Float32l,
	'world_saturation_0x1c' / Float32l,
	'unk_enum_0x20' / Int32ul,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 4085824509),
)

any_genesys_obj__genesys__gen__performance_modification_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'value_0x10' / Float32l,
	'unk_enum_0x14' / Int16ul,
	'modification_type_0x16' / Int16ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1555583970),
)

any_genesys_obj__genesys__gen__collision_effects__traffic_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__collision_effects__traffic_effect__extra_roll_params_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__traffic_effect__extra_roll_params),
	'genesys__gen__collision_effects__traffic_effect__extra_roll_params_0x24' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__traffic_effect__extra_roll_params),
	'genesys__gen__collision_effects__traffic_effect__extra_roll_params_0x3c' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__traffic_effect__extra_roll_params),
	'cam__effect_0x54' / FixedSized(8, GreedyBytes),
	'cam__effect__unstable_0x5c' / FixedSized(8, GreedyBytes),
	'cam__effect__scale_0x64' / Float32l,
	'stable__camera__threshold_0x68' / Float32l,
	'unstable__camera__threshold_0x6c' / Float32l,
	'size' / Computed(lambda this: 116),
	'mu_version_hash' / Computed(lambda this: 2066481913),
)

any_genesys_obj__genesys__gen__nitrous_parameters__punch_usage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters_usage),
	'punch_burn_percent_0x1c' / Float32l,
	'punch_delay_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 3479966800),
)

any_genesys_obj__genesys__gen__handling_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_genesys__gen__aerodynamic_behaviour_0x10' / Int32ul,
	'ptr_genesys__gen__aligning_torque_0x14' / Int32ul,
	'ptr_genesys__gen__body_movement_behaviour_0x18' / Int32ul,
	'ptr_genesys__gen__brake_behaviour_0x1c' / Int32ul,
	'ptr_genesys__gen__donut_ability_0x20' / Int32ul,
	'ptr_drift_0x24' / Int32ul,
	'ptr_engine_0x28' / Int32ul,
	'ptr_genesys__gen__handbrake_ability_0x2c' / Int32ul,
	'ptr_genesys__gen__hard_driving_behaviour_0x30' / Int32ul,
	'ptr_genesys__gen__steering_behaviour_0x34' / Int32ul,
	'ptr_genesys__gen__steering_wheel_physics_0x38' / Int32ul,
	'ptr_genesys__gen__suspension_0x3c' / Int32ul,
	'ptr_genesys__gen__tyres_0x40' / Int32ul,
	'inst_genesys__gen__brake_behaviour_0x1c' / Pointer(this.ptr_genesys__gen__brake_behaviour_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__brake_behaviour)),
	'inst_genesys__gen__handbrake_ability_0x2c' / Pointer(this.ptr_genesys__gen__handbrake_ability_0x2c, LazyBound(lambda: any_genesys_obj__genesys__gen__handbrake_ability)),
	'inst_genesys__gen__body_movement_behaviour_0x18' / Pointer(this.ptr_genesys__gen__body_movement_behaviour_0x18, LazyBound(lambda: any_genesys_obj__genesys__gen__body_movement_behaviour)),
	'inst_drift_0x24' / Pointer(this.ptr_drift_0x24, LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour)),
	'inst_engine_0x28' / Pointer(this.ptr_engine_0x28, LazyBound(lambda: any_genesys_obj__genesys__gen__engine)),
	'inst_genesys__gen__donut_ability_0x20' / Pointer(this.ptr_genesys__gen__donut_ability_0x20, LazyBound(lambda: any_genesys_obj__genesys__gen__donut_ability)),
	'inst_genesys__gen__hard_driving_behaviour_0x30' / Pointer(this.ptr_genesys__gen__hard_driving_behaviour_0x30, LazyBound(lambda: any_genesys_obj__genesys__gen__hard_driving_behaviour)),
	'inst_genesys__gen__aerodynamic_behaviour_0x10' / Pointer(this.ptr_genesys__gen__aerodynamic_behaviour_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__aerodynamic_behaviour)),
	'inst_genesys__gen__aligning_torque_0x14' / Pointer(this.ptr_genesys__gen__aligning_torque_0x14, LazyBound(lambda: any_genesys_obj__genesys__gen__aligning_torque)),
	'size' / Computed(lambda this: 72),
	'inst_genesys__gen__steering_behaviour_0x34' / Pointer(this.ptr_genesys__gen__steering_behaviour_0x34, LazyBound(lambda: any_genesys_obj__genesys__gen__steering_behaviour)),
	'inst_genesys__gen__tyres_0x40' / Pointer(this.ptr_genesys__gen__tyres_0x40, LazyBound(lambda: any_genesys_obj__genesys__gen__tyres)),
	'inst_genesys__gen__suspension_0x3c' / Pointer(this.ptr_genesys__gen__suspension_0x3c, LazyBound(lambda: any_genesys_obj__genesys__gen__suspension)),
	'inst_genesys__gen__steering_wheel_physics_0x38' / Pointer(this.ptr_genesys__gen__steering_wheel_physics_0x38, LazyBound(lambda: any_genesys_obj__genesys__gen__steering_wheel_physics)),
	'mu_version_hash' / Computed(lambda this: 3811132854),
)

any_genesys_obj__genesys__gen__wcremove_world_entity_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 1055028229),
)

any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 210492029),
)

any_genesys_obj__genesys__gen__gameplay_trigger__output__sequence_output = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'sequence_0xc' / Int32ul,
	'sequence_type_0x10' / Int16ul,
	'bool8_t_0x12' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 2222283730),
)

any_genesys_obj__genesys__gen__car_select_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cop_idle_sequences_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__car_select_data__sequences),
	'cop_sequences_0x28' / LazyBound(lambda: any_genesys_obj__genesys__gen__car_select_data__sequences),
	'racer_idle_sequences_0x44' / LazyBound(lambda: any_genesys_obj__genesys__gen__car_select_data__sequences),
	'racer_sequences_0x60' / LazyBound(lambda: any_genesys_obj__genesys__gen__car_select_data__sequences),
	'ptr_arr_cop_placements_0x7c' / Int32ul,
	'game_changer_id_0x80' / Int32ul,
	'ptr_arr_racer_placements_0x84' / Int32ul,
	'uimemory_limit_0x88' / Float32l,
	'uiresource_limit_0x8c' / Int32sl,
	'array_count_for_0x7c' / Int16ul,
	'array_count_for_0x84' / Int16ul,
	'loop_sequences_0x94' / Int8ub,
	'split_by_tier_0x95' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_cop_placements_0x7c' / Pointer(this.ptr_arr_cop_placements_0x7c, Array(this.array_count_for_0x7c, Int32ul)),
	'inst_racer_placements_0x84' / Pointer(this.ptr_arr_racer_placements_0x84, Array(this.array_count_for_0x84, Int32ul)),
	'size' / Computed(lambda this: 152),
	'mu_version_hash' / Computed(lambda this: 4000545794),
)

any_genesys_obj__genesys__gen__vehicle__sound = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__unique_id_0xc' / Int32ul,
	'cgs_core__unique_id_0x10' / Int32ul,
	'game_changer_id_0x14' / Int32ul,
	'horn_0x18' / Int32ul,
	'cgs_core__unique_id_0x1c' / Int32ul,
	'ptr_arr_cgs_core__unique_id_0x20' / Int32ul,
	'array_count_for_0x20' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_cgs_core__unique_id_0x20' / Pointer(this.ptr_arr_cgs_core__unique_id_0x20, Array(this.array_count_for_0x20, Int32ul)),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 535359424),
)

any_genesys_obj__genesys__gen__timeline_controllers__race_car_entity_timeline_controller = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_timeline_controller),
	'unk_enum_0x1c' / Int32ul,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 267183785),
)

any_genesys_obj__genesys__gen__nitrous_parameters__catching_air = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'nitrous_reward_0x14' / Float32l,
	'time_in_air_0x18' / Float32l,
	'is_enabled_0x1c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 2075263523),
)

any_genesys_obj__genesys__gen__aligning_torque = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3406519319),
)

any_genesys_obj__genesys__gen__collision_responses__global__crashing_race_car_vs_traffic = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'crashing__race__car__angular__solve_0x10' / Float32l,
	'crashing__race__car__linear__solve_0x14' / Float32l,
	'friction_0x18' / Float32l,
	'restitution_0x1c' / Float32l,
	'traffic__angular__solve_0x20' / Float32l,
	'traffic__linear__solve_0x24' / Float32l,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 2626118372),
)

any_genesys_obj__genesys__gen__enable_compound_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour),
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3591755513),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__damage_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'damage_0x14' / Float32l,
	'linear__solve_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3134806732),
)

any_genesys_obj__genesys__gen__sound_distance_falloff = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'curve_type_0x10' / Float32l,
	'curve_type_reverb_0x14' / Float32l,
	'divergence_at_max_distance_0x18' / Float32l,
	'divergence_at_min_distance_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'initial_gain_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'arrays_motioned_0x30' / Float32l,
	'max_distance_0x34' / Float32l,
	'max_distance_divergence_0x38' / Float32l,
	'max_distance_reverb_0x3c' / Float32l,
	'min_distance_0x40' / Float32l,
	'min_distance_divergence_0x44' / Float32l,
	'min_distance_reverb_0x48' / Float32l,
	'occlusion_multiplier_0x4c' / Float32l,
	'peak_gain_0x50' / Float32l,
	'float32_t_0x54' / Float32l,
	'float32_t_0x58' / Float32l,
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 591869524),
)

any_genesys_obj__genesys__gen__challenge_action__hit_trigger = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'size' / Computed(lambda this: 80),
	'mu_version_hash' / Computed(lambda this: 3231281576),
)

any_genesys_obj__genesys__gen__scoring_action__online_scoring_feedback = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'description_0xc' / Int32ul,
	'sequence_0x10' / Int32ul,
	'cgs_core__unique_id_0x14' / Int32ul,
	'title_0x18' / Int32ul,
	'deferrable_0x1c' / Int8ub,
	'opposing__team_0x1d' / Int8ub,
	'scoring__player_0x1e' / Int8ub,
	'scoring__team_0x1f' / Int8ub,
	'bool8_t_0x20' / Int8ub,
	'victim__player_0x21' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 1781716212),
)

any_genesys_obj__genesys__gen__general_trigger_sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'trigger_0x28' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 3179911126),
)

any_genesys_obj__genesys__gen__vehicle__gameplay__tyre_trails = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'unk_enum_0xc' / Int16ul,
	'stock_0xe' / Int16ul,
	'track_0x10' / Int32ul,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 4100294056),
)

any_genesys_obj__int8_t = Struct(
)

any_genesys_obj__genesys__gen__online__driving_test_list_groups = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_ptr_driving_test_list_groups_0x10' / Int32ul,
	'array_count_for_0x10' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_driving_test_list_groups_0x10' / Pointer(this.ptr_arr_ptr_driving_test_list_groups_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 4242000614),
)

any_genesys_obj__genesys__gen__donut_ability__donut_grip_values = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 4164557270),
)

any_genesys_obj__genesys__gen__aerodynamic_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'float32_t_0x48' / Float32l,
	'float32_t_0x4c' / Float32l,
	'float32_t_0x50' / Float32l,
	'float32_t_0x54' / Float32l,
	'float32_t_0x58' / Float32l,
	'float32_t_0x5c' / Float32l,
	'float32_t_0x60' / Float32l,
	'float32_t_0x64' / Float32l,
	'bool8_t_0x68' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 108),
	'mu_version_hash' / Computed(lambda this: 3037639290),
)

any_genesys_obj__genesys__gen__suspension_wheel = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__string_base_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'cgs_core__string_base_0x14' / LazyBound(lambda: any_genesys_obj__string_base),
	'damage_0x1c' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x24' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0x2c' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x34' / Int32ul,
	'float32_t_0x38' / Float32l,
	'size' / Computed(lambda this: 64),
	'mu_version_hash' / Computed(lambda this: 1279163701),
)

any_genesys_obj__genesys__gen__point2d = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'inline_arr_float32_t_0xc' / Array(2, Float32l),
	'array_count_for_0xc' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3430005461),
)

any_genesys_obj__genesys__gen__challenge_action__jump_stats = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'size' / Computed(lambda this: 80),
	'mu_version_hash' / Computed(lambda this: 3366752106),
)

any_genesys_obj__genesys__gen__suspension = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1387924581),
)

any_genesys_obj__genesys__gen__event = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_arr_autotest_checkpoints_0xc' / Int32ul,
	'cinematic_name_0x10' / Int32ul,
	'description_0x14' / Int32ul,
	'game_changer_id_0x18' / Int32ul,
	'game_mode_0x1c' / Int32ul,
	'game_pack_0x20' / Int32ul,
	'cgs_core__unique_id_0x24' / Int32ul,
	'cycle_time_of_day_0x28' / Float32l,
	'finish_time_of_day_0x2c' / Float32l,
	'sun_direction_0x30' / Float32l,
	'time_of_day_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'ptr_arr_ptr_chevron_list_0x3c' / Int32ul,
	'road_surface_conditions_0x40' / Int16ul,
	'array_count_for_0xc' / Int16ul,
	'is_alternative_weather_0x44' / Int8ub,
	'is_rain_active_0x45' / Int8ub,
	'is_thunder_active_0x46' / Int8ub,
	'override_sun_direction_0x47' / Int8ub,
	'bool8_t_0x48' / Int8ub,
	'array_count_for_0x3c' / Int8ub,
	'uint8_t_0x4a' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'inst_autotest_checkpoints_0xc' / Pointer(this.ptr_arr_autotest_checkpoints_0xc, Array(this.array_count_for_0xc, Int32ul)),
	'inst_chevron_list_0x3c' / Pointer(this.ptr_arr_ptr_chevron_list_0x3c, Array(this.array_count_for_0x3c, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 3089457678),
)

any_genesys_obj__genesys__gen__engine__transmission = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'float32_t_0xc' / Float32l,
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 3829466250),
)

any_genesys_obj__genesys__gen__vehicle_paint__material_properties = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'rw_math_vpu__vector3_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector3_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector4_0x30' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x40' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x50' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x60' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'game_changer_id_0x70' / Int32ul,
	'float32_t_0x74' / Float32l,
	'float32_t_0x78' / Float32l,
	'size' / Computed(lambda this: 128),
	'mu_version_hash' / Computed(lambda this: 2896523173),
)

any_genesys_obj__cgs_core__unique_id = Struct(
)

any_genesys_obj__genesys__gen__aiplayer_type = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__unique_id_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'rollout_0x14' / Int32ul,
	'ptr_arr_target_placement_0x18' / Int32ul,
	'aggression_delay_0x1c' / Float32l,
	'aggression_frequency_0x20' / Float32l,
	'blinded_time_scale_0x24' / Float32l,
	'escaping_speed_0x28' / Float32l,
	'fail_jump_daze_time_0x2c' / Float32l,
	'flat_out_initial_time_0x30' / Float32l,
	'flat_out_time_0x34' / Float32l,
	'hit_damage_percentage_to_daze_0x38' / Float32l,
	'hit_daze_time_0x3c' / Float32l,
	'max_damage_for_speed_effect_0x40' / Float32l,
	'max_event_balancing_distance_0x44' / Float32l,
	'max_speed_for_distance_0x48' / Float32l,
	'min_damage_for_speed_effect_0x4c' / Float32l,
	'min_event_balancing_distance_0x50' / Float32l,
	'min_shortcut_time_0x54' / Float32l,
	'min_speed_for_distance_0x58' / Float32l,
	'min_throttle_damage_percent_0x5c' / Float32l,
	'min_time_between_weapon_uses_0x60' / Float32l,
	'respawn_time_0x64' / Float32l,
	'shortcut_taking_percentage_0x68' / Float32l,
	'spawn_speed_0x6c' / Float32l,
	'speed_0x70' / Float32l,
	'speed_matching_max_distance_0x74' / Float32l,
	'speed_matching_max_speed_0x78' / Float32l,
	'float32_t_0x7c' / Float32l,
	'speed_matching_min_speed_0x80' / Float32l,
	'speed_matching_speed_difference_0x84' / Float32l,
	'toughness_0x88' / Float32l,
	'turn_at_junction_percentage_0x8c' / Float32l,
	'uturn_min_time_0x90' / Float32l,
	'weapon_avoidance_percentage_0x94' / Float32l,
	'weapon_use_delay_at_event_start_0x98' / Float32l,
	'weaving_duration_0x9c' / Float32l,
	'weaving_frequency_0xa0' / Float32l,
	'aggression_type_0xa4' / Int16ul,
	'behaviour_0xa6' / Int16ul,
	'unk_enum_0xa8' / Int16ul,
	'nitrous_usage_0xaa' / Int16ul,
	'weaving_type_0xac' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'allowed_to_respawn_0xb0' / Int8ub,
	'can_rhino_0xb1' / Int8ub,
	'do_uturns_0xb2' / Int8ub,
	'is_aggressor_0xb3' / Int8ub,
	'is_blacklist_0xb4' / Int8ub,
	'is_cop_0xb5' / Int8ub,
	'bool8_t_0xb6' / Int8ub,
	'uint8_t_0xb7' / Int8ub,
	'weapon_use_chance_0xb8' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_target_placement_0x18' / Pointer(this.ptr_arr_target_placement_0x18, Array(this.array_count_for_0x18, Int32ul)),
	'size' / Computed(lambda this: 188),
	'mu_version_hash' / Computed(lambda this: 3533118493),
)

any_genesys_obj__ptr = Struct(
	'offset' / Int32sl,
	'data' / Pointer(this.offset, If(this.offset != 0, LazyBound(lambda: any_genesys_obj__atype))),
)

any_genesys_obj__genesys__gen__mixer_channel_sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'mixer__channel_0x2c' / FixedSized(8, GreedyBytes),
	'ptr_arr_double__params_0x34' / Int32ul,
	'array_count_for_0x34' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_double__params_0x34' / Pointer(this.ptr_arr_double__params_0x34, Array(this.array_count_for_0x34, LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value))),
	'size' / Computed(lambda this: 60),
	'mu_version_hash' / Computed(lambda this: 2706222886),
)

any_genesys_obj__int32_t = Struct(
)

any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'game_changer_id_0x50' / Int32ul,
	'half_length_0x54' / Float32l,
	'radius_0x58' / Float32l,
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 18021398),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ai__stable_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__damage_params),
	'ai__unstable_0x28' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__damage_params),
	'player__stable_0x44' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__damage_params),
	'player__unstable_0x60' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__damage_params),
	'ai__crashed_0x7c' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__basic_params),
	'player__crashed_0x94' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__basic_params),
	'player__invulnerable_0xac' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__basic_params),
	'player__when__ai__crashed_0xc4' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__basic_params),
	'game_changer_id_0xdc' / Int32ul,
	'friction_0xe0' / Float32l,
	'restitution_0xe4' / Float32l,
	'size' / Computed(lambda this: 236),
	'mu_version_hash' / Computed(lambda this: 2391445668),
)

any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__corona = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'colour_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'cgs_resource__handle_0x20' / FixedSized(8, GreedyBytes),
	'corona_definition_0x28' / FixedSized(8, GreedyBytes),
	'locator_group_0x30' / Int32ul,
	'brightness_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'unk_enum_0x40' / Int16ul,
	'time_of_day_0x42' / Int16ul,
	'bool8_t_0x44' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 72),
	'mu_version_hash' / Computed(lambda this: 3445640778),
)

any_genesys_obj__genesys__gen__engine_sound2__gain_param = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_resource__handle_0xc' / FixedSized(8, GreedyBytes),
	'gain_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 4223711972),
)

any_genesys_obj__genesys__gen__gameplay__condition = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_arr_strings_0xc' / Int32ul,
	'game_changer_id_0x10' / Int32ul,
	'ptr_arr_references_0x14' / Int32ul,
	'ptr_arr_values_0x18' / Int32ul,
	'test_0x1c' / Int16ul,
	'type_0x1e' / Int16ul,
	'array_count_for_0x14' / Int16ul,
	'array_count_for_0xc' / Int16ul,
	'array_count_for_0x18' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_strings_0xc' / Pointer(this.ptr_arr_strings_0xc, Array(this.array_count_for_0xc, LazyBound(lambda: any_genesys_obj__string_base))),
	'inst_references_0x14' / Pointer(this.ptr_arr_references_0x14, Array(this.array_count_for_0x14, Int32ul)),
	'size' / Computed(lambda this: 40),
	'inst_values_0x18' / Pointer(this.ptr_arr_values_0x18, Array(this.array_count_for_0x18, Int32ul)),
	'mu_version_hash' / Computed(lambda this: 1901216409),
)

any_genesys_obj__genesys__gen__vehicle__driver_setup__seat_belt_bone_offset = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'position_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rotation_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 3542932618),
)

any_genesys_obj__genesys__gen__challenge_action__speed_run = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'route_count_0x50' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 84),
	'mu_version_hash' / Computed(lambda this: 3616318101),
)

any_genesys_obj__genesys__gen__vehicle_paint__structure2 = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 1082129393),
)

any_genesys_obj__genesys__gen__snd_player_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 2473868341),
)

any_genesys_obj__genesys__gen__sub_harmoniser_dsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 489513931),
)

any_genesys_obj__genesys__gen__control_mesh = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'rw_math_vpu__vector2_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector2),
	'rw_math_vpu__vector3_0x20' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector3_0x30' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector4_0x40' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0x50' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'game_changer_id_0x60' / Int32ul,
	'size' / Computed(lambda this: 104),
	'mu_version_hash' / Computed(lambda this: 1980202577),
)

any_genesys_obj__genesys__gen__offline_event__checkpoint_info = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'sequence_0xc' / Int32ul,
	'type_0x10' / Int16ul,
	'bool8_t_0x12' / Int8ub,
	'show_split_time_0x13' / Int8ub,
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 2582603530),
)

any_genesys_obj__genesys__gen__collision_responses__world__player__flip_state = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'flip_graph_power_0x10' / Float32l,
	'flip_min_threshold_0x14' / Float32l,
	'flip_scale_0x18' / Float32l,
	'player_speed_mph_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 1278315440),
)

any_genesys_obj__genesys__gen__pan2ddsp_plug_in = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 3858691605),
)

any_genesys_obj__genesys__gen__store_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'name_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'psnpackage_name_0x14' / LazyBound(lambda: any_genesys_obj__string_base),
	'nucleus_ent_tag_0x1c' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x24' / Int32ul,
	'ptr_arr_long__description_0x28' / Int32ul,
	'main_image_0x2c' / Int32ul,
	'sub_image1_0x30' / Int32ul,
	'sub_image2_0x34' / Int32ul,
	'title_0x38' / Int32ul,
	'ptr_arr_entitlements_0x3c' / Int32ul,
	'x360license_mask_0x40' / Int32ul,
	'x360offer_id_0x44' / Int32ul,
	'array_count_for_0x28' / Int16ul,
	'show__in__store_0x4a' / Int8ub,
	'array_count_for_0x3c' / Int8ub,
	'inst_long__description_0x28' / Pointer(this.ptr_arr_long__description_0x28, Array(this.array_count_for_0x28, Int32ul)),
	'inst_entitlements_0x3c' / Pointer(this.ptr_arr_entitlements_0x3c, Array(this.array_count_for_0x3c, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 80),
	'mu_version_hash' / Computed(lambda this: 325575367),
)

any_genesys_obj__genesys__gen__collision_responses__world__traffic = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'friction_0x10' / Float32l,
	'restitution_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 174645272),
)

any_genesys_obj__genesys__gen__brake_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 2252962025),
)

any_genesys_obj__genesys__gen__jump_timeline_controller = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_timeline_controller),
	'destination_time_0x1c' / Float32l,
	'trigger_time_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 115778840),
)

any_genesys_obj__genesys__gen__collision_info__traffic_effect = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cam__effect_0xc' / FixedSized(8, GreedyBytes),
	'cam__effect__scale_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2276451180),
)

any_genesys_obj__genesys__gen__impact_damage_graphs = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'general_damage_graph_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__impact_damage_graphs__graph),
	'race_car_vs_race_car_damage_graph_0x30' / LazyBound(lambda: any_genesys_obj__genesys__gen__impact_damage_graphs__graph),
	'game_changer_id_0x54' / Int32ul,
	'velocity_for_full_damage_mph_0x58' / Float32l,
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 196190359),
)

any_genesys_obj__genesys__gen__easy_guide__page = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'cgs_core__unique_id_0x10' / Int32ul,
	'ptr_arr_cgs_core__unique_id_0x14' / Int32ul,
	'sequence_0x18' / Int32ul,
	'ptr_arr_text_0x1c' / Int32ul,
	'ptr_arr_cgs_resource__handle_0x20' / Int32ul,
	'unk_enum_0x24' / Int16ul,
	'array_count_for_0x1c' / Int16ul,
	'array_count_for_0x20' / Int8ub,
	'array_count_for_0x14' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_text_0x1c' / Pointer(this.ptr_arr_text_0x1c, Array(this.array_count_for_0x1c, Int32ul)),
	'inst_cgs_resource__handle_0x20' / Pointer(this.ptr_arr_cgs_resource__handle_0x20, Array(this.array_count_for_0x20, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'size' / Computed(lambda this: 44),
	'inst_cgs_core__unique_id_0x14' / Pointer(this.ptr_arr_cgs_core__unique_id_0x14, Array(this.array_count_for_0x14, Int32ul)),
	'mu_version_hash' / Computed(lambda this: 1365071824),
)

any_genesys_obj__genesys__gen__car_swap_spot = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__unique_id_0xc' / Int32ul,
	'colour_id_0x10' / Int32ul,
	'game_changer_id_0x14' / Int32ul,
	'cgs_core__unique_id_0x18' / Int32ul,
	'parking_placement_0x1c' / Int32ul,
	'placement_0x20' / Int32ul,
	'vehicle_id_0x24' / Int32ul,
	'vehicle_placement_0x28' / Int32ul,
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 1611423524),
)

any_genesys_obj__genesys__gen__road_block_layer__item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'cgs_core__unique_id_0x10' / Int32ul,
	'angle_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 2808391399),
)

any_genesys_obj__genesys__gen__vehicles__nitrous_upgrade = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 980106560),
)

any_genesys_obj__genesys__gen__mixer_channel__priority = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'priority_0xc' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 16),
	'mu_version_hash' / Computed(lambda this: 2235129779),
)

any_genesys_obj__genesys__gen__challenge_action__jump_over_players = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'bool8_t_0x4c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 80),
	'mu_version_hash' / Computed(lambda this: 1058158881),
)

any_genesys_obj__genesys__gen__tyre__long__grip__curve = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'fgow_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 84747879),
)

any_genesys_obj__genesys__gen__physical_definition__rigid_body__convex_hull_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'convex_hull_0x50' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x58' / Int32ul,
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 1664340785),
)

any_genesys_obj__genesys__gen__physical_definition__rigid_body__box_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'halfsize_0x50' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'game_changer_id_0x60' / Int32ul,
	'i6je_0x64' / Int32sl,
	'size' / Computed(lambda this: 108),
	'mu_version_hash' / Computed(lambda this: 678938689),
)

any_genesys_obj__genesys__gen__tyre_vfx_behaviour__long_lat_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 1442317719),
)

any_genesys_obj__genesys__gen__heat_level_sound_set__nitrous = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'compressor__override_0xc' / Int32ul,
	'cop__on_0x10' / Int32ul,
	'ptr_arr_mix__snapshot__set_0x14' / Int32ul,
	'racer__off_0x18' / Int32ul,
	'racer__on_0x1c' / Int32ul,
	'array_count_for_0x14' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_mix__snapshot__set_0x14' / Pointer(this.ptr_arr_mix__snapshot__set_0x14, Array(this.array_count_for_0x14, Int32ul)),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 3178679735),
)

any_genesys_obj__genesys__gen__vfx_locator_group_vehicle_spot_effect_sequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'rw_math_vpu__vector3_0x30' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'rw_math_vpu__vector3_0x40' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'intensity_0x50' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value),
	'cgs_core__string_base_0x88' / LazyBound(lambda: any_genesys_obj__string_base),
	'cgs_resource__handle_0x90' / FixedSized(8, GreedyBytes),
	'locator_group_0x98' / Int32ul,
	'size' / Computed(lambda this: 160),
	'mu_version_hash' / Computed(lambda this: 574246386),
)

any_genesys_obj__genesys__object = Struct(
)

any_genesys_obj__genesys__gen__wheel_damage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'size' / Computed(lambda this: 52),
	'mu_version_hash' / Computed(lambda this: 2504213501),
)

any_genesys_obj__genesys__gen__collision_info__world_damage = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_aggressive_0xc' / Int32ul,
	'ptr_self__inflicted_0x10' / Int32ul,
	'inst_aggressive_0xc' / Pointer(this.ptr_aggressive_0xc, LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info_damage_profile)),
	'inst_self__inflicted_0x10' / Pointer(this.ptr_self__inflicted_0x10, LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info_damage_profile)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 756034263),
)

any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_core__unique_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'cop_behaviour_0x14' / Int16ul,
	'positioning_0x16' / Int8sb,
	'padding' / FixedSized(1, GreedyBytes),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 35335782),
)

any_genesys_obj__uint16_t = Struct(
)

any_genesys_obj__genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'angular__solve_0x10' / Float32l,
	'linear__solve_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 3881994110),
)

any_genesys_obj__genesys__gen__event_arena_data__spawn_point_collection = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_spawn_points_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_spawn_points_0x10' / Pointer(this.ptr_arr_spawn_points_0x10, Array(this.array_count_for_0x10, Int32ul)),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 4090590688),
)

any_genesys_obj__genesys__gen__tyre__lateral__grip__curve = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 2479955317),
)

any_genesys_obj__genesys__gen__game_unlock_list = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'ptr_arr_ptr_item_0x10' / Int32ul,
	'array_count_for_0x10' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_item_0x10' / Pointer(this.ptr_arr_ptr_item_0x10, Array(this.array_count_for_0x10, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 24),
	'mu_version_hash' / Computed(lambda this: 738476701),
)

any_genesys_obj__genesys__gen__corona__glow = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'unk_enum_0x10' / Int8ub,
	'colour_0xa0' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'rw_math_vpu__vector4_0xb0' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4),
	'material_0xc0' / FixedSized(8, GreedyBytes),
	'depth_bias_0xc8' / Float32l,
	'rotation_offset_0xcc' / Float32l,
	'render_buffer_0xd0' / Int32ul,
	'size' / Computed(lambda this: 216),
	'mu_version_hash' / Computed(lambda this: 3040986089),
)

any_genesys_obj__genesys__gen__gameplay_trigger = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'predicate_0xc' / LazyBound(lambda: any_genesys_obj__string_base),
	'game_changer_id_0x14' / Int32ul,
	'time_to_wait_0x18' / Float32l,
	'ptr_arr_input_0x1c' / Int32ul,
	'ptr_arr_output_0x20' / Int32ul,
	'trigger_lifetime_0x24' / Int16ul,
	'array_count_for_0x1c' / Int16ul,
	'array_count_for_0x20' / Int16ul,
	'add_to_mini_map_0x2a' / Int8ub,
	'bool8_t_0x2b' / Int8ub,
	'bool8_t_0x2c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_input_0x1c' / Pointer(this.ptr_arr_input_0x1c, Array(this.array_count_for_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__input))),
	'inst_output_0x20' / Pointer(this.ptr_arr_output_0x20, Array(this.array_count_for_0x20, LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__output))),
	'size' / Computed(lambda this: 48),
	'mu_version_hash' / Computed(lambda this: 23772465),
)

any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'volume_to_body_transform_0x10' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine),
	'halfsize_0x50' / LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3),
	'game_changer_id_0x60' / Int32ul,
	'i6je_0x64' / Int32sl,
	'size' / Computed(lambda this: 108),
	'mu_version_hash' / Computed(lambda this: 678938689),
)

any_genesys_obj__genesys__gen__collision_responses__world__crashed_player__constraint_data = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'friction_0x10' / Float32l,
	'restitution_0x14' / Float32l,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1592993583),
)

any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'first__frame_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile),
	'low__speed_0x34' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile),
	'subsequent__frames_0x5c' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile),
	'player__invulnerable_0x84' / LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params),
	'game_changer_id_0x9c' / Int32ul,
	'full__high__speed__mph_0xa0' / Float32l,
	'full__low__speed__mph_0xa4' / Float32l,
	'size' / Computed(lambda this: 172),
	'mu_version_hash' / Computed(lambda this: 3256016364),
)

any_genesys_obj__genesys__gen__challenge__online_challenge = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__online_event),
	'intro_0x70' / Int32ul,
	'deallocated_nodule_0x74' / Int32ul,
	'ptr_arr_ptr_parts_0x78' / Int32ul,
	'elimination_type_0x7c' / Int16ul,
	'type_0x7e' / Int16ul,
	'array_count_for_0x78' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'inst_parts_0x78' / Pointer(this.ptr_arr_ptr_parts_0x78, Array(this.array_count_for_0x78, LazyBound(lambda: any_genesys_obj__ptr))),
	'size' / Computed(lambda this: 132),
	'mu_version_hash' / Computed(lambda this: 2121274978),
)

any_genesys_obj__genesys__gen__safehouse = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'discovery_trigger_0xc' / Int32ul,
	'entry_sequence_0x10' / Int32ul,
	'exit_sequence_0x14' / Int32ul,
	'exit_spawn_location_0x18' / Int32ul,
	'game_changer_id_0x1c' / Int32ul,
	'name_0x20' / Int32ul,
	'placement_0x24' / Int32ul,
	'size' / Computed(lambda this: 44),
	'mu_version_hash' / Computed(lambda this: 3469692361),
)

any_genesys_obj__genesys__gen__light__spot = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__light__cone),
	'float32_t_0x70' / Float32l,
	'size' / Computed(lambda this: 120),
	'mu_version_hash' / Computed(lambda this: 2189872818),
)

any_genesys_obj__genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'plug_in_0xc' / Int32ul,
	'plug_in__type_0x10' / Int32ul,
	'ptr_arr_sound_distance_falloff_0x14' / Int32ul,
	'ptr_value_0x18' / Int32ul,
	'parameter__name_0x1c' / Int32ul,
	'automated__property_0x20' / Int16ul,
	'array_count_for_0x14' / Int8ub,
	'padding' / FixedSized(1, GreedyBytes),
	'inst_sound_distance_falloff_0x14' / Pointer(this.ptr_arr_sound_distance_falloff_0x14, Array(this.array_count_for_0x14, LazyBound(lambda: any_genesys_obj__cgs_resource__handle))),
	'inst_value_0x18' / Pointer(this.ptr_value_0x18, LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value)),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 1967128889),
)

any_genesys_obj__genesys__gen__post_fxsequence_item = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item),
	'genesys__gen__sequence_item__modulating_double_value_0x5c' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value),
	'genesys__gen__sequence_item__modulating_double_value_0x94' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value),
	'genesys__gen__sequence_item__modulating_double_value_0xcc' / LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value),
	'cgs_core__string_base_0x104' / LazyBound(lambda: any_genesys_obj__string_base),
	'post_fxstate_0x10c' / FixedSized(8, GreedyBytes),
	'unk_enum_0x114' / Int16ul,
	'override_intensity_0x116' / Int8ub,
	'endless__environment_0x117' / Int8ub,
	'size' / Computed(lambda this: 284),
	'mu_version_hash' / Computed(lambda this: 4032173314),
)

any_genesys_obj__genesys__gen__nitrous_strength = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'jump_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_strength__jump),
	'punch_0x24' / LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_strength__punch),
	'game_changer_id_0x38' / Int32ul,
	'float32_t_0x3c' / Float32l,
	'size' / Computed(lambda this: 68),
	'mu_version_hash' / Computed(lambda this: 1201833830),
)

any_genesys_obj__genesys__gen__camera_gameplay_gradient_adjustments = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__camera_gameplay_gradient_adjustments__params_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_gradient_adjustments__params),
	'genesys__gen__camera_gameplay_gradient_adjustments__params_0x24' / LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_gradient_adjustments__params),
	'game_changer_id_0x3c' / Int32ul,
	'float32_t_0x40' / Float32l,
	'size' / Computed(lambda this: 72),
	'mu_version_hash' / Computed(lambda this: 980871986),
)

any_genesys_obj__genesys__gen__camera_rear_view = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'inline_arr_float32_t_0xc' / Array(3, Float32l),
	'game_changer_id_0x18' / Int32ul,
	'float32_t_0x1c' / Float32l,
	'ptr_genesys__gen__camera_rear_view_globals_0x20' / Int32ul,
	'array_count_for_0xc' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_genesys__gen__camera_rear_view_globals_0x20' / Pointer(this.ptr_genesys__gen__camera_rear_view_globals_0x20, LazyBound(lambda: any_genesys_obj__genesys__gen__camera_rear_view_globals)),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 998115052),
)

any_genesys_obj__genesys__gen__drift_behaviour__drift_scale = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'size' / Computed(lambda this: 56),
	'mu_version_hash' / Computed(lambda this: 2655111671),
)

any_genesys_obj__genesys__gen__nitrous_parameters__crash_escape = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'minimum_speed_0x14' / Float32l,
	'nitrous_reward_0x18' / Float32l,
	'is_enabled_0x1c' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 1463097890),
)

any_genesys_obj__genesys__gen__damage_bar_profiles__profile = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'segment_recharge_time_0x10' / Float32l,
	'segment_recharge_wait_0x14' / Float32l,
	'ptr_arr_segment_limits_0x18' / Int32ul,
	'ptr_arr_world_segment_limits_0x1c' / Int32ul,
	'array_count_for_0x18' / Int16ul,
	'array_count_for_0x1c' / Int16ul,
	'inst_segment_limits_0x18' / Pointer(this.ptr_arr_segment_limits_0x18, Array(this.array_count_for_0x18, LazyBound(lambda: any_genesys_obj__genesys__gen__damage_bar_profiles__profile__segment_data))),
	'inst_world_segment_limits_0x1c' / Pointer(this.ptr_arr_world_segment_limits_0x1c, Array(this.array_count_for_0x1c, LazyBound(lambda: any_genesys_obj__genesys__gen__damage_bar_profiles__profile__segment_data))),
	'size' / Computed(lambda this: 40),
	'mu_version_hash' / Computed(lambda this: 2099267897),
)

any_genesys_obj__genesys__gen__traffic_flow_type__traffic_flow_type = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'traffic_vehicle_type_0xc' / FixedSized(8, GreedyBytes),
	'colour_0x14' / Int32ul,
	'game_changer_id_0x18' / Int32ul,
	'proportion_0x1c' / Float32l,
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 2353212897),
)

any_genesys_obj__genesys__gen__nitrous_parameters__hitting_another_competitor = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'message_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'minimum_speed_0x14' / Float32l,
	'minimum_time_0x18' / Float32l,
	'nitrous_reward_0x1c' / Float32l,
	'is_enabled_0x20' / Int8ub,
	'padding' / FixedSized(3, GreedyBytes),
	'size' / Computed(lambda this: 36),
	'mu_version_hash' / Computed(lambda this: 2656703430),
)

any_genesys_obj__genesys__gen__game_rank = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'rank__image_0x10' / Int32ul,
	'rank__name_0x14' / Int32ul,
	'rank__number_0x18' / Int32sl,
	'size' / Computed(lambda this: 32),
	'mu_version_hash' / Computed(lambda this: 3159067131),
)

any_genesys_obj__genesys__gen__vehicles__performance_upgrades = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'pro_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__performance_upgrades__category),
	'standard_0x60' / LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__performance_upgrades__category),
	'game_changer_id_0xb4' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0xb8' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0xbc' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0xc0' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0xc4' / Int32ul,
	'ptr_genesys__gen__vehicles__upgrade_base_0xc8' / Int32ul,
	'inst_genesys__gen__vehicles__upgrade_base_0xb8' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0xb8, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0xbc' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0xbc, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0xc8' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0xc8, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'inst_genesys__gen__vehicles__upgrade_base_0xc4' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0xc4, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'size' / Computed(lambda this: 208),
	'inst_genesys__gen__vehicles__upgrade_base_0xc0' / Pointer(this.ptr_genesys__gen__vehicles__upgrade_base_0xc0, LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base)),
	'mu_version_hash' / Computed(lambda this: 662978111),
)

any_genesys_obj__genesys__gen__heat_level__behaviour_coordination = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour),
	'genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x30' / LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour),
	'float32_t_0x54' / Float32l,
	'ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58' / Int32ul,
	'array_count_for_0x58' / Int16ul,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58' / Pointer(this.ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58, Array(this.array_count_for_0x58, LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour))),
	'size' / Computed(lambda this: 96),
	'mu_version_hash' / Computed(lambda this: 1883284107),
)

any_genesys_obj__cgs_core__string_base = Struct(
	'ofs_arr_buffer_0x0' / Int32ul,
	'array_count_for_0x0' / Int32ul,
	'inst_buffer_0x0' / Pointer(this.ofs_arr_buffer_0x0, FixedSized(this.array_count_for_0x0, GreedyString(encoding='ascii'))),
	'size' / Computed(lambda this: 12),
	'mu_version_hash' / Computed(lambda this: 2516314814),
)

any_genesys_obj__genesys__gen__challenge_action__accumulate_time = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base),
	'padding' / FixedSized(2, GreedyBytes),
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 1205733723),
)

any_genesys_obj__genesys__gen__engine = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'genesys__gen__engine__power_curve_0xc' / LazyBound(lambda: any_genesys_obj__genesys__gen__engine__power_curve),
	'genesys__gen__engine__sound_0x60' / LazyBound(lambda: any_genesys_obj__genesys__gen__engine__sound),
	'genesys__gen__engine__differentials_0x9c' / LazyBound(lambda: any_genesys_obj__genesys__gen__engine__differentials),
	'genesys__gen__engine__normal_quality_engine_0xb8' / LazyBound(lambda: any_genesys_obj__genesys__gen__engine__normal_quality_engine),
	'genesys__gen__engine__transmission_0xcc' / LazyBound(lambda: any_genesys_obj__genesys__gen__engine__transmission),
	'cgs_resource__handle_0xdc' / FixedSized(8, GreedyBytes),
	'cgs_resource__handle_0xe4' / FixedSized(8, GreedyBytes),
	'game_changer_id_0xec' / Int32ul,
	'float32_t_0xf0' / Float32l,
	'float32_t_0xf4' / Float32l,
	'float32_t_0xf8' / Float32l,
	'float32_t_0xfc' / Float32l,
	'float32_t_0x100' / Float32l,
	'float32_t_0x104' / Float32l,
	'float32_t_0x108' / Float32l,
	'float32_t_0x10c' / Float32l,
	'ptr_genesys__gen__gearbox_0x110' / Int32ul,
	'ptr_genesys__gen__gearbox_0x114' / Int32ul,
	'ptr_genesys__gen__nitrous_strength_0x118' / Int32ul,
	'inst_genesys__gen__gearbox_0x114' / Pointer(this.ptr_genesys__gen__gearbox_0x114, LazyBound(lambda: any_genesys_obj__genesys__gen__gearbox)),
	'size' / Computed(lambda this: 288),
	'inst_genesys__gen__gearbox_0x110' / Pointer(this.ptr_genesys__gen__gearbox_0x110, LazyBound(lambda: any_genesys_obj__genesys__gen__gearbox)),
	'inst_genesys__gen__nitrous_strength_0x118' / Pointer(this.ptr_genesys__gen__nitrous_strength_0x118, LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_strength)),
	'mu_version_hash' / Computed(lambda this: 834676531),
)

any_genesys_obj__genesys_obj_collection = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'unk_id' / Int32ul,
	'collection_start_offset' / Int32ul,
	'collection_count' / Int32ul,
	'obj_collection' / Pointer(this.collection_start_offset, Array(this.collection_count, LazyBound(lambda: any_genesys_obj__ptr))),
)

any_genesys_obj__genesys__gen__drift_behaviour__other = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'game_changer_id_0xc' / Int32ul,
	'float32_t_0x10' / Float32l,
	'float32_t_0x14' / Float32l,
	'float32_t_0x18' / Float32l,
	'float32_t_0x1c' / Float32l,
	'float32_t_0x20' / Float32l,
	'float32_t_0x24' / Float32l,
	'float32_t_0x28' / Float32l,
	'float32_t_0x2c' / Float32l,
	'float32_t_0x30' / Float32l,
	'float32_t_0x34' / Float32l,
	'float32_t_0x38' / Float32l,
	'float32_t_0x3c' / Float32l,
	'float32_t_0x40' / Float32l,
	'float32_t_0x44' / Float32l,
	'size' / Computed(lambda this: 76),
	'mu_version_hash' / Computed(lambda this: 4254634071),
)

any_genesys_obj__genesys__gen__engine_sound2__gain_param_wrapper = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ptr_gain_0xc' / Int32ul,
	'inst_gain_0xc' / Pointer(this.ptr_gain_0xc, LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__gain_param)),
	'size' / Computed(lambda this: 20),
	'mu_version_hash' / Computed(lambda this: 1218098277),
)

any_genesys_obj__genesys__gen__gameplay__revenge_bonus = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'bonus_score_0xc' / Int32ul,
	'description_0x10' / Int32ul,
	'game_changer_id_0x14' / Int32ul,
	'icon_0x18' / Int32ul,
	'name_0x1c' / Int32ul,
	'duration_0x20' / Float32l,
	'ptr_arr_ptr_genesys__gen__nitrous_parameters_0x24' / Int32ul,
	'ptr_arr_ptr_genesys__gen__performance_modifier_0x28' / Int32ul,
	'ptr_arr_feature_0x2c' / Int32ul,
	'array_count_for_0x2c' / Int16ul,
	'bool8_t_0x32' / Int8ub,
	'array_count_for_0x24' / Int8ub,
	'array_count_for_0x28' / Int8ub,
	'wrecks_count_0x35' / Int8ub,
	'padding' / FixedSized(2, GreedyBytes),
	'inst_feature_0x2c' / Pointer(this.ptr_arr_feature_0x2c, Array(this.array_count_for_0x2c, Int32ul)),
	'size' / Computed(lambda this: 56),
	'inst_genesys__gen__nitrous_parameters_0x24' / Pointer(this.ptr_arr_ptr_genesys__gen__nitrous_parameters_0x24, Array(this.array_count_for_0x24, LazyBound(lambda: any_genesys_obj__ptr))),
	'inst_genesys__gen__performance_modifier_0x28' / Pointer(this.ptr_arr_ptr_genesys__gen__performance_modifier_0x28, Array(this.array_count_for_0x28, LazyBound(lambda: any_genesys_obj__ptr))),
	'mu_version_hash' / Computed(lambda this: 1707511637),
)

any_genesys_obj__atype = Struct(
	'data' / Switch(this.dtype, {u"genesys__gen__engine__normal_quality_engine": LazyBound(lambda: any_genesys_obj__genesys__gen__engine__normal_quality_engine), u"string_base": LazyBound(lambda: any_genesys_obj__string_base), u"genesys__gen__paint_pack": LazyBound(lambda: any_genesys_obj__genesys__gen__paint_pack), u"genesys__gen__camera_gameplay_external__yaw_spring_modification": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__yaw_spring_modification), u"genesys__gen__impact_damage_graphs__graph": LazyBound(lambda: any_genesys_obj__genesys__gen__impact_damage_graphs__graph), u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume), u"genesys__gen__high_shelf_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__high_shelf_dsp_plug_in), u"genesys__gen__vehicle_info": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_info), u"genesys__gen__vehicle_camera_container": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_camera_container), u"genesys__gen__collision_responses__world__player": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__player), u"genesys__gen__online__driving_test_list_groups": LazyBound(lambda: any_genesys_obj__genesys__gen__online__driving_test_list_groups), u"any_genesys_obj": LazyBound(lambda: any_genesys_obj), u"genesys__gen__steering_wheel_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__steering_wheel_behaviour), u"s4": Int32sl, u"genesys__gen__nitrous_parameters__drifting": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__drifting), u"genesys__gen__collision_responses__global__crashing_race_car_vs_traffic": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__crashing_race_car_vs_traffic), u"genesys__gen__vehicle_colour_palette": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_colour_palette), u"genesys__gen__body_movement_behaviour__angle_control": LazyBound(lambda: any_genesys_obj__genesys__gen__body_movement_behaviour__angle_control), u"genesys__gen__collision_effects__battling_effect__extra_roll_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect__extra_roll_params), u"genesys__gen__collision_responses__race_car__aivs_traffic__damage_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__damage_params), u"genesys__gen__high_pass_butterworth_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__high_pass_butterworth_dsp_plug_in), u"genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face), u"genesys__gen__aiplayer_type": LazyBound(lambda: any_genesys_obj__genesys__gen__aiplayer_type), u"genesys__gen__nitrous_parameters__jump_usage": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__jump_usage), u"genesys__gen__post_fxstate__value_modifier": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__value_modifier), u"genesys__gen__aiplayer_instance": LazyBound(lambda: any_genesys_obj__genesys__gen__aiplayer_instance), u"genesys__gen__camera_gameplay_external_globals__impact_shake": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external_globals__impact_shake), u"genesys__gen__vehicle_damage_behaviour__spot_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__spot_effect), u"genesys__gen__vehicle_vfx_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour), u"genesys__gen__nitrous_parameters__restrictions": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__restrictions), u"genesys__gen__gameplay__milestone": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__milestone), u"genesys__gen__event_location": LazyBound(lambda: any_genesys_obj__genesys__gen__event_location), u"genesys__gen__vehicle__sound": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__sound), u"genesys__gen__uicamera": LazyBound(lambda: any_genesys_obj__genesys__gen__uicamera), u"genesys__gen__heat_level_sound_set": LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level_sound_set), u"genesys__gen__physical_definition__rigid_body": LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body), u"genesys__gen__collision_info_damage_profile": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info_damage_profile), u"genesys__gen__engine_sound2__dsp_param": LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__dsp_param), u"genesys__gen__collision_responses__world__player__flip_state": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__player__flip_state), u"genesys__gen__roadblock_instance": LazyBound(lambda: any_genesys_obj__genesys__gen__roadblock_instance), u"genesys__gen__delay_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__delay_dsp_plug_in), u"genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params), u"genesys__gen__entitlement": LazyBound(lambda: any_genesys_obj__genesys__gen__entitlement), u"genesys__gen__vehicles__performance_upgrades__category": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__performance_upgrades__category), u"genesys__gen__steering_behaviour__steering_angle_curve": LazyBound(lambda: any_genesys_obj__genesys__gen__steering_behaviour__steering_angle_curve), u"genesys__gen__scoring_action": LazyBound(lambda: any_genesys_obj__genesys__gen__scoring_action), u"genesys__gen__damage_bar_profiles__profile": LazyBound(lambda: any_genesys_obj__genesys__gen__damage_bar_profiles__profile), u"genesys__gen__challenge_action__jump_over_players": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__jump_over_players), u"genesys__gen__donut_ability": LazyBound(lambda: any_genesys_obj__genesys__gen__donut_ability), u"genesys__gen__heat_level_sound_set__nitrous": LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level_sound_set__nitrous), u"genesys__gen__body_movement_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__body_movement_behaviour), u"genesys__gen__camera_gameplay_gradient_adjustments": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_gradient_adjustments), u"genesys__gen__tyres__tyres": LazyBound(lambda: any_genesys_obj__genesys__gen__tyres__tyres), u"genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car), u"genesys__gen__gameplay__allowed_vehicle_list": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__allowed_vehicle_list), u"genesys__gen__collision_responses__race_car__player_vs_ai": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai), u"genesys__gen__drift_behaviour__yaw_torque": LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__yaw_torque), u"genesys__gen__gameplay__cop_type": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__cop_type), u"genesys__gen__post_fx_keyframe__general": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__general), u"genesys__gen__online__driving_test_list": LazyBound(lambda: any_genesys_obj__genesys__gen__online__driving_test_list), u"genesys__gen__colour_group": LazyBound(lambda: any_genesys_obj__genesys__gen__colour_group), u"genesys__gen__light__cone": LazyBound(lambda: any_genesys_obj__genesys__gen__light__cone), u"genesys__gen__camera_gameplay_shake_effect__translation__axis_params": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation__axis_params), u"genesys__gen__physical_definition": LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition), u"genesys__gen__nitrous_parameters": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters), u"genesys__object": LazyBound(lambda: any_genesys_obj__genesys__object), u"genesys__gen__drift_behaviour__side_force": LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__side_force), u"genesys__gen__challenge_action__speed_camera_action": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__speed_camera_action), u"genesys__gen__tyre_sound_params__long_spin": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__long_spin), u"genesys__gen__suspension": LazyBound(lambda: any_genesys_obj__genesys__gen__suspension), u"genesys__gen__ginsu_sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__ginsu_sequence_item), u"genesys__gen__vehicle__driver_setup": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__driver_setup), u"genesys__gen__custom_chevron": LazyBound(lambda: any_genesys_obj__genesys__gen__custom_chevron), u"genesys__gen__vehicle_damage_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour), u"genesys__gen__sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item), u"genesys__gen__online_challenge": LazyBound(lambda: any_genesys_obj__genesys__gen__online_challenge), u"genesys__gen__mixer_channel__priority": LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel__priority), u"genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params), u"genesys__gen__collision_responses__race_car__aivs_crashing_race_car": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_crashing_race_car), u"genesys__gen__vehicles__vehicle_category_info": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__vehicle_category_info), u"genesys__gen__wcvfx_behaviour__lights": LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour__lights), u"genesys__gen__ginsu_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__ginsu_dsp_plug_in), u"genesys__gen__camera_gameplay_shake_effect__translation": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation), u"genesys__gen__vehicle_damage_behaviour__bodypart": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__bodypart), u"genesys__gen__tyre__long__grip__curve": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__grip__curve), u"genesys__gen__offline_event": LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event), u"genesys__gen__corona": LazyBound(lambda: any_genesys_obj__genesys__gen__corona), u"genesys__gen__collision_responses__global": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global), u"genesys__gen__enable_compound_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__enable_compound_behaviour), u"genesys__gen__event_arena": LazyBound(lambda: any_genesys_obj__genesys__gen__event_arena), u"genesys__gen__paint_pack_group": LazyBound(lambda: any_genesys_obj__genesys__gen__paint_pack_group), u"genesys__gen__post_fx_keyframe__depth_of__field": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__depth_of__field), u"genesys__gen__collision_info": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info), u"genesys__gen__distortion_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__distortion_dsp_plug_in), u"genesys__gen__challenge_action__jump_stats": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__jump_stats), u"genesys__gen__camera_gameplay_external__speed_based_height_change": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_height_change), u"genesys__gen__gearbox": LazyBound(lambda: any_genesys_obj__genesys__gen__gearbox), u"genesys__gen__tyre_sound_params__lateral": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__lateral), u"genesys__gen__corona__beam": LazyBound(lambda: any_genesys_obj__genesys__gen__corona__beam), u"genesys__gen__rollout": LazyBound(lambda: any_genesys_obj__genesys__gen__rollout), u"genesys__gen__online_route": LazyBound(lambda: any_genesys_obj__genesys__gen__online_route), u"genesys__gen__scoring_action__online_scoring_feedback": LazyBound(lambda: any_genesys_obj__genesys__gen__scoring_action__online_scoring_feedback), u"genesys__gen__safehouse": LazyBound(lambda: any_genesys_obj__genesys__gen__safehouse), u"genesys__gen__nitrous_parameters__slipstreaming": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__slipstreaming), u"genesys__gen__event__checkpoint_info": LazyBound(lambda: any_genesys_obj__genesys__gen__event__checkpoint_info), u"genesys__gen__nitrous_parameters__speedbreaker_usage": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__speedbreaker_usage), u"genesys__gen__hard_driving_behaviour__steering_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__hard_driving_behaviour__steering_effect), u"genesys__gen__collision_info__payload_damage": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__payload_damage), u"genesys__gen__heat_level__behaviour_coordination": LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination), u"genesys__gen__collision_effects__battling_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect), u"genesys__gen__engine__power_curve": LazyBound(lambda: any_genesys_obj__genesys__gen__engine__power_curve), u"genesys__gen__wheel_suspension_constraint": LazyBound(lambda: any_genesys_obj__genesys__gen__wheel_suspension_constraint), u"genesys__gen__offline_event__custom_chevrons": LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__custom_chevrons), u"genesys__gen__pidcontroller": LazyBound(lambda: any_genesys_obj__genesys__gen__pidcontroller), u"genesys__gen__online_event": LazyBound(lambda: any_genesys_obj__genesys__gen__online_event), u"genesys__gen__make_physical_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__make_physical_behaviour), u"genesys__gen__handbrake_ability": LazyBound(lambda: any_genesys_obj__genesys__gen__handbrake_ability), u"genesys__gen__general_trigger_sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__general_trigger_sequence_item), u"cgs_core__unique_id": LazyBound(lambda: any_genesys_obj__cgs_core__unique_id), u"genesys__gen__gameplay__drift_marker": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__drift_marker), u"genesys__gen__tyre_sound_params__long_spin_braking": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__long_spin_braking), u"bool8_t": LazyBound(lambda: any_genesys_obj__bool8_t), u"genesys__gen__traffic_vehicle": LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_vehicle), u"genesys__gen__camera_gameplay_bonnet": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_bonnet), u"genesys__gen__vehicles__performance_upgrades": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__performance_upgrades), u"genesys__gen__camera_gameplay_external__acceleration_movement": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__acceleration_movement), u"genesys__gen__post_fx_keyframe": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe), u"genesys__gen__voice_group": LazyBound(lambda: any_genesys_obj__genesys__gen__voice_group), u"genesys__gen__nucleus_grant_mappings_list__mapping": LazyBound(lambda: any_genesys_obj__genesys__gen__nucleus_grant_mappings_list__mapping), u"genesys__gen__heat_level_sound_set__sirens": LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level_sound_set__sirens), u"genesys__gen__tyre__lateral__slip__factors": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__lateral__slip__factors), u"genesys__gen__gameplay_trigger": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger), u"genesys__gen__pan2ddsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__pan2ddsp_plug_in), u"s1": Int8sb, u"genesys__gen__vehicle_component__wheel": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_component__wheel), u"genesys__gen__camera_gameplay_gradient_adjustments__params": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_gradient_adjustments__params), u"genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value": LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value), u"genesys__gen__vehicle_surface_profile": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_surface_profile), u"genesys__gen__passby_sequence_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__passby_sequence_behaviour), u"genesys__gen__physics__crashing_rules__impact_rules": LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules), u"genesys__gen__post_fxsequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxsequence_item), u"genesys__gen__challenge_action__speed_run": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__speed_run), u"genesys__gen__camera_rear_view_globals": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_rear_view_globals), u"genesys__gen__nitrous_strength": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_strength), u"genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile), u"genesys__gen__camera_gameplay_shake_effect__rotation__axis_params": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation__axis_params), u"genesys__gen__vehicle_paint": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_paint), u"genesys__gen__vehicle__gameplay": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay), u"genesys__gen__vehicles__modifier_upgrade": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__modifier_upgrade), u"genesys__gen__nitrous_parameters__nitrous_power": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__nitrous_power), u"genesys__gen__game_unlock": LazyBound(lambda: any_genesys_obj__genesys__gen__game_unlock), u"genesys__gen__wheel_sizes": LazyBound(lambda: any_genesys_obj__genesys__gen__wheel_sizes), u"float32_t": LazyBound(lambda: any_genesys_obj__float32_t), u"genesys__gen__nucleus_entitlement_tag": LazyBound(lambda: any_genesys_obj__genesys__gen__nucleus_entitlement_tag), u"genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control), u"u4": Int32ul, u"genesys__gen__dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in), u"genesys__gen__collision_responses__race_car": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car), u"genesys__gen__camera_gameplay_external": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external), u"genesys__gen__tyre_vfx_behaviour__front_rear_params": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params), u"genesys__gen__challenge_action__get_to_location": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__get_to_location), u"genesys__gen__nitrous_parameters__nitrous_usage": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__nitrous_usage), u"genesys__gen__road_block_definition": LazyBound(lambda: any_genesys_obj__genesys__gen__road_block_definition), u"genesys__gen__engine__reverse_whine": LazyBound(lambda: any_genesys_obj__genesys__gen__engine__reverse_whine), u"genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold), u"genesys__gen__event_arena_data": LazyBound(lambda: any_genesys_obj__genesys__gen__event_arena_data), u"genesys__gen__camera_gameplay_bumper": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_bumper), u"genesys__gen__thank_you_screen_item": LazyBound(lambda: any_genesys_obj__genesys__gen__thank_you_screen_item), u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body), u"genesys__gen__collision_responses__global__race_car_vs_race_car__params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car__params), u"gen_obj": LazyBound(lambda: any_genesys_obj__gen_obj), u"genesys__gen__tyre_sound_params__longitudinal": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__longitudinal), u"genesys__gen__collision_responses__global__traffic_vs_dynamic": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__traffic_vs_dynamic), u"genesys__gen__tyre": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre), u"genesys__gen__aligning_torque": LazyBound(lambda: any_genesys_obj__genesys__gen__aligning_torque), u"genesys__gen__vehicle_vfx_behaviour__spot_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__spot_effect), u"genesys__gen__corona__glow": LazyBound(lambda: any_genesys_obj__genesys__gen__corona__glow), u"genesys__gen__light__base__flash_pattern": LazyBound(lambda: any_genesys_obj__genesys__gen__light__base__flash_pattern), u"genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params), u"genesys__gen__point2dwith_tangents": LazyBound(lambda: any_genesys_obj__genesys__gen__point2dwith_tangents), u"genesys__gen__race_car_physical_definition__convex_hull_conectivity_data": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__convex_hull_conectivity_data), u"genesys__gen__offline_event__alternate_routes": LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__alternate_routes), u"genesys__gen__collision_effects__traffic_effect__extra_roll_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__traffic_effect__extra_roll_params), u"u2": Int16ul, u"genesys__gen__vehicle_info__extra_axle": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_info__extra_axle), u"genesys__gen__cloud_compete_award": LazyBound(lambda: any_genesys_obj__genesys__gen__cloud_compete_award), u"cgs_resource__handle": LazyBound(lambda: any_genesys_obj__cgs_resource__handle), u"genesys__gen__point2d": LazyBound(lambda: any_genesys_obj__genesys__gen__point2d), u"genesys__gen__nitrous_parameters__donutting": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__donutting), u"genesys__gen__vehicle_component": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_component), u"genesys__gen__damage_bar_profiles": LazyBound(lambda: any_genesys_obj__genesys__gen__damage_bar_profiles), u"genesys__gen__score_view_model": LazyBound(lambda: any_genesys_obj__genesys__gen__score_view_model), u"genesys__gen__challenge_action__car_state": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__car_state), u"genesys__gen__race_car_effect_sequence_item__effect_double_value": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_effect_sequence_item__effect_double_value), u"genesys__gen__nitrous_parameters__hitting_another_competitor": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__hitting_another_competitor), u"rw_math_vpu__matrix44affine": LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine), u"genesys__gen__collision_responses__race_car__player_vs_ai__damage_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__damage_params), u"genesys__gen__gameplay__offline_upgrade": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__offline_upgrade), u"genesys__gen__mixing_group": LazyBound(lambda: any_genesys_obj__genesys__gen__mixing_group), u"int16_t": LazyBound(lambda: any_genesys_obj__int16_t), u"genesys__gen__wcvfx_behaviour__spot_effects": LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour__spot_effects), u"genesys__gen__submix_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__submix_dsp_plug_in), u"s2": Int16sl, u"genesys__gen__tyres": LazyBound(lambda: any_genesys_obj__genesys__gen__tyres), u"genesys__gen__wave_sequence_item__fade": LazyBound(lambda: any_genesys_obj__genesys__gen__wave_sequence_item__fade), u"genesys__gen__camera_gameplay_external__speed_based_movement": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_movement), u"genesys__gen__collision_effects__world_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__world_effect), u"genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params), u"genesys__gen__race_car_handling_disruption_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_handling_disruption_effect), u"genesys__gen__rollout__weapon_data": LazyBound(lambda: any_genesys_obj__genesys__gen__rollout__weapon_data), u"genesys__gen__damage_bar_profiles__profile__segment_data": LazyBound(lambda: any_genesys_obj__genesys__gen__damage_bar_profiles__profile__segment_data), u"genesys__gen__jump_timeline_controller": LazyBound(lambda: any_genesys_obj__genesys__gen__jump_timeline_controller), u"genesys__gen__online__license_plate": LazyBound(lambda: any_genesys_obj__genesys__gen__online__license_plate), u"genesys__gen__physical_definition__rigid_body__sphere_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__sphere_volume), u"genesys__gen__tyre_vfx_behaviour__long_lat_params": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__long_lat_params), u"genesys__gen__drift_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour), u"genesys__gen__gameplay_trigger__input": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__input), u"genesys__gen__uilist_items": LazyBound(lambda: any_genesys_obj__genesys__gen__uilist_items), u"genesys__gen__traffic_vehicle_traits": LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_vehicle_traits), u"genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold), u"genesys__gen__nitrous_parameters__crash_escape": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__crash_escape), u"genesys__gen__drift_behaviour__other": LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__other), u"strz": NullTerminated(GreedyString(encoding='ascii'), term=b'\x00', include=False, consume=True), u"genesys__gen__impact_damage_graphs": LazyBound(lambda: any_genesys_obj__genesys__gen__impact_damage_graphs), u"genesys__gen__physical_definition__rigid_body__convex_hull_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__convex_hull_volume), u"genesys__gen__traffic_flow_type": LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_flow_type), u"genesys_obj_collection": LazyBound(lambda: any_genesys_obj__genesys_obj_collection), u"genesys__gen__nitrous_parameters_usage": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters_usage), u"genesys__gen__score_view_model__score": LazyBound(lambda: any_genesys_obj__genesys__gen__score_view_model__score), u"genesys__gen__vehicle__gameplay__mod_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect), u"genesys__gen__challenge__location": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge__location), u"genesys__gen__timeline_controllers__race_car_entity_timeline_controller": LazyBound(lambda: any_genesys_obj__genesys__gen__timeline_controllers__race_car_entity_timeline_controller), u"genesys__gen__tyre_vfx_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour), u"genesys__gen__gameplay__blacklist_shutdown_data": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data), u"genesys__gen__vehicle_paint__material_properties": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_paint__material_properties), u"genesys__gen__race_car_effect_sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_effect_sequence_item), u"genesys__gen__engine_sound2__gain_param_wrapper": LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__gain_param_wrapper), u"genesys__gen__wcvfx_behaviour__coronas": LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour__coronas), u"genesys__gen__physics__crashing_rules": LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules), u"genesys__gen__hard_driving_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__hard_driving_behaviour), u"genesys__gen__physical_definition__rigid_body__cylinder_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__cylinder_volume), u"genesys__gen__physics__landing_damage": LazyBound(lambda: any_genesys_obj__genesys__gen__physics__landing_damage), u"genesys__gen__challenge_action__accumulate_distance": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulate_distance), u"genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params), u"genesys__gen__quit_sequence_timeline_controller": LazyBound(lambda: any_genesys_obj__genesys__gen__quit_sequence_timeline_controller), u"rw_math_vpu__vector3": LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3), u"genesys__gen__tyre__long__slip__factors": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__slip__factors), u"genesys__gen__brake_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__brake_behaviour), u"genesys__gen__offline_event__checkpoint_info": LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__checkpoint_info), u"genesys__gen__collision_info__world_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__world_effect), u"genesys__gen__collision_responses__race_car__aivs_traffic": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic), u"genesys__gen__uilist_items__item": LazyBound(lambda: any_genesys_obj__genesys__gen__uilist_items__item), u"genesys__gen__engine__sound": LazyBound(lambda: any_genesys_obj__genesys__gen__engine__sound), u"rw_math_vpu__vector2": LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector2), u"genesys__gen__challenge_action__accumulation_helper_data": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulation_helper_data), u"genesys__gen__race_balancing_data__opponent_balancing_data": LazyBound(lambda: any_genesys_obj__genesys__gen__race_balancing_data__opponent_balancing_data), u"genesys__gen__vehicles__tyre_upgrade": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__tyre_upgrade), u"genesys__gen__drift_behaviour__drift_scale": LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__drift_scale), u"genesys__gen__online__driving_test_list_group": LazyBound(lambda: any_genesys_obj__genesys__gen__online__driving_test_list_group), u"genesys__gen__easy_guide__page": LazyBound(lambda: any_genesys_obj__genesys__gen__easy_guide__page), u"genesys__gen__collision_responses__global__race_car_vs_race_car": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car), u"genesys__gen__challenge__challenge_part": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge__challenge_part), u"genesys__gen__event": LazyBound(lambda: any_genesys_obj__genesys__gen__event), u"genesys__gen__light__spot": LazyBound(lambda: any_genesys_obj__genesys__gen__light__spot), u"genesys__gen__sequence_timeline_controller": LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_timeline_controller), u"genesys__gen__nitrous_strength__jump": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_strength__jump), u"genesys__gen__gameplay__milestone__entry": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__milestone__entry), u"genesys__gen__camera_gameplay_bonnet__wind_sound": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_bonnet__wind_sound), u"genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params), u"genesys__gen__handbrake_ability__handbrake_grip_values": LazyBound(lambda: any_genesys_obj__genesys__gen__handbrake_ability__handbrake_grip_values), u"genesys__gen__steering_wheel_physics": LazyBound(lambda: any_genesys_obj__genesys__gen__steering_wheel_physics), u"f4": Float32l, u"genesys__gen__send_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__send_dsp_plug_in), u"u1": Int8ub, u"genesys__gen__lfo_sequence_item__lfo_double_value": LazyBound(lambda: any_genesys_obj__genesys__gen__lfo_sequence_item__lfo_double_value), u"genesys__gen__camera_rear_view": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_rear_view), u"genesys__gen__sequence_items__post_fx_override_sequence_item__effect_double_value": LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_items__post_fx_override_sequence_item__effect_double_value), u"genesys__gen__nitrous_parameters__fatal_hit": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__fatal_hit), u"uint16_t": LazyBound(lambda: any_genesys_obj__uint16_t), u"genesys__gen__camera_gameplay_shake_effect__rotation": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation), u"genesys__gen__collision_effects": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects), u"genesys__gen__post_fx_keyframe__vignette": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__vignette), u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__capsule_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__capsule_volume), u"genesys__gen__wave_sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__wave_sequence_item), u"genesys__gen__score_view_model__score_data": LazyBound(lambda: any_genesys_obj__genesys__gen__score_view_model__score_data), u"genesys__gen__camera_gameplay_external_globals__lens_properties": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external_globals__lens_properties), u"genesys__gen__low_pass_butterworth_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__low_pass_butterworth_dsp_plug_in), u"genesys__gen__light__point": LazyBound(lambda: any_genesys_obj__genesys__gen__light__point), u"genesys__gen__collision_responses__world__crashed_player": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__crashed_player), u"genesys__gen__challenge_action__action_base__feedback_data": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base__feedback_data), u"genesys__gen__road_block_layer__item": LazyBound(lambda: any_genesys_obj__genesys__gen__road_block_layer__item), u"genesys__gen__challenge_action__accumulate_takedowns": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulate_takedowns), u"genesys__gen__challenge_action__hit_trigger": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__hit_trigger), u"genesys__gen__collision_responses__race_car__player_vs_traffic": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic), u"genesys__gen__physics__damage_bar_profile": LazyBound(lambda: any_genesys_obj__genesys__gen__physics__damage_bar_profile), u"genesys__gen__physical_definition__rigid_body__capsule_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__capsule_volume), u"genesys__gen__physics__damage_bar_profile__impact_location_damage_scale": LazyBound(lambda: any_genesys_obj__genesys__gen__physics__damage_bar_profile__impact_location_damage_scale), u"genesys__gen__store_item": LazyBound(lambda: any_genesys_obj__genesys__gen__store_item), u"genesys__gen__smash_proxy_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__smash_proxy_behaviour), u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume), u"genesys__gen__online_challenge_target": LazyBound(lambda: any_genesys_obj__genesys__gen__online_challenge_target), u"genesys__gen__engine": LazyBound(lambda: any_genesys_obj__genesys__gen__engine), u"genesys__gen__vehicles__upgrade_base": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base), u"genesys__gen__camera_gameplay_shake_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect), u"genesys__gen__challenge_action__accumulate_near_misses": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulate_near_misses), u"genesys__gen__challenge_action__coop_accumulate_distance": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__coop_accumulate_distance), u"genesys__gen__nitrous_parameters__traffic_near_miss": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__traffic_near_miss), u"genesys__gen__dynamic_additional_info": LazyBound(lambda: any_genesys_obj__genesys__gen__dynamic_additional_info), u"genesys__gen__mixer_channel": LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel), u"genesys__gen__collision_responses__world": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world), u"genesys__gen__gameplay_trigger__output__sequence_output": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__output__sequence_output), u"genesys__gen__collision_responses__world__traffic": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__traffic), u"genesys__gen__band_pass_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__band_pass_dsp_plug_in), u"genesys__gen__vehicle_surface_profile__surface_link": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_surface_profile__surface_link), u"genesys__gen__heat_level": LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level), u"genesys__gen__collision_responses__race_car__aivs_traffic__basic_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__basic_params), u"genesys__gen__engine_sound2__dsp_param_wrapper": LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__dsp_param_wrapper), u"genesys__gen__tyre_sound_params": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params), u"genesys__gen__collision_info__traffic_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__traffic_effect), u"genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params), u"genesys__gen__nitrous_parameters__punch_usage": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__punch_usage), u"genesys__gen__nitrous_parameters__taking_shortcut": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__taking_shortcut), u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume), u"genesys__gen__online__vote_event": LazyBound(lambda: any_genesys_obj__genesys__gen__online__vote_event), u"int32_t": LazyBound(lambda: any_genesys_obj__int32_t), u"genesys__gen__traffic_flow": LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_flow), u"genesys__gen__collision_info__battling_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__battling_effect), u"genesys__gen__vehicles__nitrous_upgrade": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__nitrous_upgrade), u"genesys__gen__game_unlock_list": LazyBound(lambda: any_genesys_obj__genesys__gen__game_unlock_list), u"genesys__gen__gameplay__revenge_bonus": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__revenge_bonus), u"genesys__gen__vehicle_damage_behaviour__damage_sequence": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__damage_sequence), u"genesys__gen__vehicle__gameplay__damage_stats": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__damage_stats), u"genesys__gen__control_mesh": LazyBound(lambda: any_genesys_obj__genesys__gen__control_mesh), u"genesys__gen__light__base": LazyBound(lambda: any_genesys_obj__genesys__gen__light__base), u"genesys__gen__drift_behaviour__drift_exit": LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__drift_exit), u"genesys__gen__challenge_action__do_jump": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__do_jump), u"genesys__gen__event_list": LazyBound(lambda: any_genesys_obj__genesys__gen__event_list), u"genesys__gen__collision_responses__race_car__race_car_vs_dynamic": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__race_car_vs_dynamic), u"genesys__gen__gearbox__gear": LazyBound(lambda: any_genesys_obj__genesys__gen__gearbox__gear), u"genesys__gen__donut_ability__donut_scale": LazyBound(lambda: any_genesys_obj__genesys__gen__donut_ability__donut_scale), u"genesys__gen__tyres__surface_effects": LazyBound(lambda: any_genesys_obj__genesys__gen__tyres__surface_effects), u"genesys__gen__tyre__lateral__grip__curve": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__lateral__grip__curve), u"genesys__gen__vehicle_info__axle": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_info__axle), u"genesys__gen__nucleus_grant_mappings_list": LazyBound(lambda: any_genesys_obj__genesys__gen__nucleus_grant_mappings_list), u"genesys__gen__thankyou_mapping": LazyBound(lambda: any_genesys_obj__genesys__gen__thankyou_mapping), u"genesys__gen__sound_distance_falloff": LazyBound(lambda: any_genesys_obj__genesys__gen__sound_distance_falloff), u"genesys__gen__challenge_action__action_base": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base), u"char": LazyBound(lambda: any_genesys_obj__char), u"genesys__gen__race_balancing_data": LazyBound(lambda: any_genesys_obj__genesys__gen__race_balancing_data), u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume), u"genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake), u"genesys__gen__store_pack_list": LazyBound(lambda: any_genesys_obj__genesys__gen__store_pack_list), u"genesys__gen__game_rank": LazyBound(lambda: any_genesys_obj__genesys__gen__game_rank), u"genesys__gen__snd_player_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__snd_player_dsp_plug_in), u"genesys__gen__collision_effects__battling_effect__skid_effects": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect__skid_effects), u"genesys__gen__collision_info__battling_damage": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__battling_damage), u"genesys__gen__vehicles__sound__transmission_whine": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__sound__transmission_whine), u"genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods), u"genesys__gen__store_pack": LazyBound(lambda: any_genesys_obj__genesys__gen__store_pack), u"genesys__gen__wcvfx_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour), u"genesys__gen__post_fxstate__colour_cube_settings": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__colour_cube_settings), u"genesys__gen__collision_responses__world__in_air_player": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__in_air_player), u"genesys__gen__collision_info__battling_effect__extra_roll_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__battling_effect__extra_roll_params), u"genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params), u"genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour), u"genesys__gen__game_pack": LazyBound(lambda: any_genesys_obj__genesys__gen__game_pack), u"genesys__gen__vehicle__driver_setup__seat_belt_bone_offset": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__driver_setup__seat_belt_bone_offset), u"genesys__gen__engine__transmission": LazyBound(lambda: any_genesys_obj__genesys__gen__engine__transmission), u"genesys__gen__performance_modification_item": LazyBound(lambda: any_genesys_obj__genesys__gen__performance_modification_item), u"genesys__gen__engine__differentials": LazyBound(lambda: any_genesys_obj__genesys__gen__engine__differentials), u"genesys__gen__donut_ability__donut_grip_values": LazyBound(lambda: any_genesys_obj__genesys__gen__donut_ability__donut_grip_values), u"genesys__gen__sub_harmoniser_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__sub_harmoniser_dsp_plug_in), u"genesys__gen__camera_gameplay_external_globals": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external_globals), u"genesys__gen__suspension_wheel": LazyBound(lambda: any_genesys_obj__genesys__gen__suspension_wheel), u"genesys__gen__steering_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__steering_behaviour), u"genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params), u"genesys__gen__wheel_damage": LazyBound(lambda: any_genesys_obj__genesys__gen__wheel_damage), u"genesys__gen__engine_sound2": LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2), u"genesys__gen__behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour), u"genesys__gen__challenge__online_challenge": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge__online_challenge), u"genesys__gen__aerodynamic_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__aerodynamic_behaviour), u"genesys__gen__vehicle__gameplay__tyre_trails": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__tyre_trails), u"genesys__gen__post_fxstate": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate), u"genesys__gen__nitrous_parameters__high_speed": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__high_speed), u"genesys__gen__game_mode": LazyBound(lambda: any_genesys_obj__genesys__gen__game_mode), u"genesys__gen__corona__flare": LazyBound(lambda: any_genesys_obj__genesys__gen__corona__flare), u"genesys__gen__nitrous_parameters__traffic_oncoming": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__traffic_oncoming), u"genesys__gen__ginsu_sequence_item__fade": LazyBound(lambda: any_genesys_obj__genesys__gen__ginsu_sequence_item__fade), u"genesys__gen__vehicle_vfx_behaviour__corona": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__corona), u"genesys__gen__chevron": LazyBound(lambda: any_genesys_obj__genesys__gen__chevron), u"genesys__gen__sequence": LazyBound(lambda: any_genesys_obj__genesys__gen__sequence), u"genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal": LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal), u"genesys__gen__tyre_vfx_behaviour__smoke_params": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__smoke_params), u"genesys__gen__drift_behaviour__drift_trigger": LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__drift_trigger), u"genesys__gen__mixer_channel_sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel_sequence_item), u"rw_math_vpu__vector4": LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4), u"int8_t": LazyBound(lambda: any_genesys_obj__int8_t), u"genesys__gen__offline_event__aiplayer_information": LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__aiplayer_information), u"genesys__gen__road_block_layer": LazyBound(lambda: any_genesys_obj__genesys__gen__road_block_layer), u"genesys__gen__engine_sound2__gain_param": LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__gain_param), u"genesys__gen__collision_responses__race_car__player_vs_ai__basic_params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__basic_params), u"genesys__gen__vehicle_paint__structure2": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_paint__structure2), u"genesys__gen__sequence_items__post_fx_override_sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_items__post_fx_override_sequence_item), u"genesys__gen__gameplay_trigger__aiplayer_information": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__aiplayer_information), u"genesys__gen__body_movement_behaviour__take_off_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__body_movement_behaviour__take_off_behaviour), u"genesys__gen__collision_responses__world__crashed_player__constraint_data": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__crashed_player__constraint_data), u"genesys__gen__nucleus_entitlement_tags": LazyBound(lambda: any_genesys_obj__genesys__gen__nucleus_entitlement_tags), u"genesys__gen__wcplay_sound_behaviour__prop_surface_sound": LazyBound(lambda: any_genesys_obj__genesys__gen__wcplay_sound_behaviour__prop_surface_sound), u"cgs_core__string_base": LazyBound(lambda: any_genesys_obj__cgs_core__string_base), u"genesys__gen__race_car_physical_definition__physical_definition": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition), u"genesys__gen__traffic_flow_type__traffic_flow_type": LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_flow_type__traffic_flow_type), u"genesys__gen__engine__mix": LazyBound(lambda: any_genesys_obj__genesys__gen__engine__mix), u"genesys__gen__gameplay_trigger__output": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__output), u"genesys__gen__vehicle_vfx_behaviour__light": LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__light), u"genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value": LazyBound(lambda: any_genesys_obj__genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value), u"genesys__gen__physical_definition__rigid_body__box_volume": LazyBound(lambda: any_genesys_obj__genesys__gen__physical_definition__rigid_body__box_volume), u"genesys__gen__nitrous_parameters__catching_air": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__catching_air), u"genesys__gen__car_select_data": LazyBound(lambda: any_genesys_obj__genesys__gen__car_select_data), u"uint8_t": LazyBound(lambda: any_genesys_obj__uint8_t), u"genesys__gen__collision_effects__traffic_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__traffic_effect), u"genesys__gen__event_arena_data__spawn_point_collection": LazyBound(lambda: any_genesys_obj__genesys__gen__event_arena_data__spawn_point_collection), u"genesys__gen__physics__damage_bar_profile__segment": LazyBound(lambda: any_genesys_obj__genesys__gen__physics__damage_bar_profile__segment), u"genesys__gen__nitrous_strength__punch": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_strength__punch), u"genesys__gen__nitrous_parameters__min_speed": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__min_speed), u"genesys__gen__post_fx_keyframe__stereo_3d": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__stereo_3d), u"genesys__gen__camera_gameplay_external__deceleration__pitch__change": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__deceleration__pitch__change), u"genesys__gen__collision_responses__global__traffic_vs_traffic": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__traffic_vs_traffic), u"genesys__gen__dsp_plug_in_chain": LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in_chain), u"genesys__gen__physics__landing_damage__roll": LazyBound(lambda: any_genesys_obj__genesys__gen__physics__landing_damage__roll), u"genesys__gen__nitrous_parameters__balancing": LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__balancing), u"genesys__gen__peaking_dsp_plug_in": LazyBound(lambda: any_genesys_obj__genesys__gen__peaking_dsp_plug_in), u"genesys__gen__car_select_data__sequences": LazyBound(lambda: any_genesys_obj__genesys__gen__car_select_data__sequences), u"genesys__gen__collision_info__world_damage": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__world_damage), u"genesys__gen__wheel_suspension_spring_constraint": LazyBound(lambda: any_genesys_obj__genesys__gen__wheel_suspension_spring_constraint), u"genesys__gen__performance_modifier": LazyBound(lambda: any_genesys_obj__genesys__gen__performance_modifier), u"genesys__gen__wcplay_sound_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__wcplay_sound_behaviour), u"genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params), u"genesys__gen__race_balancing_profile": LazyBound(lambda: any_genesys_obj__genesys__gen__race_balancing_profile), u"genesys__gen__post_fx_keyframe__bloom": LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__bloom), u"genesys__gen__bus_mixer_channel_sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__bus_mixer_channel_sequence_item), u"genesys__gen__car_swap_spot": LazyBound(lambda: any_genesys_obj__genesys__gen__car_swap_spot), u"genesys__gen__sequence_item__modulating_double_value": LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value), u"genesys__gen__compound_additional_info": LazyBound(lambda: any_genesys_obj__genesys__gen__compound_additional_info), u"genesys__gen__collision_responses__global__dynamic_vs_dynamic": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__dynamic_vs_dynamic), u"genesys__gen__physics__landing_damage__pitch": LazyBound(lambda: any_genesys_obj__genesys__gen__physics__landing_damage__pitch), u"uint32_t": LazyBound(lambda: any_genesys_obj__uint32_t), u"genesys__gen__lfo_sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__lfo_sequence_item), u"genesys__gen__challenge_action__accumulate_time": LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulate_time), u"genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour), u"genesys__gen__tyre_vfx_behaviour__skid_mark_params": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__skid_mark_params), u"genesys__gen__vfx_locator_group_vehicle_spot_effect_sequence_item": LazyBound(lambda: any_genesys_obj__genesys__gen__vfx_locator_group_vehicle_spot_effect_sequence_item), u"genesys__gen__gameplay__condition": LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__condition), u"genesys__gen__hard_driving_behaviour__gas_effect": LazyBound(lambda: any_genesys_obj__genesys__gen__hard_driving_behaviour__gas_effect), u"genesys__gen__light__projected_texture": LazyBound(lambda: any_genesys_obj__genesys__gen__light__projected_texture), u"genesys__gen__camera_gameplay_external__camera__roll": LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__camera__roll), u"genesys__gen__engine__mixer__channel__gain__modification": LazyBound(lambda: any_genesys_obj__genesys__gen__engine__mixer__channel__gain__modification), u"genesys__gen__handling_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__handling_behaviour), u"genesys__gen__collision_responses__race_car__player_vs_crashing_race_car": LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car), u"genesys__gen__wcremove_world_entity_behaviour": LazyBound(lambda: any_genesys_obj__genesys__gen__wcremove_world_entity_behaviour), u"genesys__gen__race_car_physical_definition": LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition), u"genesys__gen__tyre_sound_params__lat_slip": LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__lat_slip), }, default=LazyBound(lambda: any_genesys_obj__dummy)),
)

any_genesys_obj__genesys__gen__vehicle_damage_behaviour__damage_sequence = Struct(
	'base_object' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'cgs_resource__handle_0xc' / FixedSized(8, GreedyBytes),
	'game_changer_id_0x14' / Int32ul,
	'size' / Computed(lambda this: 28),
	'mu_version_hash' / Computed(lambda this: 1109621193),
)

any_genesys_obj = Struct(
	'save_ofs' / If(this.ofs < 0, FixedSized(0, GreedyBytes)),
	'obj' / LazyBound(lambda: any_genesys_obj__gen_obj),
	'ofs' / Computed(lambda this: stream_tell(_io)),
	'data' / Pointer(this.ofs, Switch(this.obj.mu_type_version, {2847735672: LazyBound(lambda: any_genesys_obj__genesys__gen__engine__normal_quality_engine), 738476701: LazyBound(lambda: any_genesys_obj__genesys__gen__game_unlock_list), 669436076: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_paint), 1202023644: LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules), 3375675327: LazyBound(lambda: any_genesys_obj__genesys__gen__corona__beam), 21856074: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre), 3231281576: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__hit_trigger), 2099267897: LazyBound(lambda: any_genesys_obj__genesys__gen__damage_bar_profiles__profile), 1763676845: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects), 1316353574: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition), 1106192363: LazyBound(lambda: any_genesys_obj__genesys__gen__online__license_plate), 1279163701: LazyBound(lambda: any_genesys_obj__genesys__gen__suspension_wheel), 682066218: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params), 2949464142: LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_flow), 1880813572: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour), 2262242598: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data), 2121274978: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge__online_challenge), 4084465158: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_strength__punch), 3881994110: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params), 2956570466: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__damage_params), 1489464845: LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item__modulating_double_value), 1913150235: LazyBound(lambda: any_genesys_obj__genesys__gen__paint_pack_group), 368598916: LazyBound(lambda: any_genesys_obj__genesys__gen__tyres__tyres), 1329740588: LazyBound(lambda: any_genesys_obj__genesys__gen__steering_wheel_physics), 618870438: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__sound__transmission_whine), 524753351: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car), 1687823060: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__taking_shortcut), 1883284107: LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination), 1668851487: LazyBound(lambda: any_genesys_obj__genesys__gen__car_select_data__sequences), 1667642657: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__do_jump), 196190359: LazyBound(lambda: any_genesys_obj__genesys__gen__impact_damage_graphs), 3547832794: LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__yaw_torque), 4242000614: LazyBound(lambda: any_genesys_obj__genesys__gen__online__driving_test_list_groups), 4274679117: LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour), 3641337381: LazyBound(lambda: any_genesys_obj__genesys__gen__engine__sound), 1081328468: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__slipstreaming), 981367156: LazyBound(lambda: any_genesys_obj__genesys__gen__event_list), 2252962025: LazyBound(lambda: any_genesys_obj__genesys__gen__brake_behaviour), 3366752106: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__jump_stats), 3826155101: LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in_chain), 451352474: LazyBound(lambda: any_genesys_obj__genesys__gen__thankyou_mapping), 3989427985: LazyBound(lambda: any_genesys_obj__genesys__gen__light__cone), 3089457678: LazyBound(lambda: any_genesys_obj__genesys__gen__event), 3054130878: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params), 724902868: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_handling_disruption_effect), 1836975283: LazyBound(lambda: any_genesys_obj__genesys__gen__rollout), 2560361681: LazyBound(lambda: any_genesys_obj__genesys__gen__entitlement), 2076212613: LazyBound(lambda: any_genesys_obj__genesys__gen__wheel_suspension_constraint), 3584499810: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__driver_setup), 3616318101: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__speed_run), 3014928914: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__get_to_location), 3635654829: LazyBound(lambda: any_genesys_obj__genesys__gen__physics__landing_damage__roll), 709116355: LazyBound(lambda: any_genesys_obj__genesys__gen__engine__differentials), 2321043106: LazyBound(lambda: any_genesys_obj__genesys__gen__wheel_sizes), 259534121: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_rear_view_globals), 481138910: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai__basic_params), 231346471: LazyBound(lambda: any_genesys_obj__genesys__gen__ginsu_dsp_plug_in), 1694754426: LazyBound(lambda: any_genesys_obj__genesys__gen__road_block_layer), 174067018: LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__dsp_param), 1217853836: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global), 1231510099: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params), 1080225187: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world), 542430507: LazyBound(lambda: any_genesys_obj__genesys__gen__damage_bar_profiles__profile__segment_data), 3626200052: LazyBound(lambda: any_genesys_obj__genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value), 520558439: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay), 123660642: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__light), 2600311769: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__high_speed), 1963215010: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_movement), 793749252: LazyBound(lambda: any_genesys_obj__genesys__gen__game_pack), 3992764498: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__allowed_vehicle_list), 983393262: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_bumper), 2353212897: LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_flow_type__traffic_flow_type), 2361784635: LazyBound(lambda: any_genesys_obj__genesys__gen__engine__mixer__channel__gain__modification), 2169939698: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__spot_effect), 4000215473: LazyBound(lambda: any_genesys_obj__genesys__gen__low_pass_butterworth_dsp_plug_in), 1186319577: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car), 3274903722: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_bonnet__wind_sound), 115778840: LazyBound(lambda: any_genesys_obj__genesys__gen__jump_timeline_controller), 2626118372: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__crashing_race_car_vs_traffic), 1912243431: LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules), 2825220545: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__world_effect), 394812715: LazyBound(lambda: any_genesys_obj__genesys__gen__send_dsp_plug_in), 1685430085: LazyBound(lambda: any_genesys_obj__genesys__gen__hard_driving_behaviour__steering_effect), 3948195379: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base), 3823531688: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__speed_camera_action), 3469692361: LazyBound(lambda: any_genesys_obj__genesys__gen__safehouse), 3071320584: LazyBound(lambda: any_genesys_obj__genesys__gen__store_pack), 80463996: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__nitrous_usage), 306714612: LazyBound(lambda: any_genesys_obj__genesys__gen__light__base__flash_pattern), 2477895213: LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__dsp_param_wrapper), 4032173314: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxsequence_item), 3479966800: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__punch_usage), 2169124928: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params), 1901399892: LazyBound(lambda: any_genesys_obj__genesys__gen__engine__mix), 3652314633: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation__axis_params), 1483915852: LazyBound(lambda: any_genesys_obj__genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal), 615742248: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate), 3907892408: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__dynamic_vs_dynamic), 3829466250: LazyBound(lambda: any_genesys_obj__genesys__gen__engine__transmission), 4090590688: LazyBound(lambda: any_genesys_obj__genesys__gen__event_arena_data__spawn_point_collection), 1273350923: LazyBound(lambda: any_genesys_obj__genesys__gen__race_balancing_data__opponent_balancing_data), 4102322433: LazyBound(lambda: any_genesys_obj__genesys__gen__event_arena), 3530258211: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params), 3396244228: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect__extra_roll_params), 3178679735: LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level_sound_set__nitrous), 3023685899: LazyBound(lambda: any_genesys_obj__genesys__gen__body_movement_behaviour__angle_control), 509958626: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__bodypart), 1324301512: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__stereo_3d), 3179911126: LazyBound(lambda: any_genesys_obj__genesys__gen__general_trigger_sequence_item), 4085824509: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__general), 3791727622: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake), 542473885: LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__custom_chevrons), 3263786457: LazyBound(lambda: any_genesys_obj__genesys__gen__peaking_dsp_plug_in), 935932605: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__jump_usage), 3959582479: LazyBound(lambda: any_genesys_obj__genesys__gen__compound_additional_info), 1555583970: LazyBound(lambda: any_genesys_obj__genesys__gen__performance_modification_item), 3229542978: LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour__lights), 2921338515: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__milestone__entry), 866205257: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation), 4164557270: LazyBound(lambda: any_genesys_obj__genesys__gen__donut_ability__donut_grip_values), 1320933699: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__milestone), 18021398: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume), 1109621193: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__damage_sequence), 2473868341: LazyBound(lambda: any_genesys_obj__genesys__gen__snd_player_dsp_plug_in), 564124160: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__lateral), 2607248643: LazyBound(lambda: any_genesys_obj__genesys__gen__physics__landing_damage), 1325791513: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__crashed_player), 2419838023: LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event), 4260207896: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__player), 1951683017: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__basic_params), 1294158455: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__action_base__feedback_data), 2656703430: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__hitting_another_competitor), 4263309034: LazyBound(lambda: any_genesys_obj__genesys__gen__nucleus_grant_mappings_list__mapping), 1655947362: LazyBound(lambda: any_genesys_obj__genesys__gen__voice_group), 1408090920: LazyBound(lambda: any_genesys_obj__genesys__gen__handbrake_ability__handbrake_grip_values), 4159289097: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__skid_mark_params), 3131401224: LazyBound(lambda: any_genesys_obj__genesys__gen__nucleus_entitlement_tags), 1664340785: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume), 1886238258: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__battling_effect), 3664056692: LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_items__post_fx_override_sequence_item), 2776745689: LazyBound(lambda: any_genesys_obj__genesys__gen__race_balancing_profile), 4093540154: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulation_helper_data), 1852100653: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_effect_sequence_item__effect_double_value), 3115085927: LazyBound(lambda: any_genesys_obj__genesys__gen__wcplay_sound_behaviour__prop_surface_sound), 1558321222: LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour), 2041922261: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__acceleration_movement), 1015007408: LazyBound(lambda: any_genesys_obj__genesys__gen__donut_ability__donut_scale), 1543118382: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control), 3106899705: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params), 1476111906: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold), 3996354190: LazyBound(lambda: any_genesys_obj__genesys__gen__cloud_compete_award), 1901216409: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__condition), 1377850816: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__restrictions), 835914245: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__output), 4074208643: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour), 1781716212: LazyBound(lambda: any_genesys_obj__genesys__gen__scoring_action__online_scoring_feedback), 834676531: LazyBound(lambda: any_genesys_obj__genesys__gen__engine), 1356872704: LazyBound(lambda: any_genesys_obj__genesys__gen__dsp_plug_in), 1055028229: LazyBound(lambda: any_genesys_obj__genesys__gen__wcremove_world_entity_behaviour), 1967128889: LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value), 86537152: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_camera_container), 3359156872: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car), 3055337662: LazyBound(lambda: any_genesys_obj__genesys__gen__race_balancing_data), 3148721321: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external), 3542932618: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__driver_setup__seat_belt_bone_offset), 975568910: LazyBound(lambda: any_genesys_obj__genesys__gen__nucleus_grant_mappings_list), 773308239: LazyBound(lambda: any_genesys_obj__genesys__gen__ginsu_sequence_item), 2612185096: LazyBound(lambda: any_genesys_obj__genesys__gen__steering_behaviour), 2631887699: LazyBound(lambda: any_genesys_obj__genesys__gen__scoring_action), 1082129393: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_paint__structure2), 1387924581: LazyBound(lambda: any_genesys_obj__genesys__gen__suspension), 3415849662: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_component), 3815813836: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulate_distance), 1611423524: LazyBound(lambda: any_genesys_obj__genesys__gen__car_swap_spot), 2144572099: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params), 944731751: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge__location), 2784884141: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__tyre_upgrade), 3789082911: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__min_speed), 2504213501: LazyBound(lambda: any_genesys_obj__genesys__gen__wheel_damage), 3768680712: LazyBound(lambda: any_genesys_obj__genesys__gen__online_challenge), 1722819130: LazyBound(lambda: any_genesys_obj__genesys__gen__wave_sequence_item), 1110789791: LazyBound(lambda: any_genesys_obj__genesys__gen__high_pass_butterworth_dsp_plug_in), 1278315440: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__player__flip_state), 4097165157: LazyBound(lambda: any_genesys_obj__genesys__gen__lfo_sequence_item__lfo_double_value), 484081367: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__slip__factors), 3256016364: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car), 1394693111: LazyBound(lambda: any_genesys_obj__genesys__gen__donut_ability), 3085449154: LazyBound(lambda: any_genesys_obj__genesys__gen__smash_proxy_behaviour), 802364842: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__deceleration__pitch__change), 2081469541: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__long_spin), 732433969: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulate_near_misses), 2957925672: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params), 591869524: LazyBound(lambda: any_genesys_obj__genesys__gen__sound_distance_falloff), 4100294056: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__tyre_trails), 160896465: LazyBound(lambda: any_genesys_obj__genesys__gen__behaviour), 2479955317: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__lateral__grip__curve), 2066481913: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__traffic_effect), 855876020: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters), 2583194568: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_component__wheel), 1711822367: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params), 606909642: LazyBound(lambda: any_genesys_obj__genesys__gen__score_view_model__score_data), 166064775: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__lateral__slip__factors), 2808391399: LazyBound(lambda: any_genesys_obj__genesys__gen__road_block_layer__item), 3445640778: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour__corona), 2706222886: LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel_sequence_item), 956776100: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods), 2331975734: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info_damage_profile), 3746299654: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_strength__jump), 1425943760: LazyBound(lambda: any_genesys_obj__genesys__gen__tyres), 489513931: LazyBound(lambda: any_genesys_obj__genesys__gen__sub_harmoniser_dsp_plug_in), 3800105053: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic), 1844756468: LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2), 2222283730: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__output__sequence_output), 2189872818: LazyBound(lambda: any_genesys_obj__genesys__gen__light__spot), 4182861931: LazyBound(lambda: any_genesys_obj__genesys__gen__online__driving_test_list_group), 889829961: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__upgrade_base), 3500617746: LazyBound(lambda: any_genesys_obj__genesys__gen__hard_driving_behaviour), 2063558262: LazyBound(lambda: any_genesys_obj__genesys__gen__rollout__weapon_data), 3788863516: LazyBound(lambda: any_genesys_obj__genesys__gen__make_physical_behaviour), 860059237: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__lat_slip), 3190011655: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__long_spin_braking), 3533118493: LazyBound(lambda: any_genesys_obj__genesys__gen__aiplayer_type), 1589286504: LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__drift_trigger), 267183785: LazyBound(lambda: any_genesys_obj__genesys__gen__timeline_controllers__race_car_entity_timeline_controller), 1212586379: LazyBound(lambda: any_genesys_obj__genesys__gen__nucleus_entitlement_tag), 202861526: LazyBound(lambda: any_genesys_obj__genesys__gen__online_route), 1807127390: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__traffic_effect__extra_roll_params), 1234658497: LazyBound(lambda: any_genesys_obj__genesys__gen__corona), 2626560424: LazyBound(lambda: any_genesys_obj__genesys__gen__uilist_items), 456164053: LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level_sound_set), 1198075180: LazyBound(lambda: any_genesys_obj__genesys__gen__bus_mixer_channel_sequence_item), 1530679421: LazyBound(lambda: any_genesys_obj__genesys__gen__tyres__surface_effects), 4254634071: LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__other), 2078321761: LazyBound(lambda: any_genesys_obj__genesys__gen__online_challenge_target), 101265141: LazyBound(lambda: any_genesys_obj__genesys__gen__uilist_items__item), 3508674618: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__camera__roll), 166370211: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_effect_sequence_item), 678938689: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume), 1129268118: LazyBound(lambda: any_genesys_obj__genesys__gen__body_movement_behaviour__take_off_behaviour), 1980202577: LazyBound(lambda: any_genesys_obj__genesys__gen__control_mesh), 1058122174: LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level_sound_set__sirens), 3108376025: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__speed_based_height_change), 722756325: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_crashing_race_car), 3483480738: LazyBound(lambda: any_genesys_obj__genesys__gen__submix_dsp_plug_in), 2276451180: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__traffic_effect), 1365071824: LazyBound(lambda: any_genesys_obj__genesys__gen__easy_guide__page), 84747879: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre__long__grip__curve), 2483448381: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__nitrous_power), 23772465: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger), 48016591: LazyBound(lambda: any_genesys_obj__genesys__gen__pidcontroller), 2501750206: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__world_effect), 325575367: LazyBound(lambda: any_genesys_obj__genesys__gen__store_item), 3732602870: LazyBound(lambda: any_genesys_obj__genesys__gen__gearbox), 2075263523: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__catching_air), 2516314814: LazyBound(lambda: any_genesys_obj__string_base), 2089690370: LazyBound(lambda: any_genesys_obj__genesys__gen__roadblock_instance), 3195239353: LazyBound(lambda: any_genesys_obj__genesys__gen__engine__power_curve), 3257509935: LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector4), 2230798373: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__performance_upgrades__category), 477429240: LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour__coronas), 2784336371: LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector3), 1567458252: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body), 716630460: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__race_car_vs_race_car__params), 4062005660: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_colour_palette), 2006186034: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__colour_cube_settings), 2571445580: LazyBound(lambda: any_genesys_obj__genesys__gen__event__checkpoint_info), 4046186056: LazyBound(lambda: any_genesys_obj__genesys__gen__light__base), 3591755513: LazyBound(lambda: any_genesys_obj__genesys__gen__enable_compound_behaviour), 3928390869: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__donutting), 4117767557: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_damage_behaviour__spot_effect), 2207259302: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__drifting), 2593852305: LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_vehicle_traits), 2391445668: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_ai), 1600514099: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__depth_of__field), 3000817087: LazyBound(lambda: any_genesys_obj__genesys__gen__performance_modifier), 835486276: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__drift_marker), 1442317719: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__long_lat_params), 2270583296: LazyBound(lambda: any_genesys_obj__genesys__gen__event_arena_data), 3587969770: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__battling_damage), 3062587406: LazyBound(lambda: any_genesys_obj__rw_math_vpu__matrix44affine), 1291389730: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__aiplayer_information), 393413962: LazyBound(lambda: any_genesys_obj__genesys__gen__online_event), 1519651292: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe), 736842216: LazyBound(lambda: any_genesys_obj__genesys__gen__wheel_suspension_spring_constraint), 3794314553: LazyBound(lambda: any_genesys_obj__genesys__gen__band_pass_dsp_plug_in), 1472679887: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info), 3588678847: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_info__extra_axle), 3464877079: LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour), 1201833830: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_strength), 1730251222: LazyBound(lambda: any_genesys_obj__genesys__gen__quit_sequence_timeline_controller), 3643052795: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__smoke_params), 2235640885: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external_globals__impact_shake), 3162856831: LazyBound(lambda: any_genesys_obj__genesys_obj_collection), 210492029: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params), 229133803: LazyBound(lambda: any_genesys_obj__genesys__gen__light__projected_texture), 4067794056: LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_timeline_controller), 3691324629: LazyBound(lambda: any_genesys_obj__genesys__gen__aiplayer_instance), 2896762174: LazyBound(lambda: any_genesys_obj__genesys__gen__custom_chevron), 998115052: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_rear_view), 2519567673: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition), 3627785814: LazyBound(lambda: any_genesys_obj__genesys__gen__delay_dsp_plug_in), 1680453612: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_traffic), 2971966527: LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel), 2655111671: LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__drift_scale), 2169095089: LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__side_force), 61953676: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect__skid_effects), 3237867664: LazyBound(lambda: any_genesys_obj__genesys__gen__ginsu_sequence_item__fade), 4149479710: LazyBound(lambda: any_genesys_obj__genesys__gen__high_shelf_dsp_plug_in), 174008559: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__car_state), 4179189423: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume), 3085849010: LazyBound(lambda: any_genesys_obj__genesys__gen__passby_sequence_behaviour), 4049496118: LazyBound(lambda: any_genesys_obj__genesys__gen__mixing_group), 3032331154: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params), 786918963: LazyBound(lambda: any_genesys_obj__rw_math_vpu__vector2), 1822997286: LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_item), 1058158881: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__jump_over_players), 283467013: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_surface_profile__surface_link), 3691704753: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__battling_effect__extra_roll_params), 2080073476: LazyBound(lambda: any_genesys_obj__genesys__gen__score_view_model__score), 880609546: LazyBound(lambda: any_genesys_obj__genesys__gen__physics__damage_bar_profile__segment), 372702530: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__damage_stats), 2950917875: LazyBound(lambda: any_genesys_obj__genesys__gen__dynamic_additional_info), 3935354064: LazyBound(lambda: any_genesys_obj__genesys__gen__steering_behaviour__steering_angle_curve), 3136795337: LazyBound(lambda: any_genesys_obj__genesys__gen__online__vote_event), 832200604: LazyBound(lambda: any_genesys_obj__genesys__gen__paint_pack), 2896523173: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_paint__material_properties), 2235129779: LazyBound(lambda: any_genesys_obj__genesys__gen__mixer_channel__priority), 1259832621: LazyBound(lambda: any_genesys_obj__genesys__gen__colour_group), 4218582003: LazyBound(lambda: any_genesys_obj__genesys__gen__wcplay_sound_behaviour), 3916132985: LazyBound(lambda: any_genesys_obj__genesys__gen__event_location), 1692280813: LazyBound(lambda: any_genesys_obj__genesys__gen__point2dwith_tangents), 980106560: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__nitrous_upgrade), 3727471200: LazyBound(lambda: any_genesys_obj__genesys__gen__engine__reverse_whine), 2817660171: LazyBound(lambda: any_genesys_obj__genesys__gen__physics__damage_bar_profile__impact_location_damage_scale), 1205733723: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulate_time), 3159067131: LazyBound(lambda: any_genesys_obj__genesys__gen__game_rank), 3049882700: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_surface_profile), 2488860623: LazyBound(lambda: any_genesys_obj__genesys__gen__road_block_definition), 397117973: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_gradient_adjustments__params), 3080674119: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__traffic_vs_dynamic), 4117431335: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__modifier_upgrade), 3785567855: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__fatal_hit), 35335782: LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour), 3910465619: LazyBound(lambda: any_genesys_obj__genesys__gen__sequence), 2992725297: LazyBound(lambda: any_genesys_obj__genesys__gen__tyre_sound_params__longitudinal), 3592057837: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__bloom), 3796279727: LazyBound(lambda: any_genesys_obj__genesys__gen__damage_bar_profiles), 3434016526: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__gameplay__mod_effect), 980871986: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_gradient_adjustments), 3683195322: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external_globals), 1445450323: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__convex_hull_conectivity_data), 2474227476: LazyBound(lambda: any_genesys_obj__genesys__gen__lfo_sequence_item), 2952229338: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__race_car_vs_dynamic), 3430005461: LazyBound(lambda: any_genesys_obj__genesys__gen__point2d), 3181724531: LazyBound(lambda: any_genesys_obj__genesys__gen__distortion_dsp_plug_in), 4000545794: LazyBound(lambda: any_genesys_obj__genesys__gen__car_select_data), 1642529028: LazyBound(lambda: any_genesys_obj__genesys__gen__sequence_items__post_fx_override_sequence_item__effect_double_value), 662978111: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__performance_upgrades), 3650009805: LazyBound(lambda: any_genesys_obj__genesys__gen__physics__damage_bar_profile), 3037639290: LazyBound(lambda: any_genesys_obj__genesys__gen__aerodynamic_behaviour), 3040986089: LazyBound(lambda: any_genesys_obj__genesys__gen__corona__glow), 2522613547: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__speedbreaker_usage), 963800229: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__global__traffic_vs_traffic), 467841911: LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_flow_type), 574246386: LazyBound(lambda: any_genesys_obj__genesys__gen__vfx_locator_group_vehicle_spot_effect_sequence_item), 3440578930: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_info__axle), 1758839251: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__cop_type), 4265727012: LazyBound(lambda: any_genesys_obj__genesys__gen__uicamera), 3580468080: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect), 3858691605: LazyBound(lambda: any_genesys_obj__genesys__gen__pan2ddsp_plug_in), 106358757: LazyBound(lambda: any_genesys_obj__genesys__gen__body_movement_behaviour), 4002008184: LazyBound(lambda: any_genesys_obj__genesys__gen__handbrake_ability), 3395112625: LazyBound(lambda: any_genesys_obj__genesys__gen__traffic_vehicle), 3954992488: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_info), 850192155: LazyBound(lambda: any_genesys_obj__genesys__gen__chevron), 1703771469: LazyBound(lambda: any_genesys_obj__genesys__gen__impact_damage_graphs__graph), 1811326154: LazyBound(lambda: any_genesys_obj__genesys__gen__wave_sequence_item__fade), 3342396752: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_bonnet), 4256545587: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__traffic_near_miss), 174645272: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__traffic), 2039183453: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__coop_accumulate_distance), 3811132854: LazyBound(lambda: any_genesys_obj__genesys__gen__handling_behaviour), 3529693283: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__translation__axis_params), 401492861: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters_usage), 4191696074: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_effects__battling_effect), 3736686144: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold), 2634904179: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay_trigger__input), 3616117713: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge_action__accumulate_takedowns), 814214755: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external__yaw_spring_modification), 1021288769: LazyBound(lambda: any_genesys_obj__genesys__gen__hard_driving_behaviour__gas_effect), 3124672599: LazyBound(lambda: any_genesys_obj__genesys__gen__steering_wheel_behaviour), 1707511637: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__revenge_bonus), 3591252192: LazyBound(lambda: any_genesys_obj__genesys__gen__challenge__challenge_part), 456387781: LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__alternate_routes), 1592993583: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__crashed_player__constraint_data), 760083: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicles__vehicle_category_info), 756034263: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__world_damage), 456234940: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_info__payload_damage), 3406519319: LazyBound(lambda: any_genesys_obj__genesys__gen__aligning_torque), 3302002317: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle_vfx_behaviour), 535359424: LazyBound(lambda: any_genesys_obj__genesys__gen__vehicle__sound), 2600271809: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__traffic_oncoming), 1755540478: LazyBound(lambda: any_genesys_obj__genesys__gen__online__driving_test_list), 1218098277: LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__gain_param_wrapper), 112782069: LazyBound(lambda: any_genesys_obj__genesys__gen__gameplay__offline_upgrade), 2401606622: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_external_globals__lens_properties), 2578912561: LazyBound(lambda: any_genesys_obj__genesys__gen__thank_you_screen_item), 1463097890: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__crash_escape), 2208212217: LazyBound(lambda: any_genesys_obj__genesys__gen__wcvfx_behaviour__spot_effects), 3608189499: LazyBound(lambda: any_genesys_obj__genesys__gen__gearbox__gear), 616120463: LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__aiplayer_information), 2658850274: LazyBound(lambda: any_genesys_obj__genesys__gen__game_mode), 4039040682: LazyBound(lambda: any_genesys_obj__genesys__gen__drift_behaviour__drift_exit), 3583346207: LazyBound(lambda: any_genesys_obj__genesys__gen__game_unlock), 4223711972: LazyBound(lambda: any_genesys_obj__genesys__gen__engine_sound2__gain_param), 3975851796: LazyBound(lambda: any_genesys_obj__genesys__gen__light__point), 2582603530: LazyBound(lambda: any_genesys_obj__genesys__gen__offline_event__checkpoint_info), 4081022393: LazyBound(lambda: any_genesys_obj__genesys__gen__nitrous_parameters__balancing), 1001882986: LazyBound(lambda: any_genesys_obj__genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face), 1091853463: LazyBound(lambda: any_genesys_obj__genesys__gen__heat_level), 1517189091: LazyBound(lambda: any_genesys_obj__genesys__gen__physics__landing_damage__pitch), 3357198890: LazyBound(lambda: any_genesys_obj__genesys__gen__corona__flare), 2328783125: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__world__in_air_player), 3573113074: LazyBound(lambda: any_genesys_obj__genesys__gen__store_pack_list), 1171375143: LazyBound(lambda: any_genesys_obj__genesys__gen__score_view_model), 1220037810: LazyBound(lambda: any_genesys_obj__genesys__gen__camera_gameplay_shake_effect__rotation), 4120564202: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fxstate__value_modifier), 4035751676: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile), 3180273648: LazyBound(lambda: any_genesys_obj__genesys__gen__post_fx_keyframe__vignette), 3134806732: LazyBound(lambda: any_genesys_obj__genesys__gen__collision_responses__race_car__aivs_traffic__damage_params), })),
)

_schema = any_genesys_obj
