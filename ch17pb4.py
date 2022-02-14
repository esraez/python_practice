# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 10:56:04 2021

@author: erkol
"""

seq="GAGAGAGAGATATGAGA"
subseq="GAGA"
index=0
counter=0
for index in range(0, len(seq)+ 1):
    if subseq[0:2]==subseq[2:4]:
        if subseq[index+index+4]==subseq[index+4:index+8]:
            index=index+4
        elif subseq[index+index+4]==subseq[index+4+1:index+8+1]:
            
    
for index in range(0, len(seq)+ 1):
    if seq[index:index+1]==seq[index+2:index+3]:
        counter=counter+1
        index=index+1


print(counter)