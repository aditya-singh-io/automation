#!/usr/bin/env python3.7
#Program to create cluster
####
######@Author : Aditya Singh alias: aditya.singh@weka.io

import os
import time

### Def
#####
####################    

def default_cluster():
	print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
	print("\n*************Entering Default Cluster formation Module******************\n")
	option=input("Do you want to create Default cluster ? y/Yes/No : ")
	if 'y' in option or 'Y' in option:
		cluster_name=input("Enter the cluster name : Note: Don't use _ or Underscore :")
		print("\nSuccess..! Cluster Creation in progress \n")
		cmd_create="./teka lab provision --template m5-clients-instance.yaml {} --size=6 && ./teka install {}".format(cluster_name,cluster_name)
		os.system(cmd_create)
		print("Cluster created Successfully. ! Pls run details from Automation tool ")		
		time.sleep(216000)
		cmd_alive="./teka lab keepalive "+cluster_name
		os.system(cmd_alive)
		print("Keeping system Alive ")
		time.sleep(216000)
		print("keeping system Alive for the second time ")
		os.system(cmd_alive)
		
	else:
		cmd_create=input("Enter the teka command to create cluster e.g. ./teka lab provision --> : ")
		os.system(cmd_create)
		print("Cluster created Successfully. ! Pls run details from Automation tool ")		
		time.sleep(216000)
		cmd_alive="./teka lab keepalive "+cluster_name
		os.system(cmd_alive)
		print("Keeping system Alive ")
		time.sleep(432000)
		print("keeping system Alive for the second time ")
		os.system(cmd_alive)
		
def particular_build():
	print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
	print("\n*************Entering Specific build Cluster formation Module******************\n")
	cluster_name=input("Enter the cluster name : ")
	size=5
	try:
		size_inp=input("Enter the size of the backends to be needed. By default it is 5 : ")
		size=int(size_inp)
	except:
		size=5
	ver_in=input("Enter the build version you want ? (Optional) default: Latest Build  : ")
	cmd=''
	if len(ver_in)>3:
		print("Installing cluster with below mentioned details ")
		print("Cluster name "+cluster_name)		
		print("Size of the BE ",size)
		print("Build to be installed in the cluster "+ver_in)
		cmd='./teka lab provision --template=stateless-clients-testing.yaml '+cluster_name+' --size '+str(size)+' --env=oci && ./teka install --from-version '+ver_in+' '+cluster_name
	else:
		print("Installing cluster with latest Default Build")
		print("Installing cluster with below mentioned details ")
		print("Cluster name "+cluster_name)		
		print("Size of the BE ",size)
		print("Build to be installed in the cluster : Latest build (Fetching by System) ")
		cmd='./teka lab provision --template=stateless-clients-testing.yaml '+cluster_name+' --size '+str(size)+' --env=oci && ./teka install '+cluster_name
	os.system(cmd)

def mbc_cluster():
	print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
	print("\n*************Entering MBC Cluster formation Module******************\n")
	cluster_name=input("Enter the cluster name : ")
	cmd='./teka lab provision '+cluster_name+' --size 6 --type i3.2xlarge --env oci --ionode-count 3 --mbc-installation=yes -f && ./teka install '+cluster_name
	os.system(cmd)

def tesla_fd_config():
	print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
	print("\n*************Entering TESLA FD CONFIG cluster formation Module******************\n")
	cluster_name=input("Enter the cluster name : ")
	cmd="./teka lab provision "+cluster_name+" --size 8 --type i3.xlarge --env oci --hosts-per-failure-domain AUTO && ./teka install "+cluster_name
	os.system(cmd)

def checkout_3_13_dev_staging():
	cmd_1='git checkout CI/3.13-dev-staging'
	os.system(cmd_1)
	time.sleep(10)
	cmd_2='git status'
	os.system(cmd_2)
	time.sleep(1)
	cmd_3='git pull --rebase'
	os.system(cmd_3)
	time.sleep(20)
	cmd_4='git submodule update --init --recursive'
	os.system(cmd_4)
	time.sleep(20)
	print("Command Ran Successfully")

def checkout_3_14_dev_staging():
	cmd_1='git checkout CI/3.14-dev-staging'
	os.system(cmd_1)
	time.sleep(10)
	cmd_2='git status'
	os.system(cmd_2)
	time.sleep(1)
	cmd_3='git pull --rebase'
	os.system(cmd_3)
	time.sleep(20)
	cmd_4='git submodule update --init --recursive'
	os.system(cmd_4)
	time.sleep(20)
	print("Command Ran Successfully")

def checkout_4_0_dev():
	cmd_1='git checkout CI/4.0-dev'
	os.system(cmd_1)
	time.sleep(3)
	cmd_2='git status'
	os.system(cmd_2)
	time.sleep(1)
	cmd_5="git stash"
	time.sleep(5)
	os.system(cmd_5)
	cmd_3='git pull --rebase'
	os.system(cmd_3)
	time.sleep(10)
	cmd_6="git stash pop"
	os.system(cmd_6)
	time.sleep(5)
	cmd_4='git submodule update --init --recursive'
	os.system(cmd_4)
	time.sleep(20)
	print("Command Ran Successfully")

def checkout_particular():
	input_branch=input('Enter the branch you want to checkout.( E.g: 4.0-dev-staging ) --> : ')
	cmd_1='git checkout CI/'+input_branch
	os.system(cmd_1)
	time.sleep(10)
	cmd_2='git status'
	os.system(cmd_2)
	time.sleep(20)
	cmd_3='git pull --rebase'
	os.system(cmd_3)
	time.sleep(20)
	cmd_4='git submodule update --init --recursive'
	os.system(cmd_4)
	time.sleep(20)
	print("Command Ran Successfully")


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
	default_cluster()
elif input_1==2:
	os.system(cmd_clear)
	mbc_cluster()
elif input_1==3:
	os.system(cmd_clear)
	tesla_fd_config()
elif input_1==4:
	os.system(cmd_clear)
	particular_build()
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
		checkout_3_13_dev_staging()
	elif input_checkout==2:
		checkout_3_14_dev_staging()
	elif input_checkout==3:
		checkout_4_0_dev()
	elif input_checkout==4:
		checkout_particular()
	elif input_checkout==5:
		exit()
else:
	print("Functionality not available for now..! Destroying self in 5 secs")
	time.sleep(5)
	os.system(cmd_clear)
	exit()
