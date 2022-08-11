#!/usr/bin/env python3.7
#Program to get details of the cluster

#@Author : Aditya Singh alias: aditya.singh@weka.io

import os

cmd_clear='clear'
os.system(cmd_clear)
print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
print("Current Directory :--> "+os.getcwd())
cmd_home="/home/aditya.singh/.ssh/wekapp_v4/wekapp/"
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

