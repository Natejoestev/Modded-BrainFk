
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
# | write the bytes of the next character in the code to pointer
# !
# " save value at pointer to Use Storage
# ' write value of Use Storage to pointer
# = [A, B] >> [A, B]
#    ^         ^
#run function B if Use Storage == A
#
#[A, B, C] >> [A, B, C]
#    ^            ^
#run function C if A==B
# ! terminate
# % floor half
#[A, 0] >> [A, floor(A/2)]
# ^             ^
# : move
#[A, 0] >> [0, A]
# ^            ^
# ` write the number of input to pointer
# ? get string input
#[Func, c]
#  ^      
#when the function is run pointer is at c
#loops through all characters in the string:
#  sets c to the bytes of the character
#  runs Func for each character

# ^ set memory pointer to value at index
# loops???
# multi char input "_"
#[Func, A]
#  ^
# for each char in input:
#   run func
#   A = char


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
		self.use = 0
	def prmem(self):
		print("Use:", self.use)
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
		def intager(a):
			b = ""
			for c in a:
				if c in "0123456789": b+=c
			return 0 if len(b)==0 else int(b)
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
				if len(self.loops)==0:
					ERR("Can't end a loop that wasn't started", code, i, self)
				if self.mem[self.p]!=0: i=self.loops[-1]
				else: del self.loops[-1]
			elif c==",": self.mem[self.p]=ord(input("input: ")[0])
			elif c==".": self.o+=chr(self.mem[self.p])
			elif c==";": self.o+=str(self.mem[self.p])
			elif c=="$": self.o=""
			elif c=="#":
				if self.p+1==len(self.mem): self.mem.append(0)
				self.mem[self.p+1] = len(str(self.mem[self.p]))
				self.p+=1
			elif c=="~":
				if len(self.mem)-self.p<2:
					ERR("Can't index next in memory", code, i, self)
				self.mem[self.p+1] -= self.mem[self.p]
			elif c=="*":
				if not self.isFnc:
					self.mem[self.p] = Func()
				self.isFnc = not self.isFnc
			elif c=="/":
				if not isinstance(self.mem[self.p], Func):
					ERR("Can't run a number", code, i, self)
				r = self.run(self.mem[self.p].code)
				#if r=="T":
				#	print(r)
				#	return r
			elif c=="@":
				self.prmem()
				input("Done looking at memory?")
			elif c=="|":
				i+=1
				self.mem[self.p] = ord(code[i])
			elif c=="\"": self.use = self.mem[self.p]
			elif c=="'": self.mem[self.p] = self.use
			elif c=="=":
				if len(self.mem)-self.p<2: #3:
					ERR("Can't index next in memory", code, i, self)
				a = self.use #self.mem[self.p]
				b = self.mem[self.p] #+1
				c = self.mem[self.p+1] #+2
				if a==b:
					if not isinstance(c, Func):
						ERR("Can't run a number", code, i, self)
					self.run(c.code)
			elif c=="!": #return "T"
				print("TERMINATE")
				self.prmem()
				exit()
			elif c=="%":
				self.p+=1
				if isinstance(self.mem[self.p-1], Func): ERR("Can't half a Function", code, i, self)
				self.mem[self.p]=floor(self.mem[self.p-1]/2)
			elif c==":":
				self.mem[self.p+1]=self.mem[self.p]
				self.mem[self.p]=0
				self.p+=1
			elif c=="`":
				v = intager(input("Intager: "))
				self.mem[self.p]=v
				print(f"Registerd as: {v}")
			elif c=="?":
				if not isinstance(self.mem[self.p], Func):
					ERR("Can't run a non function", code, i, self)
				if len(self.mem)-1==self.p:self.mem.append(0)
				idx = int(self.p)
				s = input("String: ")
				for c in s:
					self.p=idx+1
					self.mem[idx+1] = ord(c)
					self.run(self.mem[idx].code)
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
