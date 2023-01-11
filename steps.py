import time
import os

system=input("Enter the name of the system : ")
#Program for creating legacy client
for i in range(12,19):
    cmd="ssh {}-1.wekalab.io 'weka cluster container deactivate {} --allow-unavailable'".format(system,i)
    os.system(cmd)
    time.sleep(5)
    cmd="ssh {}-1.wekalab.io 'weka cluster container cores {} 1 --frontend-dedicated-cores 1'".format(system,i)
    os.system(cmd)
    time.sleep(5)
    cmd="ssh {}-1.wekalab.io 'weka cluster container apply {} --force'".format(system,i)
    os.system(cmd)
    time.sleep(15)
    cmd="ssh {}-1.wekalab.io 'weka cluster container activate {}'".format(system,i)
    os.system(cmd)
