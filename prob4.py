# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

seq =  "GAGAGAGAGATATGAGA"
subseq='GAGA'
seq1=seq.split(subseq)
print(seq1)
lens=[len(seq) for seq in seq1]
print(lens)
loc=[None]*(len(lens)-1)

for i in range(0,len(lens)-1):
    if i==0:
        loc[i]=int(lens[i])+1
    elif i>0:
        loc[i]=loc[i-1]+len(subseq)+lens[i]
   
print(loc)


   