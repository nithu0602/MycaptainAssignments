# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 09:11:52 2021

@author: Nithyashri
"""

"""
our task now is to write a Python program which accepts the radius of a circle from the user and computes area.
Your Input and Output should look something like this

Input the radius of the circle : 1.1 The area of the circle with radius 1.1 is: 3.8013271108436504

Your second task now is to write a Python program to accept a filename from the user and print the extension of that.
Your Input and Output should look something like this

Input the Filename: abc.py The extension of the file is : 'python'

Let's start coding !
"""
import math
r=eval(input("Enter radius"))
area=3.141592653589793*r*r
print(area)

filename=(input("enter file name"))
fn=filename.split('.')
print("Extension is ", (fn[-1]))
