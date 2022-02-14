# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:06:41 2021

@author: erkol
"""
#given a string, windowsize and stepsize, returns a list of strings of the given windowsize#
def get_windows(seq,windowsize,stepsize):
    index=0
    s=[]
    t=[]
    while index<=len(seq)-windowsize:
        seqpiece=seq[index:index+windowsize]
        s.append(seqpiece)
        index=index+stepsize
        t.append(index)
        print(index)
    return s