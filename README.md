  
# Modded-BrainFk
BrainFk modded  
Based off of Esolang BrainFk: [BrainFk](https://esolangs.org/wiki/Brainfuck)  
  
# Commands
normal commands in BrainFk with extra  
edits:  
`,` writes "Input: " in console and asks for one char and then writes the byte of that char to the current idx  
`.` add the char of the byte at current idx to the output string  
new:  
`;` add the byte itself of current idx to the output string  
`$` reset the output string (set to empty/blank)  
`~` subtract next:  
`[A, B] >> [A, B-A]`  
` idx 1 >> keep same idx`  
`#` length of the bytes at current idx:  
`[A, 0] >> [A, len(A)]`  
` idx 1 >> idx goes to next +1`  
`*` toggle is function (start & end a function)  
`/` call function at current idx  
`@` print memory at current time (waits until you press enter so you can still read the memory)  
`|` write the bytes of the next character in the code to pointer  
`"` save value at pointer to Use Storage  
`'` write value of Use Storage to pointer  
`=` run function B if Use Storage == A  
`[A, B] >> [A, B]`  
` idx 1 >> keep same idx`  
`!` terminate program  
any other character is not delt with (comment)
  
# the Output String
how the outputs work is; in back end there is a string called output.  
when the output string is updated: console is cleared then prints the output string  

# the Use Storage
so you have memory: [A, B, C, ...]
but with the Use Storage thre is one constant that you can't move throught
you can read and write to and from the Use Storage to the current memory pointer
  
# how to run
CMD `python ModdedBrainFK.py` to open console  
CMD `python ModdedBrainFK.py FILE.EXT` runs code in that file (skips all "\n" (new line))

## Implementing in code
Python:  
```from ModdedBrainFK import Code #import interpreter
c = Code() #create the Base to run the code
c.run(CODE) #run the code {CODE} (you can run this multiple times to run difrent code)
c.prmem() #print memory (same as @)
```

# errors
if you run some code and the interpretur crashes plece make an issue on this repo including:
1. a screenshot of the error or just the error itself as text,
2. the code you ran
and i will fix the error and update it
(NOTE: if the error *not* a python error that is an implemented error i made (already fixed))

# Credit
Made by: [Natejoestev](https://github.com/Natejoestev)  
Bassed on: [BrainFk](https://esolangs.org/wiki/Brainfuck)  
Language: [Python](https://www.python.org/)  

Crediting:
 if you use this for a Video, Stream, Program, Repo, System, etc. please credit Me @Natejoestev  
 you are allowed to View, Revive, and Pull this repo  
