#!/usr/bin/python

import os
import time
import csv
from colorama import init
from bs4 import BeautifulSoup
import argparse
import pyfiglet
from termcolor import colored
import bs4

init()
# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
Y = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'

# Email Template Variables
#{{user.firstname}} The target's first name
#{{user.lastname}} The target's last name
#{{user.email}} The target's email address

SMTP_Server = ""
Port = ""
User = ""
Password = ""
#Mail_From = ""
Mail_From = ""
#"Display Name <add@re.ss>" Sender's name address (or address only).
From = ""
RCPT_TO = ""
#"Display Name <add@re.ss>"
To = "" 
Subject = ""
#Plaintext and/or HTML body of the message If both are provided the message is sent as multipart.
#<text|filename>
Plain_Text_Body = "" 
#<text|filename>
Html_Body = ""
#Attach a given filename. MIME-Type of the attachment is guessed by default guessed but can optionally be specified after '@' delimiter. For instance: --attach mail.log@text/plain Parameter can be used multiple times.
#<filename>[@<MIME/Type>]
File_Attachement = "" 
#Attach a given filename (typically a picture)as a 'related' part to the above 'body-html'. Refer to these pictures as <img src='cid:filename'> in the 'body-html' contents. See --attach for details about MIME-Type. Can be used multiple times.
Inline_Attachement = ""
temptemplate = "Temp.html"
#Time delay per email default is 1 minute
Time = "60"

def banner():
        
        print(colored(pyfiglet.figlet_format("SMTP Relay Phisher", font="standard"), "red" ))


def Email_Template_Alter(FirstName,LastName,Email):
        with open(Html_Body, "r") as f:
                data = f.read()
                data = data.replace('{{user.firstname}}',FirstName)
                data = data.replace('{{user.lastname}}',LastName)
                data = data.replace('{{user.email}}',Email)
                soup = BeautifulSoup(data, 'lxml')
                #print soup
                html =  (soup.prettify())
                #print html
        with open(temptemplate, "w") as outf:
                #outf.write(str(soup))
                outf.write(html.encode('utf-8'))

def Mail_Send(Login_Details,User_CSV):
    if Login_Details:
        if not (User.strip() and Password.strip()):
            print R+"[+] "+END+Y+"Add SMTP username and password above in the script"+END
            
        else:
            if not (Plain_Text_Body.strip() or Html_Body.strip() or File_Attachement.strip() or Inline_Attachement.strip()):
                    print R+"[+] "+END+Y+"Please provide any one from Plain_Text_Body, Html_Body, File_Attachement and Inline_Attachement for sending the email"+END
            else:
                    file = open(User_CSV,'r')
                    content = csv.reader(file)
                    for data in content:
                        FirstName = str(data[0])
                        FirstName = FirstName.rstrip()
                        FirstName = FirstName.lstrip()
                        LastName = str(data[1])
                        LastName = LastName.rstrip()
                        LastName = LastName.lstrip()
                        Email = str(data[2])
                        Email = Email.rstrip()
                        Email = Email.lstrip()
                        Email_Template_Alter(FirstName,LastName,Email)
                        print G+"[+]"+END+O+"Email sending to "+END+G+FirstName+" "+LastName+END+" : "+END+Y+"<"+Email+">"+END
                        cmd = './custom-smtp-cli --text-encoding=8bit --missing-modules-ok --host '+SMTP_Server+':'+str(Port)+' --user '+User+' --password '+Password+' --from '+Mail_From+' --to '+Email+' --subject "'+Subject+'" --body-plain "'+Plain_Text_Body+'" --body-html "'+temptemplate+'" --attach "'+File_Attachement+'" --attach-inline "'+Inline_Attachement+'"'
                        #print cmd
                        cmd = cmd+' | '+'tee -a emaillogs.txt'
                        os.system(cmd)
                        os.remove(temptemplate)
                        time.sleep(float(Time))


    else:
            if not (Plain_Text_Body.strip() or Html_Body.strip() or File_Attachement.strip() or Inline_Attachement.strip()):
                    print R+"[+] "+END+Y+"Please provide any one from Plain_Text_Body, Html_Body, File_Attachement and Inline_Attachement for sending the email"+END
            else:
                    file = open(User_CSV,'r')
                    content = csv.reader(file)
                    for data in content:
                            FirstName = str(data[0])
                            FirstName = FirstName.rstrip()
                            FirstName = FirstName.lstrip()
                            LastName = str(data[1])
                            LastName = LastName.rstrip()
                            LastName = LastName.lstrip()
                            Email = str(data[2])
                            Email = Email.rstrip()
                            Email = Email.lstrip()
                            Email_Template_Alter(FirstName,LastName,Email)
                            print G+"[+]"+END+O+"Email sending to "+END+G+FirstName+" "+LastName+END+" : "+END+Y+"<"+Email+">"+END
                            cmd = './custom-smtp-cli --text-encoding=8bit --missing-modules-ok --host '+SMTP_Server+':'+str(Port)+' --from '+Mail_From+' --to '+Email+' --subject "'+Subject+'" --body-plain "'+Plain_Text_Body+'" --body-html "'+temptemplate+'" --attach "'+File_Attachement+'" --attach-inline "'+Inline_Attachement+'"'
                            #print cmd
                            cmd = cmd+' | '+'tee -a emaillogs.txt'
                            os.system(cmd)
                            os.remove(temptemplate)
                            time.sleep(float(Time))

               
def Mail_Send_RCPT(Login_Details):
    if Login_Details:
        if not (User.strip() and Password.strip()):
            print R+"[+] "+END+Y+"Add SMTP username and password above in the script"+END
            
        else:
            if not (Plain_Text_Body.strip() or Html_Body.strip() or File_Attachement.strip() or Inline_Attachement.strip()):
                    print R+"[+] "+END+Y+"Please provide any one from Plain_Text_Body, Html_Body, File_Attachement and Inline_Attachement for sending the email"+END
            else:
                    print G+"[+]"+END+O+"Email sending to "+To+" <"+RCPT_TO+">"+END
                    cmd = './custom-smtp-cli --host '+SMTP_Server+':'+str(Port)+' --user '+User+' --password '+Password+' --from '+Mail_From+' --to '+RCPT_TO+' --subject "'+Subject+'" --body-plain "'+Plain_Text_Body+'" --body-html "'+Html_Body+'" --attach "'+File_Attachement+'" --attach-inline "'+Inline_Attachement+'"'
                    #print cmd
                    os.system(cmd)
            
    else:
        if not (Plain_Text_Body.strip() or Html_Body.strip() or File_Attachement.strip() or Inline_Attachement.strip()):
                print R+"[+] "+END+Y+"Please provide any one from Plain_Text_Body, Html_Body, File_Attachement and Inline_Attachement for sending the email"+END
        else:
                print G+"[+]"+END+O+"Email sending to "+To+" <"+RCPT_TO+">"+END
                cmd = './custom-smtp-cli --host '+SMTP_Server+':'+str(Port)+' --from '+Mail_From+' --to '+RCPT_TO+' --subject "'+Subject+'" --body-plain "'+Plain_Text_Body+'" --body-html "'+Html_Body+'" --attach "'+File_Attachement+'" --attach-inline "'+Inline_Attachement+'"'
                #print cmd
                os.system(cmd)


def User_Enum(User_CSV):

        file = open(User_CSV,'r')
        content = csv.reader(file)
        for data in content:
                FirstName = str(data[0])
                FirstName = FirstName.rstrip()
                FirstName = FirstName.lstrip()
                LastName = str(data[1])
                LastName = LastName.rstrip()
                LastName = LastName.lstrip()
                Email = str(data[2])
                Email = Email.rstrip()
                Email = Email.lstrip()
                print G+"[+]"+END+O+"Checking User "+END+G+FirstName+" "+LastName+END+" : "+END+Y+"<"+Email+">"+END
                cmd = './custom-smtp-cli --text-encoding=8bit --missing-modules-ok --host '+SMTP_Server+':'+str(Port)+' --from '+Mail_From+' --to '+Email
                cmd = cmd+' | '+'tee -a userenumoutput.txt'
                #print cmd
                os.system(cmd)
                time.sleep(float(Time))
        


def main():

    banner()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-C", "--csv",nargs=1, dest='csv', required=False, help="Provide CSV file which contain list of targets in this format <First Name><Last Name><Email>")
    parser.add_argument("-L", "--credential", action="store_true", help="Mention this option for authenticated email sending. For credential add username and password in the script.")
    parser.add_argument("-U", "--UserEnumeration", action="store_true", help="Find valid user by 'RCPT TO' command. You need to provide CSV file in this format <First Name><Last Name><Email>")
    parser.add_argument("-V", "--verbose", action="store_true", help="Show variables data from the script. It helps you to verify details before running the script.")
    
    args = parser.parse_args()
    User_Data =  args.csv
    Login_Details = args.credential
    User_Enumeration = args.UserEnumeration
    Verbose = args.verbose

    if Verbose:
            print G+BOLD+"Details mentioned in script\n"+END
            print O+"SMTP SERVER: "+END+SMTP_Server
            print O+"PORT: "+END+Port
            print O+"USER: "+END+User
            print O+"PASSWORD :"+END+Password
            print O+"MAIL FROM: "+END+Mail_From
            print O+"FROM: "+END+From
            print O+"RCPT TO: "+END+RCPT_TO
            print O+"TO: "+END+To
            print O+"SUBJECT: "+END+Subject
            print O+"PLAIN TEXT BODY FILE NAME: "+END+Plain_Text_Body
            print O+"HTML BODY FILE NAME: "+END+Html_Body
            print O+"ATTACHEMENT FILE NAME: "+END+File_Attachement
            print O+"INLINE FILE NAME: "+END+Inline_Attachement
            print "\n"

    elif User_Enumeration:
            if User_Data is None:
                    print (R+"[+] "+END+Y+"Please provide CSV file in <First Name><Last Name><Email> format"+END)
            else:

                    User_CSV = User_Data[0]
                    print O+BOLD+"CSV File Name is: "+END+str(User_CSV)
                    User_Enum(User_CSV)
            

    else:
            if not (SMTP_Server.strip() and Port.strip() and Mail_From.strip() and Subject.strip()):
                print (R+"[+] "+END+Y+"Please add input in the script\nSMTP_Server\nPort\nMail_From\nSubject"+END)
            else:
                if User_Data is None:
                    if not (RCPT_TO.strip()):
                        print (R+"[+] "+END+Y+"Please add RCPT_TO in the script or you can use --csv argument. Please check --help"+END)
                    else:
                        Mail_Send_RCPT(Login_Details)
                else:
                    User_CSV = User_Data[0]
                    print O+BOLD+"CSV File Name is: "+END+str(User_CSV)
                    Mail_Send(Login_Details,User_CSV)
        

if __name__ =='__main__':
        main()
