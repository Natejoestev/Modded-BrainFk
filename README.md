  
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
`[A, B] >> [A, B-A]`  
` idx 1 >> keep same ix`  
`#` length of the bytes at current idx:  
`[A, 0] >> [A, len(A)]`  
` idx 1 >> idx goes to next +1`  
`*` toggle is function (start & end a function)  
`/` call function at current idx  
`@` print memory at current time  
any other character is not delt with (comment)  
  
# the Output String  
how the outputs work is; in back end there is a string called output.  
when the output string is updated: console is cleared then prints the output string  
  
# how to run
CMD `python ModdedBrainFK.py` to open console  
CMD `python ModdedBrainFK.py FILE.EXT` runs code in that file

## Implementing in code
Python:
`from ModdedBrainFK import Code #import interpreter
c = Code() #create the Base to run the code
c.run(CODE) #run the code {CODE} (you can run this multiple times to run difrent code)
c.prmem() #print memory (same as @)`

# errors
if you run some code and the interpretur crashes plece make an issue on this repo including:
1. a screenshot of the error or just the error itself as text,
2. the code you ran
and i will fix the error and update it

# Credit
Made by: [Natejoestev](https://github.com/Natejoestev)  
Bassed on: [BrainFk](https://esolangs.org/wiki/Brainfuck)  
Language: [Python](https://www.python.org/)  

Crediting:  
 if you use this for a Video, Stream, Program, Repo, System, etc. please credit Me @Natejoestev  
 you are allowed to View, Revive, and Pull this repo  
  
