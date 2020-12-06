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
    self.j, self.k, self.m, self.n = map(int,params[2:])
    self.circuit={}
    f=open(params[1],'r')
    while True:
      line=f.readline().strip().split(' ')
      if line==['']: break
      self.circuit[int(line[1])]=int(line[0])
  
  """ update """
  """ can iterate by columns through the fpga """
  def update(self,iteration): 
    self.board={}
    input_pins={}
    for j in range(self.j): # initialize input pins
      pins[j]=(iteration&(1<<j))>>j
    for i in range(self.m): 
      self.board[i]=pins[self.circuit[i]]
    for i in range(self.n): # concepts --> column layers 
      for j in range(self.m):
        self.values[self.nand_out_idx(2*j)]=self.nand(self.values[2*j],self.values[2*j+1])

  """ maps either input of a nand to the output label """
  def nand_out_idx(self, a): a//2 + self.j

  """ not and """
  def nand(self, a, b): return not (a&b)

  """ prints the result """
  def output(self): 
    # print header (input pins and output pins)
    print("---------------------------------------------")
    print("---------------------------------------------")
    # print rows for every possible input combo
    for i in range(2**self.j):
      #print row
      for j in range(self.j-1, -1, -1):
        #print("{2}|".format(i&(1<<j))) 
        print(" "+str((i&(1<<j))>>j)+ " |",end='')
      out=self.update(i)
      #for j in range(self.k):
      #  print(self.values[2*self.n*self.m+j],end='')
      print()


def main():
  g = B18(sys.argv)
  g.output()

main()














