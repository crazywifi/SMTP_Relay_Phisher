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
Recently, I am working on a Red Team activity, where I found SMTP open relay vulnerability. I used "SMTP-cli" tool to run the phishing campaign for the exploitation of open relay issue but the challenges were that I was not able to alter the First Name, Last Name and Email like we do by Kingphisher and other phishing toolkits. One more challenge was that Open relay issue was allowed to validate the user by 'RCPT TO', so  I gather the information from Linkedin and crate Email ids in <FirstName>.<LastName> pattern but didn't know any tool that automates this work. So by using the idea of Kingphisher and by using [smtp-cli](https://github.com/mludvig/smtp-cli), I develop this tool. Thanks, Kingphisher and SMTP-cli for developing such an awesome tool.
  
## Why Use SMTP Relay Phisher
* This tool doesn't work on the client-server model like other phishing toolkits. 
* This tool runs directly from the attacker machine. 
* This tool is lightweight and easy to use.
* This tool helps in a red team activity to run a phishing campaign by exploiting SMTP open relay.
* This tool helps to validate the user by **RCPT TO**.

