# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:43:21 2021

@author: Nithyashri
"""

"""
Write a Python Program for Fibonacci numbers
"""

a=0
b=1
no=0
n=(eval(input("Enter n")))


if n==1:
    print(a)
    
    
elif n==2:
    print(a)
    print(b)
    
else:
    print(a)
    print(b)
    for i in range(3,n+1):
        
        no=a+b
        a=b
        b=no
        print(no," ")
