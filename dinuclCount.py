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
## followed by printing the count of each dinucleotide.##
## After going through all of the files, it will print ##
## out the dinucleotides for all the species and the   ##
## total count of all the dinucleotides for all the    ##
## species.                                            ##
#########################################################

import re
import sys
import os

def dinucleotideCounter(directory):
  d = {'AA':re.compile("(?=(AA))"), 'AC':re.compile("(?=(AC))"), 'AG':re.compile("(?=(AG))"), 'AT':re.compile("(?=(AT))"), 'CA':re.compile("(?=(CA))"), 'CC':re.compile("(?=(CC))"), 'CG':re.compile("(?=(CG))"), 'CT':re.compile("(?=(CT))"), 'GA':re.compile("(?=(GA))"), 'GC':re.compile("(?=(GC))"), 'GG':re.compile("(?=(GG))"), 'GT':re.compile("(?=(GT))"), 'TA':re.compile("(?=(TA))"), 'TC':re.compile("(?=(TC))"), 'TG':re.compile("(?=(TG))"), 'TT':re.compile("(?=(TT))")}

  count = {'AA':0, 'AC':0, 'AG':0, 'AT':0, 'CA':0, 'CC':0, 'CG':0, 'CT':0, 'GA':0, 'GC':0, 'GG':0, 'GT':0, 'TA':0, 'TC':0, 'TG':0, 'TT':0}
  
  totalCount = {'AA':0, 'AC':0, 'AG':0, 'AT':0, 'CA':0, 'CC':0, 'CG':0, 'CT':0, 'GA':0, 'GC':0, 'GG':0, 'GT':0, 'TA':0, 'TC':0, 'TG':0, 'TT':0}

  names = ['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 'CG', 'CT', 'GA', 'GC', 'GG', 'GT', 'TA', 'TC', 'TG', 'TT']

  for dirname, dirnames, files in os.walk(directory):  
    for filename in files:
      if filename.endswith(".fa"):
        fin = open(filename)    
        for line in fin:
          if line[0] == '>':
            line = line.strip('>')
            print()
            print(line)
            print()
          else:  
            for x in names:
              count[x] = len(d[x].findall(line))
              totalCount[x] = totalCount[x] + len(d[x].findall(line))
              print('Dinucleotide ', x, 'Count ', count[x])
  print()      
  print('Total dinucleotide counts')
  print()
  for x in names:
    print('Dinucleotide ', x, 'Count ', totalCount[x])

if __name__ == "__main__":
  directory = str(sys.argv[1])
  dinucleotideCounter(directory)
  sys.exit()