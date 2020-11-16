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
        ch = r.recognize_google(audio)
        
        if ('linux' in sh) or ('Linux' in ch):
                wb.open('ip:80/cgi-bin/backend.py?x=linux')
                print("Menu opened in browser...")
                print("What next?")
                with r.Microphone() as source:
                        print("listening....")
                        audio = r.listen(source)
                        print("done..")
                y = r.recognize_google(audio)
                if ('directory' in y):
                        print("Name of directory")
                        with r.Microphone() as source:
                                print("listening....")
                                audio = r.listen(source)
                                print("done..")
                        z = r.recognize_google(audio)
                        wb.open('ip:80/cgi-bin/backend.py?x=linux&y=1&z={}'.format(z))
                        
        
  
