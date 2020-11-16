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
        	09. Check if command is present
        	10. Removes a command
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
		
	
