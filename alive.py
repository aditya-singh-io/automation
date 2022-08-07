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
cluster_name=input("Enter the cluster name to alive it since it is cancelled : ")
cmd_alive="./teka lab keepalive "+cluster_name
os.system(cmd_alive)
print("Keeping system Alive ")
time.sleep(216000)
print("keeping system Alive for the second time ")
os.system(cmd_alive)
time.sleep(216000)
print("keeping system Alive for the second time ")
os.system(cmd_alive)


