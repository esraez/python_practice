# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:09:01 2021

@author: erkol
"""
#takes a DNA sequence string and an integer and returns a dictionary of kmers as keys and its frequency as values
def count_kmers(seq,n):
    s=get_windows(seq,n,1)  
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    return d  
         

def get_windows(seq,windowsize,stepsize):
    index=0
    s=[]
    while index<=len(seq)-windowsize:
        seqpiece=seq[index:index+windowsize]
        s.append(seqpiece)
        index=index+stepsize
    return s