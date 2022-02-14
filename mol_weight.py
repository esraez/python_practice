# -*- coding: utf-8 -*-|column -t
"""
Created on Tue Nov 16 11:47:24 2021

@author: erkol
"""

import io

fhandle=io.open("ids_seqs.txt")
t=[]
s=[]
res=[]
ids=[]
for line in fhandle:
    line_stripped=line.strip()
    seqs=line_stripped.split("\t")
    ids.append(seqs[0])
    res.append(seqs[1])
for i in range(0,len(res)):
    numA=res[i].count('A')
    numT=res[i].count('T')
    numC=res[i].count('C')
    numG=res[i].count('G')   
    nums=[numA,numT,numC,numG]
    t.append(nums)
    print (numA, numT, numC, numG)
    total_mol_weight=(float(numA)*313.21 + float(numT)*304.2+float(numC)*289.18 +float( numG)*329.21) - 61.96
    s.append(total_mol_weight)
print(total_mol_weight)
fhandle=io.open("mol_weight_seqs.py","w")
fhandle.write(str(s).strip("[]").replace("[]","\n").replace(",","\n").replace("[]","\n") +"\n")

fhandle.close()
              
