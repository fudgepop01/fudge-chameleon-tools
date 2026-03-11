/*
 * This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
 */
import KaitaiStream from 'kaitai-struct/KaitaiStream'

export class GenesysType {
  _is_le?: boolean;

  constructor(
    readonly _io: KaitaiStream,
    readonly _parent?: unknown,
    readonly _root?: GenesysType,
  ) {
    this._root ??= this;

    this._read();
  }

  _read() {
    this.muGenesysVersion = (this._io.readU1()) as any
    this.meNativeType = (this._io.readU1()) as any
    this.muPropertyCount = (this._io.readU2le()) as any
    switch ((this.meNativeType as any)) {
      case 5: {
        this.typeData = (new GenesysType.GenesysNativetypeEnumerationData(this._io, this, this._root)) as any
        break;
      }
      case 6: {
        this.typeData = (new GenesysType.GenesysNativetypeObjectData(this._io, this, this._root)) as any
        break;
      }
      case 7: {
        this.typeData = (new GenesysType.GenesysNativetypeObjectData(this._io, this, this._root)) as any
        break;
      }
      default: {
        this.typeData = (new GenesysType.GenesysNativetypeObjectData(this._io, this, this._root)) as any
        break;
      }
    }
  }

  private _sizes: GenesysType.TypeSizeCollection;
  get sizes(): GenesysType.TypeSizeCollection {
    if (typeof this._sizes !== 'undefined')
      return this._sizes;
    this._sizes = (new GenesysType.TypeSizeCollection(this._io, this, this._root)) as any
    return this._sizes;
  }

  private _nativeType: GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType;
  get nativeType(): GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType {
    if (typeof this._nativeType !== 'undefined')
      return this._nativeType;
    switch ((this.meNativeType as any)) {
      case 10: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_count")) as any
        break;
      }
      case 0: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_integer")) as any
        break;
      }
      case 4: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_char")) as any
        break;
      }
      case 6: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_object")) as any
        break;
      }
      case 7: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_genesysobject")) as any
        break;
      }
      case 1: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_unsigned_integer")) as any
        break;
      }
      case 3: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_boolean")) as any
        break;
      }
      case 5: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_enumeration")) as any
        break;
      }
      case 8: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_resource_handle")) as any
        break;
      }
      case 9: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_resource_id")) as any
        break;
      }
      case 2: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "e_nativetype_float")) as any
        break;
      }
      default: {
        this._nativeType = (new GenesysType.DisplayType(this._io, this, this._root, "undocumented")) as any
        break;
      }
    }
    return this._nativeType;
  }

  muGenesysVersion: number;
  meNativeType: number;
  muPropertyCount: number;
  typeData: GenesysType.GenesysNativetypeEnumerationData | GenesysType.GenesysNativetypeObjectData | GenesysType.GenesysNativetypeObjectData | GenesysType.GenesysNativetypeObjectData;
}

export namespace GenesysType {
  export class DisplayType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: GenesysType | undefined,
      readonly _root: GenesysType | undefined,
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

export namespace GenesysType {
  export class GenesysNativetypeEnumerationData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysType,
      readonly _root?: GenesysType,
    ) {

      this._read();
    }

    _read() {
      this.mpBaseTypePtr = (this._io.readU4le()) as any
      this.muBaseTypeVersion = (this._io.readU4le()) as any
      this.mpaPropertiesPtr = (new GenesysType.PtrArray(this._io, this, this._root, "genesys_property", (this._parent as any).muPropertyCount)) as any
      this.muVersion = (this._io.readU4le()) as any
      this.muId = (this._io.readU4le()) as any
      this.muSize = (this._io.readU4le()) as any
      this.maReserved = [];
      for (let i = 0; i < 3; i++) {
        this.maReserved.push(this._io.readU1());
      }
      this.muAlignment = (this._io.readU1()) as any
    }

    mpBaseTypePtr: number;
    muBaseTypeVersion: number;
    mpaPropertiesPtr: GenesysType.PtrArray;
    muVersion: number;
    muId: number;
    muSize: number;
    maReserved: Array<number>;
    muAlignment: number;
  }
}

export namespace GenesysType {
  export class GenesysValueType {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysType.GenesysProperty,
      readonly _root?: GenesysType,
    ) {

      this._read();
    }

    _read() {
      this.valueFlags = (this._io.readU1()) as any
    }

    private _eValueTypeP1: number;
    get eValueTypeP1(): number {
      if (typeof this._eValueTypeP1 !== 'undefined')
        return this._eValueTypeP1;
      this._eValueTypeP1 = (((this.valueFlags as any) & 3)) as any
      return this._eValueTypeP1;
    }

    private _eValueTypeP2: number;
    get eValueTypeP2(): number {
      if (typeof this._eValueTypeP2 !== 'undefined')
        return this._eValueTypeP2;
      this._eValueTypeP2 = ((((this.valueFlags as any) & 12) >>> 2)) as any
      return this._eValueTypeP2;
    }

    private _eValueTypeP3: number;
    get eValueTypeP3(): number {
      if (typeof this._eValueTypeP3 !== 'undefined')
        return this._eValueTypeP3;
      this._eValueTypeP3 = ((((this.valueFlags as any) & 48) >>> 4)) as any
      return this._eValueTypeP3;
    }

    private _eValueTypeP4: number;
    get eValueTypeP4(): number {
      if (typeof this._eValueTypeP4 !== 'undefined')
        return this._eValueTypeP4;
      this._eValueTypeP4 = ((((this.valueFlags as any) & 192) >>> 6)) as any
      return this._eValueTypeP4;
    }

    valueFlags: number;
  }
}

export namespace GenesysType {
  export class PtrPtr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysType | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _ptr: GenesysType.Ptr | undefined;
    get ptr(): GenesysType.Ptr | undefined {
      if (typeof this._ptr !== 'undefined')
        return this._ptr;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptr = (new GenesysType.Ptr(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._ptr;
    }

    offset: number;
    dtype: string;
  }
}

export namespace GenesysType {
  export class PtrArray {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysType | undefined,
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

    private _entries: Array<GenesysType.Atype>;
    get entries(): Array<GenesysType.Atype> {
      if (typeof this._entries !== 'undefined')
        return this._entries;
      let _pos = this._io.pos;
      this._io.seek((this.offset as any));
      this._entries = [];
      for (let i = 0; i < (this.amt as any); i++) {
        this._entries.push(new GenesysType.Atype(this._io, this, this._root, (this.dtype as any)));
      }
      this._io.seek(_pos);
      return this._entries;
    }

    offset: number;
    dtype: string;
    amt: number;
  }
}

export namespace GenesysType {
  export class PtrPtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysType | undefined,
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

    private _ptrTable: GenesysType.PtrTable | undefined;
    get ptrTable(): GenesysType.PtrTable | undefined {
      if (typeof this._ptrTable !== 'undefined')
        return this._ptrTable;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptrTable = (new GenesysType.PtrTable(this._io, this, this._root, (this.dtype as any), (this.len as any))) as any
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

export namespace GenesysType {
  export class PtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysType | undefined,
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
        this.entries.push(new GenesysType.Ptr(this._io, this, this._root, (this.dtype as any)));
      }
    }

    entries: Array<GenesysType.Ptr>;
    dtype: string;
    amt: number;
  }
}

export namespace GenesysType {
  export class Dummy {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysType.Atype,
      readonly _root?: GenesysType,
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

export namespace GenesysType {
  export class GenesysNativetypeObjectData {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysType,
      readonly _root?: GenesysType,
    ) {

      this._read();
    }

    _read() {
      this.mpBaseTypePtr = (this._io.readU4le()) as any
      this.muBaseTypeVersion = (this._io.readU4le()) as any
      this.mpaPropertiesPtr = (new GenesysType.PtrArray(this._io, this, this._root, "genesys_property", (this._parent as any).muPropertyCount)) as any
      this.muVersion = (this._io.readU4le()) as any
      this.muId = (this._io.readU4le()) as any
      this.muSize = (this._io.readU4le()) as any
      this.maReserved = [];
      for (let i = 0; i < 3; i++) {
        this.maReserved.push(this._io.readU1());
      }
      this.muAlignment = (this._io.readU1()) as any
      this.muTypeInfoPtr = (new GenesysType.Ptr(this._io, this, this._root, "genesys_type_information")) as any
    }

    mpBaseTypePtr: number;
    muBaseTypeVersion: number;
    mpaPropertiesPtr: GenesysType.PtrArray;
    muVersion: number;
    muId: number;
    muSize: number;
    maReserved: Array<number>;
    muAlignment: number;
    muTypeInfoPtr: GenesysType.Ptr;
  }
}

export namespace GenesysType {
  export class GenesysTypeHash {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenesysType,
    ) {

      this._read();
    }

    _read() {
      this.hash = (this._io.readU4le()) as any
      this.padding = (this._io.readU4le()) as any
      this.value = (this._io.readF4le()) as any
    }

    private _name: GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType;
    get name(): GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType | GenesysType.DisplayType {
      if (typeof this._name !== 'undefined')
        return this._name;
      switch ((this.hash as any)) {
        case 2393620497: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "uint8_t")) as any
          break;
        }
        case 315911266: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "int32_t")) as any
          break;
        }
        case 2365478815: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "char")) as any
          break;
        }
        case 188736650: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "CgsResource.Handle")) as any
          break;
        }
        case 786114023: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "Genesys.Object")) as any
          break;
        }
        case 237695873: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "uint32_t")) as any
          break;
        }
        case 1380374412: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "bool8_t")) as any
          break;
        }
        case 2737476566: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "uint16_t")) as any
          break;
        }
        case 1393192327: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "float32_t")) as any
          break;
        }
        case 1077953281: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "CgsCore.StringBase")) as any
          break;
        }
        case 3218345013: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "int16_t")) as any
          break;
        }
        case 3106047474: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "CgsCore.UniqueId")) as any
          break;
        }
        default: {
          this._name = (new GenesysType.DisplayType(this._io, (this as any), this._root, "unknown")) as any
          break;
        }
      }
      return this._name;
    }

    hash: number;
    padding: number;
    value: number;
  }
}

export namespace GenesysType {
  export class TypeSizeCollection {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysType,
      readonly _root?: GenesysType,
    ) {

      this._read();
    }

    _read() {
    }

    private _genesysTypeHash: number;
    get genesysTypeHash(): number {
      if (typeof this._genesysTypeHash !== 'undefined')
        return this._genesysTypeHash;
      this._genesysTypeHash = (12) as any
      return this._genesysTypeHash;
    }

    private _genesysTypeInformation: number;
    get genesysTypeInformation(): number {
      if (typeof this._genesysTypeInformation !== 'undefined')
        return this._genesysTypeInformation;
      this._genesysTypeInformation = (8) as any
      return this._genesysTypeInformation;
    }

    private _genesysValueType: number;
    get genesysValueType(): number {
      if (typeof this._genesysValueType !== 'undefined')
        return this._genesysValueType;
      this._genesysValueType = (1) as any
      return this._genesysValueType;
    }

    private _genesysNativetypeObjectData: number;
    get genesysNativetypeObjectData(): number {
      if (typeof this._genesysNativetypeObjectData !== 'undefined')
        return this._genesysNativetypeObjectData;
      this._genesysNativetypeObjectData = (32) as any
      return this._genesysNativetypeObjectData;
    }

    private _genesysNativetypeEnumerationData: number;
    get genesysNativetypeEnumerationData(): number {
      if (typeof this._genesysNativetypeEnumerationData !== 'undefined')
        return this._genesysNativetypeEnumerationData;
      this._genesysNativetypeEnumerationData = (32) as any
      return this._genesysNativetypeEnumerationData;
    }

    private _genesysProperty: number;
    get genesysProperty(): number {
      if (typeof this._genesysProperty !== 'undefined')
        return this._genesysProperty;
      this._genesysProperty = (28) as any
      return this._genesysProperty;
    }

    private _genesysTypeEntry: number;
    get genesysTypeEntry(): number {
      if (typeof this._genesysTypeEntry !== 'undefined')
        return this._genesysTypeEntry;
      this._genesysTypeEntry = (16) as any
      return this._genesysTypeEntry;
    }

  }
}

export namespace GenesysType {
  export class Ptr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysType | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _data: GenesysType.Atype | undefined;
    get data(): GenesysType.Atype | undefined {
      if (typeof this._data !== 'undefined')
        return this._data;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._data = (new GenesysType.Atype(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._data;
    }

    offset: number;
    dtype: string;
  }
}

export namespace GenesysType {
  export class GenesysTypeEntry {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenesysType,
    ) {

      this._read();
    }

    _read() {
      this.typeHashId = (this._io.readBytes(8)) as any
      this.position = (this._io.readU4le()) as any
      this.padding = (this._io.readBytes(4)) as any
    }

    typeHashId: Uint8Array;
    position: number;
    padding: Uint8Array;
  }
}

export namespace GenesysType {
  export class GenesysTypeInformation {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysType.Atype,
      readonly _root?: GenesysType,
    ) {

      this._read();
    }

    _read() {
      this.mpNamePtr = (new GenesysType.Ptr(this._io, this, this._root, "strz")) as any
      this.mpaPropertyNamesPtr = (new GenesysType.Ptr(this._io, this, this._root, "strz")) as any
    }

    mpNamePtr: GenesysType.Ptr;
    mpaPropertyNamesPtr: GenesysType.Ptr;
  }
}

export namespace GenesysType {
  export class GenesysProperty {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysType.Atype,
      readonly _root?: GenesysType,
    ) {

      this._read();
    }

    _read() {
      this.mpTypePtr = (new GenesysType.Ptr(this._io, this, this._root, "genesys_type")) as any
      this.muTypeVersion = (this._io.readU4le()) as any
      this.mpArrayCountPropertyPtr = (this._io.readU4le()) as any
      this.muId = (this._io.readU4le()) as any
      this.muTypeSize = (this._io.readU4le()) as any
      this.muOffset = (this._io.readU4le()) as any
      this.muCount = (this._io.readU2le()) as any
      this.muTypeAlignment = (this._io.readU1()) as any
      this.mValueType = (new GenesysType.GenesysValueType(this._io, this, this._root)) as any
    }

    mpTypePtr: GenesysType.Ptr;
    muTypeVersion: number;
    mpArrayCountPropertyPtr: number;
    muId: number;

    /**
     * size of each element in bytes
     */
    muTypeSize: number;

    /**
     * location of the property relative to type start
     */
    muOffset: number;

    /**
     * number of elements
     */
    muCount: number;
    muTypeAlignment: number;
    mValueType: GenesysType.GenesysValueType;
  }
}

export namespace GenesysType {
  export class Atype {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysType | undefined,
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
        case "genesys_type_information": {
          this.data = (new GenesysType.GenesysTypeInformation(this._io, this, this._root)) as any
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
        case "f4": {
          this.data = (this._io.readF4le()) as any
          break;
        }
        case "u1": {
          this.data = (this._io.readU1()) as any
          break;
        }
        case "genesys_type": {
          this.data = (new GenesysType(this._io, this, null)) as any
          break;
        }
        case "genesys_property": {
          this.data = (new GenesysType.GenesysProperty(this._io, this, this._root)) as any
          break;
        }
        default: {
          this.data = (new GenesysType.Dummy(this._io, this, this._root)) as any
          break;
        }
      }
    }

    data: number | GenesysType.GenesysTypeInformation | number | number | number | number | string | number | number | GenesysType.Dummy | GenesysType | GenesysType.GenesysProperty;
    dtype: string;
  }
}
export namespace GenesysType {
  export enum ENativeType {
    E_NATIVETYPE_INTEGER = 0,
    E_NATIVETYPE_UNSIGNED_INTEGER = 1,
    E_NATIVETYPE_FLOAT = 2,
    E_NATIVETYPE_BOOLEAN = 3,
    E_NATIVETYPE_CHAR = 4,
    E_NATIVETYPE_ENUMERATION = 5,
    E_NATIVETYPE_OBJECT = 6,
    E_NATIVETYPE_GENESYSOBJECT = 7,
    E_NATIVETYPE_RESOURCE_HANDLE = 8,
    E_NATIVETYPE_RESOURCE_ID = 9,
    E_NATIVETYPE_COUNT = 10,
  }
}
export namespace GenesysType {
  export enum EValuetype {
    E_VALUETYPE_VALUE = 0,
    E_VALUETYPE_POINTER = 1,
    E_VALUETYPE_ARRAY = 2,
    E_VALUETYPE_OFFSET = 3,
    E_VALUETYPE_COUNT = 4,
  }
}
