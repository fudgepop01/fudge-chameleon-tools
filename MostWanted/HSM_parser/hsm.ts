/*
 * This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
 */
import KaitaiStream from 'kaitai-struct/KaitaiStream'

export class Hsm {
  _is_le?: boolean;

  constructor(
    readonly _io: KaitaiStream,
    readonly _parent?: unknown,
    readonly _root?: Hsm,
  ) {
    this._root ??= this;

    this._read();
  }

  _read() {
    this.miVersionNumber0x0 = (this._io.readS4le()) as any
    this.ptrMaTopStateDefinitions0x4 = (this._io.readU4le()) as any
    this.miNumTopStateDefinitions0x8 = (this._io.readS4le()) as any
    this.ptrMaStateDefinitions0xc = (this._io.readU4le()) as any
    this.miNumStateDefinitions0x10 = (this._io.readS4le()) as any
    this.ptrMaDataDefinitions0x14 = (this._io.readU4le()) as any
    this.miNumDataDefinitions0x18 = (this._io.readS4le()) as any
    this.ptrMaBehaviourInterfaces0x1c = (this._io.readU4le()) as any
    this.miNumBehaviourInterfaces0x20 = (this._io.readS4le()) as any
  }

  private _topStateDefinitions: Array<Hsm.GameGameLogicHsmDataHsmTopStateDefinition>;
  get topStateDefinitions(): Array<Hsm.GameGameLogicHsmDataHsmTopStateDefinition> {
    if (typeof this._topStateDefinitions !== 'undefined')
      return this._topStateDefinitions;
    let _pos = this._io.pos;
    this._io.seek((this.ptrMaTopStateDefinitions0x4 as any));
    this._topStateDefinitions = [];
    for (let i = 0; i < (this.miNumTopStateDefinitions0x8 as any); i++) {
      this._topStateDefinitions.push(new Hsm.GameGameLogicHsmDataHsmTopStateDefinition(this._io, this, this._root));
    }
    this._io.seek(_pos);
    return this._topStateDefinitions;
  }

  private _stateDefinitions: Array<Hsm.GameGameLogicHsmDataHsmStateDefinition>;
  get stateDefinitions(): Array<Hsm.GameGameLogicHsmDataHsmStateDefinition> {
    if (typeof this._stateDefinitions !== 'undefined')
      return this._stateDefinitions;
    let _pos = this._io.pos;
    this._io.seek((this.ptrMaStateDefinitions0xc as any));
    this._stateDefinitions = [];
    for (let i = 0; i < (this.miNumStateDefinitions0x10 as any); i++) {
      this._stateDefinitions.push(new Hsm.GameGameLogicHsmDataHsmStateDefinition(this._io, this, this._root));
    }
    this._io.seek(_pos);
    return this._stateDefinitions;
  }

  private _dataDefinitions: Array<Hsm.GameGameLogicHsmDataHsmDataDefinition>;
  get dataDefinitions(): Array<Hsm.GameGameLogicHsmDataHsmDataDefinition> {
    if (typeof this._dataDefinitions !== 'undefined')
      return this._dataDefinitions;
    let _pos = this._io.pos;
    this._io.seek((this.ptrMaDataDefinitions0x14 as any));
    this._dataDefinitions = [];
    for (let i = 0; i < (this.miNumDataDefinitions0x18 as any); i++) {
      this._dataDefinitions.push(new Hsm.GameGameLogicHsmDataHsmDataDefinition(this._io, this, this._root));
    }
    this._io.seek(_pos);
    return this._dataDefinitions;
  }

  private _behaviourInterfaces: Array<Hsm.GameGameLogicHsmDataHsmBehaviourInterface>;
  get behaviourInterfaces(): Array<Hsm.GameGameLogicHsmDataHsmBehaviourInterface> {
    if (typeof this._behaviourInterfaces !== 'undefined')
      return this._behaviourInterfaces;
    let _pos = this._io.pos;
    this._io.seek((this.ptrMaBehaviourInterfaces0x1c as any));
    this._behaviourInterfaces = [];
    for (let i = 0; i < (this.miNumBehaviourInterfaces0x20 as any); i++) {
      this._behaviourInterfaces.push(new Hsm.GameGameLogicHsmDataHsmBehaviourInterface(this._io, this, this._root));
    }
    this._io.seek(_pos);
    return this._behaviourInterfaces;
  }


  /**
   * Version number _ 3
   */
  miVersionNumber0x0: number;

  /**
   * Top-level state definitions
   */
  ptrMaTopStateDefinitions0x4: number;

  /**
   * Number of top-level state definitions
   */
  miNumTopStateDefinitions0x8: number;

  /**
   * State definitions
   */
  ptrMaStateDefinitions0xc: number;

  /**
   * Number of state definitions
   */
  miNumStateDefinitions0x10: number;

  /**
   * Data definitions
   */
  ptrMaDataDefinitions0x14: number;

  /**
   * Number of data definitions
   */
  miNumDataDefinitions0x18: number;

  /**
   * Behaviour interfaces
   */
  ptrMaBehaviourInterfaces0x1c: number;

  /**
   * Number of behaviour interfaces
   */
  miNumBehaviourInterfaces0x20: number;
}

export namespace Hsm {
  export class GameGameLogicStateBehaviourId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.stateBehaviourId = (this._io.readS4le()) as any
    }


    /**
     * JAMCRC hash of behaviour ID
     * ID matches decoded HSMBehaviourInterface__mBehaviourInterfaceID
     */
    stateBehaviourId: number;
  }
}

export namespace Hsm {
  export class DisplayType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Hsm | undefined,
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

export namespace Hsm {
  export class PtrPtr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Hsm | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _ptr: Hsm.Ptr | undefined;
    get ptr(): Hsm.Ptr | undefined {
      if (typeof this._ptr !== 'undefined')
        return this._ptr;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptr = (new Hsm.Ptr(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._ptr;
    }

    offset: number;
    dtype: string;
  }
}

export namespace Hsm {
  export class GameGameLogicDataDefinitionId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Hsm.GameGameLogicHsmDataHsmDataDefinition,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.dataDefinitionId = (this._io.readS4le()) as any
    }


    /**
     * Unique ID
     */
    dataDefinitionId: number;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmChildExitPointData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.mParentExitPointId0x0 = (new Hsm.GameGameLogicStateExitPointId(this._io, this, this._root)) as any
      this.mChildExitPointId0x8 = (new Hsm.GameGameLogicStateExitPointId(this._io, this, this._root)) as any
      this.muAction0x10 = (this._io.readU1()) as any
      this.muNumChildren0x11 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
      this.ptrMaChildSpawnData0x14 = (this._io.readU4le()) as any
    }

    private _childSpawnData: Array<Hsm.GameGameLogicHsmDataHsmStateSpawnData>;
    get childSpawnData(): Array<Hsm.GameGameLogicHsmDataHsmStateSpawnData> {
      if (typeof this._childSpawnData !== 'undefined')
        return this._childSpawnData;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaChildSpawnData0x14 as any));
      this._childSpawnData = [];
      for (let i = 0; i < (this.muNumChildren0x11 as any); i++) {
        this._childSpawnData.push(new Hsm.GameGameLogicHsmDataHsmStateSpawnData(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._childSpawnData;
    }


    /**
     * Parent exit point ID
     */
    mParentExitPointId0x0: Hsm.GameGameLogicStateExitPointId;

    /**
     * Child exit point ID
     */
    mChildExitPointId0x8: Hsm.GameGameLogicStateExitPointId;

    /**
     * Action; See EHSMAction
     */
    muAction0x10: number;

    /**
     * Number of children
     */
    muNumChildren0x11: number;
    padding: Uint8Array;

    /**
     * Child state spawn data
     */
    ptrMaChildSpawnData0x14: number;
  }
}

export namespace Hsm {
  export class PtrArray {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Hsm | undefined,
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

    private _entries: Array<Hsm.Atype>;
    get entries(): Array<Hsm.Atype> {
      if (typeof this._entries !== 'undefined')
        return this._entries;
      let _pos = this._io.pos;
      this._io.seek((this.offset as any));
      this._entries = [];
      for (let i = 0; i < (this.amt as any); i++) {
        this._entries.push(new Hsm.Atype(this._io, this as any, this._root, (this.dtype as any)));
      }
      this._io.seek(_pos);
      return this._entries;
    }

    offset: number;
    dtype: string;
    amt: number;
  }
}

export namespace Hsm {
  export class GameGameLogicStateDefinitionId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.stateDefinitionId = (this._io.readS4le()) as any
    }


    /**
     * Unique ID
     */
    stateDefinitionId: number;
  }
}

export namespace Hsm {
  export class GameGameLogicStateEntryPointId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.stateEntryPointId = (new Hsm.CgsId(this._io, this, this._root)) as any
    }


    /**
     * Little endian
     */
    stateEntryPointId: Hsm.CgsId;
  }
}

export namespace Hsm {
  export class PtrPtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Hsm | undefined,
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

    private _ptrTable: Hsm.PtrTable | undefined;
    get ptrTable(): Hsm.PtrTable | undefined {
      if (typeof this._ptrTable !== 'undefined')
        return this._ptrTable;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptrTable = (new Hsm.PtrTable(this._io, this, this._root, (this.dtype as any), (this.len as any))) as any
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

export namespace Hsm {
  export class GameGameLogicStateExitPointId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Hsm.GameGameLogicHsmDataHsmChildExitPointData,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.stateExitPointId = (new Hsm.CgsId(this._io, this, this._root)) as any
    }


    /**
     * Little endian
     */
    stateExitPointId: Hsm.CgsId;
  }
}

export namespace Hsm {
  export class PtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Hsm | undefined,
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
        this.entries.push(new Hsm.Ptr(this._io, this, this._root, (this.dtype as any)));
      }
    }

    entries: Array<Hsm.Ptr>;
    dtype: string;
    amt: number;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmStructureInstance {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.ptrMaParameters0x0 = (this._io.readU4le()) as any
      this.miNumParameters0x4 = (this._io.readS2le()) as any
      this.padding = (this._io.readBytes(2)) as any
    }

    private _parameters: Array<Hsm.GameGameLogicHsmDataHsmParameter>;
    get parameters(): Array<Hsm.GameGameLogicHsmDataHsmParameter> {
      if (typeof this._parameters !== 'undefined')
        return this._parameters;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaParameters0x0 as any));
      this._parameters = [];
      for (let i = 0; i < (this.miNumParameters0x4 as any); i++) {
        this._parameters.push(new Hsm.GameGameLogicHsmDataHsmParameter(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._parameters;
    }


    /**
     * Parameters
     */
    ptrMaParameters0x0: number;

    /**
     * Number of parameters
     */
    miNumParameters0x4: number;
    padding: Uint8Array;
  }
}

export namespace Hsm {
  export class Dummy {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Hsm.Atype,
      readonly _root?: Hsm,
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

export namespace Hsm {
  export class CgsId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.value = (this._io.readBytes(8)) as any
    }

    value: Uint8Array;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmParameter {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.mParamId0x0 = (new Hsm.GameGameLogicHsmDataParameterId(this._io, this, this._root)) as any
      this.union0x8 = (this._io.readU4le()) as any
      this.meParamType0xc = (this._io.readS2le()) as any
      this.miNumValues0xe = (this._io.readS2le()) as any
    }

    private _parameterValues: Array<Hsm.AnonymousParamUnion>;
    get parameterValues(): Array<Hsm.AnonymousParamUnion> {
      if (typeof this._parameterValues !== 'undefined')
        return this._parameterValues;
      let _pos = this._io.pos;
      this._io.seek((this.union0x8 as any));
      this._parameterValues = [];
      for (let i = 0; i < (this.miNumValues0xe as any); i++) {
        this._parameterValues.push(new Hsm.AnonymousParamUnion(this._io, this, this._root, (this.meParamType0xc as any)));
      }
      this._io.seek(_pos);
      return this._parameterValues;
    }


    /**
     * Parameter ID
     */
    mParamId0x0: Hsm.GameGameLogicHsmDataParameterId;

    /**
     * Pointer to value or child parameter list
     */
    union0x8: number;

    /**
     * Parameter type; See EHSMParamTypes
     */
    meParamType0xc: Hsm.EHsmParamType;

    /**
     * Number of values
     */
    miNumValues0xe: number;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmStateDefinition {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.mStateBehaviourId0x0 = (new Hsm.GameGameLogicStateBehaviourId(this._io, this, this._root)) as any
      this.mStateDefinitionId0x4 = (new Hsm.GameGameLogicStateDefinitionId(this._io, this, this._root)) as any
      this.ptrMaStateEntryPoints0x8 = (this._io.readU4le()) as any
      this.ptrMaChildExitData0xc = (this._io.readU4le()) as any
      this.ptrMaParameters0x10 = (this._io.readU4le()) as any
      this.mpDataDefinition0x14 = (new Hsm.Ptr(this._io, this, this._root, "game__game_logic__hsm_data__hsm_data_definition")) as any
      this.mpcDebugStateDefinitionName0x18 = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
      this.muNumParameters0x1c = (this._io.readU1()) as any
      this.muFallbackBehaviour0x1d = (this._io.readU1()) as any
      this.muNumStateEntryPoints0x1e = (this._io.readU1()) as any
      this.muNumChildren0x1f = (this._io.readU1()) as any
    }

    private _stateEntryPoints: Array<Hsm.GameGameLogicHsmDataHsmStateEntryPoint>;
    get stateEntryPoints(): Array<Hsm.GameGameLogicHsmDataHsmStateEntryPoint> {
      if (typeof this._stateEntryPoints !== 'undefined')
        return this._stateEntryPoints;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaStateEntryPoints0x8 as any));
      this._stateEntryPoints = [];
      for (let i = 0; i < (this.muNumStateEntryPoints0x1e as any); i++) {
        this._stateEntryPoints.push(new Hsm.GameGameLogicHsmDataHsmStateEntryPoint(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._stateEntryPoints;
    }

    private _childExitData: Array<Hsm.GameGameLogicHsmDataHsmChildExitData>;
    get childExitData(): Array<Hsm.GameGameLogicHsmDataHsmChildExitData> {
      if (typeof this._childExitData !== 'undefined')
        return this._childExitData;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaChildExitData0xc as any));
      this._childExitData = [];
      for (let i = 0; i < (this.muNumChildren0x1f as any); i++) {
        this._childExitData.push(new Hsm.GameGameLogicHsmDataHsmChildExitData(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._childExitData;
    }

    private _parameters: Array<Hsm.GameGameLogicHsmDataHsmParameter>;
    get parameters(): Array<Hsm.GameGameLogicHsmDataHsmParameter> {
      if (typeof this._parameters !== 'undefined')
        return this._parameters;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaParameters0x10 as any));
      this._parameters = [];
      for (let i = 0; i < (this.muNumParameters0x1c as any); i++) {
        this._parameters.push(new Hsm.GameGameLogicHsmDataHsmParameter(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._parameters;
    }


    /**
     * State behaviour ID
     */
    mStateBehaviourId0x0: Hsm.GameGameLogicStateBehaviourId;

    /**
     * State definition ID
     */
    mStateDefinitionId0x4: Hsm.GameGameLogicStateDefinitionId;

    /**
     * State entry points
     */
    ptrMaStateEntryPoints0x8: number;

    /**
     * Child exit data
     */
    ptrMaChildExitData0xc: number;

    /**
     * Parameters
     */
    ptrMaParameters0x10: number;

    /**
     * Data definition
     */
    mpDataDefinition0x14: Hsm.Ptr;

    /**
     * Name
     */
    mpcDebugStateDefinitionName0x18: Hsm.Ptr;

    /**
     * Number of parameters
     */
    muNumParameters0x1c: number;

    /**
     * Fallback behaviour; See EFallbackBehaviour
     */
    muFallbackBehaviour0x1d: number;

    /**
     * Number of state entry points
     */
    muNumStateEntryPoints0x1e: number;

    /**
     * Number of children
     */
    muNumChildren0x1f: number;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmBehaviourInterface {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.mBehaviourInterfaceId0x0 = (new Hsm.CgsId(this._io, this, this._root)) as any
      this.mpcDebugName0x8 = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
      this.ptrMaEntryPointIds0xc = (this._io.readU4le()) as any
      this.ptrMaExitPointIds0x10 = (this._io.readU4le()) as any
      this.ptrMaParameters0x14 = (this._io.readU4le()) as any
      this.miNumParameters0x18 = (this._io.readS4le()) as any
      this.miNumEntryPoints0x1c = (this._io.readS2le()) as any
      this.miNumExitPoints0x1e = (this._io.readS2le()) as any
    }

    private _entryPointIds: Array<Hsm.CgsId>;
    get entryPointIds(): Array<Hsm.CgsId> {
      if (typeof this._entryPointIds !== 'undefined')
        return this._entryPointIds;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaEntryPointIds0xc as any));
      this._entryPointIds = [];
      for (let i = 0; i < (this.miNumEntryPoints0x1c as any); i++) {
        this._entryPointIds.push(new Hsm.CgsId(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._entryPointIds;
    }

    private _exitPointIds: Array<Hsm.CgsId>;
    get exitPointIds(): Array<Hsm.CgsId> {
      if (typeof this._exitPointIds !== 'undefined')
        return this._exitPointIds;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaExitPointIds0x10 as any));
      this._exitPointIds = [];
      for (let i = 0; i < (this.miNumExitPoints0x1e as any); i++) {
        this._exitPointIds.push(new Hsm.CgsId(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._exitPointIds;
    }

    private _parameters: Array<Hsm.GameGameLogicHsmDataHsmParameter>;
    get parameters(): Array<Hsm.GameGameLogicHsmDataHsmParameter> {
      if (typeof this._parameters !== 'undefined')
        return this._parameters;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaParameters0x14 as any));
      this._parameters = [];
      for (let i = 0; i < (this.miNumParameters0x18 as any); i++) {
        this._parameters.push(new Hsm.GameGameLogicHsmDataHsmParameter(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._parameters;
    }


    /**
     * Behaviour ID
     */
    mBehaviourInterfaceId0x0: Hsm.CgsId;

    /**
     * Name
     */
    mpcDebugName0x8: Hsm.Ptr;

    /**
     * Entry point IDs
     */
    ptrMaEntryPointIds0xc: number;

    /**
     * Exit point IDs
     */
    ptrMaExitPointIds0x10: number;

    /**
     * Parameters
     */
    ptrMaParameters0x14: number;

    /**
     * Number of parameters
     */
    miNumParameters0x18: number;

    /**
     * Number of entry points
     */
    miNumEntryPoints0x1c: number;

    /**
     * Number of exit points
     */
    miNumExitPoints0x1e: number;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmTopStateDefinition {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.mTopStateDefinitionId0x0 = (new Hsm.GameGameLogicStateDefinitionId(this._io, this, this._root)) as any
      this.mTopStateBehaviourId0x4 = (new Hsm.GameGameLogicStateBehaviourId(this._io, this, this._root)) as any
      this.mTopStateInstanceId0x8 = (new Hsm.GameGameLogicStateInstanceId(this._io, this, this._root)) as any
    }


    /**
     * Definition ID
     */
    mTopStateDefinitionId0x0: Hsm.GameGameLogicStateDefinitionId;

    /**
     * Behaviour ID
     */
    mTopStateBehaviourId0x4: Hsm.GameGameLogicStateBehaviourId;

    /**
     * Instance ID
     */
    mTopStateInstanceId0x8: Hsm.GameGameLogicStateInstanceId;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmDataDefinition {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.mDataDefinitionId0x0 = (new Hsm.GameGameLogicDataDefinitionId(this._io, this, this._root)) as any
      this.mpcPath0x4 = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
      this.mpData0x8 = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
      this.muDataSize0xc = (this._io.readU4le()) as any
      this.mpcDebugDataDefinitionName0x10 = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
    }


    /**
     * ID
     */
    mDataDefinitionId0x0: Hsm.GameGameLogicDataDefinitionId;

    /**
     * Path
     */
    mpcPath0x4: Hsm.Ptr;

    /**
     * Data
     */
    mpData0x8: Hsm.Ptr;

    /**
     * Data size
     */
    muDataSize0xc: number;

    /**
     * Name
     */
    mpcDebugDataDefinitionName0x10: Hsm.Ptr;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmStateSpawnData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.mEntryPointId0x0 = (new Hsm.GameGameLogicStateEntryPointId(this._io, this, this._root)) as any
      this.mStateDefinitionId0x8 = (new Hsm.GameGameLogicStateDefinitionId(this._io, this, this._root)) as any
      this.mpcDebugStateDefinitionName0xc = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
    }


    /**
     * Entry point ID
     */
    mEntryPointId0x0: Hsm.GameGameLogicStateEntryPointId;

    /**
     * State definition ID
     */
    mStateDefinitionId0x8: Hsm.GameGameLogicStateDefinitionId;

    /**
     * State definition name
     */
    mpcDebugStateDefinitionName0xc: Hsm.Ptr;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmChildExitData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.mChildStateDefinitionId0x0 = (new Hsm.GameGameLogicStateDefinitionId(this._io, this, this._root)) as any
      this.ptrMaChildExitPointData0x4 = (this._io.readU4le()) as any
      this.miNumChildExitPoints0x8 = (this._io.readS4le()) as any
      this.mpcDebugStateDefinitionName0xc = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
    }

    private _childExitPoints: Array<Hsm.GameGameLogicHsmDataHsmChildExitPointData>;
    get childExitPoints(): Array<Hsm.GameGameLogicHsmDataHsmChildExitPointData> {
      if (typeof this._childExitPoints !== 'undefined')
        return this._childExitPoints;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaChildExitPointData0x4 as any));
      this._childExitPoints = [];
      for (let i = 0; i < (this.miNumChildExitPoints0x8 as any); i++) {
        this._childExitPoints.push(new Hsm.GameGameLogicHsmDataHsmChildExitPointData(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._childExitPoints;
    }


    /**
     * Child state definition ID
     */
    mChildStateDefinitionId0x0: Hsm.GameGameLogicStateDefinitionId;

    /**
     * Child exit points
     */
    ptrMaChildExitPointData0x4: number;

    /**
     * Number of child exit points
     */
    miNumChildExitPoints0x8: number;

    /**
     * State definition name
     */
    mpcDebugStateDefinitionName0xc: Hsm.Ptr;
  }
}

export namespace Hsm {
  export class Ptr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: Hsm | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _data: Hsm.Atype | undefined;
    get data(): Hsm.Atype | undefined {
      if (typeof this._data !== 'undefined')
        return this._data;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._data = (new Hsm.Atype(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._data;
    }

    offset: number;
    dtype: string;
  }
}

export namespace Hsm {
  export class AnonymousParamUnion {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: Hsm.GameGameLogicHsmDataHsmParameter | undefined,
      readonly _root: Hsm | undefined,
      paramType: Hsm.EHsmParamType,
    ) {
      this.paramType = paramType;

      this._read();
    }

    _read() {
      switch ((this.paramType as any)) {
        case Hsm.EHsmParamType.INVALID: {
          this.param = (this._io.readU4le()) as any
          break;
        }
        case Hsm.EHsmParamType.STRUCTURE: {
          this.param = (new Hsm.GameGameLogicHsmDataHsmStructureInstance(this._io, this, this._root)) as any
          break;
        }
        case Hsm.EHsmParamType.ASSET_REFERENCE: {
          this.param = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
          break;
        }
        case Hsm.EHsmParamType.INT: {
          this.param = (new Hsm.Ptr(this._io, this, this._root, "u4")) as any
          break;
        }
        case Hsm.EHsmParamType.STRING: {
          this.param = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
          break;
        }
        case Hsm.EHsmParamType.ID: {
          this.param = (this._io.readU4le()) as any
          break;
        }
        case Hsm.EHsmParamType.BOOL: {
          this.param = (new Hsm.Ptr(this._io, this, this._root, "strz")) as any
          break;
        }
        case Hsm.EHsmParamType.FLOAT: {
          this.param = (new Hsm.Ptr(this._io, this, this._root, "f4")) as any
          break;
        }
      }
    }

    param: number | undefined | Hsm.GameGameLogicHsmDataHsmStructureInstance | undefined | Hsm.Ptr | undefined | Hsm.Ptr | undefined | Hsm.Ptr | undefined | number | undefined | Hsm.Ptr | undefined | Hsm.Ptr | undefined | undefined;
    paramType: Hsm.EHsmParamType;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataHsmStateEntryPoint {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.mEntryPointId0x0 = (new Hsm.GameGameLogicStateEntryPointId(this._io, this, this._root)) as any
      this.muAction0x8 = (this._io.readU1()) as any
      this.muNumChildren0x9 = (this._io.readU1()) as any
      this.padding = (this._io.readBytes(2)) as any
      this.ptrMaChildSpawnData0xc = (this._io.readU4le()) as any
    }

    private _childSpawnData: Array<Hsm.GameGameLogicHsmDataHsmStateSpawnData>;
    get childSpawnData(): Array<Hsm.GameGameLogicHsmDataHsmStateSpawnData> {
      if (typeof this._childSpawnData !== 'undefined')
        return this._childSpawnData;
      let _pos = this._io.pos;
      this._io.seek((this.ptrMaChildSpawnData0xc as any));
      this._childSpawnData = [];
      for (let i = 0; i < (this.muNumChildren0x9 as any); i++) {
        this._childSpawnData.push(new Hsm.GameGameLogicHsmDataHsmStateSpawnData(this._io, this, this._root));
      }
      this._io.seek(_pos);
      return this._childSpawnData;
    }


    /**
     * Entry point ID
     */
    mEntryPointId0x0: Hsm.GameGameLogicStateEntryPointId;

    /**
     * Action; See EHSMActio
     */
    muAction0x8: number;

    /**
     * Number of children
     */
    muNumChildren0x9: number;
    padding: Uint8Array;

    /**
     * Child state spawn data
     */
    ptrMaChildSpawnData0xc: number;
  }
}

export namespace Hsm {
  export class GameGameLogicStateInstanceId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Hsm.GameGameLogicHsmDataHsmTopStateDefinition,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.stateInstanceId = (this._io.readS4le()) as any
    }


    /**
     * Unique ID
     */
    stateInstanceId: number;
  }
}

export namespace Hsm {
  export class GameGameLogicHsmDataParameterId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: Hsm.GameGameLogicHsmDataHsmParameter,
      readonly _root?: Hsm,
    ) {

      this._read();
    }

    _read() {
      this.parameterId = (new Hsm.CgsId(this._io, this, this._root)) as any
    }

    parameterId: Hsm.CgsId;
  }
}

export namespace Hsm {
  export class Atype {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: Hsm.Ptr | undefined,
      readonly _root: Hsm | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      switch ((this.dtype as any)) {
        case "game__game_logic__hsm_data__hsm_child_exit_data": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmChildExitData(this._io, this, this._root)) as any
          break;
        }
        case "s4": {
          this.data = (this._io.readS4le()) as any
          break;
        }
        case "game__game_logic__hsm_data__hsm_data_definition": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmDataDefinition(this._io, this, this._root)) as any
          break;
        }
        case "game__game_logic__hsm_data__hsm_child_exit_point_data": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmChildExitPointData(this._io, this, this._root)) as any
          break;
        }
        case "s1": {
          this.data = (this._io.readS1()) as any
          break;
        }
        case "game__game_logic__hsm_data__hsm_behaviour_interface": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmBehaviourInterface(this._io, this, this._root)) as any
          break;
        }
        case "game__game_logic__hsm_data__hsm_state_definition": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmStateDefinition(this._io, this, this._root)) as any
          break;
        }
        case "u4": {
          this.data = (this._io.readU4le()) as any
          break;
        }
        case "u2": {
          this.data = (this._io.readU2le()) as any
          break;
        }
        case "game__game_logic__hsm_data__hsm_parameter": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmParameter(this._io, this, this._root)) as any
          break;
        }
        case "game__game_logic__hsm_data__hsm_state_entry_point": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmStateEntryPoint(this._io, this, this._root)) as any
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
        case "f4": {
          this.data = (this._io.readF4le()) as any
          break;
        }
        case "u1": {
          this.data = (this._io.readU1()) as any
          break;
        }
        case "game__game_logic__hsm_data__hsm_state_spawn_data": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmStateSpawnData(this._io, this, this._root)) as any
          break;
        }
        case "cgs_id": {
          this.data = (new Hsm.CgsId(this._io, this, this._root)) as any
          break;
        }
        case "game__game_logic__hsm_data__hsm_top_state_definition": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmTopStateDefinition(this._io, this, this._root)) as any
          break;
        }
        case "game__game_logic__hsm_data__hsm_structure_instance": {
          this.data = (new Hsm.GameGameLogicHsmDataHsmStructureInstance(this._io, this, this._root)) as any
          break;
        }
        default: {
          this.data = (new Hsm.Dummy(this._io, this, this._root)) as any
          break;
        }
      }
    }

    data: Hsm.GameGameLogicHsmDataHsmChildExitData | number | Hsm.GameGameLogicHsmDataHsmDataDefinition | Hsm.GameGameLogicHsmDataHsmChildExitPointData | number | Hsm.GameGameLogicHsmDataHsmBehaviourInterface | Hsm.GameGameLogicHsmDataHsmStateDefinition | number | number | Hsm.GameGameLogicHsmDataHsmParameter | Hsm.GameGameLogicHsmDataHsmStateEntryPoint | number | string | number | number | Hsm.GameGameLogicHsmDataHsmStateSpawnData | Hsm.Dummy | Hsm.CgsId | Hsm.GameGameLogicHsmDataHsmTopStateDefinition | Hsm.GameGameLogicHsmDataHsmStructureInstance;
    dtype: string;
  }
}
export namespace Hsm {
  export enum EFallbackBehaviour {
    RUN_CHILDREN = 0,
    EXIT = 1,
    ASSERT_THEN_EXIT = 2,
    COUNT = 3,
  }
}
export namespace Hsm {
  export enum EHsmAction {
    NOTHING = 0,
    CHILD = 1,
    EXIT = 2,
    HSM_ACTION_COUNT = 3,
  }
}
export namespace Hsm {
  export enum EHsmParamType {
    STRING = 0,
    INT = 1,
    FLOAT = 2,
    ID = 3,
    BOOL = 4,
    ASSET_REFERENCE = 5,
    STRUCTURE = 6,
    INVALID = 7,
  }
}
