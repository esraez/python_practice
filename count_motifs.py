# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:40:11 2021

@author: erkol
"""

import re
def count_motifs(seq,motif):
    pieces=re.split(motif,seq)
    return len(pieces)-1

fhandle=open("grape_promoters.txt")
for line in fhandle:
    line_stripped=line.strip()
    line_list=re.split( r"\s+",line_stripped)
    gid=line_list[0]
    seq=line_list[1]
    
    num_motifs=count_motifs(seq, r"[AT]GATA[GA]")
    print(gid+"\t"+str(num_motifs))       

fhandle.close()