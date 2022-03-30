
#MODED BrainFK
#<>+-[],.
# ; add value at index to output
# $ clear output
# ~ [A, B] >> [A, B-A]
#    ^         ^
# # [A, 0] >> [A, len(A)]
#    ^            ^
# / call function at pointer
# * toggle is function
# @ print memory at current time

import os
import sys
import time

def con(x):
	if x<0: return 255
	if x>255: return 0
	return x
def ERR(reason, code, i, c):
	print("Error:", reason)
	print(code)
	print(" "*i+"^")
	c.prmem()
	exit()

class Func:
	def __init__(self):
		self.code = ""
	def __repr__(self): return f"Func:\"{self.code}\""

class Code:
	def __init__(self):
		self.mem = [0]
		self.p = 0
		self.o = ""
		self.onscreen = ""
		self.loops = []
		self.isFnc = False
	def prmem(self):
		print("Memory:")
		print(", ".join([str(m) for m in self.mem]))
		o = 0
		for i in range(self.p):
			o+=len(str(self.mem[i]))+2
		if isinstance(self.mem[self.p], Func): o+=2
		print(" "*o+"^")
	def run(self, code):
		i = 0
		def change(b):
			if isinstance(self.mem[self.p], Func):
				ERR(f"Can't add {b} to Function", code, i, self)
			self.mem[self.p]=con(self.mem[self.p]+b)
		while i<len(code):
			c = code[i]
			if c!="*" and self.isFnc:
				self.mem[self.p].code += c
			elif c==">":
				self.p+=1
				if len(self.mem)==self.p: self.mem.append(0)
			elif c=="<": self.p-=1
			elif c=="+": change(1)
			elif c=="-": change(-1)
			elif c=="[": self.loops.append(i)
			elif c=="]":
				if self.mem[self.p]!=0: i=self.loops[-1]
				else: del self.loops[-1]
			elif c==",": self.mem[p]=ord(input("input: ")[0])
			elif c==".": self.o+=chr(self.mem[self.p])
			elif c==";": self.o+=str(self.mem[self.p])
			elif c=="$": self.o=""
			elif c=="#":
				if self.p+1==len(self.mem): self.mem.append(0)
				self.mem[self.p+1] = len(str(self.mem[self.p]))
				self.p+=1
			elif c=="~": mem[self.p+1] -= self.mem[self.p]
			elif c=="*":
				if not self.isFnc:
					self.mem[self.p] = Func()
				self.isFnc = not self.isFnc
			elif c=="/":
				if not isinstance(self.mem[self.p], Func):
					ERR("Can't run a number", code, i, self)
				self.run(self.mem[self.p].code)
			elif c=="@": self.prmem()
			else: pass
			if self.onscreen != self.o:
				os.system("cls")
				self.onscreen=self.o
				print(self.o)
				time.sleep(.1)
			i+=1
		#self.prmem()


if __name__ == "__main__":
	if len(sys.argv)>1:
		with open(sys.argv[1], 'r') as f:
			c = Code()
			c.run(f.read().replace("\n", ""))
			c.prmem()
			exit()
	while True:
		code = input("> ")
		c = Code()
		c.run(code)
		c.prmem()
