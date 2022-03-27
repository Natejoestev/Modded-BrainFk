
#MODED BrainFK
#<>+-[],.
#; add value at index to output
#$ clear output
#~ [A, B] >> [A, B-A]
#   ^         ^
## [A, 0] >> [A, len(A)]
#   ^            ^

import os
import sys
import time

def con(x):
	if x<0: return 255
	if x>255: return 0
	return x

def run(code):
	mem = [0]
	p = 0
	
	o = ""
	onscreen = ""

	loops = []
	
	i = 0
	while i<len(code):
		c = code[i]
		if c==">":
			p+=1
			if len(mem)==p: mem.append(0)
		elif c=="<": p-=1
		elif c=="+": mem[p]=con(mem[p]+1)
		elif c=="-": mem[p]=con(mem[p]-1)
		elif c=="[": loops.append(i)
		elif c=="]":
			if mem[p]!=0: i=loops[-1]
			else: del loops[-1]
		elif c==",": mem[p]=ord(input("input: ")[0])
		elif c==".": o+=chr(mem[p])
		elif c==";": o+=str(mem[p])
		elif c=="$": o=""
		elif c=="#":
			mem[p+1] = len(str(mem[p]))
			p+=1
		elif c=="~": mem[p+1] -= mem[p]
		if onscreen != o:
			os.system("cls")
			onscreen=o
			print(o)
			time.sleep(.1)
		i+=1
	
	print("Memery:")
	print(", ".join([str(m) for m in mem]))
	


if __name__ == "__main__":
	if len(sys.argv)>1:
		with open(sys.argv[1], 'r') as f:
			run(f.read().replace("\n", ""))
			exit()
	while True:
		code = input("> ")
		run(code)