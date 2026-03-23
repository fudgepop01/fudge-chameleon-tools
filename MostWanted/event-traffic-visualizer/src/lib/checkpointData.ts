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

export interface GameplayTriggerAIPlayer {
    placement: number;
    id: number;
    idhash: string;
    type: number;
}

export interface GameplayTriggerOutputRoadblock {
    id: number;
    idhash: string;
    placement: number;
    type: number;
}

export interface GameplayTriggerOutput {
    predicate?: string;
    roadblocks: GameplayTriggerOutputRoadblock[];
    aiplayers: GameplayTriggerAIPlayer[];
}

export interface GameplayTriggers {
    [key: number]: {
        idx: number;
        id: number;
        idhash: string;
        predicate?: string
        inputTriggers?: number[];
        addToMinimap: boolean;
        outputs: GameplayTriggerOutput[];
    }
}

export interface CopAITypes {
    [key: number]: {
        _formation: string;
        playerType: number;
        bool0x14: number;
        gameChangerId: number;
        canSpawnBehind: number;
        canSpawnHeadOn: number;
        canSpawnIntercepting: number;
        bool0x18: number;
        bool0x19: number;
    }
}

export interface AIPlayerTypes {
    [key: number]: {
        idx: number;
        id: number;
        rolloutID: number;
        aggressionType: number;
        enum0xa8: number;
        weavingType: number;
        behaviour: number;
        allowedToRespawn: number;
        canRhino: number;
        bool8T0x86: number;
        nitrousUsage: number;
        doUturns: number;
        isAggressor: number;
        isBlacklist: number;
        isCop: number;
    }
}

export interface RolloutTypes {
    [key: number]: {
        idx: number;
        id: number;
        name: number;
        vehicle: string | number;
        colour: number;
        bodyUpgrade: number;
        chassisUpgrade: number;
        nitrousUpgrade: number;
        characters?: number[];
        uniqIdInst?: number[];
        isOnlineRollout: number;
        isPlayerRollout: number;
        weaponData: {
            weaponID: number;
            weaponUpgrades?: number[];
        };
    }
}

export interface TriggersById {
    [key: number]: {
        kind: number,
        LEHash: string,
        type: "locator" | "box" | "sphere",
        data: {
            position: {
                x: number;
                y: number;
                z: number;
            },
            rotation?: {
                w: number;
                x: number;
                y: number;
                z: number;
            }
            radius?: number
            dimension?: {
                x: number;
                y: number;
                z: number;
            }
            direction?: {
                w: number;
                x: number;
                y: number;
                z: number;
            }
        }
    }
}

export default async () => {
    const checkpoints: Checkpoints = (await (await fetch('checkpoint-results.json')).json()).boxes;
    const races: Races = (await (await fetch('all-races.json')).json());
    const gameplayTriggers: GameplayTriggers = (await (await fetch('gameplay-trigger-data-collection.json')).json());
    const copAiTypes: CopAITypes = (await (await fetch('cop-ai-types.json')).json());
    const aiPlayerTypes: AIPlayerTypes = (await (await fetch('player-type-data.json')).json());
    const rolloutTypes: RolloutTypes = (await (await fetch('rollout-types.json')).json());
    const triggersById: TriggersById = (await (await fetch('trigger-byid-results.json')).json());
    return {checkpoints, races, gameplayTriggers, copAiTypes, aiPlayerTypes, rolloutTypes, triggersById};
}