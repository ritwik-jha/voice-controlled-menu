import subprocess as sp
import os
import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()

while True:
        os.system("tput setaf 10")
        print("\t\tWELCOME TO VOICE CONTROLLED AUTOMATION MENU")
        print("\t\t--------------------------------")
        print()
        print()
        print("which services would you like to automate:")
        print("""
        01. Linux
        02. AWS
        03. Hadoop
        04. Docker
        05. Exit
        """)
        input("Press enter....")
        with r.Microphone() as source:
                print("We are listening to you.......")
                audio = r.listen(source)
                print("done...")
        record = r.recognize_google(audio)
        
	
	
	# linux frontend
        if ('linux' in record) or ('Linux' in record):
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
                print("What next?")
                with r.Microphone() as source:
                        print("listening....")
                        audio = r.listen(source)
                        print("done..")
                ch = r.recognize_google(audio)
                if ('directory' in ch):
                        print("Name of directory")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
                        str = "mkdir " + z
			os.system(str)
		elif ('list' in ch) or ('show all' in ch):
			os.system("ls")
                elif ('create' or 'make' in ch) and ('empty' or 'blank' in ch) and ('file' in ch):
			print("Give the name of file")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=3&z={}'.format(z))
			str = "touch "+ z
			os.system(str)
		elif ('create' in ch) and ('file' in ch):
			print("Give the name of file")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=4&z={}'.format(z))
			str = "cat " + z
			os.system(str)
		elif ('add' or 'make' in ch) and ('user' in ch):
			print("Give the name of user")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=5&z={}'.format(z))
			str = "useradd " + z
			sp.getoutput(str)
		elif ('set' or 'make' in ch) and ('password' or 'passcode' in ch):
			print("Give the password")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=6&z={}'.format(z))
			str = "passwd " + z
			os.system(str)
		elif ('show' or 'what' in ch) and ('ram' in ch) and ('usage' or 'utilization' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=7')
			os.system("free -m")
		elif ('show' or 'what' in ch) and ('disk' in ch) and ('usage' or 'utilization' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=8')
			os.system("df -hT")
		elif ('package' or 'software' in ch) and ('present' in ch):
			print("give name of package")
			with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=9&z={}'.format(z))
			os.system("rpm -q {}".format(z))
        	elif ('package' or 'software' in ch) and ('delete' in ch):
			print("give name of package")
			with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=10&z={}'.format(z))
			os.system("rpm -e {}".format(z))
		elif ("ip" or "network configuration" in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=11')
			os.system("ifconfig")
		elif ('java' in ch) and ('processes' or 'process' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=12')
			os.system("jps")
		elif ('cpu' or 'CPU' in ch) and ('information' or 'info' or 'data' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=13')
			os.system("lscpu")
		elif ('running' in ch) and ('processes' or 'process' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=14')
			os.system("ps -aux")
		elif ('running' in ch) and ('time' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=15')
			os.system("uptime")
		elif ('clear' or 'clean') and ('chache' or 'chaches' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=16')
			os.system("echo 3 > /proc/sys/vm/drop_caches")
		elif ('which' or 'what' in ch) and ('package' or 'software' in ch) and ('provides' in ch):
			print("give name of package")
			with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=17&z={}'.format(z))
			os.system("yum whatprovides {}".format(z))
		elif ('ping' in ch) or ('check connectivity' in ch):
			print("give the ip of system")
			with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=18&z={}'.format(z))
			os.system("ping {}".format(z))
		elif ('create user' in ch) and ('command' in ch):
			print("give the name of user")
			with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			print("give the command to be run")
			with r.Microphone() as source:
                                print("listening....")
                                audio1 = r.listen(source)
                                print("done..")
                        a = r.recognize_google(audio1)
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=19&z={}&a={}'.format(z,a))
			os.system("useradd -s {} {}".format(z,a))
		elif ('go back' or 'previous' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=linux&y=20')
			continue
		else:
			print("ERROR: invalid search")
			
	# docker frontend
	elif ("docker" in record):
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
		print("What next?")
		with r.Microphone() as source:
                	print("listening....")
                        audio = r.listen(source)
                        print("done..")
                ch = r.recognize_google(audio)
		if ('docker version' or 'version' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=1')
			os.system("docker --version")
		elif ('container' in ch) and ('launch' in ch):
			print('Give the name of the container')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			print('Give the name of the image to  be used')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			a = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=2&z={}&a={}'.format(z,a))
			os.system("docker run -it --name {} {}".format(z,a))
		elif ('image' in ch) and ('pull' in ch):
			print('Give the name of the image')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=3&z={}'.format(z))
			os.system("docker pull {}".format(z))
		elif ('list' in ch) and ('running' in ch) and ('containers' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=4')
			os.system("docker ps")
		elif ('list' and 'all' in ch) and ('containers' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=5')
			os.system("docker ps -a")
		elif ('list' in ch) and ('images' in ch):
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=6')
			os.system("docker images")
		elif ('container' in ch) and ('start' in ch):
			print('Give the name/id of the container')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=7&z={}'.format(z))
			os.system("docker start {}".format(z))
		elif ('container' in ch) and ('stop' in ch):
			print('Give the name/id of the container')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=8&z={}'.format(z))
			os.system("docker stop {}".format(z))
		elif ('container' in ch) and ('delete' in ch):
			print('Give the name/id of the container')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=9&z={}'.format(z))
			os.system("docker rm {}".format(z))
		elif ('container' in ch) and ('stop' in ch) and ('all' in ch): 
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=11')
			os.system("docker container rm $(docker container ls –aq)")
		elif ('container' in ch) and ('delete' in ch) and ('all' in ch): 
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=10')
			os.system("docker container stop $(docker container ls –aq) && docker system prune –af ––volumes")
		elif ('go' or 'show' in ch) and ('back' or 'previous' in ch): 
			#wb.open('ip:80/cgi-bin/backend.py?x=docker&y=12')
			continue
		else:
			print("ERROR: Couldn't understand the command")
			
	# hadoop fronend
	elif ("hadoop" in record):
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
		print("What next?")
		with r.Microphone() as source:
                	print("listening....")
                        audio = r.listen(source)
                       	print("done..")
		ch = r.recognize_google(audio)
		if ("show" in ch) and ("hadoop" in ch) and ("version" in ch):
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=1")
			os.system("hadoop version")
		elif ("namenode" in ch) and ("format" in ch):
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=2")
			os.system("hadoop namenode -format")
		elif ("start" in ch) and ("namenode" in ch):
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=3")
			os.system("hadoop-daemon.sh start namenode")
		elif ("start" in ch) and ("datanode" in ch):
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=4")
			os.system("hadoop-daemon.sh start datanode")
		elif ("hadoop" or "namenode" in ch) and ("report" in ch):
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=5")
			os.system("hadoop dfsadmin -report")
		elif ("list" in ch) and ("cluster" or "filesystem" in ch):
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=6")
			os.system("hadoop fs -ls /")
		elif ("upload" or "put" in ch) and ("files" or "file" in ch):
			print("File name?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			print("File destination in cluster?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio1 = r.listen(source)
                       		print("done..")
			a = r.recognize_google(audio1)
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=7&z={}&a={}".format(z,a))
			os.system("hadoop fs -put {} /{} ".format(z,a))
		elif ("remove" or "delete" in ch) and ("hadoop" or "cluster" or "file system" in ch):
			print("File name?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=8&z={}".format(z))
			os.system("hadoop fs -rm /{}".format(z))
		elif ("read" or "show" in ch) and ("file" in ch):
			print("File name?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=9&z={}".format(z))
			os.system("hadoop fs -cat /{}".format(z))
		elif ("block size" in ch) and ("upload" or "load" in ch) and ("file system" or "cluster" in ch):
			print("Block size?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			print("File name?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio1 = r.listen(source)
                       		print("done..")
			a = r.recognize_google(audio1)
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=10&z={}&a={}".format(z,a))
			os.system("hadoop fs -Ddfs.block.size={} -put {} /".format(z))
		elif ("create" or "make" in ch) and ("empty" in ch) ("file" in ch):
			print("File name?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=11&z={}".format(z))
			os.system("hadoop fs -touchz  {} /".format(z))
		elif ("go back" or "show previous" in ch):
			#wb.open("ip:80/cgi-bin/backend.py?x=hadoop&y=12")
			continue
		else:
			print("ERROR: Couldn't find anything")
	
	#AWS frontend
	elif ("aws" or "AWS" or "A W S" in record):
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
		print("What next?")
		with r.Microphone() as source:
                	print("listening....")
                        audio = r.listen(source)
                       	print("done..")
		ch = r.recognize_google(audio)
		if ("configure" in ch) and ("aws" in ch):
			#wb.open("ip:80/cgi-bin/backend.py?x=aws&y=1")
			os.system("aws configure")
		elif ("create" or "make" in ch) and ("key" in ch) and ("pair" in ch):
			print("key name ?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			#wb.open("ip:80/cgi-bin/backend.py?x=aws&y=2&z={}".format(z))
			os.system("aws ec2 create-key-pair --key-name {}".format(z))
		elif ("create" or "make" in ch) and ("security" in ch) and ("group" in ch):
			print("security group name?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			print("description?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio1 = r.listen(source)
                       		print("done..")
			a = r.recognize_google(audio1)
			#wb.open("ip:80/cgi-bin/backend.py?x=aws&y=3&z={}&a={}".format(z,a))
			os.system('aws ec2 create-security-group --group-name {} --description {}'.format(z,a))
		elif ("launch" or "open" in ch) and ("instance" or "os" in ch):
			print("image id?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			print("instance type?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			a = r.recognize_google(audio)
			print("count?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			b = r.recognize_google(audio)
			print("subnet id?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			c = r.recognize_google(audio)
			print("key name?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			d = r.recognize_google(audio)
			print("security group id")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			e = r.recognize_google(audio)
			#wb.open("ip:80/cgi-bin/backend.py?x=aws&y=4&z={}&a={}&b={}&c={}&d={}&e={}".format(z,a,b,c,d,e))
			os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --key-name {} --security-group-ids {}".format(z,a,b,c,d,e))
		elif ("create" or "make" in ch) and ("ebs" or "EBS" in ch) and ("storage" or "volume" in ch):
			print("availability zone?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			print("size/volume?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			a = r.recognize_google(audio)
			#wb.open("ip:80/cgi-bin/backend.py?x=aws&y=5&z={}&a={}".format(z,a))
			os.system("aws ec2 create-volume --availability-zone {} --no-encrypted --size {}".format(z,a))
		elif ("attach" or "connect" in ch) and ("volume" or "storage" in ch):
			print("instance id?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			print("volume id?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			a = r.recognize_google(audio)
			#wb.open("ip:80/cgi-bin/backend.py?x=aws&y=6&z={}&a={}".format(z,a))
			os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device xvdh".format(z,a))
		elif ("create" or "make" in ch) and ("bucket" in ch):
			print("bucket name?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			print("region?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			a = r.recognize_google(audio)
			#wb.open("ip:80/cgi-bin/backend.py?x=aws&y=7&z={}&a={}".format(z,a))
			os.system = input("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(z,a,a))
		elif ("put" or "store" in ch) and ("bucket" in ch):
			print("bucket name?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			print("body?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			a = r.recognize_google(audio)
			print("key?")
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			b = r.recognize_google(audio)
			#wb.open("ip:80/cgi-bin/backend.py?x=aws&y=8&z={}&a={}&b={}".format(z,a,b))
			os.system = input("aws s3api put-object --bucket {} --key {} --body \"{}\"".format(z,a,b))
		elif ("go back" or "previous menu" in ch):
			#wb.open("ip:80/cgi-bin/backend.py?x=aws&y=0")
			continue
		input()
		os.system('clear')
