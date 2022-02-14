# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:49:32 2021

@author: erkol
"""
def molecular_weight(seq):
    for i in range(0,len(seq)):
        numA=seq[i].count('A')
        numT=seq[i].count('T')
        numC=seq[i].count('C')
        numG=seq[i].count('G')   
        nums=[numA,numT,numC,numG]
        total_mol_weight=(float(numA)*313.21 + float(numT)*304.2+float(numC)*289.18 +float( numG)*329.21) - 61.96
      
    return total_mol_weight
  

              
