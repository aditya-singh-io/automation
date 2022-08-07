#!/usr/bin/env python3.7
import os
import time

### Def
#####
####################    
print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
print("Current Directory :--> "+os.getcwd())
cmd_home="/home/aditya.singh/.ssh/wekapp_v4/wekapp/"
os.chdir(cmd_home)
print("Directory Path pointed to :-> "+os.getcwd())
cluster_name=input("\nEnter the cluster name to alive it for the day : ")
cmd_alive="./teka lab keepalive "+cluster_name
inp_hours=input("For how many hours you want to keep the system alive (in Hours) :  ")
for i in range(1,int(inp_hours)+1):
    print("Machine running from  "+str(i)+" hour ")
    os.system(cmd_alive)
    time.sleep(3600)
    if i==48:  
        cmd_kill="./teka lab kill --destroy "+cluster_name
        os.system(cmd_kill)
        print("Cluster Destroyed Successfully ")
        time.sleep(10)
        cmd_kill="./teka lab list"
        os.system(cmd_kill)
        print(" Verification Successfull ")
        exit()
cmd_kill_1="./teka lab kill --destroy "+cluster_name
os.system(cmd_kill_1)
time.sleep(10)
print("Cluster Destroyed Successfully ")
cmd_list="./teka lab list"
os.system(cmd_list)
print(" Verification Successfull ")
