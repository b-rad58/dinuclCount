#!/usr/bin/python3

#########################################################
## CS 2500 (Fall 2014), Assignment #4, Question #1     ##
## Script File Name: X GChain.py                       ##
## Student Name: X Bradley Gavan                       ##
## Login Name: X bmg610                                ##
## MUN #: 201208634                                    ##
##                                                     ##
## This script takes a directory as an input and then  ##
## opens each file with the extension ".fa".  It goes  ##
## through each file, printing the name of each species##
## followed by printing all non-overlapping three      ##
## nucleotides leading and tailing a G chain           ##
#########################################################

import sys 
import os
import re

def GChain(directory):
  for dirname, dirnames, files in os.walk(directory):  
    for filename in files:
      if filename.endswith(".fa"):
        fin = open(filename) 
        r = re.compile('G{3,}')   
        for line in fin:
          if line[0] == '>':
            line = line.strip('>')
            print()
            print(line)
          else:  
            chains = re.findall(r'.{,3}G{3,}.{,3}', line)
            i = 0
            for w in chains:
              f = r.split(chains[i])
              i = i + 1
              lead = f[0]
              tail = f[1]
              if lead == "":
                lead = 'NONE'
              elif tail == "":
                tail = 'NONE'
              else:
                pass
              print('Lead = ', lead, 'Tail = ', tail)
              
if __name__ == "__main__":
  directory = str(sys.argv[1])
  GChain(directory)
  sys.exit()
