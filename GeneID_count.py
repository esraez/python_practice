# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:32:27 2021

@author: erkol
"""
import io
fhandle=io.open("PZ.annot.txt")

ids_to_counts = dict()

# Parse input
for line in fhandle:
    line_list = line.strip().split("\t")
    seqid = line_list[0]
    if seqid in ids_to_counts:
        ids_to_counts[seqid] = ids_to_counts[seqid] + 1
    else:
        ids_to_counts[seqid] = 1

# Print dict contents
ids_list = ids_to_counts.keys()
for seqid in ids_list:
    count = ids_to_counts[seqid]
    print(str(count) + "\t" + seqid)

fhandle.close()

        