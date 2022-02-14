# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:22:17 2021

@author: erkol
"""

import sys

counter=1
for line in sys.stdin:
    linestripped=line.strip()
    print("line"+str(counter)+"is" + linestripped)
    counter=counter+1