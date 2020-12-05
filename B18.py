"""
Author: Gabriel Hofer
Date: December 8, 2020
Description: B18 Simulator

@param j - number of input pins
@param k - number of output pins
@param m - grid array rows
@param n - grid array cols


input pins are labeled
[0, j-1]
output pins are labeled
[2*n*m, 2*n*m+k-1]
nand inputs are labeled
[0, 2*n*m-1]
nand ouptuts are labeled
[j, j+n*m-1]


we need to define a mapping for nand inputs to nand outputs


"""
import numpy as np
import sys

class B18:
  def __init__(self,params): 
    self.j, self.k, self.m, self.n = params[2:]
    self.circuit={}
    f=open(params[1],'r')
    while True:
      line=f.readline().strip().split(' ')
      if line==['']: break
      self.circuit[int(line[0])]=int(line[1])
    self.values={}
    print(self.circuit)
  
  def percolate(self):
    pass

  def 


  def NAND(self, a, b): return not a&b

  def print(self): pass
    




def main():
  b18 = B18(sys.argv)


main()



