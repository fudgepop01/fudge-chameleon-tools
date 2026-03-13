import { readFile, writeFile } from "fs/promises";
import { Hsm } from "./hsm";
import KaitaiStream from "kaitai-struct/KaitaiStream"
import { CleanKStruct } from "../helpers/recursiveOmit";

const ParseHsmFile = async () => {
    // change this to the HSM file you're looking to parse
    const res = (await readFile(__dirname + '/E8_F1_0E_00.dat'));
    const HSM = new Hsm(new KaitaiStream(res));
    return HSM;
}
const out = [];
let indent = 0;
const pushOut = (str: any) => {
    out.push(''.padStart(indent * 2, ' ') + str);
}

const parseStructureArgument = (params: CleanKStruct<Hsm.GameGameLogicHsmDataHsmParameter>[]) => {
    for (const [_idx, param] of params.entries()) {
        pushOut(`params[${_idx}]`);
        indent ++;
        for (const [__idx, val] of param.parameterValues.entries()) {
            switch (val.paramType) {
                case Hsm.EHsmParamType.STRING: {
                    const data = (val.param as Hsm.Ptr).data.data;
                    pushOut(`${__idx}: String: ${data}`)
                } break;
                case Hsm.EHsmParamType.INT: {
                    const data = (val.param as Hsm.Ptr).data.data;
                    pushOut(`${__idx}: Int: ${data}`)
                } break;
                case Hsm.EHsmParamType.FLOAT: {
                    const data = (val.param as Hsm.Ptr).data.data;
                    pushOut(`${__idx}: Float: ${data}`)
                } break;
                case Hsm.EHsmParamType.ID: {
                    const data = val.param as number;
                    pushOut(`${__idx}: ID: ${data}`)
                } break;
                case Hsm.EHsmParamType.BOOL: {
                    const data = (val.param as Hsm.Ptr).data.data;
                    pushOut(`${__idx}: Bool: ${data}`)
                } break;
                case Hsm.EHsmParamType.ASSET_REFERENCE: {
                    const data = (val.param as Hsm.Ptr).data.data;
                    pushOut(`${__idx}: Reference: ${data}`)
                } break;
                case Hsm.EHsmParamType.STRUCTURE: {
                    pushOut(`${__idx}: Structure:`)
                    indent ++;
                    parseStructureArgument((val.param as Hsm.GameGameLogicHsmDataHsmStructureInstance).parameters);
                    indent --;
                } break;
                case Hsm.EHsmParamType.INVALID: {
                    pushOut(`${__idx}: INVALID`);
                } break;
            }
        }
        indent --;
    }
}

const main = async () => {
    const parsed = await ParseHsmFile() as CleanKStruct<Hsm>;

    for (const [idx, defs] of parsed.stateDefinitions.entries()) {
        pushOut(defs.mpcDebugStateDefinitionName0x18.data.data)
        indent ++;
        pushOut('state entry points:')
        indent ++;
        for (const [_idx, entryPoints] of defs.stateEntryPoints.entries()) {
            pushOut(`[${_idx}]`)
            indent ++;
            for (const [__idx, csp] of entryPoints.childSpawnData.entries()) {
                pushOut(csp.mpcDebugStateDefinitionName0xc.data.data);
            }
            indent --;
        }
        indent --;
        pushOut('state exit points:')
        indent ++;
        for (const [_idx, exitData] of defs.childExitData.entries()) {
            pushOut(`[${_idx}]: ` + exitData.mpcDebugStateDefinitionName0xc.data.data);
            if (exitData.miNumChildExitPoints0x8 > 0) {
                indent ++;
                pushOut('child exit point spawn data:')
                indent ++;
                for (const [__idx, exitPoint] of exitData.childExitPoints.entries()) {
                    for (const [___idx, spawnData] of exitPoint.childSpawnData.entries()) {
                        pushOut(`[${__idx}, ${___idx}]: ` + spawnData.mpcDebugStateDefinitionName0xc.data.data);
                    }
                }
                indent --;
                indent --;
            }
        }
        indent --;
        if (defs.parameters.length > 0) {
            pushOut('parameters:');
            indent ++;
            parseStructureArgument(defs.parameters);
            indent --;
        } else {
            pushOut('no parameters');
        }
        indent--;
    }
    
    // write state defs    
    await writeFile(__dirname + '/stateDefs.txt', out.join('\n'), 'ascii');
    out.length = 0;

    for (const [idx, ddef] of parsed.dataDefinitions.entries()) {
        pushOut('path: "' + ddef.mpcPath0x4.data.data + '"');
        pushOut(JSON.stringify(JSON.parse(ddef.mpData0x8.data.data as string), null, 2));
        pushOut('-----');
    }

    await writeFile(__dirname + '/dataDefs.txt', out.join('\n'), 'ascii');
    out.length = 0;

    for (const [idx, bface] of parsed.behaviourInterfaces.entries()) {
        pushOut('name: ' + bface.mpcDebugName0x8.data.data);
        indent ++;
        pushOut('param count: ' + bface.parameters.length);
        indent --;
    }

    await writeFile(__dirname + '/behaviourInterfaceDefs.txt', out.join('\n'), 'ascii');
}

main();


