# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class AnyGenesysObj(KaitaiStruct):

    class EDe300000(Enum):
        invalid = 0
        small = 1
        medium = 2
        large = 3

    class EB2350700(Enum):
        default = 0
        reverb = 1
        ev2 = 2
        ev3 = 3
        buffering__percents = 4

    class EE8Bc1600(Enum):
        stock = 0
        track = 1
        ev2 = 2

    class E53371100(Enum):
        move_on = 0
        fail = 1

    class E27300000(Enum):
        none = 0
        engine = 1
        skid = 2
        player = 3
        competitor = 4
        traffic = 5
        ui = 6

    class E29F70300(Enum):
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

    class E69321100(Enum):
        chasing = 0
        blocking = 1
        bruising = 2
        rhino = 3
        ev4 = 4
        idle = 5
        default = 6

    class EA8600400(Enum):
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

    class E2d391100(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2
        simultaneous = 3
        ev4 = 4

    class EA12e0000(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2
        ev3 = 3
        ev4 = 4
        ev5 = 5

    class E8e4e4912(Enum):
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

    class E77Cc0600(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2
        ev3 = 3
        ev4 = 4
        ev5 = 5
        ev6 = 6
        ev7 = 7

    class E15F70300(Enum):
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

    class EFfF81700(Enum):
        none = 0
        ev1 = 1
        ev2 = 2
        ev3 = 3
        random = 4

    class E76F50e00(Enum):
        ev0 = 0
        imagen_rewarding = 1
        live_feed = 2
        photo_gallery = 3

    class E13371100(Enum):
        none = 0
        raw = 1
        tick = 2
        speed = 3
        time = 4
        position = 5
        distance = 6

    class E0f340700(Enum):
        ev0 = 0
        ev1 = 1
        clip = 2
        off = 3

    class ED9651500(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2
        ev3 = 3
        ev4 = 4
        ev5 = 5
        ev6 = 6
        ev7 = 7
        ev8 = 8

    class EF6310000(Enum):
        ev0 = 0
        ev1 = 1
        grey = 2
        ev3 = 3
        ev4 = 4
        ev5 = 5
        ev6 = 6
        blue = 7
        ev8 = 8

    class E86F40e00(Enum):
        multi_player = 0
        single_player = 1
        social = 2
        ev3 = 3
        ev4 = 4
        disallowed__currently = 5
        ev6 = 6

    class E8aFa0600(Enum):
        none = 0

    class E28371100(Enum):
        none = 0
        ev1 = 1
        on__finish = 2

    class EE6391100(Enum):
        allow_fail = 0
        ev1 = 1

    class E5bF60300(Enum):
        multiply = 0
        offset = 1
        absolute = 2

    class EA3370900(Enum):
        default = 0
        helicopter = 1

    class ED5F60300(Enum):
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

    class E3d300000(Enum):
        none = 0
        power = 1
        multiply = 2

    class E83F60300(Enum):
        time = 0
        binding = 1
        none = 2

    class EE3310f00(Enum):
        standard = 0
        pro = 1

    class E095e0f00(Enum):
        scalar = 0
        addition = 1
        override = 2

    class EB9B21700(Enum):
        ev0 = 0
        online_only = 1
        ev2 = 2

    class EC4F30300(Enum):
        loaded = 0
        streamed = 1
        ev2 = 2
        decay_exceptionally = 3
        ev4 = 4
        speech__stream = 5
        ev6 = 6
        ev7 = 7

    class E2b770f00(Enum):
        ev0 = 0
        ev1 = 1
        sector_start = 2
        lap_start = 3
        ev4 = 4

    class E3e5f0400(Enum):
        seconds = 0
        chain = 1
        lives = 2
        events = 3
        speed_lists = 4
        all__time = 5

    class ED7310f00(Enum):
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

    class EF0310000(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2
        ev3 = 3
        traffic = 4

    class E53Bc1600(Enum):
        none = 0
        individual = 1
        social = 2
        team = 3

    class E32670d00(Enum):
        ev0 = 0
        shunt = 1
        ev2 = 2
        skid = 3

    class EBc350700(Enum):
        gain = 0
        frequency = 1
        q = 2
        time = 3
        feedback = 4
        ev5 = 5
        ev6 = 6
        ev7 = 7
        ev8 = 8

    class EE4330700(Enum):
        mono = 0
        stereo = 1
        ev2 = 2

    class E22300000(Enum):
        none = 0
        low = 1
        normal = 2
        extreme = 3

    class ED7E31000(Enum):
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

    class E55310f00(Enum):
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

    class E35300000(Enum):
        ev0 = 0
        high_cost = 1

    class EA7D81900(Enum):
        equals = 0
        ev1 = 1

    class E1d300000(Enum):
        near = 0
        mid = 1
        far = 2
        ev3 = 3

    class E38300000(Enum):
        invalid = 0
        match = 1
        linear = 2
        exponential = 3

    class E13940e00(Enum):
        no_retry = 0
        ev1 = 1
        ev2 = 2

    class E42F30e00(Enum):
        ev0 = 0
        timeout = 1

    class E18320000(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2

    class EC82f0000(Enum):
        ev0 = 0
        dlc1 = 1
        dlc2 = 2
        dlc3 = 3
        dlc4 = 4

    class E2b551900(Enum):
        acceleration = 0
        top_speed = 1
        ev2 = 2
        ev3 = 3
        toughness = 4
        ev5 = 5
        nitrous = 6

    class E58391100(Enum):
        current_action = 0
        last_action = 1

    class EF7F20e00(Enum):
        none = 0
        ev1 = 1
        ev2 = 2
        ev3 = 3

    class E93370900(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2

    class E04320000(Enum):
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

    class E71Fa0600(Enum):
        none = 0

    class EB327000002(Enum):
        none = 0
        camera_aligned = 1

    class ED9310000(Enum):
        ev0 = 0
        ev1 = 1
        rear = 2
        left = 3
        ev4 = 4
        ev5 = 5
        ev6 = 6
        ev7 = 7
        ev8 = 8

    class E68F10e00(Enum):
        win = 0
        lose = 1
        special = 2

    class EC3381100(Enum):
        speed_test = 0
        team = 1
        social = 2

    class EEe330700(Enum):
        source = 0
        ev1 = 1
        perceives_several = 2
        ev3 = 3
        ev4 = 4
        ev5 = 5
        ev6 = 6

    class E4a630400(Enum):
        deducted__shield = 0
        ev1 = 1

    class EF30d0600(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2
        ev3 = 3

    class ED0390b00(Enum):
        constantly = 0
        periodically = 1
        on__entry = 2
        once = 3

    class E93F30500(Enum):
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

    class E831d1000(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2
        ev3 = 3
        ev4 = 4
        ev5 = 5
        ev6 = 6

    class E858d1000(Enum):
        once = 0
        random = 1
        periodic = 2
        ev3 = 3
        ev4 = 4
        ev5 = 5

    class ED9F00e00(Enum):
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

    class EF45f0f00(Enum):
        ev0 = 0
        ev1 = 1
        road = 2
        ev3 = 3
        track = 4

    class E000f1600(Enum):
        ev0 = 0
        ev1 = 1
        ev2 = 2

    class E956a960c(Enum):
        ev0 = 0
        online = 1

    class E24371100(Enum):
        individual = 0
        team = 1
        everyone = 2

    class EF02f0000(Enum):
        none = 0
        ev1 = 1
        ev2 = 2
        ev3 = 3

    class EE1Bc1600(Enum):
        off = 0
        standard = 1
        pro = 2

    class E2aBe0700(Enum):
        high_quality = 0
        low_quality = 1

    class E8f7d0f00(Enum):
        brightness = 0
        contrast = 1
        motion__blur = 2

    class EA45d0f00(Enum):
        ev0 = 0
        ev1 = 1
        stock = 2
        track = 3
        ev4 = 4
        ev5 = 5

    class E025e0f00(Enum):
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

    class E55210a00(Enum):
        none = 0
        channel_animation = 1
        ev2 = 2

    class E435f0400(Enum):
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

    class E72Cc0600(Enum):
        play__once = 0
        ev1 = 1
        ev2 = 2

    class E0f391100(Enum):
        longest = 0
        shortest = 1
        most = 2
        least = 3
        closest = 4
        ev5 = 5

    class EE2B21700(Enum):
        ev0 = 0

    class EF7340700(Enum):
        rate = 0
        ev1 = 1
        ev2 = 2

    class E70Fa0600(Enum):
        none = 0

    class E8b380900(Enum):
        dry = 0
        wet = 1
        standing_water = 2

    class E43F60500(Enum):
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

    class E0eF70500(Enum):
        time = 0
        score = 1

    class E2a6b0700(Enum):
        stop = 0
        restart = 1
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        if self.ofs < 0:
            self.save_ofs = self._io.read_bytes(0)

        self.obj = AnyGenesysObj.GenObj(self._io, self, self._root)

    class GenesysGenTyreLongSlipFactors(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 484081367
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicsDamageBarProfile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__physics__damage_bar_profile__impact_location_damage_scale_0xc = AnyGenesysObj.GenesysGenPhysicsDamageBarProfileImpactLocationDamageScale(self._io, self, self._root)
            self.crashing_rules_0x34 = self._io.read_bytes(8)
            self.game_changer_id_0x3c = self._io.read_u4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.ejected_rubbish_0x48 = self._io.read_f4le()
            self.float32_t_0x4c = self._io.read_f4le()
            self.float32_t_0x50 = self._io.read_f4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.float32_t_0x58 = self._io.read_f4le()
            self.float32_t_0x5c = self._io.read_f4le()
            self.float32_t_0x60 = self._io.read_f4le()
            self.float32_t_0x64 = self._io.read_f4le()
            self.float32_t_0x68 = self._io.read_f4le()
            self.float32_t_0x6c = self._io.read_f4le()
            self.ptr_arr_segments_0x70 = self._io.read_u4le()
            self.array_count_for_0x70 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_segments_0x70(self):
            if hasattr(self, '_m_inst_segments_0x70'):
                return self._m_inst_segments_0x70

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_segments_0x70)
            self._m_inst_segments_0x70 = []
            for i in range(self.array_count_for_0x70):
                self._m_inst_segments_0x70.append(AnyGenesysObj.GenesysGenPhysicsDamageBarProfileSegment(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_segments_0x70', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 120
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3650009805
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCorona(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.unk_enum_0x10 = self._io.read_u1()
            self.game_changer_id_0xa0 = self._io.read_u4le()
            self.float32_t_0xa4 = self._io.read_f4le()
            self.max_visible_distance_0xa8 = self._io.read_f4le()
            self.visibility_test_depth_bias_0xac = self._io.read_f4le()
            self.ptr_arr_beams_0xb0 = self._io.read_u4le()
            self.ptr_arr_flares_0xb4 = self._io.read_u4le()
            self.ptr_arr_env_map_glows_0xb8 = self._io.read_u4le()
            self.ptr_arr_glows_0xbc = self._io.read_u4le()
            self.ptr_arr_planar_reflection_glows_0xc0 = self._io.read_u4le()
            self.ptr_arr_rear_view_mirror_glows_0xc4 = self._io.read_u4le()
            self.flags_0xc8 = self._io.read_u2le()
            self.array_count_for_0xb0 = self._io.read_u2le()
            self.array_count_for_0xb8 = self._io.read_u2le()
            self.array_count_for_0xb4 = self._io.read_u2le()
            self.array_count_for_0xbc = self._io.read_u2le()
            self.array_count_for_0xc0 = self._io.read_u2le()
            self.array_count_for_0xc4 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_planar_reflection_glows_0xc0(self):
            if hasattr(self, '_m_inst_planar_reflection_glows_0xc0'):
                return self._m_inst_planar_reflection_glows_0xc0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_planar_reflection_glows_0xc0)
            self._m_inst_planar_reflection_glows_0xc0 = []
            for i in range(self.array_count_for_0xc0):
                self._m_inst_planar_reflection_glows_0xc0.append(AnyGenesysObj.GenesysGenCoronaGlow(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_planar_reflection_glows_0xc0', None)

        @property
        def inst_beams_0xb0(self):
            if hasattr(self, '_m_inst_beams_0xb0'):
                return self._m_inst_beams_0xb0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_beams_0xb0)
            self._m_inst_beams_0xb0 = []
            for i in range(self.array_count_for_0xb0):
                self._m_inst_beams_0xb0.append(AnyGenesysObj.GenesysGenCoronaBeam(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_beams_0xb0', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 216
            return getattr(self, '_m_size', None)

        @property
        def inst_flares_0xb4(self):
            if hasattr(self, '_m_inst_flares_0xb4'):
                return self._m_inst_flares_0xb4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_flares_0xb4)
            self._m_inst_flares_0xb4 = []
            for i in range(self.array_count_for_0xb4):
                self._m_inst_flares_0xb4.append(AnyGenesysObj.GenesysGenCoronaFlare(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_flares_0xb4', None)

        @property
        def inst_glows_0xbc(self):
            if hasattr(self, '_m_inst_glows_0xbc'):
                return self._m_inst_glows_0xbc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_glows_0xbc)
            self._m_inst_glows_0xbc = []
            for i in range(self.array_count_for_0xbc):
                self._m_inst_glows_0xbc.append(AnyGenesysObj.GenesysGenCoronaGlow(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_glows_0xbc', None)

        @property
        def inst_env_map_glows_0xb8(self):
            if hasattr(self, '_m_inst_env_map_glows_0xb8'):
                return self._m_inst_env_map_glows_0xb8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_env_map_glows_0xb8)
            self._m_inst_env_map_glows_0xb8 = []
            for i in range(self.array_count_for_0xb8):
                self._m_inst_env_map_glows_0xb8.append(AnyGenesysObj.GenesysGenCoronaGlow(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_env_map_glows_0xb8', None)

        @property
        def inst_rear_view_mirror_glows_0xc4(self):
            if hasattr(self, '_m_inst_rear_view_mirror_glows_0xc4'):
                return self._m_inst_rear_view_mirror_glows_0xc4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_rear_view_mirror_glows_0xc4)
            self._m_inst_rear_view_mirror_glows_0xc4 = []
            for i in range(self.array_count_for_0xc4):
                self._m_inst_rear_view_mirror_glows_0xc4.append(AnyGenesysObj.GenesysGenCoronaGlow(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_rear_view_mirror_glows_0xc4', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1234658497
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParameters(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.traffic_oncoming_0xc = AnyGenesysObj.GenesysGenNitrousParametersTrafficOncoming(self._io, self, self._root)
            self.balancing_0x34 = AnyGenesysObj.GenesysGenNitrousParametersBalancing(self._io, self, self._root)
            self.donutting_0x58 = AnyGenesysObj.GenesysGenNitrousParametersDonutting(self._io, self, self._root)
            self.drifting_0x7c = AnyGenesysObj.GenesysGenNitrousParametersDrifting(self._io, self, self._root)
            self.hitting_another_competitor_0xa0 = AnyGenesysObj.GenesysGenNitrousParametersHittingAnotherCompetitor(self._io, self, self._root)
            self.punch_0xc4 = AnyGenesysObj.GenesysGenNitrousParametersPunchUsage(self._io, self, self._root)
            self.slip_streaming_0xe8 = AnyGenesysObj.GenesysGenNitrousParametersSlipstreaming(self._io, self, self._root)
            self.catching_air_0x10c = AnyGenesysObj.GenesysGenNitrousParametersCatchingAir(self._io, self, self._root)
            self.crash_escape_0x12c = AnyGenesysObj.GenesysGenNitrousParametersCrashEscape(self._io, self, self._root)
            self.driving_at_high_speed_0x14c = AnyGenesysObj.GenesysGenNitrousParametersHighSpeed(self._io, self, self._root)
            self.driving_at_speed_0x16c = AnyGenesysObj.GenesysGenNitrousParametersMinSpeed(self._io, self, self._root)
            self.nitrous_0x18c = AnyGenesysObj.GenesysGenNitrousParametersNitrousUsage(self._io, self, self._root)
            self.taking_shortcut_0x1ac = AnyGenesysObj.GenesysGenNitrousParametersTakingShortcut(self._io, self, self._root)
            self.traffic_near_miss_0x1cc = AnyGenesysObj.GenesysGenNitrousParametersTrafficNearMiss(self._io, self, self._root)
            self.traffic_near_miss_oncoming_0x1ec = AnyGenesysObj.GenesysGenNitrousParametersTrafficNearMiss(self._io, self, self._root)
            self.fatal_hit_0x20c = AnyGenesysObj.GenesysGenNitrousParametersFatalHit(self._io, self, self._root)
            self.jump_0x228 = AnyGenesysObj.GenesysGenNitrousParametersJumpUsage(self._io, self, self._root)
            self.shared_0x244 = AnyGenesysObj.GenesysGenNitrousParametersRestrictions(self._io, self, self._root)
            self.genesys__gen__nitrous_parameters__speedbreaker_usage_0x260 = AnyGenesysObj.GenesysGenNitrousParametersSpeedbreakerUsage(self._io, self, self._root)
            self.game_changer_id_0x27c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 644
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 855876020
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersJumpUsage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenNitrousParametersUsage(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 935932605
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenUilistItems(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_items_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_items_0x10(self):
            if hasattr(self, '_m_inst_items_0x10'):
                return self._m_inst_items_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_items_0x10)
            self._m_inst_items_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_items_0x10.append(AnyGenesysObj.GenesysGenUilistItemsItem(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_items_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2626560424
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayBlacklistShutdownDataDamageThreshold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.damage_value_0xc = self._io.read_f4le()
            self.ptr_arr_speed_control_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_speed_control_0x10(self):
            if hasattr(self, '_m_inst_speed_control_0x10'):
                return self._m_inst_speed_control_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_speed_control_0x10)
            self._m_inst_speed_control_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_speed_control_0x10.append(AnyGenesysObj.GenesysGenGameplayBlacklistShutdownDataDamageThresholdSpeedControl(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_speed_control_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3736686144
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionInfoPayloadDamage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_genesys__gen__collision_info_damage_profile_0xc = self._io.read_u4le()
            self.ptr_self_inflicted_0x10 = self._io.read_u4le()

        @property
        def inst_genesys__gen__collision_info_damage_profile_0xc(self):
            if hasattr(self, '_m_inst_genesys__gen__collision_info_damage_profile_0xc'):
                return self._m_inst_genesys__gen__collision_info_damage_profile_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__collision_info_damage_profile_0xc)
            self._m_inst_genesys__gen__collision_info_damage_profile_0xc = AnyGenesysObj.GenesysGenCollisionInfoDamageProfile(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__collision_info_damage_profile_0xc', None)

        @property
        def inst_self_inflicted_0x10(self):
            if hasattr(self, '_m_inst_self_inflicted_0x10'):
                return self._m_inst_self_inflicted_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_self_inflicted_0x10)
            self._m_inst_self_inflicted_0x10 = AnyGenesysObj.GenesysGenCollisionInfoDamageProfile(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_self_inflicted_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 456234940
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenLightCone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenLightBase(self._io, self, self._root)
            self.float32_t_0x60 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 104
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3989427985
            return getattr(self, '_m_mu_version_hash', None)


    class RwMathVpuVector4(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.inline_arr_elements_0x0 = []
            for i in range(4):
                self.inline_arr_elements_0x0.append(self._io.read_f4le())


        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 8
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3257509935
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersMinSpeed(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.minimum_speed_0x14 = self._io.read_f4le()
            self.nitrous_reward_0x18 = self._io.read_f4le()
            self.is_enabled_0x1c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3789082911
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenImpactDamageGraphsGraph(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.maximum_closing_velocity_mph_0xc = self._io.read_f4le()
            self.maximum_velocity_damage_0x10 = self._io.read_f4le()
            self.medium_closing_velocity_mph_0x14 = self._io.read_f4le()
            self.medium_velocity_damage_0x18 = self._io.read_f4le()
            self.minimum_closing_velocity_mph_0x1c = self._io.read_f4le()
            self.minimum_velocity_damage_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1703771469
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeChallengePart(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__unique_id_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.instruction_0x14 = self._io.read_u4le()
            self.cgs_core__unique_id_0x18 = self._io.read_u4le()
            self.short_instruction_0x1c = self._io.read_u4le()
            self.ptr_arr_ptr_actions_0x20 = self._io.read_u4le()
            self.unk_enum_0x24 = self._io.read_u2le()
            self.unk_enum_0x26 = self._io.read_u2le()
            self.uint16_t_0x28 = self._io.read_u2le()
            self.bool8_t_0x2a = self._io.read_u1()
            self.array_count_for_0x20 = self._io.read_u1()

        @property
        def inst_actions_0x20(self):
            if hasattr(self, '_m_inst_actions_0x20'):
                return self._m_inst_actions_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_actions_0x20)
            self._m_inst_actions_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_actions_0x20.append(AnyGenesysObj.Ptr(u"genesys__gen__challenge_action__action_base", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_actions_0x20', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3591252192
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOnlineRoute(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_arr_checkpoints_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_checkpoints_0xc(self):
            if hasattr(self, '_m_inst_checkpoints_0xc'):
                return self._m_inst_checkpoints_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_checkpoints_0xc)
            self._m_inst_checkpoints_0xc = []
            for i in range(self.array_count_for_0xc):
                self._m_inst_checkpoints_0xc.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_checkpoints_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 202861526
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersBalancing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.close_burn_rate_0xc = self._io.read_f4le()
            self.close_multiplier_0x10 = self._io.read_f4le()
            self.far_burn_rate_0x14 = self._io.read_f4le()
            self.far_multiplier_0x18 = self._io.read_f4le()
            self.max_distance_0x1c = self._io.read_f4le()
            self.slipstream_distance_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4081022393
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenBandPassDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            self.frequency_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3794314553
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionAccumulationHelperData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.target_0x10 = self._io.read_u4le()
            self.operator_0x14 = self._io.read_u2le()
            self.bool8_t_0x16 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4093540154
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineMixerChannelGainModification(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.mixer__channel_0xc = self._io.read_bytes(8)
            self.gain_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2361784635
            return getattr(self, '_m_mu_version_hash', None)


    class CgsResourceHandle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenCollisionInfoBattlingEffectExtraRollParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.damage__for__full__extra__roll_0xc = self._io.read_f4le()
            self.damage__for__no__extra__roll_0x10 = self._io.read_f4le()
            self.extra__limit__duration_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3691704753
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWheelSizes(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2321043106
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionGetToLocation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.route_location_0x4c = self._io.read_u1()
            self.bool8_t_0x4d = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 80
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3014928914
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHardDrivingBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__hard_driving_behaviour__gas_effect_0xc = AnyGenesysObj.GenesysGenHardDrivingBehaviourGasEffect(self._io, self, self._root)
            self.genesys__gen__hard_driving_behaviour__steering_effect_0x4c = AnyGenesysObj.GenesysGenHardDrivingBehaviourSteeringEffect(self._io, self, self._root)
            self.game_changer_id_0x60 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 104
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3500617746
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleGameplay(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__vehicle__gameplay__damage_stats_0xc = AnyGenesysObj.GenesysGenVehicleGameplayDamageStats(self._io, self, self._root)
            self.genesys__gen__vehicle__gameplay__damage_stats_0x28 = AnyGenesysObj.GenesysGenVehicleGameplayDamageStats(self._io, self, self._root)
            self.id_0nkx_0x44 = AnyGenesysObj.GenesysGenVehicleGameplayDamageStats(self._io, self, self._root)
            self.genesys__gen__vehicle__gameplay__tyre_trails_0x60 = AnyGenesysObj.GenesysGenVehicleGameplayTyreTrails(self._io, self, self._root)
            self.cgs_resource__handle_0x74 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x7c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x84 = self._io.read_bytes(8)
            self.cgs_core__unique_id_0x8c = self._io.read_u4le()
            self.game_changer_id_0x90 = self._io.read_u4le()
            self.cgs_core__unique_id_0x94 = self._io.read_u4le()
            self.cgs_core__unique_id_0x98 = self._io.read_u4le()
            self.cgs_core__unique_id_0x9c = self._io.read_u4le()
            self.cgs_core__unique_id_0xa0 = self._io.read_u4le()
            self.cgs_core__unique_id_0xa4 = self._io.read_u4le()
            self.cgs_core__unique_id_0xa8 = self._io.read_u4le()
            self.float32_t_0xac = self._io.read_f4le()
            self.ptr_genesys__gen__pidcontroller_0xb0 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb4 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb8 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xbc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc0 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc4 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc8 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xcc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd0 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd4 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd8 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xdc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe0 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe4 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe8 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xec = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf0 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf4 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf8 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xfc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x100 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x104 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x108 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x10c = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x110 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x114 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x118 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x11c = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x120 = self._io.read_u4le()
            self.array_count_for_0xb4 = self._io.read_u1()
            self.array_count_for_0xb8 = self._io.read_u1()
            self.array_count_for_0xbc = self._io.read_u1()
            self.array_count_for_0xc0 = self._io.read_u1()
            self.array_count_for_0xc4 = self._io.read_u1()
            self.array_count_for_0xc8 = self._io.read_u1()
            self.array_count_for_0xcc = self._io.read_u1()
            self.array_count_for_0xd0 = self._io.read_u1()
            self.array_count_for_0xd4 = self._io.read_u1()
            self.array_count_for_0xd8 = self._io.read_u1()
            self.array_count_for_0xdc = self._io.read_u1()
            self.array_count_for_0xe0 = self._io.read_u1()
            self.array_count_for_0xe4 = self._io.read_u1()
            self.array_count_for_0xe8 = self._io.read_u1()
            self.array_count_for_0xec = self._io.read_u1()
            self.array_count_for_0xf0 = self._io.read_u1()
            self.array_count_for_0xf4 = self._io.read_u1()
            self.array_count_for_0xf8 = self._io.read_u1()
            self.array_count_for_0xfc = self._io.read_u1()
            self.array_count_for_0x100 = self._io.read_u1()
            self.array_count_for_0x104 = self._io.read_u1()
            self.array_count_for_0x108 = self._io.read_u1()
            self.array_count_for_0x10c = self._io.read_u1()
            self.array_count_for_0x110 = self._io.read_u1()
            self.array_count_for_0x114 = self._io.read_u1()
            self.array_count_for_0x118 = self._io.read_u1()
            self.array_count_for_0x11c = self._io.read_u1()
            self.array_count_for_0x120 = self._io.read_u1()
            self.uint8_t_0x140 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xf8(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf8'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf8)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf8 = []
            for i in range(self.array_count_for_0xf8):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf8.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf8', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0x10c(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x10c'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x10c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x10c)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x10c = []
            for i in range(self.array_count_for_0x10c):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x10c.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x10c', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xf0(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf0'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf0)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf0 = []
            for i in range(self.array_count_for_0xf0):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf0.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf0', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xc4(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc4'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc4)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc4 = []
            for i in range(self.array_count_for_0xc4):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc4.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc4', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0x11c(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x11c'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x11c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x11c)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x11c = []
            for i in range(self.array_count_for_0x11c):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x11c.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x11c', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xf4(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf4'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xf4)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf4 = []
            for i in range(self.array_count_for_0xf4):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf4.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xf4', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xd4(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd4'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd4)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd4 = []
            for i in range(self.array_count_for_0xd4):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd4.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd4', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0x114(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x114'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x114

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x114)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x114 = []
            for i in range(self.array_count_for_0x114):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x114.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x114', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xcc(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xcc'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xcc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xcc)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xcc = []
            for i in range(self.array_count_for_0xcc):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xcc.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xcc', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xdc(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xdc'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xdc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xdc)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xdc = []
            for i in range(self.array_count_for_0xdc):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xdc.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xdc', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0x104(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x104'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x104

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x104)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x104 = []
            for i in range(self.array_count_for_0x104):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x104.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x104', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xc8(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc8'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc8)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc8 = []
            for i in range(self.array_count_for_0xc8):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc8.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc8', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 324
            return getattr(self, '_m_size', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xb8(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb8'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb8)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb8 = []
            for i in range(self.array_count_for_0xb8):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb8.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb8', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0x108(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x108'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x108

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x108)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x108 = []
            for i in range(self.array_count_for_0x108):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x108.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x108', None)

        @property
        def inst_genesys__gen__pidcontroller_0xb0(self):
            if hasattr(self, '_m_inst_genesys__gen__pidcontroller_0xb0'):
                return self._m_inst_genesys__gen__pidcontroller_0xb0

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__pidcontroller_0xb0)
            self._m_inst_genesys__gen__pidcontroller_0xb0 = AnyGenesysObj.GenesysGenPidcontroller(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__pidcontroller_0xb0', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xd8(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd8'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd8)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd8 = []
            for i in range(self.array_count_for_0xd8):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd8.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd8', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0x118(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x118'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x118

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x118)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x118 = []
            for i in range(self.array_count_for_0x118):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x118.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x118', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0x110(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x110'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x110

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x110)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x110 = []
            for i in range(self.array_count_for_0x110):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x110.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x110', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xd0(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd0'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xd0)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd0 = []
            for i in range(self.array_count_for_0xd0):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd0.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xd0', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xec(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xec'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xec

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xec)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xec = []
            for i in range(self.array_count_for_0xec):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xec.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xec', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xbc(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xbc'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xbc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xbc)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xbc = []
            for i in range(self.array_count_for_0xbc):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xbc.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xbc', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0x120(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x120'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x120

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x120)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x120 = []
            for i in range(self.array_count_for_0x120):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x120.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x120', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xfc(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xfc'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xfc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xfc)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xfc = []
            for i in range(self.array_count_for_0xfc):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xfc.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xfc', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xe4(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe4'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe4)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe4 = []
            for i in range(self.array_count_for_0xe4):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe4.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe4', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xc0(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc0'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xc0)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc0 = []
            for i in range(self.array_count_for_0xc0):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc0.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xc0', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0x100(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x100'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x100

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0x100)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x100 = []
            for i in range(self.array_count_for_0x100):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x100.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0x100', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xb4(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb4'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xb4)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb4 = []
            for i in range(self.array_count_for_0xb4):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb4.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xb4', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xe0(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe0'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe0)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe0 = []
            for i in range(self.array_count_for_0xe0):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe0.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe0', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 520558439
            return getattr(self, '_m_mu_version_hash', None)

        @property
        def inst_genesys__gen__vehicle__gameplay__mod_effect_0xe8(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe8'):
                return self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__gameplay__mod_effect_0xe8)
            self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe8 = []
            for i in range(self.array_count_for_0xe8):
                self._m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe8.append(AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__gameplay__mod_effect_0xe8', None)


    class GenesysGenRaceBalancingDataOpponentBalancingData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ahead_distance_0x10 = self._io.read_f4le()
            self.behind_distance_0x14 = self._io.read_f4le()
            self.end_cutoff_ratio_0x18 = self._io.read_f4le()
            self.end_speed_value_ahead_0x1c = self._io.read_f4le()
            self.end_speed_value_behind_0x20 = self._io.read_f4le()
            self.start_cutoff_ratio_0x24 = self._io.read_f4le()
            self.start_speed_value_ahead_0x28 = self._io.read_f4le()
            self.start_speed_value_behind_0x2c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1273350923
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayGradientAdjustmentsParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 397117973
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayBonnetWindSound(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.cgs_core__unique_id_0x10 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3274903722
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSteeringBehaviourSteeringAngleCurve(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3935354064
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHighPassButterworthDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            self.order_0x18 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1110789791
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyConvexHullVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.convex_hull_0x50 = self._io.read_bytes(8)
            self.game_changer_id_0x58 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1664340785
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleDamageBehaviourBodypartDamageThreshold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.damage_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1476111906
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.body_to_object_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.com_offset_0x50 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.inertia__scale_0x60 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.local_aabbcenter_0x70 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.local_aabbhalf_diagonal_0x80 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.ptr_arr_symmetrical_in_axis_0x90 = self._io.read_u4le()
            self.game_changer_id_0x94 = self._io.read_u4le()
            self.angular_drag_0x98 = self._io.read_f4le()
            self.bounciness_0x9c = self._io.read_f4le()
            self.friction_0xa0 = self._io.read_f4le()
            self.linear_drag_0xa4 = self._io.read_f4le()
            self.mass_0xa8 = self._io.read_f4le()
            self.ptr_arr_box_volumes_0xac = self._io.read_u4le()
            self.ptr_arr_capsule_volumes_0xb0 = self._io.read_u4le()
            self.ptr_bounding_convex_hull_0xb4 = self._io.read_u4le()
            self.ptr_arr_convex_hull_volumes_0xb8 = self._io.read_u4le()
            self.ptr_arr_cylinder_volumes_0xbc = self._io.read_u4le()
            self.ptr_arr_sphere_volumes_0xc0 = self._io.read_u4le()
            self.array_count_for_0xac = self._io.read_u2le()
            self.array_count_for_0xb0 = self._io.read_u2le()
            self.array_count_for_0xb8 = self._io.read_u2le()
            self.array_count_for_0xbc = self._io.read_u2le()
            self.array_count_for_0xc0 = self._io.read_u2le()
            self.array_count_for_0x90 = self._io.read_u2le()
            self.is_wheel_0xd0 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_capsule_volumes_0xb0(self):
            if hasattr(self, '_m_inst_capsule_volumes_0xb0'):
                return self._m_inst_capsule_volumes_0xb0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_capsule_volumes_0xb0)
            self._m_inst_capsule_volumes_0xb0 = []
            for i in range(self.array_count_for_0xb0):
                self._m_inst_capsule_volumes_0xb0.append(AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyCapsuleVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_capsule_volumes_0xb0', None)

        @property
        def inst_box_volumes_0xac(self):
            if hasattr(self, '_m_inst_box_volumes_0xac'):
                return self._m_inst_box_volumes_0xac

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_box_volumes_0xac)
            self._m_inst_box_volumes_0xac = []
            for i in range(self.array_count_for_0xac):
                self._m_inst_box_volumes_0xac.append(AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyBoxVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_box_volumes_0xac', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 212
            return getattr(self, '_m_size', None)

        @property
        def inst_bounding_convex_hull_0xb4(self):
            if hasattr(self, '_m_inst_bounding_convex_hull_0xb4'):
                return self._m_inst_bounding_convex_hull_0xb4

            _pos = self._io.pos()
            self._io.seek(self.ptr_bounding_convex_hull_0xb4)
            self._m_inst_bounding_convex_hull_0xb4 = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyConvexHullVolume(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_bounding_convex_hull_0xb4', None)

        @property
        def inst_sphere_volumes_0xc0(self):
            if hasattr(self, '_m_inst_sphere_volumes_0xc0'):
                return self._m_inst_sphere_volumes_0xc0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_sphere_volumes_0xc0)
            self._m_inst_sphere_volumes_0xc0 = []
            for i in range(self.array_count_for_0xc0):
                self._m_inst_sphere_volumes_0xc0.append(AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodySphereVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_sphere_volumes_0xc0', None)

        @property
        def inst_symmetrical_in_axis_0x90(self):
            if hasattr(self, '_m_inst_symmetrical_in_axis_0x90'):
                return self._m_inst_symmetrical_in_axis_0x90

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_symmetrical_in_axis_0x90)
            self._m_inst_symmetrical_in_axis_0x90 = []
            for i in range(self.array_count_for_0x90):
                self._m_inst_symmetrical_in_axis_0x90.append(self._io.read_u1())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_symmetrical_in_axis_0x90', None)

        @property
        def inst_cylinder_volumes_0xbc(self):
            if hasattr(self, '_m_inst_cylinder_volumes_0xbc'):
                return self._m_inst_cylinder_volumes_0xbc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cylinder_volumes_0xbc)
            self._m_inst_cylinder_volumes_0xbc = []
            for i in range(self.array_count_for_0xbc):
                self._m_inst_cylinder_volumes_0xbc.append(AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyCylinderVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cylinder_volumes_0xbc', None)

        @property
        def inst_convex_hull_volumes_0xb8(self):
            if hasattr(self, '_m_inst_convex_hull_volumes_0xb8'):
                return self._m_inst_convex_hull_volumes_0xb8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_convex_hull_volumes_0xb8)
            self._m_inst_convex_hull_volumes_0xb8 = []
            for i in range(self.array_count_for_0xb8):
                self._m_inst_convex_hull_volumes_0xb8.append(AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyConvexHullVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_convex_hull_volumes_0xb8', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1567458252
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionDoJump(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.accumulate_0x4c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 80
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1667642657
            return getattr(self, '_m_mu_version_hash', None)


    class Bool8T(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenPhysicsLandingDamagePitch(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.max_damage_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1517189091
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicalDefinitionRigidBodyCylinderVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.game_changer_id_0x50 = self._io.read_u4le()
            self.half_length_0x54 = self._io.read_f4le()
            self.radius_0x58 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 18021398
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersDrifting(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.minimum_speed_0x14 = self._io.read_f4le()
            self.nitrous_reward_0x18 = self._io.read_f4le()
            self.time_drifting_0x1c = self._io.read_f4le()
            self.is_enabled_0x20 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2207259302
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenLowPassButterworthDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            self.order_0x18 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4000215473
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPostFxstateValueModifier(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.modification__value_0x10 = self._io.read_f4le()
            self.modification__type_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4120564202
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleSurfaceProfile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle_surface_profile__surface_link_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_genesys__gen__vehicle_surface_profile__surface_link_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_surface_profile__surface_link_0x10'):
                return self._m_inst_genesys__gen__vehicle_surface_profile__surface_link_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle_surface_profile__surface_link_0x10)
            self._m_inst_genesys__gen__vehicle_surface_profile__surface_link_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_genesys__gen__vehicle_surface_profile__surface_link_0x10.append(AnyGenesysObj.GenesysGenVehicleSurfaceProfileSurfaceLink(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_surface_profile__surface_link_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3049882700
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWcvfxBehaviourCoronas(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.corona_definition_0xc = self._io.read_bytes(8)
            self.locator_group_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 477429240
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarEffectSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.ptr_arr_automated__values_0x2c = self._io.read_u4le()
            self.array_count_for_0x2c = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_automated__values_0x2c(self):
            if hasattr(self, '_m_inst_automated__values_0x2c'):
                return self._m_inst_automated__values_0x2c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_automated__values_0x2c)
            self._m_inst_automated__values_0x2c = []
            for i in range(self.array_count_for_0x2c):
                self._m_inst_automated__values_0x2c.append(AnyGenesysObj.GenesysGenRaceCarEffectSequenceItemEffectDoubleValue(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_automated__values_0x2c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 166370211
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameMode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.maps_acceptors_0xc = self._io.read_u4le()
            self.cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.description_0x14 = self._io.read_u4le()
            self.game_changer_id_0x18 = self._io.read_u4le()
            self.hsm_0x1c = self._io.read_u4le()
            self.hud__hsm_0x20 = self._io.read_u4le()
            self.intro_0x24 = self._io.read_u4le()
            self.mix_snap_shot_0x28 = self._io.read_u4le()
            self.cgs_core__unique_id_0x2c = self._io.read_u4le()
            self.name_0x30 = self._io.read_u4le()
            self.results_sequence_0x34 = self._io.read_u4le()
            self.score_view_model_0x38 = self._io.read_u4le()
            self.cgs_core__unique_id_0x3c = self._io.read_u4le()
            self.weapon_list_0x40 = self._io.read_u4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.mode_intro_time_limit_0x48 = self._io.read_f4le()
            self.mode_time_limit_0x4c = self._io.read_f4le()
            self.timeout_time_0x50 = self._io.read_f4le()
            self.on_bust_0x54 = self._io.read_u2le()
            self.ranking_type_0x56 = self._io.read_u2le()
            self.unk_enum_0x58 = self._io.read_u2le()
            self.intercepting_cop_frequency_0x5a = self._io.read_u2le()
            self.minimap_distance_0x5c = self._io.read_u2le()
            self.mode_score_limit_0x5e = self._io.read_u2le()
            self.oncoming_cop_frequency_0x60 = self._io.read_u2le()
            self.trailing_cop_frequency_0x62 = self._io.read_u2le()
            self.uint16_t_0x64 = self._io.read_u2le()
            self.allow_airacer_damage_from_world_0x66 = self._io.read_u1()
            self.allow_friendly_fire_0x67 = self._io.read_u1()
            self.bool8_t_0x68 = self._io.read_u1()
            self.bool8_t_0x69 = self._io.read_u1()
            self.host_can_end_game_0x6a = self._io.read_u1()
            self.online_0x6b = self._io.read_u1()
            self.retry_enabled_0x6c = self._io.read_u1()
            self.bool8_t_0x6d = self._io.read_u1()
            self.show_checkpoints_0x6e = self._io.read_u1()
            self.bool8_t_0x6f = self._io.read_u1()
            self.spawn_towards_ai_0x70 = self._io.read_u1()
            self.team_game_0x71 = self._io.read_u1()
            self.timer_counts_up_0x72 = self._io.read_u1()
            self.bool8_t_0x73 = self._io.read_u1()
            self.bool8_t_0x74 = self._io.read_u1()
            self.feedback_group_id_0x75 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 120
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2658850274
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEventArena(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.image_0x10 = self._io.read_u4le()
            self.map_0x14 = self._io.read_u4le()
            self.name_0x18 = self._io.read_u4le()
            self.world_0x1c = self._io.read_u4le()
            self.ptr_arena_data_0x20 = self._io.read_u4le()

        @property
        def inst_arena_data_0x20(self):
            if hasattr(self, '_m_inst_arena_data_0x20'):
                return self._m_inst_arena_data_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arena_data_0x20)
            self._m_inst_arena_data_0x20 = AnyGenesysObj.GenesysGenEventArenaData(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_arena_data_0x20', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4102322433
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalSpeedBasedHeightChange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3108376025
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarPlayerVsTrafficDamageParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.damage_0x14 = self._io.read_f4le()
            self.linear__solve_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2169124928
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersTrafficOncoming(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.minimum_speed_0x14 = self._io.read_f4le()
            self.minimum_time_0x18 = self._io.read_f4le()
            self.nitrous_reward_0x1c = self._io.read_f4le()
            self.oncoming_timeout_0x20 = self._io.read_f4le()
            self.is_enabled_0x24 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2600271809
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGamePack(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.name_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.car_pack_image_0x14 = self._io.read_u4le()
            self.display_name_0x18 = self._io.read_u4le()
            self.game_changer_id_0x1c = self._io.read_u4le()
            self.cgs_core__unique_id_0x20 = self._io.read_u4le()
            self.show_pack_on_entitlement_0x24 = self._io.read_u4le()
            self.release_0x28 = self._io.read_u2le()
            self.display_purchase_0x2a = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 793749252
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenBodyMovementBehaviourTakeOffBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 72
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1129268118
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRoadBlockDefinition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_arr_back_layers_0xc = self._io.read_u4le()
            self.ptr_arr_front_layers_0x10 = self._io.read_u4le()
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.ptr_arr_cgs_core__unique_id_0x18 = self._io.read_u4le()
            self.primary_layer_0x1c = self._io.read_u4le()
            self.sequence_0x20 = self._io.read_u4le()
            self.layer_distance_0x24 = self._io.read_f4le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_back_layers_0xc(self):
            if hasattr(self, '_m_inst_back_layers_0xc'):
                return self._m_inst_back_layers_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_back_layers_0xc)
            self._m_inst_back_layers_0xc = []
            for i in range(self.array_count_for_0xc):
                self._m_inst_back_layers_0xc.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_back_layers_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def inst_cgs_core__unique_id_0x18(self):
            if hasattr(self, '_m_inst_cgs_core__unique_id_0x18'):
                return self._m_inst_cgs_core__unique_id_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_core__unique_id_0x18)
            self._m_inst_cgs_core__unique_id_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_cgs_core__unique_id_0x18.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_core__unique_id_0x18', None)

        @property
        def inst_front_layers_0x10(self):
            if hasattr(self, '_m_inst_front_layers_0x10'):
                return self._m_inst_front_layers_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_front_layers_0x10)
            self._m_inst_front_layers_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_front_layers_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_front_layers_0x10', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2488860623
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWheelSuspensionSpringConstraint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.bool8_t_0x24 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 736842216
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.roadblock_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c = self._io.read_u4le()
            self.array_count_for_0x1c = self._io.read_u2le()
            self.spawn_cops_0x22 = self._io.read_u1()
            self.middleton_datagram_0x23 = self._io.read_u1()

        @property
        def inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c(self):
            if hasattr(self, '_m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c'):
                return self._m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c)
            self._m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c.append(AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour_0x1c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1558321222
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPassbySequenceBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.cgs_resource__handle_0x1c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x24 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x2c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x34 = self._io.read_bytes(8)
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.float32_t_0x4c = self._io.read_f4le()
            self.float32_t_0x50 = self._io.read_f4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.float32_t_0x58 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3085849010
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionCoopAccumulateDistance(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2039183453
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGinsuDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 231346471
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionEffectsTrafficEffectExtraRollParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1807127390
            return getattr(self, '_m_mu_version_hash', None)


    class PtrPtr(KaitaiStruct):
        def __init__(self, dtype, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.dtype = dtype
            self._read()

        def _read(self):
            self.offset = self._io.read_s4le()

        @property
        def ptr(self):
            if hasattr(self, '_m_ptr'):
                return self._m_ptr

            if self.offset != 0:
                _pos = self._io.pos()
                self._io.seek(self.offset)
                self._m_ptr = AnyGenesysObj.Ptr(self.dtype, self._io, self, self._root)
                self._io.seek(_pos)

            return getattr(self, '_m_ptr', None)


    class GenesysGenPhysicalDefinitionRigidBody(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.body_to_object_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.com_offset_0x50 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.inertia__scale_0x60 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.local_aabbcenter_0x70 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.local_aabbhalf_diagonal_0x80 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.ptr_arr_symmetrical_in_axis_0x90 = self._io.read_u4le()
            self.game_changer_id_0x94 = self._io.read_u4le()
            self.angular_drag_0x98 = self._io.read_f4le()
            self.bounciness_0x9c = self._io.read_f4le()
            self.friction_0xa0 = self._io.read_f4le()
            self.linear_drag_0xa4 = self._io.read_f4le()
            self.mass_0xa8 = self._io.read_f4le()
            self.ptr_arr_box_volumes_0xac = self._io.read_u4le()
            self.ptr_arr_capsule_volumes_0xb0 = self._io.read_u4le()
            self.ptr_bounding_convex_hull_0xb4 = self._io.read_u4le()
            self.ptr_arr_convex_hull_volumes_0xb8 = self._io.read_u4le()
            self.ptr_arr_cylinder_volumes_0xbc = self._io.read_u4le()
            self.ptr_arr_sphere_volumes_0xc0 = self._io.read_u4le()
            self.array_count_for_0xac = self._io.read_u2le()
            self.array_count_for_0xb0 = self._io.read_u2le()
            self.array_count_for_0xb8 = self._io.read_u2le()
            self.array_count_for_0xbc = self._io.read_u2le()
            self.array_count_for_0xc0 = self._io.read_u2le()
            self.array_count_for_0x90 = self._io.read_u2le()
            self.is_wheel_0xd0 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_capsule_volumes_0xb0(self):
            if hasattr(self, '_m_inst_capsule_volumes_0xb0'):
                return self._m_inst_capsule_volumes_0xb0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_capsule_volumes_0xb0)
            self._m_inst_capsule_volumes_0xb0 = []
            for i in range(self.array_count_for_0xb0):
                self._m_inst_capsule_volumes_0xb0.append(AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodyCapsuleVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_capsule_volumes_0xb0', None)

        @property
        def inst_box_volumes_0xac(self):
            if hasattr(self, '_m_inst_box_volumes_0xac'):
                return self._m_inst_box_volumes_0xac

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_box_volumes_0xac)
            self._m_inst_box_volumes_0xac = []
            for i in range(self.array_count_for_0xac):
                self._m_inst_box_volumes_0xac.append(AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodyBoxVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_box_volumes_0xac', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 212
            return getattr(self, '_m_size', None)

        @property
        def inst_bounding_convex_hull_0xb4(self):
            if hasattr(self, '_m_inst_bounding_convex_hull_0xb4'):
                return self._m_inst_bounding_convex_hull_0xb4

            _pos = self._io.pos()
            self._io.seek(self.ptr_bounding_convex_hull_0xb4)
            self._m_inst_bounding_convex_hull_0xb4 = AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_bounding_convex_hull_0xb4', None)

        @property
        def inst_sphere_volumes_0xc0(self):
            if hasattr(self, '_m_inst_sphere_volumes_0xc0'):
                return self._m_inst_sphere_volumes_0xc0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_sphere_volumes_0xc0)
            self._m_inst_sphere_volumes_0xc0 = []
            for i in range(self.array_count_for_0xc0):
                self._m_inst_sphere_volumes_0xc0.append(AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodySphereVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_sphere_volumes_0xc0', None)

        @property
        def inst_symmetrical_in_axis_0x90(self):
            if hasattr(self, '_m_inst_symmetrical_in_axis_0x90'):
                return self._m_inst_symmetrical_in_axis_0x90

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_symmetrical_in_axis_0x90)
            self._m_inst_symmetrical_in_axis_0x90 = []
            for i in range(self.array_count_for_0x90):
                self._m_inst_symmetrical_in_axis_0x90.append(self._io.read_u1())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_symmetrical_in_axis_0x90', None)

        @property
        def inst_cylinder_volumes_0xbc(self):
            if hasattr(self, '_m_inst_cylinder_volumes_0xbc'):
                return self._m_inst_cylinder_volumes_0xbc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cylinder_volumes_0xbc)
            self._m_inst_cylinder_volumes_0xbc = []
            for i in range(self.array_count_for_0xbc):
                self._m_inst_cylinder_volumes_0xbc.append(AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cylinder_volumes_0xbc', None)

        @property
        def inst_convex_hull_volumes_0xb8(self):
            if hasattr(self, '_m_inst_convex_hull_volumes_0xb8'):
                return self._m_inst_convex_hull_volumes_0xb8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_convex_hull_volumes_0xb8)
            self._m_inst_convex_hull_volumes_0xb8 = []
            for i in range(self.array_count_for_0xb8):
                self._m_inst_convex_hull_volumes_0xb8.append(AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_convex_hull_volumes_0xb8', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1567458252
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleVfxBehaviourLight(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.colour_0x10 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.cgs_resource__handle_0x20 = self._io.read_bytes(8)
            self.light_definition_0x28 = self._io.read_bytes(8)
            self.locator_group_0x30 = self._io.read_u4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.unk_enum_0x38 = self._io.read_u2le()
            self.time_of_day_0x3a = self._io.read_u2le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 64
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 123660642
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayAllowedVehicleListVehicleAndMods(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.vehicle_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.ptr_arr_mods_0x14 = self._io.read_u4le()
            self.inline_arr_target_scores_0x18 = []
            for i in range(3):
                self.inline_arr_target_scores_0x18.append(self._io.read_s2le())

            self.inline_arr_target_speeds_0x1e = []
            for i in range(3):
                self.inline_arr_target_speeds_0x1e.append(self._io.read_s2le())

            self.array_count_for_0x14 = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.array_count_for_0x1e = self._io.read_u2le()
            self.difficulty_0x2a = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def inst_mods_0x14(self):
            if hasattr(self, '_m_inst_mods_0x14'):
                return self._m_inst_mods_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_mods_0x14)
            self._m_inst_mods_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_mods_0x14.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_mods_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 956776100
            return getattr(self, '_m_mu_version_hash', None)


    class Int16T(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenDynamicAdditionalInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.sequence_0xc = self._io.read_bytes(8)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.strength_0x20 = self._io.read_f4le()
            self.score_0x24 = self._io.read_u2le()
            self.bool8_t_0x26 = self._io.read_u1()
            self.bool8_t_0x27 = self._io.read_u1()
            self.bool8_t_0x28 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2950917875
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayMilestoneEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.award_0xc = self._io.read_u4le()
            self.value_0x10 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2921338515
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineDifferentials(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 709116355
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineSound2DspParamWrapper(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_genesys__gen__engine_sound2__dsp_param_0xc = self._io.read_u4le()

        @property
        def inst_genesys__gen__engine_sound2__dsp_param_0xc(self):
            if hasattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_0xc'):
                return self._m_inst_genesys__gen__engine_sound2__dsp_param_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__engine_sound2__dsp_param_0xc)
            self._m_inst_genesys__gen__engine_sound2__dsp_param_0xc = AnyGenesysObj.GenesysGenEngineSound2DspParam(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2477895213
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEventList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_ordered_list_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_ordered_list_0x10(self):
            if hasattr(self, '_m_inst_ordered_list_0x10'):
                return self._m_inst_ordered_list_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ordered_list_0x10)
            self._m_inst_ordered_list_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_ordered_list_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_ordered_list_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 981367156
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionInfoBattlingEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ai__extra__roll_0xc = AnyGenesysObj.GenesysGenCollisionInfoBattlingEffectExtraRollParams(self._io, self, self._root)
            self.player__extra__roll_0x24 = AnyGenesysObj.GenesysGenCollisionInfoBattlingEffectExtraRollParams(self._io, self, self._root)
            self.cam__effect_0x3c = self._io.read_bytes(8)
            self.cam__effect__scale_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 80
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1886238258
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreVfxBehaviourFrontRearParamsSkidMarkParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params_0xc = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLatParams(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x3c = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLongParams(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x64 = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLongParams(self._io, self, self._root)
            self.game_changer_id_0x8c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 148
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3530258211
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineMix(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.engine_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.pops_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1901399892
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclesSoundTransmissionWhine(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_sequences_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_sequences_0x10(self):
            if hasattr(self, '_m_inst_sequences_0x10'):
                return self._m_inst_sequences_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_sequences_0x10)
            self._m_inst_sequences_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_sequences_0x10.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_sequences_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 618870438
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousStrengthPunch(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4084465158
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSteeringBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.float32_t_0x4c = self._io.read_f4le()
            self.float32_t_0x50 = self._io.read_f4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.float32_t_0x58 = self._io.read_f4le()
            self.float32_t_0x5c = self._io.read_f4le()
            self.float32_t_0x60 = self._io.read_f4le()
            self.float32_t_0x64 = self._io.read_f4le()
            self.float32_t_0x68 = self._io.read_f4le()
            self.float32_t_0x6c = self._io.read_f4le()
            self.float32_t_0x70 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 120
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2612185096
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGinsuSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.fade__out_0x38 = AnyGenesysObj.GenesysGenGinsuSequenceItemFade(self._io, self, self._root)
            self.cgs_resource__handle_0x4c = self._io.read_bytes(8)
            self.mixer__channel_0x54 = self._io.read_bytes(8)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 92
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 773308239
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSteeringWheelPhysics(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1329740588
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicsDamageBarProfileSegment(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.lamps_corked_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.recharge_time_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.size_0x24 = self._io.read_f4le()
            self.bool8_t_0x28 = self._io.read_u1()
            self.recharges_0x29 = self._io.read_u1()
            self.adapter_wales_0x2a = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 880609546
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOfflineEventAlternateRoutes(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.checkpoint_0xc = self._io.read_u4le()
            self.ptr_arr_route_markers_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_route_markers_0x10(self):
            if hasattr(self, '_m_inst_route_markers_0x10'):
                return self._m_inst_route_markers_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_route_markers_0x10)
            self._m_inst_route_markers_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_route_markers_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_route_markers_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 456387781
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesWorldCrashedPlayer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__collision_responses__world__crashed_player__constraint_data_0xc = AnyGenesysObj.GenesysGenCollisionResponsesWorldCrashedPlayerConstraintData(self._io, self, self._root)
            self.dodge_ginger_0x24 = AnyGenesysObj.GenesysGenCollisionResponsesWorldCrashedPlayerConstraintData(self._io, self, self._root)
            self.game_changer_id_0x3c = self._io.read_u4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1325791513
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDelayDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            self.time_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3627785814
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDonutAbilityDonutScale(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1015007408
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGearbox(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__gearbox__gear_0xc = AnyGenesysObj.GenesysGenGearboxGear(self._io, self, self._root)
            self.game_changer_id_0x28 = self._io.read_u4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.ptr_arr_genesys__gen__gearbox__gear_0x4c = self._io.read_u4le()
            self.array_count_for_0x4c = self._io.read_u2le()
            self.bool8_t_0x52 = self._io.read_u1()
            self.bool8_t_0x53 = self._io.read_u1()
            self.bool8_t_0x54 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_genesys__gen__gearbox__gear_0x4c(self):
            if hasattr(self, '_m_inst_genesys__gen__gearbox__gear_0x4c'):
                return self._m_inst_genesys__gen__gearbox__gear_0x4c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__gearbox__gear_0x4c)
            self._m_inst_genesys__gen__gearbox__gear_0x4c = []
            for i in range(self.array_count_for_0x4c):
                self._m_inst_genesys__gen__gearbox__gear_0x4c.append(AnyGenesysObj.GenesysGenGearboxGear(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__gearbox__gear_0x4c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 88
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3732602870
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicsDamageBarProfileImpactLocationDamageScale(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2817660171
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeLocation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__unique_id_0xc = self._io.read_u4le()
            self.ptr_arr_display_trigger_0x10 = self._io.read_u4le()
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.ptr_arr_triggers_0x18 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()

        @property
        def inst_display_trigger_0x10(self):
            if hasattr(self, '_m_inst_display_trigger_0x10'):
                return self._m_inst_display_trigger_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_display_trigger_0x10)
            self._m_inst_display_trigger_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_display_trigger_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_display_trigger_0x10', None)

        @property
        def inst_triggers_0x18(self):
            if hasattr(self, '_m_inst_triggers_0x18'):
                return self._m_inst_triggers_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_triggers_0x18)
            self._m_inst_triggers_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_triggers_0x18.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_triggers_0x18', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 944731751
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCloudCompeteAward(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.description_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.title_0x14 = self._io.read_u4le()
            self.unlock_string_0x18 = self._io.read_u4le()
            self.category_0x1c = self._io.read_u2le()
            self.action_destination_0x1e = self._io.read_u2le()
            self.uint16_t_0x20 = self._io.read_u2le()
            self.bool8_t_0x22 = self._io.read_u1()
            self.uint8_t_0x23 = self._io.read_u1()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3996354190
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSequenceItemsPostFxOverrideSequenceItemEffectDoubleValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_modulating_value_0xc = self._io.read_u4le()
            self.automated__property_0x10 = self._io.read_u4le()

        @property
        def inst_modulating_value_0xc(self):
            if hasattr(self, '_m_inst_modulating_value_0xc'):
                return self._m_inst_modulating_value_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_modulating_value_0xc)
            self._m_inst_modulating_value_0xc = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_modulating_value_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1642529028
            return getattr(self, '_m_mu_version_hash', None)


    class PtrArray(KaitaiStruct):
        def __init__(self, dtype, amt, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.dtype = dtype
            self.amt = amt
            self._read()

        def _read(self):
            self.offset = self._io.read_s4le()

        @property
        def entries(self):
            if hasattr(self, '_m_entries'):
                return self._m_entries

            _pos = self._io.pos()
            self._io.seek(self.offset)
            self._m_entries = []
            for i in range(self.amt):
                self._m_entries.append(AnyGenesysObj.Atype(self.dtype, self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_entries', None)


    class GenesysGenEngineSound(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.idle_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 64
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3641337381
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersDonutting(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.max_speed_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.nitrous_reward_0x1c = self._io.read_f4le()
            self.is_enabled_0x20 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3928390869
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleInfoExtraAxle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.int32_t_0x14 = self._io.read_s4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3588678847
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreSoundParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__tyre_sound_params__lateral_0xc = AnyGenesysObj.GenesysGenTyreSoundParamsLateral(self._io, self, self._root)
            self.genesys__gen__tyre_sound_params__lat_slip_0x3c = AnyGenesysObj.GenesysGenTyreSoundParamsLatSlip(self._io, self, self._root)
            self.genesys__gen__tyre_sound_params__longitudinal_0x64 = AnyGenesysObj.GenesysGenTyreSoundParamsLongitudinal(self._io, self, self._root)
            self.genesys__gen__tyre_sound_params__long_spin_braking_0x8c = AnyGenesysObj.GenesysGenTyreSoundParamsLongSpinBraking(self._io, self, self._root)
            self.genesys__gen__tyre_sound_params__long_spin_0xb4 = AnyGenesysObj.GenesysGenTyreSoundParamsLongSpin(self._io, self, self._root)
            self.game_changer_id_0xd8 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 224
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3054130878
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineReverseWhine(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__unique_id_0xc = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3727471200
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyres(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__tyres__tyres_0xc = AnyGenesysObj.GenesysGenTyresTyres(self._io, self, self._root)
            self.genesys__gen__tyres__surface_effects_0x24 = AnyGenesysObj.GenesysGenTyresSurfaceEffects(self._io, self, self._root)
            self.game_changer_id_0x38 = self._io.read_u4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.float32_t_0x4c = self._io.read_f4le()
            self.float32_t_0x50 = self._io.read_f4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.float32_t_0x58 = self._io.read_f4le()
            self.float32_t_0x5c = self._io.read_f4le()
            self.float32_t_0x60 = self._io.read_f4le()
            self.ptr_genesys__gen__tyre_sound_params_0x64 = self._io.read_u4le()

        @property
        def inst_genesys__gen__tyre_sound_params_0x64(self):
            if hasattr(self, '_m_inst_genesys__gen__tyre_sound_params_0x64'):
                return self._m_inst_genesys__gen__tyre_sound_params_0x64

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__tyre_sound_params_0x64)
            self._m_inst_genesys__gen__tyre_sound_params_0x64 = AnyGenesysObj.GenesysGenTyreSoundParams(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__tyre_sound_params_0x64', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 108
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1425943760
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenLightPoint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenLightBase(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 92
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3975851796
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarPhysicalDefinition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10 = self._io.read_u4le()
            self.ptr_genesys__gen__race_car_physical_definition__physical_definition_0x14 = self._io.read_u4le()
            self.int32_t_0x18 = self._io.read_s4le()
            self.int32_t_0x1c = self._io.read_s4le()
            self.int32_t_0x20 = self._io.read_s4le()
            self.int32_t_0x24 = self._io.read_s4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10'):
                return self._m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10)
            self._m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10.append(AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionConvexHullConectivityData(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data_0x10', None)

        @property
        def inst_genesys__gen__race_car_physical_definition__physical_definition_0x14(self):
            if hasattr(self, '_m_inst_genesys__gen__race_car_physical_definition__physical_definition_0x14'):
                return self._m_inst_genesys__gen__race_car_physical_definition__physical_definition_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__race_car_physical_definition__physical_definition_0x14)
            self._m_inst_genesys__gen__race_car_physical_definition__physical_definition_0x14 = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinition(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__race_car_physical_definition__physical_definition_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1316353574
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDspPlugInChain(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_plug_ins_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_plug_ins_0x10(self):
            if hasattr(self, '_m_inst_plug_ins_0x10'):
                return self._m_inst_plug_ins_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_plug_ins_0x10)
            self._m_inst_plug_ins_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_plug_ins_0x10.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_plug_ins_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3826155101
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyresTyres(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_genesys__gen__tyre_0x10 = self._io.read_u4le()
            self.ptr_genesys__gen__tyre_0x14 = self._io.read_u4le()

        @property
        def inst_genesys__gen__tyre_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__tyre_0x10'):
                return self._m_inst_genesys__gen__tyre_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__tyre_0x10)
            self._m_inst_genesys__gen__tyre_0x10 = AnyGenesysObj.GenesysGenTyre(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__tyre_0x10', None)

        @property
        def inst_genesys__gen__tyre_0x14(self):
            if hasattr(self, '_m_inst_genesys__gen__tyre_0x14'):
                return self._m_inst_genesys__gen__tyre_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__tyre_0x14)
            self._m_inst_genesys__gen__tyre_0x14 = AnyGenesysObj.GenesysGenTyre(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__tyre_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 368598916
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.label_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.activate_on_hit_0x18 = self._io.read_u1()
            self.deactivate_on_hit_0x19 = self._io.read_u1()
            self.initially_on_0x1a = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 160896465
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenThankYouScreenItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.heading_0x10 = self._io.read_u4le()
            self.message_0x14 = self._io.read_u4le()
            self.bounty_reward_0x18 = self._io.read_s4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2578912561
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenLightProjectedTexture(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenLightBase(self._io, self, self._root)
            self.rw_math_vpu__vector2_0x60 = AnyGenesysObj.RwMathVpuVector2(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x70 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x80 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.material_0x90 = self._io.read_bytes(8)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 152
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 229133803
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalCameraRoll(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3508674618
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineNormalQualityEngine(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2847735672
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesGlobalRaceCarVsRaceCarParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.damage_0x14 = self._io.read_f4le()
            self.linear__solve_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 716630460
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayOfflineUpgrade(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.apply_sequence_0xc = self._io.read_u4le()
            self.description_0x10 = self._io.read_u4le()
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.image_0x18 = self._io.read_u4le()
            self.milestone_required_0x1c = self._io.read_u4le()
            self.name_0x20 = self._io.read_u4le()
            self.short_name_0x24 = self._io.read_u4le()
            self.category_0x28 = self._io.read_u2le()
            self.type_0x2a = self._io.read_u2le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 112782069
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreVfxBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params_0xc = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParams(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params_0x13c = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParams(self._io, self, self._root)
            self.game_changer_id_0x26c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 628
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4074208643
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenLightBaseFlashPattern(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.duration_0x10 = self._io.read_f4le()
            self.frequency_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.offset_0x1c = self._io.read_f4le()
            self.type_0x20 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 306714612
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayTriggerOutput(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.predicate_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.ptr_arr_speech__events_0x14 = self._io.read_u4le()
            self.ptr_arr_ptr_aiplayers_0x18 = self._io.read_u4le()
            self.ptr_arr_sequence_0x1c = self._io.read_u4le()
            self.ptr_arr_ptr_roadblock_instance_0x20 = self._io.read_u4le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.array_count_for_0x1c = self._io.read_u2le()
            self.array_count_for_0x20 = self._io.read_u1()
            self.array_count_for_0x14 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_aiplayers_0x18(self):
            if hasattr(self, '_m_inst_aiplayers_0x18'):
                return self._m_inst_aiplayers_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_aiplayers_0x18)
            self._m_inst_aiplayers_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_aiplayers_0x18.append(AnyGenesysObj.Ptr(u"genesys__gen__gameplay_trigger__aiplayer_information", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_aiplayers_0x18', None)

        @property
        def inst_roadblock_instance_0x20(self):
            if hasattr(self, '_m_inst_roadblock_instance_0x20'):
                return self._m_inst_roadblock_instance_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_roadblock_instance_0x20)
            self._m_inst_roadblock_instance_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_roadblock_instance_0x20.append(AnyGenesysObj.Ptr(u"genesys__gen__roadblock_instance", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_roadblock_instance_0x20', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def inst_sequence_0x1c(self):
            if hasattr(self, '_m_inst_sequence_0x1c'):
                return self._m_inst_sequence_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_sequence_0x1c)
            self._m_inst_sequence_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_sequence_0x1c.append(AnyGenesysObj.GenesysGenGameplayTriggerOutputSequenceOutput(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_sequence_0x1c', None)

        @property
        def inst_speech__events_0x14(self):
            if hasattr(self, '_m_inst_speech__events_0x14'):
                return self._m_inst_speech__events_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_speech__events_0x14)
            self._m_inst_speech__events_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_speech__events_0x14.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_speech__events_0x14', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 835914245
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionEffectsWorldEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cam__effect_0xc = self._io.read_bytes(8)
            self.cam__effect__unstable_0x14 = self._io.read_bytes(8)
            self.cam__effect__scale_0x1c = self._io.read_f4le()
            self.stable__camera__threshold_0x20 = self._io.read_f4le()
            self.unstable__camera__threshold_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2825220545
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicalDefinitionRigidBodyCapsuleVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.game_changer_id_0x50 = self._io.read_u4le()
            self.half_length_0x54 = self._io.read_f4le()
            self.radius_0x58 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 18021398
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEnginePowerCurve(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.ptr_arr_ptr_genesys__gen__point2dwith_tangents_0x4c = self._io.read_u4le()
            self.array_count_for_0x4c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_genesys__gen__point2dwith_tangents_0x4c(self):
            if hasattr(self, '_m_inst_genesys__gen__point2dwith_tangents_0x4c'):
                return self._m_inst_genesys__gen__point2dwith_tangents_0x4c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_genesys__gen__point2dwith_tangents_0x4c)
            self._m_inst_genesys__gen__point2dwith_tangents_0x4c = []
            for i in range(self.array_count_for_0x4c):
                self._m_inst_genesys__gen__point2dwith_tangents_0x4c.append(AnyGenesysObj.Ptr(u"genesys__gen__point2dwith_tangents", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__point2dwith_tangents_0x4c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 84
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3195239353
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicsCrashingRulesImpactRulesDamageToDeal(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.damage_to_deal_0xc = self._io.read_f4le()
            self.should_wreck_0x10 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1483915852
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCar(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.player__vs__traffic_0xc = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTraffic(self._io, self, self._root)
            self.player__vs__ai_0x100 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAi(self._io, self, self._root)
            self.ai__vs__traffic_0x1e8 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTraffic(self._io, self, self._root)
            self.player__vs__crashing__race__car_0x2c0 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCar(self._io, self, self._root)
            self.ai__vs__crashing__race__car_0x368 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsCrashingRaceCar(self._io, self, self._root)
            self.ai__car__vs__dynamic_0x3d0 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarRaceCarVsDynamic(self._io, self, self._root)
            self.player_or__network_car__vs__dynamic_0x40c = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarRaceCarVsDynamic(self._io, self, self._root)
            self.game_changer_id_0x448 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 1104
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 524753351
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarEffectSequenceItemEffectDoubleValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_modulating_value_0xc = self._io.read_u4le()
            self.automated__property_0x10 = self._io.read_u4le()

        @property
        def inst_modulating_value_0xc(self):
            if hasattr(self, '_m_inst_modulating_value_0xc'):
                return self._m_inst_modulating_value_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_modulating_value_0xc)
            self._m_inst_modulating_value_0xc = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_modulating_value_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1852100653
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayCopType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.aiplayer_type_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.bool8_t_0x14 = self._io.read_u1()
            self.can_spawn_behind_0x15 = self._io.read_u1()
            self.can_spawn_head_on_0x16 = self._io.read_u1()
            self.can_spawn_intercepting_0x17 = self._io.read_u1()
            self.bool8_t_0x18 = self._io.read_u1()
            self.bool8_t_0x19 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1758839251
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNucleusGrantMappingsListMapping(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.nucleus_tag_0x10 = self._io.read_u4le()
            self.ptr_arr_entitlement_0x14 = self._io.read_u4le()
            self.array_count_for_0x14 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_entitlement_0x14(self):
            if hasattr(self, '_m_inst_entitlement_0x14'):
                return self._m_inst_entitlement_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_entitlement_0x14)
            self._m_inst_entitlement_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_entitlement_0x14.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_entitlement_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4263309034
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionActionBase(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.feedback_data_0xc = AnyGenesysObj.GenesysGenChallengeActionActionBaseFeedbackData(self._io, self, self._root)
            self.cgs_core__unique_id_0x30 = self._io.read_u4le()
            self.cgs_core__unique_id_0x34 = self._io.read_u4le()
            self.game_changer_id_0x38 = self._io.read_u4le()
            self.ptr_accumulation_data_0x3c = self._io.read_u4le()
            self.builtin_evoke_0x40 = self._io.read_u2le()
            self.scoring_method_0x42 = self._io.read_u2le()
            self.unk_enum_0x44 = self._io.read_u2le()
            self.who_0x46 = self._io.read_u2le()

        @property
        def inst_accumulation_data_0x3c(self):
            if hasattr(self, '_m_inst_accumulation_data_0x3c'):
                return self._m_inst_accumulation_data_0x3c

            _pos = self._io.pos()
            self._io.seek(self.ptr_accumulation_data_0x3c)
            self._m_inst_accumulation_data_0x3c = AnyGenesysObj.GenesysGenChallengeActionAccumulationHelperData(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_accumulation_data_0x3c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3948195379
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOnlineDrivingTestList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.description_0xc = self._io.read_u4le()
            self.ptr_arr_driving_tests_0x10 = self._io.read_u4le()
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.name_0x18 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_driving_tests_0x10(self):
            if hasattr(self, '_m_inst_driving_tests_0x10'):
                return self._m_inst_driving_tests_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_driving_tests_0x10)
            self._m_inst_driving_tests_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_driving_tests_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_driving_tests_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1755540478
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenLfoSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.unit_0x28 = self._io.read_u2le()
            self.automated__values_count_0x2a = self._io.read_u2le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2474227476
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDriftBehaviourDriftExit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4039040682
            return getattr(self, '_m_mu_version_hash', None)


    class PtrPtrTable(KaitaiStruct):
        def __init__(self, dtype, amt, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.dtype = dtype
            self.amt = amt
            self._read()

        def _read(self):
            self.offset = self._io.read_s4le()
            if self.amt == 0:
                self.count = self._io.read_u4le()


        @property
        def len(self):
            if hasattr(self, '_m_len'):
                return self._m_len

            self._m_len = (0 if self.amt == -1 else (self.count if self.amt == 0 else self.amt))
            return getattr(self, '_m_len', None)

        @property
        def ptr_table(self):
            if hasattr(self, '_m_ptr_table'):
                return self._m_ptr_table

            if self.offset != 0:
                _pos = self._io.pos()
                self._io.seek(self.offset)
                self._m_ptr_table = AnyGenesysObj.PtrTable(self.dtype, self.len, self._io, self, self._root)
                self._io.seek(_pos)

            return getattr(self, '_m_ptr_table', None)


    class GenesysGenCollisionEffectsBattlingEffectExtraRollParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3396244228
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicsCrashingRulesImpactRules(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_arr_float32_t_0xc = self._io.read_u4le()
            self.ptr_arr_float32_t_0x10 = self._io.read_u4le()
            self.ptr_arr_float32_t_0x14 = self._io.read_u4le()
            self.ptr_arr_damage_override_0x18 = self._io.read_u4le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.array_count_for_0x14 = self._io.read_u2le()

        @property
        def inst_float32_t_0x14(self):
            if hasattr(self, '_m_inst_float32_t_0x14'):
                return self._m_inst_float32_t_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_float32_t_0x14)
            self._m_inst_float32_t_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_float32_t_0x14.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_float32_t_0x14', None)

        @property
        def inst_float32_t_0xc(self):
            if hasattr(self, '_m_inst_float32_t_0xc'):
                return self._m_inst_float32_t_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_float32_t_0xc)
            self._m_inst_float32_t_0xc = []
            for i in range(self.array_count_for_0xc):
                self._m_inst_float32_t_0xc.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_float32_t_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def inst_float32_t_0x10(self):
            if hasattr(self, '_m_inst_float32_t_0x10'):
                return self._m_inst_float32_t_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_float32_t_0x10)
            self._m_inst_float32_t_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_float32_t_0x10.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_float32_t_0x10', None)

        @property
        def inst_damage_override_0x18(self):
            if hasattr(self, '_m_inst_damage_override_0x18'):
                return self._m_inst_damage_override_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_damage_override_0x18)
            self._m_inst_damage_override_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_damage_override_0x18.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRulesDamageToDeal(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_damage_override_0x18', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1202023644
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclePaint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x10 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x20 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x30 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x40 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x50 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x60 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.cgs_core__unique_id_0x70 = self._io.read_u4le()
            self.game_changer_id_0x74 = self._io.read_u4le()
            self.name_0x78 = self._io.read_u4le()
            self.float32_t_0x7c = self._io.read_f4le()
            self.float32_t_0x80 = self._io.read_f4le()
            self.float32_t_0x84 = self._io.read_f4le()
            self.float32_t_0x88 = self._io.read_f4le()
            self.float32_t_0x8c = self._io.read_f4le()
            self.float32_t_0x90 = self._io.read_f4le()
            self.float32_t_0x94 = self._io.read_f4le()
            self.float32_t_0x98 = self._io.read_f4le()
            self.unk_enum_0x9c = self._io.read_u2le()
            self.type_0x9e = self._io.read_u2le()
            self.bool8_t_0xa0 = self._io.read_u1()
            self.bool8_t_0xa1 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 164
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 669436076
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayBlacklistShutdownDataDamageThresholdSpeedControl(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.far_distance_0xc = self._io.read_f4le()
            self.near_distance_0x10 = self._io.read_f4le()
            self.rewarding_highlighting_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1543118382
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersFatalHit(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.nitrous_reward_0x14 = self._io.read_f4le()
            self.is_enabled_0x18 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3785567855
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarHandlingDisruptionEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.effect_duration_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.high_speed_front_lat_grip_0x18 = self._io.read_f4le()
            self.high_speed_front_long_grip_0x1c = self._io.read_f4le()
            self.high_speed_rear_lat_grip_0x20 = self._io.read_f4le()
            self.high_speed_rear_long_grip_0x24 = self._io.read_f4le()
            self.high_speed_steer_amount_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.high_speed_threshold_0x30 = self._io.read_f4le()
            self.low_speed_front_lat_grip_0x34 = self._io.read_f4le()
            self.low_speed_front_long_grip_0x38 = self._io.read_f4le()
            self.low_speed_rear_lat_grip_0x3c = self._io.read_f4le()
            self.low_speed_rear_long_grip_0x40 = self._io.read_f4le()
            self.low_speed_steer_amount_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.low_speed_threshold_0x4c = self._io.read_f4le()
            self.affects_all_wheels_0x50 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 84
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 724902868
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenLightBase(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.colour_0x10 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.genesys__gen__light__base__flash_pattern_0x20 = AnyGenesysObj.GenesysGenLightBaseFlashPattern(self._io, self, self._root)
            self.game_changer_id_0x44 = self._io.read_u4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.intensity_0x4c = self._io.read_f4le()
            self.bool8_t_0x50 = self._io.read_u1()
            self.bool8_t_0x51 = self._io.read_u1()
            self.bool8_t_0x52 = self._io.read_u1()
            self.bool8_t_0x53 = self._io.read_u1()
            self.bool8_t_0x54 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 88
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4046186056
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenScoreViewModelScoreData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.binding_path_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.rank_0x18 = self._io.read_s4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 606909642
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionActionBaseFeedbackData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.instruction_0xc = self._io.read_u4le()
            self.cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.cgs_core__unique_id_0x14 = self._io.read_u4le()
            self.cgs_core__unique_id_0x18 = self._io.read_u4le()
            self.cgs_core__unique_id_0x1c = self._io.read_u4le()
            self.unk_enum_0x20 = self._io.read_u2le()
            self.bool8_t_0x22 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1294158455
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSequenceItemModulatingDoubleValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.binding_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.binding__exponent_0x14 = self._io.read_f4le()
            self.binding__range__max_0x18 = self._io.read_f4le()
            self.binding__range__min_0x1c = self._io.read_f4le()
            self.output__value__max_0x20 = self._io.read_f4le()
            self.output__value__min_0x24 = self._io.read_f4le()
            self.value_0x28 = self._io.read_f4le()
            self.unk_enum_0x2c = self._io.read_u4le()
            self.animation__modulation__type_0x30 = self._io.read_u2le()
            self.binding__modulation__type_0x32 = self._io.read_u2le()
            self.array_count_for_0x2c = self._io.read_u2le()
            self.bool8_t_0x36 = self._io.read_u1()
            self.binding__invert_0x37 = self._io.read_u1()

        @property
        def inst_5a__f6_03_00_0_1_0x2c(self):
            if hasattr(self, '_m_inst_5a__f6_03_00_0_1_0x2c'):
                return self._m_inst_5a__f6_03_00_0_1_0x2c

            _pos = self._io.pos()
            self._io.seek(self.unk_enum_0x2c)
            self._m_inst_5a__f6_03_00_0_1_0x2c = []
            for i in range(self.array_count_for_0x2c):
                self._m_inst_5a__f6_03_00_0_1_0x2c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_5a__f6_03_00_0_1_0x2c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 60
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1489464845
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHeatLevelSoundSetSirens(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_arr_blip__waves_0xc = self._io.read_u4le()
            self.ptr_arr_extra__waves_0x10 = self._io.read_u4le()
            self.ptr_arr_rumbler__waves_0x14 = self._io.read_u4le()
            self.standard__wave_0x18 = self._io.read_u4le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.array_count_for_0x14 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def inst_rumbler__waves_0x14(self):
            if hasattr(self, '_m_inst_rumbler__waves_0x14'):
                return self._m_inst_rumbler__waves_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_rumbler__waves_0x14)
            self._m_inst_rumbler__waves_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_rumbler__waves_0x14.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_rumbler__waves_0x14', None)

        @property
        def inst_extra__waves_0x10(self):
            if hasattr(self, '_m_inst_extra__waves_0x10'):
                return self._m_inst_extra__waves_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_extra__waves_0x10)
            self._m_inst_extra__waves_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_extra__waves_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_extra__waves_0x10', None)

        @property
        def inst_blip__waves_0xc(self):
            if hasattr(self, '_m_inst_blip__waves_0xc'):
                return self._m_inst_blip__waves_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_blip__waves_0xc)
            self._m_inst_blip__waves_0xc = []
            for i in range(self.array_count_for_0xc):
                self._m_inst_blip__waves_0xc.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_blip__waves_0xc', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1058122174
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayTriggerAiplayerInformation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.placement_0xc = self._io.read_u4le()
            self.ptr_aiplayer_instance_0x10 = self._io.read_u4le()

        @property
        def inst_aiplayer_instance_0x10(self):
            if hasattr(self, '_m_inst_aiplayer_instance_0x10'):
                return self._m_inst_aiplayer_instance_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_aiplayer_instance_0x10)
            self._m_inst_aiplayer_instance_0x10 = AnyGenesysObj.GenesysGenAiplayerInstance(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_aiplayer_instance_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1291389730
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleDriverSetup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x10 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.ptr_arr_cgs_core__unique_id_0x20 = self._io.read_u4le()
            self.cgs_core__unique_id_0x24 = self._io.read_u4le()
            self.game_changer_id_0x28 = self._io.read_u4le()
            self.cgs_core__unique_id_0x2c = self._io.read_u4le()
            self.cgs_core__unique_id_0x30 = self._io.read_u4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.ptr_arr_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c = self._io.read_u4le()
            self.array_count_for_0x20 = self._io.read_u2le()
            self.array_count_for_0x3c = self._io.read_u2le()
            self.bool8_t_0x44 = self._io.read_u1()
            self.bool8_t_0x45 = self._io.read_u1()
            self.bool8_t_0x46 = self._io.read_u1()
            self.bool8_t_0x47 = self._io.read_u1()

        @property
        def inst_cgs_core__unique_id_0x20(self):
            if hasattr(self, '_m_inst_cgs_core__unique_id_0x20'):
                return self._m_inst_cgs_core__unique_id_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_core__unique_id_0x20)
            self._m_inst_cgs_core__unique_id_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_cgs_core__unique_id_0x20.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_core__unique_id_0x20', None)

        @property
        def inst_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c'):
                return self._m_inst_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c)
            self._m_inst_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c = []
            for i in range(self.array_count_for_0x3c):
                self._m_inst_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c.append(AnyGenesysObj.GenesysGenVehicleDriverSetupSeatBeltBoneOffset(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle__driver_setup__seat_belt_bone_offset_0x3c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3584499810
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenUilistItemsItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.value_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.display_string_0x14 = self._io.read_u4le()
            self.game_changer_id_0x18 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 101265141
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionSpeedCameraAction(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.on_hit_sequence_0x4c = self._io.read_u4le()
            self.ptr_genesys__gen__challenge__location_0x50 = self._io.read_u4le()

        @property
        def inst_genesys__gen__challenge__location_0x50(self):
            if hasattr(self, '_m_inst_genesys__gen__challenge__location_0x50'):
                return self._m_inst_genesys__gen__challenge__location_0x50

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__challenge__location_0x50)
            self._m_inst_genesys__gen__challenge__location_0x50 = AnyGenesysObj.GenesysGenChallengeLocation(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__challenge__location_0x50', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 88
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3823531688
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalGlobalsLensProperties(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.bool8_t_0x18 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2401606622
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarPhysicalDefinitionPhysicalDefinition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.local_aabbcenter_0x10 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.local_aabbhalf_diagonal_0x20 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.additional_info_0x30 = self._io.read_bytes(8)
            self.ptr_arr_rigid_bodies_names_0x38 = self._io.read_u4le()
            self.game_changer_id_0x3c = self._io.read_u4le()
            self.ptr_arr_rigid_bodies_0x40 = self._io.read_u4le()
            self.game_changer_id_0x44 = self._io.read_s4le()
            self.main_rigid_body_index_0x48 = self._io.read_s4le()
            self.array_count_for_0x40 = self._io.read_u2le()
            self.array_count_for_0x38 = self._io.read_u2le()
            self.bool8_t_0x50 = self._io.read_u1()
            self.bool8_t_0x51 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_rigid_bodies_names_0x38(self):
            if hasattr(self, '_m_inst_rigid_bodies_names_0x38'):
                return self._m_inst_rigid_bodies_names_0x38

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_rigid_bodies_names_0x38)
            self._m_inst_rigid_bodies_names_0x38 = []
            for i in range(self.array_count_for_0x38):
                self._m_inst_rigid_bodies_names_0x38.append(AnyGenesysObj.StringBase(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_rigid_bodies_names_0x38', None)

        @property
        def inst_rigid_bodies_0x40(self):
            if hasattr(self, '_m_inst_rigid_bodies_0x40'):
                return self._m_inst_rigid_bodies_0x40

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_rigid_bodies_0x40)
            self._m_inst_rigid_bodies_0x40 = []
            for i in range(self.array_count_for_0x40):
                self._m_inst_rigid_bodies_0x40.append(AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBody(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_rigid_bodies_0x40', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 84
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2519567673
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayShakeEffectTranslation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.x_0xc = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectTranslationAxisParams(self._io, self, self._root)
            self.y_0x38 = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectTranslationAxisParams(self._io, self, self._root)
            self.z_0x64 = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectTranslationAxisParams(self._io, self, self._root)
            self.game_changer_id_0x90 = self._io.read_u4le()
            self.amplitude_0x94 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 156
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 866205257
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreSoundParamsLongitudinal(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2992725297
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionAccumulateNearMisses(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.ptr_location_0x4c = self._io.read_u4le()
            self.in_air_0x50 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_location_0x4c(self):
            if hasattr(self, '_m_inst_location_0x4c'):
                return self._m_inst_location_0x4c

            _pos = self._io.pos()
            self._io.seek(self.ptr_location_0x4c)
            self._m_inst_location_0x4c = AnyGenesysObj.GenesysGenChallengeLocation(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_location_0x4c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 84
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 732433969
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayBumper(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenCameraGameplayBonnet(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 132
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 983393262
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclesTyreUpgrade(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2784884141
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEntitlement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.description_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.entitlement_tag_0x14 = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.name_0x1c = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.game_changer_id_0x24 = self._io.read_u4le()
            self.purchasable_0x28 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2560361681
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineSound2DspParam(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_resource__handle_0xc = self._io.read_bytes(8)
            self.plug_in_0x14 = self._io.read_u4le()
            self.value_0x18 = self._io.read_f4le()
            self.unk_enum_0x1c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 174067018
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenScoreViewModelScore(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.action_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.string_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2080073476
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWcvfxBehaviourSpotEffects(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_resource__handle_0xc = self._io.read_bytes(8)
            self.locator_group_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2208212217
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesWorldPlayer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.high_speed_flip_state_0xc = AnyGenesysObj.GenesysGenCollisionResponsesWorldPlayerFlipState(self._io, self, self._root)
            self.low_speed_flip_state_0x2c = AnyGenesysObj.GenesysGenCollisionResponsesWorldPlayerFlipState(self._io, self, self._root)
            self.game_changer_id_0x4c = self._io.read_u4le()
            self.dynamic_friction_0x50 = self._io.read_f4le()
            self.restitution_0x54 = self._io.read_f4le()
            self.solve_position_angular_scale_0x58 = self._io.read_f4le()
            self.solve_velocity_angular_scale_0x5c = self._io.read_f4le()
            self.static_friction_0x60 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 104
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4260207896
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOnlineVoteEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenOnlineEvent(self._io, self, self._root)
            self.cgs_core__unique_id_0x70 = self._io.read_u4le()
            self.cgs_core__unique_id_0x74 = self._io.read_u4le()
            self.cgs_core__unique_id_0x78 = self._io.read_u4le()
            self.cgs_core__unique_id_0x7c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 132
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3136795337
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreLateralSlipFactors(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 166064775
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenMixerChannel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.distance_falloff_0xc = self._io.read_bytes(8)
            self.plug_in__chain_0x14 = self._io.read_bytes(8)
            self.game_changer_id_0x1c = self._io.read_u4le()
            self.mixing_group_0x20 = self._io.read_u4le()
            self.centre_level_0x24 = self._io.read_f4le()
            self.emitter_response_0x28 = self._io.read_f4le()
            self.focus_0x2c = self._io.read_f4le()
            self.gain_0x30 = self._io.read_f4le()
            self.lfe_send_0x34 = self._io.read_f4le()
            self.panning__cosine_0x38 = self._io.read_f4le()
            self.panning__divergence_0x3c = self._io.read_f4le()
            self.panning__sine_0x40 = self._io.read_f4le()
            self.reverb_send_a_0x44 = self._io.read_f4le()
            self.reverb_send_b_0x48 = self._io.read_f4le()
            self.ptr_arr_priority_0x4c = self._io.read_u4le()
            self.ptr_voice_group_0x50 = self._io.read_u4le()
            self.doppler_model_0x54 = self._io.read_u2le()
            self.virtual_voice_behaviour_0x56 = self._io.read_u2le()
            self.array_count_for_0x4c = self._io.read_u2le()
            self.cull_playing_voices_0x5a = self._io.read_u1()
            self.panning__override_0x5b = self._io.read_u1()
            self.instance_limit_0x5c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_priority_0x4c(self):
            if hasattr(self, '_m_inst_priority_0x4c'):
                return self._m_inst_priority_0x4c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_priority_0x4c)
            self._m_inst_priority_0x4c = []
            for i in range(self.array_count_for_0x4c):
                self._m_inst_priority_0x4c.append(AnyGenesysObj.GenesysGenMixerChannelPriority(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_priority_0x4c', None)

        @property
        def inst_voice_group_0x50(self):
            if hasattr(self, '_m_inst_voice_group_0x50'):
                return self._m_inst_voice_group_0x50

            _pos = self._io.pos()
            self._io.seek(self.ptr_voice_group_0x50)
            self._m_inst_voice_group_0x50 = AnyGenesysObj.GenesysGenVoiceGroup(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_voice_group_0x50', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2971966527
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarAivsTrafficBasicParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.linear__solve_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1951683017
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOnlineLicensePlate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.backing_image_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.name_0x14 = self._io.read_u4le()
            self.release_0x18 = self._io.read_u4le()
            self.bool8_t_0x1c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1106192363
            return getattr(self, '_m_mu_version_hash', None)


    class Uint8T(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenEventLocation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.inline_arr_position_0xc = []
            for i in range(3):
                self.inline_arr_position_0xc.append(self._io.read_f4le())

            self.event_list_0x18 = self._io.read_bytes(8)
            self.main_map_camera_0x20 = self._io.read_bytes(8)
            self.zoomed_map_camera_0x28 = self._io.read_bytes(8)
            self.freedrive_event_0x30 = self._io.read_u4le()
            self.game_changer_id_0x34 = self._io.read_u4le()
            self.name_0x38 = self._io.read_u4le()
            self.original_game_pack_0x3c = self._io.read_u4le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.is_cop_location_0x42 = self._io.read_u1()
            self.is_online_0x43 = self._io.read_u1()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 72
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3916132985
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclesPerformanceUpgradesCategory(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x10 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x14 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x18 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x1c = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x20 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x24 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x28 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x2c = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x30 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x34 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x38 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x3c = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x40 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x44 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x48 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x4c = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0x50 = self._io.read_u4le()

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x24(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x24'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x24)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x24 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x24', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x18(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x18'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x18)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x18 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x18', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x38(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x38'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x38

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x38)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x38 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x38', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x10'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x10)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x10 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x10', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x14(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x14'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x14)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x14 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x14', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x3c(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x3c'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x3c

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x3c)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x3c = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x3c', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x28(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x28'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x28)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x28 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x28', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x20(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x20'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x20)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x20 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x20', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 88
            return getattr(self, '_m_size', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x34(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x34'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x34

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x34)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x34 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x34', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x40(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x40'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x40

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x40)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x40 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x40', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x30(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x30'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x30

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x30)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x30 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x30', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x2c(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x2c'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x2c

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x2c)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x2c = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x2c', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x50(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x50'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x50

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x50)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x50 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x50', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x1c(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x1c'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x1c)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x1c = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x1c', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x48(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x48'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x48

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x48)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x48 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x48', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x44(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x44'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x44

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x44)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x44 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x44', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2230798373
            return getattr(self, '_m_mu_version_hash', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0x4c(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x4c'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0x4c

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0x4c)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0x4c = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0x4c', None)


    class GenesysGenMakePhysicalBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.unk_enum_0x1c = self._io.read_u2le()
            self.collidable_0x1e = self._io.read_u1()
            self.initially_frozen_0x1f = self._io.read_u1()
            self.bool8_t_0x20 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3788863516
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSmashProxyBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3085449154
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayShakeEffectTranslationAxisParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.amplitude_0x10 = self._io.read_f4le()
            self.inwards__damping_0x14 = self._io.read_f4le()
            self.lower__translation__limit_0x18 = self._io.read_f4le()
            self.outwards__damping_0x1c = self._io.read_f4le()
            self.spring__coefficient_0x20 = self._io.read_f4le()
            self.upper__translation__limit_0x24 = self._io.read_f4le()
            self.invert__force__direction_0x28 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3529693283
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleCameraContainer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_genesys__gen__camera_gameplay_bonnet_0x10 = self._io.read_u4le()
            self.ptr_genesys__gen__camera_gameplay_bumper_0x14 = self._io.read_u4le()
            self.ptr_genesys__gen__camera_gameplay_external_0x18 = self._io.read_u4le()
            self.ptr_genesys__gen__camera_rear_view_0x1c = self._io.read_u4le()

        @property
        def inst_genesys__gen__camera_rear_view_0x1c(self):
            if hasattr(self, '_m_inst_genesys__gen__camera_rear_view_0x1c'):
                return self._m_inst_genesys__gen__camera_rear_view_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__camera_rear_view_0x1c)
            self._m_inst_genesys__gen__camera_rear_view_0x1c = AnyGenesysObj.GenesysGenCameraRearView(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__camera_rear_view_0x1c', None)

        @property
        def inst_genesys__gen__camera_gameplay_external_0x18(self):
            if hasattr(self, '_m_inst_genesys__gen__camera_gameplay_external_0x18'):
                return self._m_inst_genesys__gen__camera_gameplay_external_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__camera_gameplay_external_0x18)
            self._m_inst_genesys__gen__camera_gameplay_external_0x18 = AnyGenesysObj.GenesysGenCameraGameplayExternal(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__camera_gameplay_external_0x18', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def inst_genesys__gen__camera_gameplay_bonnet_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__camera_gameplay_bonnet_0x10'):
                return self._m_inst_genesys__gen__camera_gameplay_bonnet_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__camera_gameplay_bonnet_0x10)
            self._m_inst_genesys__gen__camera_gameplay_bonnet_0x10 = AnyGenesysObj.GenesysGenCameraGameplayBonnet(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__camera_gameplay_bonnet_0x10', None)

        @property
        def inst_genesys__gen__camera_gameplay_bumper_0x14(self):
            if hasattr(self, '_m_inst_genesys__gen__camera_gameplay_bumper_0x14'):
                return self._m_inst_genesys__gen__camera_gameplay_bumper_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__camera_gameplay_bumper_0x14)
            self._m_inst_genesys__gen__camera_gameplay_bumper_0x14 = AnyGenesysObj.GenesysGenCameraGameplayBumper(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__camera_gameplay_bumper_0x14', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 86537152
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarPhysicalDefinitionConvexHullConectivityData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10'):
                return self._m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10)
            self._m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10.append(AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionConvexHullConectivityDataConvexHullConnectingFace(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1445450323
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDriftBehaviourDriftTrigger(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1589286504
            return getattr(self, '_m_mu_version_hash', None)


    class Uint32T(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenCoronaBeam(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.unk_enum_0x10 = self._io.read_u1()
            self.colour_0xa0 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0xb0 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.material_0xc0 = self._io.read_bytes(8)
            self.end_radius_0xc8 = self._io.read_f4le()
            self.start_radius_0xcc = self._io.read_f4le()
            self.render_buffer_0xd0 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 216
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3375675327
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRollout(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.weapon_data_0xc = AnyGenesysObj.GenesysGenRolloutWeaponData(self._io, self, self._root)
            self.body_upgrade_0x24 = self._io.read_u4le()
            self.ptr_arr_characters_0x28 = self._io.read_u4le()
            self.chassis_upgrade_0x2c = self._io.read_u4le()
            self.colour_0x30 = self._io.read_u4le()
            self.damage_bar_profile_0x34 = self._io.read_u4le()
            self.game_changer_id_0x38 = self._io.read_u4le()
            self.ptr_arr_cgs_core__unique_id_0x3c = self._io.read_u4le()
            self.name_0x40 = self._io.read_u4le()
            self.nitrous_upgrade_0x44 = self._io.read_u4le()
            self.ptr_arr_number_plate_0x48 = self._io.read_u4le()
            self.cgs_core__unique_id_0x4c = self._io.read_u4le()
            self.revenge_bonus_0x50 = self._io.read_u4le()
            self.cgs_core__unique_id_0x54 = self._io.read_u4le()
            self.vehicle_0x58 = self._io.read_u4le()
            self.dirt_amount_0x5c = self._io.read_f4le()
            self.dust_amount_0x60 = self._io.read_f4le()
            self.array_count_for_0x28 = self._io.read_u2le()
            self.array_count_for_0x3c = self._io.read_u2le()
            self.array_count_for_0x48 = self._io.read_u2le()
            self.bool8_t_0x6a = self._io.read_u1()
            self.is_online_rollout_0x6b = self._io.read_u1()
            self.is_player_rollout_0x6c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_cgs_core__unique_id_0x3c(self):
            if hasattr(self, '_m_inst_cgs_core__unique_id_0x3c'):
                return self._m_inst_cgs_core__unique_id_0x3c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_core__unique_id_0x3c)
            self._m_inst_cgs_core__unique_id_0x3c = []
            for i in range(self.array_count_for_0x3c):
                self._m_inst_cgs_core__unique_id_0x3c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_core__unique_id_0x3c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 112
            return getattr(self, '_m_size', None)

        @property
        def inst_number_plate_0x48(self):
            if hasattr(self, '_m_inst_number_plate_0x48'):
                return self._m_inst_number_plate_0x48

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_number_plate_0x48)
            self._m_inst_number_plate_0x48 = []
            for i in range(self.array_count_for_0x48):
                self._m_inst_number_plate_0x48.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_number_plate_0x48', None)

        @property
        def inst_characters_0x28(self):
            if hasattr(self, '_m_inst_characters_0x28'):
                return self._m_inst_characters_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_characters_0x28)
            self._m_inst_characters_0x28 = []
            for i in range(self.array_count_for_0x28):
                self._m_inst_characters_0x28.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_characters_0x28', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1836975283
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarPlayerVsAiBasicParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.linear__solve_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 481138910
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPostFxKeyframeStereo3d(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.focus__distance_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1324301512
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNucleusEntitlementTag(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.tag_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.game_changer_id_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1212586379
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesWorldInAirPlayer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.dynamic_friction_0x10 = self._io.read_f4le()
            self.restitution_0x14 = self._io.read_f4le()
            self.solve_position_angular_scale_0x18 = self._io.read_f4le()
            self.solve_velocity_angular_scale_0x1c = self._io.read_f4le()
            self.static_friction_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2328783125
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOnlineChallenge(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.description_0xc = self._io.read_u4le()
            self.ptr_arr_cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.equipment__vehicle_0x14 = self._io.read_u4le()
            self.cgs_core__unique_id_0x18 = self._io.read_u4le()
            self.game_changer_id_0x1c = self._io.read_u4le()
            self.ptr_arr_game_mode_0x20 = self._io.read_u4le()
            self.ptr_arr_license_plates_0x24 = self._io.read_u4le()
            self.manufacturer_0x28 = self._io.read_u4le()
            self.cgs_core__unique_id_0x2c = self._io.read_u4le()
            self.name_0x30 = self._io.read_u4le()
            self.revenge_bonus_0x34 = self._io.read_u4le()
            self.att0_0x38 = self._io.read_u4le()
            self.screen_description_0x3c = self._io.read_u4le()
            self.ticket_0x40 = self._io.read_u4le()
            self.title_0x44 = self._io.read_u4le()
            self.trigger_0x48 = self._io.read_u4le()
            self.vehicle_category_0x4c = self._io.read_u4le()
            self.cgs_core__unique_id_0x50 = self._io.read_u4le()
            self.vehicle_nationality_0x54 = self._io.read_u4le()
            self.cgs_core__unique_id_0x58 = self._io.read_u4le()
            self.cgs_core__unique_id_0x5c = self._io.read_u4le()
            self.ptr_arr_ptr_target_0x60 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.array_count_for_0x20 = self._io.read_u2le()
            self.array_count_for_0x24 = self._io.read_u2le()
            self.scope_actions_0x6a = self._io.read_u2le()
            self.bool8_t_0x6c = self._io.read_u1()
            self.most_wanted_0x6d = self._io.read_u1()
            self.not_eliminated_0x6e = self._io.read_u1()
            self.not_wrecked_0x6f = self._io.read_u1()
            self.on_rims_0x70 = self._io.read_u1()
            self.same_victim_0x71 = self._io.read_u1()
            self.bool8_t_0x72 = self._io.read_u1()
            self.bool8_t_0x73 = self._io.read_u1()
            self.bool8_t_0x74 = self._io.read_u1()
            self.unk_enum_0x75 = self._io.read_u1()
            self.action__type_0x76 = self._io.read_u1()
            self.condition_0x77 = self._io.read_u1()
            self.unk_enum_0x78 = self._io.read_u1()
            self.time__period_0x79 = self._io.read_u1()
            self.array_count_for_0x60 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 124
            return getattr(self, '_m_size', None)

        @property
        def inst_license_plates_0x24(self):
            if hasattr(self, '_m_inst_license_plates_0x24'):
                return self._m_inst_license_plates_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_license_plates_0x24)
            self._m_inst_license_plates_0x24 = []
            for i in range(self.array_count_for_0x24):
                self._m_inst_license_plates_0x24.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_license_plates_0x24', None)

        @property
        def inst_target_0x60(self):
            if hasattr(self, '_m_inst_target_0x60'):
                return self._m_inst_target_0x60

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_target_0x60)
            self._m_inst_target_0x60 = []
            for i in range(self.array_count_for_0x60):
                self._m_inst_target_0x60.append(AnyGenesysObj.Ptr(u"genesys__gen__online_challenge_target", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_target_0x60', None)

        @property
        def inst_game_mode_0x20(self):
            if hasattr(self, '_m_inst_game_mode_0x20'):
                return self._m_inst_game_mode_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_game_mode_0x20)
            self._m_inst_game_mode_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_game_mode_0x20.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_game_mode_0x20', None)

        @property
        def inst_cgs_core__unique_id_0x10(self):
            if hasattr(self, '_m_inst_cgs_core__unique_id_0x10'):
                return self._m_inst_cgs_core__unique_id_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_core__unique_id_0x10)
            self._m_inst_cgs_core__unique_id_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_cgs_core__unique_id_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_core__unique_id_0x10', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3768680712
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCustomChevron(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_float32_t_0x10 = self._io.read_u4le()
            self.ptr_arr_float32_t_0x14 = self._io.read_u4le()
            self.ptr_arr_float32_t_0x18 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.array_count_for_0x14 = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.invert_normal_0x22 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def inst_float32_t_0x14(self):
            if hasattr(self, '_m_inst_float32_t_0x14'):
                return self._m_inst_float32_t_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_float32_t_0x14)
            self._m_inst_float32_t_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_float32_t_0x14.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_float32_t_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def inst_float32_t_0x10(self):
            if hasattr(self, '_m_inst_float32_t_0x10'):
                return self._m_inst_float32_t_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_float32_t_0x10)
            self._m_inst_float32_t_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_float32_t_0x10.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_float32_t_0x10', None)

        @property
        def inst_float32_t_0x18(self):
            if hasattr(self, '_m_inst_float32_t_0x18'):
                return self._m_inst_float32_t_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_float32_t_0x18)
            self._m_inst_float32_t_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_float32_t_0x18.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_float32_t_0x18', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2896762174
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWaveSequenceItemFade(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.curve_0xc = self._io.read_f4le()
            self.time_0x10 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1811326154
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesWorld(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.player_0xc = AnyGenesysObj.GenesysGenCollisionResponsesWorldPlayer(self._io, self, self._root)
            self.crashed_player_0x70 = AnyGenesysObj.GenesysGenCollisionResponsesWorldCrashedPlayer(self._io, self, self._root)
            self.in_air_player_0xb8 = AnyGenesysObj.GenesysGenCollisionResponsesWorldInAirPlayer(self._io, self, self._root)
            self.crashed_traffic_0xdc = AnyGenesysObj.GenesysGenCollisionResponsesWorldTraffic(self._io, self, self._root)
            self.traffic_0xf4 = AnyGenesysObj.GenesysGenCollisionResponsesWorldTraffic(self._io, self, self._root)
            self.game_changer_id_0x10c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 276
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1080225187
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDriftBehaviourSideForce(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 60
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2169095089
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHardDrivingBehaviourSteeringEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1685430085
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarAivsTraffic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ai__stable_0xc = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficDamageParams(self._io, self, self._root)
            self.ai__unstable_0x28 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficDamageParams(self._io, self, self._root)
            self.traffic__stable_0x44 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficDamageParams(self._io, self, self._root)
            self.traffic__unstable_0x60 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficDamageParams(self._io, self, self._root)
            self.ai__crashed_0x7c = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficBasicParams(self._io, self, self._root)
            self.ai__low__speed_0x94 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficBasicParams(self._io, self, self._root)
            self.traffic__low__speed_0xac = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficBasicParams(self._io, self, self._root)
            self.game_changer_id_0xc4 = self._io.read_u4le()
            self.friction_0xc8 = self._io.read_f4le()
            self.full__high__speed__mph_0xcc = self._io.read_f4le()
            self.full__low__speed__mph_0xd0 = self._io.read_f4le()
            self.restitution_0xd4 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 220
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3800105053
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenBodyMovementBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__body_movement_behaviour__take_off_behaviour_0xc = AnyGenesysObj.GenesysGenBodyMovementBehaviourTakeOffBehaviour(self._io, self, self._root)
            self.game_changer_id_0x50 = self._io.read_u4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.float32_t_0x58 = self._io.read_f4le()
            self.float32_t_0x5c = self._io.read_f4le()
            self.float32_t_0x60 = self._io.read_f4le()
            self.float32_t_0x64 = self._io.read_f4le()
            self.float32_t_0x68 = self._io.read_f4le()
            self.float32_t_0x6c = self._io.read_f4le()
            self.float32_t_0x70 = self._io.read_f4le()
            self.float32_t_0x74 = self._io.read_f4le()
            self.float32_t_0x78 = self._io.read_f4le()
            self.float32_t_0x7c = self._io.read_f4le()
            self.float32_t_0x80 = self._io.read_f4le()
            self.float32_t_0x84 = self._io.read_f4le()
            self.float32_t_0x88 = self._io.read_f4le()
            self.float32_t_0x8c = self._io.read_f4le()
            self.float32_t_0x90 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 152
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 106358757
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersSlipstreaming(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.minimum_speed_0x14 = self._io.read_f4le()
            self.min_slip_streaming_0x18 = self._io.read_f4le()
            self.nitrous_reward_0x1c = self._io.read_f4le()
            self.is_enabled_0x20 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1081328468
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenMixingGroup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.bus_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4049496118
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarBasicParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.linear__solve_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3106899705
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesGlobalTrafficVsDynamic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.dynamic__angular__solve_0x10 = self._io.read_f4le()
            self.dynamic__linear__solve_0x14 = self._io.read_f4le()
            self.restitution_0x18 = self._io.read_f4le()
            self.traffic__angular__solve_0x1c = self._io.read_f4le()
            self.traffic__linear__solve_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3080674119
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersRestrictions(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.nitrous_ready_message_0xc = self._io.read_u4le()
            self.min_nitrous_amount_0x10 = self._io.read_f4le()
            self.min_nitrous_punch_0x14 = self._io.read_f4le()
            self.min_nitrous_speed_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1377850816
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarAivsCrashingRaceCar(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.high__speed_0xc = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsCrashingRaceCarParams(self._io, self, self._root)
            self.low__speed_0x34 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsCrashingRaceCarParams(self._io, self, self._root)
            self.game_changer_id_0x5c = self._io.read_u4le()
            self.full__high__speed__mph_0x60 = self._io.read_f4le()
            self.full__low__speed__mph_0x64 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 108
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 722756325
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarProfile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.crashing__race__car__angular__solve_0x10 = self._io.read_f4le()
            self.crashing__race__car__linear__solve_0x14 = self._io.read_f4le()
            self.friction_0x18 = self._io.read_f4le()
            self.player__angular__solve_0x1c = self._io.read_f4le()
            self.player__linear__solve_0x20 = self._io.read_f4le()
            self.restitution_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4035751676
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRolloutWeaponData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.weapon_0xc = self._io.read_u4le()
            self.ptr_arr_weapon_upgrades_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_weapon_upgrades_0x10(self):
            if hasattr(self, '_m_inst_weapon_upgrades_0x10'):
                return self._m_inst_weapon_upgrades_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_weapon_upgrades_0x10)
            self._m_inst_weapon_upgrades_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_weapon_upgrades_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_weapon_upgrades_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2063558262
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWcplaySoundBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.offset_0x20 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.mixer_channel_0x30 = self._io.read_bytes(8)
            self.ptr_arr_cgs_resource__handle_0x38 = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x3c = self._io.read_u4le()
            self.ptr_arr_surface__collisions_0x40 = self._io.read_u4le()
            self.array_count_for_0x38 = self._io.read_u2le()
            self.array_count_for_0x3c = self._io.read_u2le()
            self.array_count_for_0x40 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_surface__collisions_0x40(self):
            if hasattr(self, '_m_inst_surface__collisions_0x40'):
                return self._m_inst_surface__collisions_0x40

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_surface__collisions_0x40)
            self._m_inst_surface__collisions_0x40 = []
            for i in range(self.array_count_for_0x40):
                self._m_inst_surface__collisions_0x40.append(AnyGenesysObj.GenesysGenWcplaySoundBehaviourPropSurfaceSound(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_surface__collisions_0x40', None)

        @property
        def inst_cgs_resource__handle_0x38(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x38'):
                return self._m_inst_cgs_resource__handle_0x38

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x38)
            self._m_inst_cgs_resource__handle_0x38 = []
            for i in range(self.array_count_for_0x38):
                self._m_inst_cgs_resource__handle_0x38.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x38', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def inst_cgs_resource__handle_0x3c(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x3c'):
                return self._m_inst_cgs_resource__handle_0x3c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x3c)
            self._m_inst_cgs_resource__handle_0x3c = []
            for i in range(self.array_count_for_0x3c):
                self._m_inst_cgs_resource__handle_0x3c.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x3c', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4218582003
            return getattr(self, '_m_mu_version_hash', None)


    class RwMathVpuVector3(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.inline_arr_elements_0x0 = []
            for i in range(3):
                self.inline_arr_elements_0x0.append(self._io.read_f4le())


        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 8
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2784336371
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarRaceCarVsDynamic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.race__car__invulnerable_0xc = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarRaceCarVsDynamicBasicParams(self._io, self, self._root)
            self.game_changer_id_0x24 = self._io.read_u4le()
            self.dynamic__angular__solve_0x28 = self._io.read_f4le()
            self.dynamic__linear__solve_0x2c = self._io.read_f4le()
            self.race__car__angular__solve_0x30 = self._io.read_f4le()
            self.race__car__linear__solve_0x34 = self._io.read_f4le()
            self.restitution_0x38 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 64
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2952229338
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodySphereVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.game_changer_id_0x50 = self._io.read_u4le()
            self.radius_0x54 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 92
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4179189423
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.collision__effects_0xc = self._io.read_bytes(8)
            self.damage__bars_0x14 = self._io.read_bytes(8)
            self.damage__graphs_0x1c = self._io.read_bytes(8)
            self.global__collision__responses_0x24 = self._io.read_bytes(8)
            self.race__car__collision__responses_0x2c = self._io.read_bytes(8)
            self.world__collision__responses_0x34 = self._io.read_bytes(8)
            self.game_changer_id_0x3c = self._io.read_u4le()
            self.average__world__strength_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.float32_t_0x4c = self._io.read_f4le()
            self.float32_t_0x50 = self._io.read_f4le()
            self.bloodstained_ends_0x54 = self._io.read_f4le()
            self.ptr_landing__damage_0x58 = self._io.read_u4le()

        @property
        def inst_landing__damage_0x58(self):
            if hasattr(self, '_m_inst_landing__damage_0x58'):
                return self._m_inst_landing__damage_0x58

            _pos = self._io.pos()
            self._io.seek(self.ptr_landing__damage_0x58)
            self._m_inst_landing__damage_0x58 = AnyGenesysObj.GenesysGenPhysicsLandingDamage(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_landing__damage_0x58', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1472679887
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalYawSpringModification(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.x_ryd_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 814214755
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenScoreViewModel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_scores_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_scores_0x10(self):
            if hasattr(self, '_m_inst_scores_0x10'):
                return self._m_inst_scores_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_scores_0x10)
            self._m_inst_scores_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_scores_0x10.append(AnyGenesysObj.GenesysGenScoreViewModelScore(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_scores_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1171375143
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleGameplayDamageStats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.uint16_t_0xc = self._io.read_u2le()
            self.uint16_t_0xe = self._io.read_u2le()
            self.uint16_t_0x10 = self._io.read_u2le()
            self.uint16_t_0x12 = self._io.read_u2le()
            self.uint16_t_0x14 = self._io.read_u2le()
            self.uint16_t_0x16 = self._io.read_u2le()
            self.strength_0x18 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 372702530
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreVfxBehaviourFrontRearParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params_0xc = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsSkidMarkParams(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params_0x9c = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsSmokeParams(self._io, self, self._root)
            self.game_changer_id_0x12c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 308
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 682066218
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyCapsuleVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.game_changer_id_0x50 = self._io.read_u4le()
            self.half_length_0x54 = self._io.read_f4le()
            self.radius_0x58 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 18021398
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleComponent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_resource__handle_0xc = self._io.read_bytes(8)
            self.category_0x14 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x1c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x24 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x2c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x34 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x3c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x44 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x4c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x54 = self._io.read_bytes(8)
            self.game_changer_id_0x5c = self._io.read_u4le()
            self.cgs_core__unique_id_0x60 = self._io.read_u4le()
            self.manufacturer_0x64 = self._io.read_u4le()
            self.name_0x68 = self._io.read_u4le()
            self.cgs_core__unique_id_0x6c = self._io.read_u4le()
            self.cgs_core__unique_id_0x70 = self._io.read_u4le()
            self.cgs_core__unique_id_0x74 = self._io.read_u4le()
            self.cgs_core__unique_id_0x78 = self._io.read_u4le()
            self.ptr_arr_cgs_core__unique_id_0x7c = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x80 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle_component__wheel_0x84 = self._io.read_u4le()
            self.array_count_for_0x7c = self._io.read_u2le()
            self.array_count_for_0x84 = self._io.read_u2le()
            self.bool8_t_0x8c = self._io.read_u1()
            self.bool8_t_0x8d = self._io.read_u1()
            self.bool8_t_0x8e = self._io.read_u1()
            self.bool8_t_0x8f = self._io.read_u1()
            self.bool8_t_0x90 = self._io.read_u1()
            self.bool8_t_0x91 = self._io.read_u1()
            self.bool8_t_0x92 = self._io.read_u1()
            self.bool8_t_0x93 = self._io.read_u1()
            self.array_count_for_0x80 = self._io.read_u1()
            self.uint8_t_0x95 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_genesys__gen__vehicle_component__wheel_0x84(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_component__wheel_0x84'):
                return self._m_inst_genesys__gen__vehicle_component__wheel_0x84

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle_component__wheel_0x84)
            self._m_inst_genesys__gen__vehicle_component__wheel_0x84 = []
            for i in range(self.array_count_for_0x84):
                self._m_inst_genesys__gen__vehicle_component__wheel_0x84.append(AnyGenesysObj.GenesysGenVehicleComponentWheel(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_component__wheel_0x84', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 152
            return getattr(self, '_m_size', None)

        @property
        def inst_cgs_core__unique_id_0x7c(self):
            if hasattr(self, '_m_inst_cgs_core__unique_id_0x7c'):
                return self._m_inst_cgs_core__unique_id_0x7c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_core__unique_id_0x7c)
            self._m_inst_cgs_core__unique_id_0x7c = []
            for i in range(self.array_count_for_0x7c):
                self._m_inst_cgs_core__unique_id_0x7c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_core__unique_id_0x7c', None)

        @property
        def inst_cgs_resource__handle_0x80(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x80'):
                return self._m_inst_cgs_resource__handle_0x80

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x80)
            self._m_inst_cgs_resource__handle_0x80 = []
            for i in range(self.array_count_for_0x80):
                self._m_inst_cgs_resource__handle_0x80.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x80', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3415849662
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPoint2dwithTangents(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenPoint2d(self._io, self, self._root)
            self.genesys__gen__point2d_0x18 = AnyGenesysObj.GenesysGenPoint2d(self._io, self, self._root)
            self.genesys__gen__point2d_0x30 = AnyGenesysObj.GenesysGenPoint2d(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 56
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1692280813
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPostFxKeyframeDepthOfField(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1600514099
            return getattr(self, '_m_mu_version_hash', None)


    class PtrTable(KaitaiStruct):
        def __init__(self, dtype, amt, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.dtype = dtype
            self.amt = amt
            self._read()

        def _read(self):
            self.entries = []
            for i in range(self.amt):
                self.entries.append(AnyGenesysObj.Ptr(self.dtype, self._io, self, self._root))



    class GenesysGenPostFxKeyframe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.vignette_0x10 = AnyGenesysObj.GenesysGenPostFxKeyframeVignette(self._io, self, self._root)
            self.bloom_0x80 = AnyGenesysObj.GenesysGenPostFxKeyframeBloom(self._io, self, self._root)
            self.general_0xd0 = AnyGenesysObj.GenesysGenPostFxKeyframeGeneral(self._io, self, self._root)
            self.genesys__gen__post_fx_keyframe__depth_of__field_0xf4 = AnyGenesysObj.GenesysGenPostFxKeyframeDepthOfField(self._io, self, self._root)
            self.stereo_3d_0x110 = AnyGenesysObj.GenesysGenPostFxKeyframeStereo3d(self._io, self, self._root)
            self.game_changer_id_0x128 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 304
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1519651292
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSubmixDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            self.uint16_t_0x18 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3483480738
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalDecelerationPitchChange(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 802364842
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayTriggerInput(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.trigger_0xc = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2634904179
            return getattr(self, '_m_mu_version_hash', None)


    class RwMathVpuMatrix44affine(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.inline_arr_elements_0x0 = []
            for i in range(4):
                self.inline_arr_elements_0x0.append(AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root))


        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 8
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3062587406
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOfflineEventCustomChevrons(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_arr_float32_t_0xc = self._io.read_u4le()
            self.ptr_arr_float32_t_0x10 = self._io.read_u4le()
            self.ptr_arr_float32_t_0x14 = self._io.read_u4le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.array_count_for_0x14 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_float32_t_0x14(self):
            if hasattr(self, '_m_inst_float32_t_0x14'):
                return self._m_inst_float32_t_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_float32_t_0x14)
            self._m_inst_float32_t_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_float32_t_0x14.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_float32_t_0x14', None)

        @property
        def inst_float32_t_0xc(self):
            if hasattr(self, '_m_inst_float32_t_0xc'):
                return self._m_inst_float32_t_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_float32_t_0xc)
            self._m_inst_float32_t_0xc = []
            for i in range(self.array_count_for_0xc):
                self._m_inst_float32_t_0xc.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_float32_t_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def inst_float32_t_0x10(self):
            if hasattr(self, '_m_inst_float32_t_0x10'):
                return self._m_inst_float32_t_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_float32_t_0x10)
            self._m_inst_float32_t_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_float32_t_0x10.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_float32_t_0x10', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 542473885
            return getattr(self, '_m_mu_version_hash', None)


    class Float32T(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenBusMixerChannelSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.ptr_arr_automated__values_0x28 = self._io.read_u4le()
            self.array_count_for_0x28 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_automated__values_0x28(self):
            if hasattr(self, '_m_inst_automated__values_0x28'):
                return self._m_inst_automated__values_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_automated__values_0x28)
            self._m_inst_automated__values_0x28 = []
            for i in range(self.array_count_for_0x28):
                self._m_inst_automated__values_0x28.append(AnyGenesysObj.GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_automated__values_0x28', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1198075180
            return getattr(self, '_m_mu_version_hash', None)


    class GenObj(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.dynamic_gamedata = self._io.read_bytes(8)
            self.mu_type_version = self._io.read_u4be()


    class GenesysGenOfflineEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenEvent(self._io, self, self._root)
            self.traffic_overrides_0x4c = self._io.read_bytes(8)
            self.ptr_arr_additional_assets_0x54 = self._io.read_u4le()
            self.ptr_arr_aihints_0x58 = self._io.read_u4le()
            self.allowed_vehicle_list_0x5c = self._io.read_u4le()
            self.maps_acceptors_0x60 = self._io.read_u4le()
            self.ptr_arr_checkpoints_0x64 = self._io.read_u4le()
            self.cgs_core__unique_id_0x68 = self._io.read_u4le()
            self.ptr_arr_default_heat_levels_0x6c = self._io.read_u4le()
            self.event_intro_0x70 = self._io.read_u4le()
            self.event_outro_0x74 = self._io.read_u4le()
            self.feedback_message_group_0x78 = self._io.read_u4le()
            self.ptr_arr_gameplay_triggers_0x7c = self._io.read_u4le()
            self.cgs_core__unique_id_0x80 = self._io.read_u4le()
            self.name_0x84 = self._io.read_u4le()
            self.name_formatted_0x88 = self._io.read_u4le()
            self.next_story_event_0x8c = self._io.read_u4le()
            self.cgs_core__unique_id_0x90 = self._io.read_u4le()
            self.race_balancing_data_0x94 = self._io.read_u4le()
            self.race_balancing_profile_0x98 = self._io.read_u4le()
            self.spawn_position_0x9c = self._io.read_u4le()
            self.ptr_arr_timeline_0xa0 = self._io.read_u4le()
            self.type_name_0xa4 = self._io.read_u4le()
            self.ptr_arr_target_speed_0xa8 = self._io.read_u4le()
            self.ptr_arr_target_time_0xac = self._io.read_u4le()
            self.traffic_density_0xb0 = self._io.read_f4le()
            self.ptr_arr_ptr_genesys__gen__chevron_0xb4 = self._io.read_u4le()
            self.ptr_arr_ptr_genesys__gen__custom_chevron_0xb8 = self._io.read_u4le()
            self.ptr_arr_ptr_conditions_0xbc = self._io.read_u4le()
            self.ptr_arr_aiplayers_0xc0 = self._io.read_u4le()
            self.ptr_arr_alternative_routes_0xc4 = self._io.read_u4le()
            self.ptr_arr_checkpoint_info_0xc8 = self._io.read_u4le()
            self.target_score_0xcc = self._io.read_u4le()
            self.demo_mode_0xd0 = self._io.read_u2le()
            self.array_count_for_0x54 = self._io.read_u2le()
            self.array_count_for_0x58 = self._io.read_u2le()
            self.array_count_for_0xc0 = self._io.read_u2le()
            self.array_count_for_0xc4 = self._io.read_u2le()
            self.array_count_for_0xc8 = self._io.read_u2le()
            self.array_count_for_0x64 = self._io.read_u2le()
            self.array_count_for_0x6c = self._io.read_u2le()
            self.array_count_for_0xb4 = self._io.read_u2le()
            self.array_count_for_0xa8 = self._io.read_u2le()
            self.array_count_for_0xac = self._io.read_u2le()
            self.array_count_for_0xa0 = self._io.read_u2le()
            self.cop_spawning_0xe8 = self._io.read_u1()
            self.bool8_t_0xe9 = self._io.read_u1()
            self.listens_pervade_0xea = self._io.read_u1()
            self.bool8_t_0xeb = self._io.read_u1()
            self.nitrous_allowed_0xec = self._io.read_u1()
            self.no_racing_line_traffic_0xed = self._io.read_u1()
            self.brightening_capsule_0xee = self._io.read_u1()
            self.start_with_engine_on_0xef = self._io.read_u1()
            self.traffic_enabled_0xf0 = self._io.read_u1()
            self.bool8_t_0xf1 = self._io.read_u1()
            self.weapons_allowed_0xf2 = self._io.read_u1()
            self.array_count_for_0xb8 = self._io.read_u1()
            self.array_count_for_0xbc = self._io.read_u1()
            self.array_count_for_0x7c = self._io.read_u1()
            self.laps_0xf6 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def inst_aihints_0x58(self):
            if hasattr(self, '_m_inst_aihints_0x58'):
                return self._m_inst_aihints_0x58

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_aihints_0x58)
            self._m_inst_aihints_0x58 = []
            for i in range(self.array_count_for_0x58):
                self._m_inst_aihints_0x58.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_aihints_0x58', None)

        @property
        def inst_alternative_routes_0xc4(self):
            if hasattr(self, '_m_inst_alternative_routes_0xc4'):
                return self._m_inst_alternative_routes_0xc4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_alternative_routes_0xc4)
            self._m_inst_alternative_routes_0xc4 = []
            for i in range(self.array_count_for_0xc4):
                self._m_inst_alternative_routes_0xc4.append(AnyGenesysObj.GenesysGenOfflineEventAlternateRoutes(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_alternative_routes_0xc4', None)

        @property
        def inst_checkpoint_info_0xc8(self):
            if hasattr(self, '_m_inst_checkpoint_info_0xc8'):
                return self._m_inst_checkpoint_info_0xc8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_checkpoint_info_0xc8)
            self._m_inst_checkpoint_info_0xc8 = []
            for i in range(self.array_count_for_0xc8):
                self._m_inst_checkpoint_info_0xc8.append(AnyGenesysObj.GenesysGenOfflineEventCheckpointInfo(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_checkpoint_info_0xc8', None)

        @property
        def inst_additional_assets_0x54(self):
            if hasattr(self, '_m_inst_additional_assets_0x54'):
                return self._m_inst_additional_assets_0x54

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_additional_assets_0x54)
            self._m_inst_additional_assets_0x54 = []
            for i in range(self.array_count_for_0x54):
                self._m_inst_additional_assets_0x54.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_additional_assets_0x54', None)

        @property
        def inst_timeline_0xa0(self):
            if hasattr(self, '_m_inst_timeline_0xa0'):
                return self._m_inst_timeline_0xa0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_timeline_0xa0)
            self._m_inst_timeline_0xa0 = []
            for i in range(self.array_count_for_0xa0):
                self._m_inst_timeline_0xa0.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_timeline_0xa0', None)

        @property
        def inst_gameplay_triggers_0x7c(self):
            if hasattr(self, '_m_inst_gameplay_triggers_0x7c'):
                return self._m_inst_gameplay_triggers_0x7c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_gameplay_triggers_0x7c)
            self._m_inst_gameplay_triggers_0x7c = []
            for i in range(self.array_count_for_0x7c):
                self._m_inst_gameplay_triggers_0x7c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_gameplay_triggers_0x7c', None)

        @property
        def inst_default_heat_levels_0x6c(self):
            if hasattr(self, '_m_inst_default_heat_levels_0x6c'):
                return self._m_inst_default_heat_levels_0x6c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_default_heat_levels_0x6c)
            self._m_inst_default_heat_levels_0x6c = []
            for i in range(self.array_count_for_0x6c):
                self._m_inst_default_heat_levels_0x6c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_default_heat_levels_0x6c', None)

        @property
        def inst_genesys__gen__custom_chevron_0xb8(self):
            if hasattr(self, '_m_inst_genesys__gen__custom_chevron_0xb8'):
                return self._m_inst_genesys__gen__custom_chevron_0xb8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_genesys__gen__custom_chevron_0xb8)
            self._m_inst_genesys__gen__custom_chevron_0xb8 = []
            for i in range(self.array_count_for_0xb8):
                self._m_inst_genesys__gen__custom_chevron_0xb8.append(AnyGenesysObj.Ptr(u"genesys__gen__custom_chevron", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__custom_chevron_0xb8', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 248
            return getattr(self, '_m_size', None)

        @property
        def inst_conditions_0xbc(self):
            if hasattr(self, '_m_inst_conditions_0xbc'):
                return self._m_inst_conditions_0xbc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_conditions_0xbc)
            self._m_inst_conditions_0xbc = []
            for i in range(self.array_count_for_0xbc):
                self._m_inst_conditions_0xbc.append(AnyGenesysObj.Ptr(u"genesys__gen__gameplay__condition", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_conditions_0xbc', None)

        @property
        def inst_aiplayers_0xc0(self):
            if hasattr(self, '_m_inst_aiplayers_0xc0'):
                return self._m_inst_aiplayers_0xc0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_aiplayers_0xc0)
            self._m_inst_aiplayers_0xc0 = []
            for i in range(self.array_count_for_0xc0):
                self._m_inst_aiplayers_0xc0.append(AnyGenesysObj.GenesysGenOfflineEventAiplayerInformation(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_aiplayers_0xc0', None)

        @property
        def inst_checkpoints_0x64(self):
            if hasattr(self, '_m_inst_checkpoints_0x64'):
                return self._m_inst_checkpoints_0x64

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_checkpoints_0x64)
            self._m_inst_checkpoints_0x64 = []
            for i in range(self.array_count_for_0x64):
                self._m_inst_checkpoints_0x64.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_checkpoints_0x64', None)

        @property
        def inst_target_time_0xac(self):
            if hasattr(self, '_m_inst_target_time_0xac'):
                return self._m_inst_target_time_0xac

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_target_time_0xac)
            self._m_inst_target_time_0xac = []
            for i in range(self.array_count_for_0xac):
                self._m_inst_target_time_0xac.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_target_time_0xac', None)

        @property
        def inst_target_speed_0xa8(self):
            if hasattr(self, '_m_inst_target_speed_0xa8'):
                return self._m_inst_target_speed_0xa8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_target_speed_0xa8)
            self._m_inst_target_speed_0xa8 = []
            for i in range(self.array_count_for_0xa8):
                self._m_inst_target_speed_0xa8.append(self._io.read_f4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_target_speed_0xa8', None)

        @property
        def inst_genesys__gen__chevron_0xb4(self):
            if hasattr(self, '_m_inst_genesys__gen__chevron_0xb4'):
                return self._m_inst_genesys__gen__chevron_0xb4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_genesys__gen__chevron_0xb4)
            self._m_inst_genesys__gen__chevron_0xb4 = []
            for i in range(self.array_count_for_0xb4):
                self._m_inst_genesys__gen__chevron_0xb4.append(AnyGenesysObj.Ptr(u"genesys__gen__chevron", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__chevron_0xb4', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2419838023
            return getattr(self, '_m_mu_version_hash', None)


    class Char(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenCollisionResponsesGlobalRaceCarVsRaceCar(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.stable_0xc = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCarParams(self._io, self, self._root)
            self.unstable_0x28 = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCarParams(self._io, self, self._root)
            self.crashed_0x44 = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCarCrashedParams(self._io, self, self._root)
            self.game_changer_id_0x5c = self._io.read_u4le()
            self.friction_0x60 = self._io.read_f4le()
            self.restitution_0x64 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 108
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3359156872
            return getattr(self, '_m_mu_version_hash', None)


    class Dummy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

        @property
        def d(self):
            if hasattr(self, '_m_d'):
                return self._m_d

            self._m_d = u"dummy"
            return getattr(self, '_m_d', None)


    class GenesysGenQuitSequenceTimelineController(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenJumpTimelineController(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1730251222
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDonutAbility(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__donut_ability__donut_grip_values_0xc = AnyGenesysObj.GenesysGenDonutAbilityDonutGripValues(self._io, self, self._root)
            self.genesys__gen__donut_ability__donut_scale_0x3c = AnyGenesysObj.GenesysGenDonutAbilityDonutScale(self._io, self, self._root)
            self.game_changer_id_0x5c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 100
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1394693111
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalGlobalsImpactShake(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.inline_arr_float32_t_0xc = []
            for i in range(3):
                self.inline_arr_float32_t_0xc.append(self._io.read_f4le())

            self.inline_arr_float32_t_0x18 = []
            for i in range(3):
                self.inline_arr_float32_t_0x18.append(self._io.read_f4le())

            self.inline_arr_float32_t_0x24 = []
            for i in range(3):
                self.inline_arr_float32_t_0x24.append(self._io.read_f4le())

            self.game_changer_id_0x30 = self._io.read_u4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.float32_t_0x4c = self._io.read_f4le()
            self.float32_t_0x50 = self._io.read_f4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.array_count_for_0x24 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2235640885
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersUsage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.decrease_nitrous_0x10 = self._io.read_f4le()
            self.time_to_full_nitrous_0x14 = self._io.read_f4le()
            self.enabled_0x18 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 401492861
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSequence(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.binding_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.binding__max_0x18 = self._io.read_f4le()
            self.binding__min_0x1c = self._io.read_f4le()
            self.ptr_arr_ptr_sequence_items_0x20 = self._io.read_u4le()
            self.ptr_arr_ptr_timeline_controllers_0x24 = self._io.read_u4le()
            self.default__progression__controller_0x28 = self._io.read_u2le()
            self.array_count_for_0x20 = self._io.read_u1()
            self.array_count_for_0x24 = self._io.read_u1()

        @property
        def inst_sequence_items_0x20(self):
            if hasattr(self, '_m_inst_sequence_items_0x20'):
                return self._m_inst_sequence_items_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_sequence_items_0x20)
            self._m_inst_sequence_items_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_sequence_items_0x20.append(AnyGenesysObj.Ptr(u"genesys__gen__sequence_item", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_sequence_items_0x20', None)

        @property
        def inst_timeline_controllers_0x24(self):
            if hasattr(self, '_m_inst_timeline_controllers_0x24'):
                return self._m_inst_timeline_controllers_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_timeline_controllers_0x24)
            self._m_inst_timeline_controllers_0x24 = []
            for i in range(self.array_count_for_0x24):
                self._m_inst_timeline_controllers_0x24.append(AnyGenesysObj.Ptr(u"genesys__gen__sequence_timeline_controller", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_timeline_controllers_0x24', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3910465619
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclesModifierUpgrade(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4117431335
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPidcontroller(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 48016591
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTrafficFlow(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.flow_type_0xc = self._io.read_bytes(8)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.density_0x20 = self._io.read_f4le()
            self.speed_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2949464142
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPostFxstate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.inline_arr_colour_cubes_0xc = []
            for i in range(2):
                self.inline_arr_colour_cubes_0xc.append(AnyGenesysObj.GenesysGenPostFxstateColourCubeSettings(self._io, self, self._root))

            self.bloom__value__modification_0x44 = AnyGenesysObj.GenesysGenPostFxstateValueModifier(self._io, self, self._root)
            self.colour__cube__value__modification_0x5c = AnyGenesysObj.GenesysGenPostFxstateValueModifier(self._io, self, self._root)
            self.dof__value__modification_0x74 = AnyGenesysObj.GenesysGenPostFxstateValueModifier(self._io, self, self._root)
            self.general__value__modification_0x8c = AnyGenesysObj.GenesysGenPostFxstateValueModifier(self._io, self, self._root)
            self.vignette__value__modification_0xa4 = AnyGenesysObj.GenesysGenPostFxstateValueModifier(self._io, self, self._root)
            self.activity_binding_0xbc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.keyframe_blend_binding_0xc4 = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.value_binding_0xcc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.key_frame1_0xd4 = self._io.read_bytes(8)
            self.key_frame2_0xdc = self._io.read_bytes(8)
            self.game_changer_id_0xe4 = self._io.read_u4le()
            self.rate_of_change_0xe8 = self._io.read_f4le()
            self.value_0xec = self._io.read_f4le()
            self.change_behaviour_0xf0 = self._io.read_u2le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.use__bloom_0xf4 = self._io.read_u1()
            self.use__dof_0xf5 = self._io.read_u1()
            self.use__general__fx_0xf6 = self._io.read_u1()
            self.use__vignette_0xf7 = self._io.read_u1()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 252
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 615742248
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesGlobalTrafficVsTraffic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.friction_0x14 = self._io.read_f4le()
            self.linear__solve_0x18 = self._io.read_f4le()
            self.restitution_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 963800229
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOnlineDrivingTestListGroup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.name_0x14 = self._io.read_u4le()
            self.ptr_arr_ptr_driving_test_list_0x18 = self._io.read_u4le()
            self.array_count_for_0x18 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_driving_test_list_0x18(self):
            if hasattr(self, '_m_inst_driving_test_list_0x18'):
                return self._m_inst_driving_test_list_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_driving_test_list_0x18)
            self._m_inst_driving_test_list_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_driving_test_list_0x18.append(AnyGenesysObj.Ptr(u"genesys__gen__online__driving_test_list", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_driving_test_list_0x18', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4182861931
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousStrengthJump(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3746299654
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreVfxBehaviourSkidMarkParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__long_lat_params_0xc = AnyGenesysObj.GenesysGenTyreVfxBehaviourLongLatParams(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__long_lat_params_0x30 = AnyGenesysObj.GenesysGenTyreVfxBehaviourLongLatParams(self._io, self, self._root)
            self.game_changer_id_0x54 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 92
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4159289097
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPaintPackGroup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_ptr_paint_packs_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_paint_packs_0x10(self):
            if hasattr(self, '_m_inst_paint_packs_0x10'):
                return self._m_inst_paint_packs_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_paint_packs_0x10)
            self._m_inst_paint_packs_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_paint_packs_0x10.append(AnyGenesysObj.Ptr(u"genesys__gen__paint_pack", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_paint_packs_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1913150235
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayBlacklistShutdownData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cloud_compete_award_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.cgs_core__unique_id_0x14 = self._io.read_u4le()
            self.cgs_core__unique_id_0x18 = self._io.read_u4le()
            self.name_0x1c = self._io.read_u4le()
            self.ptr_aiplayer_instance_0x20 = self._io.read_u4le()
            self.ptr_arr_damage_thresholds_0x24 = self._io.read_u4le()
            self.array_count_for_0x24 = self._io.read_u2le()
            self.blacklist_number_0x2a = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def inst_aiplayer_instance_0x20(self):
            if hasattr(self, '_m_inst_aiplayer_instance_0x20'):
                return self._m_inst_aiplayer_instance_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_aiplayer_instance_0x20)
            self._m_inst_aiplayer_instance_0x20 = AnyGenesysObj.GenesysGenAiplayerInstance(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_aiplayer_instance_0x20', None)

        @property
        def inst_damage_thresholds_0x24(self):
            if hasattr(self, '_m_inst_damage_thresholds_0x24'):
                return self._m_inst_damage_thresholds_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_damage_thresholds_0x24)
            self._m_inst_damage_thresholds_0x24 = []
            for i in range(self.array_count_for_0x24):
                self._m_inst_damage_thresholds_0x24.append(AnyGenesysObj.GenesysGenGameplayBlacklistShutdownDataDamageThreshold(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_damage_thresholds_0x24', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2262242598
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHeatLevel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.coordination_0xc = AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordination(self._io, self, self._root)
            self.cgs_core__unique_id_0x6c = self._io.read_u4le()
            self.game_changer_id_0x70 = self._io.read_u4le()
            self.helicopter_0x74 = self._io.read_u4le()
            self.aim_for_payload_time_0x78 = self._io.read_f4le()
            self.float32_t_0x7c = self._io.read_f4le()
            self.float32_t_0x80 = self._io.read_f4le()
            self.float32_t_0x84 = self._io.read_f4le()
            self.float32_t_0x88 = self._io.read_f4le()
            self.float32_t_0x8c = self._io.read_f4le()
            self.cop_hearing_range_for_idle_player_0x90 = self._io.read_f4le()
            self.cop_hearing_range_for_moving_player_0x94 = self._io.read_f4le()
            self.cop_sight_cone_angle_when_alert_0x98 = self._io.read_f4le()
            self.cop_sight_cone_angle_when_idle_0x9c = self._io.read_f4le()
            self.cop_sight_range_when_alert_0xa0 = self._io.read_f4le()
            self.cop_sight_range_when_chasing_0xa4 = self._io.read_f4le()
            self.cop_sight_range_when_idle_0xa8 = self._io.read_f4le()
            self.float32_t_0xac = self._io.read_f4le()
            self.float32_t_0xb0 = self._io.read_f4le()
            self.float32_t_0xb4 = self._io.read_f4le()
            self.float32_t_0xb8 = self._io.read_f4le()
            self.float32_t_0xbc = self._io.read_f4le()
            self.float32_t_0xc0 = self._io.read_f4le()
            self.float32_t_0xc4 = self._io.read_f4le()
            self.float32_t_0xc8 = self._io.read_f4le()
            self.float32_t_0xcc = self._io.read_f4le()
            self.float32_t_0xd0 = self._io.read_f4le()
            self.float32_t_0xd4 = self._io.read_f4le()
            self.float32_t_0xd8 = self._io.read_f4le()
            self.pursuit_radius_0xdc = self._io.read_f4le()
            self.search_radius_0xe0 = self._io.read_f4le()
            self.float32_t_0xe4 = self._io.read_f4le()
            self.float32_t_0xe8 = self._io.read_f4le()
            self.unk_enum_0xec = self._io.read_u4le()
            self.ptr_arr_formation_ahead_0xf0 = self._io.read_u4le()
            self.ptr_arr_uint8_t_0xf4 = self._io.read_u4le()
            self.ptr_arr_formation_behind_0xf8 = self._io.read_u4le()
            self.ptr_arr_uint8_t_0xfc = self._io.read_u4le()
            self.int16_t_0x100 = self._io.read_s2le()
            self.array_count_for_0xec = self._io.read_u2le()
            self.uint16_t_0x104 = self._io.read_u2le()
            self.array_count_for_0xf0 = self._io.read_u2le()
            self.array_count_for_0xf4 = self._io.read_u2le()
            self.array_count_for_0xf8 = self._io.read_u2le()
            self.array_count_for_0xfc = self._io.read_u2le()
            self.threshold_0x10e = self._io.read_u2le()
            self.allow_cooldown_0x110 = self._io.read_u1()
            self.bool8_t_0x111 = self._io.read_u1()
            self.force_cooldown_0x112 = self._io.read_u1()
            self.bool8_t_0x113 = self._io.read_u1()
            self.helicopter_permanent_0x114 = self._io.read_u1()
            self.aim_for_payload_angle_0x115 = self._io.read_u1()
            self.display_number_0x116 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def inst_formation_behind_0xf8(self):
            if hasattr(self, '_m_inst_formation_behind_0xf8'):
                return self._m_inst_formation_behind_0xf8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_formation_behind_0xf8)
            self._m_inst_formation_behind_0xf8 = []
            for i in range(self.array_count_for_0xf8):
                self._m_inst_formation_behind_0xf8.append(self._io.read_u1())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_formation_behind_0xf8', None)

        @property
        def inst_83_1d_10_00_0xec(self):
            if hasattr(self, '_m_inst_83_1d_10_00_0xec'):
                return self._m_inst_83_1d_10_00_0xec

            _pos = self._io.pos()
            self._io.seek(self.unk_enum_0xec)
            self._m_inst_83_1d_10_00_0xec = []
            for i in range(self.array_count_for_0xec):
                self._m_inst_83_1d_10_00_0xec.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_83_1d_10_00_0xec', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 280
            return getattr(self, '_m_size', None)

        @property
        def inst_formation_ahead_0xf0(self):
            if hasattr(self, '_m_inst_formation_ahead_0xf0'):
                return self._m_inst_formation_ahead_0xf0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_formation_ahead_0xf0)
            self._m_inst_formation_ahead_0xf0 = []
            for i in range(self.array_count_for_0xf0):
                self._m_inst_formation_ahead_0xf0.append(self._io.read_u1())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_formation_ahead_0xf0', None)

        @property
        def inst_uint8_t_0xfc(self):
            if hasattr(self, '_m_inst_uint8_t_0xfc'):
                return self._m_inst_uint8_t_0xfc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_uint8_t_0xfc)
            self._m_inst_uint8_t_0xfc = []
            for i in range(self.array_count_for_0xfc):
                self._m_inst_uint8_t_0xfc.append(self._io.read_u1())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_uint8_t_0xfc', None)

        @property
        def inst_uint8_t_0xf4(self):
            if hasattr(self, '_m_inst_uint8_t_0xf4'):
                return self._m_inst_uint8_t_0xf4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_uint8_t_0xf4)
            self._m_inst_uint8_t_0xf4 = []
            for i in range(self.array_count_for_0xf4):
                self._m_inst_uint8_t_0xf4.append(self._io.read_u1())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_uint8_t_0xf4', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1091853463
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenStorePackList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_store_packs_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_store_packs_0x10(self):
            if hasattr(self, '_m_inst_store_packs_0x10'):
                return self._m_inst_store_packs_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_store_packs_0x10)
            self._m_inst_store_packs_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_store_packs_0x10.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_store_packs_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3573113074
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOnlineEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenEvent(self._io, self, self._root)
            self.inline_arr_float32_t_0x4c = []
            for i in range(2):
                self.inline_arr_float32_t_0x4c.append(self._io.read_f4le())

            self.arena_0x54 = self._io.read_u4le()
            self.cgs_core__unique_id_0x58 = self._io.read_u4le()
            self.cgs_core__unique_id_0x5c = self._io.read_u4le()
            self.ptr_arr_cgs_core__unique_id_0x60 = self._io.read_u4le()
            self.route_0x64 = self._io.read_u4le()
            self.array_count_for_0x4c = self._io.read_u2le()
            self.array_count_for_0x60 = self._io.read_u2le()
            self.requires_airport_0x6c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_cgs_core__unique_id_0x60(self):
            if hasattr(self, '_m_inst_cgs_core__unique_id_0x60'):
                return self._m_inst_cgs_core__unique_id_0x60

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_core__unique_id_0x60)
            self._m_inst_cgs_core__unique_id_0x60 = []
            for i in range(self.array_count_for_0x60):
                self._m_inst_cgs_core__unique_id_0x60.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_core__unique_id_0x60', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 112
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 393413962
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameUnlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.entitlement__required_0xc = self._io.read_bytes(8)
            self.asset__to__unlock_0x14 = self._io.read_u4le()
            self.associated_asset_0x18 = self._io.read_u4le()
            self.challenge__target__required_0x1c = self._io.read_u4le()
            self.game_changer_id_0x20 = self._io.read_u4le()
            self.ptr_arr_required_assets_0x24 = self._io.read_u4le()
            self.sequence_0x28 = self._io.read_u4le()
            self.text_0x2c = self._io.read_u4le()
            self.bounty__required_0x30 = self._io.read_s4le()
            self.int32_t_0x34 = self._io.read_s4le()
            self.int32_t_0x38 = self._io.read_s4le()
            self.int32_t_0x3c = self._io.read_s4le()
            self.progression__type_0x40 = self._io.read_u2le()
            self.unlock_asset_type_0x42 = self._io.read_u2le()
            self.array_count_for_0x24 = self._io.read_u2le()
            self.is_enabled_0x46 = self._io.read_u1()
            self.is_silent_0x47 = self._io.read_u1()
            self.bool8_t_0x48 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_required_assets_0x24(self):
            if hasattr(self, '_m_inst_required_assets_0x24'):
                return self._m_inst_required_assets_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_required_assets_0x24)
            self._m_inst_required_assets_0x24 = []
            for i in range(self.array_count_for_0x24):
                self._m_inst_required_assets_0x24.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_required_assets_0x24', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3583346207
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDriftBehaviourYawTorque(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 68
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3547832794
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraRearViewGlobals(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 259534121
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPostFxKeyframeVignette(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.rw_math_vpu__vector2_0x10 = AnyGenesysObj.RwMathVpuVector2(self._io, self, self._root)
            self.scale_0x20 = AnyGenesysObj.RwMathVpuVector2(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x30 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x40 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.game_changer_id_0x50 = self._io.read_u4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.fisheye_power_0x58 = self._io.read_f4le()
            self.fisheye_scale_0x5c = self._io.read_f4le()
            self.fisheye_warp_0x60 = self._io.read_f4le()
            self.sharpness_0x64 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 108
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3180273648
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicsCrashingRules(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x10 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x14 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x18 = self._io.read_u4le()
            self.ptr_arr_landing_rules_0x1c = self._io.read_u4le()
            self.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x20 = self._io.read_u4le()
            self.ptr_arr_player_rules_0x24 = self._io.read_u4le()
            self.ptr_arr_props_rules_0x28 = self._io.read_u4le()
            self.ptr_arr_roadblock_rules_0x2c = self._io.read_u4le()
            self.ptr_arr_traffic_rules_0x30 = self._io.read_u4le()
            self.ptr_arr_world_rules_0x34 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.array_count_for_0x14 = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.array_count_for_0x1c = self._io.read_u2le()
            self.array_count_for_0x20 = self._io.read_u2le()
            self.array_count_for_0x24 = self._io.read_u2le()
            self.array_count_for_0x28 = self._io.read_u2le()
            self.array_count_for_0x2c = self._io.read_u2le()
            self.array_count_for_0x30 = self._io.read_u2le()
            self.array_count_for_0x34 = self._io.read_u2le()

        @property
        def inst_genesys__gen__physics__crashing_rules__impact_rules_0x18(self):
            if hasattr(self, '_m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x18'):
                return self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x18)
            self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x18.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x18', None)

        @property
        def inst_world_rules_0x34(self):
            if hasattr(self, '_m_inst_world_rules_0x34'):
                return self._m_inst_world_rules_0x34

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_world_rules_0x34)
            self._m_inst_world_rules_0x34 = []
            for i in range(self.array_count_for_0x34):
                self._m_inst_world_rules_0x34.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_world_rules_0x34', None)

        @property
        def inst_genesys__gen__physics__crashing_rules__impact_rules_0x20(self):
            if hasattr(self, '_m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x20'):
                return self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x20)
            self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x20.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x20', None)

        @property
        def inst_landing_rules_0x1c(self):
            if hasattr(self, '_m_inst_landing_rules_0x1c'):
                return self._m_inst_landing_rules_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_landing_rules_0x1c)
            self._m_inst_landing_rules_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_landing_rules_0x1c.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_landing_rules_0x1c', None)

        @property
        def inst_traffic_rules_0x30(self):
            if hasattr(self, '_m_inst_traffic_rules_0x30'):
                return self._m_inst_traffic_rules_0x30

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_traffic_rules_0x30)
            self._m_inst_traffic_rules_0x30 = []
            for i in range(self.array_count_for_0x30):
                self._m_inst_traffic_rules_0x30.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_traffic_rules_0x30', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 80
            return getattr(self, '_m_size', None)

        @property
        def inst_player_rules_0x24(self):
            if hasattr(self, '_m_inst_player_rules_0x24'):
                return self._m_inst_player_rules_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_player_rules_0x24)
            self._m_inst_player_rules_0x24 = []
            for i in range(self.array_count_for_0x24):
                self._m_inst_player_rules_0x24.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_player_rules_0x24', None)

        @property
        def inst_genesys__gen__physics__crashing_rules__impact_rules_0x14(self):
            if hasattr(self, '_m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x14'):
                return self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x14)
            self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x14.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x14', None)

        @property
        def inst_props_rules_0x28(self):
            if hasattr(self, '_m_inst_props_rules_0x28'):
                return self._m_inst_props_rules_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_props_rules_0x28)
            self._m_inst_props_rules_0x28 = []
            for i in range(self.array_count_for_0x28):
                self._m_inst_props_rules_0x28.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_props_rules_0x28', None)

        @property
        def inst_roadblock_rules_0x2c(self):
            if hasattr(self, '_m_inst_roadblock_rules_0x2c'):
                return self._m_inst_roadblock_rules_0x2c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_roadblock_rules_0x2c)
            self._m_inst_roadblock_rules_0x2c = []
            for i in range(self.array_count_for_0x2c):
                self._m_inst_roadblock_rules_0x2c.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_roadblock_rules_0x2c', None)

        @property
        def inst_genesys__gen__physics__crashing_rules__impact_rules_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x10'):
                return self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__physics__crashing_rules__impact_rules_0x10)
            self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x10.append(AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__physics__crashing_rules__impact_rules_0x10', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1912243431
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChevron(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.road_section_0x10 = self._io.read_u4le()
            self.should_block_start_0x14 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 850192155
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleColourPalette(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x10 = self._io.read_u4le()
            self.ptr_arr_ptr_genesys__gen__colour_group_0x14 = self._io.read_u4le()
            self.array_count_for_0x14 = self._io.read_u1()
            self.array_count_for_0x10 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_cgs_resource__handle_0x10(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x10'):
                return self._m_inst_cgs_resource__handle_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x10)
            self._m_inst_cgs_resource__handle_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_cgs_resource__handle_0x10.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x10', None)

        @property
        def inst_genesys__gen__colour_group_0x14(self):
            if hasattr(self, '_m_inst_genesys__gen__colour_group_0x14'):
                return self._m_inst_genesys__gen__colour_group_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_genesys__gen__colour_group_0x14)
            self._m_inst_genesys__gen__colour_group_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_genesys__gen__colour_group_0x14.append(AnyGenesysObj.Ptr(u"genesys__gen__colour_group", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__colour_group_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4062005660
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSendDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            self.voice__routing_0x1c = self._io.read_bytes(8)
            self.gain_0x24 = self._io.read_f4le()
            self.bus__routing_0x28 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 394812715
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalGlobals(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_external_globals__impact_shake_0xc = AnyGenesysObj.GenesysGenCameraGameplayExternalGlobalsImpactShake(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_external_globals__lens_properties_0x6c = AnyGenesysObj.GenesysGenCameraGameplayExternalGlobalsLensProperties(self._io, self, self._root)
            self.game_changer_id_0x88 = self._io.read_u4le()
            self.ptr_genesys__gen__camera_gameplay_shake_effect_0x8c = self._io.read_u4le()

        @property
        def inst_genesys__gen__camera_gameplay_shake_effect_0x8c(self):
            if hasattr(self, '_m_inst_genesys__gen__camera_gameplay_shake_effect_0x8c'):
                return self._m_inst_genesys__gen__camera_gameplay_shake_effect_0x8c

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__camera_gameplay_shake_effect_0x8c)
            self._m_inst_genesys__gen__camera_gameplay_shake_effect_0x8c = AnyGenesysObj.GenesysGenCameraGameplayShakeEffect(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__camera_gameplay_shake_effect_0x8c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 148
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3683195322
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersHighSpeed(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.nitrous_reward_0x14 = self._io.read_f4le()
            self.speed_percentage_0x18 = self._io.read_f4le()
            self.is_enabled_0x1c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2600311769
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreSoundParamsLongSpinBraking(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.ya_am_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3190011655
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGearboxGear(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3608189499
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHandbrakeAbilityHandbrakeGripValues(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1408090920
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCompoundAdditionalInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDynamicAdditionalInfo(self._io, self, self._root)
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 60
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3959582479
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineSound2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_resource__handle_0xc = self._io.read_bytes(8)
            self.cgs_resource__handle_0x14 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x1c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x24 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x2c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x34 = self._io.read_bytes(8)
            self.game_changer_id_0x3c = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x40 = self._io.read_u4le()
            self.ptr_arr_drift_0x44 = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x48 = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x4c = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x50 = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x54 = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x58 = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x5c = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x60 = self._io.read_u4le()
            self.ptr_arr_reversing_0x64 = self._io.read_u4le()
            self.ptr_arr_sequences_0x68 = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x6c = self._io.read_u4le()
            self.float32_t_0x70 = self._io.read_f4le()
            self.float32_t_0x74 = self._io.read_f4le()
            self.float32_t_0x78 = self._io.read_f4le()
            self.float32_t_0x7c = self._io.read_f4le()
            self.float32_t_0x80 = self._io.read_f4le()
            self.float32_t_0x84 = self._io.read_f4le()
            self.float32_t_0x88 = self._io.read_f4le()
            self.float32_t_0x8c = self._io.read_f4le()
            self.float32_t_0x90 = self._io.read_f4le()
            self.float32_t_0x94 = self._io.read_f4le()
            self.float32_t_0x98 = self._io.read_f4le()
            self.float32_t_0x9c = self._io.read_f4le()
            self.float32_t_0xa0 = self._io.read_f4le()
            self.float32_t_0xa4 = self._io.read_f4le()
            self.float32_t_0xa8 = self._io.read_f4le()
            self.float32_t_0xac = self._io.read_f4le()
            self.float32_t_0xb0 = self._io.read_f4le()
            self.float32_t_0xb4 = self._io.read_f4le()
            self.float32_t_0xb8 = self._io.read_f4le()
            self.float32_t_0xbc = self._io.read_f4le()
            self.float32_t_0xc0 = self._io.read_f4le()
            self.float32_t_0xc4 = self._io.read_f4le()
            self.float32_t_0xc8 = self._io.read_f4le()
            self.float32_t_0xcc = self._io.read_f4le()
            self.float32_t_0xd0 = self._io.read_f4le()
            self.float32_t_0xd4 = self._io.read_f4le()
            self.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__engine_sound2__gain_param_wrapper_0xe8 = self._io.read_u4le()
            self.array_count_for_0xd8 = self._io.read_u2le()
            self.array_count_for_0xdc = self._io.read_u2le()
            self.array_count_for_0xe8 = self._io.read_u2le()
            self.array_count_for_0xe0 = self._io.read_u2le()
            self.array_count_for_0xe4 = self._io.read_u2le()
            self.bool8_t_0xf6 = self._io.read_u1()
            self.array_count_for_0x40 = self._io.read_u1()
            self.array_count_for_0x44 = self._io.read_u1()
            self.array_count_for_0x4c = self._io.read_u1()
            self.array_count_for_0x48 = self._io.read_u1()
            self.array_count_for_0x54 = self._io.read_u1()
            self.array_count_for_0x50 = self._io.read_u1()
            self.array_count_for_0x58 = self._io.read_u1()
            self.array_count_for_0x5c = self._io.read_u1()
            self.array_count_for_0x60 = self._io.read_u1()
            self.uint8_t_0x100 = self._io.read_u1()
            self.array_count_for_0x64 = self._io.read_u1()
            self.array_count_for_0x68 = self._io.read_u1()
            self.array_count_for_0x6c = self._io.read_u1()

        @property
        def inst_cgs_resource__handle_0x54(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x54'):
                return self._m_inst_cgs_resource__handle_0x54

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x54)
            self._m_inst_cgs_resource__handle_0x54 = []
            for i in range(self.array_count_for_0x54):
                self._m_inst_cgs_resource__handle_0x54.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x54', None)

        @property
        def inst_cgs_resource__handle_0x40(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x40'):
                return self._m_inst_cgs_resource__handle_0x40

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x40)
            self._m_inst_cgs_resource__handle_0x40 = []
            for i in range(self.array_count_for_0x40):
                self._m_inst_cgs_resource__handle_0x40.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x40', None)

        @property
        def inst_cgs_resource__handle_0x4c(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x4c'):
                return self._m_inst_cgs_resource__handle_0x4c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x4c)
            self._m_inst_cgs_resource__handle_0x4c = []
            for i in range(self.array_count_for_0x4c):
                self._m_inst_cgs_resource__handle_0x4c.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x4c', None)

        @property
        def inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4(self):
            if hasattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4'):
                return self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4)
            self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4 = []
            for i in range(self.array_count_for_0xe4):
                self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4.append(AnyGenesysObj.GenesysGenEngineSound2DspParamWrapper(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe4', None)

        @property
        def inst_genesys__gen__engine_sound2__gain_param_wrapper_0xe8(self):
            if hasattr(self, '_m_inst_genesys__gen__engine_sound2__gain_param_wrapper_0xe8'):
                return self._m_inst_genesys__gen__engine_sound2__gain_param_wrapper_0xe8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__engine_sound2__gain_param_wrapper_0xe8)
            self._m_inst_genesys__gen__engine_sound2__gain_param_wrapper_0xe8 = []
            for i in range(self.array_count_for_0xe8):
                self._m_inst_genesys__gen__engine_sound2__gain_param_wrapper_0xe8.append(AnyGenesysObj.GenesysGenEngineSound2GainParamWrapper(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__engine_sound2__gain_param_wrapper_0xe8', None)

        @property
        def inst_reversing_0x64(self):
            if hasattr(self, '_m_inst_reversing_0x64'):
                return self._m_inst_reversing_0x64

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_reversing_0x64)
            self._m_inst_reversing_0x64 = []
            for i in range(self.array_count_for_0x64):
                self._m_inst_reversing_0x64.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_reversing_0x64', None)

        @property
        def inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8(self):
            if hasattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8'):
                return self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8)
            self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8 = []
            for i in range(self.array_count_for_0xd8):
                self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8.append(AnyGenesysObj.GenesysGenEngineSound2DspParamWrapper(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xd8', None)

        @property
        def inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0(self):
            if hasattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0'):
                return self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0)
            self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0 = []
            for i in range(self.array_count_for_0xe0):
                self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0.append(AnyGenesysObj.GenesysGenEngineSound2DspParamWrapper(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xe0', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 264
            return getattr(self, '_m_size', None)

        @property
        def inst_cgs_resource__handle_0x5c(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x5c'):
                return self._m_inst_cgs_resource__handle_0x5c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x5c)
            self._m_inst_cgs_resource__handle_0x5c = []
            for i in range(self.array_count_for_0x5c):
                self._m_inst_cgs_resource__handle_0x5c.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x5c', None)

        @property
        def inst_cgs_resource__handle_0x58(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x58'):
                return self._m_inst_cgs_resource__handle_0x58

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x58)
            self._m_inst_cgs_resource__handle_0x58 = []
            for i in range(self.array_count_for_0x58):
                self._m_inst_cgs_resource__handle_0x58.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x58', None)

        @property
        def inst_drift_0x44(self):
            if hasattr(self, '_m_inst_drift_0x44'):
                return self._m_inst_drift_0x44

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_drift_0x44)
            self._m_inst_drift_0x44 = []
            for i in range(self.array_count_for_0x44):
                self._m_inst_drift_0x44.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_drift_0x44', None)

        @property
        def inst_cgs_resource__handle_0x60(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x60'):
                return self._m_inst_cgs_resource__handle_0x60

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x60)
            self._m_inst_cgs_resource__handle_0x60 = []
            for i in range(self.array_count_for_0x60):
                self._m_inst_cgs_resource__handle_0x60.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x60', None)

        @property
        def inst_sequences_0x68(self):
            if hasattr(self, '_m_inst_sequences_0x68'):
                return self._m_inst_sequences_0x68

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_sequences_0x68)
            self._m_inst_sequences_0x68 = []
            for i in range(self.array_count_for_0x68):
                self._m_inst_sequences_0x68.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_sequences_0x68', None)

        @property
        def inst_cgs_resource__handle_0x6c(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x6c'):
                return self._m_inst_cgs_resource__handle_0x6c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x6c)
            self._m_inst_cgs_resource__handle_0x6c = []
            for i in range(self.array_count_for_0x6c):
                self._m_inst_cgs_resource__handle_0x6c.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x6c', None)

        @property
        def inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc(self):
            if hasattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc'):
                return self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc)
            self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc = []
            for i in range(self.array_count_for_0xdc):
                self._m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc.append(AnyGenesysObj.GenesysGenEngineSound2DspParamWrapper(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__engine_sound2__dsp_param_wrapper_0xdc', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1844756468
            return getattr(self, '_m_mu_version_hash', None)

        @property
        def inst_cgs_resource__handle_0x50(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x50'):
                return self._m_inst_cgs_resource__handle_0x50

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x50)
            self._m_inst_cgs_resource__handle_0x50 = []
            for i in range(self.array_count_for_0x50):
                self._m_inst_cgs_resource__handle_0x50.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x50', None)

        @property
        def inst_cgs_resource__handle_0x48(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x48'):
                return self._m_inst_cgs_resource__handle_0x48

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x48)
            self._m_inst_cgs_resource__handle_0x48 = []
            for i in range(self.array_count_for_0x48):
                self._m_inst_cgs_resource__handle_0x48.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x48', None)


    class GenesysGenDamageBarProfiles(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ai_0xc = self._io.read_bytes(8)
            self.impactor_sustaining_0x14 = self._io.read_bytes(8)
            self.player_online_0x1c = self._io.read_bytes(8)
            self.traffic_0x24 = self._io.read_bytes(8)
            self.game_changer_id_0x2c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3796279727
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclesUpgradeBase(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.icon_0x10 = self._io.read_u4le()
            self.name_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 889829961
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTrafficFlowType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_flow_type_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_flow_type_0x10(self):
            if hasattr(self, '_m_inst_flow_type_0x10'):
                return self._m_inst_flow_type_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_flow_type_0x10)
            self._m_inst_flow_type_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_flow_type_0x10.append(AnyGenesysObj.GenesysGenTrafficFlowTypeTrafficFlowType(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_flow_type_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 467841911
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleInfoAxle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_resource__handle_0xc = self._io.read_bytes(8)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x18 = self._io.read_u4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_cgs_resource__handle_0x18(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x18'):
                return self._m_inst_cgs_resource__handle_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x18)
            self._m_inst_cgs_resource__handle_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_cgs_resource__handle_0x18.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x18', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3440578930
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNucleusEntitlementTags(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_nucleus_tag_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_nucleus_tag_0x10(self):
            if hasattr(self, '_m_inst_nucleus_tag_0x10'):
                return self._m_inst_nucleus_tag_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_nucleus_tag_0x10)
            self._m_inst_nucleus_tag_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_nucleus_tag_0x10.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_nucleus_tag_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3131401224
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionEffectsBattlingEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__collision_effects__battling_effect__skid_effects_0xc = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffectSkidEffects(self._io, self, self._root)
            self.looser_shrinks_0x30 = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffectSkidEffects(self._io, self, self._root)
            self.genesys__gen__collision_effects__battling_effect__skid_effects_0x54 = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffectSkidEffects(self._io, self, self._root)
            self.genesys__gen__collision_effects__battling_effect__extra_roll_params_0x78 = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffectExtraRollParams(self._io, self, self._root)
            self.genesys__gen__collision_effects__battling_effect__extra_roll_params_0x90 = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffectExtraRollParams(self._io, self, self._root)
            self.cam__effect__stable_0xa8 = self._io.read_bytes(8)
            self.cam__effect__unstable_0xb0 = self._io.read_bytes(8)
            self.cam__effect__scale_0xb8 = self._io.read_f4le()
            self.stable__camera__threshold_0xbc = self._io.read_f4le()
            self.unstable__camera__threshold_0xc0 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 200
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4191696074
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarPlayerVsTraffic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.player__stable_0xc = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficDamageParams(self._io, self, self._root)
            self.player__unstable_0x28 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficDamageParams(self._io, self, self._root)
            self.traffic__stable_0x44 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficDamageParams(self._io, self, self._root)
            self.traffic__unstable_0x60 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficDamageParams(self._io, self, self._root)
            self.player__crashed_0x7c = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficBasicParams(self._io, self, self._root)
            self.player__invulnerable_0x94 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficBasicParams(self._io, self, self._root)
            self.player__low__speed_0xac = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficBasicParams(self._io, self, self._root)
            self.traffic__low__speed_0xc4 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficBasicParams(self._io, self, self._root)
            self.game_changer_id_0xdc = self._io.read_u4le()
            self.float32_t_0xe0 = self._io.read_f4le()
            self.friction_0xe4 = self._io.read_f4le()
            self.full__high__speed__mph_0xe8 = self._io.read_f4le()
            self.full__low__speed__mph_0xec = self._io.read_f4le()
            self.restitution_0xf0 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 248
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1680453612
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclesVehicleCategoryInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.description_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.name_0x14 = self._io.read_u4le()
            self.cgs_core__unique_id_0x18 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 760083
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersTrafficNearMiss(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.minimum_speed_0x14 = self._io.read_f4le()
            self.nitrous_reward_0x18 = self._io.read_f4le()
            self.is_enabled_0x1c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4256545587
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayShakeEffectRotation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.pitch_0xc = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectRotationAxisParams(self._io, self, self._root)
            self.roll_0x34 = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectRotationAxisParams(self._io, self, self._root)
            self.yaw_0x5c = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectRotationAxisParams(self._io, self, self._root)
            self.game_changer_id_0x84 = self._io.read_u4le()
            self.amplitude_0x88 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 144
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1220037810
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionEffectsBattlingEffectSkidEffects(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.high_damage_skid_effect_0xc = self._io.read_bytes(8)
            self.low_damage_skid_effect_0x14 = self._io.read_bytes(8)
            self.high_damage_for_skid_effect_0x1c = self._io.read_f4le()
            self.low_damage_for_skid_effect_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 61953676
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayAllowedVehicleList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10'):
                return self._m_inst_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10)
            self._m_inst_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10.append(AnyGenesysObj.GenesysGenGameplayAllowedVehicleListVehicleAndMods(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3992764498
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarPhysicalDefinitionConvexHullConectivityDataConvexHullConnectingFace(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x10 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x20 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.game_changer_id_0x30 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 56
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1001882986
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.enabled_binding_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.end_time_0x18 = self._io.read_f4le()
            self.start_time_0x1c = self._io.read_f4le()
            self.unk_enum_0x20 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1822997286
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWcvfxBehaviourLights(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.light_definition_0xc = self._io.read_bytes(8)
            self.locator_group_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3229542978
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVoiceGroup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.instance_limit_0x10 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1655947362
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTrafficVehicleTraits(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.acceleration_0x10 = self._io.read_f4le()
            self.scale_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2593852305
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenScoringAction(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.predicate_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.gameplay_trigger_0x18 = self._io.read_u4le()
            self.sequence_0x1c = self._io.read_u4le()
            self.title_0x20 = self._io.read_u4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.ptr_arr_online_feedback_0x28 = self._io.read_u4le()
            self.ptr_arr_uint32_t_0x2c = self._io.read_u4le()
            self.ptr_arr_score_0x30 = self._io.read_u4le()
            self.ptr_arr_initiates_raids_0x34 = self._io.read_u4le()
            self.scope_0x38 = self._io.read_u2le()
            self.queue_0x3a = self._io.read_u2le()
            self.array_count_for_0x2c = self._io.read_u2le()
            self.array_count_for_0x28 = self._io.read_u2le()
            self.array_count_for_0x30 = self._io.read_u2le()
            self.array_count_for_0x34 = self._io.read_u2le()
            self.bool8_t_0x44 = self._io.read_u1()
            self.feedback_deferrable_0x45 = self._io.read_u1()
            self.priority_0x46 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 72
            return getattr(self, '_m_size', None)

        @property
        def inst_online_feedback_0x28(self):
            if hasattr(self, '_m_inst_online_feedback_0x28'):
                return self._m_inst_online_feedback_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_online_feedback_0x28)
            self._m_inst_online_feedback_0x28 = []
            for i in range(self.array_count_for_0x28):
                self._m_inst_online_feedback_0x28.append(AnyGenesysObj.GenesysGenScoringActionOnlineScoringFeedback(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_online_feedback_0x28', None)

        @property
        def inst_score_0x30(self):
            if hasattr(self, '_m_inst_score_0x30'):
                return self._m_inst_score_0x30

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_score_0x30)
            self._m_inst_score_0x30 = []
            for i in range(self.array_count_for_0x30):
                self._m_inst_score_0x30.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_score_0x30', None)

        @property
        def inst_uint32_t_0x2c(self):
            if hasattr(self, '_m_inst_uint32_t_0x2c'):
                return self._m_inst_uint32_t_0x2c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_uint32_t_0x2c)
            self._m_inst_uint32_t_0x2c = []
            for i in range(self.array_count_for_0x2c):
                self._m_inst_uint32_t_0x2c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_uint32_t_0x2c', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2631887699
            return getattr(self, '_m_mu_version_hash', None)

        @property
        def inst_initiates_raids_0x34(self):
            if hasattr(self, '_m_inst_initiates_raids_0x34'):
                return self._m_inst_initiates_raids_0x34

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_initiates_raids_0x34)
            self._m_inst_initiates_raids_0x34 = []
            for i in range(self.array_count_for_0x34):
                self._m_inst_initiates_raids_0x34.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_initiates_raids_0x34', None)


    class GenesysGenCarSelectDataSequences(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_sequences_0x10 = self._io.read_u4le()
            self.time_0x14 = self._io.read_s4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_sequences_0x10(self):
            if hasattr(self, '_m_inst_sequences_0x10'):
                return self._m_inst_sequences_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_sequences_0x10)
            self._m_inst_sequences_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_sequences_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_sequences_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1668851487
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSequenceItemsPostFxOverrideSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.automated__values_count_0x28 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3664056692
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPostFxstateColourCubeSettings(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.colour_cube_0xc = self._io.read_bytes(8)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.zero__if__not__set_0x18 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2006186034
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOfflineEventAiplayerInformation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.aiplayer_type_0xc = self._io.read_u4le()
            self.back_up_colour_0x10 = self._io.read_u4le()
            self.placement_0x14 = self._io.read_u4le()
            self.primary_colour_0x18 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 616120463
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionEffects(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.battling__collision__effect_0xc = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffect(self._io, self, self._root)
            self.traffic__collision__effect_0xd0 = AnyGenesysObj.GenesysGenCollisionEffectsTrafficEffect(self._io, self, self._root)
            self.world__collision__effect_0x140 = AnyGenesysObj.GenesysGenCollisionEffectsWorldEffect(self._io, self, self._root)
            self.game_changer_id_0x168 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 368
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1763676845
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOnlineChallengeTarget(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.award_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.uint32_t_0x14 = self._io.read_u4le()
            self.xp_0x18 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2078321761
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTrafficVehicle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.positive_pitch__negative_pitch__yaw__roll_0x10 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.trailer_0x20 = self._io.read_bytes(8)
            self.traits_0x28 = self._io.read_bytes(8)
            self.game_changer_id_0x30 = self._io.read_u4le()
            self.vehicle_component_0x34 = self._io.read_u4le()
            self.score_0x38 = self._io.read_u4le()
            self.bool8_t_0x3c = self._io.read_u1()
            self.use_thick_wheel_smoke_0x3d = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 64
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3395112625
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCoronaFlare(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.unk_enum_0x10 = self._io.read_u1()
            self.colour_0xa0 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0xb0 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.material_0xc0 = self._io.read_bytes(8)
            self.position_0xc8 = self._io.read_f4le()
            self.rotation_offset_0xcc = self._io.read_f4le()
            self.render_buffer_0xd0 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 216
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3357198890
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionInfoDamageProfile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.minimum__damage_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2331975734
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarPlayerVsAiDamageParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.damage_0x14 = self._io.read_f4le()
            self.linear__solve_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2956570466
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHeatLevelSoundSet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.nitrous_dump_0xc = self._io.read_bytes(8)
            self.nitrous_local_0x14 = self._io.read_bytes(8)
            self.game_changer_id_0x1c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 456164053
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalAccelerationMovement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 64
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2041922261
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalSpeedBasedMovement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake_0xc = AnyGenesysObj.GenesysGenCameraGameplayExternalSpeedBasedMovementHighSpeedShake(self._io, self, self._root)
            self.game_changer_id_0x30 = self._io.read_u4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1963215010
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionInfoWorldEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cam__effect_0xc = self._io.read_bytes(8)
            self.cam__effect__scale_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2501750206
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionAccumulateTakedowns(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3616117713
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreVfxBehaviourSmokeParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__long_lat_params_0xc = AnyGenesysObj.GenesysGenTyreVfxBehaviourLongLatParams(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__long_lat_params_0x30 = AnyGenesysObj.GenesysGenTyreVfxBehaviourLongLatParams(self._io, self, self._root)
            self.game_changer_id_0x54 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 92
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3643052795
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesGlobalDynamicVsDynamic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.linear__solve_0x14 = self._io.read_f4le()
            self.restitution_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3907892408
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPostFxKeyframeBloom(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.colour_0x10 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.game_changer_id_0x20 = self._io.read_u4le()
            self.dark_bloom_weight_0x24 = self._io.read_f4le()
            self.dark_bloom_white_point_0x28 = self._io.read_f4le()
            self.large_weight_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.medium_weight_0x34 = self._io.read_f4le()
            self.saturation_0x38 = self._io.read_f4le()
            self.small_weight_0x3c = self._io.read_f4le()
            self.threshold_0x40 = self._io.read_f4le()
            self.threshold_large_0x44 = self._io.read_f4le()
            self.threshold_medium_0x48 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 80
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3592057837
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWcplaySoundBehaviourPropSurfaceSound(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.surface_0x10 = self._io.read_u4le()
            self.ptr_arr_rolling__waves_0x14 = self._io.read_u4le()
            self.ptr_arr_scraping__waves_0x18 = self._io.read_u4le()
            self.ptr_arr_waves_0x1c = self._io.read_u4le()
            self.array_count_for_0x14 = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.array_count_for_0x1c = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_waves_0x1c(self):
            if hasattr(self, '_m_inst_waves_0x1c'):
                return self._m_inst_waves_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_waves_0x1c)
            self._m_inst_waves_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_waves_0x1c.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_waves_0x1c', None)

        @property
        def inst_rolling__waves_0x14(self):
            if hasattr(self, '_m_inst_rolling__waves_0x14'):
                return self._m_inst_rolling__waves_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_rolling__waves_0x14)
            self._m_inst_rolling__waves_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_rolling__waves_0x14.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_rolling__waves_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def inst_scraping__waves_0x18(self):
            if hasattr(self, '_m_inst_scraping__waves_0x18'):
                return self._m_inst_scraping__waves_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_scraping__waves_0x18)
            self._m_inst_scraping__waves_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_scraping__waves_0x18.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_scraping__waves_0x18', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3115085927
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayDriftMarker(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.cgs_core__unique_id_0x14 = self._io.read_u4le()
            self.safety_trigger_0x18 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 835486276
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.rw_math_vpu__matrix44affine_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x50 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x60 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x70 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.game_changer_id_0x80 = self._io.read_u4le()
            self.float32_t_0x84 = self._io.read_f4le()
            self.float32_t_0x88 = self._io.read_f4le()
            self.float32_t_0x8c = self._io.read_f4le()
            self.float32_t_0x90 = self._io.read_f4le()
            self.float32_t_0x94 = self._io.read_f4le()
            self.ptr_arr_genesys__gen__vehicle_info__axle_0x98 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle_info__extra_axle_0x9c = self._io.read_u4le()
            self.array_count_for_0x98 = self._io.read_u2le()
            self.array_count_for_0x9c = self._io.read_u2le()
            self.bool8_t_0xa4 = self._io.read_u1()
            self.bool8_t_0xa5 = self._io.read_u1()
            self.bool8_t_0xa6 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def inst_genesys__gen__vehicle_info__axle_0x98(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_info__axle_0x98'):
                return self._m_inst_genesys__gen__vehicle_info__axle_0x98

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle_info__axle_0x98)
            self._m_inst_genesys__gen__vehicle_info__axle_0x98 = []
            for i in range(self.array_count_for_0x98):
                self._m_inst_genesys__gen__vehicle_info__axle_0x98.append(AnyGenesysObj.GenesysGenVehicleInfoAxle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_info__axle_0x98', None)

        @property
        def inst_genesys__gen__vehicle_info__extra_axle_0x9c(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_info__extra_axle_0x9c'):
                return self._m_inst_genesys__gen__vehicle_info__extra_axle_0x9c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle_info__extra_axle_0x9c)
            self._m_inst_genesys__gen__vehicle_info__extra_axle_0x9c = []
            for i in range(self.array_count_for_0x9c):
                self._m_inst_genesys__gen__vehicle_info__extra_axle_0x9c.append(AnyGenesysObj.GenesysGenVehicleInfoExtraAxle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_info__extra_axle_0x9c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 168
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3954992488
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayShakeEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.translation_0xc = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectTranslation(self._io, self, self._root)
            self.rotation_0xa4 = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectRotation(self._io, self, self._root)
            self.game_changer_id_0x130 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 312
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3580468080
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarPlayerVsTrafficBasicParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.linear__solve_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2144572099
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSteeringWheelBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.cgs_resource__handle_0x1c = self._io.read_bytes(8)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3124672599
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersTakingShortcut(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.minimum_speed_0x14 = self._io.read_f4le()
            self.nitrous_reward_0x18 = self._io.read_f4le()
            self.is_enabled_0x1c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1687823060
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleDamageBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.cgs_resource__handle_0x1c = self._io.read_bytes(8)
            self.ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart_0x24 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c = self._io.read_u4le()
            self.array_count_for_0x24 = self._io.read_u2le()
            self.array_count_for_0x28 = self._io.read_u2le()
            self.array_count_for_0x2c = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c'):
                return self._m_inst_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c)
            self._m_inst_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c = []
            for i in range(self.array_count_for_0x2c):
                self._m_inst_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c.append(AnyGenesysObj.GenesysGenVehicleDamageBehaviourSpotEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_damage_behaviour__spot_effect_0x2c', None)

        @property
        def inst_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28'):
                return self._m_inst_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28)
            self._m_inst_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28 = []
            for i in range(self.array_count_for_0x28):
                self._m_inst_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28.append(AnyGenesysObj.GenesysGenVehicleDamageBehaviourDamageSequence(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_damage_behaviour__damage_sequence_0x28', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 56
            return getattr(self, '_m_size', None)

        @property
        def inst_genesys__gen__vehicle_damage_behaviour__bodypart_0x24(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_damage_behaviour__bodypart_0x24'):
                return self._m_inst_genesys__gen__vehicle_damage_behaviour__bodypart_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart_0x24)
            self._m_inst_genesys__gen__vehicle_damage_behaviour__bodypart_0x24 = []
            for i in range(self.array_count_for_0x24):
                self._m_inst_genesys__gen__vehicle_damage_behaviour__bodypart_0x24.append(AnyGenesysObj.GenesysGenVehicleDamageBehaviourBodypart(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_damage_behaviour__bodypart_0x24', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1880813572
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayMilestone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__unique_id_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.name_0x14 = self._io.read_u4le()
            self.progress_0x18 = self._io.read_u4le()
            self.ptr_arr_entries_0x1c = self._io.read_u4le()
            self.stat_0x20 = self._io.read_u2le()
            self.array_count_for_0x1c = self._io.read_u2le()

        @property
        def inst_entries_0x1c(self):
            if hasattr(self, '_m_inst_entries_0x1c'):
                return self._m_inst_entries_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_entries_0x1c)
            self._m_inst_entries_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_entries_0x1c.append(AnyGenesysObj.GenesysGenGameplayMilestoneEntry(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_entries_0x1c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1320933699
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenLfoSequenceItemLfoDoubleValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_value_0xc = self._io.read_u4le()
            self.automated__property_0x10 = self._io.read_u4le()

        @property
        def inst_value_0xc(self):
            if hasattr(self, '_m_inst_value_0xc'):
                return self._m_inst_value_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_value_0xc)
            self._m_inst_value_0xc = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_value_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4097165157
            return getattr(self, '_m_mu_version_hash', None)


    class StringBase(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ofs_arr_buffer_0x0 = self._io.read_u4le()
            self.array_count_for_0x0 = self._io.read_u4le()

        @property
        def inst_buffer_0x0(self):
            if hasattr(self, '_m_inst_buffer_0x0'):
                return self._m_inst_buffer_0x0

            _pos = self._io.pos()
            self._io.seek(self.ofs_arr_buffer_0x0)
            self._m_inst_buffer_0x0 = (self._io.read_bytes(self.array_count_for_0x0)).decode(u"ascii")
            self._io.seek(_pos)
            return getattr(self, '_m_inst_buffer_0x0', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 12
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2516314814
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayShakeEffectRotationAxisParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.amplitude_0x10 = self._io.read_f4le()
            self.damping_0x14 = self._io.read_f4le()
            self.maximum__angle_0x18 = self._io.read_f4le()
            self.minimum__angle_0x1c = self._io.read_f4le()
            self.spring__coefficient_0x20 = self._io.read_f4le()
            self.invert__force__direction_0x24 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3652314633
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleDamageBehaviourBodypart(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.rw_math_vpu__vector2_0x10 = AnyGenesysObj.RwMathVpuVector2(self._io, self, self._root)
            self.rw_math_vpu__vector2_0x20 = AnyGenesysObj.RwMathVpuVector2(self._io, self, self._root)
            self.rw_math_vpu__vector2_0x30 = AnyGenesysObj.RwMathVpuVector2(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x40 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x50 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x60 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x70 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x80 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.cgs_core__string_base_0x90 = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.cgs_resource__handle_0x98 = self._io.read_bytes(8)
            self.game_changer_id_0xa0 = self._io.read_u4le()
            self.locator_group_0xa4 = self._io.read_u4le()
            self.mass_0xa8 = self._io.read_f4le()
            self.ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac = self._io.read_u4le()
            self.unk_enum_0xb0 = self._io.read_u2le()
            self.array_count_for_0xac = self._io.read_u2le()
            self.bool8_t_0xb4 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac'):
                return self._m_inst_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac)
            self._m_inst_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac = []
            for i in range(self.array_count_for_0xac):
                self._m_inst_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac.append(AnyGenesysObj.GenesysGenVehicleDamageBehaviourBodypartDamageThreshold(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold_0xac', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 184
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 509958626
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesGlobalCrashingRaceCarVsCrashingRaceCar(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.friction_0x14 = self._io.read_f4le()
            self.linear__solve_0x18 = self._io.read_f4le()
            self.restitution_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1186319577
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternal(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_external__speed_based_movement_0xc = AnyGenesysObj.GenesysGenCameraGameplayExternalSpeedBasedMovement(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_external__acceleration_movement_0x54 = AnyGenesysObj.GenesysGenCameraGameplayExternalAccelerationMovement(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_external__camera__roll_0x90 = AnyGenesysObj.GenesysGenCameraGameplayExternalCameraRoll(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_external__yaw_spring_modification_0xbc = AnyGenesysObj.GenesysGenCameraGameplayExternalYawSpringModification(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_external__deceleration__pitch__change_0xe8 = AnyGenesysObj.GenesysGenCameraGameplayExternalDecelerationPitchChange(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_external__speed_based_height_change_0x10c = AnyGenesysObj.GenesysGenCameraGameplayExternalSpeedBasedHeightChange(self._io, self, self._root)
            self.inline_arr_float32_t_0x124 = []
            for i in range(3):
                self.inline_arr_float32_t_0x124.append(self._io.read_f4le())

            self.inline_arr_float32_t_0x130 = []
            for i in range(3):
                self.inline_arr_float32_t_0x130.append(self._io.read_f4le())

            self.inline_arr_float32_t_0x13c = []
            for i in range(3):
                self.inline_arr_float32_t_0x13c.append(self._io.read_f4le())

            self.inline_arr_float32_t_0x148 = []
            for i in range(3):
                self.inline_arr_float32_t_0x148.append(self._io.read_f4le())

            self.cgs_resource__handle_0x154 = self._io.read_bytes(8)
            self.game_changer_id_0x15c = self._io.read_u4le()
            self.float32_t_0x160 = self._io.read_f4le()
            self.float32_t_0x164 = self._io.read_f4le()
            self.float32_t_0x168 = self._io.read_f4le()
            self.float32_t_0x16c = self._io.read_f4le()
            self.float32_t_0x170 = self._io.read_f4le()
            self.ptr_genesys__gen__camera_gameplay_external_globals_0x174 = self._io.read_u4le()
            self.ptr_genesys__gen__camera_gameplay_gradient_adjustments_0x178 = self._io.read_u4le()
            self.array_count_for_0x124 = self._io.read_u2le()
            self.array_count_for_0x130 = self._io.read_u2le()
            self.array_count_for_0x13c = self._io.read_u2le()
            self.array_count_for_0x148 = self._io.read_u2le()
            self.uint8_t_0x184 = self._io.read_u1()
            self.uint8_t_0x185 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_genesys__gen__camera_gameplay_external_globals_0x174(self):
            if hasattr(self, '_m_inst_genesys__gen__camera_gameplay_external_globals_0x174'):
                return self._m_inst_genesys__gen__camera_gameplay_external_globals_0x174

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__camera_gameplay_external_globals_0x174)
            self._m_inst_genesys__gen__camera_gameplay_external_globals_0x174 = AnyGenesysObj.GenesysGenCameraGameplayExternalGlobals(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__camera_gameplay_external_globals_0x174', None)

        @property
        def inst_genesys__gen__camera_gameplay_gradient_adjustments_0x178(self):
            if hasattr(self, '_m_inst_genesys__gen__camera_gameplay_gradient_adjustments_0x178'):
                return self._m_inst_genesys__gen__camera_gameplay_gradient_adjustments_0x178

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__camera_gameplay_gradient_adjustments_0x178)
            self._m_inst_genesys__gen__camera_gameplay_gradient_adjustments_0x178 = AnyGenesysObj.GenesysGenCameraGameplayGradientAdjustments(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__camera_gameplay_gradient_adjustments_0x178', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 392
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3148721321
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_modulating_value_0xc = self._io.read_u4le()
            self.bus_mixer_channel_property_0x10 = self._io.read_u4le()

        @property
        def inst_modulating_value_0xc(self):
            if hasattr(self, '_m_inst_modulating_value_0xc'):
                return self._m_inst_modulating_value_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_modulating_value_0xc)
            self._m_inst_modulating_value_0xc = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_modulating_value_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3626200052
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyresSurfaceEffects(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_genesys__gen__vehicle_surface_profile_0x10 = self._io.read_u4le()

        @property
        def inst_genesys__gen__vehicle_surface_profile_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_surface_profile_0x10'):
                return self._m_inst_genesys__gen__vehicle_surface_profile_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicle_surface_profile_0x10)
            self._m_inst_genesys__gen__vehicle_surface_profile_0x10 = AnyGenesysObj.GenesysGenVehicleSurfaceProfile(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_surface_profile_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1530679421
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleGameplayModEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.value_0xc = self._io.read_f4le()
            self.stat_0x10 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3434016526
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicsLandingDamage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.pitch_0xc = AnyGenesysObj.GenesysGenPhysicsLandingDamagePitch(self._io, self, self._root)
            self.roll_0x30 = AnyGenesysObj.GenesysGenPhysicsLandingDamageRoll(self._io, self, self._root)
            self.game_changer_id_0x50 = self._io.read_u4le()
            self.float32_t_0x54 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 92
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2607248643
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleComponentWheel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__unique_id_0xc = self._io.read_u4le()
            self.type_0x10 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2583194568
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleVfxBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.ptr_arr_coronas_0x1c = self._io.read_u4le()
            self.ptr_arr_lights_0x20 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24 = self._io.read_u4le()
            self.array_count_for_0x1c = self._io.read_u2le()
            self.array_count_for_0x20 = self._io.read_u2le()
            self.array_count_for_0x24 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_lights_0x20(self):
            if hasattr(self, '_m_inst_lights_0x20'):
                return self._m_inst_lights_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_lights_0x20)
            self._m_inst_lights_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_lights_0x20.append(AnyGenesysObj.GenesysGenVehicleVfxBehaviourLight(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_lights_0x20', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def inst_coronas_0x1c(self):
            if hasattr(self, '_m_inst_coronas_0x1c'):
                return self._m_inst_coronas_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_coronas_0x1c)
            self._m_inst_coronas_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_coronas_0x1c.append(AnyGenesysObj.GenesysGenVehicleVfxBehaviourCorona(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_coronas_0x1c', None)

        @property
        def inst_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24'):
                return self._m_inst_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24)
            self._m_inst_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24 = []
            for i in range(self.array_count_for_0x24):
                self._m_inst_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24.append(AnyGenesysObj.GenesysGenVehicleVfxBehaviourSpotEffect(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicle_vfx_behaviour__spot_effect_0x24', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3302002317
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNucleusGrantMappingsList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_items_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_items_0x10(self):
            if hasattr(self, '_m_inst_items_0x10'):
                return self._m_inst_items_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_items_0x10)
            self._m_inst_items_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_items_0x10.append(AnyGenesysObj.GenesysGenNucleusGrantMappingsListMapping(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_items_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 975568910
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayExternalSpeedBasedMovementHighSpeedShake(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.amplitude_0x10 = self._io.read_f4le()
            self.frequency_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.power_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3791727622
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRoadblockInstance(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.placement_0x10 = self._io.read_u4le()
            self.type_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2089690370
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPaintPack(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.colour_0xc = self._io.read_u4le()
            self.cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.image_0x18 = self._io.read_u4le()
            self.livery_0x1c = self._io.read_u4le()
            self.name_0x20 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 832200604
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWcvfxBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.impact_effect_0x1c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x24 = self._io.read_bytes(8)
            self.flash_frequency_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.nonprocedurally_slocum_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.ptr_arr_coronas_0x40 = self._io.read_u4le()
            self.ptr_arr_lights_0x44 = self._io.read_u4le()
            self.ptr_arr_genesys__gen__wcvfx_behaviour__spot_effects_0x48 = self._io.read_u4le()
            self.int32_t_0x4c = self._io.read_s4le()
            self.int32_t_0x50 = self._io.read_s4le()
            self.array_count_for_0x40 = self._io.read_u2le()
            self.array_count_for_0x44 = self._io.read_u2le()
            self.array_count_for_0x48 = self._io.read_u2le()
            self.bool8_t_0x5a = self._io.read_u1()
            self.bool8_t_0x5b = self._io.read_u1()
            self.bool8_t_0x5c = self._io.read_u1()
            self.bool8_t_0x5d = self._io.read_u1()
            self.bool8_t_0x5e = self._io.read_u1()
            self.bool8_t_0x5f = self._io.read_u1()
            self.bool8_t_0x60 = self._io.read_u1()
            self.bool8_t_0x61 = self._io.read_u1()
            self.bool8_t_0x62 = self._io.read_u1()
            self.bool8_t_0x63 = self._io.read_u1()
            self.bool8_t_0x64 = self._io.read_u1()
            self.bool8_t_0x65 = self._io.read_u1()
            self.bool8_t_0x66 = self._io.read_u1()
            self.bool8_t_0x67 = self._io.read_u1()
            self.bool8_t_0x68 = self._io.read_u1()
            self.bool8_t_0x69 = self._io.read_u1()
            self.bool8_t_0x6a = self._io.read_u1()
            self.bool8_t_0x6b = self._io.read_u1()

        @property
        def inst_lights_0x44(self):
            if hasattr(self, '_m_inst_lights_0x44'):
                return self._m_inst_lights_0x44

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_lights_0x44)
            self._m_inst_lights_0x44 = []
            for i in range(self.array_count_for_0x44):
                self._m_inst_lights_0x44.append(AnyGenesysObj.GenesysGenWcvfxBehaviourLights(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_lights_0x44', None)

        @property
        def inst_genesys__gen__wcvfx_behaviour__spot_effects_0x48(self):
            if hasattr(self, '_m_inst_genesys__gen__wcvfx_behaviour__spot_effects_0x48'):
                return self._m_inst_genesys__gen__wcvfx_behaviour__spot_effects_0x48

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__wcvfx_behaviour__spot_effects_0x48)
            self._m_inst_genesys__gen__wcvfx_behaviour__spot_effects_0x48 = []
            for i in range(self.array_count_for_0x48):
                self._m_inst_genesys__gen__wcvfx_behaviour__spot_effects_0x48.append(AnyGenesysObj.GenesysGenWcvfxBehaviourSpotEffects(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__wcvfx_behaviour__spot_effects_0x48', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 112
            return getattr(self, '_m_size', None)

        @property
        def inst_coronas_0x40(self):
            if hasattr(self, '_m_inst_coronas_0x40'):
                return self._m_inst_coronas_0x40

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_coronas_0x40)
            self._m_inst_coronas_0x40 = []
            for i in range(self.array_count_for_0x40):
                self._m_inst_coronas_0x40.append(AnyGenesysObj.GenesysGenWcvfxBehaviourCoronas(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_coronas_0x40', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3464877079
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPeakingDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            self.gain_0x18 = self._io.read_f4le()
            self.q_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3263786457
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionInfoBattlingDamage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3587969770
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenBodyMovementBehaviourAngleControl(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.damping_0xc = self._io.read_f4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3023685899
            return getattr(self, '_m_mu_version_hash', None)


    class RwMathVpuVector2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.inline_arr_elements_0x0 = []
            for i in range(2):
                self.inline_arr_elements_0x0.append(self._io.read_f4le())


        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 8
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 786918963
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesGlobalRaceCarVsRaceCarCrashedParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.linear__solve_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1231510099
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenAiplayerInstance(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.back_up_colour_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.primary_colour_0x14 = self._io.read_u4le()
            self.type_0x18 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3691324629
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleDamageBehaviourSpotEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_resource__handle_0xc = self._io.read_bytes(8)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.locator_group_0x18 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4117767557
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicalDefinition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.local_aabbcenter_0x10 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.local_aabbhalf_diagonal_0x20 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.additional_info_0x30 = self._io.read_bytes(8)
            self.ptr_arr_rigid_bodies_names_0x38 = self._io.read_u4le()
            self.game_changer_id_0x3c = self._io.read_u4le()
            self.ptr_arr_rigid_bodies_0x40 = self._io.read_u4le()
            self.game_changer_id_0x44 = self._io.read_s4le()
            self.main_rigid_body_index_0x48 = self._io.read_s4le()
            self.array_count_for_0x40 = self._io.read_u2le()
            self.array_count_for_0x38 = self._io.read_u2le()
            self.bool8_t_0x50 = self._io.read_u1()
            self.bool8_t_0x51 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_rigid_bodies_names_0x38(self):
            if hasattr(self, '_m_inst_rigid_bodies_names_0x38'):
                return self._m_inst_rigid_bodies_names_0x38

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_rigid_bodies_names_0x38)
            self._m_inst_rigid_bodies_names_0x38 = []
            for i in range(self.array_count_for_0x38):
                self._m_inst_rigid_bodies_names_0x38.append(AnyGenesysObj.StringBase(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_rigid_bodies_names_0x38', None)

        @property
        def inst_rigid_bodies_0x40(self):
            if hasattr(self, '_m_inst_rigid_bodies_0x40'):
                return self._m_inst_rigid_bodies_0x40

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_rigid_bodies_0x40)
            self._m_inst_rigid_bodies_0x40 = []
            for i in range(self.array_count_for_0x40):
                self._m_inst_rigid_bodies_0x40.append(AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBody(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_rigid_bodies_0x40', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 84
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2519567673
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEventCheckpointInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.sequence_0xc = self._io.read_u4le()
            self.show_split_time_0x10 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2571445580
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHighShelfDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            self.gain_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4149479710
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDamageBarProfilesProfileSegmentData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.damage_to_leave_segment_0x10 = self._io.read_f4le()
            self.segment_0x14 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 542430507
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDriftBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__drift_behaviour__other_0xc = AnyGenesysObj.GenesysGenDriftBehaviourOther(self._io, self, self._root)
            self.genesys__gen__drift_behaviour__yaw_torque_0x54 = AnyGenesysObj.GenesysGenDriftBehaviourYawTorque(self._io, self, self._root)
            self.genesys__gen__drift_behaviour__side_force_0x94 = AnyGenesysObj.GenesysGenDriftBehaviourSideForce(self._io, self, self._root)
            self.genesys__gen__drift_behaviour__drift_scale_0xcc = AnyGenesysObj.GenesysGenDriftBehaviourDriftScale(self._io, self, self._root)
            self.genesys__gen__drift_behaviour__drift_exit_0x100 = AnyGenesysObj.GenesysGenDriftBehaviourDriftExit(self._io, self, self._root)
            self.genesys__gen__drift_behaviour__drift_trigger_0x128 = AnyGenesysObj.GenesysGenDriftBehaviourDriftTrigger(self._io, self, self._root)
            self.game_changer_id_0x14c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 340
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4274679117
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreVfxBehaviourFrontRearParamsLongParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3032331154
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionAccumulateDistance(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3815813836
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGinsuSequenceItemFade(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.curve_0xc = self._io.read_f4le()
            self.time_0x10 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3237867664
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSequenceTimelineController(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.enabled_binding_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.trigger_type_0x18 = self._io.read_u2le()
            self.test_continuously_0x1a = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4067794056
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenThankyouMapping(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.nucleus_entitlement_0xc = self._io.read_bytes(8)
            self.thankyou_item_0x14 = self._io.read_bytes(8)
            self.entitlement_0x1c = self._io.read_u4le()
            self.game_changer_id_0x20 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 451352474
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHardDrivingBehaviourGasEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 68
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1021288769
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarAivsCrashingRaceCarParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ai__angular__solve_0x10 = self._io.read_f4le()
            self.ai__linear__solve_0x14 = self._io.read_f4le()
            self.crashing__race__car__angular__solve_0x18 = self._io.read_f4le()
            self.crashing__race__car__linear__solve_0x1c = self._io.read_f4le()
            self.friction_0x20 = self._io.read_f4le()
            self.restitution_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2957925672
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreVfxBehaviourFrontRearParamsSmokeParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params_0xc = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLatParams(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x3c = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLongParams(self._io, self, self._root)
            self.genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params_0x64 = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLongParams(self._io, self, self._root)
            self.game_changer_id_0x8c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 148
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1711822367
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEventArenaData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.loading__point__location_0x10 = self._io.read_u4le()
            self.ptr_arr_lockdown_points_0x14 = self._io.read_u4le()
            self.ptr_arr_point_to_point_checkpoints_0x18 = self._io.read_u4le()
            self.ptr_arr_repair_points_0x1c = self._io.read_u4le()
            self.ptr_arr_spawn__locations_0x20 = self._io.read_u4le()
            self.vista_camera_location_0x24 = self._io.read_u4le()
            self.ptr_arr_ptr_chevrons_0x28 = self._io.read_u4le()
            self.ptr_arr_ptr_custom_chevron_list_0x2c = self._io.read_u4le()
            self.ptr_arr_team_spawn_locations_0x30 = self._io.read_u4le()
            self.array_count_for_0x28 = self._io.read_u2le()
            self.array_count_for_0x14 = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.array_count_for_0x1c = self._io.read_u2le()
            self.array_count_for_0x20 = self._io.read_u2le()
            self.array_count_for_0x30 = self._io.read_u2le()
            self.array_count_for_0x2c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_point_to_point_checkpoints_0x18(self):
            if hasattr(self, '_m_inst_point_to_point_checkpoints_0x18'):
                return self._m_inst_point_to_point_checkpoints_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_point_to_point_checkpoints_0x18)
            self._m_inst_point_to_point_checkpoints_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_point_to_point_checkpoints_0x18.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_point_to_point_checkpoints_0x18', None)

        @property
        def inst_repair_points_0x1c(self):
            if hasattr(self, '_m_inst_repair_points_0x1c'):
                return self._m_inst_repair_points_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_repair_points_0x1c)
            self._m_inst_repair_points_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_repair_points_0x1c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_repair_points_0x1c', None)

        @property
        def inst_chevrons_0x28(self):
            if hasattr(self, '_m_inst_chevrons_0x28'):
                return self._m_inst_chevrons_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_chevrons_0x28)
            self._m_inst_chevrons_0x28 = []
            for i in range(self.array_count_for_0x28):
                self._m_inst_chevrons_0x28.append(AnyGenesysObj.Ptr(u"genesys__gen__chevron", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_chevrons_0x28', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 68
            return getattr(self, '_m_size', None)

        @property
        def inst_lockdown_points_0x14(self):
            if hasattr(self, '_m_inst_lockdown_points_0x14'):
                return self._m_inst_lockdown_points_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_lockdown_points_0x14)
            self._m_inst_lockdown_points_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_lockdown_points_0x14.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_lockdown_points_0x14', None)

        @property
        def inst_team_spawn_locations_0x30(self):
            if hasattr(self, '_m_inst_team_spawn_locations_0x30'):
                return self._m_inst_team_spawn_locations_0x30

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_team_spawn_locations_0x30)
            self._m_inst_team_spawn_locations_0x30 = []
            for i in range(self.array_count_for_0x30):
                self._m_inst_team_spawn_locations_0x30.append(AnyGenesysObj.GenesysGenEventArenaDataSpawnPointCollection(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_team_spawn_locations_0x30', None)

        @property
        def inst_custom_chevron_list_0x2c(self):
            if hasattr(self, '_m_inst_custom_chevron_list_0x2c'):
                return self._m_inst_custom_chevron_list_0x2c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_custom_chevron_list_0x2c)
            self._m_inst_custom_chevron_list_0x2c = []
            for i in range(self.array_count_for_0x2c):
                self._m_inst_custom_chevron_list_0x2c.append(AnyGenesysObj.Ptr(u"genesys__gen__custom_chevron", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_custom_chevron_list_0x2c', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2270583296
            return getattr(self, '_m_mu_version_hash', None)

        @property
        def inst_spawn__locations_0x20(self):
            if hasattr(self, '_m_inst_spawn__locations_0x20'):
                return self._m_inst_spawn__locations_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_spawn__locations_0x20)
            self._m_inst_spawn__locations_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_spawn__locations_0x20.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_spawn__locations_0x20', None)


    class GenesysGenChallengeActionCarState(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.float32_t_0x4c = self._io.read_f4le()
            self.float32_t_0x50 = self._io.read_f4le()
            self.max_speed_0x54 = self._io.read_u2le()
            self.min_speed_0x56 = self._io.read_u2le()
            self.bool8_t_0x58 = self._io.read_u1()
            self.bool8_t_0x59 = self._io.read_u1()
            self.bool8_t_0x5a = self._io.read_u1()
            self.donutting_0x5b = self._io.read_u1()
            self.drifting_0x5c = self._io.read_u1()
            self.in_air_0x5d = self._io.read_u1()
            self.nitrous_0x5e = self._io.read_u1()
            self.bool8_t_0x5f = self._io.read_u1()
            self.reversing_0x60 = self._io.read_u1()
            self.slipstreaming_0x61 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 100
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 174008559
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWaveSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.pitch_0x5c = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self.fade__in_0x94 = AnyGenesysObj.GenesysGenWaveSequenceItemFade(self._io, self, self._root)
            self.fade__out_0xa8 = AnyGenesysObj.GenesysGenWaveSequenceItemFade(self._io, self, self._root)
            self.snapshot__property_0xbc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.transform__override__binding_0xc4 = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.mixer__channel_0xcc = self._io.read_bytes(8)
            self.ptr_arr_waves_0xd4 = self._io.read_u4le()
            self.ptr_arr_trigger__probability_0xd8 = self._io.read_u4le()
            self.re_trigger_0xdc = self._io.read_u2le()
            self.type_0xde = self._io.read_u2le()
            self.auto__pitch_0xe0 = self._io.read_u1()
            self.array_count_for_0xd8 = self._io.read_u1()
            self.array_count_for_0xd4 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def inst_waves_0xd4(self):
            if hasattr(self, '_m_inst_waves_0xd4'):
                return self._m_inst_waves_0xd4

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_waves_0xd4)
            self._m_inst_waves_0xd4 = []
            for i in range(self.array_count_for_0xd4):
                self._m_inst_waves_0xd4.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_waves_0xd4', None)

        @property
        def inst_trigger__probability_0xd8(self):
            if hasattr(self, '_m_inst_trigger__probability_0xd8'):
                return self._m_inst_trigger__probability_0xd8

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_trigger__probability_0xd8)
            self._m_inst_trigger__probability_0xd8 = []
            for i in range(self.array_count_for_0xd8):
                self._m_inst_trigger__probability_0xd8.append(AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_trigger__probability_0xd8', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 228
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1722819130
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreSoundParamsLateral(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 564124160
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayBonnet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.inline_arr_float32_t_0xc = []
            for i in range(3):
                self.inline_arr_float32_t_0xc.append(self._io.read_f4le())

            self.inline_arr_float32_t_0x18 = []
            for i in range(3):
                self.inline_arr_float32_t_0x18.append(self._io.read_f4le())

            self.inline_arr_float32_t_0x24 = []
            for i in range(3):
                self.inline_arr_float32_t_0x24.append(self._io.read_f4le())

            self.game_changer_id_0x30 = self._io.read_u4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.float32_t_0x4c = self._io.read_f4le()
            self.float32_t_0x50 = self._io.read_f4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.float32_t_0x58 = self._io.read_f4le()
            self.float32_t_0x5c = self._io.read_f4le()
            self.float32_t_0x60 = self._io.read_f4le()
            self.float32_t_0x64 = self._io.read_f4le()
            self.float32_t_0x68 = self._io.read_f4le()
            self.float32_t_0x6c = self._io.read_f4le()
            self.int32_t_0x70 = self._io.read_s4le()
            self.int32_t_0x74 = self._io.read_s4le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.array_count_for_0x24 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 128
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3342396752
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyre(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__tyre__lateral__slip__factors_0xc = AnyGenesysObj.GenesysGenTyreLateralSlipFactors(self._io, self, self._root)
            self.genesys__gen__tyre__lateral__slip__factors_0x30 = AnyGenesysObj.GenesysGenTyreLateralSlipFactors(self._io, self, self._root)
            self.genesys__gen__tyre__lateral__grip__curve_0x54 = AnyGenesysObj.GenesysGenTyreLateralGripCurve(self._io, self, self._root)
            self.genesys__gen__tyre__lateral__grip__curve_0x74 = AnyGenesysObj.GenesysGenTyreLateralGripCurve(self._io, self, self._root)
            self.genesys__gen__tyre__lateral__grip__curve_0x94 = AnyGenesysObj.GenesysGenTyreLateralGripCurve(self._io, self, self._root)
            self.genesys__gen__tyre__long__grip__curve_0xb4 = AnyGenesysObj.GenesysGenTyreLongGripCurve(self._io, self, self._root)
            self.genesys__gen__tyre__long__grip__curve_0xd4 = AnyGenesysObj.GenesysGenTyreLongGripCurve(self._io, self, self._root)
            self.genesys__gen__tyre__long__grip__curve_0xf4 = AnyGenesysObj.GenesysGenTyreLongGripCurve(self._io, self, self._root)
            self.genesys__gen__tyre__long__grip__curve_0x114 = AnyGenesysObj.GenesysGenTyreLongGripCurve(self._io, self, self._root)
            self.genesys__gen__tyre__long__slip__factors_0x134 = AnyGenesysObj.GenesysGenTyreLongSlipFactors(self._io, self, self._root)
            self.genesys__gen__tyre__long__slip__factors_0x154 = AnyGenesysObj.GenesysGenTyreLongSlipFactors(self._io, self, self._root)
            self.game_changer_id_0x174 = self._io.read_u4le()
            self.float32_t_0x178 = self._io.read_f4le()
            self.float32_t_0x17c = self._io.read_f4le()
            self.float32_t_0x180 = self._io.read_f4le()
            self.float32_t_0x184 = self._io.read_f4le()
            self.float32_t_0x188 = self._io.read_f4le()
            self.float32_t_0x18c = self._io.read_f4le()
            self.float32_t_0x190 = self._io.read_f4le()
            self.float32_t_0x194 = self._io.read_f4le()
            self.float32_t_0x198 = self._io.read_f4le()
            self.float32_t_0x19c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 420
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 21856074
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceBalancingProfile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.max_speed_0x10 = self._io.read_f4le()
            self.min_speed_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2776745689
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenColourGroup(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.primary_colour_0xc = self._io.read_bytes(8)
            self.cgs_resource__handle_0x14 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x1c = self._io.read_bytes(8)
            self.game_changer_id_0x24 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1259832621
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDistortionDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            self.model_0x18 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3181724531
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleSurfaceProfileSurfaceLink(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_cgs_core__unique_id_0x10(self):
            if hasattr(self, '_m_inst_cgs_core__unique_id_0x10'):
                return self._m_inst_cgs_core__unique_id_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_core__unique_id_0x10)
            self._m_inst_cgs_core__unique_id_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_cgs_core__unique_id_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_core__unique_id_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 60
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 283467013
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersSpeedbreakerUsage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenNitrousParametersUsage(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2522613547
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleVfxBehaviourSpotEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_resource__handle_0xc = self._io.read_bytes(8)
            self.locator_group_0x14 = self._io.read_u4le()
            self.unk_enum_0x18 = self._io.read_u2le()
            self.time_of_day_0x1a = self._io.read_u2le()
            self.bool8_t_0x1c = self._io.read_u1()
            self.bool8_t_0x1d = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2169939698
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicalDefinitionRigidBodySphereVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.game_changer_id_0x50 = self._io.read_u4le()
            self.radius_0x54 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 92
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4179189423
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersNitrousUsage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenNitrousParametersUsage(self._io, self, self._root)
            self.min_nitrous_time_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 80463996
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicsLandingDamageRoll(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3635654829
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenStorePack(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.pack_item_0xc = self._io.read_bytes(8)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.ptr_arr_content_items_0x18 = self._io.read_u4le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_content_items_0x18(self):
            if hasattr(self, '_m_inst_content_items_0x18'):
                return self._m_inst_content_items_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_content_items_0x18)
            self._m_inst_content_items_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_content_items_0x18.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_content_items_0x18', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3071320584
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHandbrakeAbility(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4002008184
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPerformanceModifier(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_ptr_modifications_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_modifications_0x10(self):
            if hasattr(self, '_m_inst_modifications_0x10'):
                return self._m_inst_modifications_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_modifications_0x10)
            self._m_inst_modifications_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_modifications_0x10.append(AnyGenesysObj.Ptr(u"genesys__gen__performance_modification_item", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_modifications_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3000817087
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWheelSuspensionConstraint(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angle_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.bool8_t_0x28 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2076212613
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesGlobal(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.race__car__vs__race__car_0xc = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCar(self._io, self, self._root)
            self.crashing__race__car__vs__traffic_0x74 = AnyGenesysObj.GenesysGenCollisionResponsesGlobalCrashingRaceCarVsTraffic(self._io, self, self._root)
            self.traffic__vs__dynamic_0x9c = AnyGenesysObj.GenesysGenCollisionResponsesGlobalTrafficVsDynamic(self._io, self, self._root)
            self.crashing__race__car__vs__crashing__race__car_0xc0 = AnyGenesysObj.GenesysGenCollisionResponsesGlobalCrashingRaceCarVsCrashingRaceCar(self._io, self, self._root)
            self.traffic__vs__traffic_0xe0 = AnyGenesysObj.GenesysGenCollisionResponsesGlobalTrafficVsTraffic(self._io, self, self._root)
            self.dynamic__vs__dynamic_0x100 = AnyGenesysObj.GenesysGenCollisionResponsesGlobalDynamicVsDynamic(self._io, self, self._root)
            self.game_changer_id_0x11c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 292
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1217853836
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenUicamera(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.look_at_0x10 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.position_0x20 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.up_vector_0x30 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.game_changer_id_0x40 = self._io.read_u4le()
            self.aspect_ratio_0x44 = self._io.read_f4le()
            self.far_clip_0x48 = self._io.read_f4le()
            self.field_of_view_0x4c = self._io.read_f4le()
            self.near_clip_0x50 = self._io.read_f4le()
            self.aspect_correct_0x54 = self._io.read_u1()
            self.bool8_t_0x55 = self._io.read_u1()
            self.bool8_t_0x56 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 88
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4265727012
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRoadBlockLayer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.middle_item_0xc = AnyGenesysObj.GenesysGenRoadBlockLayerItem(self._io, self, self._root)
            self.game_changer_id_0x24 = self._io.read_u4le()
            self.distance_0x28 = self._io.read_f4le()
            self.first_distance_0x2c = self._io.read_f4le()
            self.ptr_arr_left_items_0x30 = self._io.read_u4le()
            self.ptr_arr_right_items_0x34 = self._io.read_u4le()
            self.array_count_for_0x30 = self._io.read_u2le()
            self.array_count_for_0x34 = self._io.read_u2le()

        @property
        def inst_left_items_0x30(self):
            if hasattr(self, '_m_inst_left_items_0x30'):
                return self._m_inst_left_items_0x30

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_left_items_0x30)
            self._m_inst_left_items_0x30 = []
            for i in range(self.array_count_for_0x30):
                self._m_inst_left_items_0x30.append(AnyGenesysObj.GenesysGenRoadBlockLayerItem(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_left_items_0x30', None)

        @property
        def inst_right_items_0x34(self):
            if hasattr(self, '_m_inst_right_items_0x34'):
                return self._m_inst_right_items_0x34

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_right_items_0x34)
            self._m_inst_right_items_0x34 = []
            for i in range(self.array_count_for_0x34):
                self._m_inst_right_items_0x34.append(AnyGenesysObj.GenesysGenRoadBlockLayerItem(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_right_items_0x34', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 64
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1694754426
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceBalancingData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.extra_crash_schedule_time_0x10 = self._io.read_f4le()
            self.extra_schedule_time_0x14 = self._io.read_f4le()
            self.ptr_arr_opponent_data_0x18 = self._io.read_u4le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_opponent_data_0x18(self):
            if hasattr(self, '_m_inst_opponent_data_0x18'):
                return self._m_inst_opponent_data_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_opponent_data_0x18)
            self._m_inst_opponent_data_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_opponent_data_0x18.append(AnyGenesysObj.GenesysGenRaceBalancingDataOpponentBalancingData(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_opponent_data_0x18', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3055337662
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreSoundParamsLongSpin(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.ya_am_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2081469541
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersNitrousPower(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.time_to_full_nitrous_0xc = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2483448381
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreSoundParamsLatSlip(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.ya_am_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 860059237
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.output__channels_0x10 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1356872704
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPostFxKeyframeGeneral(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.car_motion_blur_0x10 = self._io.read_f4le()
            self.world_colour_cube_weight_0x14 = self._io.read_f4le()
            self.world_motion_blur_0x18 = self._io.read_f4le()
            self.world_saturation_0x1c = self._io.read_f4le()
            self.unk_enum_0x20 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4085824509
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPerformanceModificationItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.value_0x10 = self._io.read_f4le()
            self.unk_enum_0x14 = self._io.read_u2le()
            self.modification_type_0x16 = self._io.read_u2le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1555583970
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionEffectsTrafficEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__collision_effects__traffic_effect__extra_roll_params_0xc = AnyGenesysObj.GenesysGenCollisionEffectsTrafficEffectExtraRollParams(self._io, self, self._root)
            self.genesys__gen__collision_effects__traffic_effect__extra_roll_params_0x24 = AnyGenesysObj.GenesysGenCollisionEffectsTrafficEffectExtraRollParams(self._io, self, self._root)
            self.genesys__gen__collision_effects__traffic_effect__extra_roll_params_0x3c = AnyGenesysObj.GenesysGenCollisionEffectsTrafficEffectExtraRollParams(self._io, self, self._root)
            self.cam__effect_0x54 = self._io.read_bytes(8)
            self.cam__effect__unstable_0x5c = self._io.read_bytes(8)
            self.cam__effect__scale_0x64 = self._io.read_f4le()
            self.stable__camera__threshold_0x68 = self._io.read_f4le()
            self.unstable__camera__threshold_0x6c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 116
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2066481913
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersPunchUsage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenNitrousParametersUsage(self._io, self, self._root)
            self.punch_burn_percent_0x1c = self._io.read_f4le()
            self.punch_delay_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3479966800
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHandlingBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_genesys__gen__aerodynamic_behaviour_0x10 = self._io.read_u4le()
            self.ptr_genesys__gen__aligning_torque_0x14 = self._io.read_u4le()
            self.ptr_genesys__gen__body_movement_behaviour_0x18 = self._io.read_u4le()
            self.ptr_genesys__gen__brake_behaviour_0x1c = self._io.read_u4le()
            self.ptr_genesys__gen__donut_ability_0x20 = self._io.read_u4le()
            self.ptr_drift_0x24 = self._io.read_u4le()
            self.ptr_engine_0x28 = self._io.read_u4le()
            self.ptr_genesys__gen__handbrake_ability_0x2c = self._io.read_u4le()
            self.ptr_genesys__gen__hard_driving_behaviour_0x30 = self._io.read_u4le()
            self.ptr_genesys__gen__steering_behaviour_0x34 = self._io.read_u4le()
            self.ptr_genesys__gen__steering_wheel_physics_0x38 = self._io.read_u4le()
            self.ptr_genesys__gen__suspension_0x3c = self._io.read_u4le()
            self.ptr_genesys__gen__tyres_0x40 = self._io.read_u4le()

        @property
        def inst_genesys__gen__brake_behaviour_0x1c(self):
            if hasattr(self, '_m_inst_genesys__gen__brake_behaviour_0x1c'):
                return self._m_inst_genesys__gen__brake_behaviour_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__brake_behaviour_0x1c)
            self._m_inst_genesys__gen__brake_behaviour_0x1c = AnyGenesysObj.GenesysGenBrakeBehaviour(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__brake_behaviour_0x1c', None)

        @property
        def inst_genesys__gen__handbrake_ability_0x2c(self):
            if hasattr(self, '_m_inst_genesys__gen__handbrake_ability_0x2c'):
                return self._m_inst_genesys__gen__handbrake_ability_0x2c

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__handbrake_ability_0x2c)
            self._m_inst_genesys__gen__handbrake_ability_0x2c = AnyGenesysObj.GenesysGenHandbrakeAbility(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__handbrake_ability_0x2c', None)

        @property
        def inst_genesys__gen__body_movement_behaviour_0x18(self):
            if hasattr(self, '_m_inst_genesys__gen__body_movement_behaviour_0x18'):
                return self._m_inst_genesys__gen__body_movement_behaviour_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__body_movement_behaviour_0x18)
            self._m_inst_genesys__gen__body_movement_behaviour_0x18 = AnyGenesysObj.GenesysGenBodyMovementBehaviour(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__body_movement_behaviour_0x18', None)

        @property
        def inst_drift_0x24(self):
            if hasattr(self, '_m_inst_drift_0x24'):
                return self._m_inst_drift_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_drift_0x24)
            self._m_inst_drift_0x24 = AnyGenesysObj.GenesysGenDriftBehaviour(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_drift_0x24', None)

        @property
        def inst_engine_0x28(self):
            if hasattr(self, '_m_inst_engine_0x28'):
                return self._m_inst_engine_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_engine_0x28)
            self._m_inst_engine_0x28 = AnyGenesysObj.GenesysGenEngine(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_engine_0x28', None)

        @property
        def inst_genesys__gen__donut_ability_0x20(self):
            if hasattr(self, '_m_inst_genesys__gen__donut_ability_0x20'):
                return self._m_inst_genesys__gen__donut_ability_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__donut_ability_0x20)
            self._m_inst_genesys__gen__donut_ability_0x20 = AnyGenesysObj.GenesysGenDonutAbility(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__donut_ability_0x20', None)

        @property
        def inst_genesys__gen__hard_driving_behaviour_0x30(self):
            if hasattr(self, '_m_inst_genesys__gen__hard_driving_behaviour_0x30'):
                return self._m_inst_genesys__gen__hard_driving_behaviour_0x30

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__hard_driving_behaviour_0x30)
            self._m_inst_genesys__gen__hard_driving_behaviour_0x30 = AnyGenesysObj.GenesysGenHardDrivingBehaviour(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__hard_driving_behaviour_0x30', None)

        @property
        def inst_genesys__gen__aerodynamic_behaviour_0x10(self):
            if hasattr(self, '_m_inst_genesys__gen__aerodynamic_behaviour_0x10'):
                return self._m_inst_genesys__gen__aerodynamic_behaviour_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__aerodynamic_behaviour_0x10)
            self._m_inst_genesys__gen__aerodynamic_behaviour_0x10 = AnyGenesysObj.GenesysGenAerodynamicBehaviour(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__aerodynamic_behaviour_0x10', None)

        @property
        def inst_genesys__gen__aligning_torque_0x14(self):
            if hasattr(self, '_m_inst_genesys__gen__aligning_torque_0x14'):
                return self._m_inst_genesys__gen__aligning_torque_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__aligning_torque_0x14)
            self._m_inst_genesys__gen__aligning_torque_0x14 = AnyGenesysObj.GenesysGenAligningTorque(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__aligning_torque_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 72
            return getattr(self, '_m_size', None)

        @property
        def inst_genesys__gen__steering_behaviour_0x34(self):
            if hasattr(self, '_m_inst_genesys__gen__steering_behaviour_0x34'):
                return self._m_inst_genesys__gen__steering_behaviour_0x34

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__steering_behaviour_0x34)
            self._m_inst_genesys__gen__steering_behaviour_0x34 = AnyGenesysObj.GenesysGenSteeringBehaviour(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__steering_behaviour_0x34', None)

        @property
        def inst_genesys__gen__tyres_0x40(self):
            if hasattr(self, '_m_inst_genesys__gen__tyres_0x40'):
                return self._m_inst_genesys__gen__tyres_0x40

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__tyres_0x40)
            self._m_inst_genesys__gen__tyres_0x40 = AnyGenesysObj.GenesysGenTyres(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__tyres_0x40', None)

        @property
        def inst_genesys__gen__suspension_0x3c(self):
            if hasattr(self, '_m_inst_genesys__gen__suspension_0x3c'):
                return self._m_inst_genesys__gen__suspension_0x3c

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__suspension_0x3c)
            self._m_inst_genesys__gen__suspension_0x3c = AnyGenesysObj.GenesysGenSuspension(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__suspension_0x3c', None)

        @property
        def inst_genesys__gen__steering_wheel_physics_0x38(self):
            if hasattr(self, '_m_inst_genesys__gen__steering_wheel_physics_0x38'):
                return self._m_inst_genesys__gen__steering_wheel_physics_0x38

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__steering_wheel_physics_0x38)
            self._m_inst_genesys__gen__steering_wheel_physics_0x38 = AnyGenesysObj.GenesysGenSteeringWheelPhysics(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__steering_wheel_physics_0x38', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3811132854
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenWcremoveWorldEntityBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1055028229
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreVfxBehaviourFrontRearParamsLatParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 210492029
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayTriggerOutputSequenceOutput(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.sequence_0xc = self._io.read_u4le()
            self.sequence_type_0x10 = self._io.read_u2le()
            self.bool8_t_0x12 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2222283730
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCarSelectData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cop_idle_sequences_0xc = AnyGenesysObj.GenesysGenCarSelectDataSequences(self._io, self, self._root)
            self.cop_sequences_0x28 = AnyGenesysObj.GenesysGenCarSelectDataSequences(self._io, self, self._root)
            self.racer_idle_sequences_0x44 = AnyGenesysObj.GenesysGenCarSelectDataSequences(self._io, self, self._root)
            self.racer_sequences_0x60 = AnyGenesysObj.GenesysGenCarSelectDataSequences(self._io, self, self._root)
            self.ptr_arr_cop_placements_0x7c = self._io.read_u4le()
            self.game_changer_id_0x80 = self._io.read_u4le()
            self.ptr_arr_racer_placements_0x84 = self._io.read_u4le()
            self.uimemory_limit_0x88 = self._io.read_f4le()
            self.uiresource_limit_0x8c = self._io.read_s4le()
            self.array_count_for_0x7c = self._io.read_u2le()
            self.array_count_for_0x84 = self._io.read_u2le()
            self.loop_sequences_0x94 = self._io.read_u1()
            self.split_by_tier_0x95 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_cop_placements_0x7c(self):
            if hasattr(self, '_m_inst_cop_placements_0x7c'):
                return self._m_inst_cop_placements_0x7c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cop_placements_0x7c)
            self._m_inst_cop_placements_0x7c = []
            for i in range(self.array_count_for_0x7c):
                self._m_inst_cop_placements_0x7c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cop_placements_0x7c', None)

        @property
        def inst_racer_placements_0x84(self):
            if hasattr(self, '_m_inst_racer_placements_0x84'):
                return self._m_inst_racer_placements_0x84

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_racer_placements_0x84)
            self._m_inst_racer_placements_0x84 = []
            for i in range(self.array_count_for_0x84):
                self._m_inst_racer_placements_0x84.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_racer_placements_0x84', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 152
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4000545794
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleSound(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__unique_id_0xc = self._io.read_u4le()
            self.cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.horn_0x18 = self._io.read_u4le()
            self.cgs_core__unique_id_0x1c = self._io.read_u4le()
            self.ptr_arr_cgs_core__unique_id_0x20 = self._io.read_u4le()
            self.array_count_for_0x20 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_cgs_core__unique_id_0x20(self):
            if hasattr(self, '_m_inst_cgs_core__unique_id_0x20'):
                return self._m_inst_cgs_core__unique_id_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_core__unique_id_0x20)
            self._m_inst_cgs_core__unique_id_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_cgs_core__unique_id_0x20.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_core__unique_id_0x20', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 535359424
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTimelineControllersRaceCarEntityTimelineController(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceTimelineController(self._io, self, self._root)
            self.unk_enum_0x1c = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 267183785
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersCatchingAir(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.nitrous_reward_0x14 = self._io.read_f4le()
            self.time_in_air_0x18 = self._io.read_f4le()
            self.is_enabled_0x1c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2075263523
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenAligningTorque(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3406519319
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesGlobalCrashingRaceCarVsTraffic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.crashing__race__car__angular__solve_0x10 = self._io.read_f4le()
            self.crashing__race__car__linear__solve_0x14 = self._io.read_f4le()
            self.friction_0x18 = self._io.read_f4le()
            self.restitution_0x1c = self._io.read_f4le()
            self.traffic__angular__solve_0x20 = self._io.read_f4le()
            self.traffic__linear__solve_0x24 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2626118372
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEnableCompoundBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3591755513
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarAivsTrafficDamageParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.damage_0x14 = self._io.read_f4le()
            self.linear__solve_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3134806732
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSoundDistanceFalloff(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.curve_type_0x10 = self._io.read_f4le()
            self.curve_type_reverb_0x14 = self._io.read_f4le()
            self.divergence_at_max_distance_0x18 = self._io.read_f4le()
            self.divergence_at_min_distance_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.initial_gain_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.arrays_motioned_0x30 = self._io.read_f4le()
            self.max_distance_0x34 = self._io.read_f4le()
            self.max_distance_divergence_0x38 = self._io.read_f4le()
            self.max_distance_reverb_0x3c = self._io.read_f4le()
            self.min_distance_0x40 = self._io.read_f4le()
            self.min_distance_divergence_0x44 = self._io.read_f4le()
            self.min_distance_reverb_0x48 = self._io.read_f4le()
            self.occlusion_multiplier_0x4c = self._io.read_f4le()
            self.peak_gain_0x50 = self._io.read_f4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.float32_t_0x58 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 591869524
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionHitTrigger(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 80
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3231281576
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenScoringActionOnlineScoringFeedback(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.description_0xc = self._io.read_u4le()
            self.sequence_0x10 = self._io.read_u4le()
            self.cgs_core__unique_id_0x14 = self._io.read_u4le()
            self.title_0x18 = self._io.read_u4le()
            self.deferrable_0x1c = self._io.read_u1()
            self.opposing__team_0x1d = self._io.read_u1()
            self.scoring__player_0x1e = self._io.read_u1()
            self.scoring__team_0x1f = self._io.read_u1()
            self.bool8_t_0x20 = self._io.read_u1()
            self.victim__player_0x21 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1781716212
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGeneralTriggerSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.trigger_0x28 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3179911126
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleGameplayTyreTrails(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.unk_enum_0xc = self._io.read_u2le()
            self.stock_0xe = self._io.read_u2le()
            self.track_0x10 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4100294056
            return getattr(self, '_m_mu_version_hash', None)


    class Int8T(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenOnlineDrivingTestListGroups(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_ptr_driving_test_list_groups_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_driving_test_list_groups_0x10(self):
            if hasattr(self, '_m_inst_driving_test_list_groups_0x10'):
                return self._m_inst_driving_test_list_groups_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_driving_test_list_groups_0x10)
            self._m_inst_driving_test_list_groups_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_driving_test_list_groups_0x10.append(AnyGenesysObj.Ptr(u"genesys__gen__online__driving_test_list_group", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_driving_test_list_groups_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4242000614
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDonutAbilityDonutGripValues(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4164557270
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenAerodynamicBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()
            self.float32_t_0x48 = self._io.read_f4le()
            self.float32_t_0x4c = self._io.read_f4le()
            self.float32_t_0x50 = self._io.read_f4le()
            self.float32_t_0x54 = self._io.read_f4le()
            self.float32_t_0x58 = self._io.read_f4le()
            self.float32_t_0x5c = self._io.read_f4le()
            self.float32_t_0x60 = self._io.read_f4le()
            self.float32_t_0x64 = self._io.read_f4le()
            self.bool8_t_0x68 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 108
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3037639290
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSuspensionWheel(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__string_base_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.cgs_core__string_base_0x14 = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.damage_0x1c = self._io.read_bytes(8)
            self.cgs_resource__handle_0x24 = self._io.read_bytes(8)
            self.cgs_resource__handle_0x2c = self._io.read_bytes(8)
            self.game_changer_id_0x34 = self._io.read_u4le()
            self.float32_t_0x38 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 64
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1279163701
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPoint2d(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.inline_arr_float32_t_0xc = []
            for i in range(2):
                self.inline_arr_float32_t_0xc.append(self._io.read_f4le())

            self.array_count_for_0xc = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3430005461
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionJumpStats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 80
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3366752106
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSuspension(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1387924581
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEvent(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_arr_autotest_checkpoints_0xc = self._io.read_u4le()
            self.cinematic_name_0x10 = self._io.read_u4le()
            self.description_0x14 = self._io.read_u4le()
            self.game_changer_id_0x18 = self._io.read_u4le()
            self.game_mode_0x1c = self._io.read_u4le()
            self.game_pack_0x20 = self._io.read_u4le()
            self.cgs_core__unique_id_0x24 = self._io.read_u4le()
            self.cycle_time_of_day_0x28 = self._io.read_f4le()
            self.finish_time_of_day_0x2c = self._io.read_f4le()
            self.sun_direction_0x30 = self._io.read_f4le()
            self.time_of_day_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.ptr_arr_ptr_chevron_list_0x3c = self._io.read_u4le()
            self.road_surface_conditions_0x40 = self._io.read_u2le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.is_alternative_weather_0x44 = self._io.read_u1()
            self.is_rain_active_0x45 = self._io.read_u1()
            self.is_thunder_active_0x46 = self._io.read_u1()
            self.override_sun_direction_0x47 = self._io.read_u1()
            self.bool8_t_0x48 = self._io.read_u1()
            self.array_count_for_0x3c = self._io.read_u1()
            self.uint8_t_0x4a = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def inst_autotest_checkpoints_0xc(self):
            if hasattr(self, '_m_inst_autotest_checkpoints_0xc'):
                return self._m_inst_autotest_checkpoints_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_autotest_checkpoints_0xc)
            self._m_inst_autotest_checkpoints_0xc = []
            for i in range(self.array_count_for_0xc):
                self._m_inst_autotest_checkpoints_0xc.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_autotest_checkpoints_0xc', None)

        @property
        def inst_chevron_list_0x3c(self):
            if hasattr(self, '_m_inst_chevron_list_0x3c'):
                return self._m_inst_chevron_list_0x3c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_chevron_list_0x3c)
            self._m_inst_chevron_list_0x3c = []
            for i in range(self.array_count_for_0x3c):
                self._m_inst_chevron_list_0x3c.append(AnyGenesysObj.Ptr(u"genesys__gen__custom_chevron", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_chevron_list_0x3c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3089457678
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineTransmission(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.float32_t_0xc = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3829466250
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclePaintMaterialProperties(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x10 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x20 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x30 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x40 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x50 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x60 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.game_changer_id_0x70 = self._io.read_u4le()
            self.float32_t_0x74 = self._io.read_f4le()
            self.float32_t_0x78 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 128
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2896523173
            return getattr(self, '_m_mu_version_hash', None)


    class CgsCoreUniqueId(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenAiplayerType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__unique_id_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.rollout_0x14 = self._io.read_u4le()
            self.ptr_arr_target_placement_0x18 = self._io.read_u4le()
            self.aggression_delay_0x1c = self._io.read_f4le()
            self.aggression_frequency_0x20 = self._io.read_f4le()
            self.blinded_time_scale_0x24 = self._io.read_f4le()
            self.escaping_speed_0x28 = self._io.read_f4le()
            self.fail_jump_daze_time_0x2c = self._io.read_f4le()
            self.flat_out_initial_time_0x30 = self._io.read_f4le()
            self.flat_out_time_0x34 = self._io.read_f4le()
            self.hit_damage_percentage_to_daze_0x38 = self._io.read_f4le()
            self.hit_daze_time_0x3c = self._io.read_f4le()
            self.max_damage_for_speed_effect_0x40 = self._io.read_f4le()
            self.max_event_balancing_distance_0x44 = self._io.read_f4le()
            self.max_speed_for_distance_0x48 = self._io.read_f4le()
            self.min_damage_for_speed_effect_0x4c = self._io.read_f4le()
            self.min_event_balancing_distance_0x50 = self._io.read_f4le()
            self.min_shortcut_time_0x54 = self._io.read_f4le()
            self.min_speed_for_distance_0x58 = self._io.read_f4le()
            self.min_throttle_damage_percent_0x5c = self._io.read_f4le()
            self.min_time_between_weapon_uses_0x60 = self._io.read_f4le()
            self.respawn_time_0x64 = self._io.read_f4le()
            self.shortcut_taking_percentage_0x68 = self._io.read_f4le()
            self.spawn_speed_0x6c = self._io.read_f4le()
            self.speed_0x70 = self._io.read_f4le()
            self.speed_matching_max_distance_0x74 = self._io.read_f4le()
            self.speed_matching_max_speed_0x78 = self._io.read_f4le()
            self.float32_t_0x7c = self._io.read_f4le()
            self.speed_matching_min_speed_0x80 = self._io.read_f4le()
            self.speed_matching_speed_difference_0x84 = self._io.read_f4le()
            self.toughness_0x88 = self._io.read_f4le()
            self.turn_at_junction_percentage_0x8c = self._io.read_f4le()
            self.uturn_min_time_0x90 = self._io.read_f4le()
            self.weapon_avoidance_percentage_0x94 = self._io.read_f4le()
            self.weapon_use_delay_at_event_start_0x98 = self._io.read_f4le()
            self.weaving_duration_0x9c = self._io.read_f4le()
            self.weaving_frequency_0xa0 = self._io.read_f4le()
            self.aggression_type_0xa4 = self._io.read_u2le()
            self.behaviour_0xa6 = self._io.read_u2le()
            self.unk_enum_0xa8 = self._io.read_u2le()
            self.nitrous_usage_0xaa = self._io.read_u2le()
            self.weaving_type_0xac = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.allowed_to_respawn_0xb0 = self._io.read_u1()
            self.can_rhino_0xb1 = self._io.read_u1()
            self.do_uturns_0xb2 = self._io.read_u1()
            self.is_aggressor_0xb3 = self._io.read_u1()
            self.is_blacklist_0xb4 = self._io.read_u1()
            self.is_cop_0xb5 = self._io.read_u1()
            self.bool8_t_0xb6 = self._io.read_u1()
            self.uint8_t_0xb7 = self._io.read_u1()
            self.weapon_use_chance_0xb8 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_target_placement_0x18(self):
            if hasattr(self, '_m_inst_target_placement_0x18'):
                return self._m_inst_target_placement_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_target_placement_0x18)
            self._m_inst_target_placement_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_target_placement_0x18.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_target_placement_0x18', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 188
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3533118493
            return getattr(self, '_m_mu_version_hash', None)


    class Ptr(KaitaiStruct):
        def __init__(self, dtype, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.dtype = dtype
            self._read()

        def _read(self):
            self.offset = self._io.read_s4le()

        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            if self.offset != 0:
                _pos = self._io.pos()
                self._io.seek(self.offset)
                self._m_data = AnyGenesysObj.Atype(self.dtype, self._io, self, self._root)
                self._io.seek(_pos)

            return getattr(self, '_m_data', None)


    class GenesysGenMixerChannelSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.mixer__channel_0x2c = self._io.read_bytes(8)
            self.ptr_arr_double__params_0x34 = self._io.read_u4le()
            self.array_count_for_0x34 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_double__params_0x34(self):
            if hasattr(self, '_m_inst_double__params_0x34'):
                return self._m_inst_double__params_0x34

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_double__params_0x34)
            self._m_inst_double__params_0x34 = []
            for i in range(self.array_count_for_0x34):
                self._m_inst_double__params_0x34.append(AnyGenesysObj.GenesysGenMixerChannelSequenceItemMixerChannelDoubleValue(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_double__params_0x34', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 60
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2706222886
            return getattr(self, '_m_mu_version_hash', None)


    class Int32T(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyCylinderVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.game_changer_id_0x50 = self._io.read_u4le()
            self.half_length_0x54 = self._io.read_f4le()
            self.radius_0x58 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 18021398
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarPlayerVsAi(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ai__stable_0xc = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiDamageParams(self._io, self, self._root)
            self.ai__unstable_0x28 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiDamageParams(self._io, self, self._root)
            self.player__stable_0x44 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiDamageParams(self._io, self, self._root)
            self.player__unstable_0x60 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiDamageParams(self._io, self, self._root)
            self.ai__crashed_0x7c = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiBasicParams(self._io, self, self._root)
            self.player__crashed_0x94 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiBasicParams(self._io, self, self._root)
            self.player__invulnerable_0xac = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiBasicParams(self._io, self, self._root)
            self.player__when__ai__crashed_0xc4 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiBasicParams(self._io, self, self._root)
            self.game_changer_id_0xdc = self._io.read_u4le()
            self.friction_0xe0 = self._io.read_f4le()
            self.restitution_0xe4 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 236
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2391445668
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleVfxBehaviourCorona(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.colour_0x10 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.cgs_resource__handle_0x20 = self._io.read_bytes(8)
            self.corona_definition_0x28 = self._io.read_bytes(8)
            self.locator_group_0x30 = self._io.read_u4le()
            self.brightness_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.unk_enum_0x40 = self._io.read_u2le()
            self.time_of_day_0x42 = self._io.read_u2le()
            self.bool8_t_0x44 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 72
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3445640778
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineSound2GainParam(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_resource__handle_0xc = self._io.read_bytes(8)
            self.gain_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4223711972
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayCondition(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_arr_strings_0xc = self._io.read_u4le()
            self.game_changer_id_0x10 = self._io.read_u4le()
            self.ptr_arr_references_0x14 = self._io.read_u4le()
            self.ptr_arr_values_0x18 = self._io.read_u4le()
            self.test_0x1c = self._io.read_u2le()
            self.type_0x1e = self._io.read_u2le()
            self.array_count_for_0x14 = self._io.read_u2le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_strings_0xc(self):
            if hasattr(self, '_m_inst_strings_0xc'):
                return self._m_inst_strings_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_strings_0xc)
            self._m_inst_strings_0xc = []
            for i in range(self.array_count_for_0xc):
                self._m_inst_strings_0xc.append(AnyGenesysObj.StringBase(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_strings_0xc', None)

        @property
        def inst_references_0x14(self):
            if hasattr(self, '_m_inst_references_0x14'):
                return self._m_inst_references_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_references_0x14)
            self._m_inst_references_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_references_0x14.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_references_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def inst_values_0x18(self):
            if hasattr(self, '_m_inst_values_0x18'):
                return self._m_inst_values_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_values_0x18)
            self._m_inst_values_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_values_0x18.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_values_0x18', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1901216409
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehicleDriverSetupSeatBeltBoneOffset(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.position_0x10 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rotation_0x20 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3542932618
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionSpeedRun(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.route_count_0x50 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 84
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3616318101
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclePaintStructure2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1082129393
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSndPlayerDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2473868341
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSubHarmoniserDspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 489513931
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenControlMesh(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.rw_math_vpu__vector2_0x10 = AnyGenesysObj.RwMathVpuVector2(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x20 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x30 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x40 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0x50 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.game_changer_id_0x60 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 104
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1980202577
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenOfflineEventCheckpointInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.sequence_0xc = self._io.read_u4le()
            self.type_0x10 = self._io.read_u2le()
            self.bool8_t_0x12 = self._io.read_u1()
            self.show_split_time_0x13 = self._io.read_u1()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2582603530
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesWorldPlayerFlipState(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.flip_graph_power_0x10 = self._io.read_f4le()
            self.flip_min_threshold_0x14 = self._io.read_f4le()
            self.flip_scale_0x18 = self._io.read_f4le()
            self.player_speed_mph_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1278315440
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPan2ddspPlugIn(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3858691605
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenStoreItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.name_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.psnpackage_name_0x14 = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.nucleus_ent_tag_0x1c = self._io.read_bytes(8)
            self.game_changer_id_0x24 = self._io.read_u4le()
            self.ptr_arr_long__description_0x28 = self._io.read_u4le()
            self.main_image_0x2c = self._io.read_u4le()
            self.sub_image1_0x30 = self._io.read_u4le()
            self.sub_image2_0x34 = self._io.read_u4le()
            self.title_0x38 = self._io.read_u4le()
            self.ptr_arr_entitlements_0x3c = self._io.read_u4le()
            self.x360license_mask_0x40 = self._io.read_u4le()
            self.x360offer_id_0x44 = self._io.read_u4le()
            self.array_count_for_0x28 = self._io.read_u2le()
            self.show__in__store_0x4a = self._io.read_u1()
            self.array_count_for_0x3c = self._io.read_u1()

        @property
        def inst_long__description_0x28(self):
            if hasattr(self, '_m_inst_long__description_0x28'):
                return self._m_inst_long__description_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_long__description_0x28)
            self._m_inst_long__description_0x28 = []
            for i in range(self.array_count_for_0x28):
                self._m_inst_long__description_0x28.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_long__description_0x28', None)

        @property
        def inst_entitlements_0x3c(self):
            if hasattr(self, '_m_inst_entitlements_0x3c'):
                return self._m_inst_entitlements_0x3c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_entitlements_0x3c)
            self._m_inst_entitlements_0x3c = []
            for i in range(self.array_count_for_0x3c):
                self._m_inst_entitlements_0x3c.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_entitlements_0x3c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 80
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 325575367
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesWorldTraffic(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.friction_0x10 = self._io.read_f4le()
            self.restitution_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 174645272
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenBrakeBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2252962025
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenJumpTimelineController(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceTimelineController(self._io, self, self._root)
            self.destination_time_0x1c = self._io.read_f4le()
            self.trigger_time_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 115778840
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionInfoTrafficEffect(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cam__effect_0xc = self._io.read_bytes(8)
            self.cam__effect__scale_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2276451180
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenImpactDamageGraphs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.general_damage_graph_0xc = AnyGenesysObj.GenesysGenImpactDamageGraphsGraph(self._io, self, self._root)
            self.race_car_vs_race_car_damage_graph_0x30 = AnyGenesysObj.GenesysGenImpactDamageGraphsGraph(self._io, self, self._root)
            self.game_changer_id_0x54 = self._io.read_u4le()
            self.velocity_for_full_damage_mph_0x58 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 196190359
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEasyGuidePage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.ptr_arr_cgs_core__unique_id_0x14 = self._io.read_u4le()
            self.sequence_0x18 = self._io.read_u4le()
            self.ptr_arr_text_0x1c = self._io.read_u4le()
            self.ptr_arr_cgs_resource__handle_0x20 = self._io.read_u4le()
            self.unk_enum_0x24 = self._io.read_u2le()
            self.array_count_for_0x1c = self._io.read_u2le()
            self.array_count_for_0x20 = self._io.read_u1()
            self.array_count_for_0x14 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_text_0x1c(self):
            if hasattr(self, '_m_inst_text_0x1c'):
                return self._m_inst_text_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_text_0x1c)
            self._m_inst_text_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_text_0x1c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_text_0x1c', None)

        @property
        def inst_cgs_resource__handle_0x20(self):
            if hasattr(self, '_m_inst_cgs_resource__handle_0x20'):
                return self._m_inst_cgs_resource__handle_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_resource__handle_0x20)
            self._m_inst_cgs_resource__handle_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_cgs_resource__handle_0x20.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_resource__handle_0x20', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def inst_cgs_core__unique_id_0x14(self):
            if hasattr(self, '_m_inst_cgs_core__unique_id_0x14'):
                return self._m_inst_cgs_core__unique_id_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_cgs_core__unique_id_0x14)
            self._m_inst_cgs_core__unique_id_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_cgs_core__unique_id_0x14.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_cgs_core__unique_id_0x14', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1365071824
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCarSwapSpot(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__unique_id_0xc = self._io.read_u4le()
            self.colour_id_0x10 = self._io.read_u4le()
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.cgs_core__unique_id_0x18 = self._io.read_u4le()
            self.parking_placement_0x1c = self._io.read_u4le()
            self.placement_0x20 = self._io.read_u4le()
            self.vehicle_id_0x24 = self._io.read_u4le()
            self.vehicle_placement_0x28 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1611423524
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRoadBlockLayerItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.cgs_core__unique_id_0x10 = self._io.read_u4le()
            self.angle_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2808391399
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclesNitrousUpgrade(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 980106560
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenMixerChannelPriority(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.priority_0xc = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 16
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2235129779
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionJumpOverPlayers(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.bool8_t_0x4c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 80
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1058158881
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreLongGripCurve(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.fgow_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 84747879
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.convex_hull_0x50 = self._io.read_bytes(8)
            self.game_changer_id_0x58 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1664340785
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPhysicalDefinitionRigidBodyBoxVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.halfsize_0x50 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.game_changer_id_0x60 = self._io.read_u4le()
            self.i6je_0x64 = self._io.read_s4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 108
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 678938689
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreVfxBehaviourLongLatParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1442317719
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHeatLevelSoundSetNitrous(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.compressor__override_0xc = self._io.read_u4le()
            self.cop__on_0x10 = self._io.read_u4le()
            self.ptr_arr_mix__snapshot__set_0x14 = self._io.read_u4le()
            self.racer__off_0x18 = self._io.read_u4le()
            self.racer__on_0x1c = self._io.read_u4le()
            self.array_count_for_0x14 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_mix__snapshot__set_0x14(self):
            if hasattr(self, '_m_inst_mix__snapshot__set_0x14'):
                return self._m_inst_mix__snapshot__set_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_mix__snapshot__set_0x14)
            self._m_inst_mix__snapshot__set_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_mix__snapshot__set_0x14.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_mix__snapshot__set_0x14', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3178679735
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVfxLocatorGroupVehicleSpotEffectSequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x30 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.rw_math_vpu__vector3_0x40 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.intensity_0x50 = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self.cgs_core__string_base_0x88 = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.cgs_resource__handle_0x90 = self._io.read_bytes(8)
            self.locator_group_0x98 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 160
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 574246386
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysObject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenWheelDamage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 52
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2504213501
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionInfoWorldDamage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_aggressive_0xc = self._io.read_u4le()
            self.ptr_self__inflicted_0x10 = self._io.read_u4le()

        @property
        def inst_aggressive_0xc(self):
            if hasattr(self, '_m_inst_aggressive_0xc'):
                return self._m_inst_aggressive_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_aggressive_0xc)
            self._m_inst_aggressive_0xc = AnyGenesysObj.GenesysGenCollisionInfoDamageProfile(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_aggressive_0xc', None)

        @property
        def inst_self__inflicted_0x10(self):
            if hasattr(self, '_m_inst_self__inflicted_0x10'):
                return self._m_inst_self__inflicted_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_self__inflicted_0x10)
            self._m_inst_self__inflicted_0x10 = AnyGenesysObj.GenesysGenCollisionInfoDamageProfile(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_self__inflicted_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 756034263
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_core__unique_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.cop_behaviour_0x14 = self._io.read_u2le()
            self.positioning_0x16 = self._io.read_s1()
            self.padding = self._io.read_bytes(1)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 35335782
            return getattr(self, '_m_mu_version_hash', None)


    class Uint16T(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class GenesysGenCollisionResponsesRaceCarRaceCarVsDynamicBasicParams(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.angular__solve_0x10 = self._io.read_f4le()
            self.linear__solve_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3881994110
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEventArenaDataSpawnPointCollection(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_spawn_points_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_spawn_points_0x10(self):
            if hasattr(self, '_m_inst_spawn_points_0x10'):
                return self._m_inst_spawn_points_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_spawn_points_0x10)
            self._m_inst_spawn_points_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_spawn_points_0x10.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_spawn_points_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4090590688
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTyreLateralGripCurve(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2479955317
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameUnlockList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.ptr_arr_ptr_item_0x10 = self._io.read_u4le()
            self.array_count_for_0x10 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_item_0x10(self):
            if hasattr(self, '_m_inst_item_0x10'):
                return self._m_inst_item_0x10

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_item_0x10)
            self._m_inst_item_0x10 = []
            for i in range(self.array_count_for_0x10):
                self._m_inst_item_0x10.append(AnyGenesysObj.Ptr(u"any_genesys_obj", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_item_0x10', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 24
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 738476701
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCoronaGlow(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.unk_enum_0x10 = self._io.read_u1()
            self.colour_0xa0 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.rw_math_vpu__vector4_0xb0 = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            self.material_0xc0 = self._io.read_bytes(8)
            self.depth_bias_0xc8 = self._io.read_f4le()
            self.rotation_offset_0xcc = self._io.read_f4le()
            self.render_buffer_0xd0 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 216
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3040986089
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayTrigger(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.predicate_0xc = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.time_to_wait_0x18 = self._io.read_f4le()
            self.ptr_arr_input_0x1c = self._io.read_u4le()
            self.ptr_arr_output_0x20 = self._io.read_u4le()
            self.trigger_lifetime_0x24 = self._io.read_u2le()
            self.array_count_for_0x1c = self._io.read_u2le()
            self.array_count_for_0x20 = self._io.read_u2le()
            self.add_to_mini_map_0x2a = self._io.read_u1()
            self.bool8_t_0x2b = self._io.read_u1()
            self.bool8_t_0x2c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_input_0x1c(self):
            if hasattr(self, '_m_inst_input_0x1c'):
                return self._m_inst_input_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_input_0x1c)
            self._m_inst_input_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_input_0x1c.append(AnyGenesysObj.GenesysGenGameplayTriggerInput(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_input_0x1c', None)

        @property
        def inst_output_0x20(self):
            if hasattr(self, '_m_inst_output_0x20'):
                return self._m_inst_output_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_output_0x20)
            self._m_inst_output_0x20 = []
            for i in range(self.array_count_for_0x20):
                self._m_inst_output_0x20.append(AnyGenesysObj.GenesysGenGameplayTriggerOutput(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_output_0x20', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 48
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 23772465
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyBoxVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.volume_to_body_transform_0x10 = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            self.halfsize_0x50 = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            self.game_changer_id_0x60 = self._io.read_u4le()
            self.i6je_0x64 = self._io.read_s4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 108
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 678938689
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesWorldCrashedPlayerConstraintData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.friction_0x10 = self._io.read_f4le()
            self.restitution_0x14 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1592993583
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCar(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.first__frame_0xc = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarProfile(self._io, self, self._root)
            self.low__speed_0x34 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarProfile(self._io, self, self._root)
            self.subsequent__frames_0x5c = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarProfile(self._io, self, self._root)
            self.player__invulnerable_0x84 = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarBasicParams(self._io, self, self._root)
            self.game_changer_id_0x9c = self._io.read_u4le()
            self.full__high__speed__mph_0xa0 = self._io.read_f4le()
            self.full__low__speed__mph_0xa4 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 172
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3256016364
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeOnlineChallenge(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenOnlineEvent(self._io, self, self._root)
            self.intro_0x70 = self._io.read_u4le()
            self.deallocated_nodule_0x74 = self._io.read_u4le()
            self.ptr_arr_ptr_parts_0x78 = self._io.read_u4le()
            self.elimination_type_0x7c = self._io.read_u2le()
            self.type_0x7e = self._io.read_u2le()
            self.array_count_for_0x78 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def inst_parts_0x78(self):
            if hasattr(self, '_m_inst_parts_0x78'):
                return self._m_inst_parts_0x78

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_parts_0x78)
            self._m_inst_parts_0x78 = []
            for i in range(self.array_count_for_0x78):
                self._m_inst_parts_0x78.append(AnyGenesysObj.Ptr(u"genesys__gen__challenge__challenge_part", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_parts_0x78', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 132
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2121274978
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenSafehouse(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.discovery_trigger_0xc = self._io.read_u4le()
            self.entry_sequence_0x10 = self._io.read_u4le()
            self.exit_sequence_0x14 = self._io.read_u4le()
            self.exit_spawn_location_0x18 = self._io.read_u4le()
            self.game_changer_id_0x1c = self._io.read_u4le()
            self.name_0x20 = self._io.read_u4le()
            self.placement_0x24 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 44
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3469692361
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenLightSpot(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenLightCone(self._io, self, self._root)
            self.float32_t_0x70 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 120
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2189872818
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenMixerChannelSequenceItemMixerChannelDoubleValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.plug_in_0xc = self._io.read_u4le()
            self.plug_in__type_0x10 = self._io.read_u4le()
            self.ptr_arr_sound_distance_falloff_0x14 = self._io.read_u4le()
            self.ptr_value_0x18 = self._io.read_u4le()
            self.parameter__name_0x1c = self._io.read_u4le()
            self.automated__property_0x20 = self._io.read_u2le()
            self.array_count_for_0x14 = self._io.read_u1()
            self.padding = self._io.read_bytes(1)

        @property
        def inst_sound_distance_falloff_0x14(self):
            if hasattr(self, '_m_inst_sound_distance_falloff_0x14'):
                return self._m_inst_sound_distance_falloff_0x14

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_sound_distance_falloff_0x14)
            self._m_inst_sound_distance_falloff_0x14 = []
            for i in range(self.array_count_for_0x14):
                self._m_inst_sound_distance_falloff_0x14.append(AnyGenesysObj.CgsResourceHandle(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_sound_distance_falloff_0x14', None)

        @property
        def inst_value_0x18(self):
            if hasattr(self, '_m_inst_value_0x18'):
                return self._m_inst_value_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_value_0x18)
            self._m_inst_value_0x18 = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_value_0x18', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1967128889
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenPostFxsequenceItem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            self.genesys__gen__sequence_item__modulating_double_value_0x5c = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self.genesys__gen__sequence_item__modulating_double_value_0x94 = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self.genesys__gen__sequence_item__modulating_double_value_0xcc = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            self.cgs_core__string_base_0x104 = AnyGenesysObj.StringBase(self._io, self, self._root)
            self.post_fxstate_0x10c = self._io.read_bytes(8)
            self.unk_enum_0x114 = self._io.read_u2le()
            self.override_intensity_0x116 = self._io.read_u1()
            self.endless__environment_0x117 = self._io.read_u1()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 284
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4032173314
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousStrength(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.jump_0xc = AnyGenesysObj.GenesysGenNitrousStrengthJump(self._io, self, self._root)
            self.punch_0x24 = AnyGenesysObj.GenesysGenNitrousStrengthPunch(self._io, self, self._root)
            self.game_changer_id_0x38 = self._io.read_u4le()
            self.float32_t_0x3c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 68
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1201833830
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraGameplayGradientAdjustments(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_gradient_adjustments__params_0xc = AnyGenesysObj.GenesysGenCameraGameplayGradientAdjustmentsParams(self._io, self, self._root)
            self.genesys__gen__camera_gameplay_gradient_adjustments__params_0x24 = AnyGenesysObj.GenesysGenCameraGameplayGradientAdjustmentsParams(self._io, self, self._root)
            self.game_changer_id_0x3c = self._io.read_u4le()
            self.float32_t_0x40 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 72
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 980871986
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenCameraRearView(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.inline_arr_float32_t_0xc = []
            for i in range(3):
                self.inline_arr_float32_t_0xc.append(self._io.read_f4le())

            self.game_changer_id_0x18 = self._io.read_u4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.ptr_genesys__gen__camera_rear_view_globals_0x20 = self._io.read_u4le()
            self.array_count_for_0xc = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_genesys__gen__camera_rear_view_globals_0x20(self):
            if hasattr(self, '_m_inst_genesys__gen__camera_rear_view_globals_0x20'):
                return self._m_inst_genesys__gen__camera_rear_view_globals_0x20

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__camera_rear_view_globals_0x20)
            self._m_inst_genesys__gen__camera_rear_view_globals_0x20 = AnyGenesysObj.GenesysGenCameraRearViewGlobals(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__camera_rear_view_globals_0x20', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 998115052
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDriftBehaviourDriftScale(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 56
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2655111671
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersCrashEscape(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.minimum_speed_0x14 = self._io.read_f4le()
            self.nitrous_reward_0x18 = self._io.read_f4le()
            self.is_enabled_0x1c = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1463097890
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenDamageBarProfilesProfile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.segment_recharge_time_0x10 = self._io.read_f4le()
            self.segment_recharge_wait_0x14 = self._io.read_f4le()
            self.ptr_arr_segment_limits_0x18 = self._io.read_u4le()
            self.ptr_arr_world_segment_limits_0x1c = self._io.read_u4le()
            self.array_count_for_0x18 = self._io.read_u2le()
            self.array_count_for_0x1c = self._io.read_u2le()

        @property
        def inst_segment_limits_0x18(self):
            if hasattr(self, '_m_inst_segment_limits_0x18'):
                return self._m_inst_segment_limits_0x18

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_segment_limits_0x18)
            self._m_inst_segment_limits_0x18 = []
            for i in range(self.array_count_for_0x18):
                self._m_inst_segment_limits_0x18.append(AnyGenesysObj.GenesysGenDamageBarProfilesProfileSegmentData(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_segment_limits_0x18', None)

        @property
        def inst_world_segment_limits_0x1c(self):
            if hasattr(self, '_m_inst_world_segment_limits_0x1c'):
                return self._m_inst_world_segment_limits_0x1c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_world_segment_limits_0x1c)
            self._m_inst_world_segment_limits_0x1c = []
            for i in range(self.array_count_for_0x1c):
                self._m_inst_world_segment_limits_0x1c.append(AnyGenesysObj.GenesysGenDamageBarProfilesProfileSegmentData(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_world_segment_limits_0x1c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 40
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2099267897
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenTrafficFlowTypeTrafficFlowType(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.traffic_vehicle_type_0xc = self._io.read_bytes(8)
            self.colour_0x14 = self._io.read_u4le()
            self.game_changer_id_0x18 = self._io.read_u4le()
            self.proportion_0x1c = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2353212897
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenNitrousParametersHittingAnotherCompetitor(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.message_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.minimum_speed_0x14 = self._io.read_f4le()
            self.minimum_time_0x18 = self._io.read_f4le()
            self.nitrous_reward_0x1c = self._io.read_f4le()
            self.is_enabled_0x20 = self._io.read_u1()
            self.padding = self._io.read_bytes(3)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 36
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2656703430
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameRank(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.rank__image_0x10 = self._io.read_u4le()
            self.rank__name_0x14 = self._io.read_u4le()
            self.rank__number_0x18 = self._io.read_s4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 32
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 3159067131
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenVehiclesPerformanceUpgrades(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.pro_0xc = AnyGenesysObj.GenesysGenVehiclesPerformanceUpgradesCategory(self._io, self, self._root)
            self.standard_0x60 = AnyGenesysObj.GenesysGenVehiclesPerformanceUpgradesCategory(self._io, self, self._root)
            self.game_changer_id_0xb4 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0xb8 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0xbc = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0xc0 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0xc4 = self._io.read_u4le()
            self.ptr_genesys__gen__vehicles__upgrade_base_0xc8 = self._io.read_u4le()

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0xb8(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xb8'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0xb8

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0xb8)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0xb8 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xb8', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0xbc(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xbc'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0xbc

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0xbc)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0xbc = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xbc', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0xc8(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xc8'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0xc8

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0xc8)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0xc8 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xc8', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0xc4(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xc4'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0xc4

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0xc4)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0xc4 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xc4', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 208
            return getattr(self, '_m_size', None)

        @property
        def inst_genesys__gen__vehicles__upgrade_base_0xc0(self):
            if hasattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xc0'):
                return self._m_inst_genesys__gen__vehicles__upgrade_base_0xc0

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__vehicles__upgrade_base_0xc0)
            self._m_inst_genesys__gen__vehicles__upgrade_base_0xc0 = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__vehicles__upgrade_base_0xc0', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 662978111
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenHeatLevelBehaviourCoordination(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0xc = AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour(self._io, self, self._root)
            self.genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x30 = AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour(self._io, self, self._root)
            self.float32_t_0x54 = self._io.read_f4le()
            self.ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58 = self._io.read_u4le()
            self.array_count_for_0x58 = self._io.read_u2le()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58(self):
            if hasattr(self, '_m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58'):
                return self._m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58)
            self._m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58 = []
            for i in range(self.array_count_for_0x58):
                self._m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58.append(AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour(self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour_0x58', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 96
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1883284107
            return getattr(self, '_m_mu_version_hash', None)


    class CgsCoreStringBase(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ofs_arr_buffer_0x0 = self._io.read_u4le()
            self.array_count_for_0x0 = self._io.read_u4le()

        @property
        def inst_buffer_0x0(self):
            if hasattr(self, '_m_inst_buffer_0x0'):
                return self._m_inst_buffer_0x0

            _pos = self._io.pos()
            self._io.seek(self.ofs_arr_buffer_0x0)
            self._m_inst_buffer_0x0 = (self._io.read_bytes(self.array_count_for_0x0)).decode(u"ascii")
            self._io.seek(_pos)
            return getattr(self, '_m_inst_buffer_0x0', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 12
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 2516314814
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenChallengeActionAccumulateTime(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            self.padding = self._io.read_bytes(2)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1205733723
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngine(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.genesys__gen__engine__power_curve_0xc = AnyGenesysObj.GenesysGenEnginePowerCurve(self._io, self, self._root)
            self.genesys__gen__engine__sound_0x60 = AnyGenesysObj.GenesysGenEngineSound(self._io, self, self._root)
            self.genesys__gen__engine__differentials_0x9c = AnyGenesysObj.GenesysGenEngineDifferentials(self._io, self, self._root)
            self.genesys__gen__engine__normal_quality_engine_0xb8 = AnyGenesysObj.GenesysGenEngineNormalQualityEngine(self._io, self, self._root)
            self.genesys__gen__engine__transmission_0xcc = AnyGenesysObj.GenesysGenEngineTransmission(self._io, self, self._root)
            self.cgs_resource__handle_0xdc = self._io.read_bytes(8)
            self.cgs_resource__handle_0xe4 = self._io.read_bytes(8)
            self.game_changer_id_0xec = self._io.read_u4le()
            self.float32_t_0xf0 = self._io.read_f4le()
            self.float32_t_0xf4 = self._io.read_f4le()
            self.float32_t_0xf8 = self._io.read_f4le()
            self.float32_t_0xfc = self._io.read_f4le()
            self.float32_t_0x100 = self._io.read_f4le()
            self.float32_t_0x104 = self._io.read_f4le()
            self.float32_t_0x108 = self._io.read_f4le()
            self.float32_t_0x10c = self._io.read_f4le()
            self.ptr_genesys__gen__gearbox_0x110 = self._io.read_u4le()
            self.ptr_genesys__gen__gearbox_0x114 = self._io.read_u4le()
            self.ptr_genesys__gen__nitrous_strength_0x118 = self._io.read_u4le()

        @property
        def inst_genesys__gen__gearbox_0x114(self):
            if hasattr(self, '_m_inst_genesys__gen__gearbox_0x114'):
                return self._m_inst_genesys__gen__gearbox_0x114

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__gearbox_0x114)
            self._m_inst_genesys__gen__gearbox_0x114 = AnyGenesysObj.GenesysGenGearbox(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__gearbox_0x114', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 288
            return getattr(self, '_m_size', None)

        @property
        def inst_genesys__gen__gearbox_0x110(self):
            if hasattr(self, '_m_inst_genesys__gen__gearbox_0x110'):
                return self._m_inst_genesys__gen__gearbox_0x110

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__gearbox_0x110)
            self._m_inst_genesys__gen__gearbox_0x110 = AnyGenesysObj.GenesysGenGearbox(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__gearbox_0x110', None)

        @property
        def inst_genesys__gen__nitrous_strength_0x118(self):
            if hasattr(self, '_m_inst_genesys__gen__nitrous_strength_0x118'):
                return self._m_inst_genesys__gen__nitrous_strength_0x118

            _pos = self._io.pos()
            self._io.seek(self.ptr_genesys__gen__nitrous_strength_0x118)
            self._m_inst_genesys__gen__nitrous_strength_0x118 = AnyGenesysObj.GenesysGenNitrousStrength(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__nitrous_strength_0x118', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 834676531
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysObjCollection(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.unk_id = self._io.read_u4le()
            self.collection_start_offset = self._io.read_u4le()
            self.collection_count = self._io.read_u4le()

        @property
        def obj_collection(self):
            if hasattr(self, '_m_obj_collection'):
                return self._m_obj_collection

            _pos = self._io.pos()
            self._io.seek(self.collection_start_offset)
            self._m_obj_collection = []
            for i in range(self.collection_count):
                self._m_obj_collection.append(AnyGenesysObj.Ptr(u"any_genesys_obj", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_obj_collection', None)


    class GenesysGenDriftBehaviourOther(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.game_changer_id_0xc = self._io.read_u4le()
            self.float32_t_0x10 = self._io.read_f4le()
            self.float32_t_0x14 = self._io.read_f4le()
            self.float32_t_0x18 = self._io.read_f4le()
            self.float32_t_0x1c = self._io.read_f4le()
            self.float32_t_0x20 = self._io.read_f4le()
            self.float32_t_0x24 = self._io.read_f4le()
            self.float32_t_0x28 = self._io.read_f4le()
            self.float32_t_0x2c = self._io.read_f4le()
            self.float32_t_0x30 = self._io.read_f4le()
            self.float32_t_0x34 = self._io.read_f4le()
            self.float32_t_0x38 = self._io.read_f4le()
            self.float32_t_0x3c = self._io.read_f4le()
            self.float32_t_0x40 = self._io.read_f4le()
            self.float32_t_0x44 = self._io.read_f4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 76
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 4254634071
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenEngineSound2GainParamWrapper(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.ptr_gain_0xc = self._io.read_u4le()

        @property
        def inst_gain_0xc(self):
            if hasattr(self, '_m_inst_gain_0xc'):
                return self._m_inst_gain_0xc

            _pos = self._io.pos()
            self._io.seek(self.ptr_gain_0xc)
            self._m_inst_gain_0xc = AnyGenesysObj.GenesysGenEngineSound2GainParam(self._io, self, self._root)
            self._io.seek(_pos)
            return getattr(self, '_m_inst_gain_0xc', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 20
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1218098277
            return getattr(self, '_m_mu_version_hash', None)


    class GenesysGenGameplayRevengeBonus(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.bonus_score_0xc = self._io.read_u4le()
            self.description_0x10 = self._io.read_u4le()
            self.game_changer_id_0x14 = self._io.read_u4le()
            self.icon_0x18 = self._io.read_u4le()
            self.name_0x1c = self._io.read_u4le()
            self.duration_0x20 = self._io.read_f4le()
            self.ptr_arr_ptr_genesys__gen__nitrous_parameters_0x24 = self._io.read_u4le()
            self.ptr_arr_ptr_genesys__gen__performance_modifier_0x28 = self._io.read_u4le()
            self.ptr_arr_feature_0x2c = self._io.read_u4le()
            self.array_count_for_0x2c = self._io.read_u2le()
            self.bool8_t_0x32 = self._io.read_u1()
            self.array_count_for_0x24 = self._io.read_u1()
            self.array_count_for_0x28 = self._io.read_u1()
            self.wrecks_count_0x35 = self._io.read_u1()
            self.padding = self._io.read_bytes(2)

        @property
        def inst_feature_0x2c(self):
            if hasattr(self, '_m_inst_feature_0x2c'):
                return self._m_inst_feature_0x2c

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_feature_0x2c)
            self._m_inst_feature_0x2c = []
            for i in range(self.array_count_for_0x2c):
                self._m_inst_feature_0x2c.append(self._io.read_u4le())

            self._io.seek(_pos)
            return getattr(self, '_m_inst_feature_0x2c', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 56
            return getattr(self, '_m_size', None)

        @property
        def inst_genesys__gen__nitrous_parameters_0x24(self):
            if hasattr(self, '_m_inst_genesys__gen__nitrous_parameters_0x24'):
                return self._m_inst_genesys__gen__nitrous_parameters_0x24

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_genesys__gen__nitrous_parameters_0x24)
            self._m_inst_genesys__gen__nitrous_parameters_0x24 = []
            for i in range(self.array_count_for_0x24):
                self._m_inst_genesys__gen__nitrous_parameters_0x24.append(AnyGenesysObj.Ptr(u"genesys__gen__nitrous_parameters", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__nitrous_parameters_0x24', None)

        @property
        def inst_genesys__gen__performance_modifier_0x28(self):
            if hasattr(self, '_m_inst_genesys__gen__performance_modifier_0x28'):
                return self._m_inst_genesys__gen__performance_modifier_0x28

            _pos = self._io.pos()
            self._io.seek(self.ptr_arr_ptr_genesys__gen__performance_modifier_0x28)
            self._m_inst_genesys__gen__performance_modifier_0x28 = []
            for i in range(self.array_count_for_0x28):
                self._m_inst_genesys__gen__performance_modifier_0x28.append(AnyGenesysObj.Ptr(u"genesys__gen__performance_modifier", self._io, self, self._root))

            self._io.seek(_pos)
            return getattr(self, '_m_inst_genesys__gen__performance_modifier_0x28', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1707511637
            return getattr(self, '_m_mu_version_hash', None)


    class Atype(KaitaiStruct):
        def __init__(self, dtype, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.dtype = dtype
            self._read()

        def _read(self):
            _on = self.dtype
            if _on == u"genesys__gen__engine__normal_quality_engine":
                self.data = AnyGenesysObj.GenesysGenEngineNormalQualityEngine(self._io, self, self._root)
            elif _on == u"string_base":
                self.data = AnyGenesysObj.StringBase(self._io, self, self._root)
            elif _on == u"genesys__gen__paint_pack":
                self.data = AnyGenesysObj.GenesysGenPaintPack(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external__yaw_spring_modification":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalYawSpringModification(self._io, self, self._root)
            elif _on == u"genesys__gen__impact_damage_graphs__graph":
                self.data = AnyGenesysObj.GenesysGenImpactDamageGraphsGraph(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__convex_hull_volume":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyConvexHullVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__high_shelf_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenHighShelfDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_info":
                self.data = AnyGenesysObj.GenesysGenVehicleInfo(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_camera_container":
                self.data = AnyGenesysObj.GenesysGenVehicleCameraContainer(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__world__player":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesWorldPlayer(self._io, self, self._root)
            elif _on == u"genesys__gen__online__driving_test_list_groups":
                self.data = AnyGenesysObj.GenesysGenOnlineDrivingTestListGroups(self._io, self, self._root)
            elif _on == u"any_genesys_obj":
                self.data = AnyGenesysObj(self._io)
            elif _on == u"genesys__gen__steering_wheel_behaviour":
                self.data = AnyGenesysObj.GenesysGenSteeringWheelBehaviour(self._io, self, self._root)
            elif _on == u"s4":
                self.data = self._io.read_s4le()
            elif _on == u"genesys__gen__nitrous_parameters__drifting":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersDrifting(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__global__crashing_race_car_vs_traffic":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalCrashingRaceCarVsTraffic(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_colour_palette":
                self.data = AnyGenesysObj.GenesysGenVehicleColourPalette(self._io, self, self._root)
            elif _on == u"genesys__gen__body_movement_behaviour__angle_control":
                self.data = AnyGenesysObj.GenesysGenBodyMovementBehaviourAngleControl(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_effects__battling_effect__extra_roll_params":
                self.data = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffectExtraRollParams(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__aivs_traffic__damage_params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficDamageParams(self._io, self, self._root)
            elif _on == u"genesys__gen__high_pass_butterworth_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenHighPassButterworthDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition__convex_hull_conectivity_data__convex_hull_connecting_face":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionConvexHullConectivityDataConvexHullConnectingFace(self._io, self, self._root)
            elif _on == u"genesys__gen__aiplayer_type":
                self.data = AnyGenesysObj.GenesysGenAiplayerType(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__jump_usage":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersJumpUsage(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fxstate__value_modifier":
                self.data = AnyGenesysObj.GenesysGenPostFxstateValueModifier(self._io, self, self._root)
            elif _on == u"genesys__gen__aiplayer_instance":
                self.data = AnyGenesysObj.GenesysGenAiplayerInstance(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external_globals__impact_shake":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalGlobalsImpactShake(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_damage_behaviour__spot_effect":
                self.data = AnyGenesysObj.GenesysGenVehicleDamageBehaviourSpotEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_vfx_behaviour":
                self.data = AnyGenesysObj.GenesysGenVehicleVfxBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__restrictions":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersRestrictions(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__milestone":
                self.data = AnyGenesysObj.GenesysGenGameplayMilestone(self._io, self, self._root)
            elif _on == u"genesys__gen__event_location":
                self.data = AnyGenesysObj.GenesysGenEventLocation(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle__sound":
                self.data = AnyGenesysObj.GenesysGenVehicleSound(self._io, self, self._root)
            elif _on == u"genesys__gen__uicamera":
                self.data = AnyGenesysObj.GenesysGenUicamera(self._io, self, self._root)
            elif _on == u"genesys__gen__heat_level_sound_set":
                self.data = AnyGenesysObj.GenesysGenHeatLevelSoundSet(self._io, self, self._root)
            elif _on == u"genesys__gen__physical_definition__rigid_body":
                self.data = AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBody(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_info_damage_profile":
                self.data = AnyGenesysObj.GenesysGenCollisionInfoDamageProfile(self._io, self, self._root)
            elif _on == u"genesys__gen__engine_sound2__dsp_param":
                self.data = AnyGenesysObj.GenesysGenEngineSound2DspParam(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__world__player__flip_state":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesWorldPlayerFlipState(self._io, self, self._root)
            elif _on == u"genesys__gen__roadblock_instance":
                self.data = AnyGenesysObj.GenesysGenRoadblockInstance(self._io, self, self._root)
            elif _on == u"genesys__gen__delay_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenDelayDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__player_vs_traffic__damage_params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficDamageParams(self._io, self, self._root)
            elif _on == u"genesys__gen__entitlement":
                self.data = AnyGenesysObj.GenesysGenEntitlement(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicles__performance_upgrades__category":
                self.data = AnyGenesysObj.GenesysGenVehiclesPerformanceUpgradesCategory(self._io, self, self._root)
            elif _on == u"genesys__gen__steering_behaviour__steering_angle_curve":
                self.data = AnyGenesysObj.GenesysGenSteeringBehaviourSteeringAngleCurve(self._io, self, self._root)
            elif _on == u"genesys__gen__scoring_action":
                self.data = AnyGenesysObj.GenesysGenScoringAction(self._io, self, self._root)
            elif _on == u"genesys__gen__damage_bar_profiles__profile":
                self.data = AnyGenesysObj.GenesysGenDamageBarProfilesProfile(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__jump_over_players":
                self.data = AnyGenesysObj.GenesysGenChallengeActionJumpOverPlayers(self._io, self, self._root)
            elif _on == u"genesys__gen__donut_ability":
                self.data = AnyGenesysObj.GenesysGenDonutAbility(self._io, self, self._root)
            elif _on == u"genesys__gen__heat_level_sound_set__nitrous":
                self.data = AnyGenesysObj.GenesysGenHeatLevelSoundSetNitrous(self._io, self, self._root)
            elif _on == u"genesys__gen__body_movement_behaviour":
                self.data = AnyGenesysObj.GenesysGenBodyMovementBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_gradient_adjustments":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayGradientAdjustments(self._io, self, self._root)
            elif _on == u"genesys__gen__tyres__tyres":
                self.data = AnyGenesysObj.GenesysGenTyresTyres(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__global__crashing_race_car_vs_crashing_race_car":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalCrashingRaceCarVsCrashingRaceCar(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__allowed_vehicle_list":
                self.data = AnyGenesysObj.GenesysGenGameplayAllowedVehicleList(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__player_vs_ai":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAi(self._io, self, self._root)
            elif _on == u"genesys__gen__drift_behaviour__yaw_torque":
                self.data = AnyGenesysObj.GenesysGenDriftBehaviourYawTorque(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__cop_type":
                self.data = AnyGenesysObj.GenesysGenGameplayCopType(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fx_keyframe__general":
                self.data = AnyGenesysObj.GenesysGenPostFxKeyframeGeneral(self._io, self, self._root)
            elif _on == u"genesys__gen__online__driving_test_list":
                self.data = AnyGenesysObj.GenesysGenOnlineDrivingTestList(self._io, self, self._root)
            elif _on == u"genesys__gen__colour_group":
                self.data = AnyGenesysObj.GenesysGenColourGroup(self._io, self, self._root)
            elif _on == u"genesys__gen__light__cone":
                self.data = AnyGenesysObj.GenesysGenLightCone(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_shake_effect__translation__axis_params":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectTranslationAxisParams(self._io, self, self._root)
            elif _on == u"genesys__gen__physical_definition":
                self.data = AnyGenesysObj.GenesysGenPhysicalDefinition(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters":
                self.data = AnyGenesysObj.GenesysGenNitrousParameters(self._io, self, self._root)
            elif _on == u"genesys__object":
                self.data = AnyGenesysObj.GenesysObject(self._io, self, self._root)
            elif _on == u"genesys__gen__drift_behaviour__side_force":
                self.data = AnyGenesysObj.GenesysGenDriftBehaviourSideForce(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__speed_camera_action":
                self.data = AnyGenesysObj.GenesysGenChallengeActionSpeedCameraAction(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_sound_params__long_spin":
                self.data = AnyGenesysObj.GenesysGenTyreSoundParamsLongSpin(self._io, self, self._root)
            elif _on == u"genesys__gen__suspension":
                self.data = AnyGenesysObj.GenesysGenSuspension(self._io, self, self._root)
            elif _on == u"genesys__gen__ginsu_sequence_item":
                self.data = AnyGenesysObj.GenesysGenGinsuSequenceItem(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle__driver_setup":
                self.data = AnyGenesysObj.GenesysGenVehicleDriverSetup(self._io, self, self._root)
            elif _on == u"genesys__gen__custom_chevron":
                self.data = AnyGenesysObj.GenesysGenCustomChevron(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_damage_behaviour":
                self.data = AnyGenesysObj.GenesysGenVehicleDamageBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__sequence_item":
                self.data = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
            elif _on == u"genesys__gen__online_challenge":
                self.data = AnyGenesysObj.GenesysGenOnlineChallenge(self._io, self, self._root)
            elif _on == u"genesys__gen__mixer_channel__priority":
                self.data = AnyGenesysObj.GenesysGenMixerChannelPriority(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_vfx_behaviour__front_rear_params__smoke_params":
                self.data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsSmokeParams(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__aivs_crashing_race_car":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsCrashingRaceCar(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicles__vehicle_category_info":
                self.data = AnyGenesysObj.GenesysGenVehiclesVehicleCategoryInfo(self._io, self, self._root)
            elif _on == u"genesys__gen__wcvfx_behaviour__lights":
                self.data = AnyGenesysObj.GenesysGenWcvfxBehaviourLights(self._io, self, self._root)
            elif _on == u"genesys__gen__ginsu_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenGinsuDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_shake_effect__translation":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectTranslation(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_damage_behaviour__bodypart":
                self.data = AnyGenesysObj.GenesysGenVehicleDamageBehaviourBodypart(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre__long__grip__curve":
                self.data = AnyGenesysObj.GenesysGenTyreLongGripCurve(self._io, self, self._root)
            elif _on == u"genesys__gen__offline_event":
                self.data = AnyGenesysObj.GenesysGenOfflineEvent(self._io, self, self._root)
            elif _on == u"genesys__gen__corona":
                self.data = AnyGenesysObj.GenesysGenCorona(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__global":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesGlobal(self._io, self, self._root)
            elif _on == u"genesys__gen__enable_compound_behaviour":
                self.data = AnyGenesysObj.GenesysGenEnableCompoundBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__event_arena":
                self.data = AnyGenesysObj.GenesysGenEventArena(self._io, self, self._root)
            elif _on == u"genesys__gen__paint_pack_group":
                self.data = AnyGenesysObj.GenesysGenPaintPackGroup(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fx_keyframe__depth_of__field":
                self.data = AnyGenesysObj.GenesysGenPostFxKeyframeDepthOfField(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_info":
                self.data = AnyGenesysObj.GenesysGenCollisionInfo(self._io, self, self._root)
            elif _on == u"genesys__gen__distortion_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenDistortionDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__jump_stats":
                self.data = AnyGenesysObj.GenesysGenChallengeActionJumpStats(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external__speed_based_height_change":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalSpeedBasedHeightChange(self._io, self, self._root)
            elif _on == u"genesys__gen__gearbox":
                self.data = AnyGenesysObj.GenesysGenGearbox(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_sound_params__lateral":
                self.data = AnyGenesysObj.GenesysGenTyreSoundParamsLateral(self._io, self, self._root)
            elif _on == u"genesys__gen__corona__beam":
                self.data = AnyGenesysObj.GenesysGenCoronaBeam(self._io, self, self._root)
            elif _on == u"genesys__gen__rollout":
                self.data = AnyGenesysObj.GenesysGenRollout(self._io, self, self._root)
            elif _on == u"genesys__gen__online_route":
                self.data = AnyGenesysObj.GenesysGenOnlineRoute(self._io, self, self._root)
            elif _on == u"genesys__gen__scoring_action__online_scoring_feedback":
                self.data = AnyGenesysObj.GenesysGenScoringActionOnlineScoringFeedback(self._io, self, self._root)
            elif _on == u"genesys__gen__safehouse":
                self.data = AnyGenesysObj.GenesysGenSafehouse(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__slipstreaming":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersSlipstreaming(self._io, self, self._root)
            elif _on == u"genesys__gen__event__checkpoint_info":
                self.data = AnyGenesysObj.GenesysGenEventCheckpointInfo(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__speedbreaker_usage":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersSpeedbreakerUsage(self._io, self, self._root)
            elif _on == u"genesys__gen__hard_driving_behaviour__steering_effect":
                self.data = AnyGenesysObj.GenesysGenHardDrivingBehaviourSteeringEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_info__payload_damage":
                self.data = AnyGenesysObj.GenesysGenCollisionInfoPayloadDamage(self._io, self, self._root)
            elif _on == u"genesys__gen__heat_level__behaviour_coordination":
                self.data = AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordination(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_effects__battling_effect":
                self.data = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__engine__power_curve":
                self.data = AnyGenesysObj.GenesysGenEnginePowerCurve(self._io, self, self._root)
            elif _on == u"genesys__gen__wheel_suspension_constraint":
                self.data = AnyGenesysObj.GenesysGenWheelSuspensionConstraint(self._io, self, self._root)
            elif _on == u"genesys__gen__offline_event__custom_chevrons":
                self.data = AnyGenesysObj.GenesysGenOfflineEventCustomChevrons(self._io, self, self._root)
            elif _on == u"genesys__gen__pidcontroller":
                self.data = AnyGenesysObj.GenesysGenPidcontroller(self._io, self, self._root)
            elif _on == u"genesys__gen__online_event":
                self.data = AnyGenesysObj.GenesysGenOnlineEvent(self._io, self, self._root)
            elif _on == u"genesys__gen__make_physical_behaviour":
                self.data = AnyGenesysObj.GenesysGenMakePhysicalBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__handbrake_ability":
                self.data = AnyGenesysObj.GenesysGenHandbrakeAbility(self._io, self, self._root)
            elif _on == u"genesys__gen__general_trigger_sequence_item":
                self.data = AnyGenesysObj.GenesysGenGeneralTriggerSequenceItem(self._io, self, self._root)
            elif _on == u"cgs_core__unique_id":
                self.data = AnyGenesysObj.CgsCoreUniqueId(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__drift_marker":
                self.data = AnyGenesysObj.GenesysGenGameplayDriftMarker(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_sound_params__long_spin_braking":
                self.data = AnyGenesysObj.GenesysGenTyreSoundParamsLongSpinBraking(self._io, self, self._root)
            elif _on == u"bool8_t":
                self.data = AnyGenesysObj.Bool8T(self._io, self, self._root)
            elif _on == u"genesys__gen__traffic_vehicle":
                self.data = AnyGenesysObj.GenesysGenTrafficVehicle(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_bonnet":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayBonnet(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicles__performance_upgrades":
                self.data = AnyGenesysObj.GenesysGenVehiclesPerformanceUpgrades(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external__acceleration_movement":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalAccelerationMovement(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fx_keyframe":
                self.data = AnyGenesysObj.GenesysGenPostFxKeyframe(self._io, self, self._root)
            elif _on == u"genesys__gen__voice_group":
                self.data = AnyGenesysObj.GenesysGenVoiceGroup(self._io, self, self._root)
            elif _on == u"genesys__gen__nucleus_grant_mappings_list__mapping":
                self.data = AnyGenesysObj.GenesysGenNucleusGrantMappingsListMapping(self._io, self, self._root)
            elif _on == u"genesys__gen__heat_level_sound_set__sirens":
                self.data = AnyGenesysObj.GenesysGenHeatLevelSoundSetSirens(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre__lateral__slip__factors":
                self.data = AnyGenesysObj.GenesysGenTyreLateralSlipFactors(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay_trigger":
                self.data = AnyGenesysObj.GenesysGenGameplayTrigger(self._io, self, self._root)
            elif _on == u"genesys__gen__pan2ddsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenPan2ddspPlugIn(self._io, self, self._root)
            elif _on == u"s1":
                self.data = self._io.read_s1()
            elif _on == u"genesys__gen__vehicle_component__wheel":
                self.data = AnyGenesysObj.GenesysGenVehicleComponentWheel(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_gradient_adjustments__params":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayGradientAdjustmentsParams(self._io, self, self._root)
            elif _on == u"genesys__gen__mixer_channel_sequence_item__mixer_channel_double_value":
                self.data = AnyGenesysObj.GenesysGenMixerChannelSequenceItemMixerChannelDoubleValue(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_surface_profile":
                self.data = AnyGenesysObj.GenesysGenVehicleSurfaceProfile(self._io, self, self._root)
            elif _on == u"genesys__gen__passby_sequence_behaviour":
                self.data = AnyGenesysObj.GenesysGenPassbySequenceBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__physics__crashing_rules__impact_rules":
                self.data = AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fxsequence_item":
                self.data = AnyGenesysObj.GenesysGenPostFxsequenceItem(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__speed_run":
                self.data = AnyGenesysObj.GenesysGenChallengeActionSpeedRun(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_rear_view_globals":
                self.data = AnyGenesysObj.GenesysGenCameraRearViewGlobals(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_strength":
                self.data = AnyGenesysObj.GenesysGenNitrousStrength(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__profile":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarProfile(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_shake_effect__rotation__axis_params":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectRotationAxisParams(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_paint":
                self.data = AnyGenesysObj.GenesysGenVehiclePaint(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle__gameplay":
                self.data = AnyGenesysObj.GenesysGenVehicleGameplay(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicles__modifier_upgrade":
                self.data = AnyGenesysObj.GenesysGenVehiclesModifierUpgrade(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__nitrous_power":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersNitrousPower(self._io, self, self._root)
            elif _on == u"genesys__gen__game_unlock":
                self.data = AnyGenesysObj.GenesysGenGameUnlock(self._io, self, self._root)
            elif _on == u"genesys__gen__wheel_sizes":
                self.data = AnyGenesysObj.GenesysGenWheelSizes(self._io, self, self._root)
            elif _on == u"float32_t":
                self.data = AnyGenesysObj.Float32T(self._io, self, self._root)
            elif _on == u"genesys__gen__nucleus_entitlement_tag":
                self.data = AnyGenesysObj.GenesysGenNucleusEntitlementTag(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold__speed_control":
                self.data = AnyGenesysObj.GenesysGenGameplayBlacklistShutdownDataDamageThresholdSpeedControl(self._io, self, self._root)
            elif _on == u"u4":
                self.data = self._io.read_u4le()
            elif _on == u"genesys__gen__dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCar(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternal(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_vfx_behaviour__front_rear_params":
                self.data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParams(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__get_to_location":
                self.data = AnyGenesysObj.GenesysGenChallengeActionGetToLocation(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__nitrous_usage":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersNitrousUsage(self._io, self, self._root)
            elif _on == u"genesys__gen__road_block_definition":
                self.data = AnyGenesysObj.GenesysGenRoadBlockDefinition(self._io, self, self._root)
            elif _on == u"genesys__gen__engine__reverse_whine":
                self.data = AnyGenesysObj.GenesysGenEngineReverseWhine(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__blacklist_shutdown_data__damage_threshold":
                self.data = AnyGenesysObj.GenesysGenGameplayBlacklistShutdownDataDamageThreshold(self._io, self, self._root)
            elif _on == u"genesys__gen__event_arena_data":
                self.data = AnyGenesysObj.GenesysGenEventArenaData(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_bumper":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayBumper(self._io, self, self._root)
            elif _on == u"genesys__gen__thank_you_screen_item":
                self.data = AnyGenesysObj.GenesysGenThankYouScreenItem(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBody(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__global__race_car_vs_race_car__params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCarParams(self._io, self, self._root)
            elif _on == u"gen_obj":
                self.data = AnyGenesysObj.GenObj(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_sound_params__longitudinal":
                self.data = AnyGenesysObj.GenesysGenTyreSoundParamsLongitudinal(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__global__traffic_vs_dynamic":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalTrafficVsDynamic(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre":
                self.data = AnyGenesysObj.GenesysGenTyre(self._io, self, self._root)
            elif _on == u"genesys__gen__aligning_torque":
                self.data = AnyGenesysObj.GenesysGenAligningTorque(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_vfx_behaviour__spot_effect":
                self.data = AnyGenesysObj.GenesysGenVehicleVfxBehaviourSpotEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__corona__glow":
                self.data = AnyGenesysObj.GenesysGenCoronaGlow(self._io, self, self._root)
            elif _on == u"genesys__gen__light__base__flash_pattern":
                self.data = AnyGenesysObj.GenesysGenLightBaseFlashPattern(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_vfx_behaviour__front_rear_params__long_params":
                self.data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLongParams(self._io, self, self._root)
            elif _on == u"genesys__gen__point2dwith_tangents":
                self.data = AnyGenesysObj.GenesysGenPoint2dwithTangents(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition__convex_hull_conectivity_data":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionConvexHullConectivityData(self._io, self, self._root)
            elif _on == u"genesys__gen__offline_event__alternate_routes":
                self.data = AnyGenesysObj.GenesysGenOfflineEventAlternateRoutes(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_effects__traffic_effect__extra_roll_params":
                self.data = AnyGenesysObj.GenesysGenCollisionEffectsTrafficEffectExtraRollParams(self._io, self, self._root)
            elif _on == u"u2":
                self.data = self._io.read_u2le()
            elif _on == u"genesys__gen__vehicle_info__extra_axle":
                self.data = AnyGenesysObj.GenesysGenVehicleInfoExtraAxle(self._io, self, self._root)
            elif _on == u"genesys__gen__cloud_compete_award":
                self.data = AnyGenesysObj.GenesysGenCloudCompeteAward(self._io, self, self._root)
            elif _on == u"cgs_resource__handle":
                self.data = AnyGenesysObj.CgsResourceHandle(self._io, self, self._root)
            elif _on == u"genesys__gen__point2d":
                self.data = AnyGenesysObj.GenesysGenPoint2d(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__donutting":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersDonutting(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_component":
                self.data = AnyGenesysObj.GenesysGenVehicleComponent(self._io, self, self._root)
            elif _on == u"genesys__gen__damage_bar_profiles":
                self.data = AnyGenesysObj.GenesysGenDamageBarProfiles(self._io, self, self._root)
            elif _on == u"genesys__gen__score_view_model":
                self.data = AnyGenesysObj.GenesysGenScoreViewModel(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__car_state":
                self.data = AnyGenesysObj.GenesysGenChallengeActionCarState(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_effect_sequence_item__effect_double_value":
                self.data = AnyGenesysObj.GenesysGenRaceCarEffectSequenceItemEffectDoubleValue(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__hitting_another_competitor":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersHittingAnotherCompetitor(self._io, self, self._root)
            elif _on == u"rw_math_vpu__matrix44affine":
                self.data = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__player_vs_ai__damage_params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiDamageParams(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__offline_upgrade":
                self.data = AnyGenesysObj.GenesysGenGameplayOfflineUpgrade(self._io, self, self._root)
            elif _on == u"genesys__gen__mixing_group":
                self.data = AnyGenesysObj.GenesysGenMixingGroup(self._io, self, self._root)
            elif _on == u"int16_t":
                self.data = AnyGenesysObj.Int16T(self._io, self, self._root)
            elif _on == u"genesys__gen__wcvfx_behaviour__spot_effects":
                self.data = AnyGenesysObj.GenesysGenWcvfxBehaviourSpotEffects(self._io, self, self._root)
            elif _on == u"genesys__gen__submix_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenSubmixDspPlugIn(self._io, self, self._root)
            elif _on == u"s2":
                self.data = self._io.read_s2le()
            elif _on == u"genesys__gen__tyres":
                self.data = AnyGenesysObj.GenesysGenTyres(self._io, self, self._root)
            elif _on == u"genesys__gen__wave_sequence_item__fade":
                self.data = AnyGenesysObj.GenesysGenWaveSequenceItemFade(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external__speed_based_movement":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalSpeedBasedMovement(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_effects__world_effect":
                self.data = AnyGenesysObj.GenesysGenCollisionEffectsWorldEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__global__race_car_vs_race_car__crashed_params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCarCrashedParams(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_handling_disruption_effect":
                self.data = AnyGenesysObj.GenesysGenRaceCarHandlingDisruptionEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__rollout__weapon_data":
                self.data = AnyGenesysObj.GenesysGenRolloutWeaponData(self._io, self, self._root)
            elif _on == u"genesys__gen__damage_bar_profiles__profile__segment_data":
                self.data = AnyGenesysObj.GenesysGenDamageBarProfilesProfileSegmentData(self._io, self, self._root)
            elif _on == u"genesys__gen__jump_timeline_controller":
                self.data = AnyGenesysObj.GenesysGenJumpTimelineController(self._io, self, self._root)
            elif _on == u"genesys__gen__online__license_plate":
                self.data = AnyGenesysObj.GenesysGenOnlineLicensePlate(self._io, self, self._root)
            elif _on == u"genesys__gen__physical_definition__rigid_body__sphere_volume":
                self.data = AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodySphereVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_vfx_behaviour__long_lat_params":
                self.data = AnyGenesysObj.GenesysGenTyreVfxBehaviourLongLatParams(self._io, self, self._root)
            elif _on == u"genesys__gen__drift_behaviour":
                self.data = AnyGenesysObj.GenesysGenDriftBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay_trigger__input":
                self.data = AnyGenesysObj.GenesysGenGameplayTriggerInput(self._io, self, self._root)
            elif _on == u"genesys__gen__uilist_items":
                self.data = AnyGenesysObj.GenesysGenUilistItems(self._io, self, self._root)
            elif _on == u"genesys__gen__traffic_vehicle_traits":
                self.data = AnyGenesysObj.GenesysGenTrafficVehicleTraits(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_damage_behaviour__bodypart__damage_threshold":
                self.data = AnyGenesysObj.GenesysGenVehicleDamageBehaviourBodypartDamageThreshold(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__crash_escape":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersCrashEscape(self._io, self, self._root)
            elif _on == u"genesys__gen__drift_behaviour__other":
                self.data = AnyGenesysObj.GenesysGenDriftBehaviourOther(self._io, self, self._root)
            elif _on == u"strz":
                self.data = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            elif _on == u"genesys__gen__impact_damage_graphs":
                self.data = AnyGenesysObj.GenesysGenImpactDamageGraphs(self._io, self, self._root)
            elif _on == u"genesys__gen__physical_definition__rigid_body__convex_hull_volume":
                self.data = AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodyConvexHullVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__traffic_flow_type":
                self.data = AnyGenesysObj.GenesysGenTrafficFlowType(self._io, self, self._root)
            elif _on == u"genesys_obj_collection":
                self.data = AnyGenesysObj.GenesysObjCollection(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters_usage":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersUsage(self._io, self, self._root)
            elif _on == u"genesys__gen__score_view_model__score":
                self.data = AnyGenesysObj.GenesysGenScoreViewModelScore(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle__gameplay__mod_effect":
                self.data = AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge__location":
                self.data = AnyGenesysObj.GenesysGenChallengeLocation(self._io, self, self._root)
            elif _on == u"genesys__gen__timeline_controllers__race_car_entity_timeline_controller":
                self.data = AnyGenesysObj.GenesysGenTimelineControllersRaceCarEntityTimelineController(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_vfx_behaviour":
                self.data = AnyGenesysObj.GenesysGenTyreVfxBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__blacklist_shutdown_data":
                self.data = AnyGenesysObj.GenesysGenGameplayBlacklistShutdownData(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_paint__material_properties":
                self.data = AnyGenesysObj.GenesysGenVehiclePaintMaterialProperties(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_effect_sequence_item":
                self.data = AnyGenesysObj.GenesysGenRaceCarEffectSequenceItem(self._io, self, self._root)
            elif _on == u"genesys__gen__engine_sound2__gain_param_wrapper":
                self.data = AnyGenesysObj.GenesysGenEngineSound2GainParamWrapper(self._io, self, self._root)
            elif _on == u"genesys__gen__wcvfx_behaviour__coronas":
                self.data = AnyGenesysObj.GenesysGenWcvfxBehaviourCoronas(self._io, self, self._root)
            elif _on == u"genesys__gen__physics__crashing_rules":
                self.data = AnyGenesysObj.GenesysGenPhysicsCrashingRules(self._io, self, self._root)
            elif _on == u"genesys__gen__hard_driving_behaviour":
                self.data = AnyGenesysObj.GenesysGenHardDrivingBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__physical_definition__rigid_body__cylinder_volume":
                self.data = AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodyCylinderVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__physics__landing_damage":
                self.data = AnyGenesysObj.GenesysGenPhysicsLandingDamage(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__accumulate_distance":
                self.data = AnyGenesysObj.GenesysGenChallengeActionAccumulateDistance(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_vfx_behaviour__front_rear_params__lat_params":
                self.data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLatParams(self._io, self, self._root)
            elif _on == u"genesys__gen__quit_sequence_timeline_controller":
                self.data = AnyGenesysObj.GenesysGenQuitSequenceTimelineController(self._io, self, self._root)
            elif _on == u"rw_math_vpu__vector3":
                self.data = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre__long__slip__factors":
                self.data = AnyGenesysObj.GenesysGenTyreLongSlipFactors(self._io, self, self._root)
            elif _on == u"genesys__gen__brake_behaviour":
                self.data = AnyGenesysObj.GenesysGenBrakeBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__offline_event__checkpoint_info":
                self.data = AnyGenesysObj.GenesysGenOfflineEventCheckpointInfo(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_info__world_effect":
                self.data = AnyGenesysObj.GenesysGenCollisionInfoWorldEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__aivs_traffic":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTraffic(self._io, self, self._root)
            elif _on == u"genesys__gen__uilist_items__item":
                self.data = AnyGenesysObj.GenesysGenUilistItemsItem(self._io, self, self._root)
            elif _on == u"genesys__gen__engine__sound":
                self.data = AnyGenesysObj.GenesysGenEngineSound(self._io, self, self._root)
            elif _on == u"rw_math_vpu__vector2":
                self.data = AnyGenesysObj.RwMathVpuVector2(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__accumulation_helper_data":
                self.data = AnyGenesysObj.GenesysGenChallengeActionAccumulationHelperData(self._io, self, self._root)
            elif _on == u"genesys__gen__race_balancing_data__opponent_balancing_data":
                self.data = AnyGenesysObj.GenesysGenRaceBalancingDataOpponentBalancingData(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicles__tyre_upgrade":
                self.data = AnyGenesysObj.GenesysGenVehiclesTyreUpgrade(self._io, self, self._root)
            elif _on == u"genesys__gen__drift_behaviour__drift_scale":
                self.data = AnyGenesysObj.GenesysGenDriftBehaviourDriftScale(self._io, self, self._root)
            elif _on == u"genesys__gen__online__driving_test_list_group":
                self.data = AnyGenesysObj.GenesysGenOnlineDrivingTestListGroup(self._io, self, self._root)
            elif _on == u"genesys__gen__easy_guide__page":
                self.data = AnyGenesysObj.GenesysGenEasyGuidePage(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__global__race_car_vs_race_car":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCar(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge__challenge_part":
                self.data = AnyGenesysObj.GenesysGenChallengeChallengePart(self._io, self, self._root)
            elif _on == u"genesys__gen__event":
                self.data = AnyGenesysObj.GenesysGenEvent(self._io, self, self._root)
            elif _on == u"genesys__gen__light__spot":
                self.data = AnyGenesysObj.GenesysGenLightSpot(self._io, self, self._root)
            elif _on == u"genesys__gen__sequence_timeline_controller":
                self.data = AnyGenesysObj.GenesysGenSequenceTimelineController(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_strength__jump":
                self.data = AnyGenesysObj.GenesysGenNitrousStrengthJump(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__milestone__entry":
                self.data = AnyGenesysObj.GenesysGenGameplayMilestoneEntry(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_bonnet__wind_sound":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayBonnetWindSound(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__player_vs_crashing_race_car__basic_params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarBasicParams(self._io, self, self._root)
            elif _on == u"genesys__gen__handbrake_ability__handbrake_grip_values":
                self.data = AnyGenesysObj.GenesysGenHandbrakeAbilityHandbrakeGripValues(self._io, self, self._root)
            elif _on == u"genesys__gen__steering_wheel_physics":
                self.data = AnyGenesysObj.GenesysGenSteeringWheelPhysics(self._io, self, self._root)
            elif _on == u"f4":
                self.data = self._io.read_f4le()
            elif _on == u"genesys__gen__send_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenSendDspPlugIn(self._io, self, self._root)
            elif _on == u"u1":
                self.data = self._io.read_u1()
            elif _on == u"genesys__gen__lfo_sequence_item__lfo_double_value":
                self.data = AnyGenesysObj.GenesysGenLfoSequenceItemLfoDoubleValue(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_rear_view":
                self.data = AnyGenesysObj.GenesysGenCameraRearView(self._io, self, self._root)
            elif _on == u"genesys__gen__sequence_items__post_fx_override_sequence_item__effect_double_value":
                self.data = AnyGenesysObj.GenesysGenSequenceItemsPostFxOverrideSequenceItemEffectDoubleValue(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__fatal_hit":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersFatalHit(self._io, self, self._root)
            elif _on == u"uint16_t":
                self.data = AnyGenesysObj.Uint16T(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_shake_effect__rotation":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectRotation(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_effects":
                self.data = AnyGenesysObj.GenesysGenCollisionEffects(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fx_keyframe__vignette":
                self.data = AnyGenesysObj.GenesysGenPostFxKeyframeVignette(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__capsule_volume":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyCapsuleVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__wave_sequence_item":
                self.data = AnyGenesysObj.GenesysGenWaveSequenceItem(self._io, self, self._root)
            elif _on == u"genesys__gen__score_view_model__score_data":
                self.data = AnyGenesysObj.GenesysGenScoreViewModelScoreData(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external_globals__lens_properties":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalGlobalsLensProperties(self._io, self, self._root)
            elif _on == u"genesys__gen__low_pass_butterworth_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenLowPassButterworthDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__light__point":
                self.data = AnyGenesysObj.GenesysGenLightPoint(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__world__crashed_player":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesWorldCrashedPlayer(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__action_base__feedback_data":
                self.data = AnyGenesysObj.GenesysGenChallengeActionActionBaseFeedbackData(self._io, self, self._root)
            elif _on == u"genesys__gen__road_block_layer__item":
                self.data = AnyGenesysObj.GenesysGenRoadBlockLayerItem(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__accumulate_takedowns":
                self.data = AnyGenesysObj.GenesysGenChallengeActionAccumulateTakedowns(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__hit_trigger":
                self.data = AnyGenesysObj.GenesysGenChallengeActionHitTrigger(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__player_vs_traffic":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTraffic(self._io, self, self._root)
            elif _on == u"genesys__gen__physics__damage_bar_profile":
                self.data = AnyGenesysObj.GenesysGenPhysicsDamageBarProfile(self._io, self, self._root)
            elif _on == u"genesys__gen__physical_definition__rigid_body__capsule_volume":
                self.data = AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodyCapsuleVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__physics__damage_bar_profile__impact_location_damage_scale":
                self.data = AnyGenesysObj.GenesysGenPhysicsDamageBarProfileImpactLocationDamageScale(self._io, self, self._root)
            elif _on == u"genesys__gen__store_item":
                self.data = AnyGenesysObj.GenesysGenStoreItem(self._io, self, self._root)
            elif _on == u"genesys__gen__smash_proxy_behaviour":
                self.data = AnyGenesysObj.GenesysGenSmashProxyBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__box_volume":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyBoxVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__online_challenge_target":
                self.data = AnyGenesysObj.GenesysGenOnlineChallengeTarget(self._io, self, self._root)
            elif _on == u"genesys__gen__engine":
                self.data = AnyGenesysObj.GenesysGenEngine(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicles__upgrade_base":
                self.data = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_shake_effect":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__accumulate_near_misses":
                self.data = AnyGenesysObj.GenesysGenChallengeActionAccumulateNearMisses(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__coop_accumulate_distance":
                self.data = AnyGenesysObj.GenesysGenChallengeActionCoopAccumulateDistance(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__traffic_near_miss":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersTrafficNearMiss(self._io, self, self._root)
            elif _on == u"genesys__gen__dynamic_additional_info":
                self.data = AnyGenesysObj.GenesysGenDynamicAdditionalInfo(self._io, self, self._root)
            elif _on == u"genesys__gen__mixer_channel":
                self.data = AnyGenesysObj.GenesysGenMixerChannel(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__world":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesWorld(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay_trigger__output__sequence_output":
                self.data = AnyGenesysObj.GenesysGenGameplayTriggerOutputSequenceOutput(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__world__traffic":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesWorldTraffic(self._io, self, self._root)
            elif _on == u"genesys__gen__band_pass_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenBandPassDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_surface_profile__surface_link":
                self.data = AnyGenesysObj.GenesysGenVehicleSurfaceProfileSurfaceLink(self._io, self, self._root)
            elif _on == u"genesys__gen__heat_level":
                self.data = AnyGenesysObj.GenesysGenHeatLevel(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__aivs_traffic__basic_params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficBasicParams(self._io, self, self._root)
            elif _on == u"genesys__gen__engine_sound2__dsp_param_wrapper":
                self.data = AnyGenesysObj.GenesysGenEngineSound2DspParamWrapper(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_sound_params":
                self.data = AnyGenesysObj.GenesysGenTyreSoundParams(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_info__traffic_effect":
                self.data = AnyGenesysObj.GenesysGenCollisionInfoTrafficEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__player_vs_traffic__basic_params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficBasicParams(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__punch_usage":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersPunchUsage(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__taking_shortcut":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersTakingShortcut(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__cylinder_volume":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyCylinderVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__online__vote_event":
                self.data = AnyGenesysObj.GenesysGenOnlineVoteEvent(self._io, self, self._root)
            elif _on == u"int32_t":
                self.data = AnyGenesysObj.Int32T(self._io, self, self._root)
            elif _on == u"genesys__gen__traffic_flow":
                self.data = AnyGenesysObj.GenesysGenTrafficFlow(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_info__battling_effect":
                self.data = AnyGenesysObj.GenesysGenCollisionInfoBattlingEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicles__nitrous_upgrade":
                self.data = AnyGenesysObj.GenesysGenVehiclesNitrousUpgrade(self._io, self, self._root)
            elif _on == u"genesys__gen__game_unlock_list":
                self.data = AnyGenesysObj.GenesysGenGameUnlockList(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__revenge_bonus":
                self.data = AnyGenesysObj.GenesysGenGameplayRevengeBonus(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_damage_behaviour__damage_sequence":
                self.data = AnyGenesysObj.GenesysGenVehicleDamageBehaviourDamageSequence(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle__gameplay__damage_stats":
                self.data = AnyGenesysObj.GenesysGenVehicleGameplayDamageStats(self._io, self, self._root)
            elif _on == u"genesys__gen__control_mesh":
                self.data = AnyGenesysObj.GenesysGenControlMesh(self._io, self, self._root)
            elif _on == u"genesys__gen__light__base":
                self.data = AnyGenesysObj.GenesysGenLightBase(self._io, self, self._root)
            elif _on == u"genesys__gen__drift_behaviour__drift_exit":
                self.data = AnyGenesysObj.GenesysGenDriftBehaviourDriftExit(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__do_jump":
                self.data = AnyGenesysObj.GenesysGenChallengeActionDoJump(self._io, self, self._root)
            elif _on == u"genesys__gen__event_list":
                self.data = AnyGenesysObj.GenesysGenEventList(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__race_car_vs_dynamic":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarRaceCarVsDynamic(self._io, self, self._root)
            elif _on == u"genesys__gen__gearbox__gear":
                self.data = AnyGenesysObj.GenesysGenGearboxGear(self._io, self, self._root)
            elif _on == u"genesys__gen__donut_ability__donut_scale":
                self.data = AnyGenesysObj.GenesysGenDonutAbilityDonutScale(self._io, self, self._root)
            elif _on == u"genesys__gen__tyres__surface_effects":
                self.data = AnyGenesysObj.GenesysGenTyresSurfaceEffects(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre__lateral__grip__curve":
                self.data = AnyGenesysObj.GenesysGenTyreLateralGripCurve(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_info__axle":
                self.data = AnyGenesysObj.GenesysGenVehicleInfoAxle(self._io, self, self._root)
            elif _on == u"genesys__gen__nucleus_grant_mappings_list":
                self.data = AnyGenesysObj.GenesysGenNucleusGrantMappingsList(self._io, self, self._root)
            elif _on == u"genesys__gen__thankyou_mapping":
                self.data = AnyGenesysObj.GenesysGenThankyouMapping(self._io, self, self._root)
            elif _on == u"genesys__gen__sound_distance_falloff":
                self.data = AnyGenesysObj.GenesysGenSoundDistanceFalloff(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__action_base":
                self.data = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
            elif _on == u"char":
                self.data = AnyGenesysObj.Char(self._io, self, self._root)
            elif _on == u"genesys__gen__race_balancing_data":
                self.data = AnyGenesysObj.GenesysGenRaceBalancingData(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition__physical_definition__rigid_body__sphere_volume":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodySphereVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external__speed_based_movement__high__speed__shake":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalSpeedBasedMovementHighSpeedShake(self._io, self, self._root)
            elif _on == u"genesys__gen__store_pack_list":
                self.data = AnyGenesysObj.GenesysGenStorePackList(self._io, self, self._root)
            elif _on == u"genesys__gen__game_rank":
                self.data = AnyGenesysObj.GenesysGenGameRank(self._io, self, self._root)
            elif _on == u"genesys__gen__snd_player_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenSndPlayerDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_effects__battling_effect__skid_effects":
                self.data = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffectSkidEffects(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_info__battling_damage":
                self.data = AnyGenesysObj.GenesysGenCollisionInfoBattlingDamage(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicles__sound__transmission_whine":
                self.data = AnyGenesysObj.GenesysGenVehiclesSoundTransmissionWhine(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__allowed_vehicle_list__vehicle_and_mods":
                self.data = AnyGenesysObj.GenesysGenGameplayAllowedVehicleListVehicleAndMods(self._io, self, self._root)
            elif _on == u"genesys__gen__store_pack":
                self.data = AnyGenesysObj.GenesysGenStorePack(self._io, self, self._root)
            elif _on == u"genesys__gen__wcvfx_behaviour":
                self.data = AnyGenesysObj.GenesysGenWcvfxBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fxstate__colour_cube_settings":
                self.data = AnyGenesysObj.GenesysGenPostFxstateColourCubeSettings(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__world__in_air_player":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesWorldInAirPlayer(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_info__battling_effect__extra_roll_params":
                self.data = AnyGenesysObj.GenesysGenCollisionInfoBattlingEffectExtraRollParams(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_vfx_behaviour__front_rear_params__skid_mark_params":
                self.data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsSkidMarkParams(self._io, self, self._root)
            elif _on == u"genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour":
                self.data = AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__game_pack":
                self.data = AnyGenesysObj.GenesysGenGamePack(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle__driver_setup__seat_belt_bone_offset":
                self.data = AnyGenesysObj.GenesysGenVehicleDriverSetupSeatBeltBoneOffset(self._io, self, self._root)
            elif _on == u"genesys__gen__engine__transmission":
                self.data = AnyGenesysObj.GenesysGenEngineTransmission(self._io, self, self._root)
            elif _on == u"genesys__gen__performance_modification_item":
                self.data = AnyGenesysObj.GenesysGenPerformanceModificationItem(self._io, self, self._root)
            elif _on == u"genesys__gen__engine__differentials":
                self.data = AnyGenesysObj.GenesysGenEngineDifferentials(self._io, self, self._root)
            elif _on == u"genesys__gen__donut_ability__donut_grip_values":
                self.data = AnyGenesysObj.GenesysGenDonutAbilityDonutGripValues(self._io, self, self._root)
            elif _on == u"genesys__gen__sub_harmoniser_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenSubHarmoniserDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external_globals":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalGlobals(self._io, self, self._root)
            elif _on == u"genesys__gen__suspension_wheel":
                self.data = AnyGenesysObj.GenesysGenSuspensionWheel(self._io, self, self._root)
            elif _on == u"genesys__gen__steering_behaviour":
                self.data = AnyGenesysObj.GenesysGenSteeringBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__race_car_vs_dynamic__basic_params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarRaceCarVsDynamicBasicParams(self._io, self, self._root)
            elif _on == u"genesys__gen__wheel_damage":
                self.data = AnyGenesysObj.GenesysGenWheelDamage(self._io, self, self._root)
            elif _on == u"genesys__gen__engine_sound2":
                self.data = AnyGenesysObj.GenesysGenEngineSound2(self._io, self, self._root)
            elif _on == u"genesys__gen__behaviour":
                self.data = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge__online_challenge":
                self.data = AnyGenesysObj.GenesysGenChallengeOnlineChallenge(self._io, self, self._root)
            elif _on == u"genesys__gen__aerodynamic_behaviour":
                self.data = AnyGenesysObj.GenesysGenAerodynamicBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle__gameplay__tyre_trails":
                self.data = AnyGenesysObj.GenesysGenVehicleGameplayTyreTrails(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fxstate":
                self.data = AnyGenesysObj.GenesysGenPostFxstate(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__high_speed":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersHighSpeed(self._io, self, self._root)
            elif _on == u"genesys__gen__game_mode":
                self.data = AnyGenesysObj.GenesysGenGameMode(self._io, self, self._root)
            elif _on == u"genesys__gen__corona__flare":
                self.data = AnyGenesysObj.GenesysGenCoronaFlare(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__traffic_oncoming":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersTrafficOncoming(self._io, self, self._root)
            elif _on == u"genesys__gen__ginsu_sequence_item__fade":
                self.data = AnyGenesysObj.GenesysGenGinsuSequenceItemFade(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_vfx_behaviour__corona":
                self.data = AnyGenesysObj.GenesysGenVehicleVfxBehaviourCorona(self._io, self, self._root)
            elif _on == u"genesys__gen__chevron":
                self.data = AnyGenesysObj.GenesysGenChevron(self._io, self, self._root)
            elif _on == u"genesys__gen__sequence":
                self.data = AnyGenesysObj.GenesysGenSequence(self._io, self, self._root)
            elif _on == u"genesys__gen__physics__crashing_rules__impact_rules__damage_to_deal":
                self.data = AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRulesDamageToDeal(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_vfx_behaviour__smoke_params":
                self.data = AnyGenesysObj.GenesysGenTyreVfxBehaviourSmokeParams(self._io, self, self._root)
            elif _on == u"genesys__gen__drift_behaviour__drift_trigger":
                self.data = AnyGenesysObj.GenesysGenDriftBehaviourDriftTrigger(self._io, self, self._root)
            elif _on == u"genesys__gen__mixer_channel_sequence_item":
                self.data = AnyGenesysObj.GenesysGenMixerChannelSequenceItem(self._io, self, self._root)
            elif _on == u"rw_math_vpu__vector4":
                self.data = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
            elif _on == u"int8_t":
                self.data = AnyGenesysObj.Int8T(self._io, self, self._root)
            elif _on == u"genesys__gen__offline_event__aiplayer_information":
                self.data = AnyGenesysObj.GenesysGenOfflineEventAiplayerInformation(self._io, self, self._root)
            elif _on == u"genesys__gen__road_block_layer":
                self.data = AnyGenesysObj.GenesysGenRoadBlockLayer(self._io, self, self._root)
            elif _on == u"genesys__gen__engine_sound2__gain_param":
                self.data = AnyGenesysObj.GenesysGenEngineSound2GainParam(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__player_vs_ai__basic_params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiBasicParams(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_paint__structure2":
                self.data = AnyGenesysObj.GenesysGenVehiclePaintStructure2(self._io, self, self._root)
            elif _on == u"genesys__gen__sequence_items__post_fx_override_sequence_item":
                self.data = AnyGenesysObj.GenesysGenSequenceItemsPostFxOverrideSequenceItem(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay_trigger__aiplayer_information":
                self.data = AnyGenesysObj.GenesysGenGameplayTriggerAiplayerInformation(self._io, self, self._root)
            elif _on == u"genesys__gen__body_movement_behaviour__take_off_behaviour":
                self.data = AnyGenesysObj.GenesysGenBodyMovementBehaviourTakeOffBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__world__crashed_player__constraint_data":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesWorldCrashedPlayerConstraintData(self._io, self, self._root)
            elif _on == u"genesys__gen__nucleus_entitlement_tags":
                self.data = AnyGenesysObj.GenesysGenNucleusEntitlementTags(self._io, self, self._root)
            elif _on == u"genesys__gen__wcplay_sound_behaviour__prop_surface_sound":
                self.data = AnyGenesysObj.GenesysGenWcplaySoundBehaviourPropSurfaceSound(self._io, self, self._root)
            elif _on == u"cgs_core__string_base":
                self.data = AnyGenesysObj.CgsCoreStringBase(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition__physical_definition":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinition(self._io, self, self._root)
            elif _on == u"genesys__gen__traffic_flow_type__traffic_flow_type":
                self.data = AnyGenesysObj.GenesysGenTrafficFlowTypeTrafficFlowType(self._io, self, self._root)
            elif _on == u"genesys__gen__engine__mix":
                self.data = AnyGenesysObj.GenesysGenEngineMix(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay_trigger__output":
                self.data = AnyGenesysObj.GenesysGenGameplayTriggerOutput(self._io, self, self._root)
            elif _on == u"genesys__gen__vehicle_vfx_behaviour__light":
                self.data = AnyGenesysObj.GenesysGenVehicleVfxBehaviourLight(self._io, self, self._root)
            elif _on == u"genesys__gen__bus_mixer_channel_sequence_item__bus_mixer_channel_double_value":
                self.data = AnyGenesysObj.GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue(self._io, self, self._root)
            elif _on == u"genesys__gen__physical_definition__rigid_body__box_volume":
                self.data = AnyGenesysObj.GenesysGenPhysicalDefinitionRigidBodyBoxVolume(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__catching_air":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersCatchingAir(self._io, self, self._root)
            elif _on == u"genesys__gen__car_select_data":
                self.data = AnyGenesysObj.GenesysGenCarSelectData(self._io, self, self._root)
            elif _on == u"uint8_t":
                self.data = AnyGenesysObj.Uint8T(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_effects__traffic_effect":
                self.data = AnyGenesysObj.GenesysGenCollisionEffectsTrafficEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__event_arena_data__spawn_point_collection":
                self.data = AnyGenesysObj.GenesysGenEventArenaDataSpawnPointCollection(self._io, self, self._root)
            elif _on == u"genesys__gen__physics__damage_bar_profile__segment":
                self.data = AnyGenesysObj.GenesysGenPhysicsDamageBarProfileSegment(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_strength__punch":
                self.data = AnyGenesysObj.GenesysGenNitrousStrengthPunch(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__min_speed":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersMinSpeed(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fx_keyframe__stereo_3d":
                self.data = AnyGenesysObj.GenesysGenPostFxKeyframeStereo3d(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external__deceleration__pitch__change":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalDecelerationPitchChange(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__global__traffic_vs_traffic":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalTrafficVsTraffic(self._io, self, self._root)
            elif _on == u"genesys__gen__dsp_plug_in_chain":
                self.data = AnyGenesysObj.GenesysGenDspPlugInChain(self._io, self, self._root)
            elif _on == u"genesys__gen__physics__landing_damage__roll":
                self.data = AnyGenesysObj.GenesysGenPhysicsLandingDamageRoll(self._io, self, self._root)
            elif _on == u"genesys__gen__nitrous_parameters__balancing":
                self.data = AnyGenesysObj.GenesysGenNitrousParametersBalancing(self._io, self, self._root)
            elif _on == u"genesys__gen__peaking_dsp_plug_in":
                self.data = AnyGenesysObj.GenesysGenPeakingDspPlugIn(self._io, self, self._root)
            elif _on == u"genesys__gen__car_select_data__sequences":
                self.data = AnyGenesysObj.GenesysGenCarSelectDataSequences(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_info__world_damage":
                self.data = AnyGenesysObj.GenesysGenCollisionInfoWorldDamage(self._io, self, self._root)
            elif _on == u"genesys__gen__wheel_suspension_spring_constraint":
                self.data = AnyGenesysObj.GenesysGenWheelSuspensionSpringConstraint(self._io, self, self._root)
            elif _on == u"genesys__gen__performance_modifier":
                self.data = AnyGenesysObj.GenesysGenPerformanceModifier(self._io, self, self._root)
            elif _on == u"genesys__gen__wcplay_sound_behaviour":
                self.data = AnyGenesysObj.GenesysGenWcplaySoundBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__aivs_crashing_race_car__params":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsCrashingRaceCarParams(self._io, self, self._root)
            elif _on == u"genesys__gen__race_balancing_profile":
                self.data = AnyGenesysObj.GenesysGenRaceBalancingProfile(self._io, self, self._root)
            elif _on == u"genesys__gen__post_fx_keyframe__bloom":
                self.data = AnyGenesysObj.GenesysGenPostFxKeyframeBloom(self._io, self, self._root)
            elif _on == u"genesys__gen__bus_mixer_channel_sequence_item":
                self.data = AnyGenesysObj.GenesysGenBusMixerChannelSequenceItem(self._io, self, self._root)
            elif _on == u"genesys__gen__car_swap_spot":
                self.data = AnyGenesysObj.GenesysGenCarSwapSpot(self._io, self, self._root)
            elif _on == u"genesys__gen__sequence_item__modulating_double_value":
                self.data = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
            elif _on == u"genesys__gen__compound_additional_info":
                self.data = AnyGenesysObj.GenesysGenCompoundAdditionalInfo(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__global__dynamic_vs_dynamic":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalDynamicVsDynamic(self._io, self, self._root)
            elif _on == u"genesys__gen__physics__landing_damage__pitch":
                self.data = AnyGenesysObj.GenesysGenPhysicsLandingDamagePitch(self._io, self, self._root)
            elif _on == u"uint32_t":
                self.data = AnyGenesysObj.Uint32T(self._io, self, self._root)
            elif _on == u"genesys__gen__lfo_sequence_item":
                self.data = AnyGenesysObj.GenesysGenLfoSequenceItem(self._io, self, self._root)
            elif _on == u"genesys__gen__challenge_action__accumulate_time":
                self.data = AnyGenesysObj.GenesysGenChallengeActionAccumulateTime(self._io, self, self._root)
            elif _on == u"genesys__gen__heat_level__behaviour_coordination__pursuit_behaviour__cop_behaviour":
                self.data = AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_vfx_behaviour__skid_mark_params":
                self.data = AnyGenesysObj.GenesysGenTyreVfxBehaviourSkidMarkParams(self._io, self, self._root)
            elif _on == u"genesys__gen__vfx_locator_group_vehicle_spot_effect_sequence_item":
                self.data = AnyGenesysObj.GenesysGenVfxLocatorGroupVehicleSpotEffectSequenceItem(self._io, self, self._root)
            elif _on == u"genesys__gen__gameplay__condition":
                self.data = AnyGenesysObj.GenesysGenGameplayCondition(self._io, self, self._root)
            elif _on == u"genesys__gen__hard_driving_behaviour__gas_effect":
                self.data = AnyGenesysObj.GenesysGenHardDrivingBehaviourGasEffect(self._io, self, self._root)
            elif _on == u"genesys__gen__light__projected_texture":
                self.data = AnyGenesysObj.GenesysGenLightProjectedTexture(self._io, self, self._root)
            elif _on == u"genesys__gen__camera_gameplay_external__camera__roll":
                self.data = AnyGenesysObj.GenesysGenCameraGameplayExternalCameraRoll(self._io, self, self._root)
            elif _on == u"genesys__gen__engine__mixer__channel__gain__modification":
                self.data = AnyGenesysObj.GenesysGenEngineMixerChannelGainModification(self._io, self, self._root)
            elif _on == u"genesys__gen__handling_behaviour":
                self.data = AnyGenesysObj.GenesysGenHandlingBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__collision_responses__race_car__player_vs_crashing_race_car":
                self.data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCar(self._io, self, self._root)
            elif _on == u"genesys__gen__wcremove_world_entity_behaviour":
                self.data = AnyGenesysObj.GenesysGenWcremoveWorldEntityBehaviour(self._io, self, self._root)
            elif _on == u"genesys__gen__race_car_physical_definition":
                self.data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinition(self._io, self, self._root)
            elif _on == u"genesys__gen__tyre_sound_params__lat_slip":
                self.data = AnyGenesysObj.GenesysGenTyreSoundParamsLatSlip(self._io, self, self._root)
            else:
                self.data = AnyGenesysObj.Dummy(self._io, self, self._root)


    class GenesysGenVehicleDamageBehaviourDamageSequence(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_object = AnyGenesysObj.GenObj(self._io, self, self._root)
            self.cgs_resource__handle_0xc = self._io.read_bytes(8)
            self.game_changer_id_0x14 = self._io.read_u4le()

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 28
            return getattr(self, '_m_size', None)

        @property
        def mu_version_hash(self):
            if hasattr(self, '_m_mu_version_hash'):
                return self._m_mu_version_hash

            self._m_mu_version_hash = 1109621193
            return getattr(self, '_m_mu_version_hash', None)


    @property
    def ofs(self):
        if hasattr(self, '_m_ofs'):
            return self._m_ofs

        self._m_ofs = self._io.pos()
        return getattr(self, '_m_ofs', None)

    @property
    def data(self):
        if hasattr(self, '_m_data'):
            return self._m_data

        _pos = self._io.pos()
        self._io.seek(self.ofs)
        _on = self.obj.mu_type_version
        if _on == 2847735672:
            self._m_data = AnyGenesysObj.GenesysGenEngineNormalQualityEngine(self._io, self, self._root)
        elif _on == 738476701:
            self._m_data = AnyGenesysObj.GenesysGenGameUnlockList(self._io, self, self._root)
        elif _on == 669436076:
            self._m_data = AnyGenesysObj.GenesysGenVehiclePaint(self._io, self, self._root)
        elif _on == 1202023644:
            self._m_data = AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRules(self._io, self, self._root)
        elif _on == 3375675327:
            self._m_data = AnyGenesysObj.GenesysGenCoronaBeam(self._io, self, self._root)
        elif _on == 21856074:
            self._m_data = AnyGenesysObj.GenesysGenTyre(self._io, self, self._root)
        elif _on == 3231281576:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionHitTrigger(self._io, self, self._root)
        elif _on == 2099267897:
            self._m_data = AnyGenesysObj.GenesysGenDamageBarProfilesProfile(self._io, self, self._root)
        elif _on == 1763676845:
            self._m_data = AnyGenesysObj.GenesysGenCollisionEffects(self._io, self, self._root)
        elif _on == 1316353574:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinition(self._io, self, self._root)
        elif _on == 1106192363:
            self._m_data = AnyGenesysObj.GenesysGenOnlineLicensePlate(self._io, self, self._root)
        elif _on == 1279163701:
            self._m_data = AnyGenesysObj.GenesysGenSuspensionWheel(self._io, self, self._root)
        elif _on == 682066218:
            self._m_data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParams(self._io, self, self._root)
        elif _on == 2949464142:
            self._m_data = AnyGenesysObj.GenesysGenTrafficFlow(self._io, self, self._root)
        elif _on == 1880813572:
            self._m_data = AnyGenesysObj.GenesysGenVehicleDamageBehaviour(self._io, self, self._root)
        elif _on == 2262242598:
            self._m_data = AnyGenesysObj.GenesysGenGameplayBlacklistShutdownData(self._io, self, self._root)
        elif _on == 2121274978:
            self._m_data = AnyGenesysObj.GenesysGenChallengeOnlineChallenge(self._io, self, self._root)
        elif _on == 4084465158:
            self._m_data = AnyGenesysObj.GenesysGenNitrousStrengthPunch(self._io, self, self._root)
        elif _on == 3881994110:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarRaceCarVsDynamicBasicParams(self._io, self, self._root)
        elif _on == 2956570466:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiDamageParams(self._io, self, self._root)
        elif _on == 1489464845:
            self._m_data = AnyGenesysObj.GenesysGenSequenceItemModulatingDoubleValue(self._io, self, self._root)
        elif _on == 1913150235:
            self._m_data = AnyGenesysObj.GenesysGenPaintPackGroup(self._io, self, self._root)
        elif _on == 368598916:
            self._m_data = AnyGenesysObj.GenesysGenTyresTyres(self._io, self, self._root)
        elif _on == 1329740588:
            self._m_data = AnyGenesysObj.GenesysGenSteeringWheelPhysics(self._io, self, self._root)
        elif _on == 618870438:
            self._m_data = AnyGenesysObj.GenesysGenVehiclesSoundTransmissionWhine(self._io, self, self._root)
        elif _on == 524753351:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCar(self._io, self, self._root)
        elif _on == 1687823060:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersTakingShortcut(self._io, self, self._root)
        elif _on == 1883284107:
            self._m_data = AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordination(self._io, self, self._root)
        elif _on == 1668851487:
            self._m_data = AnyGenesysObj.GenesysGenCarSelectDataSequences(self._io, self, self._root)
        elif _on == 1667642657:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionDoJump(self._io, self, self._root)
        elif _on == 196190359:
            self._m_data = AnyGenesysObj.GenesysGenImpactDamageGraphs(self._io, self, self._root)
        elif _on == 3547832794:
            self._m_data = AnyGenesysObj.GenesysGenDriftBehaviourYawTorque(self._io, self, self._root)
        elif _on == 4242000614:
            self._m_data = AnyGenesysObj.GenesysGenOnlineDrivingTestListGroups(self._io, self, self._root)
        elif _on == 4274679117:
            self._m_data = AnyGenesysObj.GenesysGenDriftBehaviour(self._io, self, self._root)
        elif _on == 3641337381:
            self._m_data = AnyGenesysObj.GenesysGenEngineSound(self._io, self, self._root)
        elif _on == 1081328468:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersSlipstreaming(self._io, self, self._root)
        elif _on == 981367156:
            self._m_data = AnyGenesysObj.GenesysGenEventList(self._io, self, self._root)
        elif _on == 2252962025:
            self._m_data = AnyGenesysObj.GenesysGenBrakeBehaviour(self._io, self, self._root)
        elif _on == 3366752106:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionJumpStats(self._io, self, self._root)
        elif _on == 3826155101:
            self._m_data = AnyGenesysObj.GenesysGenDspPlugInChain(self._io, self, self._root)
        elif _on == 451352474:
            self._m_data = AnyGenesysObj.GenesysGenThankyouMapping(self._io, self, self._root)
        elif _on == 3989427985:
            self._m_data = AnyGenesysObj.GenesysGenLightCone(self._io, self, self._root)
        elif _on == 3089457678:
            self._m_data = AnyGenesysObj.GenesysGenEvent(self._io, self, self._root)
        elif _on == 3054130878:
            self._m_data = AnyGenesysObj.GenesysGenTyreSoundParams(self._io, self, self._root)
        elif _on == 724902868:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarHandlingDisruptionEffect(self._io, self, self._root)
        elif _on == 1836975283:
            self._m_data = AnyGenesysObj.GenesysGenRollout(self._io, self, self._root)
        elif _on == 2560361681:
            self._m_data = AnyGenesysObj.GenesysGenEntitlement(self._io, self, self._root)
        elif _on == 2076212613:
            self._m_data = AnyGenesysObj.GenesysGenWheelSuspensionConstraint(self._io, self, self._root)
        elif _on == 3584499810:
            self._m_data = AnyGenesysObj.GenesysGenVehicleDriverSetup(self._io, self, self._root)
        elif _on == 3616318101:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionSpeedRun(self._io, self, self._root)
        elif _on == 3014928914:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionGetToLocation(self._io, self, self._root)
        elif _on == 3635654829:
            self._m_data = AnyGenesysObj.GenesysGenPhysicsLandingDamageRoll(self._io, self, self._root)
        elif _on == 709116355:
            self._m_data = AnyGenesysObj.GenesysGenEngineDifferentials(self._io, self, self._root)
        elif _on == 2321043106:
            self._m_data = AnyGenesysObj.GenesysGenWheelSizes(self._io, self, self._root)
        elif _on == 259534121:
            self._m_data = AnyGenesysObj.GenesysGenCameraRearViewGlobals(self._io, self, self._root)
        elif _on == 481138910:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAiBasicParams(self._io, self, self._root)
        elif _on == 231346471:
            self._m_data = AnyGenesysObj.GenesysGenGinsuDspPlugIn(self._io, self, self._root)
        elif _on == 1694754426:
            self._m_data = AnyGenesysObj.GenesysGenRoadBlockLayer(self._io, self, self._root)
        elif _on == 174067018:
            self._m_data = AnyGenesysObj.GenesysGenEngineSound2DspParam(self._io, self, self._root)
        elif _on == 1217853836:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesGlobal(self._io, self, self._root)
        elif _on == 1231510099:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCarCrashedParams(self._io, self, self._root)
        elif _on == 1080225187:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesWorld(self._io, self, self._root)
        elif _on == 542430507:
            self._m_data = AnyGenesysObj.GenesysGenDamageBarProfilesProfileSegmentData(self._io, self, self._root)
        elif _on == 3626200052:
            self._m_data = AnyGenesysObj.GenesysGenBusMixerChannelSequenceItemBusMixerChannelDoubleValue(self._io, self, self._root)
        elif _on == 520558439:
            self._m_data = AnyGenesysObj.GenesysGenVehicleGameplay(self._io, self, self._root)
        elif _on == 123660642:
            self._m_data = AnyGenesysObj.GenesysGenVehicleVfxBehaviourLight(self._io, self, self._root)
        elif _on == 2600311769:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersHighSpeed(self._io, self, self._root)
        elif _on == 1963215010:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalSpeedBasedMovement(self._io, self, self._root)
        elif _on == 793749252:
            self._m_data = AnyGenesysObj.GenesysGenGamePack(self._io, self, self._root)
        elif _on == 3992764498:
            self._m_data = AnyGenesysObj.GenesysGenGameplayAllowedVehicleList(self._io, self, self._root)
        elif _on == 983393262:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayBumper(self._io, self, self._root)
        elif _on == 2353212897:
            self._m_data = AnyGenesysObj.GenesysGenTrafficFlowTypeTrafficFlowType(self._io, self, self._root)
        elif _on == 2361784635:
            self._m_data = AnyGenesysObj.GenesysGenEngineMixerChannelGainModification(self._io, self, self._root)
        elif _on == 2169939698:
            self._m_data = AnyGenesysObj.GenesysGenVehicleVfxBehaviourSpotEffect(self._io, self, self._root)
        elif _on == 4000215473:
            self._m_data = AnyGenesysObj.GenesysGenLowPassButterworthDspPlugIn(self._io, self, self._root)
        elif _on == 1186319577:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalCrashingRaceCarVsCrashingRaceCar(self._io, self, self._root)
        elif _on == 3274903722:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayBonnetWindSound(self._io, self, self._root)
        elif _on == 115778840:
            self._m_data = AnyGenesysObj.GenesysGenJumpTimelineController(self._io, self, self._root)
        elif _on == 2626118372:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalCrashingRaceCarVsTraffic(self._io, self, self._root)
        elif _on == 1912243431:
            self._m_data = AnyGenesysObj.GenesysGenPhysicsCrashingRules(self._io, self, self._root)
        elif _on == 2825220545:
            self._m_data = AnyGenesysObj.GenesysGenCollisionEffectsWorldEffect(self._io, self, self._root)
        elif _on == 394812715:
            self._m_data = AnyGenesysObj.GenesysGenSendDspPlugIn(self._io, self, self._root)
        elif _on == 1685430085:
            self._m_data = AnyGenesysObj.GenesysGenHardDrivingBehaviourSteeringEffect(self._io, self, self._root)
        elif _on == 3948195379:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionActionBase(self._io, self, self._root)
        elif _on == 3823531688:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionSpeedCameraAction(self._io, self, self._root)
        elif _on == 3469692361:
            self._m_data = AnyGenesysObj.GenesysGenSafehouse(self._io, self, self._root)
        elif _on == 3071320584:
            self._m_data = AnyGenesysObj.GenesysGenStorePack(self._io, self, self._root)
        elif _on == 80463996:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersNitrousUsage(self._io, self, self._root)
        elif _on == 306714612:
            self._m_data = AnyGenesysObj.GenesysGenLightBaseFlashPattern(self._io, self, self._root)
        elif _on == 2477895213:
            self._m_data = AnyGenesysObj.GenesysGenEngineSound2DspParamWrapper(self._io, self, self._root)
        elif _on == 4032173314:
            self._m_data = AnyGenesysObj.GenesysGenPostFxsequenceItem(self._io, self, self._root)
        elif _on == 3479966800:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersPunchUsage(self._io, self, self._root)
        elif _on == 2169124928:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficDamageParams(self._io, self, self._root)
        elif _on == 1901399892:
            self._m_data = AnyGenesysObj.GenesysGenEngineMix(self._io, self, self._root)
        elif _on == 3652314633:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectRotationAxisParams(self._io, self, self._root)
        elif _on == 1483915852:
            self._m_data = AnyGenesysObj.GenesysGenPhysicsCrashingRulesImpactRulesDamageToDeal(self._io, self, self._root)
        elif _on == 615742248:
            self._m_data = AnyGenesysObj.GenesysGenPostFxstate(self._io, self, self._root)
        elif _on == 3907892408:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalDynamicVsDynamic(self._io, self, self._root)
        elif _on == 3829466250:
            self._m_data = AnyGenesysObj.GenesysGenEngineTransmission(self._io, self, self._root)
        elif _on == 4090590688:
            self._m_data = AnyGenesysObj.GenesysGenEventArenaDataSpawnPointCollection(self._io, self, self._root)
        elif _on == 1273350923:
            self._m_data = AnyGenesysObj.GenesysGenRaceBalancingDataOpponentBalancingData(self._io, self, self._root)
        elif _on == 4102322433:
            self._m_data = AnyGenesysObj.GenesysGenEventArena(self._io, self, self._root)
        elif _on == 3530258211:
            self._m_data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsSkidMarkParams(self._io, self, self._root)
        elif _on == 3396244228:
            self._m_data = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffectExtraRollParams(self._io, self, self._root)
        elif _on == 3178679735:
            self._m_data = AnyGenesysObj.GenesysGenHeatLevelSoundSetNitrous(self._io, self, self._root)
        elif _on == 3023685899:
            self._m_data = AnyGenesysObj.GenesysGenBodyMovementBehaviourAngleControl(self._io, self, self._root)
        elif _on == 509958626:
            self._m_data = AnyGenesysObj.GenesysGenVehicleDamageBehaviourBodypart(self._io, self, self._root)
        elif _on == 1324301512:
            self._m_data = AnyGenesysObj.GenesysGenPostFxKeyframeStereo3d(self._io, self, self._root)
        elif _on == 3179911126:
            self._m_data = AnyGenesysObj.GenesysGenGeneralTriggerSequenceItem(self._io, self, self._root)
        elif _on == 4085824509:
            self._m_data = AnyGenesysObj.GenesysGenPostFxKeyframeGeneral(self._io, self, self._root)
        elif _on == 3791727622:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalSpeedBasedMovementHighSpeedShake(self._io, self, self._root)
        elif _on == 542473885:
            self._m_data = AnyGenesysObj.GenesysGenOfflineEventCustomChevrons(self._io, self, self._root)
        elif _on == 3263786457:
            self._m_data = AnyGenesysObj.GenesysGenPeakingDspPlugIn(self._io, self, self._root)
        elif _on == 935932605:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersJumpUsage(self._io, self, self._root)
        elif _on == 3959582479:
            self._m_data = AnyGenesysObj.GenesysGenCompoundAdditionalInfo(self._io, self, self._root)
        elif _on == 1555583970:
            self._m_data = AnyGenesysObj.GenesysGenPerformanceModificationItem(self._io, self, self._root)
        elif _on == 3229542978:
            self._m_data = AnyGenesysObj.GenesysGenWcvfxBehaviourLights(self._io, self, self._root)
        elif _on == 2921338515:
            self._m_data = AnyGenesysObj.GenesysGenGameplayMilestoneEntry(self._io, self, self._root)
        elif _on == 866205257:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectTranslation(self._io, self, self._root)
        elif _on == 4164557270:
            self._m_data = AnyGenesysObj.GenesysGenDonutAbilityDonutGripValues(self._io, self, self._root)
        elif _on == 1320933699:
            self._m_data = AnyGenesysObj.GenesysGenGameplayMilestone(self._io, self, self._root)
        elif _on == 18021398:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyCylinderVolume(self._io, self, self._root)
        elif _on == 1109621193:
            self._m_data = AnyGenesysObj.GenesysGenVehicleDamageBehaviourDamageSequence(self._io, self, self._root)
        elif _on == 2473868341:
            self._m_data = AnyGenesysObj.GenesysGenSndPlayerDspPlugIn(self._io, self, self._root)
        elif _on == 564124160:
            self._m_data = AnyGenesysObj.GenesysGenTyreSoundParamsLateral(self._io, self, self._root)
        elif _on == 2607248643:
            self._m_data = AnyGenesysObj.GenesysGenPhysicsLandingDamage(self._io, self, self._root)
        elif _on == 1325791513:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesWorldCrashedPlayer(self._io, self, self._root)
        elif _on == 2419838023:
            self._m_data = AnyGenesysObj.GenesysGenOfflineEvent(self._io, self, self._root)
        elif _on == 4260207896:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesWorldPlayer(self._io, self, self._root)
        elif _on == 1951683017:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficBasicParams(self._io, self, self._root)
        elif _on == 1294158455:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionActionBaseFeedbackData(self._io, self, self._root)
        elif _on == 2656703430:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersHittingAnotherCompetitor(self._io, self, self._root)
        elif _on == 4263309034:
            self._m_data = AnyGenesysObj.GenesysGenNucleusGrantMappingsListMapping(self._io, self, self._root)
        elif _on == 1655947362:
            self._m_data = AnyGenesysObj.GenesysGenVoiceGroup(self._io, self, self._root)
        elif _on == 1408090920:
            self._m_data = AnyGenesysObj.GenesysGenHandbrakeAbilityHandbrakeGripValues(self._io, self, self._root)
        elif _on == 4159289097:
            self._m_data = AnyGenesysObj.GenesysGenTyreVfxBehaviourSkidMarkParams(self._io, self, self._root)
        elif _on == 3131401224:
            self._m_data = AnyGenesysObj.GenesysGenNucleusEntitlementTags(self._io, self, self._root)
        elif _on == 1664340785:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyConvexHullVolume(self._io, self, self._root)
        elif _on == 1886238258:
            self._m_data = AnyGenesysObj.GenesysGenCollisionInfoBattlingEffect(self._io, self, self._root)
        elif _on == 3664056692:
            self._m_data = AnyGenesysObj.GenesysGenSequenceItemsPostFxOverrideSequenceItem(self._io, self, self._root)
        elif _on == 2776745689:
            self._m_data = AnyGenesysObj.GenesysGenRaceBalancingProfile(self._io, self, self._root)
        elif _on == 4093540154:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionAccumulationHelperData(self._io, self, self._root)
        elif _on == 1852100653:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarEffectSequenceItemEffectDoubleValue(self._io, self, self._root)
        elif _on == 3115085927:
            self._m_data = AnyGenesysObj.GenesysGenWcplaySoundBehaviourPropSurfaceSound(self._io, self, self._root)
        elif _on == 1558321222:
            self._m_data = AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviour(self._io, self, self._root)
        elif _on == 2041922261:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalAccelerationMovement(self._io, self, self._root)
        elif _on == 1015007408:
            self._m_data = AnyGenesysObj.GenesysGenDonutAbilityDonutScale(self._io, self, self._root)
        elif _on == 1543118382:
            self._m_data = AnyGenesysObj.GenesysGenGameplayBlacklistShutdownDataDamageThresholdSpeedControl(self._io, self, self._root)
        elif _on == 3106899705:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarBasicParams(self._io, self, self._root)
        elif _on == 1476111906:
            self._m_data = AnyGenesysObj.GenesysGenVehicleDamageBehaviourBodypartDamageThreshold(self._io, self, self._root)
        elif _on == 3996354190:
            self._m_data = AnyGenesysObj.GenesysGenCloudCompeteAward(self._io, self, self._root)
        elif _on == 1901216409:
            self._m_data = AnyGenesysObj.GenesysGenGameplayCondition(self._io, self, self._root)
        elif _on == 1377850816:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersRestrictions(self._io, self, self._root)
        elif _on == 835914245:
            self._m_data = AnyGenesysObj.GenesysGenGameplayTriggerOutput(self._io, self, self._root)
        elif _on == 4074208643:
            self._m_data = AnyGenesysObj.GenesysGenTyreVfxBehaviour(self._io, self, self._root)
        elif _on == 1781716212:
            self._m_data = AnyGenesysObj.GenesysGenScoringActionOnlineScoringFeedback(self._io, self, self._root)
        elif _on == 834676531:
            self._m_data = AnyGenesysObj.GenesysGenEngine(self._io, self, self._root)
        elif _on == 1356872704:
            self._m_data = AnyGenesysObj.GenesysGenDspPlugIn(self._io, self, self._root)
        elif _on == 1055028229:
            self._m_data = AnyGenesysObj.GenesysGenWcremoveWorldEntityBehaviour(self._io, self, self._root)
        elif _on == 1967128889:
            self._m_data = AnyGenesysObj.GenesysGenMixerChannelSequenceItemMixerChannelDoubleValue(self._io, self, self._root)
        elif _on == 86537152:
            self._m_data = AnyGenesysObj.GenesysGenVehicleCameraContainer(self._io, self, self._root)
        elif _on == 3359156872:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCar(self._io, self, self._root)
        elif _on == 3055337662:
            self._m_data = AnyGenesysObj.GenesysGenRaceBalancingData(self._io, self, self._root)
        elif _on == 3148721321:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternal(self._io, self, self._root)
        elif _on == 3542932618:
            self._m_data = AnyGenesysObj.GenesysGenVehicleDriverSetupSeatBeltBoneOffset(self._io, self, self._root)
        elif _on == 975568910:
            self._m_data = AnyGenesysObj.GenesysGenNucleusGrantMappingsList(self._io, self, self._root)
        elif _on == 773308239:
            self._m_data = AnyGenesysObj.GenesysGenGinsuSequenceItem(self._io, self, self._root)
        elif _on == 2612185096:
            self._m_data = AnyGenesysObj.GenesysGenSteeringBehaviour(self._io, self, self._root)
        elif _on == 2631887699:
            self._m_data = AnyGenesysObj.GenesysGenScoringAction(self._io, self, self._root)
        elif _on == 1082129393:
            self._m_data = AnyGenesysObj.GenesysGenVehiclePaintStructure2(self._io, self, self._root)
        elif _on == 1387924581:
            self._m_data = AnyGenesysObj.GenesysGenSuspension(self._io, self, self._root)
        elif _on == 3415849662:
            self._m_data = AnyGenesysObj.GenesysGenVehicleComponent(self._io, self, self._root)
        elif _on == 3815813836:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionAccumulateDistance(self._io, self, self._root)
        elif _on == 1611423524:
            self._m_data = AnyGenesysObj.GenesysGenCarSwapSpot(self._io, self, self._root)
        elif _on == 2144572099:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTrafficBasicParams(self._io, self, self._root)
        elif _on == 944731751:
            self._m_data = AnyGenesysObj.GenesysGenChallengeLocation(self._io, self, self._root)
        elif _on == 2784884141:
            self._m_data = AnyGenesysObj.GenesysGenVehiclesTyreUpgrade(self._io, self, self._root)
        elif _on == 3789082911:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersMinSpeed(self._io, self, self._root)
        elif _on == 2504213501:
            self._m_data = AnyGenesysObj.GenesysGenWheelDamage(self._io, self, self._root)
        elif _on == 3768680712:
            self._m_data = AnyGenesysObj.GenesysGenOnlineChallenge(self._io, self, self._root)
        elif _on == 1722819130:
            self._m_data = AnyGenesysObj.GenesysGenWaveSequenceItem(self._io, self, self._root)
        elif _on == 1110789791:
            self._m_data = AnyGenesysObj.GenesysGenHighPassButterworthDspPlugIn(self._io, self, self._root)
        elif _on == 1278315440:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesWorldPlayerFlipState(self._io, self, self._root)
        elif _on == 4097165157:
            self._m_data = AnyGenesysObj.GenesysGenLfoSequenceItemLfoDoubleValue(self._io, self, self._root)
        elif _on == 484081367:
            self._m_data = AnyGenesysObj.GenesysGenTyreLongSlipFactors(self._io, self, self._root)
        elif _on == 3256016364:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCar(self._io, self, self._root)
        elif _on == 1394693111:
            self._m_data = AnyGenesysObj.GenesysGenDonutAbility(self._io, self, self._root)
        elif _on == 3085449154:
            self._m_data = AnyGenesysObj.GenesysGenSmashProxyBehaviour(self._io, self, self._root)
        elif _on == 802364842:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalDecelerationPitchChange(self._io, self, self._root)
        elif _on == 2081469541:
            self._m_data = AnyGenesysObj.GenesysGenTyreSoundParamsLongSpin(self._io, self, self._root)
        elif _on == 732433969:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionAccumulateNearMisses(self._io, self, self._root)
        elif _on == 2957925672:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsCrashingRaceCarParams(self._io, self, self._root)
        elif _on == 591869524:
            self._m_data = AnyGenesysObj.GenesysGenSoundDistanceFalloff(self._io, self, self._root)
        elif _on == 4100294056:
            self._m_data = AnyGenesysObj.GenesysGenVehicleGameplayTyreTrails(self._io, self, self._root)
        elif _on == 160896465:
            self._m_data = AnyGenesysObj.GenesysGenBehaviour(self._io, self, self._root)
        elif _on == 2479955317:
            self._m_data = AnyGenesysObj.GenesysGenTyreLateralGripCurve(self._io, self, self._root)
        elif _on == 2066481913:
            self._m_data = AnyGenesysObj.GenesysGenCollisionEffectsTrafficEffect(self._io, self, self._root)
        elif _on == 855876020:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParameters(self._io, self, self._root)
        elif _on == 2583194568:
            self._m_data = AnyGenesysObj.GenesysGenVehicleComponentWheel(self._io, self, self._root)
        elif _on == 1711822367:
            self._m_data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsSmokeParams(self._io, self, self._root)
        elif _on == 606909642:
            self._m_data = AnyGenesysObj.GenesysGenScoreViewModelScoreData(self._io, self, self._root)
        elif _on == 166064775:
            self._m_data = AnyGenesysObj.GenesysGenTyreLateralSlipFactors(self._io, self, self._root)
        elif _on == 2808391399:
            self._m_data = AnyGenesysObj.GenesysGenRoadBlockLayerItem(self._io, self, self._root)
        elif _on == 3445640778:
            self._m_data = AnyGenesysObj.GenesysGenVehicleVfxBehaviourCorona(self._io, self, self._root)
        elif _on == 2706222886:
            self._m_data = AnyGenesysObj.GenesysGenMixerChannelSequenceItem(self._io, self, self._root)
        elif _on == 956776100:
            self._m_data = AnyGenesysObj.GenesysGenGameplayAllowedVehicleListVehicleAndMods(self._io, self, self._root)
        elif _on == 2331975734:
            self._m_data = AnyGenesysObj.GenesysGenCollisionInfoDamageProfile(self._io, self, self._root)
        elif _on == 3746299654:
            self._m_data = AnyGenesysObj.GenesysGenNitrousStrengthJump(self._io, self, self._root)
        elif _on == 1425943760:
            self._m_data = AnyGenesysObj.GenesysGenTyres(self._io, self, self._root)
        elif _on == 489513931:
            self._m_data = AnyGenesysObj.GenesysGenSubHarmoniserDspPlugIn(self._io, self, self._root)
        elif _on == 3800105053:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTraffic(self._io, self, self._root)
        elif _on == 1844756468:
            self._m_data = AnyGenesysObj.GenesysGenEngineSound2(self._io, self, self._root)
        elif _on == 2222283730:
            self._m_data = AnyGenesysObj.GenesysGenGameplayTriggerOutputSequenceOutput(self._io, self, self._root)
        elif _on == 2189872818:
            self._m_data = AnyGenesysObj.GenesysGenLightSpot(self._io, self, self._root)
        elif _on == 4182861931:
            self._m_data = AnyGenesysObj.GenesysGenOnlineDrivingTestListGroup(self._io, self, self._root)
        elif _on == 889829961:
            self._m_data = AnyGenesysObj.GenesysGenVehiclesUpgradeBase(self._io, self, self._root)
        elif _on == 3500617746:
            self._m_data = AnyGenesysObj.GenesysGenHardDrivingBehaviour(self._io, self, self._root)
        elif _on == 2063558262:
            self._m_data = AnyGenesysObj.GenesysGenRolloutWeaponData(self._io, self, self._root)
        elif _on == 3788863516:
            self._m_data = AnyGenesysObj.GenesysGenMakePhysicalBehaviour(self._io, self, self._root)
        elif _on == 860059237:
            self._m_data = AnyGenesysObj.GenesysGenTyreSoundParamsLatSlip(self._io, self, self._root)
        elif _on == 3190011655:
            self._m_data = AnyGenesysObj.GenesysGenTyreSoundParamsLongSpinBraking(self._io, self, self._root)
        elif _on == 3533118493:
            self._m_data = AnyGenesysObj.GenesysGenAiplayerType(self._io, self, self._root)
        elif _on == 1589286504:
            self._m_data = AnyGenesysObj.GenesysGenDriftBehaviourDriftTrigger(self._io, self, self._root)
        elif _on == 267183785:
            self._m_data = AnyGenesysObj.GenesysGenTimelineControllersRaceCarEntityTimelineController(self._io, self, self._root)
        elif _on == 1212586379:
            self._m_data = AnyGenesysObj.GenesysGenNucleusEntitlementTag(self._io, self, self._root)
        elif _on == 202861526:
            self._m_data = AnyGenesysObj.GenesysGenOnlineRoute(self._io, self, self._root)
        elif _on == 1807127390:
            self._m_data = AnyGenesysObj.GenesysGenCollisionEffectsTrafficEffectExtraRollParams(self._io, self, self._root)
        elif _on == 1234658497:
            self._m_data = AnyGenesysObj.GenesysGenCorona(self._io, self, self._root)
        elif _on == 2626560424:
            self._m_data = AnyGenesysObj.GenesysGenUilistItems(self._io, self, self._root)
        elif _on == 456164053:
            self._m_data = AnyGenesysObj.GenesysGenHeatLevelSoundSet(self._io, self, self._root)
        elif _on == 1198075180:
            self._m_data = AnyGenesysObj.GenesysGenBusMixerChannelSequenceItem(self._io, self, self._root)
        elif _on == 1530679421:
            self._m_data = AnyGenesysObj.GenesysGenTyresSurfaceEffects(self._io, self, self._root)
        elif _on == 4254634071:
            self._m_data = AnyGenesysObj.GenesysGenDriftBehaviourOther(self._io, self, self._root)
        elif _on == 2078321761:
            self._m_data = AnyGenesysObj.GenesysGenOnlineChallengeTarget(self._io, self, self._root)
        elif _on == 101265141:
            self._m_data = AnyGenesysObj.GenesysGenUilistItemsItem(self._io, self, self._root)
        elif _on == 3508674618:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalCameraRoll(self._io, self, self._root)
        elif _on == 166370211:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarEffectSequenceItem(self._io, self, self._root)
        elif _on == 678938689:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodyBoxVolume(self._io, self, self._root)
        elif _on == 1129268118:
            self._m_data = AnyGenesysObj.GenesysGenBodyMovementBehaviourTakeOffBehaviour(self._io, self, self._root)
        elif _on == 1980202577:
            self._m_data = AnyGenesysObj.GenesysGenControlMesh(self._io, self, self._root)
        elif _on == 1058122174:
            self._m_data = AnyGenesysObj.GenesysGenHeatLevelSoundSetSirens(self._io, self, self._root)
        elif _on == 3108376025:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalSpeedBasedHeightChange(self._io, self, self._root)
        elif _on == 722756325:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsCrashingRaceCar(self._io, self, self._root)
        elif _on == 3483480738:
            self._m_data = AnyGenesysObj.GenesysGenSubmixDspPlugIn(self._io, self, self._root)
        elif _on == 2276451180:
            self._m_data = AnyGenesysObj.GenesysGenCollisionInfoTrafficEffect(self._io, self, self._root)
        elif _on == 1365071824:
            self._m_data = AnyGenesysObj.GenesysGenEasyGuidePage(self._io, self, self._root)
        elif _on == 84747879:
            self._m_data = AnyGenesysObj.GenesysGenTyreLongGripCurve(self._io, self, self._root)
        elif _on == 2483448381:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersNitrousPower(self._io, self, self._root)
        elif _on == 23772465:
            self._m_data = AnyGenesysObj.GenesysGenGameplayTrigger(self._io, self, self._root)
        elif _on == 48016591:
            self._m_data = AnyGenesysObj.GenesysGenPidcontroller(self._io, self, self._root)
        elif _on == 2501750206:
            self._m_data = AnyGenesysObj.GenesysGenCollisionInfoWorldEffect(self._io, self, self._root)
        elif _on == 325575367:
            self._m_data = AnyGenesysObj.GenesysGenStoreItem(self._io, self, self._root)
        elif _on == 3732602870:
            self._m_data = AnyGenesysObj.GenesysGenGearbox(self._io, self, self._root)
        elif _on == 2075263523:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersCatchingAir(self._io, self, self._root)
        elif _on == 2516314814:
            self._m_data = AnyGenesysObj.StringBase(self._io, self, self._root)
        elif _on == 2089690370:
            self._m_data = AnyGenesysObj.GenesysGenRoadblockInstance(self._io, self, self._root)
        elif _on == 3195239353:
            self._m_data = AnyGenesysObj.GenesysGenEnginePowerCurve(self._io, self, self._root)
        elif _on == 3257509935:
            self._m_data = AnyGenesysObj.RwMathVpuVector4(self._io, self, self._root)
        elif _on == 2230798373:
            self._m_data = AnyGenesysObj.GenesysGenVehiclesPerformanceUpgradesCategory(self._io, self, self._root)
        elif _on == 477429240:
            self._m_data = AnyGenesysObj.GenesysGenWcvfxBehaviourCoronas(self._io, self, self._root)
        elif _on == 2784336371:
            self._m_data = AnyGenesysObj.RwMathVpuVector3(self._io, self, self._root)
        elif _on == 1567458252:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBody(self._io, self, self._root)
        elif _on == 716630460:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalRaceCarVsRaceCarParams(self._io, self, self._root)
        elif _on == 4062005660:
            self._m_data = AnyGenesysObj.GenesysGenVehicleColourPalette(self._io, self, self._root)
        elif _on == 2006186034:
            self._m_data = AnyGenesysObj.GenesysGenPostFxstateColourCubeSettings(self._io, self, self._root)
        elif _on == 2571445580:
            self._m_data = AnyGenesysObj.GenesysGenEventCheckpointInfo(self._io, self, self._root)
        elif _on == 4046186056:
            self._m_data = AnyGenesysObj.GenesysGenLightBase(self._io, self, self._root)
        elif _on == 3591755513:
            self._m_data = AnyGenesysObj.GenesysGenEnableCompoundBehaviour(self._io, self, self._root)
        elif _on == 3928390869:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersDonutting(self._io, self, self._root)
        elif _on == 4117767557:
            self._m_data = AnyGenesysObj.GenesysGenVehicleDamageBehaviourSpotEffect(self._io, self, self._root)
        elif _on == 2207259302:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersDrifting(self._io, self, self._root)
        elif _on == 2593852305:
            self._m_data = AnyGenesysObj.GenesysGenTrafficVehicleTraits(self._io, self, self._root)
        elif _on == 2391445668:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsAi(self._io, self, self._root)
        elif _on == 1600514099:
            self._m_data = AnyGenesysObj.GenesysGenPostFxKeyframeDepthOfField(self._io, self, self._root)
        elif _on == 3000817087:
            self._m_data = AnyGenesysObj.GenesysGenPerformanceModifier(self._io, self, self._root)
        elif _on == 835486276:
            self._m_data = AnyGenesysObj.GenesysGenGameplayDriftMarker(self._io, self, self._root)
        elif _on == 1442317719:
            self._m_data = AnyGenesysObj.GenesysGenTyreVfxBehaviourLongLatParams(self._io, self, self._root)
        elif _on == 2270583296:
            self._m_data = AnyGenesysObj.GenesysGenEventArenaData(self._io, self, self._root)
        elif _on == 3587969770:
            self._m_data = AnyGenesysObj.GenesysGenCollisionInfoBattlingDamage(self._io, self, self._root)
        elif _on == 3062587406:
            self._m_data = AnyGenesysObj.RwMathVpuMatrix44affine(self._io, self, self._root)
        elif _on == 1291389730:
            self._m_data = AnyGenesysObj.GenesysGenGameplayTriggerAiplayerInformation(self._io, self, self._root)
        elif _on == 393413962:
            self._m_data = AnyGenesysObj.GenesysGenOnlineEvent(self._io, self, self._root)
        elif _on == 1519651292:
            self._m_data = AnyGenesysObj.GenesysGenPostFxKeyframe(self._io, self, self._root)
        elif _on == 736842216:
            self._m_data = AnyGenesysObj.GenesysGenWheelSuspensionSpringConstraint(self._io, self, self._root)
        elif _on == 3794314553:
            self._m_data = AnyGenesysObj.GenesysGenBandPassDspPlugIn(self._io, self, self._root)
        elif _on == 1472679887:
            self._m_data = AnyGenesysObj.GenesysGenCollisionInfo(self._io, self, self._root)
        elif _on == 3588678847:
            self._m_data = AnyGenesysObj.GenesysGenVehicleInfoExtraAxle(self._io, self, self._root)
        elif _on == 3464877079:
            self._m_data = AnyGenesysObj.GenesysGenWcvfxBehaviour(self._io, self, self._root)
        elif _on == 1201833830:
            self._m_data = AnyGenesysObj.GenesysGenNitrousStrength(self._io, self, self._root)
        elif _on == 1730251222:
            self._m_data = AnyGenesysObj.GenesysGenQuitSequenceTimelineController(self._io, self, self._root)
        elif _on == 3643052795:
            self._m_data = AnyGenesysObj.GenesysGenTyreVfxBehaviourSmokeParams(self._io, self, self._root)
        elif _on == 2235640885:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalGlobalsImpactShake(self._io, self, self._root)
        elif _on == 3162856831:
            self._m_data = AnyGenesysObj.GenesysObjCollection(self._io, self, self._root)
        elif _on == 210492029:
            self._m_data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLatParams(self._io, self, self._root)
        elif _on == 229133803:
            self._m_data = AnyGenesysObj.GenesysGenLightProjectedTexture(self._io, self, self._root)
        elif _on == 4067794056:
            self._m_data = AnyGenesysObj.GenesysGenSequenceTimelineController(self._io, self, self._root)
        elif _on == 3691324629:
            self._m_data = AnyGenesysObj.GenesysGenAiplayerInstance(self._io, self, self._root)
        elif _on == 2896762174:
            self._m_data = AnyGenesysObj.GenesysGenCustomChevron(self._io, self, self._root)
        elif _on == 998115052:
            self._m_data = AnyGenesysObj.GenesysGenCameraRearView(self._io, self, self._root)
        elif _on == 2519567673:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinition(self._io, self, self._root)
        elif _on == 3627785814:
            self._m_data = AnyGenesysObj.GenesysGenDelayDspPlugIn(self._io, self, self._root)
        elif _on == 1680453612:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsTraffic(self._io, self, self._root)
        elif _on == 2971966527:
            self._m_data = AnyGenesysObj.GenesysGenMixerChannel(self._io, self, self._root)
        elif _on == 2655111671:
            self._m_data = AnyGenesysObj.GenesysGenDriftBehaviourDriftScale(self._io, self, self._root)
        elif _on == 2169095089:
            self._m_data = AnyGenesysObj.GenesysGenDriftBehaviourSideForce(self._io, self, self._root)
        elif _on == 61953676:
            self._m_data = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffectSkidEffects(self._io, self, self._root)
        elif _on == 3237867664:
            self._m_data = AnyGenesysObj.GenesysGenGinsuSequenceItemFade(self._io, self, self._root)
        elif _on == 4149479710:
            self._m_data = AnyGenesysObj.GenesysGenHighShelfDspPlugIn(self._io, self, self._root)
        elif _on == 174008559:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionCarState(self._io, self, self._root)
        elif _on == 4179189423:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionPhysicalDefinitionRigidBodySphereVolume(self._io, self, self._root)
        elif _on == 3085849010:
            self._m_data = AnyGenesysObj.GenesysGenPassbySequenceBehaviour(self._io, self, self._root)
        elif _on == 4049496118:
            self._m_data = AnyGenesysObj.GenesysGenMixingGroup(self._io, self, self._root)
        elif _on == 3032331154:
            self._m_data = AnyGenesysObj.GenesysGenTyreVfxBehaviourFrontRearParamsLongParams(self._io, self, self._root)
        elif _on == 786918963:
            self._m_data = AnyGenesysObj.RwMathVpuVector2(self._io, self, self._root)
        elif _on == 1822997286:
            self._m_data = AnyGenesysObj.GenesysGenSequenceItem(self._io, self, self._root)
        elif _on == 1058158881:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionJumpOverPlayers(self._io, self, self._root)
        elif _on == 283467013:
            self._m_data = AnyGenesysObj.GenesysGenVehicleSurfaceProfileSurfaceLink(self._io, self, self._root)
        elif _on == 3691704753:
            self._m_data = AnyGenesysObj.GenesysGenCollisionInfoBattlingEffectExtraRollParams(self._io, self, self._root)
        elif _on == 2080073476:
            self._m_data = AnyGenesysObj.GenesysGenScoreViewModelScore(self._io, self, self._root)
        elif _on == 880609546:
            self._m_data = AnyGenesysObj.GenesysGenPhysicsDamageBarProfileSegment(self._io, self, self._root)
        elif _on == 372702530:
            self._m_data = AnyGenesysObj.GenesysGenVehicleGameplayDamageStats(self._io, self, self._root)
        elif _on == 2950917875:
            self._m_data = AnyGenesysObj.GenesysGenDynamicAdditionalInfo(self._io, self, self._root)
        elif _on == 3935354064:
            self._m_data = AnyGenesysObj.GenesysGenSteeringBehaviourSteeringAngleCurve(self._io, self, self._root)
        elif _on == 3136795337:
            self._m_data = AnyGenesysObj.GenesysGenOnlineVoteEvent(self._io, self, self._root)
        elif _on == 832200604:
            self._m_data = AnyGenesysObj.GenesysGenPaintPack(self._io, self, self._root)
        elif _on == 2896523173:
            self._m_data = AnyGenesysObj.GenesysGenVehiclePaintMaterialProperties(self._io, self, self._root)
        elif _on == 2235129779:
            self._m_data = AnyGenesysObj.GenesysGenMixerChannelPriority(self._io, self, self._root)
        elif _on == 1259832621:
            self._m_data = AnyGenesysObj.GenesysGenColourGroup(self._io, self, self._root)
        elif _on == 4218582003:
            self._m_data = AnyGenesysObj.GenesysGenWcplaySoundBehaviour(self._io, self, self._root)
        elif _on == 3916132985:
            self._m_data = AnyGenesysObj.GenesysGenEventLocation(self._io, self, self._root)
        elif _on == 1692280813:
            self._m_data = AnyGenesysObj.GenesysGenPoint2dwithTangents(self._io, self, self._root)
        elif _on == 980106560:
            self._m_data = AnyGenesysObj.GenesysGenVehiclesNitrousUpgrade(self._io, self, self._root)
        elif _on == 3727471200:
            self._m_data = AnyGenesysObj.GenesysGenEngineReverseWhine(self._io, self, self._root)
        elif _on == 2817660171:
            self._m_data = AnyGenesysObj.GenesysGenPhysicsDamageBarProfileImpactLocationDamageScale(self._io, self, self._root)
        elif _on == 1205733723:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionAccumulateTime(self._io, self, self._root)
        elif _on == 3159067131:
            self._m_data = AnyGenesysObj.GenesysGenGameRank(self._io, self, self._root)
        elif _on == 3049882700:
            self._m_data = AnyGenesysObj.GenesysGenVehicleSurfaceProfile(self._io, self, self._root)
        elif _on == 2488860623:
            self._m_data = AnyGenesysObj.GenesysGenRoadBlockDefinition(self._io, self, self._root)
        elif _on == 397117973:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayGradientAdjustmentsParams(self._io, self, self._root)
        elif _on == 3080674119:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalTrafficVsDynamic(self._io, self, self._root)
        elif _on == 4117431335:
            self._m_data = AnyGenesysObj.GenesysGenVehiclesModifierUpgrade(self._io, self, self._root)
        elif _on == 3785567855:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersFatalHit(self._io, self, self._root)
        elif _on == 35335782:
            self._m_data = AnyGenesysObj.GenesysGenHeatLevelBehaviourCoordinationPursuitBehaviourCopBehaviour(self._io, self, self._root)
        elif _on == 3910465619:
            self._m_data = AnyGenesysObj.GenesysGenSequence(self._io, self, self._root)
        elif _on == 2992725297:
            self._m_data = AnyGenesysObj.GenesysGenTyreSoundParamsLongitudinal(self._io, self, self._root)
        elif _on == 3592057837:
            self._m_data = AnyGenesysObj.GenesysGenPostFxKeyframeBloom(self._io, self, self._root)
        elif _on == 3796279727:
            self._m_data = AnyGenesysObj.GenesysGenDamageBarProfiles(self._io, self, self._root)
        elif _on == 3434016526:
            self._m_data = AnyGenesysObj.GenesysGenVehicleGameplayModEffect(self._io, self, self._root)
        elif _on == 980871986:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayGradientAdjustments(self._io, self, self._root)
        elif _on == 3683195322:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalGlobals(self._io, self, self._root)
        elif _on == 1445450323:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionConvexHullConectivityData(self._io, self, self._root)
        elif _on == 2474227476:
            self._m_data = AnyGenesysObj.GenesysGenLfoSequenceItem(self._io, self, self._root)
        elif _on == 2952229338:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarRaceCarVsDynamic(self._io, self, self._root)
        elif _on == 3430005461:
            self._m_data = AnyGenesysObj.GenesysGenPoint2d(self._io, self, self._root)
        elif _on == 3181724531:
            self._m_data = AnyGenesysObj.GenesysGenDistortionDspPlugIn(self._io, self, self._root)
        elif _on == 4000545794:
            self._m_data = AnyGenesysObj.GenesysGenCarSelectData(self._io, self, self._root)
        elif _on == 1642529028:
            self._m_data = AnyGenesysObj.GenesysGenSequenceItemsPostFxOverrideSequenceItemEffectDoubleValue(self._io, self, self._root)
        elif _on == 662978111:
            self._m_data = AnyGenesysObj.GenesysGenVehiclesPerformanceUpgrades(self._io, self, self._root)
        elif _on == 3650009805:
            self._m_data = AnyGenesysObj.GenesysGenPhysicsDamageBarProfile(self._io, self, self._root)
        elif _on == 3037639290:
            self._m_data = AnyGenesysObj.GenesysGenAerodynamicBehaviour(self._io, self, self._root)
        elif _on == 3040986089:
            self._m_data = AnyGenesysObj.GenesysGenCoronaGlow(self._io, self, self._root)
        elif _on == 2522613547:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersSpeedbreakerUsage(self._io, self, self._root)
        elif _on == 963800229:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesGlobalTrafficVsTraffic(self._io, self, self._root)
        elif _on == 467841911:
            self._m_data = AnyGenesysObj.GenesysGenTrafficFlowType(self._io, self, self._root)
        elif _on == 574246386:
            self._m_data = AnyGenesysObj.GenesysGenVfxLocatorGroupVehicleSpotEffectSequenceItem(self._io, self, self._root)
        elif _on == 3440578930:
            self._m_data = AnyGenesysObj.GenesysGenVehicleInfoAxle(self._io, self, self._root)
        elif _on == 1758839251:
            self._m_data = AnyGenesysObj.GenesysGenGameplayCopType(self._io, self, self._root)
        elif _on == 4265727012:
            self._m_data = AnyGenesysObj.GenesysGenUicamera(self._io, self, self._root)
        elif _on == 3580468080:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffect(self._io, self, self._root)
        elif _on == 3858691605:
            self._m_data = AnyGenesysObj.GenesysGenPan2ddspPlugIn(self._io, self, self._root)
        elif _on == 106358757:
            self._m_data = AnyGenesysObj.GenesysGenBodyMovementBehaviour(self._io, self, self._root)
        elif _on == 4002008184:
            self._m_data = AnyGenesysObj.GenesysGenHandbrakeAbility(self._io, self, self._root)
        elif _on == 3395112625:
            self._m_data = AnyGenesysObj.GenesysGenTrafficVehicle(self._io, self, self._root)
        elif _on == 3954992488:
            self._m_data = AnyGenesysObj.GenesysGenVehicleInfo(self._io, self, self._root)
        elif _on == 850192155:
            self._m_data = AnyGenesysObj.GenesysGenChevron(self._io, self, self._root)
        elif _on == 1703771469:
            self._m_data = AnyGenesysObj.GenesysGenImpactDamageGraphsGraph(self._io, self, self._root)
        elif _on == 1811326154:
            self._m_data = AnyGenesysObj.GenesysGenWaveSequenceItemFade(self._io, self, self._root)
        elif _on == 3342396752:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayBonnet(self._io, self, self._root)
        elif _on == 4256545587:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersTrafficNearMiss(self._io, self, self._root)
        elif _on == 174645272:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesWorldTraffic(self._io, self, self._root)
        elif _on == 2039183453:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionCoopAccumulateDistance(self._io, self, self._root)
        elif _on == 3811132854:
            self._m_data = AnyGenesysObj.GenesysGenHandlingBehaviour(self._io, self, self._root)
        elif _on == 3529693283:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectTranslationAxisParams(self._io, self, self._root)
        elif _on == 401492861:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersUsage(self._io, self, self._root)
        elif _on == 4191696074:
            self._m_data = AnyGenesysObj.GenesysGenCollisionEffectsBattlingEffect(self._io, self, self._root)
        elif _on == 3736686144:
            self._m_data = AnyGenesysObj.GenesysGenGameplayBlacklistShutdownDataDamageThreshold(self._io, self, self._root)
        elif _on == 2634904179:
            self._m_data = AnyGenesysObj.GenesysGenGameplayTriggerInput(self._io, self, self._root)
        elif _on == 3616117713:
            self._m_data = AnyGenesysObj.GenesysGenChallengeActionAccumulateTakedowns(self._io, self, self._root)
        elif _on == 814214755:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalYawSpringModification(self._io, self, self._root)
        elif _on == 1021288769:
            self._m_data = AnyGenesysObj.GenesysGenHardDrivingBehaviourGasEffect(self._io, self, self._root)
        elif _on == 3124672599:
            self._m_data = AnyGenesysObj.GenesysGenSteeringWheelBehaviour(self._io, self, self._root)
        elif _on == 1707511637:
            self._m_data = AnyGenesysObj.GenesysGenGameplayRevengeBonus(self._io, self, self._root)
        elif _on == 3591252192:
            self._m_data = AnyGenesysObj.GenesysGenChallengeChallengePart(self._io, self, self._root)
        elif _on == 456387781:
            self._m_data = AnyGenesysObj.GenesysGenOfflineEventAlternateRoutes(self._io, self, self._root)
        elif _on == 1592993583:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesWorldCrashedPlayerConstraintData(self._io, self, self._root)
        elif _on == 760083:
            self._m_data = AnyGenesysObj.GenesysGenVehiclesVehicleCategoryInfo(self._io, self, self._root)
        elif _on == 756034263:
            self._m_data = AnyGenesysObj.GenesysGenCollisionInfoWorldDamage(self._io, self, self._root)
        elif _on == 456234940:
            self._m_data = AnyGenesysObj.GenesysGenCollisionInfoPayloadDamage(self._io, self, self._root)
        elif _on == 3406519319:
            self._m_data = AnyGenesysObj.GenesysGenAligningTorque(self._io, self, self._root)
        elif _on == 3302002317:
            self._m_data = AnyGenesysObj.GenesysGenVehicleVfxBehaviour(self._io, self, self._root)
        elif _on == 535359424:
            self._m_data = AnyGenesysObj.GenesysGenVehicleSound(self._io, self, self._root)
        elif _on == 2600271809:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersTrafficOncoming(self._io, self, self._root)
        elif _on == 1755540478:
            self._m_data = AnyGenesysObj.GenesysGenOnlineDrivingTestList(self._io, self, self._root)
        elif _on == 1218098277:
            self._m_data = AnyGenesysObj.GenesysGenEngineSound2GainParamWrapper(self._io, self, self._root)
        elif _on == 112782069:
            self._m_data = AnyGenesysObj.GenesysGenGameplayOfflineUpgrade(self._io, self, self._root)
        elif _on == 2401606622:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayExternalGlobalsLensProperties(self._io, self, self._root)
        elif _on == 2578912561:
            self._m_data = AnyGenesysObj.GenesysGenThankYouScreenItem(self._io, self, self._root)
        elif _on == 1463097890:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersCrashEscape(self._io, self, self._root)
        elif _on == 2208212217:
            self._m_data = AnyGenesysObj.GenesysGenWcvfxBehaviourSpotEffects(self._io, self, self._root)
        elif _on == 3608189499:
            self._m_data = AnyGenesysObj.GenesysGenGearboxGear(self._io, self, self._root)
        elif _on == 616120463:
            self._m_data = AnyGenesysObj.GenesysGenOfflineEventAiplayerInformation(self._io, self, self._root)
        elif _on == 2658850274:
            self._m_data = AnyGenesysObj.GenesysGenGameMode(self._io, self, self._root)
        elif _on == 4039040682:
            self._m_data = AnyGenesysObj.GenesysGenDriftBehaviourDriftExit(self._io, self, self._root)
        elif _on == 3583346207:
            self._m_data = AnyGenesysObj.GenesysGenGameUnlock(self._io, self, self._root)
        elif _on == 4223711972:
            self._m_data = AnyGenesysObj.GenesysGenEngineSound2GainParam(self._io, self, self._root)
        elif _on == 3975851796:
            self._m_data = AnyGenesysObj.GenesysGenLightPoint(self._io, self, self._root)
        elif _on == 2582603530:
            self._m_data = AnyGenesysObj.GenesysGenOfflineEventCheckpointInfo(self._io, self, self._root)
        elif _on == 4081022393:
            self._m_data = AnyGenesysObj.GenesysGenNitrousParametersBalancing(self._io, self, self._root)
        elif _on == 1001882986:
            self._m_data = AnyGenesysObj.GenesysGenRaceCarPhysicalDefinitionConvexHullConectivityDataConvexHullConnectingFace(self._io, self, self._root)
        elif _on == 1091853463:
            self._m_data = AnyGenesysObj.GenesysGenHeatLevel(self._io, self, self._root)
        elif _on == 1517189091:
            self._m_data = AnyGenesysObj.GenesysGenPhysicsLandingDamagePitch(self._io, self, self._root)
        elif _on == 3357198890:
            self._m_data = AnyGenesysObj.GenesysGenCoronaFlare(self._io, self, self._root)
        elif _on == 2328783125:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesWorldInAirPlayer(self._io, self, self._root)
        elif _on == 3573113074:
            self._m_data = AnyGenesysObj.GenesysGenStorePackList(self._io, self, self._root)
        elif _on == 1171375143:
            self._m_data = AnyGenesysObj.GenesysGenScoreViewModel(self._io, self, self._root)
        elif _on == 1220037810:
            self._m_data = AnyGenesysObj.GenesysGenCameraGameplayShakeEffectRotation(self._io, self, self._root)
        elif _on == 4120564202:
            self._m_data = AnyGenesysObj.GenesysGenPostFxstateValueModifier(self._io, self, self._root)
        elif _on == 4035751676:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarPlayerVsCrashingRaceCarProfile(self._io, self, self._root)
        elif _on == 3180273648:
            self._m_data = AnyGenesysObj.GenesysGenPostFxKeyframeVignette(self._io, self, self._root)
        elif _on == 3134806732:
            self._m_data = AnyGenesysObj.GenesysGenCollisionResponsesRaceCarAivsTrafficDamageParams(self._io, self, self._root)
        self._io.seek(_pos)
        return getattr(self, '_m_data', None)


