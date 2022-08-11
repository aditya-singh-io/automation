#!/usr/bin/env python3.7
#Program to create cluster
####
######@Author : Aditya Singh alias: aditya.singh@weka.io

import os
import time
import aadi as func

#######################
##########################
############################

cmd_clear='clear'
os.system(cmd_clear)
print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
print("Current Directory :--> "+os.getcwd())
cmd_home="/home/aditya.singh/.ssh/wekapp_v4/wekapp/"
os.chdir(cmd_home)
print("Directory Path pointed to :-> "+os.getcwd())
cmd_create=""
print("\n****SELECT THE OPTION BELOW******\n")
print("[1]. Default Cluster ( 5 Backends and 2 Clients )")
print("[2]. MBC Cluster ( 6 Backends and 0 Clients )")
print("[3]. Tesla Failure Domain(FD) Config Cluster ( 8 Backends and 0 Clients &  i3.xlarge & FD=AUTO)")
print("[4]. Create cluster with Staless Client and custom build & size of BE ")
print("[5]. I don't like automation! I will create my cluster with Command ")
print("[6]. Checkout to a particular branch")
input_1=int(input("\nEnter the number from above list : "))
input_checkout=0
if input_1==1:
	os.system(cmd_clear)
	func.default_cluster()
elif input_1==2:
	os.system(cmd_clear)
	func.mbc_cluster()
elif input_1==3:
	os.system(cmd_clear)
	func.tesla_fd_config()
elif input_1==4:
	os.system(cmd_clear)
	func.particular_build()
elif input_1==5:
	os.system(cmd_clear)
	print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
	print("\n*************Entering Command Cluster formation Module******************\n")
	cmd_create=input("Enter the teka command to create cluster e.g. ./teka lab provision --> : ")
	os.system(cmd_create)
elif input_1==6:
	os.system(cmd_clear)
	print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
	print("\n****SELECT THE OPTION BELOW******\n")
	print("[1]. Checkout to a 3.13-dev-staging branch ")
	print("[2]. Checkout to a 3.14-dev-staging branch ")
	print("[3]. Checkout to a 4.0-dev branch ")
	print("[4]. Checkout to a specific(N) branch ")
	print("[5]. Exit")
	input_checkout=int(input("\nEnter the number from above list : "))
	if input_checkout==0:
		exit()
	elif input_checkout==1:
		func.checkout_3_13_dev_staging()
	elif input_checkout==2:
		func.checkout_3_14_dev_staging()
	elif input_checkout==3:
		func.checkout_4_0_dev()
	elif input_checkout==4:
		func.checkout_particular()
	elif input_checkout==5:
		exit()
else:
	print("Functionality not available for now..! Destroying self in 5 secs")
	time.sleep(5)
	os.system(cmd_clear)
	exit()
