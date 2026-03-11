# Fudge's MW2012 Type Extractor Tool

This tool runs using [nodejs](https://nodejs.org/en) with [typescript](https://www.typescriptlang.org).

the `.ksy` files are "[Kaitai Struct](https://kaitai.io)" files that I have written, and I use the vscode extension (named "[kaitai struct vscode](https://marketplace.visualstudio.com/items?itemName=fudgepops.kaitai-struct-vscode)") to visualize and generate typescript (`.ts`) file parsers with them. This project only needs the `genesys-type.ts` parser file, but I have included a few others I have created in the hopes that it furthers modding along when I don't have the urge/time to look into it more.

## What can be done with this?:

This will let researchers in the community develop tools that are able to read and modify data from the type information extracted from this tool. Further research is necessary to determine what all of these properties *do* and give them actual names, but at least this is a solid starting point.

I've personally been using it to create further `.ksy` files. More research is needed to give many things proper names and research how various things such as `CgsCore.UniqueId` work, but I am happy with how it is coming and what has been made.

## Important Note:

to my knowledge, `MERGED_output.txt` contains all the main types from the game. The issue is I don't know how to determine what `CgsCore.UniqueId` corresponds to what type, exactly. It might be possible somehow by using the bash `find` command.

`find . -type f -name "*.dat" -exec grep -FHoab $'\x{00}\x{00}\x{00}\x{00}' {} +`

replace the values in the `{00}`s with the sequence of bytes you're searching for.

## Setup:

1. Download [nvm-windows](https://github.com/coreybutler/nvm-windows). This is a command-line tool that makes it easy to install and manage different versions of nodejs, a tool that lets you run javascript locally without a web browser.

2. Once that is installed, in the console type `nvm install 24.0.2` (this is the version of node you're installing. You can type `nvm list available` to find the list of all available versions, but `24.0.2` is what I was using when I made this before).

3. After that, type `nvm use 24.0.2` (or whatever version you installed).

### If this folder did not come with a `node_modules` folder, follow this:

4. Navigate to this folder and type `npm install`. This will install all the dependencies so long as they still exist. 
5. enter `ts-node`. If a prompt appears with `>`, it is installed and you're in something called a `REPL`. Press Ctrl+C to exit said REPL.
   - if it is installed, you can move onto the Usage section of this document. 
   - Otherwise, follow step 6 and repeat this step afterwards
6. type `npm install ts-node` (not necessasry if step 5 worked)

## Usage:

1. Take the results of extracting whatever BNDL files you wish to analyze types from and place them in this folder
2. In `type-extractor.ts`, navigate to line 197 (where `pathNameProvider` is defined), and place the paths to the folders containing the extracted `14_00_00_00` folders.
  - each line should be something like `['path here', 'resulting name here'],`
  - the last line should *not* have a comma at the end
3. run `ts-node type-extractor.ts`

You should get a file for each entry (named like `resulting name here_output`). These text files contain the string `146165144147145160157160060061o`, followed by the type information extracted from the `genysis-type` objects found in the `14_00_00_00` folders.

## Reading the Output:

### "Extends":

Many types extend other types. In these cases you will find that the generated structure matches the type it extends up to the end of that type, then adds new stuff from there (hence "extends"). For instance, `Genesys.Gen.OnlineEvent extends Genesys.Gen.Event` (line 314 in `MERGED_output.txt`) will be identical to `Genesys.Gen.Event` up to offset `0x4A`.

### Reading the Types:

taking a look at `MERGED_output.txt` again, at line 328, we find:

`  0x3C  : Genesys.Gen.CustomChevron * [size @ 0x49] *`

This means that, at offset `0x3C` the structure has a pointer to an array of pointers, which point to `Genesys.Gen.CustomChevron` objects. The array's size is defined at offset `0x49` in the same structure.

in general, the pattern is this:

- `  offset : typename` - there is an object of type `typename` at `offset`
- `  offset : typename *` - there is a pointer to an object of type `typename` at `offset`
- `  offset : typename * [size @ arraySizeOffset]` - there is a pointer to an array of objects of type `typename` at `offset` with the array's size defined at `arraySizeOffset`.
- `  offset : typename [size @ arraySizeOffset]` - there is an array of `typename` objects directly at `offset`, with the object count being defined at `arraySizeOffset`
- `  offset : typename * [size @ arraySizeOffset] *` - there is a pointer to an array of pointers to type `typename` at `offset` with the array's size defined at `arraySizeOffset`

### "Errors":

At the very bottom of each file, there will be a list of folders that contained an error in the extraction process. The reason is often only because the type is actually an `enum`, such as `13_37_11_00`. Most (if not all) should all have a type of 5 (`e_nativetype_enumeration`), and as such don't have a name built-in.
