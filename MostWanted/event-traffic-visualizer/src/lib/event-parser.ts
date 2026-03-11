import KaitaiStream from 'kaitai-struct/KaitaiStream';
import { Event as GameEvents } from "./event";

export default async () => {
    const res = await (await fetch('5B_5D_04_00.dat')).blob();
    const events = new GameEvents(new KaitaiStream(await res.arrayBuffer()));
    return events;
}