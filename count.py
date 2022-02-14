# -*- coding: utf-8
"""
Created on Fri Sep  3 12:27:57 2021

@author: erkol
"""
def find(word, letter,index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
    
def count(word,letter):
    index=0
    count=0
    for letter in word:
        print(index)
        find(word,letter,index)
        if index!=-1:
            count=count+1
        return count
 
    