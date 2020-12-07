"""
Author: Gabriel Hofer
Date: December 8, 2020
Description: B18 Simulator
"""
import numpy as np
import sys

class B18:
  def __init__(self,params): 
    self.j, self.k, self.m, self.n = map(int,params[2:])
    self.circuit={}
    f=open(params[1],'r')
    while True:
      line=f.readline().strip().split(' ')
      if line==['']: break
      self.circuit[int(line[1])]=int(line[0])
  
  """ update """
  def update(self,it): 
    red, black, out = {}, {}, {}
    for j in range(len(self.inp)):
      red[j]=int(bin(it)[2:].zfill(len(self.inp))[j:j+1])
    for i in range(self.n): # concepts --> column layers 
      for j in range(2*self.m):
        if j+2*self.m*i in self.circuit:
          black[j+2*self.m*i]=red[self.circuit[j+2*self.m*i]]
      for j in range(self.m):
        if 2*(j+i*self.m) in black:
          red[self.nand_out_idx(2*(j+i*self.m))]=self.nand(black[2*(j+i*self.m)],black[2*(j+i*self.m)+1])
    for k in range(self.k):
      if 2*self.n*self.m+k in self.circuit:
        out[2*self.n*self.m+k]=red[self.circuit[2*self.n*self.m+k]]
    return out 

  """ maps either input of a nand to the output label """
  def nand_out_idx(self, a): return (a//2 + self.j)

  """ not and """
  def nand(self, a, b): return int(not (a&b))

  """ prints the result """
  def output(self): 
    in_cnt=int(0)
    for i in range(self.j):
      if i in self.circuit.values():
        in_cnt+=int(1);
    out_cnt=int(0)
    for i in range(self.k):
      if i+2*self.n*self.m in self.circuit:
        out_cnt+=int(1)
    for i in range(in_cnt+out_cnt): print('-----',end='') 
    print()
    for i in range(in_cnt): print("{:3} |".format(i),end='')
    for i in range(out_cnt): print("{:3} |".format(2*self.m*self.n+i),end='') 
    print()
    for i in range(in_cnt+out_cnt): print('-----',end='') 
    print()
    """ only use inputs that are keys in self.circuit """
    self.inp=[]
    for i in range(self.j):
      if i in self.circuit.values():
        self.inp.append(i)
    for i in range(2**len(self.inp)):
      for j in range(len(self.inp)-1, -1, -1):
        print("{:3} |".format((i&(1<<j))>>j),end='')
      out=self.update(i)
      for i in out:
        print("{:3} |".format(out[i]),end='')
      print()

def main():
  g = B18(sys.argv)
  g.output()

main()


