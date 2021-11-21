# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:25:59 2021

@author: Nithyashri
"""

list1 = []
list2=[]
n = int(input("Enter number of elements for list 1 : "))
print("Enter values ")
for i in range (0,n):
    no=eval(input(""))
    list1.append(no)
    

for j in range (0,n):
    if list1[j]>0:
        print( list1[j])
        
        
n = int(input("Enter number of elements for list 2 : "))
print("Enter values ")
for i in range (0,n):
    no=eval(input(""))
    list2.append(no)
    

for j in range (0,n):
    if list2[j]>0:
        print(list2[j])