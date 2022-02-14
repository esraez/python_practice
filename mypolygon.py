# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:31:57 2021

@author: erkol
"""
import turtle
t = turtle.Turtle()
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)




def arc(t, r, angle):
    n = 50
    length = angle*r
    polygon(t, n, length)

    
arc(t,100,360)