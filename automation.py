import os
import time

print("*******PROGRAM TO CREATE LEGACY CLIENTS********** \n ")
system=input("Enter the name of the system: ")
inp1=int(input("Enter starting host id for mounting to stateless clients: "))
inp2=int(input("Enter Ending host id for mounting to stateless clients: "))
for i in range(inp1,inp2+1):
    cmd="ssh {}-{}.wekalab.io 'weka local stop -f && weka local rm -f --all'".format(system,i)
    os.system(cmd)
    time.sleep(5)
    cmd="ssh {}-{}.wekalab.io 'sudo weka local setup host --name default --base-port 14000'".format(system,i)
    os.system(cmd)
    time.sleep(2)
time.sleep(5)
for j in range(inp1,inp2+1):
    cmd="ssh {}-2.wekalab.io 'weka cluster container add {}-{}'".format(system,system,j)
    os.system(cmd)

print("*******PROGRAM TO MOUNT STATELESS CLIENTS********** \n ")
##Program to mount the filesystem
st_cl=int(input("Enter starting host id for mounting to stateless clients: "))
cl_cl=int(input("Enter Ending host id for mounting to stateless clients: "))
clients=[]
en_ip=input("Enter the backend IP seperated by (,) : ")
for i in range(st_cl,cl_cl+1):
        clients.append(i)
back_ip=en_ip.split(",")
for (a,b) in zip(clients,back_ip):
    cmd="ssh {}-{}.wekalab.io 'weka local stop -f && weka local rm -f --all && mkdir -p /mnt/weka && chmod 777 /mnt/weka && mount -t wekafs -o net=udp {}:/default /mnt/weka'".format(system,a,b)
    os.system(cmd)
    time.sleep(5)

