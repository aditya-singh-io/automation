#!/usr/bin/env python3.7
#Program to Delete cluster

#@Author : Aditya Singh alias: aditya.singh@weka.io


import os

print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
print("Current Directory :--> "+os.getcwd())
cmd_home="/home/aditya.singh/.ssh/wekapp_v4/wekapp"
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
