# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:02:38 2021

@author: Nithyashri
"""


def freq(s):
    d=dict()
    for key in s:
        if key in d:
            d[key]=d[key]+1
        else:
            d[key]=1
    print(d)       
        

s=input()
freq(s)