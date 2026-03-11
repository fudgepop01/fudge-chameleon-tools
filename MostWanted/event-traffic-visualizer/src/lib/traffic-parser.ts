import KaitaiStream from 'kaitai-struct/KaitaiStream';
import { Traffic } from "./traffic";

export default async () => {
    const res = await (await fetch('4C_FF_E4_1F.dat')).blob();
    const traffic = new Traffic(new KaitaiStream(await res.arrayBuffer()));
    return traffic;
}