# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import io
blast_handle=io.open("pz_blastx_yeast_top1.txt")

counter=0
eval_sum=0

eval_str=[]
for line in blast_handle:
    line_stripped=line.strip()
    line_list=line_stripped.split("\t")
    eval_str.append(line_list[10])
    
    eval_sum=eval_sum+float(eval_str[counter])
    counter=counter+1
    
blast_handle.close()
mean=eval_sum/counter
print("Mean is:" + str(mean))
sqdiff=[]
for i in range(0,len(eval_str)):
    t=[(float(eval_str[i])-mean)**2]
    sqdiff.append(t[0])
    sumsq=sum(sqdiff)
    stdev=math.sqrt(sumsq/counter)
print("Standard deviation is:" + str(stdev))