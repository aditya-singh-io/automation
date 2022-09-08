#!/usr/bin/env python3.7
#Program to create cluster
####
######@Author : Aditya Singh alias: aditya.singh@weka.io

import os
import time


#seq 0 5  | xargs -n1 -IH -P10 ssh root@test-mbc-H sudo weka local resources -C drives0
#seq 0 5  | xargs -n1 -IH -P10 ssh root@test-mbc-H sudo weka local resources -C compute0
#seq 0 5  | xargs -n1 -IH -P10 ssh root@test-mbc-H sudo weka local resources -C frontend0

cluster_name=input("Enter the name of the cluster : ")
b_host=input("Number of backends : ")
b_int_host=int(b_host)-1
cmd='seq 0 {}  | xargs -n1 -IH -P10 ssh root@{}-H sudo weka local stop -f'.format(b_int_host,cluster_name)
print(cmd)
os.system(cmd)
time.sleep(5)
#
cmd='seq 0 {}  | xargs -n1 -IH -P10 ssh root@{}-H sudo weka local rm -f --all'.format(b_int_host,cluster_name)
print(cmd)
os.system(cmd)
time.sleep(5)
#
cmd='seq 0 {}  | xargs -n1 -IH -P10 ssh root@{}-H sudo weka local ps'.format(b_int_host,cluster_name)
print(cmd)
os.system(cmd)
time.sleep(5)
#creating drive container
inp_core=input("Enter number of cores for 'drive' container : ")
cmd='seq 0 {}  | xargs -n1 -IH -P10 ssh root@{}-H sudo weka local setup host --name drive --base-port 14000 --cores={} --core-ids=1 --only-drives-cores'.format(b_int_host,cluster_name,int(inp_core))
print(cmd)
os.system(cmd)
time.sleep(5)
#creating cluster
ip=input("Enter the list of IP's connected by ','")
cluster_det=[]
for i in range(0,int(b_host)):
	p=cluster_name+"-"+str(i)
	cluster_det.append(p)
cluster=" ".join(cluster_det)
cmd='weka cluster create {} --host-ips {}'.format(cluster,ip)
print(cmd)
os.system(cmd)
time.sleep(5)
#
cmd='weka local resources'
os.system(cmd)
#creating compute container
inp_core=input("Enter number of cores for 'compute' container : ")
cmd='seq 0 {}  | xargs -n1 -IH -P10 ssh root@{}-H sudo weka local setup host --name compute --base-port 21000 --cores={} --core-ids 2 --only-compute-cores --memory 1GB --join-ips={}'.format(b_int_host,cluster_name,int(inp_core),ip.split(',')[0])
print(cmd)
os.system(cmd)
time.sleep(5)

#listing cluster details
cmd='weka cluster host'
print(cmd)
os.system(cmd)

#Attaching drives

cmd='seq 0 {} | xargs -IDD -P10 weka cluster drive add DD /dev/sdb'.format(b_int_host)
print(cmd)
os.system(cmd)
time.sleep(5)

#Status
cmd='weka status'
print(cmd)
os.system(cmd)

#adding net devices in all backends for drive
inp_dev=input("Enter the the net device for 'drive' container for backend {} : ".format(cluster_name))
for i in range(0,int(b_host)):
	inp_ip=input("Enter the the IP for 'drive' container for backend {}-{} : ".format(cluster_name,i))
	cmd='ssh {}-{} "weka local resources net add {} --container drive --ips {} --gateway 10.108.0.1 --netmask 16"'.format(cluster_name,i,inp_dev,inp_ip)
	print(cmd)	
	os.system(cmd)	

#adding net devices in all backends for frontend
inp_dev=input("Enter the the net device for 'compute' container for backend {} : ".format(cluster_name))
for i in range(0,int(b_host)):
	inp_ip=input("Enter the the IP for 'compute' container for backend {}-{} : ".format(cluster_name,i))
	cmd='ssh {}-{} "weka local resources net add {} --container compute --ips {} --gateway 10.108.0.1 --netmask 16"'.format(cluster_name,i,inp_dev,inp_ip)
	print(cmd)
	os.system(cmd)

#creating failure domain
cmd="for i in  `seq  0 11 `; do weka cluster host failure-domain $i --name FD-$i; done"
os.system(cmd)
cmd='weka cloud enable'
os.system(cmd)

#license
inp_license=input("Enter the license to be enabled in the cluster : ")
cmd='weka cluster license set '+inp_license
os.system(cmd)

#applying resources
cmd='weka cluster host apply --all -f'
os.system(cmd)
time.sleep(15)

#status
cmd='weka cluster host'
os.system(cmd)

#start io
cmd='weka cluster start-io'
os.system(cmd)
time.sleep(15)

#status
cmd='weka cluster host'
os.system(cmd)

p=input("Do you want to setup frontend container : (y/N)")
if 'y' in p or 'Y' in p:
	cmd='weka local setup host --name frontend --base-port 22000 --cores=1 --core-ids 3 --only-frontend-cores --join-ips {}'.format(ip.split(',')[0])
	os.system(cmd)
#adding net devices in all backends for frontend
	inp_dev=input("Enter the the net device for 'frontend' container : ")
	for i in range(0,int(b_host)):
		inp_ip=input("Enter the the IP for 'frontend' container for backend {}-{}".format(cluster_name,i))
		cmd='ssh {}-{} "weka local resources net add {} --container frontend --ips {} --gateway 10.108.0.1 --netmask 16"'.format(cluster_name,i,inp_dev,inp_ip)
		os.system(cmd)
