/*
 * This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
 */
import KaitaiStream from 'kaitai-struct/KaitaiStream'

export class GenesysObject {
  _is_le?: boolean;

  constructor(
    readonly _io: KaitaiStream,
    readonly _parent?: unknown,
    readonly _root?: GenesysObject,
  ) {
    this._root ??= this;

    this._read();
  }

  _read() {
    this.mpType = (new GenesysObject.CgsResourceHandle(this._io, this, this._root)) as any
    this.muTypeVersion = (this._io.readU4be()) as any
  }

  mpType: GenesysObject.CgsResourceHandle;
  muTypeVersion: number;
}

export namespace GenesysObject {
  export class CgsMemDescriptor {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysObject.CgsResourcePoolEntry,
      readonly _root?: GenesysObject,
    ) {

      this._read();
    }

    _read() {
      this.mauSizes = [];
      for (let i = 0; i < 4; i++) {
        this.mauSizes.push(this._io.readU4le());
      }
      this.mauAlignments = [];
      for (let i = 0; i < 4; i++) {
        this.mauAlignments.push(this._io.readU4le());
      }
    }

    mauSizes: Array<number>;
    mauAlignments: Array<number>;
  }
}

export namespace GenesysObject {
  export class PtrPtr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysObject | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _ptr: GenesysObject.Ptr | undefined;
    get ptr(): GenesysObject.Ptr | undefined {
      if (typeof this._ptr !== 'undefined')
        return this._ptr;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptr = (new GenesysObject.Ptr(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._ptr;
    }

    offset: number;
    dtype: string;
  }
}

export namespace GenesysObject {
  export class CgsResourceId {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysObject.CgsResourcePoolEntry,
      readonly _root?: GenesysObject,
    ) {

      this._read();
    }

    _read() {
      this.mHash = (this._io.readBytes(8)) as any
    }

    mHash: Uint8Array;
  }
}

export namespace GenesysObject {
  export class CgsResourceTypeV2 {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysObject.Atype,
      readonly _root?: GenesysObject,
    ) {

      this._read();
    }

    _read() {
      this.vtable = (new GenesysObject.Ptr(this._io, this, this._root, "u4")) as any
      this.mbMemoryOverridden = (this._io.readU1()) as any
      this.macDebugTypeName = (KaitaiStream.bytesToStr(this._io.readBytes(31), "ascii")) as any
      this.muTypeId = (this._io.readU4le()) as any
      this.mauMemoryAlignment = [];
      for (let i = 0; i < 4; i++) {
        this.mauMemoryAlignment.push(this._io.readU4le());
      }
    }

    vtable: GenesysObject.Ptr;
    mbMemoryOverridden: number;
    macDebugTypeName: string;
    muTypeId: number;
    mauMemoryAlignment: Array<number>;
  }
}

export namespace GenesysObject {
  export class PtrArray {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysObject | undefined,
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

    private _entries: Array<GenesysObject.Atype>;
    get entries(): Array<GenesysObject.Atype> {
      if (typeof this._entries !== 'undefined')
        return this._entries;
      let _pos = this._io.pos;
      this._io.seek((this.offset as any));
      this._entries = [];
      for (let i = 0; i < (this.amt as any); i++) {
        this._entries.push(new GenesysObject.Atype(this._io, this as any, this._root, (this.dtype as any)));
      }
      this._io.seek(_pos);
      return this._entries;
    }

    offset: number;
    dtype: string;
    amt: number;
  }
}

export namespace GenesysObject {
  export class PtrPtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysObject | undefined,
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

    private _ptrTable: GenesysObject.PtrTable | undefined;
    get ptrTable(): GenesysObject.PtrTable | undefined {
      if (typeof this._ptrTable !== 'undefined')
        return this._ptrTable;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._ptrTable = (new GenesysObject.PtrTable(this._io, this, this._root, (this.dtype as any), (this.len as any))) as any
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

export namespace GenesysObject {
  export class PtrTable {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysObject | undefined,
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
        this.entries.push(new GenesysObject.Ptr(this._io, this, this._root, (this.dtype as any)));
      }
    }

    entries: Array<GenesysObject.Ptr>;
    dtype: string;
    amt: number;
  }
}

export namespace GenesysObject {
  export class CgsResourceHandle {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysObject,
      readonly _root?: GenesysObject,
    ) {

      this._read();
    }

    _read() {
      this.mpEntry = (new GenesysObject.Ptr(this._io, this, this._root, "cgs_resource_pool_entry")) as any
      this.muOffset = (this._io.readU4le()) as any
    }

    mpEntry: GenesysObject.Ptr;
    muOffset: number;
  }
}

export namespace GenesysObject {
  export class Dummy {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysObject.Atype,
      readonly _root?: GenesysObject,
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

export namespace GenesysObject {
  export class CgsMemAddress {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysObject.CgsResourcePoolEntry,
      readonly _root?: GenesysObject,
    ) {

      this._read();
    }

    _read() {
      this.mapData = [];
      for (let i = 0; i < 4; i++) {
        this.mapData.push(new GenesysObject.Ptr(this._io, this, this._root, "u4"));
      }
    }

    mapData: Array<GenesysObject.Ptr>;
  }
}

export namespace GenesysObject {
  export class CgsResourcePoolEntry {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: GenesysObject.Atype,
      readonly _root?: GenesysObject,
    ) {

      this._read();
    }

    _read() {
      this.mId = (new GenesysObject.CgsResourceId(this._io, this, this._root)) as any
      this.mDescriptor = (new GenesysObject.CgsMemDescriptor(this._io, this, this._root)) as any
      this.mAddress = (new GenesysObject.CgsMemAddress(this._io, this, this._root)) as any
      this.mpResourceType = (new GenesysObject.Ptr(this._io, this, this._root, "cgs_resource_type_v2")) as any
      this.muImportTableOffset = (this._io.readU4le()) as any
      this.mauHeapIndices = [];
      for (let i = 0; i < 4; i++) {
        this.mauHeapIndices.push(this._io.readU2le());
      }
    }

    mId: GenesysObject.CgsResourceId;
    mDescriptor: GenesysObject.CgsMemDescriptor;
    mAddress: GenesysObject.CgsMemAddress;
    mpResourceType: GenesysObject.Ptr;
    muImportTableOffset: number;
    mauHeapIndices: Array<number>;
  }
}

export namespace GenesysObject {
  export class Ptr {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: unknown | undefined,
      readonly _root: GenesysObject | undefined,
      dtype: string,
    ) {
      this.dtype = dtype;

      this._read();
    }

    _read() {
      this.offset = (this._io.readS4le()) as any
    }

    private _data: GenesysObject.Atype | undefined;
    get data(): GenesysObject.Atype | undefined {
      if (typeof this._data !== 'undefined')
        return this._data;
      if ((this.offset as any) != 0) {
        let _pos = this._io.pos;
        this._io.seek((this.offset as any));
        this._data = (new GenesysObject.Atype(this._io, this, this._root, (this.dtype as any))) as any
        this._io.seek(_pos);
      }
      return this._data;
    }

    offset: number;
    dtype: string;
  }
}

export namespace GenesysObject {
  export class CgsResourceThandle {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent?: unknown,
      readonly _root?: GenesysObject,
    ) {

      this._read();
    }

    _read() {
      this.handle = (new GenesysObject.CgsResourceHandle(this._io, this as any, this._root)) as any
    }

    handle: GenesysObject.CgsResourceHandle;
  }
}

export namespace GenesysObject {
  export class Atype {
    _is_le?: boolean;

    constructor(
      readonly _io: KaitaiStream,
      readonly _parent: GenesysObject.Ptr | undefined,
      readonly _root: GenesysObject | undefined,
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
        case "cgs_resource_type_v2": {
          this.data = (new GenesysObject.CgsResourceTypeV2(this._io, this, this._root)) as any
          break;
        }
        case "cgs_resource_pool_entry": {
          this.data = (new GenesysObject.CgsResourcePoolEntry(this._io, this, this._root)) as any
          break;
        }
        default: {
          this.data = (new GenesysObject.Dummy(this._io, this, this._root)) as any
          break;
        }
      }
    }

    data: number | number | number | number | number | string | number | number | GenesysObject.CgsResourceTypeV2 | GenesysObject.Dummy | GenesysObject.CgsResourcePoolEntry;
    dtype: string;
  }
}
