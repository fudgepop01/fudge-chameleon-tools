import { write as floatWrite } from 'ieee754';

/////////////////////////////////////////////////////
// basically a trimmed down version of the field class in construct-js' source code
/////////////////////////////////////////////////////

import { Endian, BaseField } from "construct-js";

const assert = (condition, message) => {
  if (!condition) {
      throw new Error(message);
  }
};

export default class FloatField {
  public width;
  public min;
  public max;
  public toBytesFn;
  public value;
  public endian;

  constructor(width, min: number, max: number, toBytesFn: (vals: number[], isLE: boolean) => Uint8Array, value: number, endian: Endian) {
      this.width = width;
      this.min = min;
      this.max = max;
      this.toBytesFn = toBytesFn;
      this.assertInvariants(value);
      this.value = value;
      this.endian = endian;
  }
  assertInvariants(value) {
      assert(value >= this.min && value <= this.max, `value must be an integer between ${this.min} and ${this.max}`);
  }
  computeBufferSize() { return this.width; }
  toUint8Array() {
      return this.toBytesFn([this.value], this.endian === Endian.Little);
  }
  set(value) {
      this.assertInvariants(value);
      this.value = value;
  }
  get() { return this.value; }
}


export class FloatArrayField {
    public width;
    public min;
    public max;
    public toBytesFn;
    public values;
    public endian;
    constructor(width, min, max, toBytesFn, values, endian = Endian.Little) {
        this.width = width;
        this.min = min;
        this.max = max;
        this.toBytesFn = toBytesFn;
        this.assertInvariants(values);
        this.values = Object.freeze([...values]);
        this.endian = endian;
    }
    assertInvariants(values) {
        values.forEach(value => {
            assert(value >= this.min && value <= this.max, `value must be an integer between ${this.min} and ${this.max}`);
        });
    }
    computeBufferSize() {
        return this.values.length * this.width;
    }
    get() { return [...this.values]; }
    set(values) {
        this.assertInvariants(values);
        this.values = Object.freeze([...values]);
    }
    toUint8Array() {
        return this.toBytesFn(this.values, this.endian === Endian.Little);
    }
}


/////////////////////////////////////////////////////
// the implementation of the F32Type
/////////////////////////////////////////////////////

const IEEE754_FLOAT32_MAX = (2 - (2 ** -23)) * (2 ** 127);
const IEEE754_FLOAT32_MIN = IEEE754_FLOAT32_MAX * -1;

const f32sTou8s = (vals: number[], isLittleEndian: boolean) => {
  const stride = 4;
  const buff = new Uint8Array(vals.length * stride);
  for (let [i, val] of vals.entries()) {
    floatWrite(buff, val, i * stride, isLittleEndian, 23, 4);
  }
  return buff;
}

export class F32Type extends FloatField {
  constructor(value: number, endian: Endian = Endian.Little) {
    super(4, IEEE754_FLOAT32_MIN, IEEE754_FLOAT32_MAX, f32sTou8s, value, endian);
  }
}

export class F32sType extends FloatArrayField {
  constructor(values: number[], endian: Endian = Endian.Little) {
    super(4, IEEE754_FLOAT32_MIN, IEEE754_FLOAT32_MAX, f32sTou8s, values, endian);
  }
}

export const F32 = (value: number, endian: Endian = Endian.Little) => new F32Type(value, endian);
export const F32s = (values: number[], endian: Endian = Endian.Little) => new F32sType(values, endian);
