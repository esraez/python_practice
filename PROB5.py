# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:42:17 2021

@author: erkol
"""
cols =   [[10, 20, 30, 40], [5, 6, 7, 8], [0.9, 0.1, 0.11, 0.12]]  

newcols=cols[0]
newcols1=cols[1]
newcols2=cols[2]
newrows=len(cols[0])
rows=[None]*newrows

 
for i in range(0,len(newcols)):
    rows[i]=[newcols[i],newcols1[i],newcols2[i]]
print(rows)
