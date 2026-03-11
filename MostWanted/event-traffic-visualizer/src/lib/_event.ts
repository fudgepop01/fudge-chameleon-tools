/*
 * This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
 */
import KaitaiStream from 'kaitai-struct/KaitaiStream'
import {GenesysObject} from './genesys-object'

export class Event {
  _is_le?: boolean;

  constructor(
    readonly _io: KaitaiStream,
    readonly _parent?: unknown,
    readonly _root?: Event,
  ) {
    this._root ??= this;

    this._read();
  }

  _read() {
    this.header = (new GenesysObject(this._io, this, null)) as any
    this.unknownId = (this._io.readU4le()) as any
    this.eventStartOffset = (this._io.readU4le()) as any
    this.eventCount = (this._io.readU4le()) as any
    this.allEvents = [];
    for (let i = 0; i < (this.eventCount as any); i++) {
      this.allEvents.push(new Event.Ptr(this._io, this, this._root, "event_switcher"));
    }
  }

  header: GenesysObject;
  unknownId: number;
  eventStartOffset: number;
  eventCount: number;
  allEvents: Array<Event.Ptr>;
}

export namespace Event {
  export class DisplayType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Event | undefined,
      typeToDisplay: string,
    ) {
      this.typeToDisplay = typeToDisplay;

      this._read();
    }

    _read() {
    }

    private _typeName: string;
    get typeName(): string {
      if (typeof this._typeName !== 'undefined')
        return this._typeName;
      this._typeName = ((this.typeToDisplay as any)) as any
      return this._typeName;
    }

    typeToDisplay: string;
  }
}

export namespace Event {
  export class GenesysGenChallengeChallengePart {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.Atype,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.uniqueId0xc = (this._io.readU4le()) as any
      this.gameChangerId0x10 = (this._io.readU4le()) as any
      this.instruction0x14 = (this._io.readU4le()) as any
      this.uniqueId0x18 = (this._io.readU4le()) as any
      this.shortInstruction0x1c = (this._io.readU4le()) as any
      this.actionBasePtrPtrTable0x20 = (this._io.readU4le()) as any
      this.enum53371100 = (this._io.readU2le()) as any
      this.enum58391100 = (this._io.readU2le()) as any
      this.uint160x28 = (this._io.readU2le()) as any
      this.bool0x2a = (this._io.readU1()) as any
      this.arrayCountFor0x20 = (this._io.readU1()) as any
    }

    private _actionBasePtrTable: Array<Event.Ptr | undefined> | undefined;
    get actionBasePtrTable(): Array<Event.Ptr | undefined> | undefined {
      if (typeof this._actionBasePtrTable !== 'undefined')
        return this._actionBasePtrTable;
      if ((this.actionBasePtrPtrTable0x20 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.actionBasePtrPtrTable0x20 as any));
        this._actionBasePtrTable = [];
        for (let i = 0; i < (this.arrayCountFor0x20 as any); i++) {
          this._actionBasePtrTable.push(new Event.Ptr(this._io, this, this._root, "type_finder_for_genesys__gen__challenge_action__action_base"));
        }
        this._io.seek(_pos);
      }
      return this._actionBasePtrTable;
    }

    baseObject: GenesysObject;
    uniqueId0xc: number;
    gameChangerId0x10: number;
    instruction0x14: number;
    uniqueId0x18: number;
    shortInstruction0x1c: number;
    actionBasePtrPtrTable0x20: number;
    enum53371100: Event.EParentEventType;

    /**
     * 'always 1'
     */
    enum58391100: number;

    /**
     * '90, 450, or 600'
     */
    uint160x28: number;

    /**
     * 'is speedtest?'
     */
    bool0x2a: number;
    arrayCountFor0x20: number;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionAccumulationHelperData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.GenesysGenChallengeActionActionBase,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.uniqueId0xc = (this._io.readU4le()) as any
      this.uint320x10 = (this._io.readU4le()) as any
      this.enum0f391100 = (this._io.readU2le()) as any
      this.bool0x16 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    baseObject: GenesysObject;
    uniqueId0xc: number;
    uint320x10: number;
    enum0f391100: number;
    bool0x16: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionGetToLocation {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
      this.challengeLocationPtr0x48 = (new Event.Ptr(this._io, this, this._root, "genesys__gen__challenge__location")) as any
      this.routeLocation0x4c = (this._io.readU1()) as any
      this.bool0x4d = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
    challengeLocationPtr0x48: Event.Ptr;
    routeLocation0x4c: number;
    bool0x4d: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionDoJump {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
      this.challengeLocationPtr0x48 = (new Event.Ptr(this._io, this, this._root, "genesys__gen__challenge__location")) as any
      this.accumulate0x4c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
    challengeLocationPtr0x48: Event.Ptr;
    accumulate0x4c: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class VpuVector3 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.x = (this._io.readF4le()) as any
      this.y = (this._io.readF4le()) as any
      this.z = (this._io.readF4le()) as any
      this.unused2 = (this._io.readF4le()) as any
    }

    x: number;
    y: number;
    z: number;
    unused2: number;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionCoopAccumulateDistance {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
  }
}

export namespace Event {
  export class PtrPtr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Event | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _ptr: Event.Ptr | undefined;
    get ptr(): Event.Ptr | undefined {
      if (typeof this._ptr !== 'undefined')
        return this._ptr;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptr = (new Event.Ptr(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._ptr;
    }

    offset: number;
    dtype: string;
  }
}

export namespace Event {
  export class GenesysGenOfflineEventAlternateRoutes {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.OfflineEvent,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.checkpoint0xc = (this._io.readU4le()) as any
      this.routeMarkerPtrArray0x10 = (this._io.readU4le()) as any
      this.arrayCountFor0x10 = (this._io.readU2le()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _routeMarkerArray0x10: Array<number | undefined> | undefined;
    get routeMarkerArray0x10(): Array<number | undefined> | undefined {
      if (typeof this._routeMarkerArray0x10 !== 'undefined')
        return this._routeMarkerArray0x10;
      if ((this.routeMarkerPtrArray0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.routeMarkerPtrArray0x10 as any));
        this._routeMarkerArray0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._routeMarkerArray0x10.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._routeMarkerArray0x10;
    }

    baseObject: GenesysObject;
    checkpoint0xc: number;
    routeMarkerPtrArray0x10: number;
    arrayCountFor0x10: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class GenesysGenChallengeLocation {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.Atype,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.uniqueId0xc = (this._io.readU4le()) as any
      this.displayTriggerPtrArray0x10 = (this._io.readU4le()) as any
      this.gameChangerId0x14 = (this._io.readU4le()) as any
      this.triggerPtrArray0x18 = (this._io.readU4le()) as any
      this.arrayCountFor0x10 = (this._io.readU2le()) as any
      this.arrayCountFor0x18 = (this._io.readU2le()) as any
    }

    private _displayTriggerArr0x10: Array<number | undefined> | undefined;
    get displayTriggerArr0x10(): Array<number | undefined> | undefined {
      if (typeof this._displayTriggerArr0x10 !== 'undefined')
        return this._displayTriggerArr0x10;
      if ((this.displayTriggerPtrArray0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.displayTriggerPtrArray0x10 as any));
        this._displayTriggerArr0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._displayTriggerArr0x10.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._displayTriggerArr0x10;
    }

    private _triggerArr0x18: Array<number | undefined> | undefined;
    get triggerArr0x18(): Array<number | undefined> | undefined {
      if (typeof this._triggerArr0x18 !== 'undefined')
        return this._triggerArr0x18;
      if ((this.triggerPtrArray0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.triggerPtrArray0x18 as any));
        this._triggerArr0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._triggerArr0x18.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._triggerArr0x18;
    }

    baseObject: GenesysObject;
    uniqueId0xc: number;
    displayTriggerPtrArray0x10: number;
    gameChangerId0x14: number;
    triggerPtrArray0x18: number;
    arrayCountFor0x10: number;
    arrayCountFor0x18: number;
  }
}

export namespace Event {
  export class PtrArray {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Event | undefined,
      dtype: string,
      amt: number,
    ) {
      this.dtype = dtype;
      this.amt = amt;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _entries: Array<Event.Atype>;
    get entries(): Array<Event.Atype> {
      if (typeof this._entries !== 'undefined')
        return this._entries;
      let _pos = this._io.pos;
      this._io.seek((this.offset as any));
      this._entries = [];
      for (let i = 0; i < (this.amt as any); i++) {
        this._entries.push(new Event.Atype(this._io, (this as any), this._root, (this.dtype as any)));
      }
      this._io.seek(_pos);
      return this._entries;
    }

    offset: number;
    dtype: string;
    amt: number;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionActionBase {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.feedbackData = (new Event.GenesysGenChallengeActionActionBaseFeedbackData(this._io, this, this._root)) as any
      this.uniqueId0x30 = (this._io.readU4le()) as any
      this.uniqueId0x34 = (this._io.readU4le()) as any
      this.gameChangerId0x38 = (this._io.readU4le()) as any
      this.accumulationDataPtr0x3c = (this._io.readU4le()) as any
      this.enum2d391100 = (this._io.readU2le()) as any
      this.scoringMethod = (this._io.readU2le()) as any
      this.canFail = (this._io.readU2le()) as any
      this.who = (this._io.readU2le()) as any
    }

    private _accumulationData: Event.GenesysGenChallengeActionAccumulationHelperData | undefined;
    get accumulationData(): Event.GenesysGenChallengeActionAccumulationHelperData | undefined {
      if (typeof this._accumulationData !== 'undefined')
        return this._accumulationData;
      if ((this.accumulationDataPtr0x3c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.accumulationDataPtr0x3c as any));
        this._accumulationData = (new Event.GenesysGenChallengeActionAccumulationHelperData(this._io, this, this._root)) as any
        this._io.seek(_pos);
      }
      return this._accumulationData;
    }

    baseObject: GenesysObject;
    feedbackData: Event.GenesysGenChallengeActionActionBaseFeedbackData;
    uniqueId0x30: number;
    uniqueId0x34: number;
    gameChangerId0x38: number;
    accumulationDataPtr0x3c: number;
    enum2d391100: number;

    /**
     * enum_28_37_11_00
     */
    scoringMethod: number;

    /**
     * enum_e6_39_11_00
     */
    canFail: Event.EOnlineChallengeFail;

    /**
     * enum_24_37_11_00
     */
    who: Event.EOnlineChallengeInvolvement;
  }
}

export namespace Event {
  export class PtrPtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Event | undefined,
      dtype: string,
      amt: number,
    ) {
      this.dtype = dtype;
      this.amt = amt;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
      if ((this.amt as any) == 0) {
        this.count = (this._io.readU4le()) as any
      }
    }

    private _len: number;
    get len(): number {
      if (typeof this._len !== 'undefined')
        return this._len;
      this._len = (((this.amt as any) == -1 ? 0 : ((this.amt as any) == 0 ? (this.count as any) : (this.amt as any)))) as any
      return this._len;
    }

    private _ptrTable: Event.PtrTable | undefined;
    get ptrTable(): Event.PtrTable | undefined {
      if (typeof this._ptrTable !== 'undefined')
        return this._ptrTable;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptrTable = (new Event.PtrTable(this._io, this, this._root, (this.dtype as any), (this.len as any))) as any
        this._io.seek(_pos);
      }
      return this._ptrTable;
    }

    offset: number;
    count: number | undefined;
    dtype: string;
    amt: number;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionActionBaseFeedbackData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.GenesysGenChallengeActionActionBase,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.uniqueId0xc = (this._io.readU4le()) as any
      this.uniqueId0x10 = (this._io.readU4le()) as any
      this.uniqueId0x14 = (this._io.readU4le()) as any
      this.uniqueId0x18 = (this._io.readU4le()) as any
      this.uniqueId0x1c = (this._io.readU4le()) as any
      this.enum13371100 = (this._io.readU2le()) as any
      this.bool0x22 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    baseObject: GenesysObject;
    uniqueId0xc: number;
    uniqueId0x10: number;
    uniqueId0x14: number;
    uniqueId0x18: number;
    uniqueId0x1c: number;
    enum13371100: number;
    bool0x22: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionSpeedCameraAction {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
      this.uniqueId0x48 = (this._io.readU4le()) as any
      this.onHitSequence0x4c = (this._io.readU4le()) as any
      this.challengeLocationPtr0x50 = (new Event.Ptr(this._io, this, this._root, "genesys__gen__challenge__location")) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
    uniqueId0x48: number;
    onHitSequence0x4c: number;
    challengeLocationPtr0x50: Event.Ptr;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionAccumulateNearMisses {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
      this.minSpeed0x48 = (this._io.readF4le()) as any
      this.challengeLocationPtr0x4c = (new Event.Ptr(this._io, this, this._root, "genesys__gen__challenge__location")) as any
      this.inAir0x50 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
    minSpeed0x48: number;
    challengeLocationPtr0x4c: Event.Ptr;
    inAir0x50: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class OnlineEvent {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Event | undefined,
      evtOffset: number,
    ) {
      this.evtOffset = evtOffset;

      this._read();
    }

    _read() {
      this.baseObject = (new Event.EventBase(this._io, this, this._root)) as any
      this.floatArr0x4c = (this._io.readF4le()) as any
      this.floatArrEntryMaybe0x50 = (this._io.readF4le()) as any
      this.arena0x54 = (this._io.readU4le()) as any
      this.uniqueId0x58 = (this._io.readU4le()) as any
      this.uniqueId0x5c = (this._io.readU4le()) as any
      this.uniqueIdArr0x60 = (this._io.readU4le()) as any
      this.route0x64 = (this._io.readU4le()) as any
      this.arrayCountFor0x4c = (this._io.readU2le()) as any
      this.arrayCountFor0x60 = (this._io.readU2le()) as any
      this.requiresAirport0x6c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _floatArray0x50: Array<number>;
    get floatArray0x50(): Array<number> {
      if (typeof this._floatArray0x50 !== 'undefined')
        return this._floatArray0x50;
      let _pos = this._io.pos;
      this._io.seek(((this.evtOffset as any) + 76));
      this._floatArray0x50 = [];
      for (let i = 0; i < (this.arrayCountFor0x4c as any); i++) {
        this._floatArray0x50.push(this._io.readU4le());
      }
      this._io.seek(_pos);
      return this._floatArray0x50;
    }

    private _uniqueIdArray: Array<number | undefined> | undefined;
    get uniqueIdArray(): Array<number | undefined> | undefined {
      if (typeof this._uniqueIdArray !== 'undefined')
        return this._uniqueIdArray;
      if ((this.uniqueIdArr0x60 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.uniqueIdArr0x60 as any));
        this._uniqueIdArray = [];
        for (let i = 0; i < (this.arrayCountFor0x60 as any); i++) {
          this._uniqueIdArray.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._uniqueIdArray;
    }

    baseObject: Event.EventBase;
    floatArr0x4c: number;
    floatArrEntryMaybe0x50: number;
    arena0x54: number;
    uniqueId0x58: number;
    uniqueId0x5c: number;
    uniqueIdArr0x60: number;
    route0x64: number;
    arrayCountFor0x4c: number;
    arrayCountFor0x60: number;
    requiresAirport0x6c: number;
    padding: Uint8Array;
    evtOffset: number;
  }
}

export namespace Event {
  export class GenesysGenCustomChevron {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.Atype,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.gameChangerId0xc = (this._io.readU4le()) as any
      this.floatArrayPtr0x10 = (this._io.readU4le()) as any
      this.floatArrayPtr0x14 = (this._io.readU4le()) as any
      this.floatArrayPtr0x18 = (this._io.readU4le()) as any
      this.arrayCountFor0x10 = (this._io.readU2le()) as any
      this.arrayCountFor0x14 = (this._io.readU2le()) as any
      this.arrayCountFor0x18 = (this._io.readU2le()) as any
      this.invertNormal0x22 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _floatArray0x10: Array<number | undefined> | undefined;
    get floatArray0x10(): Array<number | undefined> | undefined {
      if (typeof this._floatArray0x10 !== 'undefined')
        return this._floatArray0x10;
      if ((this.floatArrayPtr0x10 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.floatArrayPtr0x10 as any));
        this._floatArray0x10 = [];
        for (let i = 0; i < (this.arrayCountFor0x10 as any); i++) {
          this._floatArray0x10.push(this._io.readF4le());
        }
        this._io.seek(_pos);
      }
      return this._floatArray0x10;
    }

    private _floatArray0x14: Array<number | undefined> | undefined;
    get floatArray0x14(): Array<number | undefined> | undefined {
      if (typeof this._floatArray0x14 !== 'undefined')
        return this._floatArray0x14;
      if ((this.floatArrayPtr0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.floatArrayPtr0x14 as any));
        this._floatArray0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0x14 as any); i++) {
          this._floatArray0x14.push(this._io.readF4le());
        }
        this._io.seek(_pos);
      }
      return this._floatArray0x14;
    }

    private _floatArray0x18: Array<number | undefined> | undefined;
    get floatArray0x18(): Array<number | undefined> | undefined {
      if (typeof this._floatArray0x18 !== 'undefined')
        return this._floatArray0x18;
      if ((this.floatArrayPtr0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.floatArrayPtr0x18 as any));
        this._floatArray0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._floatArray0x18.push(this._io.readF4le());
        }
        this._io.seek(_pos);
      }
      return this._floatArray0x18;
    }

    baseObject: GenesysObject;
    gameChangerId0xc: number;
    floatArrayPtr0x10: number;
    floatArrayPtr0x14: number;
    floatArrayPtr0x18: number;
    arrayCountFor0x10: number;
    arrayCountFor0x14: number;
    arrayCountFor0x18: number;
    invertNormal0x22: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class EventBase {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.autotestCheckpoints0xc = (this._io.readU4le()) as any
      this.cinematicName0x10 = (this._io.readU4le()) as any
      this.description0x14 = (this._io.readU4le()) as any
      this.gameChangerId0x18 = (this._io.readU4be()) as any
      this.gameMode0x1c = (this._io.readU4be()) as any
      this.gamePack0x20 = (this._io.readU4le()) as any
      this.uniqueId0x24 = (this._io.readU4le()) as any
      this.cycleTimeOfDay0x28 = (this._io.readF4le()) as any
      this.finishTimeOfDay0x2c = (this._io.readF4le()) as any
      this.sunDirection0x30 = (this._io.readF4le()) as any
      this.timeOfDay0x34 = (this._io.readF4le()) as any
      this.float0x38 = (this._io.readF4le()) as any
      this.chevronList0x3c = (this._io.readU4le()) as any
      this.roadSurfaceConditions = (this._io.readU2le()) as any
      this.arrayCountFor0xc = (this._io.readU2le()) as any
      this.isAlternativeWeather0x44 = (this._io.readU1()) as any
      this.isRainActive0x45 = (this._io.readU1()) as any
      this.isThunderActive0x46 = (this._io.readU1()) as any
      this.overrideSunDirection0x47 = (this._io.readU1()) as any
      this.bool0x48 = (this._io.readU1()) as any
      this.arrayCountFor0x3c = (this._io.readU1()) as any
      this.uint80x4a = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _uniqueIdArray: Array<number | undefined> | undefined;
    get uniqueIdArray(): Array<number | undefined> | undefined {
      if (typeof this._uniqueIdArray !== 'undefined')
        return this._uniqueIdArray;
      if ((this.autotestCheckpoints0xc as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.autotestCheckpoints0xc as any));
        this._uniqueIdArray = [];
        for (let i = 0; i < (this.arrayCountFor0xc as any); i++) {
          this._uniqueIdArray.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._uniqueIdArray;
    }

    private _kind: Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType;
    get kind(): Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType {
      if (typeof this._kind !== 'undefined')
        return this._kind;
      switch ((this.gameMode0x1c as any)) {
        case 2979270144: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "Speedrun")) as any
          break;
        }
        case 2922909952: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "mp_CHALLENGE")) as any
          break;
        }
        case 506659840: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "Cut/Unfinished")) as any
          break;
        }
        case 1361584384: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "Drift")) as any
          break;
        }
        case 703857920: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "Ambush")) as any
          break;
        }
        case 2173636352: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "mp_RACE")) as any
          break;
        }
        case 496240128: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "mp_FREEDRIVE")) as any
          break;
        }
        case 516888320: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "Intro")) as any
          break;
        }
        case 32769280: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "Free Drive")) as any
          break;
        }
        case 3509981440: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "mp_SPEEDTEST")) as any
          break;
        }
        case 134483712: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "mp_TEAM_RACE")) as any
          break;
        }
        case 3501728000: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "Smash n Grab")) as any
          break;
        }
        case 2418215680: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "Sprint or Circuit")) as any
          break;
        }
        default: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "unknown")) as any
          break;
        }
      }
      return this._kind;
    }

    private _eventName: Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType;
    get eventName(): Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType {
      if (typeof this._eventName !== 'undefined')
        return this._eventName;
      switch ((this.gameChangerId0x18 as any)) {
        case 1297356288: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COOL TAKEDOWNS")) as any
          break;
        }
        case 3115519744: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Cruise Control")) as any
          break;
        }
        case 2346983168: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Around the World")) as any
          break;
        }
        case 837294080: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DUNE JUMPER")) as any
          break;
        }
        case 1335894016: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DAM JUMP")) as any
          break;
        }
        case 1598887936: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TRAIL BLAZER")) as any
          break;
        }
        case 3245351168: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Deadline")) as any
          break;
        }
        case 195043328: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TO THE BRIDGE")) as any
          break;
        }
        case 1198006784: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Jailbird")) as any
          break;
        }
        case 95491840: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RAIL TRACK SPEED RUN")) as any
          break;
        }
        case 178266112: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TO THE BRIDGE")) as any
          break;
        }
        case 568924928: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "AROUND THE WORLD")) as any
          break;
        }
        case 528228608: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "AIRPORT SITE DRIFT")) as any
          break;
        }
        case 2825789696: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "License to Thrill")) as any
          break;
        }
        case 743839232: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STEEL CITY")) as any
          break;
        }
        case 592713216: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DOWNFALL")) as any
          break;
        }
        case 609032192: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RAIL JUMPER")) as any
          break;
        }
        case 3839104256: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MISSING LOCKS")) as any
          break;
        }
        case 894834176: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RED SHIFT")) as any
          break;
        }
        case 2565281792: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "THE GETAWAY")) as any
          break;
        }
        case 293347584: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GLOBE RAMPS DRIFT")) as any
          break;
        }
        case 3367114496: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PowerPlant")) as any
          break;
        }
        case 72030208: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "SOUTH STATION JUMP")) as any
          break;
        }
        case 173348352: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ALL OVER THE SHOP")) as any
          break;
        }
        case 2707825152: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Ship to Shore")) as any
          break;
        }
        case 468129792: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RAT RACE")) as any
          break;
        }
        case 564142080: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CHAIN REACTION")) as any
          break;
        }
        case 2505315840: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BLOCK RD SPEED TRAP")) as any
          break;
        }
        case 11144960: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Import Duty")) as any
          break;
        }
        case 832577536: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CRASHDOWN")) as any
          break;
        }
        case 1773213440: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PARK MANSION SPEED RUN")) as any
          break;
        }
        case 676599296: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "OFF THE GRID")) as any
          break;
        }
        case 1005000704: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STOPPING POWER")) as any
          break;
        }
        case 692983808: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STORM DRAIN DRIFT")) as any
          break;
        }
        case 157622784: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Air Raid")) as any
          break;
        }
        case 2335121408: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Full Overdrive")) as any
          break;
        }
        case 313464576: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PIPE MISSES")) as any
          break;
        }
        case 3571980288: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PLATFORM PARKING")) as any
          break;
        }
        case 2343507712: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "HUGHES PARK LAKE JUMP")) as any
          break;
        }
        case 518658048: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "KRUGER SPEED")) as any
          break;
        }
        case 3150317568: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Rolling Stock")) as any
          break;
        }
        case 3933217024: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Live and let Drive")) as any
          break;
        }
        case 1747918848: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Live for Speed")) as any
          break;
        }
        case 2209421056: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STORM DRAIN SPEED RUN")) as any
          break;
        }
        case 3880523776: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CARGO PLANE JUMP")) as any
          break;
        }
        case 1072306176: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "FLIGHT DISTANCE")) as any
          break;
        }
        case 2984712192: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CRASH LANDING")) as any
          break;
        }
        case 2444105472: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "INTERLOCKING DRIFTS")) as any
          break;
        }
        case 722018560: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Sidewinder")) as any
          break;
        }
        case 2351898624: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Full Throttle")) as any
          break;
        }
        case 803479296: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Steel City")) as any
          break;
        }
        case 1833703424: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BURNING RUBBER")) as any
          break;
        }
        case 736630784: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BELL HOPPING")) as any
          break;
        }
        case 1704992768: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CARGO SHIP JUMP")) as any
          break;
        }
        case 2655787008: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MEAN STREETS")) as any
          break;
        }
        case 1161894144: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COOL DRIFTING")) as any
          break;
        }
        case 2952663040: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BRIDGES FREEDRIVE")) as any
          break;
        }
        case 1112937984: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "WAVE LENGTH")) as any
          break;
        }
        case 726865408: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PYRAMID JUMP")) as any
          break;
        }
        case 3008632320: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "SHOCKING PARKING")) as any
          break;
        }
        case 3219593216: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "NEEDLE POINT")) as any
          break;
        }
        case 1323572992: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Critical Path")) as any
          break;
        }
        case 2601718016: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Stopping Power")) as any
          break;
        }
        case 1633031680: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "FAST TRACK")) as any
          break;
        }
        case 4204732416: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "INDUSTRIAL WAY")) as any
          break;
        }
        case 2494502656: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "LAKE LAUNCH")) as any
          break;
        }
        case 3367048960: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PLANE JUMPER")) as any
          break;
        }
        case 827659776: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "LORENZO AVE BRIDGE JUMP")) as any
          break;
        }
        case 131405312: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "The Fugitive")) as any
          break;
        }
        case 1884100608: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DOWNTOWN RUN")) as any
          break;
        }
        case 4187955200: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "INDUSTRIAL WAY")) as any
          break;
        }
        case 4062256384: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Keys to the City")) as any
          break;
        }
        case 3533643776: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "IMPORT DUTY")) as any
          break;
        }
        case 3410630656: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CONTAINER PARK")) as any
          break;
        }
        case 1991317248: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER PLANT SPEED RUN")) as any
          break;
        }
        case 299177216: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BLOCK JUMPER")) as any
          break;
        }
        case 1096160768: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "WAVE LENGTH")) as any
          break;
        }
        case 1642665984: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PIER DRIFT")) as any
          break;
        }
        case 2941654528: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GREEN ZONE")) as any
          break;
        }
        case 2162694144: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "OVER THE EDGE")) as any
          break;
        }
        case 2423922944: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "NOW BOARDING")) as any
          break;
        }
        case 3654554880: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MCCLANE CONVEYOR JUMP")) as any
          break;
        }
        case 3617529856: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "JUMPING JACKS")) as any
          break;
        }
        case 2582059008: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "THE GETAWAY")) as any
          break;
        }
        case 1867912704: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "SPORTS SPRINT")) as any
          break;
        }
        case 3313246464: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "KEYS TO THE CITY")) as any
          break;
        }
        case 2020024832: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Bring the Noise")) as any
          break;
        }
        case 2072383744: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PIER PRESSURE")) as any
          break;
        }
        case 1672419072: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BELL TOWER JUMP")) as any
          break;
        }
        case 2866091264: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ABANDON SHIP!")) as any
          break;
        }
        case 3947501568: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "HARRIS RD JUMP")) as any
          break;
        }
        case 1012274688: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RED SHIFT")) as any
          break;
        }
        case 1165435136: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Power Slide")) as any
          break;
        }
        case 1557468416: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TIGHT SHIPPING")) as any
          break;
        }
        case 3840282624: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Chain Reaction")) as any
          break;
        }
        case 2494633728: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BARGES SPEED RUN")) as any
          break;
        }
        case 3277067776: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PIER PARKING")) as any
          break;
        }
        case 1400512768: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TERMINAL PLANE JUMP")) as any
          break;
        }
        case 1028397056: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TERMINAL VELOCITY")) as any
          break;
        }
        case 749737728: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "AIRFIELD DRIFT")) as any
          break;
        }
        case 1196824064: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "INDUSTRIAL REVOLUTION")) as any
          break;
        }
        case 2222661888: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "FLIGHTPLAN")) as any
          break;
        }
        case 3285388544: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Off the Grid")) as any
          break;
        }
        case 2438141440: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "KRUGER AIR")) as any
          break;
        }
        case 2135693312: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "OUT OF THE LOOP")) as any
          break;
        }
        case 3534624512: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STUNT WORKSHOP")) as any
          break;
        }
        case 588583168: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Crush Hour")) as any
          break;
        }
        case 2205884672: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "FLIGHTPLAN")) as any
          break;
        }
        case 794170880: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "KINGS STOP SPRINT")) as any
          break;
        }
        case 1313675264: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER PLAY")) as any
          break;
        }
        case 2930710272: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "AN AGGRESSIVE MANOR")) as any
          break;
        }
        case 3553957120: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "LIGHTHOUSE DRIFT")) as any
          break;
        }
        case 1867323392: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DOWNTOWN RUN")) as any
          break;
        }
        case 3310163968: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "THE ENFORCER")) as any
          break;
        }
        case 2793021696: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GLOBAL JUMPERS")) as any
          break;
        }
        case 1836785920: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "LAST CALL")) as any
          break;
        }
        case 3242858496: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DOWNGRADED")) as any
          break;
        }
        case 551821056: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Terminal Velocity")) as any
          break;
        }
        case 380638976: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "WING WALKER")) as any
          break;
        }
        case 2152272640: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "To the Bridge")) as any
          break;
        }
        case 3632599296: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GOING UNDER")) as any
          break;
        }
        case 3427538944: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BELTWAY W HOOPS JUMP")) as any
          break;
        }
        case 1045174272: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TERMINAL VELOCITY")) as any
          break;
        }
        case 1213601280: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "INDUSTRIAL REVOLUTION")) as any
          break;
        }
        case 1783895552: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GRAVITY")) as any
          break;
        }
        case 2431129600: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CRANE PARKING")) as any
          break;
        }
        case 4285604096: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Running Wild")) as any
          break;
        }
        case 1168707328: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Straight to the Point")) as any
          break;
        }
        case 1583092992: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 6")) as any
          break;
        }
        case 536085760: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Freedrive")) as any
          break;
        }
        case 676075520: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PARK AND RIDE")) as any
          break;
        }
        case 3176404480: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER PLANT ALLEY JUMP")) as any
          break;
        }
        case 210112768: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PIER POWER")) as any
          break;
        }
        case 659887616: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MARKET JUMP")) as any
          break;
        }
        case 804652288: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Freedrive")) as any
          break;
        }
        case 1121067520: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Inner City Pressure")) as any
          break;
        }
        case 3231653888: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CRUSH HOUR")) as any
          break;
        }
        case 316740864: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Liberty Park")) as any
          break;
        }
        case 2678656768: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Red Shift")) as any
          break;
        }
        case 300162816: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Downfall")) as any
          break;
        }
        case 2427392256: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Industrial Revolution")) as any
          break;
        }
        case 2958431744: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GREEN ZONE")) as any
          break;
        }
        case 1901336064: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GRAVITY")) as any
          break;
        }
        case 2829259008: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Turbine")) as any
          break;
        }
        case 3209369600: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PARADISE MISSED")) as any
          break;
        }
        case 3684638720: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MUD BATH")) as any
          break;
        }
        case 4269220096: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Duty Free")) as any
          break;
        }
        case 199759872: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BURNING BRIDGES")) as any
          break;
        }
        case 3251773696: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Air Brake")) as any
          break;
        }
        case 2136348160: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "UNDER THE BRIDGE")) as any
          break;
        }
        case 226889984: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "WHITE HEAT")) as any
          break;
        }
        case 1900746752: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DRIFT THE LOOP")) as any
          break;
        }
        case 492115456: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ROSEWOOD PL JUMP")) as any
          break;
        }
        case 770316288: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DOWNHILL STEPS")) as any
          break;
        }
        case 3293386752: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "THE ENFORCER")) as any
          break;
        }
        case 3377796608: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "HIGH POWER")) as any
          break;
        }
        case 1147609600: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "High Stakes")) as any
          break;
        }
        case 1752113408: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted GTR")) as any
          break;
        }
        case 3126138368: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STEEL JUMPER")) as any
          break;
        }
        case 3235190016: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CONSTRUCTION SITE DRIFT")) as any
          break;
        }
        case 3701415936: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MUD BATH")) as any
          break;
        }
        case 2130841344: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Turbulence")) as any
          break;
        }
        case 3202816000: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "NEEDLE POINT")) as any
          break;
        }
        case 3323138304: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Burning Rubber")) as any
          break;
        }
        case 3823572992: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CANNONBALL RUN")) as any
          break;
        }
        case 729555200: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "AIRPORT BEACH JUMP")) as any
          break;
        }
        case 1162745856: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TURBINE HALL DRIFT")) as any
          break;
        }
        case 2622690816: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CONSTRUCTION TAKEDOWN")) as any
          break;
        }
        case 583997184: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Welcome To Fairhaven")) as any
          break;
        }
        case 1850480640: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BURNING RUBBER")) as any
          break;
        }
        case 3059095040: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RUNNING THE GAUNTLET")) as any
          break;
        }
        case 4289599232: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STUNT CRANE")) as any
          break;
        }
        case 3088321792: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Crash Landing")) as any
          break;
        }
        case 2740262400: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "WORKSHOP TAKEDOWN")) as any
          break;
        }
        case 541857792: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BURKE ST SPEED TRAP")) as any
          break;
        }
        case 899686400: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GET TO THE CHOPPER")) as any
          break;
        }
        case 2741113856: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BALANCE BEAM")) as any
          break;
        }
        case 849354752: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CRASHDOWN")) as any
          break;
        }
        case 547364864: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CHAIN REACTION")) as any
          break;
        }
        case 3248431104: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CRUSH HOUR")) as any
          break;
        }
        case 1692866560: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ZERO TOLERANCE")) as any
          break;
        }
        case 1290213376: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BORROWED TIME")) as any
          break;
        }
        case 3690468608: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Fast Track")) as any
          break;
        }
        case 594616576: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Pulp Friction")) as any
          break;
        }
        case 463478784: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ARCH ENEMIES")) as any
          break;
        }
        case 2773293056: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "NARROW MARGIN")) as any
          break;
        }
        case 3350337280: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Bridges")) as any
          break;
        }
        case 78649088: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "AIR PIPE")) as any
          break;
        }
        case 2712606464: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BELL TOWER DRIFT")) as any
          break;
        }
        case 3291677696: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER TRIP")) as any
          break;
        }
        case 3696367104: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PYRAMID PLATFORM")) as any
          break;
        }
        case 3030912768: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Pumping Iron")) as any
          break;
        }
        case 2538935808: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MARKET CRASH")) as any
          break;
        }
        case 4120840704: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Stock Market Crash")) as any
          break;
        }
        case 1320228608: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MCCLANE BRIDGE SPEED RUN")) as any
          break;
        }
        case 2556433408: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ARCH ANGELS")) as any
          break;
        }
        case 2839615744: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STANDARD SHIPPING")) as any
          break;
        }
        case 1339364608: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER PLANT DRIFT")) as any
          break;
        }
        case 3246788864: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DRIVE HARD")) as any
          break;
        }
        case 2640978176: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Get to Callahan")) as any
          break;
        }
        case 2440307200: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CLEAR FOR TAKEOFF")) as any
          break;
        }
        case 1555109632: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "I-92W DIRT TRACK SPEED RUN")) as any
          break;
        }
        case 2672564224: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MEAN STREETS")) as any
          break;
        }
        case 2376147200: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted Spyder")) as any
          break;
        }
        case 216537088: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BURNING BRIDGES")) as any
          break;
        }
        case 3594590464: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MONUMENTAL DRIFT")) as any
          break;
        }
        case 1729498368: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Turf War")) as any
          break;
        }
        case 3092518400: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STRAIGHT TO THE POINT")) as any
          break;
        }
        case 2152470528: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "OUT OF THE LOOP")) as any
          break;
        }
        case 2075137792: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MISSED BY THE BELL")) as any
          break;
        }
        case 1131356416: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Bootlegging")) as any
          break;
        }
        case 342172160: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Green Belt")) as any
          break;
        }
        case 2035553792: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MISSING BARGES")) as any
          break;
        }
        case 2437617664: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TAKEDOWN TO THE BRIDGE")) as any
          break;
        }
        case 2815694336: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 7")) as any
          break;
        }
        case 3271626496: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Crashdown")) as any
          break;
        }
        case 3213234432: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PIER PRESSURE")) as any
          break;
        }
        case 2169771520: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CALLAHAN OVERPASS JUMP")) as any
          break;
        }
        case 2678724352: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Bloody Nose")) as any
          break;
        }
        case 3249477376: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MANSION MISSLES")) as any
          break;
        }
        case 2330400768: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ABSOLUTE POWER")) as any
          break;
        }
        case 1391073280: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CONNORS BRIDGE RD SPEED TRAP")) as any
          break;
        }
        case 3756529664: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COLD BURN")) as any
          break;
        }
        case 4160296704: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BRIDGES FREEDRIVE")) as any
          break;
        }
        case 189470720: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MURPHY ST SPEED TRAP")) as any
          break;
        }
        case 3042317824: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RUNNING THE GAUNTLET")) as any
          break;
        }
        case 2390300160: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 9")) as any
          break;
        }
        case 2581864192: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted Venom")) as any
          break;
        }
        case 1705578240: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Arch Enemies")) as any
          break;
        }
        case 3970436864: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Power Struggle")) as any
          break;
        }
        case 2249986560: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Downgraded")) as any
          break;
        }
        case 3628800000: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PIPE UP")) as any
          break;
        }
        case 860690432: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CALLAHAN CONTAINERS JUMP")) as any
          break;
        }
        case 2792759552: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Aerial Agression")) as any
          break;
        }
        case 1716786688: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "EMMERSON BELTWAY")) as any
          break;
        }
        case 1330518016: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BELTWAY S SPEED TRAP")) as any
          break;
        }
        case 3386119424: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DRIFT HARD")) as any
          break;
        }
        case 1129125888: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PETERSON ST SPEED TRAP")) as any
          break;
        }
        case 901715712: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 4")) as any
          break;
        }
        case 609490432: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "WHITE HEAT")) as any
          break;
        }
        case 360257024: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 10")) as any
          break;
        }
        case 659953152: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STEEL CITY")) as any
          break;
        }
        case 2457084416: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CLEAR FOR TAKEOFF")) as any
          break;
        }
        case 3541766656: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Downtown Run")) as any
          break;
        }
        case 3691122432: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Park and Country")) as any
          break;
        }
        case 3182499584: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ROOFTOP PARKING")) as any
          break;
        }
        case 122558464: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "SUDDEN IMPACT")) as any
          break;
        }
        case 4099151360: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "INTO THE STORM")) as any
          break;
        }
        case 1407063296: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Collateral Damage")) as any
          break;
        }
        case 2812223488: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COLLATERAL DAMAGE")) as any
          break;
        }
        case 360390912: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BUMPY LANDINGS")) as any
          break;
        }
        case 1682642944: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PETERSON LOOP DRIFT")) as any
          break;
        }
        case 4249491456: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "FOLEY ST PARKING JUMP")) as any
          break;
        }
        case 785716480: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DRIFT LIGHT")) as any
          break;
        }
        case 1604263936: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TURBULENCE")) as any
          break;
        }
        case 3103985408: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Cannonball Run")) as any
          break;
        }
        case 2729514752: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COAL YARD SPEED RUN")) as any
          break;
        }
        case 1012209152: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "FOUR BRIDGES TOWER JUMP")) as any
          break;
        }
        case 2242909952: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "KNOCKING OFF")) as any
          break;
        }
        case 4232779776: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "I-92E PIPE JUMP")) as any
          break;
        }
        case 659298304: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PARK AND RIDE")) as any
          break;
        }
        case 548345600: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CLIFFTOP DRIFTERS")) as any
          break;
        }
        case 3567849216: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Cold Burn")) as any
          break;
        }
        case 3600752640: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "JUMPING JACKS")) as any
          break;
        }
        case 3571914752: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PUMPING IRON")) as any
          break;
        }
        case 2212566272: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 5")) as any
          break;
        }
        case 2051741696: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "HEFLIN BRIDGE JUMP")) as any
          break;
        }
        case 2829000704: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COLLATERAL DAMAGE")) as any
          break;
        }
        case 3229229312: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GROUND EFFECTS")) as any
          break;
        }
        case 4243068928: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PARK ARCHES SPEED RUN")) as any
          break;
        }
        case 176558336: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CRITICAL PATH")) as any
          break;
        }
        case 703010816: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STOCK MARKET CRASH")) as any
          break;
        }
        case 662446336: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "EXCESS BAGGAGE")) as any
          break;
        }
        case 1054152192: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 1")) as any
          break;
        }
        case 1085216512: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GANT ST SPEED TRAP")) as any
          break;
        }
        case 2152536064: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "SECOND SIGHT")) as any
          break;
        }
        case 2320766464: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "SHOCKLEY RD SPEED TRAP")) as any
          break;
        }
        case 4105049856: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "I-92E CRANE JUMP")) as any
          break;
        }
        case 626267648: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER TRIP")) as any
          break;
        }
        case 1833834496: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER PARKING")) as any
          break;
        }
        case 2669416960: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Needle Point")) as any
          break;
        }
        case 1582110720: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TRAIL BLAZER")) as any
          break;
        }
        case 1087381760: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Drift City")) as any
          break;
        }
        case 3967426816: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RUNWAY SPEED TRAP")) as any
          break;
        }
        case 1851135488: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "SPORTS SPRINT")) as any
          break;
        }
        case 3581550848: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GLOBAL DRIFTERS")) as any
          break;
        }
        case 971511808: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "HARRIS RD JUMP")) as any
          break;
        }
        case 1608912896: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Mud Bath")) as any
          break;
        }
        case 4177073920: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BRIDGES FREEDRIVE")) as any
          break;
        }
        case 2444302080: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MALL PARK")) as any
          break;
        }
        case 2337478144: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DRIFT SITE")) as any
          break;
        }
        case 1007231232: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Easy Drifter")) as any
          break;
        }
        case 3699708160: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BLACKOUT")) as any
          break;
        }
        case 585702144: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "AROUND THE WORLD")) as any
          break;
        }
        case 760616448: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "KINGPIN")) as any
          break;
        }
        case 1517560320: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TERMINAL PARKING")) as any
          break;
        }
        case 2991920640: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "LIGHTHOUSE LEAPS")) as any
          break;
        }
        case 2078547712: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Burning Bridges")) as any
          break;
        }
        case 3530957056: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Round Trip")) as any
          break;
        }
        case 2429883648: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "WITHIN THE LAW")) as any
          break;
        }
        case 1816859392: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Jumping Jacks")) as any
          break;
        }
        case 134485504: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Sprint Eastward")) as any
          break;
        }
        case 215291136: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER MISS")) as any
          break;
        }
        case 3354924288: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Running the Gauntlet")) as any
          break;
        }
        case 139335680: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "SUDDEN IMPACT")) as any
          break;
        }
        case 1964379392: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Emmerson Beltway")) as any
          break;
        }
        case 2840991232: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CONTINENTAL DRIFT")) as any
          break;
        }
        case 3899728128: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Braking Traction")) as any
          break;
        }
        case 1577912064: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Continetal Drift")) as any
          break;
        }
        case 896540928: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Sudden Impact")) as any
          break;
        }
        case 1943344640: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Get to the Chopper")) as any
          break;
        }
        case 685053184: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STRAIGHT TO THE POINT")) as any
          break;
        }
        case 1206523904: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DRIFT UP A STORM")) as any
          break;
        }
        case 4081719296: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COOLING TOWER DRIFT")) as any
          break;
        }
        case 1831737088: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 2")) as any
          break;
        }
        case 686233600: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STOCK MARKET CRASH")) as any
          break;
        }
        case 3310098432: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GARBER ST JUMP")) as any
          break;
        }
        case 424351744: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "LOWREY ST SPEED TRAP")) as any
          break;
        }
        case 3226081280: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DOWNGRADED")) as any
          break;
        }
        case 139270144: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "WING AND A PRAYER")) as any
          break;
        }
        case 3887011584: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BELL TOWER TAKEDOWN")) as any
          break;
        }
        case 1045829120: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ROLLING STOCK")) as any
          break;
        }
        case 659822080: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GOING UNDER")) as any
          break;
        }
        case 2724336640: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ARCHES JUMP")) as any
          break;
        }
        case 1286608640: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "HANGAR ON")) as any
          break;
        }
        case 3739752448: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COLD BURN")) as any
          break;
        }
        case 1726486528: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STUNT SITE")) as any
          break;
        }
        case 994908160: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CALLAHAN CONVEYOR JUMP")) as any
          break;
        }
        case 3772585216: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "The Getaway")) as any
          break;
        }
        case 480256000: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ARCH ENEMIES")) as any
          break;
        }
        case 3604288768: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STEP ON THE GRASS")) as any
          break;
        }
        case 602345472: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Trail Blazer")) as any
          break;
        }
        case 1084235776: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "INTERLOCKING LOOPS JUMP")) as any
          break;
        }
        case 1531648000: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "INTERLOCKING LOOPS DRIFT")) as any
          break;
        }
        case 1752441344: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "NOW BOARDING")) as any
          break;
        }
        case 1480003840: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MCCALE I-92 JUMP")) as any
          break;
        }
        case 1045305344: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MARKET DRIFT")) as any
          break;
        }
        case 4120846336: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TURBULENCE")) as any
          break;
        }
        case 916463616: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GET TO THE CHOPPER")) as any
          break;
        }
        case 3830061056: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COAL YARD JUMP")) as any
          break;
        }
        case 628561408: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Double Parked")) as any
          break;
        }
        case 1709643776: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ZERO TOLERANCE")) as any
          break;
        }
        case 3761051392: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Storehouse Stakeout")) as any
          break;
        }
        case 1616123392: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "EMMERSON BELTWAY")) as any
          break;
        }
        case 1836065024: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Bullet Train")) as any
          break;
        }
        case 2315456256: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Park and Ride")) as any
          break;
        }
        case 390928384: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "AIR TRAFFIC CONTROL")) as any
          break;
        }
        case 2473599232: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Mayhem")) as any
          break;
        }
        case 1826889472: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Green Zone")) as any
          break;
        }
        case 2909217280: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Speed Demon")) as any
          break;
        }
        case 2833913856: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "GREAT SCOTT!")) as any
          break;
        }
        case 1296898048: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER PLAY")) as any
          break;
        }
        case 794039808: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "OFF THE GRID")) as any
          break;
        }
        case 2313623552: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ABSOLUTE POWER")) as any
          break;
        }
        case 1028920832: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "COAL YARDAGE")) as any
          break;
        }
        case 1635524864: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CARGO PLANE JUMP")) as any
          break;
        }
        case 2706576896: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "OVER THE HIGHWAY")) as any
          break;
        }
        case 3280343296: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DRIVE HARD")) as any
          break;
        }
        case 1839929088: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "The Hunted")) as any
          break;
        }
        case 2757891072: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "LOWREY ST SPEED TRAP")) as any
          break;
        }
        case 3148814080: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TO THE MANOR AIRBORNE")) as any
          break;
        }
        case 2587957504: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DRIVEN LOOPY")) as any
          break;
        }
        case 2775523584: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted GT500")) as any
          break;
        }
        case 59052288: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CRITICAL PATH")) as any
          break;
        }
        case 2270500352: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BRIDGE WRECKED")) as any
          break;
        }
        case 4024440064: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 8")) as any
          break;
        }
        case 1330976256: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "HARBOR RUN")) as any
          break;
        }
        case 266803200: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER LOOP")) as any
          break;
        }
        case 665917184: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CONNORS BRIDGE RD SPEED RUN")) as any
          break;
        }
        case 3350206208: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RAIL TRACK SPEED RUN")) as any
          break;
        }
        case 193335552: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DOWNFALL")) as any
          break;
        }
        case 1991186176: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "MANSION JUMP")) as any
          break;
        }
        case 2236291072: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BELTWAY W JUMP")) as any
          break;
        }
        case 2833522432: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "The Descent")) as any
          break;
        }
        case 1513033728: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BLACKOUT")) as any
          break;
        }
        case 1952915968: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Fuelled")) as any
          break;
        }
        case 648742144: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Freedrive")) as any
          break;
        }
        case 4051964160: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PIER POWER")) as any
          break;
        }
        case 3303675904: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "DONT KILL THE CAR")) as any
          break;
        }
        case 1735664128: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "NOW BOARDING")) as any
          break;
        }
        case 3806795776: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CANNONBALL RUN")) as any
          break;
        }
        case 148182272: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "HARBOR RUN")) as any
          break;
        }
        case 2000754944: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ONE WAY TO PARADISE")) as any
          break;
        }
        case 1055137536: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Drive Hard")) as any
          break;
        }
        case 3550420992: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "IMPORT DUTY")) as any
          break;
        }
        case 484907008: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RAT RACE")) as any
          break;
        }
        case 3990689024: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Industrial Way")) as any
          break;
        }
        case 250025984: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "POWER LOOP")) as any
          break;
        }
        case 1366565376: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TERMINAL LEAP")) as any
          break;
        }
        case 531894016: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Power Play")) as any
          break;
        }
        case 1333534976: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CAMERON DRIVE JUMPS")) as any
          break;
        }
        case 3416921856: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Most Wanted 3")) as any
          break;
        }
        case 1853563136: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "LAST CALL")) as any
          break;
        }
        case 1261900032: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "KRUGER AVE SPEED TRAP")) as any
          break;
        }
        case 2857768448: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CONTINENTAL DRIFT")) as any
          break;
        }
        case 1021777920: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "STOPPING POWER")) as any
          break;
        }
        case 2756515840: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "NARROW MARGIN")) as any
          break;
        }
        case 3588691968: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "PUMPING IRON")) as any
          break;
        }
        case 3269922816: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Sports Sprint")) as any
          break;
        }
        case 2208567552: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Gravity")) as any
          break;
        }
        case 1616254464: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "FAST TRACK")) as any
          break;
        }
        case 4200997376: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Destruction Site")) as any
          break;
        }
        case 3001489408: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "CRASH LANDING")) as any
          break;
        }
        case 2105155840: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "RUNWAY PLANE JUMP")) as any
          break;
        }
        case 1001395968: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "TOWER DRIFT")) as any
          break;
        }
        case 3242268928: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "AIR SPEED")) as any
          break;
        }
        case 2863666944: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "HIGH HEELS")) as any
          break;
        }
        case 3296469248: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "KEYS TO THE CITY")) as any
          break;
        }
        case 2647987456: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "2ND FLOOR SQUEEZE")) as any
          break;
        }
        case 1306990592: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "BORROWED TIME")) as any
          break;
        }
        case 2731740416: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "Harbor Run")) as any
          break;
        }
        case 2351833088: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "The Enforcer")) as any
          break;
        }
        case 2461013760: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "WORKSHOP DONUTS")) as any
          break;
        }
        case 2169313280: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "SECOND SIGHT")) as any
          break;
        }
        case 1029051904: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "ROLLING STOCK")) as any
          break;
        }
        case 4283700736: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "K&N WORKSHOP DRIFT")) as any
          break;
        }
        default: {
          this._eventName = (new Event.DisplayType(this._io, this, this._root, "unknown")) as any
          break;
        }
      }
      return this._eventName;
    }

    private _roadSurfaceCondition: Event.DisplayType | undefined | Event.DisplayType | undefined | Event.DisplayType | undefined | undefined;
    get roadSurfaceCondition(): Event.DisplayType | undefined | Event.DisplayType | undefined | Event.DisplayType | undefined | undefined {
      if (typeof this._roadSurfaceCondition !== 'undefined')
        return this._roadSurfaceCondition;
      switch ((this.roadSurfaceConditions as any)) {
        case 0: {
          this._roadSurfaceCondition = (new Event.DisplayType(this._io, this, this._root, "Dry")) as any
          break;
        }
        case 1: {
          this._roadSurfaceCondition = (new Event.DisplayType(this._io, this, this._root, "Wet")) as any
          break;
        }
        case 2: {
          this._roadSurfaceCondition = (new Event.DisplayType(this._io, this, this._root, "StandingWater")) as any
          break;
        }
      }
      return this._roadSurfaceCondition;
    }

    private _customChevronPtrArray: Array<Event.Ptr | undefined> | undefined;
    get customChevronPtrArray(): Array<Event.Ptr | undefined> | undefined {
      if (typeof this._customChevronPtrArray !== 'undefined')
        return this._customChevronPtrArray;
      if ((this.chevronList0x3c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.chevronList0x3c as any));
        this._customChevronPtrArray = [];
        for (let i = 0; i < (this.arrayCountFor0x3c as any); i++) {
          this._customChevronPtrArray.push(new Event.Ptr(this._io, this, this._root, "genesys__gen__custom_chevron"));
        }
        this._io.seek(_pos);
      }
      return this._customChevronPtrArray;
    }

    baseObject: GenesysObject;
    autotestCheckpoints0xc: number;
    cinematicName0x10: number;
    description0x14: number;
    gameChangerId0x18: number;
    gameMode0x1c: number;
    gamePack0x20: number;
    uniqueId0x24: number;
    cycleTimeOfDay0x28: number;
    finishTimeOfDay0x2c: number;
    sunDirection0x30: number;
    timeOfDay0x34: number;
    float0x38: number;
    chevronList0x3c: number;

    /**
     * enum_8b_38_09_00
     */
    roadSurfaceConditions: number;
    arrayCountFor0xc: number;
    isAlternativeWeather0x44: number;
    isRainActive0x45: number;
    isThunderActive0x46: number;
    overrideSunDirection0x47: number;
    bool0x48: number;
    arrayCountFor0x3c: number;
    uint80x4a: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class PtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Event | undefined,
      dtype: string,
      amt: number,
    ) {
      this.dtype = dtype;
      this.amt = amt;

      this._read();
    }

    _read() {
      this.entries = [];
      for (let i = 0; i < (this.amt as any); i++) {
        this.entries.push(new Event.Ptr(this._io, this, this._root, (this.dtype as any)));
      }
    }

    entries: Array<Event.Ptr>;
    dtype: string;
    amt: number;
  }
}

export namespace Event {
  export class Dummy {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.Atype,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
    }

    private _d: string;
    get d(): string {
      if (typeof this._d !== 'undefined')
        return this._d;
      this._d = ("dummy") as any
      return this._d;
    }

  }
}

export namespace Event {
  export class GenesysGenChevron {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.Atype,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.gameChangerId0xc = (this._io.readU4le()) as any
      this.roadSection0x10 = (this._io.readU4le()) as any
      this.shouldBlockStart0x14 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    baseObject: GenesysObject;
    gameChangerId0xc: number;
    roadSection0x10: number;
    shouldBlockStart0x14: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class MultiplayerChallengeType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.raceHeader = (this._io.readBytes(12)) as any
    }

    raceHeader: Uint8Array;
  }
}

export namespace Event {
  export class EventSwitcher {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.Atype,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
    }

    private _offlineEvent: Event.OfflineEvent | undefined;
    get offlineEvent(): Event.OfflineEvent | undefined {
      if (typeof this._offlineEvent !== 'undefined')
        return this._offlineEvent;
      if ((this.baseObject as any).muTypeVersion == 2419838023) {
        let _pos = this._io.pos;
        this._io.seek((this._parent as any)._parent.offset);
        this._offlineEvent = (new Event.OfflineEvent(this._io, this, this._root, (this._parent as any)._parent.offset)) as any
        this._io.seek(_pos);
      }
      return this._offlineEvent;
    }

    private _onlineEvent: Event.OnlineEvent | undefined;
    get onlineEvent(): Event.OnlineEvent | undefined {
      if (typeof this._onlineEvent !== 'undefined')
        return this._onlineEvent;
      if ((this.baseObject as any).muTypeVersion == 393413962) {
        let _pos = this._io.pos;
        this._io.seek((this._parent as any)._parent.offset);
        this._onlineEvent = (new Event.OnlineEvent(this._io, this, this._root, (this._parent as any)._parent.offset)) as any
        this._io.seek(_pos);
      }
      return this._onlineEvent;
    }

    private _onlineChallenge: Event.OnlineChallenge | undefined;
    get onlineChallenge(): Event.OnlineChallenge | undefined {
      if (typeof this._onlineChallenge !== 'undefined')
        return this._onlineChallenge;
      if ((this.baseObject as any).muTypeVersion == 2121274978) {
        let _pos = this._io.pos;
        this._io.seek((this._parent as any)._parent.offset);
        this._onlineChallenge = (new Event.OnlineChallenge(this._io, this, this._root, (this._parent as any)._parent.offset)) as any
        this._io.seek(_pos);
      }
      return this._onlineChallenge;
    }

    private _voteEvent: Event.VoteEvent | undefined;
    get voteEvent(): Event.VoteEvent | undefined {
      if (typeof this._voteEvent !== 'undefined')
        return this._voteEvent;
      if ((this.baseObject as any).muTypeVersion == 3136795337) {
        let _pos = this._io.pos;
        this._io.seek((this._parent as any)._parent.offset);
        this._voteEvent = (new Event.VoteEvent(this._io, this, this._root, (this._parent as any)._parent.offset)) as any
        this._io.seek(_pos);
      }
      return this._voteEvent;
    }

    baseObject: GenesysObject;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionAccumulateTakedowns {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
  }
}

export namespace Event {
  export class VoteEvent {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: Event.EventSwitcher | undefined,
      readonly _root: Event | undefined,
      evtOffset: number,
    ) {
      this.evtOffset = evtOffset;

      this._read();
    }

    _read() {
      this.baseObject = (new Event.OnlineEvent(this._io, this, this._root, (this.evtOffset as any))) as any
      this.uniqueId0x70 = (this._io.readU4le()) as any
      this.uniqueId0x74 = (this._io.readU4le()) as any
      this.uniqueId0x78 = (this._io.readU4le()) as any
      this.uniqueId0x7c = (this._io.readU4le()) as any
    }

    baseObject: Event.OnlineEvent;
    uniqueId0x70: number;
    uniqueId0x74: number;
    uniqueId0x78: number;
    uniqueId0x7c: number;
    evtOffset: number;
  }
}

export namespace Event {
  export class MultiplayerRaceType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.raceHeader = (this._io.readBytes(12)) as any
    }

    raceHeader: Uint8Array;
  }
}

export namespace Event {
  export class OnlineChallenge {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: Event.EventSwitcher | undefined,
      readonly _root: Event | undefined,
      evtOffset: number,
    ) {
      this.evtOffset = evtOffset;

      this._read();
    }

    _read() {
      this.baseObject = (new Event.OnlineEvent(this._io, this, this._root, (this.evtOffset as any))) as any
      this.intro0x70 = (this._io.readU4le()) as any
      this.uniqueId0x74 = (this._io.readU4le()) as any
      this.challengePartPtrPtrTable0x78 = (this._io.readU4le()) as any
      this.eliminationType = (this._io.readU2le()) as any
      this.typeVal = (this._io.readU2le()) as any
      this.arrayCountFor0x78 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    private _challengePartPtrTable: Array<Event.Ptr | undefined> | undefined;
    get challengePartPtrTable(): Array<Event.Ptr | undefined> | undefined {
      if (typeof this._challengePartPtrTable !== 'undefined')
        return this._challengePartPtrTable;
      if ((this.challengePartPtrPtrTable0x78 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.challengePartPtrPtrTable0x78 as any));
        this._challengePartPtrTable = [];
        for (let i = 0; i < (this.arrayCountFor0x78 as any); i++) {
          this._challengePartPtrTable.push(new Event.Ptr(this._io, this, this._root, "genesys__gen__challenge__challenge_part"));
        }
        this._io.seek(_pos);
      }
      return this._challengePartPtrTable;
    }

    baseObject: Event.OnlineEvent;
    intro0x70: number;
    uniqueId0x74: number;
    challengePartPtrPtrTable0x78: number;

    /**
     * enum_ff_f8_17_00
     */
    eliminationType: Event.EOnlineEliminationType;

    /**
     * enum_c3_38_11_00
     */
    typeVal: Event.EOnlineChallengeType;
    arrayCountFor0x78: number;
    padding: Uint8Array;
    evtOffset: number;
  }
}

export namespace Event {
  export class OfflineEvent {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: Event.EventSwitcher | undefined,
      readonly _root: Event | undefined,
      evtOffset: number,
    ) {
      this.evtOffset = evtOffset;

      this._read();
    }

    _read() {
      this.baseObject = (new Event.EventBase(this._io, this, this._root)) as any
      this.trafficOverrides0x4c = (this._io.readBytes(8)) as any
      this.additionalAssetsPtr0x54 = (this._io.readU4le()) as any
      this.aiHintsPtr0x58 = (this._io.readU4le()) as any
      this.allowedVehicleList0x5c = (this._io.readU4le()) as any
      this.uniqueId0x60 = (this._io.readU4le()) as any
      this.checkpointsPtr0x64 = (this._io.readU4le()) as any
      this.uniqueId0x68 = (this._io.readU4le()) as any
      this.defaultHeatLevelsPtr0x6c = (this._io.readU4le()) as any
      this.eventIntro0x70 = (this._io.readU4le()) as any
      this.eventOutro0x74 = (this._io.readU4le()) as any
      this.feedbackMessageGroup0x78 = (this._io.readU4le()) as any
      this.gameplayTriggersPtr0x7c = (this._io.readU4le()) as any
      this.uniqueId0x80 = (this._io.readU4le()) as any
      this.name0x84 = (this._io.readU4le()) as any
      this.nameFormatted0x88 = (this._io.readU4le()) as any
      this.nextStoryEvent0x8c = (this._io.readU4le()) as any
      this.uniqueId0x90 = (this._io.readU4le()) as any
      this.raceBalancingData0x94 = (this._io.readU4le()) as any
      this.raceBalancingProfile0x98 = (this._io.readU4le()) as any
      this.spawnPosition0x9c = (this._io.readU4le()) as any
      this.timelinePtr0xa0 = (this._io.readU4le()) as any
      this.typeName0xa4 = (this._io.readU4le()) as any
      this.targetSpeedPtr0xa8 = (this._io.readU4le()) as any
      this.targetTimePtr0xac = (this._io.readU4le()) as any
      this.trafficDensity0xb0 = (this._io.readU4le()) as any
      this.chevronPtrPtrTable0xb4 = (this._io.readU4le()) as any
      this.customChevronPtrPtrTable0xb8 = (this._io.readU4le()) as any
      this.gameplayConditionPtrPtrTable0xbc = (this._io.readU4le()) as any
      this.aiPlayerInformationPtrArray0xc0 = (this._io.readU4le()) as any
      this.alternateRoutesPtrArray0xc4 = (this._io.readU4le()) as any
      this.checkpointInfoPtrArray0xc8 = (this._io.readU4le()) as any
      this.targetScore0xcc = (this._io.readU4le()) as any
      this.demoMode = (this._io.readU2le()) as any
      this.arrayCountFor0x54 = (this._io.readU2le()) as any
      this.arrayCountFor0x58 = (this._io.readU2le()) as any
      this.arrayCountFor0xc0 = (this._io.readU2le()) as any
      this.arrayCountFor0xc4 = (this._io.readU2le()) as any
      this.arrayCountFor0xc8 = (this._io.readU2le()) as any
      this.arrayCountFor0x64 = (this._io.readU2le()) as any
      this.arrayCountFor0x6c = (this._io.readU2le()) as any
      this.arrayCountFor0xb4 = (this._io.readU2le()) as any
      this.arrayCountFor0xa8 = (this._io.readU2le()) as any
      this.arrayCountFor0xac = (this._io.readU2le()) as any
      this.arrayCountFor0xa0 = (this._io.readU2le()) as any
      this.copSpawning0xe8 = (this._io.readU1()) as any
      this.bool0xe9 = (this._io.readU1()) as any
      this.bool0xea = (this._io.readU1()) as any
      this.bool0xeb = (this._io.readU1()) as any
      this.nitrousAllowed0xec = (this._io.readU1()) as any
      this.noRacingLineTraffic0xed = (this._io.readU1()) as any
      this.bool0xee = (this._io.readU1()) as any
      this.startWithEngineOn0xef = (this._io.readU1()) as any
      this.trafficEnabled0xf0 = (this._io.readU1()) as any
      this.bool0xf1 = (this._io.readU1()) as any
      this.weaponsAllowed0xf2 = (this._io.readU1()) as any
      this.arrayCountFor0xb8 = (this._io.readU1()) as any
      this.arrayCountFor0xbc = (this._io.readU1()) as any
      this.arrayCountFor0x7c = (this._io.readU1()) as any
      this.laps0xf6 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(1)) as any
    }

    private _gameplayTriggers0x7c: Array<number | undefined> | undefined;
    get gameplayTriggers0x7c(): Array<number | undefined> | undefined {
      if (typeof this._gameplayTriggers0x7c !== 'undefined')
        return this._gameplayTriggers0x7c;
      if ((this.gameplayTriggersPtr0x7c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.gameplayTriggersPtr0x7c as any));
        this._gameplayTriggers0x7c = [];
        for (let i = 0; i < (this.arrayCountFor0x7c as any); i++) {
          this._gameplayTriggers0x7c.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._gameplayTriggers0x7c;
    }

    private _targetSpeed0xa8: Array<number | undefined> | undefined;
    get targetSpeed0xa8(): Array<number | undefined> | undefined {
      if (typeof this._targetSpeed0xa8 !== 'undefined')
        return this._targetSpeed0xa8;
      if ((this.targetSpeedPtr0xa8 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.targetSpeedPtr0xa8 as any));
        this._targetSpeed0xa8 = [];
        for (let i = 0; i < (this.arrayCountFor0xa8 as any); i++) {
          this._targetSpeed0xa8.push(this._io.readF4le());
        }
        this._io.seek(_pos);
      }
      return this._targetSpeed0xa8;
    }

    private _gameplayConditionPtrArray0xbc: Array<Event.Ptr | undefined> | undefined;
    get gameplayConditionPtrArray0xbc(): Array<Event.Ptr | undefined> | undefined {
      if (typeof this._gameplayConditionPtrArray0xbc !== 'undefined')
        return this._gameplayConditionPtrArray0xbc;
      if ((this.gameplayConditionPtrPtrTable0xbc as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.gameplayConditionPtrPtrTable0xbc as any));
        this._gameplayConditionPtrArray0xbc = [];
        for (let i = 0; i < (this.arrayCountFor0xbc as any); i++) {
          this._gameplayConditionPtrArray0xbc.push(new Event.Ptr(this._io, this, this._root, "genesys__gen__gameplay__condition"));
        }
        this._io.seek(_pos);
      }
      return this._gameplayConditionPtrArray0xbc;
    }

    private _additionalAssets0x54: Array<number | undefined> | undefined;
    get additionalAssets0x54(): Array<number | undefined> | undefined {
      if (typeof this._additionalAssets0x54 !== 'undefined')
        return this._additionalAssets0x54;
      if ((this.additionalAssetsPtr0x54 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.additionalAssetsPtr0x54 as any));
        this._additionalAssets0x54 = [];
        for (let i = 0; i < (this.arrayCountFor0x54 as any); i++) {
          this._additionalAssets0x54.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._additionalAssets0x54;
    }

    private _aiHints0x58: Array<number | undefined> | undefined;
    get aiHints0x58(): Array<number | undefined> | undefined {
      if (typeof this._aiHints0x58 !== 'undefined')
        return this._aiHints0x58;
      if ((this.aiHintsPtr0x58 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.aiHintsPtr0x58 as any));
        this._aiHints0x58 = [];
        for (let i = 0; i < (this.arrayCountFor0x58 as any); i++) {
          this._aiHints0x58.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._aiHints0x58;
    }

    private _timeline0xa0: Array<number | undefined> | undefined;
    get timeline0xa0(): Array<number | undefined> | undefined {
      if (typeof this._timeline0xa0 !== 'undefined')
        return this._timeline0xa0;
      if ((this.timelinePtr0xa0 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.timelinePtr0xa0 as any));
        this._timeline0xa0 = [];
        for (let i = 0; i < (this.arrayCountFor0xa0 as any); i++) {
          this._timeline0xa0.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._timeline0xa0;
    }

    private _defaultHeatLevels0x6c: Array<number | undefined> | undefined;
    get defaultHeatLevels0x6c(): Array<number | undefined> | undefined {
      if (typeof this._defaultHeatLevels0x6c !== 'undefined')
        return this._defaultHeatLevels0x6c;
      if ((this.defaultHeatLevelsPtr0x6c as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.defaultHeatLevelsPtr0x6c as any));
        this._defaultHeatLevels0x6c = [];
        for (let i = 0; i < (this.arrayCountFor0x6c as any); i++) {
          this._defaultHeatLevels0x6c.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._defaultHeatLevels0x6c;
    }

    private _checkpoints0x64: Array<number | undefined> | undefined;
    get checkpoints0x64(): Array<number | undefined> | undefined {
      if (typeof this._checkpoints0x64 !== 'undefined')
        return this._checkpoints0x64;
      if ((this.checkpointsPtr0x64 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.checkpointsPtr0x64 as any));
        this._checkpoints0x64 = [];
        for (let i = 0; i < (this.arrayCountFor0x64 as any); i++) {
          this._checkpoints0x64.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._checkpoints0x64;
    }

    private _targetTime0xac: Array<number | undefined> | undefined;
    get targetTime0xac(): Array<number | undefined> | undefined {
      if (typeof this._targetTime0xac !== 'undefined')
        return this._targetTime0xac;
      if ((this.targetTimePtr0xac as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.targetTimePtr0xac as any));
        this._targetTime0xac = [];
        for (let i = 0; i < (this.arrayCountFor0xac as any); i++) {
          this._targetTime0xac.push(this._io.readF4le());
        }
        this._io.seek(_pos);
      }
      return this._targetTime0xac;
    }

    private _aiPlayerInformationArray0xc0: Array<Event.GenesysGenOfflineEventAiPlayerInformation | undefined> | undefined;
    get aiPlayerInformationArray0xc0(): Array<Event.GenesysGenOfflineEventAiPlayerInformation | undefined> | undefined {
      if (typeof this._aiPlayerInformationArray0xc0 !== 'undefined')
        return this._aiPlayerInformationArray0xc0;
      if ((this.aiPlayerInformationPtrArray0xc0 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.aiPlayerInformationPtrArray0xc0 as any));
        this._aiPlayerInformationArray0xc0 = [];
        for (let i = 0; i < (this.arrayCountFor0xc0 as any); i++) {
          this._aiPlayerInformationArray0xc0.push(new Event.GenesysGenOfflineEventAiPlayerInformation(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._aiPlayerInformationArray0xc0;
    }

    private _chevronPtrArray0xb4: Array<Event.Ptr | undefined> | undefined;
    get chevronPtrArray0xb4(): Array<Event.Ptr | undefined> | undefined {
      if (typeof this._chevronPtrArray0xb4 !== 'undefined')
        return this._chevronPtrArray0xb4;
      if ((this.chevronPtrPtrTable0xb4 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.chevronPtrPtrTable0xb4 as any));
        this._chevronPtrArray0xb4 = [];
        for (let i = 0; i < (this.arrayCountFor0xb4 as any); i++) {
          this._chevronPtrArray0xb4.push(new Event.Ptr(this._io, this, this._root, "genesys__gen__chevron"));
        }
        this._io.seek(_pos);
      }
      return this._chevronPtrArray0xb4;
    }

    private _customChevronPtrArray0xb8: Array<Event.Ptr | undefined> | undefined;
    get customChevronPtrArray0xb8(): Array<Event.Ptr | undefined> | undefined {
      if (typeof this._customChevronPtrArray0xb8 !== 'undefined')
        return this._customChevronPtrArray0xb8;
      if ((this.customChevronPtrPtrTable0xb8 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.customChevronPtrPtrTable0xb8 as any));
        this._customChevronPtrArray0xb8 = [];
        for (let i = 0; i < (this.arrayCountFor0xb8 as any); i++) {
          this._customChevronPtrArray0xb8.push(new Event.Ptr(this._io, this, this._root, "genesys__gen__custom_chevron"));
        }
        this._io.seek(_pos);
      }
      return this._customChevronPtrArray0xb8;
    }

    private _alternateRoutes0xc4: Array<Event.GenesysGenOfflineEventAlternateRoutes | undefined> | undefined;
    get alternateRoutes0xc4(): Array<Event.GenesysGenOfflineEventAlternateRoutes | undefined> | undefined {
      if (typeof this._alternateRoutes0xc4 !== 'undefined')
        return this._alternateRoutes0xc4;
      if ((this.alternateRoutesPtrArray0xc4 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.alternateRoutesPtrArray0xc4 as any));
        this._alternateRoutes0xc4 = [];
        for (let i = 0; i < (this.arrayCountFor0xc4 as any); i++) {
          this._alternateRoutes0xc4.push(new Event.GenesysGenOfflineEventAlternateRoutes(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._alternateRoutes0xc4;
    }

    private _checkpointInfoArray0xc8: Array<Event.GenesysGenOfflineEventCheckpointInfo | undefined> | undefined;
    get checkpointInfoArray0xc8(): Array<Event.GenesysGenOfflineEventCheckpointInfo | undefined> | undefined {
      if (typeof this._checkpointInfoArray0xc8 !== 'undefined')
        return this._checkpointInfoArray0xc8;
      if ((this.checkpointInfoPtrArray0xc8 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.checkpointInfoPtrArray0xc8 as any));
        this._checkpointInfoArray0xc8 = [];
        for (let i = 0; i < (this.arrayCountFor0xc8 as any); i++) {
          this._checkpointInfoArray0xc8.push(new Event.GenesysGenOfflineEventCheckpointInfo(this._io, this, this._root));
        }
        this._io.seek(_pos);
      }
      return this._checkpointInfoArray0xc8;
    }

    baseObject: Event.EventBase;
    trafficOverrides0x4c: Uint8Array;
    additionalAssetsPtr0x54: number;
    aiHintsPtr0x58: number;
    allowedVehicleList0x5c: number;
    uniqueId0x60: number;
    checkpointsPtr0x64: number;
    uniqueId0x68: number;
    defaultHeatLevelsPtr0x6c: number;
    eventIntro0x70: number;
    eventOutro0x74: number;
    feedbackMessageGroup0x78: number;
    gameplayTriggersPtr0x7c: number;
    uniqueId0x80: number;
    name0x84: number;
    nameFormatted0x88: number;
    nextStoryEvent0x8c: number;
    uniqueId0x90: number;
    raceBalancingData0x94: number;
    raceBalancingProfile0x98: number;
    spawnPosition0x9c: number;
    timelinePtr0xa0: number;
    typeName0xa4: number;
    targetSpeedPtr0xa8: number;
    targetTimePtr0xac: number;
    trafficDensity0xb0: number;
    chevronPtrPtrTable0xb4: number;
    customChevronPtrPtrTable0xb8: number;
    gameplayConditionPtrPtrTable0xbc: number;
    aiPlayerInformationPtrArray0xc0: number;
    alternateRoutesPtrArray0xc4: number;
    checkpointInfoPtrArray0xc8: number;
    targetScore0xcc: number;

    /**
     * enum_f7_f2_0e_00
     */
    demoMode: number;
    arrayCountFor0x54: number;
    arrayCountFor0x58: number;
    arrayCountFor0xc0: number;
    arrayCountFor0xc4: number;
    arrayCountFor0xc8: number;
    arrayCountFor0x64: number;
    arrayCountFor0x6c: number;
    arrayCountFor0xb4: number;
    arrayCountFor0xa8: number;
    arrayCountFor0xac: number;
    arrayCountFor0xa0: number;
    copSpawning0xe8: number;
    bool0xe9: number;
    bool0xea: number;
    bool0xeb: number;
    nitrousAllowed0xec: number;
    noRacingLineTraffic0xed: number;
    bool0xee: number;
    startWithEngineOn0xef: number;
    trafficEnabled0xf0: number;
    bool0xf1: number;
    weaponsAllowed0xf2: number;
    arrayCountFor0xb8: number;
    arrayCountFor0xbc: number;
    arrayCountFor0x7c: number;
    laps0xf6: number;
    padding: Uint8Array;
    evtOffset: number;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionAccumulateDistance {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionCarState {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
      this.carCategory0x48 = (this._io.readU4le()) as any
      this.float0x4c = (this._io.readF4le()) as any
      this.float0x50 = (this._io.readF4le()) as any
      this.maxSpeed0x54 = (this._io.readU2le()) as any
      this.minSpeed0x56 = (this._io.readU2le()) as any
      this.bool0x58 = (this._io.readU1()) as any
      this.bool0x59 = (this._io.readU1()) as any
      this.bool0x5a = (this._io.readU1()) as any
      this.donutting0x5b = (this._io.readU1()) as any
      this.drifting0x5c = (this._io.readU1()) as any
      this.inAir0x5d = (this._io.readU1()) as any
      this.nitrous0x5e = (this._io.readU1()) as any
      this.bool0x5f = (this._io.readU1()) as any
      this.reversing0x60 = (this._io.readU1()) as any
      this.slipstreaming0x61 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
    carCategory0x48: number;
    float0x4c: number;
    float0x50: number;
    maxSpeed0x54: number;
    minSpeed0x56: number;
    bool0x58: number;
    bool0x59: number;
    bool0x5a: number;
    donutting0x5b: number;
    drifting0x5c: number;
    inAir0x5d: number;
    nitrous0x5e: number;
    bool0x5f: number;
    reversing0x60: number;
    slipstreaming0x61: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionHitTrigger {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
      this.trigger0x48 = (this._io.readU4le()) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
    trigger0x48: number;
  }
}

export namespace Event {
  export class TempEventType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.raceHeader = (this._io.readBytes(12)) as any
    }

    private _lapCount: number;
    get lapCount(): number {
      if (typeof this._lapCount !== 'undefined')
        return this._lapCount;
      let _pos = this._io.pos;
      this._io.seek(238);
      this._lapCount = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._lapCount;
    }

    private _eventTypeHash: number;
    get eventTypeHash(): number {
      if (typeof this._eventTypeHash !== 'undefined')
        return this._eventTypeHash;
      let _pos = this._io.pos;
      this._io.seek(20);
      this._eventTypeHash = (this._io.readU4be()) as any
      this._io.seek(_pos);
      return this._eventTypeHash;
    }

    private _weaponAvailability: number;
    get weaponAvailability(): number {
      if (typeof this._weaponAvailability !== 'undefined')
        return this._weaponAvailability;
      let _pos = this._io.pos;
      this._io.seek(234);
      this._weaponAvailability = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._weaponAvailability;
    }

    private _easydriveStringId: Uint8Array;
    get easydriveStringId(): Uint8Array {
      if (typeof this._easydriveStringId !== 'undefined')
        return this._easydriveStringId;
      let _pos = this._io.pos;
      this._io.seek(128);
      this._easydriveStringId = (this._io.readBytes(4)) as any
      this._io.seek(_pos);
      return this._easydriveStringId;
    }

    private _evtNameId: number;
    get evtNameId(): number {
      if (typeof this._evtNameId !== 'undefined')
        return this._evtNameId;
      let _pos = this._io.pos;
      this._io.seek(84);
      this._evtNameId = (this._io.readU4be()) as any
      this._io.seek(_pos);
      return this._evtNameId;
    }

    private _cutsceneId: Uint8Array;
    get cutsceneId(): Uint8Array {
      if (typeof this._cutsceneId !== 'undefined')
        return this._cutsceneId;
      let _pos = this._io.pos;
      this._io.seek(104);
      this._cutsceneId = (this._io.readBytes(4)) as any
      this._io.seek(_pos);
      return this._cutsceneId;
    }

    private _copsInTraffic: number;
    get copsInTraffic(): number {
      if (typeof this._copsInTraffic !== 'undefined')
        return this._copsInTraffic;
      let _pos = this._io.pos;
      this._io.seek(224);
      this._copsInTraffic = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._copsInTraffic;
    }

    private _evtTypeModifier: Uint8Array;
    get evtTypeModifier(): Uint8Array {
      if (typeof this._evtTypeModifier !== 'undefined')
        return this._evtTypeModifier;
      let _pos = this._io.pos;
      this._io.seek(12);
      this._evtTypeModifier = (this._io.readBytes(4)) as any
      this._io.seek(_pos);
      return this._evtTypeModifier;
    }

    private _evtId: number;
    get evtId(): number {
      if (typeof this._evtId !== 'undefined')
        return this._evtId;
      let _pos = this._io.pos;
      this._io.seek(16);
      this._evtId = (this._io.readU4le()) as any
      this._io.seek(_pos);
      return this._evtId;
    }

    private _fileId: Uint8Array;
    get fileId(): Uint8Array {
      if (typeof this._fileId !== 'undefined')
        return this._fileId;
      let _pos = this._io.pos;
      this._io.seek(120);
      this._fileId = (this._io.readBytes(4)) as any
      this._io.seek(_pos);
      return this._fileId;
    }

    private _floatMaybe: Array<number>;
    get floatMaybe(): Array<number> {
      if (typeof this._floatMaybe !== 'undefined')
        return this._floatMaybe;
      let _pos = this._io.pos;
      this._io.seek(240);
      this._floatMaybe = [];
      for (let i = 0; i < 0; i++) {
        this._floatMaybe.push(this._io.readU4le());
      }
      this._io.seek(_pos);
      return this._floatMaybe;
    }

    private _dlcPack: Uint8Array;
    get dlcPack(): Uint8Array {
      if (typeof this._dlcPack !== 'undefined')
        return this._dlcPack;
      let _pos = this._io.pos;
      this._io.seek(24);
      this._dlcPack = (this._io.readBytes(4)) as any
      this._io.seek(_pos);
      return this._dlcPack;
    }

    private _numberOfCheckpoints: number;
    get numberOfCheckpoints(): number {
      if (typeof this._numberOfCheckpoints !== 'undefined')
        return this._numberOfCheckpoints;
      let _pos = this._io.pos;
      this._io.seek(212);
      this._numberOfCheckpoints = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._numberOfCheckpoints;
    }

    private _eventTypeName: Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType;
    get eventTypeName(): Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType {
      if (typeof this._eventTypeName !== 'undefined')
        return this._eventTypeName;
      switch ((this.eventTypeHash as any)) {
        case 2979270144: {
          this._eventTypeName = (new Event.DisplayType(this._io, this, this._root, "Speedrun")) as any
          break;
        }
        case 1361584384: {
          this._eventTypeName = (new Event.DisplayType(this._io, this, this._root, "Drift")) as any
          break;
        }
        case 703857920: {
          this._eventTypeName = (new Event.DisplayType(this._io, this, this._root, "Ambush")) as any
          break;
        }
        case 516888320: {
          this._eventTypeName = (new Event.DisplayType(this._io, this, this._root, "Intro")) as any
          break;
        }
        case 32769280: {
          this._eventTypeName = (new Event.DisplayType(this._io, this, this._root, "Free Drive")) as any
          break;
        }
        case 3501728000: {
          this._eventTypeName = (new Event.DisplayType(this._io, this, this._root, "Smash n Grab")) as any
          break;
        }
        case 2418215680: {
          this._eventTypeName = (new Event.DisplayType(this._io, this, this._root, "Sprint or Circuit")) as any
          break;
        }
        default: {
          this._eventTypeName = (new Event.DisplayType(this._io, this, this._root, "unknown")) as any
          break;
        }
      }
      return this._eventTypeName;
    }

    private _weatherConfig: Event.WeatherConditions;
    get weatherConfig(): Event.WeatherConditions {
      if (typeof this._weatherConfig !== 'undefined')
        return this._weatherConfig;
      let _pos = this._io.pos;
      this._io.seek(32);
      this._raw_weatherConfig = (this._io.readBytes(48)) as any
      let _io__raw_weatherConfig = new KaitaiStream(this._raw_weatherConfig);
      this._weatherConfig = (new Event.WeatherConditions(_io__raw_weatherConfig, this, this._root)) as any
      this._io.seek(_pos);
      return this._weatherConfig;
    }

    private _cpuCount: number;
    get cpuCount(): number {
      if (typeof this._cpuCount !== 'undefined')
        return this._cpuCount;
      let _pos = this._io.pos;
      this._io.seek(237);
      this._cpuCount = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._cpuCount;
    }

    raceHeader: Uint8Array;
    _raw_weatherConfig: Uint8Array;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionJumpStats {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
      this.challengeLocationPtr0x48 = (new Event.Ptr(this._io, this, this._root, "genesys__gen__challenge__location")) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
    challengeLocationPtr0x48: Event.Ptr;
  }
}

export namespace Event {
  export class Ptr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Event | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _data: Event.Atype | undefined;
    get data(): Event.Atype | undefined {
      if (typeof this._data !== 'undefined')
        return this._data;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._data = (new Event.Atype(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._data;
    }

    offset: number;
    dtype: string;
  }
}

export namespace Event {
  export class WeatherConditions {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
    }

    private _wetRoads: number;
    get wetRoads(): number {
      if (typeof this._wetRoads !== 'undefined')
        return this._wetRoads;
      let _pos = this._io.pos;
      this._io.seek(8);
      this._wetRoads = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._wetRoads;
    }

    private _coldColorPalette: number;
    get coldColorPalette(): number {
      if (typeof this._coldColorPalette !== 'undefined')
        return this._coldColorPalette;
      let _pos = this._io.pos;
      this._io.seek(13);
      this._coldColorPalette = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._coldColorPalette;
    }

    private _alternative: number;
    get alternative(): number {
      if (typeof this._alternative !== 'undefined')
        return this._alternative;
      let _pos = this._io.pos;
      this._io.seek(14);
      this._alternative = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._alternative;
    }

    private _thunder: number;
    get thunder(): number {
      if (typeof this._thunder !== 'undefined')
        return this._thunder;
      let _pos = this._io.pos;
      this._io.seek(12);
      this._thunder = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._thunder;
    }

    private _rainyWeather: number;
    get rainyWeather(): number {
      if (typeof this._rainyWeather !== 'undefined')
        return this._rainyWeather;
      let _pos = this._io.pos;
      this._io.seek(15);
      this._rainyWeather = (this._io.readU1()) as any
      this._io.seek(_pos);
      return this._rainyWeather;
    }

  }
}

export namespace Event {
  export class GenesysGenOfflineEventAiPlayerInformation {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.OfflineEvent,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.aiPlayerType0xc = (this._io.readU4le()) as any
      this.backUpColour0x10 = (this._io.readU4le()) as any
      this.placement0x14 = (this._io.readU4le()) as any
      this.primaryColour0x18 = (this._io.readU4le()) as any
    }

    baseObject: GenesysObject;
    aiPlayerType0xc: number;
    backUpColour0x10: number;
    placement0x14: number;
    primaryColour0x18: number;
  }
}

export namespace Event {
  export class GenesysGenGameplayCondition {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.Atype,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.stringsPtrArray0xc = (this._io.readU4le()) as any
      this.gameChangerId0x10 = (this._io.readU4le()) as any
      this.referencePtrArray0x14 = (this._io.readU4le()) as any
      this.valuesPtrArray0x18 = (this._io.readU4le()) as any
      this.testTypeVal = (this._io.readU2le()) as any
      this.typeVal = (this._io.readU2le()) as any
      this.arrayCountFor0x14 = (this._io.readU2le()) as any
      this.arrayCountFor0xc = (this._io.readU2le()) as any
      this.arrayCountFor0x18 = (this._io.readU2le()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _kind: Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType;
    get kind(): Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType {
      if (typeof this._kind !== 'undefined')
        return this._kind;
      switch ((this.typeVal as any)) {
        case 0: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "win")) as any
          break;
        }
        case 1: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "lose")) as any
          break;
        }
        case 2: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "special")) as any
          break;
        }
        default: {
          this._kind = (new Event.DisplayType(this._io, this, this._root, "unknown")) as any
          break;
        }
      }
      return this._kind;
    }

    private _testType: Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType;
    get testType(): Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType | Event.DisplayType {
      if (typeof this._testType !== 'undefined')
        return this._testType;
      switch ((this.testTypeVal as any)) {
        case 10: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "StartingScore")) as any
          break;
        }
        case 4: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "CopsWrecked")) as any
          break;
        }
        case 7: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "PlayerWrecked")) as any
          break;
        }
        case 1: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "RacersFinished")) as any
          break;
        }
        case 12: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "AirTime")) as any
          break;
        }
        case 3: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "RacersWrecked")) as any
          break;
        }
        case 5: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "Binding")) as any
          break;
        }
        case 8: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "BeatTime")) as any
          break;
        }
        case 9: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "TopSpeed")) as any
          break;
        }
        case 2: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "Drift")) as any
          break;
        }
        default: {
          this._testType = (new Event.DisplayType(this._io, this, this._root, "unknown")) as any
          break;
        }
      }
      return this._testType;
    }

    private _stringStringsArray0xc: Array<number | undefined> | undefined;
    get stringStringsArray0xc(): Array<number | undefined> | undefined {
      if (typeof this._stringStringsArray0xc !== 'undefined')
        return this._stringStringsArray0xc;
      if ((this.stringsPtrArray0xc as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.stringsPtrArray0xc as any));
        this._stringStringsArray0xc = [];
        for (let i = 0; i < (this.arrayCountFor0xc as any); i++) {
          this._stringStringsArray0xc.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._stringStringsArray0xc;
    }

    private _referenceArray0x14: Array<number | undefined> | undefined;
    get referenceArray0x14(): Array<number | undefined> | undefined {
      if (typeof this._referenceArray0x14 !== 'undefined')
        return this._referenceArray0x14;
      if ((this.referencePtrArray0x14 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.referencePtrArray0x14 as any));
        this._referenceArray0x14 = [];
        for (let i = 0; i < (this.arrayCountFor0xc as any); i++) {
          this._referenceArray0x14.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._referenceArray0x14;
    }

    private _valuesArray0x18: Array<number | undefined> | undefined;
    get valuesArray0x18(): Array<number | undefined> | undefined {
      if (typeof this._valuesArray0x18 !== 'undefined')
        return this._valuesArray0x18;
      if ((this.valuesPtrArray0x18 as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.valuesPtrArray0x18 as any));
        this._valuesArray0x18 = [];
        for (let i = 0; i < (this.arrayCountFor0x18 as any); i++) {
          this._valuesArray0x18.push(this._io.readU4le());
        }
        this._io.seek(_pos);
      }
      return this._valuesArray0x18;
    }

    baseObject: GenesysObject;
    stringsPtrArray0xc: number;
    gameChangerId0x10: number;
    referencePtrArray0x14: number;
    valuesPtrArray0x18: number;

    /**
     * enum_55_31_0f_00
     */
    testTypeVal: number;

    /**
     * enum_68_f1_0e_00
     */
    typeVal: number;
    arrayCountFor0x14: number;
    arrayCountFor0xc: number;
    arrayCountFor0x18: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionSpeedRun {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
      this.routePtrArray0x48 = [];
      for (let i = 0; i < 2; i++) {
        this.routePtrArray0x48.push(new Event.Ptr(this._io, this, this._root, "genesys__gen__challenge__location"));
      }
      this.arrayCountFor0x48 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
    routePtrArray0x48: Array<Event.Ptr>;

    /**
     * always 2
     */
    arrayCountFor0x48: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class GenesysGenOfflineEventCheckpointInfo {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.OfflineEvent,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new GenesysObject(this._io, this, null)) as any
      this.sequence0xc = (this._io.readU4le()) as any
      this.typeVal = (this._io.readU2le()) as any
      this.bool0x12 = (this._io.readU1()) as any
      this.showSplitTime0x13 = (this._io.readU1()) as any
    }

    baseObject: GenesysObject;
    sequence0xc: number;

    /**
     * enum_2b_77_0f_00
     */
    typeVal: number;
    bool0x12: number;
    showSplitTime0x13: number;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionJumpOverPlayers {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
      this.challengeLocationPtr0x48 = (new Event.Ptr(this._io, this, this._root, "genesys__gen__challenge__location")) as any
      this.bool0x4c = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(3)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
    challengeLocationPtr0x48: Event.Ptr;
    bool0x4c: number;
    padding: Uint8Array;
  }
}

export namespace Event {
  export class TypeFinderForGenesysGenChallengeActionActionBase {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Event.Atype,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.obj = (new GenesysObject(this._io, this, null)) as any
    }

    private _actionType: Event.GenesysGenChallengeActionHitTrigger | Event.GenesysGenChallengeActionDoJump | Event.GenesysGenChallengeActionJumpStats | Event.GenesysGenChallengeActionSpeedRun | Event.GenesysGenChallengeActionGetToLocation | Event.GenesysGenChallengeActionSpeedCameraAction | Event.GenesysGenChallengeActionAccumulateDistance | Event.GenesysGenChallengeActionAccumulateNearMisses | Event.GenesysGenChallengeActionActionBase | Event.GenesysGenChallengeActionCarState | Event.GenesysGenChallengeActionJumpOverPlayers | Event.GenesysGenChallengeActionAccumulateTime | Event.GenesysGenChallengeActionCoopAccumulateDistance | Event.GenesysGenChallengeActionAccumulateTakedowns;
    get actionType(): Event.GenesysGenChallengeActionHitTrigger | Event.GenesysGenChallengeActionDoJump | Event.GenesysGenChallengeActionJumpStats | Event.GenesysGenChallengeActionSpeedRun | Event.GenesysGenChallengeActionGetToLocation | Event.GenesysGenChallengeActionSpeedCameraAction | Event.GenesysGenChallengeActionAccumulateDistance | Event.GenesysGenChallengeActionAccumulateNearMisses | Event.GenesysGenChallengeActionActionBase | Event.GenesysGenChallengeActionCarState | Event.GenesysGenChallengeActionJumpOverPlayers | Event.GenesysGenChallengeActionAccumulateTime | Event.GenesysGenChallengeActionCoopAccumulateDistance | Event.GenesysGenChallengeActionAccumulateTakedowns {
      if (typeof this._actionType !== 'undefined')
        return this._actionType;
      let _pos = this._io.pos;
      this._io.seek((this._parent as any)._parent.offset);
      switch ((this.obj as any).muTypeVersion) {
        case 3231281576: {
          this._actionType = (new Event.GenesysGenChallengeActionHitTrigger(this._io, this, this._root)) as any
          break;
        }
        case 1667642657: {
          this._actionType = (new Event.GenesysGenChallengeActionDoJump(this._io, this, this._root)) as any
          break;
        }
        case 3366752106: {
          this._actionType = (new Event.GenesysGenChallengeActionJumpStats(this._io, this, this._root)) as any
          break;
        }
        case 3616318101: {
          this._actionType = (new Event.GenesysGenChallengeActionSpeedRun(this._io, this, this._root)) as any
          break;
        }
        case 3014928914: {
          this._actionType = (new Event.GenesysGenChallengeActionGetToLocation(this._io, this, this._root)) as any
          break;
        }
        case 3823531688: {
          this._actionType = (new Event.GenesysGenChallengeActionSpeedCameraAction(this._io, this, this._root)) as any
          break;
        }
        case 3815813836: {
          this._actionType = (new Event.GenesysGenChallengeActionAccumulateDistance(this._io, this, this._root)) as any
          break;
        }
        case 732433969: {
          this._actionType = (new Event.GenesysGenChallengeActionAccumulateNearMisses(this._io, this, this._root)) as any
          break;
        }
        case 174008559: {
          this._actionType = (new Event.GenesysGenChallengeActionCarState(this._io, this, this._root)) as any
          break;
        }
        case 1058158881: {
          this._actionType = (new Event.GenesysGenChallengeActionJumpOverPlayers(this._io, this, this._root)) as any
          break;
        }
        case 1205733723: {
          this._actionType = (new Event.GenesysGenChallengeActionAccumulateTime(this._io, this, this._root)) as any
          break;
        }
        case 2039183453: {
          this._actionType = (new Event.GenesysGenChallengeActionCoopAccumulateDistance(this._io, this, this._root)) as any
          break;
        }
        case 3616117713: {
          this._actionType = (new Event.GenesysGenChallengeActionAccumulateTakedowns(this._io, this, this._root)) as any
          break;
        }
        default: {
          this._actionType = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
          break;
        }
      }
      this._io.seek(_pos);
      return this._actionType;
    }

    obj: GenesysObject;
  }
}

export namespace Event {
  export class GenesysGenChallengeActionAccumulateTime {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Event,
    ) {

      this._read();
    }

    _read() {
      this.baseObject = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
    }

    baseObject: Event.GenesysGenChallengeActionActionBase;
  }
}

export namespace Event {
  export class Atype {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: Event.Ptr | undefined,
      readonly _root: Event | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      switch ((this.dtype as any)) {
        case "s4": {
          this.data = (this._io.readS4le()) as any
          break;
        }
        case "type_finder_for_genesys__gen__challenge_action__action_base": {
          this.data = (new Event.TypeFinderForGenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__jump_over_players": {
          this.data = (new Event.GenesysGenChallengeActionJumpOverPlayers(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__speed_camera_action": {
          this.data = (new Event.GenesysGenChallengeActionSpeedCameraAction(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__custom_chevron": {
          this.data = (new Event.GenesysGenCustomChevron(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__jump_stats": {
          this.data = (new Event.GenesysGenChallengeActionJumpStats(this._io, this, this._root)) as any
          break;
        }
        case "event_base": {
          this.data = (new Event.EventBase(this._io, this, this._root)) as any
          break;
        }
        case "event_switcher": {
          this.data = (new Event.EventSwitcher(this._io, this, this._root)) as any
          break;
        }
        case "s1": {
          this.data = (this._io.readS1()) as any
          break;
        }
        case "genesys__gen__challenge_action__speed_run": {
          this.data = (new Event.GenesysGenChallengeActionSpeedRun(this._io, this, this._root)) as any
          break;
        }
        case "u4": {
          this.data = (this._io.readU4le()) as any
          break;
        }
        case "genesys__gen__challenge_action__get_to_location": {
          this.data = (new Event.GenesysGenChallengeActionGetToLocation(this._io, this, this._root)) as any
          break;
        }
        case "u2": {
          this.data = (this._io.readU2le()) as any
          break;
        }
        case "genesys__gen__challenge_action__car_state": {
          this.data = (new Event.GenesysGenChallengeActionCarState(this._io, this, this._root)) as any
          break;
        }
        case "s2": {
          this.data = (this._io.readS2le()) as any
          break;
        }
        case "strz": {
          this.data = (KaitaiStream.bytesToStr(this._io.readBytesTerm(0, false, true, true), "ascii")) as any
          break;
        }
        case "genesys__gen__challenge__location": {
          this.data = (new Event.GenesysGenChallengeLocation(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__accumulate_distance": {
          this.data = (new Event.GenesysGenChallengeActionAccumulateDistance(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge__challenge_part": {
          this.data = (new Event.GenesysGenChallengeChallengePart(this._io, this, this._root)) as any
          break;
        }
        case "f4": {
          this.data = (this._io.readF4le()) as any
          break;
        }
        case "u1": {
          this.data = (this._io.readU1()) as any
          break;
        }
        case "genesys__gen__challenge_action__accumulate_takedowns": {
          this.data = (new Event.GenesysGenChallengeActionAccumulateTakedowns(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__hit_trigger": {
          this.data = (new Event.GenesysGenChallengeActionHitTrigger(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__accumulate_near_misses": {
          this.data = (new Event.GenesysGenChallengeActionAccumulateNearMisses(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__coop_accumulate_distance": {
          this.data = (new Event.GenesysGenChallengeActionCoopAccumulateDistance(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__do_jump": {
          this.data = (new Event.GenesysGenChallengeActionDoJump(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__action_base": {
          this.data = (new Event.GenesysGenChallengeActionActionBase(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__chevron": {
          this.data = (new Event.GenesysGenChevron(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__challenge_action__accumulate_time": {
          this.data = (new Event.GenesysGenChallengeActionAccumulateTime(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__gameplay__condition": {
          this.data = (new Event.GenesysGenGameplayCondition(this._io, this, this._root)) as any
          break;
        }
        default: {
          this.data = (new Event.Dummy(this._io, this, this._root)) as any
          break;
        }
      }
    }

    data: number | Event.TypeFinderForGenesysGenChallengeActionActionBase | Event.GenesysGenChallengeActionJumpOverPlayers | Event.GenesysGenChallengeActionSpeedCameraAction | Event.GenesysGenCustomChevron | Event.GenesysGenChallengeActionJumpStats | Event.EventBase | Event.EventSwitcher | number | Event.GenesysGenChallengeActionSpeedRun | number | Event.GenesysGenChallengeActionGetToLocation | number | Event.GenesysGenChallengeActionCarState | number | string | Event.GenesysGenChallengeLocation | Event.GenesysGenChallengeActionAccumulateDistance | Event.GenesysGenChallengeChallengePart | number | number | Event.GenesysGenChallengeActionAccumulateTakedowns | Event.GenesysGenChallengeActionHitTrigger | Event.GenesysGenChallengeActionAccumulateNearMisses | Event.GenesysGenChallengeActionCoopAccumulateDistance | Event.Dummy | Event.GenesysGenChallengeActionDoJump | Event.GenesysGenChallengeActionActionBase | Event.GenesysGenChevron | Event.GenesysGenChallengeActionAccumulateTime | Event.GenesysGenGameplayCondition;
    dtype: string;
  }
}
export namespace Event {
  export enum EConditionType {
    WIN = 0,
    LOSE = 1,
    SPECIAL = 2,
  }
}
export namespace Event {
  export enum EOnlineChallengeFail {
    ALLOW_FAIL = 0,
    NO_FAIL_MAYBE = 1,
  }
}
export namespace Event {
  export enum EOnlineChallengeInvolvement {
    INDIVIDUAL = 0,
    TEAM = 1,
    EVERYONE = 2,
  }
}
export namespace Event {
  export enum EConditionTestType {
    RACERS_FINISHED = 1,
    DRIFT = 2,
    RACERS_WRECKED = 3,
    COPS_WRECKED = 4,
    BINDING = 5,
    PLAYER_WRECKED = 7,
    BEAT_TIME = 8,
    TOP_SPEED = 9,
    STARTING_SCORE = 10,
    AIR_TIME = 12,
  }
}
export namespace Event {
  export enum EParentEventType {
    MP_SPEEDTEST = 0,
    MP_CHALLENGE = 1,
  }
}
export namespace Event {
  export enum EOnlineEliminationType {
    NONE = 0,
    UNK1 = 1,
    UNK2 = 2,
    UNK3 = 3,
    RANDOM = 4,
  }
}
export namespace Event {
  export enum EOnlineChallengeType {
    SPEED_TEST = 0,
    TEAM = 1,
    SOCIAL = 2,
  }
}
