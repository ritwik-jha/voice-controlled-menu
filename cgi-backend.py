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
	# AWS start
	
	elif x=="aws":
		print("""
		01. Configure AWS
        	02. Create a Key-Pair
        	03. Create a Security Group
        	04. Launching an instance
        	05. Creating EBS
        	06. Attaching EBS
        	07. Creating S3 Bucket
        	08. Storing file in S3 Bucket
        	00. Go to previous menu
		""")
		
		y = input()
		if choice == "1":
            		os.system("aws configure")
        	elif choice == "2":
            		z = input()
            		os.system("aws ec2 create-key-pair --key-name {}".format(z))
        	elif choice == "3":
            		z = input()
            		a = input()
            		os.system('aws ec2 create-security-group --group-name {} --description {}'.format(z,a))
        	elif choice == "4":
            		z = input()
            		a = input()
            		b = input()
            		c = input()
            		d = input()
            		e = input()
            		os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --key-name {} --security-group-ids {}".format(z,a,b,c,d,e))
        	elif choice == "5":
            		z = input()
            		a = input()
            		os.system("aws ec2 create-volume --availability-zone {} --no-encrypted --size {}".format(z,a))
        	elif choice == "6":
            		z = input()
           		a = input()
           		os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device xvdh".format(z,a))
        	elif choice == "7":
            		z = input()
            		a = input("Enter the region: ")
            		os.system = input("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(z,a,a))
        	elif choice == "8":
            		z = input("Enter the name of the bucket: ")
            		b = input("Enter the path of the object with name: ")
            		a = input("Enter the name which you want to give to the object when i will save in the bucket: ")
            		os.system = input("aws s3api put-object --bucket {} --key {} --body \"{}\"".format(z,a,b))
        	elif choice == "0":
            		continue
        	else:
            		print("ERROR: Command not found")

	
	# AWS end
	
	elif x=="docker":
		print("""
        	01. Checks the docker version
        	02. Launching a container
        	03. Pull image from dockerhub
        	04. List running docker containers
        	05. List all docker containers
        	06. List all images present in system
        	07. Starting a docker container
        	08. Stopping a docker container
        	09. Deleting a docker container
        	10. Stop all docker containers
        	11. Delete all docker containers
        	00. Go to previous menu
        	""")
		
		y = input()
		if y=="1":
			os.system("docker --version")
		elif y=="2":
			z = input()  #container name
			a = input()  #image
			os.system("docker run -it --name {} {}".format(z,a))
		elif y=="3":
			z = input() #image name
			os.system("docker pull {}".format(z))
		elif y=="4":
			os.system("docker ps")
		elif y=="5":
			os.system("docker ps -a")
		elif y=="6":
			os.system("docker images")
		elif y=="7":
			z = input() #container name/id
			os.system("docker start {}".format(z))
		elif y=="8":
			z = input() #container name/id
			os.system("docker stop {}".format(z))
		elif y=="9":
			z = input() #container name/id
			os.system("docker rm {}".format(z))
		elif y=="10":
			os.system("docker container rm $(docker container ls –aq")
		elif y=="11":
			os.system("docker container stop $(docker container ls –aq) && docker system prune –af ––volumes")
		elif y=="12":
			continue
		else:
			print("ERROR: command not found")
	elif x=="hadoop":
		print("""
        	01. Checks the hadoop version
        	02. Format a hadoop namenode
        	03. Start the namenode service
        	04. Start the datanode service
        	05. Show the hadoop report in namenode
        	06. List all files present in hadoop filesystem
        	07. Upload the file to hadoop filesystem
        	08. Remove the file from hadoop filesystem
        	09. List the contents of a file in hdfs
        	10. Upload the file with a defined block size
        	11. Create an empty file in hadoop filesystem
        	00. Go to previous menu
        	""")
		y = input()
		
		if y=="1":
			os.system("hadoop version")
		elif y=="2":
			os.system("hadoop namenode -format")
		elif y=="3":
			os.system("hadoop-daemon.sh start namenode")
		elif y=="4":
			os.system("hadoop-daemon.sh start datanode")
		elif y=="5":
			os.system("hadoop dfsadmin -report")
		elif y=="6":
			os.system("hadoop fs -ls /")
		elif y=="7":
			z = input()
			a = input()
			os.system("hadoop fs -put {} /{} ".format(z,a))
		elif y=="8":
			z = input()
			os.system("hadoop fs -rm /{}".format(z))
		elif y=="9":
			z = input()
			os.system("hadoop fs -cat /{}".format(z))
		elif y=="10":
			z = input()
			a = input()
			os.system("hadoop fs -Ddfs.block.size={} -put {} /".format(z))
		elif y=="11":
			z = input()
			os.system("hadoop fs -touchz  {} /".format(z))
		elif y=="12":
			continue
		else:
			print("ERROR: command not found")
			
			
			
		
			
		
	
