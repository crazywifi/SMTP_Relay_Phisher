# SMTP_Relay_Phisher

## Overview
SMTP Relay Phisher is a tool for testing and exploiting the **SMTP Open Relay** vulnerability by simulating real-world phishing attacks. 
This tool used for two purposes:

1. To run the phishing campaign by command line 
2. To exploit the SMTP Open Relay vulnerability by sending phishing email

This tool used custom SMTP-cli. I have done some basic modifications in his script.
Thanks to [smtp-cli](https://github.com/mludvig/smtp-cli) for developing such a useful tool.

## Feature Overview
* Fully open-source means there's no limits on the use
* Lightweight as compare to other phishing toolkits
* Run multiple phishing campaigns simultaneously
* Send an email with embedded First Name, Last Name, and Email
* Highly flexible to run phishing campaign by exploiting SMTP open relay issue
* User enumeration by "RCPT TO"
* Time delay is available to bypass the open relay restriction

## Reason to Develop SMTP Relay Phisher
Recently, I am working on a Red Team activity, where I found SMTP open relay vulnerability. I used "SMTP-cli" tool to run the phishing campaign for the exploitation of open relay issue but the challenges were that I was not able to alter the First Name, Last Name and Email like we do by Kingphisher and other phishing toolkits. One more challenge was that the Open relay issue was allowed to verify the user by 'RCPT TO'.So, I gather the information from Linkedin and create Email ids in FirstName.LastName pattern but didn't know any working tool that automates email verification by RCPT TO. So by using the idea of Kingphisher and by using [smtp-cli](https://github.com/mludvig/smtp-cli), I develop this tool. Thanks, Kingphisher and SMTP-cli for developing such an awesome tool.
  
## Why Use SMTP Relay Phisher
* This tool doesn't work on the client-server model like other phishing toolkits. 
* This tool runs directly from the attacker machine. 
* This tool is lightweight and easy to use.
* This tool helps in a red team activity to run a phishing campaign by exploiting SMTP open relay.
* This tool helps to validate the user by **RCPT TO**.

## Note
SMTP Relay Phisher is only to be used for legal applications when the explicit permission of the targeted organization has been obtained.

## Installation
Download the latest release from SMTP_Relay_Phisher on GitHub:
```
git clone https://github.com/crazywifi/SMTP_Relay_Phisher.git
chmod +x custom-smtp-cli
chmod +x SMTP_Relay_Phisher.py
```
### Dependencies
```
pip install -r requirements.txt
sudo apt install  libio-socket-ssl-perl  libdigest-hmac-perl  libterm-readkey-perl \
                      libmime-lite-perl libfile-libmagic-perl libio-socket-inet6-perl
cpan -i Net::DNS
```
## Screenshots
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/1.PNG)
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/2.PNG)
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/3.PNG)
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/10.PNG)
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/4.PNG)
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/5.PNG)
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/11.PNG)
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/6.PNG)
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/7.PNG)
![Alt text](https://raw.githubusercontent.com/crazywifi/SMTP_Relay_Phisher/master/poc/9.png)
