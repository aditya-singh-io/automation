#!/usr/bin/env python3.7
#Setup for the Automation tool
####
######@Author : Aditya Singh alias: aditya.singh@weka.io

import csv
import os
import aadi as a
import logging as log
import time

a.clear()
print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
print("Current Directory :--> "+os.getcwd())
print("\n ****Setup Initialized**** \n")
inp1=input("Enter Username or Alias : ")
inp2=input("Enter your Name : ")
inp4=input("Enter your Email : ")
inp3=input("Enter the wekapp directory path (Hint: type 'pwd' inside wekapp cloned directory) : ")
x=2
while x>1:
	if len(inp3)>0:
		x=0
	else:
		inp3=input("Enter the wekapp directory path (Hint: type 'pwd' inside wekapp cloned directory) : ")
header=['Name','User Name', 'Email','Working Directory']
data=[inp2,inp1,inp4,inp3]
with open('config.csv','w',encoding='utf-8') as file:
	obj=csv.writer(file)
	obj.writerow(header)
	obj.writerow(data)
time.sleep(2)
print("Setup Completed Successfully")
