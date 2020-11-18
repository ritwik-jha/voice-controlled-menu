import subprocess as sp
import os

while True:
	x = input()
	if x=="linux":
		print("""
		01. Create a directory
        	02. List files in current directory
       	 	03. Create an empty file
        	04. Create a file and open for editing
        	05. Add a new user
        	06. Set/change password
        	07. Show current RAM usage
        	08. Show the disk usage
        	09. Check if package is present
        	10. Remove a package
        	11. Lists the network configuration
        	12. Checks the java running services
        	13. List the CPU info
        	14. Show currenty running processes
        	15. Show running time of device
        	16. Clear the cache
        	17. Check which package provide the command
        	18. Checks the connectivity to IP
        	19. Create a user for running a specific command
        	00. Go to previous menu
		""")
		y = input()
		if y=="1":
			z = input()
			str = "mkdir " + z
			os.system(str)
		elif y=="2":
			os.system("ls")
		elif y=="3":
			z = input()
			str = "touch "+ z
			os.system(str)
		elif y=="4":
			z = input()
			str = "cat " + z
			os.system(str)
		elif y=="5":
			z = input()
			str = "useradd " + z
			sp.getoutput(str)
		elif y=="6":
			z = input()
			str = "passwd " + z
			os.system(str)
		elif y=="7":
			os.system("free -m")
		elif y=="8":
			os.system("df -hT")
		elif y=="9":
			z = input()
			os.system("rpm -q {}".format(z))
		elif y=="10":
			z = input()
			os.system("rpm -e {}".format(z))
		elif y=="11":
			os.system("ifconfig")
		elif y=="12":
			os.system("jps")
		elif y=="13":
			os.system("lscpu")
		elif y=="14":
			os.system("ps -aux")
		elif y=="15":
			os.system("uptime")
		elif y=="16":
			os.system("echo 3 > /proc/sys/vm/drop_caches")
		elif y=="17":
			z = input()
			os.system("yum whatprovides {}".format(z))
		elif y=="18":
			z = input()
			os.system("ping {}".format(z))
		elif y=="19":
			z = input()
			a = input()
			os.system("useradd -s {} {}".format(z,a))
		elif y=="20":
			continue
		else:
            		print("ERROR: Command not found")
		
			
		
	
