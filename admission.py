# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:47:49 2021

@author: Nithyashri
"""

import csv

def write_csv(info_list):
    
    with open("C:/Users/Nithyashri/Desktop/Nithu/PYTHON/AdmData.csv", 'a',newline='') as csvfile:
        writer=csv.writer(csvfile)
        if csvfile.tell()==0:
            writer.writerow(fields)
        #writer.writerow(i)    
        writer.writerow(student_info_list)
        #i=i+1
    
condition= True
while(condition):
    
    student_info=input("Enter details of the student in format Name Age Contact_No Email id :\n") #Accept input
    student_info_list= student_info.split(" ")  #write into lists because it is comma seperated file
    
    fields=['Name','Age','Contact', 'Email id']
    
    c=input("Is the information correct?\n  Name: {}\n  Age: {}\n  ContactNo: {}\n  Email_id: {}\n y/n "
            .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    
    if c== 'y': 
        write_csv(student_info_list)
        
        choice=input("Do you wanna add more students? y/n ")  #asking more choices
        if choice=='y':
            condition= True
            
            
        elif choice=='n':
            condition= False
            
    elif c=='n':
        print("Re-enter the values")
        
    
    
