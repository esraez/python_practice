# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 13:48:24 2021

@author: erkol
"""
import re
#takes a DNA sequence as a parameter and returns the longest 
#amino acid sequence that can be produced from it

def reverse_complement(s):
    s_rev=s[::-1]
    t=list(s_rev)
    for i in range(len(s_rev)):
        if t[i]=='T':
            t[i]='A'  
        elif t[i]=='A':
            t[i]='T'  
        elif t[i]=='C':
            t[i]='G'
        elif t[i]=='G':
            t[i]='C'
       

    delimiter=''
    u=delimiter.join(t)
    return u

#given a string, windowsize and stepsize, returns a list of strings of the given windowsize#
def get_windows(seq,windowsize,stepsize):
    index=0
    s=[]
    while index<=len(seq)-windowsize:
        seqpiece=seq[index:index+windowsize]
        s.append(seqpiece)
        index=index+stepsize
    return s

# takes a DNA sequence as a parameter and returns a 
# list of the six reading frames (as strings)
def seq_to_six_frames(s):
    n=len(s)
    seq=get_windows(s,(n-2),1)
    b=reverse_complement(s)
    seq_rest=get_windows(b,(n-2),1)
    frames=seq+seq_rest
    return frames
    
  
        
def codon_to_aa(seq):
    #3 bp string are keys, amino acid codes are values
    list1=['GCT','GCC','GCA','GCG']
    dict1 = dict.fromkeys(list1, 'A')
    list2=['CGT','CGC','CGA','CGG','AGA','AGG']
    dict2=dict.fromkeys(list2, 'R')
    list3=['AAT','AAC']
    dict3= dict.fromkeys(list3, 'N')
    list4=['GAT','GAC']
    dict4 = dict.fromkeys(list4,'D' )
    list5=['TGT','TGC']
    dict5 = dict.fromkeys(list5,'C')
    list6=['CAA','CAG']
    dict6 = dict.fromkeys(list6,'Q')
    list7=['GAA','GAG']
    dict7 = dict.fromkeys(list7,'E')
    list8=['GGT','GGC','GGA','GGG']
    dict8=dict.fromkeys(list8,'G')
    list9=['CAT','CAC']
    dict9=dict.fromkeys(list9,'H')
    dict10={'ATG':'START'}
    list11=['ATT','ATC','ATA']
    dict11=dict.fromkeys(list11,'I')
    list12=['CTT','CTC','CTA','CTG','TTA','TTG']
    dict12=dict.fromkeys(list12,'L')
    list13=['AAA','AAG']
    dict13=dict.fromkeys(list13,'K')
    dict14={'ATG':'M'}
    list15=['TTT','TTC']
    dict15=dict.fromkeys(list15,'F')
    list16=['CCT','CCC','CCA','CCG']
    dict16=dict.fromkeys(list16,'P')
    list17=['TCT','TCC','TCA','TCG','AGT','AGC']
    dict17=dict.fromkeys(list17,'S')
    list18=['ACT','ACC','ACA','ACG']
    dict18=dict.fromkeys(list18,'T')
    dict19={'TGG':'W'}
    list20=['TAT','TAC']
    dict20=dict.fromkeys(list20,'Y')
    list21=['GTT','GTC','GTA','GTG']
    dict21=dict.fromkeys(list21,'V')
    list22=['TAA','TGA','TAG']
    dict22=dict.fromkeys(list22,'STOP')
  
    if seq in dict1.keys():
        return dict1[seq]
    elif seq in dict2.keys():
        return dict2[seq]
    elif seq in dict3.keys():
        return dict3[seq]
    elif seq in dict4.keys():
        return dict4[seq]
    elif seq in dict5.keys():
        return dict5[seq]
    elif seq in dict6.keys():
        return dict6[seq]
    elif seq in dict7.keys():
        return dict7[seq]
    elif seq in dict8.keys():
        return dict8[seq]
    elif seq in dict9.keys():
        return dict9[seq]
    elif seq in dict10.keys():
        return dict10[seq]
    elif seq in dict11.keys():
        return dict11[seq]
    elif seq in dict12.keys():
        return dict12[seq]
    elif seq in dict13.keys():
        return dict13[seq]
    elif seq in dict14.keys():
        return dict14[seq]
    elif seq in dict15.keys():
        return dict15[seq]
    elif seq in dict16.keys():
        return dict16[seq]
    elif seq in dict17.keys():
        return dict17[seq]
    elif seq in dict18.keys():
        return dict18[seq]
    elif seq in dict19.keys():
        return dict19[seq]
    elif seq in dict20.keys():
        return dict20[seq]
    elif seq in dict21.keys():
        return dict21[seq]
    elif seq in dict22.keys():
        return dict22[seq]
    else:
        print("Unknown")
 
#takes a sequence string,splits into 3bp codons and returns amino acid for each codon
def DNA_to_aa(seq):
    h=get_windows(seq,3,3)
    #print (h)
    s=list()
    for i in range(0,len(h)):
        codon=h[i]
        res=codon_to_aa(codon)
        i=i+1
        s.append(res)
        rejoined="".join(s).strip('[]').strip(',')
    return rejoined

#given a DNA sequence, returns the longest non stop amino acid sequence#
def longest_non_stop(s):
    seq=seq_to_six_frames(s)
    #print(seq)
    u=[]
    for i in range(0,len(seq)): 
        c=DNA_to_aa(seq[i])
        #print(c)
        u.append(c)
    #return u 

    t=[]
    for i in range (0, len(u)):
        result=re.search(r"STOP",u[i])
        #print(result) 
        if result is None:
            print("No STOP oodons at index"+"\t"+str(i))
            a=len(u[i])
            t.append(a)
        else:
           st=result.start()    
           #print(st)
           t.append(st)  
    #print(t)
   
    maximum=max(t)
    max_index = t.index(maximum)
    print("Longest non stop sequence is"+"\t"+ str(u[max_index]))
    
  
