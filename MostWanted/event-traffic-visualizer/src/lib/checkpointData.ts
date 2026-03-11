interface ICheckpointData {
    LEHash: string;
    position: {x: number, y: number, z: number};
};

export interface IBoxCheckpointData extends ICheckpointData {
    dimension: {x: number, y: number, z: number};
    rotation: {w: number, x: number, y: number, z: number};
}

export interface Checkpoints {
    [key: number]: IBoxCheckpointData
}

export interface Races {
    [key: string]: {
        checkpoints: number[];
        evtIndex: number;
        kind: string;
        triggers: number[];
    }
}


export default async () => {
    const checkpoints: Checkpoints = (await (await fetch('checkpoint-results.json')).json()).boxes;
    const races: Races = (await (await fetch('all-races.json')).json());
    return {checkpoints, races};
}