# Modded-BrainFk
BrainFk modded
Based off of Esolang BrainFk: [BrainFk](https://esolangs.org/wiki/Brainfuck)

# Commands
normal commands in BrainFk with 4 more added  
edits:  
`,` writes "Input: " in console and asks for one char and then writes the byte of that char to the current idx  
`.` add the char of the byte at current idx to the output string  
new:  
`;` add the byte itself of current idx to the output string  
`$` reset the output string (set to empty/blank)  
`~` subtract next:  
[A, B] >> [A, B-A]  
 ^     >>  ^  
`#` length of the bytes at current idx:  
[A, 0] >> [A, len(A)]  
 ^     >>     ^  
 any other character is not delt with (comment)  
 
 # the Output String  
 how the outputs work is; in back end there is a string called output.  
 when the output string is updated: console is cleared then prints the output string  
 
 # how to run
 CMD `python ModdedBrainFK.py` to open console  
 CMD `python ModdedBrainFK.py FILE.EXT` runs code in that file
