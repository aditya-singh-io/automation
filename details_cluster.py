#!/usr/bin/env python3.7
#Program to get details of the cluster

#@Author : Aditya Singh alias: aditya.singh@weka.io

import os
import csv
import aadi as func

func.clear()
name=''
user_name=''
email=''
working_dir=''
try:
	with open("config.csv", 'r') as file:
		obj = list(csv.reader(file))
		name=obj[1][0]
		user_name=obj[1][1]
		email=obj[1][2]
		working_dir=obj[1][3]
except:
	print("\nHello! You are using this tool for the first time. Complete one time setup below !\n\n")
	x_d=input("Do you want to Enter the setup Mode y/Y/Yes/No : ")
	if 'y' in x_d or 'Y' in x_d:
		import setup
	exit()
print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
print("Current Directory :--> "+os.getcwd())
cmd_home=working_dir
os.chdir(cmd_home)
print("Directory Path pointed to :-> "+os.getcwd())
cmd_create=""
option=input("\nDo you want to see IP details of the  cluster ? y/Yes/No : ")
if 'y' in option or 'Y' in option:
    cmd_create="./teka lab list -v"
    os.system(cmd_create)
else:
    cmd_create="./teka lab list"
    os.system(cmd_create)

