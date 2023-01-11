#!/usr/bin/env python3
import os
import time

class Alive:
    def __init__(self,sys_name,hours):
        self.sys_name=sys_name
        self.hours=hours
    def alive(self,sys_name,hours):
        print("\n************Starting System Alive****************\n")
        for i in range(0,hours):
            try:
                print("\n \nMachine running from {} hours after starting of tool \n ".format(i))
                cmd="curl https://bcg0qarj4g.execute-api.eu-west-1.amazonaws.com/prod/system/keepalive?system={}&env=aws&token=qTQ7zIRMws2n1iV92hCw&action=keepalive".format(sys_name)
                os.system(cmd)
                time.sleep(3600)
            except KeyboardInterrupt:
                print("\n\nThe system won't be alive since it is stopped!")
                raise SystemExit

sys=input("Input System Name to make it alive : ")
hour=int(input("Input the number of hours for making the cluster alive : "))
Obj=Alive(sys,hour)
Obj.alive(sys,hour)

