#!/usr/bin/env python3.7
#Program to Delete cluster
######
#@Author : Aditya Singh alias: aditya.singh@weka.io


import os
import csv

name=''
user_name=''
email=''
working_dir=''
with open("config.csv", 'r') as file:
	obj = list(csv.reader(file))
	name=obj[1][0]
	user_name=obj[1][1]
	email=obj[1][2]
	working_dir=obj[1][3]
print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
print("Current Directory :--> "+os.getcwd())
cmd_home=working_dir
os.chdir(cmd_home)
print("Pointed directory :--> "+os.getcwd())
option=input("\nDo you want to kill the cluster? y/Yes/No : ")
if 'y' in option or 'Y' in option:
    cluster_name=input("Enter the cluster name : ")
    final_call=input("Do you want to preserve or final kill ? Preserve(P)/Destroy(D) : ")
    if "p" in final_call or 'P' in final_call:
        cmd="./teka lab kill "+cluster_name
    else:
        cmd="./teka lab kill --destroy "+cluster_name
    os.system(cmd)
