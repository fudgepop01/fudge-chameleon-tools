import { Vector3, Euler, Camera, Quaternion } from "three"

interface IEditorCamState {
    camSpeed: number;
    cameraPosition: Vector3;
    cameraQuaternion: Quaternion;
}

export default class EngineEditorCamera
{
    public camera: Camera;
    public domElement: HTMLElement;
    public readonly PI_2: number = Math.PI / 2;
    public euler: Euler;
    public vec: Vector3;
    public cameraForward: Vector3;
    private _rcPressed: boolean;
    public pressedKeyMap: {[key: string]: boolean};
    
    public CAM_SPEED: number;

    public editorCamState: IEditorCamState;
    public shiftSpeedMulti: number;
    public lastUpdateTime: number;

    constructor(camera: Camera, domElement: HTMLElement)
    {
        this.camera = camera;
        this.domElement = domElement;
        this.PI_2 = Math.PI / 2;
        this.euler = new Euler(0, 0, 0, 'YXZ');
        this.vec = new Vector3();
        this.cameraForward = new Vector3();
        this._rcPressed = false;
        this.CAM_SPEED = 5;
        this.lastUpdateTime = 0;
        this.pressedKeyMap = {
            w: false, // w
            a: false, // a
            s: false, // s
            d: false, // d
            q: false, // q
            e: false, // e
            shift: false // shift
        };

        window.addEventListener('keydown', this.onKeyDown.bind(this), false);
        window.addEventListener('keyup', this.onKeyUp.bind(this), false);
        window.addEventListener('mousedown', this.onMouseDown.bind(this), false);
        window.addEventListener('mouseup', this.onMouseUp.bind(this), false);
        window.addEventListener('mousemove', this.onMouseMove.bind(this), false);
        window.addEventListener('wheel', this.onMouseWheel.bind(this), {passive: false});

        //disable rClick
        document.oncontextmenu = (e) =>
        {
            if (e.preventDefault != undefined) e.preventDefault();
            if (e.stopPropagation != undefined) e.stopPropagation();
        }
        // this.retrieveSessionData();
    }

    // setSessionData() 
    // {

    //     this.editorCamState = {
    //         camSpeed: this.CAM_SPEED,
    //         cameraPosition: this.camera.position,
    //         cameraQuaternion: this.camera.quaternion
    //     }
    //     window.localStorage.setItem('camState', JSON.stringify(this.editorCamState));
    //     // console.log("saving editor camera session data");
    // }

    // retrieveSessionData() 
    // {
    //     const camState = JSON.parse(window.localStorage.getItem('camState'));
    //     if (camState == null)
    //     {
    //         this.CAM_SPEED = 0.05;
    //         this.setSessionData();
    //         return;
    //     }

    //     this.CAM_SPEED = "camSpeed" in camState ? camState["camSpeed"] : 0.05;
    //     this.camera.position.copy("cameraPosition" in camState ? camState["cameraPosition"] : new Vector3());
    //     this.camera.applyQuaternion("cameraQuaternion" in camState ? camState["cameraQuaternion"] : new Vector3());
    //     // console.log("loading editor camera session data");
    // }

    update(rawTime: number)
    {
        const deltaTime = 60 * ((rawTime - this.lastUpdateTime) / 1000);
        this.lastUpdateTime = rawTime;
        this.shiftSpeedMulti = this.pressedKeyMap.shift ? 2 : 1;
        if (this.pressedKeyMap.w) this.moveForward(this.CAM_SPEED * this.shiftSpeedMulti * deltaTime);
        if (this.pressedKeyMap.s) this.moveForward(-this.CAM_SPEED * this.shiftSpeedMulti * deltaTime);
        if (this.pressedKeyMap.e) this.moveUp(this.CAM_SPEED * this.shiftSpeedMulti * deltaTime);
        if (this.pressedKeyMap.q) this.moveUp(-this.CAM_SPEED * this.shiftSpeedMulti * deltaTime);
        if (this.pressedKeyMap.d) this.moveRight(this.CAM_SPEED * this.shiftSpeedMulti * deltaTime);
        if (this.pressedKeyMap.a) this.moveRight(-this.CAM_SPEED * this.shiftSpeedMulti * deltaTime);
    }

    onKeyDown(event: KeyboardEvent)
    {
        // console.log(event.key.toLowerCase());
        this.pressedKeyMap[event.key.toLowerCase()] = (event.key.toLowerCase() in this.pressedKeyMap);
    };
    onKeyUp(event: KeyboardEvent) { this.pressedKeyMap[event.key.toLowerCase()] = !(event.key.toLowerCase() in this.pressedKeyMap); };

    onMouseDown(event: MouseEvent)
    {
        if (event.button == 2)
        {
            this._rcPressed = true;
            this.domElement.requestPointerLock = this.domElement.requestPointerLock ||
                this.domElement["mozRequestPointerLock"];
            this.domElement.requestPointerLock()
        }
    }

    onMouseUp(event: MouseEvent)
    {
        if (event.button == 2)
        {
            this._rcPressed = false;
            document.exitPointerLock();
            // this.setSessionData();
        }
    }

    moveForward(distance: number)
    {
        this.camera.getWorldDirection(this.cameraForward);
        this.camera.position.addScaledVector(this.cameraForward, distance);
    }

    moveRight(distance: number)
    {
        this.vec.setFromMatrixColumn(this.camera.matrix, 0);
        this.camera.position.addScaledVector(this.vec, distance);
    }

    moveUp(distance: number)
    {
        this.vec.setFromMatrixColumn(this.camera.matrix, 1)
        this.camera.position.addScaledVector(this.vec, distance);
    }

    onMouseMove(event: MouseEvent)
    {
        if (!this._rcPressed) return;
        const movementX = event.movementX || event["mozMovementX"] || event["webkitMovementX"] || 0;
        const movementY = event.movementY || event["mozMovementY"] || event["webkitMovementY"] || 0;
        this.euler.setFromQuaternion(this.camera.quaternion);
        this.euler.y -= movementX * 0.008;
        this.euler.x -= movementY * 0.008;
        this.euler.x = Math.max(- this.PI_2, Math.min(this.PI_2, this.euler.x));
        this.camera.quaternion.setFromEuler(this.euler);
    }

    onMouseWheel(event: WheelEvent)
    {
        console.log({
            pos: this.camera.position,
            quat: this.camera.quaternion
        })
        event.preventDefault();
        this.CAM_SPEED = Math.max(0.01, this.CAM_SPEED -= event.deltaY * 0.01);
        // if (this._rcPressed) this.CAM_SPEED = Math.max(0.01, this.CAM_SPEED -= event.deltaY * 0.0001);
        // else this.moveForward(this.CAM_SPEED * -event.deltaY / 10);
    }
}