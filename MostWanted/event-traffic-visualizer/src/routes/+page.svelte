<script lang="ts">
    import type { Traffic } from "$lib/traffic";
    // import type * as Plotly from 'plotly.js';
    // import * as PlotlyDist from 'plotly.js-dist';
    import trafficParserBuilder from "$lib/traffic-parser";
    import eventParserBuilder from "$lib/event-parser";
    import checkpointDataFetcher from "$lib/checkpointData";
    import { onMount } from "svelte";
    import * as THREE from 'three';
    import EngineEditorCamera from "$lib/EngineCamera";
    import type { Checkpoints, IBoxCheckpointData, Races } from "$lib/checkpointData";
    import type { Event as GameEvents } from "$lib/event";
    

    let trafficParser: Traffic = $state();
    let checkpoints: Checkpoints = $state();
    let gameEvents: GameEvents = $state();
    let races: Races = $state({});
    let selectedRace: string = $state("");
    let eventInfo: any = $state({});
    let customRoute: number[] = $state([]);
    let mouseButton: number = $state(-1);
    // let plotly = PlotlyDist as typeof Plotly;
    onMount(async () => {
        trafficParser = await trafficParserBuilder();
        const eventData = await checkpointDataFetcher();
        gameEvents = await eventParserBuilder();
        checkpoints = eventData.checkpoints;
        races = eventData.races;
    })
    let container: HTMLCanvasElement;
    let infoPopup: HTMLDivElement;

    let scene: THREE.Scene;
    let camera: THREE.PerspectiveCamera;
    let renderer: THREE.WebGLRenderer;
    let raycaster: THREE.Raycaster;
    let checkpointMeshes: THREE.Object3D[] = [];
    const sceneMeshMap: Map<number, {mesh: THREE.Mesh, originalMat: THREE.Material}> = new Map();
    let meshIDSet: Set<number> = new Set();
    let mouseLocation: THREE.Vector2 = new THREE.Vector2(0, 0);
    let mouseClientLoc: [number, number] = $state([0, 0]);
    let checkpointDataDisplay: string = $state("");
    let cameraKeysPressed: Set<string> = new Set();
    // const scene = new THREE.Scene();

    const genColor = (minBrightness: number, maxBrightness: number = 255) => {
        const maxMul = (maxBrightness - minBrightness);
        const r = (minBrightness + Math.floor(Math.random() * maxMul));
        const g = (minBrightness + Math.floor(Math.random() * maxMul));
        const b = (minBrightness + Math.floor(Math.random() * maxMul));
        // console.log(r, g, b);
        // console.log((r + (g << 8) + (b << 16)).toString(16));
        return (r + (g << 8) + (b << 16));
    }


    // Dismiss this for now, we'll cover generators soon
    $effect(() => {
        if (trafficParser === undefined) return;
        if (races === undefined) return;
        if (gameEvents === undefined) return;
        // if (selectedRace.length === 0) return;
        // if (plotly === undefined) return;
        
        if (!scene) {
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 10000 );
            renderer = new THREE.WebGLRenderer({canvas: container});
            renderer.setSize(window.innerWidth, window.innerHeight);

            raycaster = new THREE.Raycaster();
            
            camera.position.set(0, 3920, 5);
            camera.quaternion.set(-0.4537693038710365, 0.5458332582394273, 0.5119719180322186, 0.4837811780242559);
    
            const controls = new EngineEditorCamera(camera, container);
            // controls.update();

            // controls.update();
            // container.appendChild(renderer.domElement)
            container.addEventListener("mousemove", (evt) => {
                mouseLocation.setX((evt.offsetX / container.clientWidth) * 2 - 1);
                mouseLocation.setY((evt.offsetY / container.clientHeight) * -2 + 1);
                mouseClientLoc = [evt.pageX, evt.pageY];
                // mouseClientLoc[1] = evt.pageY;
                document.body.style.setProperty('--mouseClientX', `${mouseClientLoc[0]}`);
                document.body.style.setProperty('--mouseClientY', `${mouseClientLoc[1]}`);
                // document.body.style = `--mouseClientX=${} --mouseClientY=${mouseClientLoc[1]}`
            });

            const moveCamera = () => {
                if (cameraKeysPressed.size === 0) return;

                const p = new THREE.Vector3();
                camera.getWorldPosition(p);
                const speed = 10;
                const direction = new THREE.Vector3();
                camera.getWorldDirection(direction);
                const worldQuat = new THREE.Quaternion();
                camera.getWorldQuaternion(worldQuat);

                const moveX = (new THREE.Vector3()).copy(direction);
                // const quat = new THREE.Quaternion(0, -1, 0, 1).normalize();
                // const halfQuat = new THREE.Quaternion(0, 0, 0, 0);
                // const quat = new THREE.Quaternion;
                moveX.applyQuaternion(worldQuat);
                moveX.multiplyScalar(speed);

                // const moveF = (new THREE.Vector3()).copy(direction);
                // const moveF = (new THREE.Vector3()).copy(direction);
                const moveF = (new THREE.Vector3()).copy(direction);
                moveF.multiplyScalar(speed);

                if (cameraKeysPressed.has('w')) {
                    camera.position.add(moveF);
                }
                else if (cameraKeysPressed.has('s')) {
                    camera.position.sub(moveF);
                }
                
                const vecRight = new THREE.Vector3(-speed, 0, 0);
                vecRight.applyQuaternion(worldQuat);
                if (cameraKeysPressed.has('d')) {
                    camera.position.sub(vecRight);
                } else if (cameraKeysPressed.has('a')) {
                    camera.position.add(vecRight);
                }

                if (cameraKeysPressed.has('ArrowLeft')) {
                    camera.rotateY(0.1);
                } else if (cameraKeysPressed.has('ArrowRight')) {
                    camera.rotateY(-0.1);
                }

                if (cameraKeysPressed.has('ArrowUp')) {
                    camera.rotateX(0.1);
                } else if (cameraKeysPressed.has('ArrowDown')) {
                    camera.rotateX(-0.1);
                }
            }
            container.addEventListener("keydown", (evt) => {
                cameraKeysPressed.add(evt.key);
            })
            container.addEventListener("keyup", (evt) => {
                cameraKeysPressed.delete(evt.key);
            })
    
            const animate: XRFrameRequestCallback = (time: number) => {
                // console.log(time);
                controls.update(time);
                // moveCamera();
                renderer.render(scene, camera);
                raycaster.setFromCamera(mouseLocation, camera);

                const foundObjects = raycaster.intersectObjects(checkpointMeshes);
                // console.log(raycaster.params);
                const highlightMesh = new THREE.MeshBasicMaterial({color: 0xFFFFFF });
                
                for (const id of meshIDSet) {
                    (scene.getObjectById(id) as THREE.Mesh).material = sceneMeshMap.get(id).originalMat;
                }

                checkpointDataDisplay = "";
                meshIDSet.clear();
                // for (const obj of foundObjects) {
                if (foundObjects.length > 0) {
                    const obj = foundObjects[0];
                    if ((obj.object as any).isMesh) {
                        const mesh = obj.object as THREE.Mesh;
                        // console.log(mesh.geometry.attributes.colors.array);
                        meshIDSet.add(mesh.id);
                        mesh.material = highlightMesh;
                        if (mesh.userData.eventName) {
                            checkpointDataDisplay = mesh.userData.eventName;
                        }
                        if (mouseButton == 0 && mesh.userData.ID) {
                            if (customRoute[customRoute.length - 1] !== mesh.userData.ID) {
                                customRoute.push(mesh.userData.ID);
                            }
                        } else if (mouseButton == 2 && mesh.userData.ID) {
                            if (customRoute[customRoute.length - 1] === mesh.userData.ID) {
                                customRoute.pop();
                            }
                        }
                        // const color = mesh.geometry.setAttribute('color', new THREE.BufferAttribute([0xFFFFFF], 1));
                    }
                }
                // }
                
                // lineMaterial.color.setHex(lineMaterial.color.getHex() + 1);
            }
            renderer.setAnimationLoop(animate);
        }

        // const scene = new THREE.Scene();
        scene.clear();
        // removes all checkpoints
        checkpointMeshes.splice(0, checkpointMeshes.length);

        const lineMaterial = new THREE.LineBasicMaterial( { color: 0x00ff00 });


        const lines: THREE.Line[] = [];
        
        // const traces = [] as Partial<Plotly.PlotData>[];

        // // Pick a DOM element to draw the graph in

        // console.log(trafficParser.mpapHullsPtrPtr.ptrTable.entries.map(p => p.data.data));

        // console.log(trafficParser);
        const hullData = trafficParser.mpapHullsPtrPtr.ptrTable.entries.map(p => p.data.data as Traffic.GameTrafficHull);
        for (const [idx, hull] of Object.entries(hullData)) {
            if (hull.muNumSections === 0) continue;
            // const hullMaterial = new THREE.LineBasicMaterial({ color: 0x555555 });
            const hullMaterial = new THREE.LineBasicMaterial({ color: genColor(20, 100) });
            // console.log(idx, hull);
            const rungs = Object.values(hull.mpaRungs.entries.map(p => p.data as Traffic.GameTrafficLaneRung));
            const sections = hull.mpaSections.entries.map(p => p.data as Traffic.GameTrafficSection);
            let points: THREE.Vector3[] = [];

            const keyIndices = sections.map(v => v.muNumRungs);
            let lastIndex = 0;
            let sectionIndex = 0;
            for (let i = 0; i < rungs.length; i ++) {
                // if (idx > 1) break;
                if (i == keyIndices[sectionIndex] + lastIndex) {
                    lastIndex = i;
                    sectionIndex += 1;
                    // console.log(keyIndices);
                    // console.log("next thing: " + (lastIndex + keyIndices[sectionIndex]));
                    
                    lines.push(new THREE.Line(new THREE.BufferGeometry().setFromPoints( points ), hullMaterial));
                    points = [];
                }
                points.push(new THREE.Vector3(
                    rungs[i].maPoints[0].x,
                    rungs[i].maPoints[0].y,
                    rungs[i].maPoints[0].z
                ));
            }
            lines.push(new THREE.Line(new THREE.BufferGeometry().setFromPoints( points ), hullMaterial));
            // camera.near = 0.1;
            // camera.frustumCulled =false;
            // camera.far = 100000;
            // camera.position.set(points[0].x, points[0].y, points[0].z);
            // camera.lookAt(points[0].x, points[0].y, points[0].z);
            // break;
        }

        for (const [idx, line] of Object.entries(lines)) {
            // const line = new THREE.Line( geo, ) );
            // console.log(line);
            
            scene.add( line );
        }

        if (selectedRace === "ALL_CHECKPOINTS") {
            const spheres: THREE.Mesh[] = [];
            const checkpointBoxes: THREE.Mesh[] = [];

            const boxColor = new THREE.MeshBasicMaterial({color: 0xFFFFFF, wireframe: true})
            for (const [racename, checkpointIDs] of Object.entries(races)) {
                const mat = new THREE.MeshBasicMaterial({color: genColor(80), wireframe: false});
                
                for (const id of checkpointIDs.checkpoints) {
                    const pos = checkpoints[id].position;
                    const dimension = checkpoints[id].dimension;
                    const rotation = checkpoints[id].rotation;
                    
                    if (isNaN(pos.x)) {
                        console.log(id);
                        continue;
                    }

                    let size = 10.0;
                    const sphereData = new THREE.SphereGeometry(size, 4, 4);

                    const sphere = new THREE.Mesh(sphereData, mat);
                    sphere.position.set(pos.x, pos.y, pos.z);
                    sphere.userData.eventName = racename;
                    sphere.userData.ID = id;

                    spheres.push(sphere);

                    const boxData = new THREE.BoxGeometry(dimension.x, dimension.y, dimension.z);
                    const box = new THREE.Mesh(boxData, boxColor);
                    box.position.set(pos.x, pos.y, pos.z);
                    box.setRotationFromQuaternion(new THREE.Quaternion(
                        rotation.x,
                        rotation.y,
                        rotation.z,
                        rotation.w
                    ));

                    checkpointBoxes.push(box);
                }
            }
            
            for (const [idx, sphere] of Object.entries(spheres)) {
                checkpointMeshes.push(sphere);
                scene.add(sphere);
                sceneMeshMap.set(sphere.id, {
                    mesh: sphere,
                    originalMat: sphere.material as THREE.Material
                });
                // console.log(sphere.isObject3D);
                for (const [idx, box] of Object.entries(checkpointBoxes)) {
                    scene.add(box);
                }
            }
        }
        else if (selectedRace.length !== 0) {
            const spheres: THREE.Mesh[] = [];
            const checkpointBoxes: THREE.Mesh[] = [];

            const mat = new THREE.MeshBasicMaterial({color: 0xFF0000, wireframe: true});
            const startColor = new THREE.MeshBasicMaterial({color: 0x00FF00});
            const endColor = new THREE.MeshBasicMaterial({color: 0xFFFF00});

            const boxColor = new THREE.MeshBasicMaterial({color: 0xFFFFFF, wireframe: true});
            // console.log(races);
            const lastIdx = races[selectedRace].checkpoints.length - 1;
            for (const [idx, checkpoint] of races[selectedRace].checkpoints.entries()) {
                const pos = checkpoints[checkpoint].position;
                const dimension = checkpoints[checkpoint].dimension;
                const rotation = checkpoints[checkpoint].rotation;

                let size = 5.0;
                if (idx === 0 || idx === lastIdx) size = 10.0
                const sphereData = new THREE.SphereGeometry(size, 4, 4);

                let matChoice = mat;
                if (idx === 0) matChoice = startColor;
                else if (idx === lastIdx) matChoice = endColor;
                const sphere = new THREE.Mesh(sphereData, matChoice);
                sphere.position.set(pos.x, pos.y, pos.z);      
                sphere.userData.eventName = `${selectedRace}\n${checkpoint}`;
                sphere.userData.ID = checkpoint;
                spheres.push(sphere);

                const boxData = new THREE.BoxGeometry(dimension.x, dimension.y, dimension.z);
                const box = new THREE.Mesh(boxData, boxColor);
                box.position.set(pos.x, pos.y, pos.z);
                box.setRotationFromQuaternion(new THREE.Quaternion(
                    rotation.x,
                    rotation.y,
                    rotation.z,
                    rotation.w
                ));



                checkpointBoxes.push(box);
            }
    
            for (const [idx, sphere] of Object.entries(spheres)) {
                checkpointMeshes.push(sphere);
                scene.add(sphere);
                sceneMeshMap.set(sphere.id, {
                    mesh: sphere,
                    originalMat: sphere.material as THREE.Material
                });
            }

            for (const [idx, box] of Object.entries(checkpointBoxes)) {
                scene.add(box);
            }

            // scene.add(scene.add(new THREE.ArrowHelper(raycaster.ray.direction, raycaster.ray.origin, 300, 0xff0000) ));
        }

        renderer.render( scene, camera );

        if (races[selectedRace]) {
            const fullEvtData = (gameEvents.allEvents[races[selectedRace].evtIndex].data.data as GameEvents.EventSwitcher).offlineEvent;
            // console.log(fullEvtData);
            // console.log(gameEvents.allEvents);
            // eventInfo.cycleTimeOfDay = fullEvtData.baseObject.cycleTimeOfDay0x28;
            // eventInfo.finishTimeOfDay = fullEvtData.baseObject.finishTimeOfDay0x2c
            // eventInfo.gameMode = fullEvtData.baseObject.gameMode0x1c;
            // eventInfo.gamePack = fullEvtData.baseObject.gamePack0x20
            // eventInfo.isAlternativeWeather = fullEvtData.baseObject.isAlternativeWeather0x44
            // eventInfo.isRainActive = fullEvtData.baseObject.isRainActive0x45
            // eventInfo.isThunderActive = fullEvtData.baseObject.isThunderActive0x46
            // eventInfo.overrideSunDirection = fullEvtData.baseObject.overrideSunDirection0x47
            // eventInfo.roadSurfaceCondition = fullEvtData.baseObject.roadSurfaceCondition.typeToDisplay
            // eventInfo.roadSurfaceConditionValue = fullEvtData.baseObject.roadSurfaceConditions
            // eventInfo.sunDirection = fullEvtData.baseObject.sunDirection0x30

            // eventInfo.allowedVehicles = fullEvtData.allowedVehicleList0x5c;
            // eventInfo.defaultHeatLevels = fullEvtData.defaultHeatLevels0x6c?.join(", ");
            // eventInfo.copSpawning = fullEvtData.copSpawning0xe8;
            // eventInfo.demoMode = fullEvtData.demoMode;
            // eventInfo.laps = fullEvtData.laps0xf6;
            // eventInfo.nitrousAllowed = fullEvtData.nitrousAllowed0xec;
            // eventInfo.noRacingLineTraffic = fullEvtData.noRacingLineTraffic0xed;
            // eventInfo.startWithEngineOn = fullEvtData.startWithEngineOn0xef;
            // eventInfo.targetScore = fullEvtData.targetScore0xcc;
            // eventInfo.targetSpeed = fullEvtData.targetSpeed0xa8?.join(', ');
            // eventInfo.targetTime = fullEvtData.targetTime0xac?.join(', ');
            // eventInfo.trafficDensity = fullEvtData.trafficDensity0xb0;
            // eventInfo.trafficEnabled = fullEvtData.trafficEnabled0xf0;
            // eventInfo.trafficOverrides = fullEvtData.trafficOverrides0x4c?.values().map(v => '0b' + v.toString(2).padStart(8, '0')).toArray().join(', ');
            // eventInfo.weaponsAllowed = fullEvtData.weaponsAllowed0xf2;
            // if (fullEvtData.checkpoints0x64.length) {
            //     eventInfo.firstCheckpointId = fullEvtData.checkpoints0x64[0];
            //     eventInfo.checkpointCount = fullEvtData.checkpoints0x64.length;
            //     // eventInfo.aihintsCount = fullEvtData.aiHints0x58.length;
            // }
            eventInfo.bool0x48 = fullEvtData.baseObject.bool0x48;
            eventInfo.float0x38 = fullEvtData.baseObject.float0x38;
            eventInfo.uint80x4a = fullEvtData.baseObject.uint80x4a;
            eventInfo.uniqueId0x24 = fullEvtData.baseObject.uniqueId0x24;

            eventInfo.uniqueId0x60 = fullEvtData.uniqueId0x60;
            eventInfo.uniqueId0x68 = fullEvtData.uniqueId0x68;
            eventInfo.uniqueId0x80 = fullEvtData.uniqueId0x80;
            eventInfo.uniqueId0x90 = fullEvtData.uniqueId0x90;

            eventInfo.bool0xe9 = fullEvtData.bool0xe9;
            eventInfo.bool0xea = fullEvtData.bool0xea;
            eventInfo.bool0xeb = fullEvtData.bool0xeb;
            eventInfo.bool0xee = fullEvtData.bool0xee;
            eventInfo.bool0xf1 = fullEvtData.bool0xf1;
            // console.log($state.snapshot(eventInfo));
        }
    });

</script>

<svelte:window on:mousedown={(mEvent: MouseEvent) => { mouseButton = mEvent.button }} on:mouseup={() => { mouseButton = -1; }} />

<div id="infoPopup" bind:this={infoPopup}>{@html checkpointDataDisplay}</div>
<canvas tabindex="0" id="vis-container" bind:this={container} style="width: 100%; height: 1000px"></canvas>

<select onchange={(v) => selectedRace = (v.target as HTMLSelectElement).value}>
    <option value="ALL_CHECKPOINTS">_ALL_</option>
    {#each Object.entries(races) as [race, val]}
        <option value="{race}">({val.kind}) {race}</option>
    {/each}
</select>

<div id="detailedInfo">
    <!-- {JSON.stringify(customRoute)} -->
    {JSON.stringify(eventInfo, null, 2)}
</div>

<style>
#infoPopup {
    display: block;
    border: 1px solid white;
    font-family: 'Courier New', Courier, monospace;
    color: white;
    white-space: pre;
    background-color: black;

    min-width: 10px;
    min-height: 10px;

    position: absolute;
    left: calc(var(--mouseClientX) * 1px + 10px);
    top: calc(var(--mouseClientY) * 1px - 10px);
    user-select: none;
    pointer-events: none;
    /* transition: all .2s ease; */
}

#vis-container {
    display: block;
    position: fixed;
    left: 0;
    top: 0;
    z-index: -1;
}

#detailedInfo {
    display: block;
    border: 1px solid white;
    font-family: 'Courier New', Courier, monospace;
    color: white;
    white-space: pre;
    background-color: black;
}
</style>