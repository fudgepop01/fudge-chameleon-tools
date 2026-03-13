# What is this?

This is a repository for me (Fudgepop01) to upload various tools I have made for the Chameleon game engine. The Chameleon Engine was by Criterion Games in the production of Burnout Paradise, Need for Speed: Hot Pursuit, Need for Speed: Most Wanted (2012), and Need for Speed: Hot Pursuit (Remastered).

My main focus is NFSMW 2012, but I believe some of these tools can be repurposed and modified to be work for the other titles as well.

Most of these things were made without the idea of other folks using it in mind until I come up with something more robust, but I figure it's good to have _something_ here in case I lose interest later.

The main technology I use is
- [NodeJS](https://nodejs.org/en)
- [Typescript](https://www.typescriptlang.org)
- [Kaitai Struct](https://doc.kaitai.io/user_guide.html)
    - alongside the [Kaitai Struct VSCode](https://marketplace.visualstudio.com/items?itemName=fudgepops.kaitai-struct-vscode) extension

For the 3D web-based visualizer, I use
- [ThreeJS](https://threejs.org)
- [Svelte](https://svelte.dev)

I use web technologies because it's the easiest way to give _everyone_ access to it.

Current Toolkit:
- Event/Traffic Visualizer
- type extractor 
    - also a kaitai struct parser generator
- "universal" kaitai struct file that can parse most files within `GenesysObject` folders
    - a `GenesysObject` instance analysis that gives a list of files within various game BNDL `GenesysObject` folders and shows what type they are 
- event file rebuilder

--- 

### Thanks

---

in the NFSMods community, knowledge can be difficult to come by - so I'd like to say thanks-

These tools would not be possible without:
- DGIorio
    - developed a bundle packer/unpacker tool: [[linked here](https://github.com/DGIorio/bundle_packer_unpacker)]
- burninrubber0
    - developed and maintains a wiki with extensive documention of Criterion titles that would otherwise be very difficult to understand: [[linked here](https://burnout.wiki/wiki/Main_Page)]
- serioussubwoofer
    - support, showed what is possible thorugh editing the in-game shaders
- polysouplist
    - gave me some info about how the maps and AI navigation works: [[kofi here](https://ko-fi.com/polysouplist)]
- Enksx1
    - not sure if they helped directly or not but they have done some insane things with mods that I had never thought even remotely possible, [[such as this](https://www.youtube.com/watch?v=oy9AbUO6Is4)]
- _mrally2
    - has shared some info that helped me get a basic understanding of the event file format. Creates youtube videos showing off some really cool concepts: [[yt channel](https://www.youtube.com/@mrally2)]
- redskywestside
    - taught me some about traffic data and how it works. Pointed me in the right direction about "triggers" for checkpoint data among other things in MW2012, and showed me a bit more about traffic data.
- others that have shown support despite the utter chaos that is the most-wanted-2012 channel lmao