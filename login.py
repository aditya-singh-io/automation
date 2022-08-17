#!/usr/bin/env python3.7
#Program to create cluster
####
######@Author : Aditya Singh alias: aditya.singh@weka.io
import os
import time

cmd_fs="weka fs snapshot"
for i in range(5,20):
    cmd1="ssh 130.61.144.175 '{}; weka fs snapshot create default snap{} '".format(cmd_fs,i)
    os.system(cmd1)
    time.sleep(2)


