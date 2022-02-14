# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:03:43 2021

@author: erkol
"""
import math   
def mysqrt(a,x):
    while True:
        y=(x+a/x)/2
        if abs(y-x)<0.0000001:
            return x
            break
        x=y
         
        
def sqrt(a):
    return math.sqrt(a)
            
def diff(a,x):
    return abs(int(mysqrt(a,x))-int(sqrt(a)))
                   
       
def test_square_root(a): 
    i = 1
    while i<=a:   
        print(i,' ', round(mysqrt(i,1),5),' ',' ', round(math.sqrt(i),5),' ',
              round(diff(i,1),5))
        i = i+1
         
    