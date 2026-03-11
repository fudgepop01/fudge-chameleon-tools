// export type RecursiveOmit<T, K extends PropertyKey> = T extends object
//   ? { [P in keyof T as Exclude<P, K>]: RecursiveOmit<T[P], K> }
//   : T;

export type RecursiveOmit<T, K extends PropertyKey> = T extends (infer U)[]
  ? RecursiveOmit<U, K>[] // Handle arrays first to preserve array-ness
  : T extends object
  ? {
      [P in keyof T as P extends K ? never : P]: RecursiveOmit<T[P], K>;
    }
  : T;

export type CleanKStruct<T> = RecursiveOmit<T, '_io' | '_parent' | '_read' | '_root' | '_is_le'>