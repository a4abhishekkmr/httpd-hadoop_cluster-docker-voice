import os
import getpass
print("\t\t\t\t WELCOME TO MY MENU")
os.system("espeak-ng 'Welcome to my menu' ")
#while true:
os.system("clear")
print(""" 
\n
press 1 : to run date
press 2 : to cal
press 3 : to reboot
press 4 : to configure webserver
press 5 : to check the ststus of the webserver
press 6 : to exit
press 7 : to activate the slave node
press 8 : to activate the master
press 9 : to check the cluster status
press 10 : to start docker
press 11 : to check status of docker
press 12: to stop docker
""")

passwd = getpass.getpass("Enter your password")

if passwd != "lw" :
	print("password incorrect ....")
	exit()

r = input("enter you choice remote/local: ")

ch = input("Enter ur choice: ")
print(ch)

if r =="local" :
	if int(ch) ==1:
    			os.system("date")
	elif int(ch) ==2:
			os.system("cal")
	elif int(ch)==3:
			os.sytem("reboot")
	elif int(ch) ==4:
			os.system("systemctl start httpd")
	elif int(ch) ==5:
			os.system("systemctl status httpd")
	elif int(ch) ==6:
			exit()
	elif int(ch)==7:
			os.system("hadoop-daemon.sh start datanode")
			os.system("jps")
	elif int(ch)==8:
			print("please choose remote login for configuring master")
	elif int(ch)==9:
			os.system("hadoop dfsadmin -report")
	elif int(ch) ==10:
			os.system("systemctl start docker")
	elif int(ch) ==11:
			os.system("systemctl status docker")
	elif int(ch) ==12:
			os.system("systemctl stop docker")
	else:
			print("not supported")

elif r =="remote":
		ip=input("Enter remote ip:" )
		if int(ch) ==1:
			os.system("ssh {} date ".format(ip))
		elif int(ch) ==2:
			os.system("ssh {} cal ".format(ip))
		elif int(ch)==3:
			os.system("ssh {} reboot".format(ip))
		elif int(ch)==4:
			os.system("ssh {} systemctl start httpd".format(ip))
		elif int(ch)==5:
			os.system("ssh {} systemctl status httpd".format(ip))
		elif int(ch) ==6:
			exit()
		elif int(ch) ==7:
			print("this system is configured as datanode, choose local login")
		elif int(ch) ==8:
			os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
			os.system("ssh {} cal ".format(ip))
		elif int(ch) ==9:
			os.system("ssh {} hadoop dfsadmin -report".format(ip))
		elif int(ch)==10:
			os.system("ssh {} systemctl start docker".format(ip))
		elif int(ch)==11:
			os.system("ssh {} systemctl status docker".format(ip))
		elif int(ch)==12:
			os.system("ssh {} systemctl stop docker".format(ip))
		else:
			print("not supported")
else:
		print("not supported login")
