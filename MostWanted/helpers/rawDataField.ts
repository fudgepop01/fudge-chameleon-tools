import { Endian, BaseField } from "construct-js";

const assert = (condition, message) => {
  if (!condition) {
      throw new Error(message);
  }
};

export default class RawDataField {
  public width;
  public toBytesFn;
  public value;
  public endian;

  constructor(value: Uint8Array, toBytesFn: (vals: number[], isLE: boolean) => Uint8Array) {
      this.width = value.length;
      this.toBytesFn = toBytesFn;
      this.assertInvariants(value);
      this.value = value;
      this.endian = Endian.Little;
  }
  
  assertInvariants(value) {
      assert(!(value instanceof Uint8Array), `value must be a UInt8Array of raw bytes!`);
  }
  computeBufferSize() { return this.width; }
  toUint8Array() {
      return this.toBytesFn([this.value], false);
  }
  set(value) {
      this.assertInvariants(value);
      this.value = value;
  }
  get() { return this.value; }
}

const RawDataToBytes 

export class RawDataType extends RawDataField {
  constructor(value: number, endian: Endian = Endian.Little) {
    super(value, f32Tou8s);
  }
}

export const F32 = (value: number, endian: Endian = Endian.Little) => new F32Type(value, endian);
