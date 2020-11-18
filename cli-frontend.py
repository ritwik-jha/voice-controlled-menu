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
        
        if ('linux' in record) or ('Linux' in record):
                wb.open('ip:80/cgi-bin/backend.py?x=linux')
                print("Menu opened in browser...")
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
                        wb.open('ip:80/cgi-bin/backend.py?x=linux&y=1&z={}'.format(z))
                 elif ('list' in ch) or ('show all' in ch):
                        wb.open('ip:80/cgi-bin/backend.py?x=linux&y=2')
                 elif ('create' or 'make' in ch) and ('empty' or 'blank' in ch) and ('file' in ch):
			print("Give the name of file")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=3&z={}'.format(z))
		elif ('create' in ch) and ('file' in ch):
			print("Give the name of file")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=4&z={}'.format(z))
		elif ('add' or 'make' in ch) and ('user' in ch):
			print("Give the name of user")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=5&z={}'.format(z))
		elif ('set' or 'make' in ch) and ('password' or 'passcode' in ch):
			print("Give the password")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=6&z={}'.format(z))
		elif ('show' or 'what' in ch) and ('ram' in ch) and ('usage' or 'utilization' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=7')
		elif ('show' or 'what' in ch) and ('disk' in ch) and ('usage' or 'utilization' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=8')
		elif ('package' or 'software' in ch) and ('present' in ch):
			print("give name of package")
			with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=9&z={}'.format(z))
        	elif ('package' or 'software' in ch) and ('delete' in ch):
			print("give name of package")
			with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=10&z={}'.format(z))
		elif ("ip" or "network configuration" in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=11')
		elif ('java' in ch) and ('processes' or 'process' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=12')
		elif ('cpu' or 'CPU' in ch) and ('information' or 'info' or 'data' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=13')
		elif ('running' in ch) and ('processes' or 'process' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=14')
		elif ('running' in ch) and ('time' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=15')
		elif ('clear' or 'clean') and ('chache' or 'chaches' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=16')
		elif ('which' or 'what' in ch) and ('package' or 'software' in ch) and ('provides' in ch):
			print("give name of package")
			with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=17&z={}'.format(z))
		elif ('ping' in ch) or ('check connectivity' in ch):
			print("give the ip of system")
			with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=18&z={}'.format(z))
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
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=19&z={}&a={}'.format(z,a))
		elif ('go back' or 'previous' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=linux&y=20')
		else:
			print("ERROR: invalid search")
	if ("docker" in record):
		wb.open("ip:80/cgi-bin/backend.py?x=docker")
		print("Options opened in browser")
		print("What next?")
		with r.Microphone() as source:
                	print("listening....")
                        audio = r.listen(source)
                        print("done..")
                ch = r.recognize_google(audio)
		if ('docker version' or 'version' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=1')
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
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=2&z={}&a={}'.format(z,a))
		elif ('image' in ch) and ('pull' in ch):
			print('Give the name of the image')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=3&z={}'.format(z))
		elif ('list' in ch) and ('running' in ch) and ('containers' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=4')
		elif ('list' and 'all' in ch) and ('containers' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=5')
		elif ('list' in ch) and ('images' in ch):
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=6')
		elif ('container' in ch) and ('start' in ch):
			print('Give the name/id of the container')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=7&z={}'.format(z))
		elif ('container' in ch) and ('stop' in ch):
			print('Give the name/id of the container')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=8&z={}'.format(z))
		elif ('container' in ch) and ('delete' in ch):
			print('Give the name/id of the container')
			with r.Microphone() as source:
                		print("listening....")
                        	audio = r.listen(source)
                       		print("done..")
			z = r.recognize_google(audio)
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=9&z={}'.format(z))
		elif ('container' in ch) and ('stop' in ch) and ('all' in ch): 
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=11')
		elif ('container' in ch) and ('delete' in ch) and ('all' in ch): 
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=10')
		elif ('go' or 'show' in ch) and ('back' or 'previous' in ch): 
			wb.open('ip:80/cgi-bin/backend.py?x=docker&y=12')
		else:
			print("ERROR: Couldn't understand the command")
