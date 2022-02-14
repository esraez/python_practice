# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 12:49:16 2021

@author: erkol
"""
#takes two dictionaries as parameters returns their “union” as a dictionary
#when a key is found in both, the larger value is used in the output
def union_dictionaries(a,b):
    
    union=dict()
    for key in a:
        if key in b:
            if a[key]>b[key]:
                union[key]=a[key]
            elif b[key]>a[key]:
                union[key]=b[key]
        else:
            union[key]=a[key]
    for key in b:
        if key not in a:
            union[key]=b[key]
      
    return union

