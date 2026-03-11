/*
 * This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
 */
import * as KaitaiStream from 'kaitai-struct/KaitaiStream'
import {GenesysObject} from './genesys-object'

export class Traffic {
  _is_le?: boolean;

  constructor(
    readonly _io: KaitaiStream,
    readonly _parent?: unknown,
    readonly _root?: Traffic,
  ) {
    this._root ??= this;

    this._read();
  }

  _read() {
    this.muDataVersion = (this._io.readU1()) as any
    this.paddingX1 = (this._io.readU1()) as any
    this.muNumHulls = (this._io.readU2le()) as any
    this.muSizeInBytes = (this._io.readU4le()) as any
    this.mpPvsPtr = (new Traffic.Ptr(this._io, this, this._root, "game_traffic_pvs")) as any
    this.mpapHullsPtrPtr = (new Traffic.PtrPtrTable(this._io, this, this._root, "game__traffic__hull", (this.muNumHulls as any))) as any
    this.mpFlowDataPtr = (this._io.readU4le()) as any
    this.muNumFlowData = (this._io.readU2le()) as any
    this.paddingX16 = (this._io.readU2le()) as any
    this.mpFlowTypeDataPtr = (this._io.readU4le()) as any
    this.muNumFlowTypeData = (this._io.readU2le()) as any
    this.paddingX1e = (this._io.readU2le()) as any
    this.miCopFlowTypeData = (this._io.readS4le()) as any
    this.muNumVehicleTypes = (this._io.readU2le()) as any
    this.muNumVehicleAssets = (this._io.readU1()) as any
    this.muNumVehicleTraits = (this._io.readU1()) as any
    this.muNumKillZones = (this._io.readU2le()) as any
    this.muNumKillZoneRegions = (this._io.readU2le()) as any
    this.mpaKillZoneIds = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__kill_zone_id", (this.muNumKillZones as any))) as any
    this.mpaKillZones = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__kill_zone", (this.muNumKillZones as any))) as any
    this.mpaKillZoneRegions = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__kill_zone_region", (this.muNumKillZoneRegions as any))) as any
    this.mpaVehicleTypes = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__vehicle_type_data", (this.muNumVehicleTypes as any))) as any
    this.mpaVehicleTypesUpdate = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__vehicle_type_update_data", (this.muNumVehicleTypes as any))) as any
    this.mpaVehicleAssets = (new Traffic.PtrArray(this._io, this, this._root, "s4", (this.muNumVehicleAssets as any))) as any
    this.mpaVehicleTraits = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__vehicle_traits", (this.muNumVehicleTraits as any))) as any
  }

  private _mpFlowData: Traffic.PtrTable;
  get mpFlowData(): Traffic.PtrTable {
    if (typeof this._mpFlowData !== 'undefined')
      return this._mpFlowData;
    let _pos = this._io.pos;
    this._io.seek((this.mpFlowDataPtr as any));
    this._mpFlowData = (new Traffic.PtrTable(this._io, this, this._root, "handle", (this.muNumFlowData as any))) as any
    this._io.seek(_pos);
    return this._mpFlowData;
  }

  private _mpFlowTypeData: Traffic.PtrTable;
  get mpFlowTypeData(): Traffic.PtrTable {
    if (typeof this._mpFlowTypeData !== 'undefined')
      return this._mpFlowTypeData;
    let _pos = this._io.pos;
    this._io.seek((this.mpFlowTypeDataPtr as any));
    this._mpFlowTypeData = (new Traffic.PtrTable(this._io, this, this._root, "handle", (this.muNumFlowTypeData as any))) as any
    this._io.seek(_pos);
    return this._mpFlowTypeData;
  }

  muDataVersion: number;
  paddingX1: number;
  muNumHulls: number;
  muSizeInBytes: number;
  mpPvsPtr: Traffic.Ptr;
  mpapHullsPtrPtr: Traffic.PtrPtrTable;
  mpFlowDataPtr: number;
  muNumFlowData: number;
  paddingX16: number;
  mpFlowTypeDataPtr: number;
  muNumFlowTypeData: number;
  paddingX1e: number;
  miCopFlowTypeData: number;
  muNumVehicleTypes: number;
  muNumVehicleAssets: number;
  muNumVehicleTraits: number;
  muNumKillZones: number;
  muNumKillZoneRegions: number;
  mpaKillZoneIds: Traffic.PtrArray;
  mpaKillZones: Traffic.PtrArray;
  mpaKillZoneRegions: Traffic.PtrArray;
  mpaVehicleTypes: Traffic.PtrArray;
  mpaVehicleTypesUpdate: Traffic.PtrArray;
  mpaVehicleAssets: Traffic.PtrArray;
  mpaVehicleTraits: Traffic.PtrArray;
}

export namespace Traffic {
  export class Vector2 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.x = (this._io.readF4le()) as any
      this.y = (this._io.readF4le()) as any
    }

    x: number;
    y: number;
  }
}

export namespace Traffic {
  export class VpuVector3 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Traffic,
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

export namespace Traffic {
  export class PtrPtr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Traffic | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _ptr: Traffic.Ptr | undefined;
    get ptr(): Traffic.Ptr | undefined {
      if (typeof this._ptr !== 'undefined')
        return this._ptr;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptr = (new Traffic.Ptr(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._ptr;
    }

    offset: number;
    dtype: string;
  }
}

export namespace Traffic {
  export class PtrArray {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Traffic | undefined,
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

    private _entries: Array<Traffic.Atype>;
    get entries(): Array<Traffic.Atype> {
      if (typeof this._entries !== 'undefined')
        return this._entries;
      let _pos = this._io.pos;
      this._io.seek((this.offset as any));
      this._entries = [];
      for (let i = 0; i < (this.amt as any); i++) {
        this._entries.push(new Traffic.Atype(this._io, this, this._root, (this.dtype as any)));
      }
      this._io.seek(_pos);
      return this._entries;
    }

    offset: number;
    dtype: string;
    amt: number;
  }
}

export namespace Traffic {
  export class GameTrafficPvscellHullpvs {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.GameTrafficPvscell,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.hullPvs = [];
      for (let i = 0; i < 9; i++) {
        this.hullPvs.push(this._io.readU2le());
      }
      this.muLength = (this._io.readU4le()) as any
    }

    hullPvs: Array<number>;
    muLength: number;
  }
}

export namespace Traffic {
  export class PtrPtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: Traffic | undefined,
      readonly _root: Traffic | undefined,
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

    private _ptrTable: Traffic.PtrTable | undefined;
    get ptrTable(): Traffic.PtrTable | undefined {
      if (typeof this._ptrTable !== 'undefined')
        return this._ptrTable;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptrTable = (new Traffic.PtrTable(this._io, this, this._root, (this.dtype as any), (this.len as any))) as any
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

export namespace Traffic {
  export class GenesysGenTrafficFlowTypeTrafficFlowTypeInternal {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.baseClass = (new GenesysObject(this._io, this, undefined)) as any
      this.mTrafficVehicleType = (new GenesysObject.CgsResourceHandle(this._io, this, this._root)) as any
      this.miColour = (new Traffic.CgsCoreUniqueId(this._io, this, this._root)) as any
      this.miGameChangerId = (new Traffic.CgsCoreUniqueId(this._io, this, this._root)) as any
      this.mfProportion = (this._io.readF4le()) as any
    }

    baseClass: GenesysObject;
    mTrafficVehicleType: GenesysObject.CgsResourceHandle;
    miColour: Traffic.CgsCoreUniqueId;
    miGameChangerId: Traffic.CgsCoreUniqueId;
    mfProportion: number;
  }
}

export namespace Traffic {
  export class GameTrafficVehicleTypeData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muTrailerFlowTypeId = (this._io.readU2le()) as any
      this.mxVehicleFlags = (this._io.readU1()) as any
      this.muVehicleClass = (this._io.readU1()) as any
      this.muInitialDirt = (this._io.readU1()) as any
      this.muAssetId = (this._io.readU1()) as any
      this.muTraitsId = (this._io.readU1()) as any
    }

    muTrailerFlowTypeId: number;
    mxVehicleFlags: number;
    muVehicleClass: number;
    muInitialDirt: number;
    muAssetId: number;
    muTraitsId: number;
  }
}

export namespace Traffic {
  export class GameTrafficSectionSpan {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muMaxVehicles = (this._io.readU2le()) as any
      this.mfMaxVehicleRecip = (this._io.readF4le()) as any
    }

    muMaxVehicles: number;
    mfMaxVehicleRecip: number;
  }
}

export namespace Traffic {
  export class GameTrafficSection {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muRungOffset = (this._io.readU4le()) as any
      this.muNumRungs = (this._io.readU1()) as any
      this.muStopLineOffset = (this._io.readU1()) as any
      this.muNumStopLines = (this._io.readU1()) as any
      this.muSpanIndex = (this._io.readU1()) as any
      this.mauForwardHulls = [];
      for (let i = 0; i < 3; i++) {
        this.mauForwardHulls.push(this._io.readU2le());
      }
      this.mauBackwardHulls = [];
      for (let i = 0; i < 3; i++) {
        this.mauBackwardHulls.push(this._io.readU2le());
      }
      this.mauForwardSections = [];
      for (let i = 0; i < 3; i++) {
        this.mauForwardSections.push(this._io.readU1());
      }
      this.mauBackwardSections = [];
      for (let i = 0; i < 3; i++) {
        this.mauBackwardSections.push(this._io.readU1());
      }
      this.muNeighbourOffset = (this._io.readU2le()) as any
      this.muLeftNeighbourCount = (this._io.readU1()) as any
      this.muRightNeighbourCount = (this._io.readU1()) as any
      this.paddingX1e = (this._io.readU2le()) as any
      this.mfLength = (this._io.readF4le()) as any
      this.muFlowDataIndex = (this._io.readU1()) as any
      this.muFlowTypeDataIndex = (this._io.readU1()) as any
      this.paddingX26 = [];
      for (let i = 0; i < 10; i++) {
        this.paddingX26.push(this._io.readU1());
      }
    }

    muRungOffset: number;
    muNumRungs: number;
    muStopLineOffset: number;
    muNumStopLines: number;
    muSpanIndex: number;
    mauForwardHulls: Array<number>;
    mauBackwardHulls: Array<number>;
    mauForwardSections: Array<number>;
    mauBackwardSections: Array<number>;
    muNeighbourOffset: number;
    muLeftNeighbourCount: number;
    muRightNeighbourCount: number;
    paddingX1e: number;
    mfLength: number;
    muFlowDataIndex: number;
    muFlowTypeDataIndex: number;
    paddingX26: Array<number>;
  }
}

export namespace Traffic {
  export class GameTrafficPvs {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muNumCells = (this._io.readU4le()) as any
      this.mpaCells = (new Traffic.Ptr(this._io, this, this._root, "game_traffic_pvscell")) as any
    }

    muNumCells: number;
    mpaCells: Traffic.Ptr;
  }
}

export namespace Traffic {
  export class VpuVector2 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.x = (this._io.readF4le()) as any
      this.y = (this._io.readF4le()) as any
      this.unused1 = (this._io.readF4le()) as any
      this.unused2 = (this._io.readF4le()) as any
    }

    x: number;
    y: number;
    unused1: number;
    unused2: number;
  }
}

export namespace Traffic {
  export class PtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Traffic | undefined,
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
        this.entries.push(new Traffic.Ptr(this._io, this, this._root, (this.dtype as any)));
      }
    }

    entries: Array<Traffic.Ptr>;
    dtype: string;
    amt: number;
  }
}

export namespace Traffic {
  export class Dummy {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
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

export namespace Traffic {
  export class Vector4 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.x = (this._io.readF4le()) as any
      this.y = (this._io.readF4le()) as any
      this.z = (this._io.readF4le()) as any
      this.w = (this._io.readF4le()) as any
    }

    x: number;
    y: number;
    z: number;
    w: number;
  }
}

export namespace Traffic {
  export class GameTrafficStopLine {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muParamFixed = (this._io.readU2le()) as any
    }

    muParamFixed: number;
  }
}

export namespace Traffic {
  export class GameTrafficKillZoneRegion {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muHull = (this._io.readU2le()) as any
      this.muSection = (this._io.readU1()) as any
      this.muStartRung = (this._io.readU1()) as any
      this.muEndRung = (this._io.readU1()) as any
      this.paddingX5 = (this._io.readU1()) as any
    }

    muHull: number;
    muSection: number;
    muStartRung: number;
    muEndRung: number;
    paddingX5: number;
  }
}

export namespace Traffic {
  export class GenesysGenTrafficFlow {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.baseClass = (new GenesysObject(this._io, this, undefined)) as any
      this.mFlowType = (new GenesysObject.CgsResourceHandle(this._io, this, this._root)) as any
      this.miGameChangerId = (new Traffic.CgsCoreUniqueId(this._io, this, this._root)) as any
      this.mfChangeLeftProbability = (this._io.readF4le()) as any
      this.mfChangeRightProbability = (this._io.readF4le()) as any
      this.mfDensity = (this._io.readF4le()) as any
      this.mfSpeed = (this._io.readF4le()) as any
      this.mfTurnLeftProbability = (this._io.readF4le()) as any
      this.mfTurnRightProbability = (this._io.readF4le()) as any
    }

    baseClass: GenesysObject;
    mFlowType: GenesysObject.CgsResourceHandle;
    miGameChangerId: Traffic.CgsCoreUniqueId;
    mfChangeLeftProbability: number;
    mfChangeRightProbability: number;
    mfDensity: number;
    mfSpeed: number;
    mfTurnLeftProbability: number;
    mfTurnRightProbability: number;
  }
}

export namespace Traffic {
  export class GameTrafficKillZone {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muOffset = (this._io.readU2le()) as any
      this.muCount = (this._io.readU1()) as any
      this.paddingX3 = (this._io.readU1()) as any
    }

    muOffset: number;
    muCount: number;
    paddingX3: number;
  }
}

export namespace Traffic {
  export class GameTrafficKillZoneId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.id = (this._io.readU8le()) as any
    }

    id: number;
  }
}

export namespace Traffic {
  export class GenesysGenTrafficFlowType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.baseClass = (new GenesysObject(this._io, this, undefined)) as any
      this.miGameChangerId = (new Traffic.CgsCoreUniqueId(this._io, this, this._root)) as any
      this.mpaFlowType = (new Traffic.Ptr(this._io, this, this._root, "genesys__gen__traffic_flow_type__traffic_flow_type_internal")) as any
      this.muFlowTypeCount = (this._io.readU2le()) as any
      this.trafficFlowTypeWastedSpace = [];
      for (let i = 0; i < 2; i++) {
        this.trafficFlowTypeWastedSpace.push(this._io.readU2le());
      }
    }

    baseClass: GenesysObject;
    miGameChangerId: Traffic.CgsCoreUniqueId;
    mpaFlowType: Traffic.Ptr;
    muFlowTypeCount: number;
    trafficFlowTypeWastedSpace: Array<number>;
  }
}

export namespace Traffic {
  export class GenesysGenTrafficVehicleTraits {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.baseClass = (new GenesysObject(this._io, this, undefined)) as any
      this.miGameChangerId = (new Traffic.CgsCoreUniqueId(this._io, this, this._root)) as any
      this.mfAcceleration = (this._io.readF4le()) as any
      this.meScale = (this._io.readS2le()) as any
      this.trafficVehicleTraitsWastedSpace = [];
      for (let i = 0; i < 2; i++) {
        this.trafficVehicleTraitsWastedSpace.push(this._io.readU1());
      }
    }

    baseClass: GenesysObject;
    miGameChangerId: Traffic.CgsCoreUniqueId;
    mfAcceleration: number;
    meScale: number;
    trafficVehicleTraitsWastedSpace: Array<number>;
  }
}

export namespace Traffic {
  export class GenesysGenTrafficVehicle {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.baseClass = (new GenesysObject(this._io, this, undefined)) as any
      this.paddingXc = (this._io.readU4le()) as any
      this.mPositivePitchNegativePitchYawRoll = (new Traffic.Vector4(this._io, this, this._root)) as any
      this.mTrailer = (new GenesysObject.CgsResourceHandle(this._io, this, this._root)) as any
      this.mTraits = (new GenesysObject.CgsResourceHandle(this._io, this, this._root)) as any
      this.miGameChangerId = (new Traffic.CgsCoreUniqueId(this._io, this, this._root)) as any
      this.miVehicleComponent = (new Traffic.CgsCoreUniqueId(this._io, this, this._root)) as any
      this.unk1 = (this._io.readU4le()) as any
      this.unk2 = (this._io.readU1()) as any
      this.mbUseThickWheelSmoke = (this._io.readU1()) as any
      this.trafficVehicleWastedSpace = [];
      for (let i = 0; i < 2; i++) {
        this.trafficVehicleWastedSpace.push(this._io.readU1());
      }
    }

    baseClass: GenesysObject;
    paddingXc: number;
    mPositivePitchNegativePitchYawRoll: Traffic.Vector4;
    mTrailer: GenesysObject.CgsResourceHandle;
    mTraits: GenesysObject.CgsResourceHandle;
    miGameChangerId: Traffic.CgsCoreUniqueId;
    miVehicleComponent: Traffic.CgsCoreUniqueId;
    unk1: number;
    unk2: number;
    mbUseThickWheelSmoke: number;
    trafficVehicleWastedSpace: Array<number>;
  }
}

export namespace Traffic {
  export class VpuMatrix44affine {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.GameTrafficStaticTrafficVehicle,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.xAxis = (new Traffic.VpuVector3(this._io, this, this._root)) as any
      this.yAxis = (new Traffic.VpuVector3(this._io, this, this._root)) as any
      this.zAxis = (new Traffic.VpuVector3(this._io, this, this._root)) as any
      this.wAxis = (new Traffic.VpuVector3(this._io, this, this._root)) as any
    }

    xAxis: Traffic.VpuVector3;
    yAxis: Traffic.VpuVector3;
    zAxis: Traffic.VpuVector3;
    wAxis: Traffic.VpuVector3;
  }
}

export namespace Traffic {
  export class GameTrafficStaticTrafficVehicle {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.mTransform = (new Traffic.VpuMatrix44affine(this._io, this, this._root)) as any
      this.mFlowTypeId = (this._io.readU2le()) as any
      this.mExistsAtAllChance = (this._io.readU1()) as any
      this.muFlags = (this._io.readU1()) as any
      this.padding44 = [];
      for (let i = 0; i < 12; i++) {
        this.padding44.push(this._io.readU1());
      }
    }

    mTransform: Traffic.VpuMatrix44affine;
    mFlowTypeId: number;
    mExistsAtAllChance: number;
    muFlags: number;
    padding44: Array<number>;
  }
}

export namespace Traffic {
  export class GameTrafficVehicleTypeUpdateData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.mfWheelRadius = (this._io.readF4le()) as any
      this.mfSuspensionRoll = (this._io.readF4le()) as any
      this.mfSuspensionPitch = (this._io.readF4le()) as any
      this.mfSuspensionTravel = (this._io.readF4le()) as any
      this.mfMass = (this._io.readF4le()) as any
    }

    mfWheelRadius: number;
    mfSuspensionRoll: number;
    mfSuspensionPitch: number;
    mfSuspensionTravel: number;
    mfMass: number;
  }
}

export namespace Traffic {
  export class GameTrafficTrafficLightController {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.GameTrafficJunctionLogicBox,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.maPlacementIds = [];
      for (let i = 0; i < 2; i++) {
        this.maPlacementIds.push(new Traffic.CgsCoreUniqueId(this._io, this, this._root));
      }
      this.mauTrafficLightIds = [];
      for (let i = 0; i < 2; i++) {
        this.mauTrafficLightIds.push(this._io.readU2le());
      }
      this.mauStopLineIds = [];
      for (let i = 0; i < 6; i++) {
        this.mauStopLineIds.push(this._io.readU1());
      }
      this.mauStopLineHulls = [];
      for (let i = 0; i < 6; i++) {
        this.mauStopLineHulls.push(this._io.readU2le());
      }
      this.muNumStopLines = (this._io.readU1()) as any
      this.muNumTrafficLights = (this._io.readU1()) as any
    }

    maPlacementIds: Array<Traffic.CgsCoreUniqueId>;
    mauTrafficLightIds: Array<number>;
    mauStopLineIds: Array<number>;
    mauStopLineHulls: Array<number>;
    muNumStopLines: number;
    muNumTrafficLights: number;
  }
}

export namespace Traffic {
  export class GameTrafficNeighbour {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muSection = (this._io.readU1()) as any
      this.muSharedLength = (this._io.readU1()) as any
      this.muOurStartRung = (this._io.readU1()) as any
      this.muTheirStartRung = (this._io.readU1()) as any
    }

    muSection: number;
    muSharedLength: number;
    muOurStartRung: number;
    muTheirStartRung: number;
  }
}

export namespace Traffic {
  export class GameTrafficHull {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muNumSections = (this._io.readU1()) as any
      this.muNumSectionSpans = (this._io.readU1()) as any
      this.muNumJunctions = (this._io.readU1()) as any
      this.muNumStoplines = (this._io.readU1()) as any
      this.muNumNeighbours = (this._io.readU1()) as any
      this.muNumStaticTraffic = (this._io.readU1()) as any
      this.muNumRungs = (this._io.readU2le()) as any
      this.muFirstTrafficLight = (this._io.readU2le()) as any
      this.muLastTrafficLight = (this._io.readU2le()) as any
      this.muNumLightTriggers = (this._io.readU1()) as any
      this.muNumLightTriggersStartData = (this._io.readU1()) as any
      this.muNumVehicleAssets = (this._io.readU1()) as any
      this.paddingXf = (this._io.readU1()) as any
      this.mpaSections = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__section", (this.muNumSections as any))) as any
      this.mpaRungs = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__lane_rung", (this.muNumRungs as any))) as any
      this.mpafCumulativeRungLengths = (new Traffic.PtrArray(this._io, this, this._root, "f4", (this.muNumRungs as any))) as any
      this.mpaNeighbourData = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__neighbour", (this.muNumNeighbours as any))) as any
      this.mpaSectionSpans = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__section_span", (this.muNumSectionSpans as any))) as any
      this.mpaStaticTrafficVehicles = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__static_traffic_vehicle", (this.muNumStaticTraffic as any))) as any
      this.mpaJunctions = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__junction_logic_box", (this.muNumJunctions as any))) as any
      this.mpaStopLines = (new Traffic.PtrArray(this._io, this, this._root, "game__traffic__stop_line", (this.muNumStoplines as any))) as any
      this.mauVehicleAssets = [];
      for (let i = 0; i < 12; i++) {
        this.mauVehicleAssets.push(this._io.readU1());
      }
      this.paddingX3c = (this._io.readU4le()) as any
    }

    muNumSections: number;
    muNumSectionSpans: number;
    muNumJunctions: number;
    muNumStoplines: number;
    muNumNeighbours: number;
    muNumStaticTraffic: number;
    muNumRungs: number;
    muFirstTrafficLight: number;
    muLastTrafficLight: number;
    muNumLightTriggers: number;
    muNumLightTriggersStartData: number;
    muNumVehicleAssets: number;
    paddingXf: number;
    mpaSections: Traffic.PtrArray;
    mpaRungs: Traffic.PtrArray;
    mpafCumulativeRungLengths: Traffic.PtrArray;
    mpaNeighbourData: Traffic.PtrArray;
    mpaSectionSpans: Traffic.PtrArray;
    mpaStaticTrafficVehicles: Traffic.PtrArray;
    mpaJunctions: Traffic.PtrArray;
    mpaStopLines: Traffic.PtrArray;
    mauVehicleAssets: Array<number>;
    paddingX3c: number;
  }
}

export namespace Traffic {
  export class CgsCoreUniqueId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.miValue = (this._io.readS4le()) as any
    }

    miValue: number;
  }
}

export namespace Traffic {
  export class Ptr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Traffic | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _data: Traffic.Atype | undefined;
    get data(): Traffic.Atype | undefined {
      if (typeof this._data !== 'undefined')
        return this._data;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._data = (new Traffic.Atype(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._data;
    }

    offset: number;
    dtype: string;
  }
}

export namespace Traffic {
  export class GameTrafficLaneRung {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.maPoints = [];
      for (let i = 0; i < 2; i++) {
        this.maPoints.push(new Traffic.VpuVector3(this._io, this, this._root));
      }
    }

    maPoints: Array<Traffic.VpuVector3>;
  }
}

export namespace Traffic {
  export class GameTrafficVehicleTraits {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.mfSwervingAmountModifier = (this._io.readF4le()) as any
      this.mfAcceleration = (this._io.readF4le()) as any
      this.muCuttingUpChance = (this._io.readU1()) as any
      this.muTailgatingChance = (this._io.readU1()) as any
      this.muPatience = (this._io.readU1()) as any
      this.muTantrumAttackCumProb = (this._io.readU1()) as any
      this.muTantrumStopCumProb = (this._io.readU1()) as any
      this.paddingXd = [];
      for (let i = 0; i < 3; i++) {
        this.paddingXd.push(this._io.readU1());
      }
    }

    mfSwervingAmountModifier: number;
    mfAcceleration: number;
    muCuttingUpChance: number;
    muTailgatingChance: number;
    muPatience: number;
    muTantrumAttackCumProb: number;
    muTantrumStopCumProb: number;
    paddingXd: Array<number>;
  }
}

export namespace Traffic {
  export class GameTrafficJunctionLogicBox {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.muId = (this._io.readU4le()) as any
      this.mauStateTimings = [];
      for (let i = 0; i < 16; i++) {
        this.mauStateTimings.push(this._io.readU2le());
      }
      this.mauStoppedLightStates = [];
      for (let i = 0; i < 16; i++) {
        this.mauStoppedLightStates.push(this._io.readU1());
      }
      this.muNumStates = (this._io.readU1()) as any
      this.muNumLights = (this._io.readU1()) as any
      this.paddingX36 = (this._io.readU2le()) as any
      this.maTrafficLightControllers = [];
      for (let i = 0; i < 8; i++) {
        this.maTrafficLightControllers.push(new Traffic.GameTrafficTrafficLightController(this._io, this, this._root));
      }
      this.paddingX140 = [];
      for (let i = 0; i < 8; i++) {
        this.paddingX140.push(this._io.readU1());
      }
      this.mPosition = (new Traffic.VpuVector3(this._io, this, this._root)) as any
    }

    muId: number;
    mauStateTimings: Array<number>;
    mauStoppedLightStates: Array<number>;
    muNumStates: number;
    muNumLights: number;
    paddingX36: number;
    maTrafficLightControllers: Array<Traffic.GameTrafficTrafficLightController>;
    paddingX140: Array<number>;
    mPosition: Traffic.VpuVector3;
  }
}

export namespace Traffic {
  export class Vector3 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.x = (this._io.readF4le()) as any
      this.y = (this._io.readF4le()) as any
      this.z = (this._io.readF4le()) as any
    }

    x: number;
    y: number;
    z: number;
  }
}

export namespace Traffic {
  export class GameTrafficPvscell {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.Atype,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.mpPoints = (new Traffic.Ptr(this._io, this, this._root, "vpu_vector2")) as any
      this.mHullPvs = (new Traffic.GameTrafficPvscellHullpvs(this._io, this, this._root)) as any
      this.paddingX1c = [];
      for (let i = 0; i < 4; i++) {
        this.paddingX1c.push(this._io.readU1());
      }
      this.mAabb = (new Traffic.CgsGeometricAxisAlignedBox(this._io, this, this._root)) as any
      this.miId = (this._io.readS4le()) as any
      this.miDistrictId = (this._io.readS4le()) as any
      this.miNumPoints = (this._io.readS2le()) as any
      this.paddingX4a = [];
      for (let i = 0; i < 6; i++) {
        this.paddingX4a.push(this._io.readU1());
      }
    }

    mpPoints: Traffic.Ptr;
    mHullPvs: Traffic.GameTrafficPvscellHullpvs;
    paddingX1c: Array<number>;
    mAabb: Traffic.CgsGeometricAxisAlignedBox;
    miId: number;
    miDistrictId: number;
    miNumPoints: number;
    paddingX4a: Array<number>;
  }
}

export namespace Traffic {
  export class CgsGeometricAxisAlignedBox {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Traffic.GameTrafficPvscell,
      readonly _root?: Traffic,
    ) {

      this._read();
    }

    _read() {
      this.mMin = (new Traffic.VpuVector3(this._io, this, this._root)) as any
      this.mMax = (new Traffic.VpuVector3(this._io, this, this._root)) as any
    }

    mMin: Traffic.VpuVector3;
    mMax: Traffic.VpuVector3;
  }
}

export namespace Traffic {
  export class Atype {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Traffic | undefined,
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
        case "game__traffic__vehicle_traits": {
          this.data = (new Traffic.GameTrafficVehicleTraits(this._io, this, this._root)) as any
          break;
        }
        case "game_traffic_pvs": {
          this.data = (new Traffic.GameTrafficPvs(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__kill_zone": {
          this.data = (new Traffic.GameTrafficKillZone(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__stop_line": {
          this.data = (new Traffic.GameTrafficStopLine(this._io, this, this._root)) as any
          break;
        }
        case "s1": {
          this.data = (this._io.readS1()) as any
          break;
        }
        case "u4": {
          this.data = (this._io.readU4le()) as any
          break;
        }
        case "game_traffic_pvscell": {
          this.data = (new Traffic.GameTrafficPvscell(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__neighbour": {
          this.data = (new Traffic.GameTrafficNeighbour(this._io, this, this._root)) as any
          break;
        }
        case "u2": {
          this.data = (this._io.readU2le()) as any
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
        case "game__traffic__hull": {
          this.data = (new Traffic.GameTrafficHull(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__vehicle_type_data": {
          this.data = (new Traffic.GameTrafficVehicleTypeData(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__section": {
          this.data = (new Traffic.GameTrafficSection(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__static_traffic_vehicle": {
          this.data = (new Traffic.GameTrafficStaticTrafficVehicle(this._io, this, this._root)) as any
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
        case "game__traffic__kill_zone_region": {
          this.data = (new Traffic.GameTrafficKillZoneRegion(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__vehicle_type_update_data": {
          this.data = (new Traffic.GameTrafficVehicleTypeUpdateData(this._io, this, this._root)) as any
          break;
        }
        case "vpu_vector2": {
          this.data = (new Traffic.VpuVector2(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__junction_logic_box": {
          this.data = (new Traffic.GameTrafficJunctionLogicBox(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__section_span": {
          this.data = (new Traffic.GameTrafficSectionSpan(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__lane_rung": {
          this.data = (new Traffic.GameTrafficLaneRung(this._io, this, this._root)) as any
          break;
        }
        case "genesys__gen__traffic_flow_type__traffic_flow_type_internal": {
          this.data = (new Traffic.GenesysGenTrafficFlowTypeTrafficFlowTypeInternal(this._io, this, this._root)) as any
          break;
        }
        case "game__traffic__kill_zone_id": {
          this.data = (new Traffic.GameTrafficKillZoneId(this._io, this, this._root)) as any
          break;
        }
        default: {
          this.data = (new Traffic.Dummy(this._io, this, this._root)) as any
          break;
        }
      }
    }

    data: number | Traffic.GameTrafficVehicleTraits | Traffic.GameTrafficPvs | Traffic.GameTrafficKillZone | Traffic.GameTrafficStopLine | number | number | Traffic.GameTrafficPvscell | Traffic.GameTrafficNeighbour | number | number | string | Traffic.GameTrafficHull | Traffic.GameTrafficVehicleTypeData | Traffic.GameTrafficSection | Traffic.GameTrafficStaticTrafficVehicle | number | number | Traffic.GameTrafficKillZoneRegion | Traffic.GameTrafficVehicleTypeUpdateData | Traffic.VpuVector2 | Traffic.GameTrafficJunctionLogicBox | Traffic.GameTrafficSectionSpan | Traffic.Dummy | Traffic.GameTrafficLaneRung | Traffic.GenesysGenTrafficFlowTypeTrafficFlowTypeInternal | Traffic.GameTrafficKillZoneId;
    dtype: string;
  }
}
export namespace Traffic {
  export enum GenesysGenTrafficvehicletraitsEsize {
    E_SIZE_INVALID = -1,
    E_SIZE_SMALL = 0,
    E_SIZE_MEDIUM = 1,
    E_SIZE_LARGE = 2,
  }
}
export namespace Traffic {
  export enum GameTrafficStatictrafficvehicleStatictrafficflags {
    E_STATIC_TRAFFIC_ON_RACING_LINE = 1,
  }
}
