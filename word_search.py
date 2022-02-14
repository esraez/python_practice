# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:01:49 2021

@author: erkol
"""
def word_list(s):
    
    fin=open("words.txt")
    d=dict()
    for line in fin:
        key=line.strip()
        d[key]=1
        
    if s in d:
        print("Yes")
    else:
        print("No")