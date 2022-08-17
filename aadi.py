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
	env='oci'
	if 'y' in option or 'Y' in option:
		cluster_name=input("Enter the cluster name : Note: Don't use _ or Underscore : ")
		inp_env=input("Please enter Env oci/aws ? (Default: oci ) : ")
		if len(env)>2:
			env=inp_env
		print("\nCluster Creation in progress. Please wait for 10-15 mins \n")
		cmd_create="./teka lab provision --template default.yaml {} --size=6  --env={} && ./teka install {}".format(cluster_name,env,cluster_name)
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
	env='oci'
	inp_env=input("Please enter Env oci/aws ? (Default: oci ) : ")
	if len(env)>2:
		env=inp_env
	if len(ver_in)>3:
		print("Installing cluster with below mentioned details ")
		print("Cluster name : "+cluster_name)		
		print("Size of the BE :",size)
		print("Build to be installed in the cluster : "+ver_in)
		cmd='./teka lab provision --template=stateless-clients-testing.yaml '+cluster_name+' --size '+str(size)+' --env='+env+' && ./teka install --from-version '+ver_in+' '+cluster_name
	else:
		print("Installing cluster with latest Default Build")
		print("Installing cluster with below mentioned details ")
		print("Cluster name :"+cluster_name)		
		print("Size of the BE :",size)
		print("Build to be installed in the cluster : Latest build (Fetching by System) ")
		#cmd='./teka lab provision --template=adi.yaml '+cluster_name+' --size '+str(size)+' --env=aws && ./teka install '+cluster_name
		cmd='./teka lab provision --template=stateless-clients-testing.yaml '+cluster_name+' --size '+str(size)+' --env='+env+' && ./teka install '+cluster_name
	os.system(cmd)

def particular_build_stateful():
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
	env='oci'
	inp_env=input("Please enter Env oci/aws ? (Default: oci ) : ")
	if len(env)>2:
		env=inp_env
	if len(ver_in)>3:
		print("Installing cluster with below mentioned details ")
		print("Cluster name : "+cluster_name)		
		print("Size of the BE :",size)
		print("Build to be installed in the cluster : "+ver_in)
		cmd='./teka lab provision --template=m5-clients-instance.yaml '+cluster_name+' --size '+str(size)+' --env='+env+' && ./teka install --from-version '+ver_in+' '+cluster_name
	else:
		print("Installing cluster with latest Default Build")
		print("Installing cluster with below mentioned details ")
		print("Cluster name :"+cluster_name)		
		print("Size of the BE :",size)
		print("Build to be installed in the cluster : Latest build (Fetching by System) ")
		cmd='./teka lab provision --template default.yaml '+cluster_name+' --size '+str(size)+' --env='+env+' && ./teka install '+cluster_name
	os.system(cmd)

def custom_details():
	print("\n **********Automated tool created by @d!+y@ S!ng#*********** \n")
	print("\n*************Entering End to end details for Cluster formation Module******************\n")
	cluster_name=input("Enter the cluster name : ")
	size=5
	try:
		size_inp=input("Enter the size of the backends to be needed. By default it is 5 : ")
		size=int(size_inp)
	except:
		size=5
	ver_in=input("Enter the build version you want ? (Optional) default: Latest Build  : ")
	cmd=''
	inp_env='oci'
	env=input("Enter the environment aws/oci (Default: OCI): ")
	if len(env)>2:
		inp_env=env
	template='stateless-clients-testing.yaml'
	temp_inp=input("Enter the template (Default: stateless-clients-testing.yaml): ")
	if len(temp_inp)>3:
		template=temp_inp
	if len(ver_in)>3:
		print("Installing cluster with below mentioned details ")
		print("Cluster name : "+cluster_name)
		print("Size of the BE :",size)
		print("Build to be installed in the cluster : "+ver_in)
		cmd='./teka lab provision --template='+template+' '+cluster_name+' --size '+str(size)+' --env='+inp_env+' && ./teka install --from-version '+ver_in+' '+cluster_name
	else:
		print("Installing cluster with latest Default Build")
		print("Installing cluster with below mentioned details ")
		print("Cluster name :"+cluster_name)
		print("Size of the BE :",size)
		print("Build to be installed in the cluster : Latest build (Fetching by System) ")
		cmd='./teka lab provision --template='+template+' '+cluster_name+' --size '+str(size)+' --env='+inp_env+' && ./teka install '+cluster_name
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
	time.sleep(2)
	cmd_2='git status'
	os.system(cmd_2)
	time.sleep(2)
	cmd_5="git stash"
	time.sleep(5)
	os.system(cmd_5)
	cmd_3='git pull --rebase'
	os.system(cmd_3)
	time.sleep(5)
	cmd_4='git submodule update --init --recursive'
	os.system(cmd_4)
	time.sleep(5)
	print("Command Ran Successfully")

def checkout_3_14_dev_staging():
	cmd_1='git checkout CI/3.14-dev-staging'
	os.system(cmd_1)
	time.sleep(2)
	cmd_2='git status'
	os.system(cmd_2)
	time.sleep(2)
	cmd_5="git stash"
	os.system(cmd_5)
	time.sleep(3)
	cmd_3='git pull --rebase'
	os.system(cmd_3)
	time.sleep(5)
	cmd_4='git submodule update --init --recursive'
	os.system(cmd_4)
	time.sleep(5)
	print("Command Ran Successfully")

def checkout_4_0_dev():
	cmd_1='git checkout CI/4.0-dev'
	os.system(cmd_1)
	time.sleep(2)
	cmd_2='git status'
	os.system(cmd_2)
	time.sleep(2)
	cmd_5="git stash"
	os.system(cmd_5)
	time.sleep(3)
	cmd_3='git pull --rebase'
	os.system(cmd_3)
	time.sleep(5)
	cmd_4='git submodule update --init --recursive'
	os.system(cmd_4)
	time.sleep(5)
	print("Command Ran Successfully")

def checkout_particular():
	input_branch=input('Enter the branch you want to checkout.( E.g: 4.0-dev-staging ) --> : ')
	cmd_1='git checkout CI/'+input_branch
	os.system(cmd_1)
	time.sleep(2)
	cmd_2='git status'
	os.system(cmd_2)
	time.sleep(2)
	cmd_5="git stash"
	time.sleep(5)
	os.system(cmd_5)
	cmd_3='git pull --rebase'
	os.system(cmd_3)
	time.sleep(5)
	cmd_4='git submodule update --init --recursive'
	os.system(cmd_4)
	time.sleep(5)
	print("Command Ran Successfully")

def clear():
	cmd='clear'
	os.system(cmd)

