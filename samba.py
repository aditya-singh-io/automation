import os

cluster_name=input("Enter the name of the cluster : ")
be=input("Enter the size of the be : ")
size_be=int(be)-1
cmd1_s='weka user ldap setup-ad 10.112.133.239 weka.lab wekadmin@weka.lab myW3ka.io --cluster-admin-group "Enterprise Admins" --regular-group "WekaGroup" --readonly-group "TestGroup"'
cmd2='''pdsh -R ssh -w "test-adi-[0-4].wekalab.io" "sed -i.bak 's/^search /search weka.lab. /' /etc/resolv.conf && sed -i.bkp '/search weka.lab. regvcn.oraclevcn.com/i \nameserver 10.112.133.239 \noptions ndots:2 \noptions timeout:1' /etc/resolv.conf"'''
cmd3_s='cat /etc/resolv.conf'
p=[]
for i in range(0,len(be)):
    p.append(i)
cmd4_s='weka smb cluster create smb weka.lab --samba-hosts {} --domain-netbios-name LAB && weka smb share add samba smb-fio && mkdir /mnt/test && mount -t wekafs smb-fio /mnt/test && sleep 3 && chmod 777 /mnt/test'.format(p)
cmd5_s='weka smb domain join wekadmin@weka.lab myW3ka.io'

server="ssh root@{}-0.wekalab.io '{}'".format(cluster_name,cmd1_s)
os.system(server)

os.system(cmd2)
server="ssh root@{}-0.wekalab.io '{}; {}; {}'".format(cluster_name,cmd3_s,cmd4_s,cmd5_s)
os.system(server)

