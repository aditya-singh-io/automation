#!/usr/bin/env python3.7
#Program to create cluster
####
######@Author : Aditya Singh alias: aditya.singh@weka.io

import os
import time
import csv
import aadi as func

#######################
##########################
############################
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
cmd_cp='cp template/* '+working_dir+'/qa/setups/templates/'
os.system(cmd_cp)
print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
print("Current Directory :--> "+os.getcwd())
cmd_home=working_dir
try:
	os.chdir(cmd_home)
except:
	print("\nWarning : You have entered incorrect path during setup. Please start the setup again and provide correct value\n")
	print("This path doesn't exists : "+working_dir+"\n")
	x_d=input("Do you want to Enter the setup Mode y/Y/Yes/No : ")
	if 'y' in x_d or 'Y' in x_d:
		import setup
	exit()
print("Directory Path pointed to :-> "+os.getcwd())
cmd_create=""
print("\nHi "+name+"! Please find the options below ")
print("\n****SELECT THE OPTION BELOW******\n")
print("[1]. Default Cluster ( 5 Backends and 2 Clients (1 stateless and 1 Stateful )")
print("[2]. MBC Cluster ( 6 Backends and 2 Clients { 1 stateless and 1 Stateful } )")
print("[3]. Tesla Failure Domain(FD) Config Cluster ( 8 Backends and 0 Clients &  i3.xlarge & FD=AUTO)")
print("[4]. Create cluster with Stateless Client and custom build & size of BE ")
print("[5]. Create cluster with Stateful Client and custom build & size of BE ")
print("[6]. Create cluster with all custom details including env, template, size ")
print("[7]. I don't like automation! I will create my cluster with Command ")
print("[8]. Checkout to a particular branch")
print("[9]. Exit")
input_1=int(input("\nEnter the number from above list : "))
input_checkout=0
if input_1==1:
	func.clear()
	func.default_cluster()
elif input_1==2:
	func.clear()
	func.mbc_cluster()
elif input_1==3:
	func.clear()
	func.tesla_fd_config()
elif input_1==4:
	func.clear()
	func.particular_build()
elif input_1==5:
	func.clear()
	func.particular_build_stateful()
elif input_1==6:
	func.clear()
	func.custom_details()
elif input_1==7:
	func.clear()
	print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
	print("\n*************Entering Command Cluster formation Module******************\n")
	cmd_create=input("Enter the teka command to create cluster e.g. ./teka lab provision --> : ")
	os.system(cmd_create)
elif input_1==8:
	func.clear()
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
elif input_1==9:
	func.clear()
	print("\n\n\n\n")
	print("Thanks for using this tool "+name+"! See you soon!\n\n\n\n")
	time.sleep(4	)
	func.clear()
	exit()
else:
	print("Functionality not available for now..! Destroying self in 5 secs")
	time.sleep(5)
	func.clear()
	exit()
