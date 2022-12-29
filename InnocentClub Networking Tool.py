import requests
import os
import colorama
import webbrowser
import random 
import string
import sys 
import time
import os
import requests
import getpass
import nmap
import socket
from cursor import hide, show
from colorama import Fore, Back, Style, init
init(autoreset=True)

username = getpass.getuser()

def get_ip_info(ip_address):
  api_key = "7cfe709c1417441cad1d10de68ee83c0" 
  api_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"
  response = requests.get(api_url)
  if response.status_code == 200:
    return response.json()
  else:
    return None

def pinger():
  while True:
    ip_address = input(Fore.WHITE + Style.BRIGHT + "Please enter the " + Fore.RED + Style.BRIGHT +  "IP address or hostname " + Fore.WHITE + Style.BRIGHT + "you want to ping: " + Fore.RED + Style.BRIGHT)
    command = f"ping -c 3 {ip_address}"  
    os.system(command)

    
    valid_choices = ["ping", "back"]
    choice = ""
    while choice not in valid_choices:
      choice = input(Fore.WHITE + Style.BRIGHT + "Do you want to keep pinging or" + Fore.RED + Style.BRIGHT + " go back" + Fore.WHITE + Style.BRIGHT + " to the main menu?" + Fore.WHITE + Style.BRIGHT + " Enter" + Fore.RED + Style.BRIGHT + ' ping' + Fore.WHITE + Style.BRIGHT + " or" + Fore.RED + Style.BRIGHT + ' back' + Fore.WHITE + Style.BRIGHT +": " + Fore.WHITE + Style.BRIGHT) 
    
   
    if choice == "back":
      break 

def port_scan(host, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(5)
  try:
    s.connect((host, port))
    return True
  except:
    return False

def iplogger():
 
  linkks = [
    ('https://iplogger.org/', colorama.Fore.RED + Style.BRIGHT + 'IP Logger'),
    ('https://grabify.link/', colorama.Fore.RED + Style.BRIGHT + 'Grabify'),
    ('https://www.blazeip.com/', colorama.Fore.RED + Style.BRIGHT + 'BlazeIP')
]

  for i, (linkk, label) in enumerate(linkks):
    print(Fore.WHITE + f"[{i}] {label}")
  print()
  selected = input(Fore.WHITE + Style.BRIGHT + "[>] Which" + Fore.RED + Style.BRIGHT + " Link" + Fore.WHITE + Style.BRIGHT + " u" + Fore.RED + Style.BRIGHT + " wanna" + Fore.WHITE + Style.BRIGHT + " open" + Fore.RED + Style.BRIGHT + "?")
  selected = int(selected)
  if selected <= 2 and selected < len(linkks):
    linkk = linkks[selected][0]
    webbrowser.open(linkk)
    input("Press Enter to close this window..." + Fore.RESET)
  else:
    input("Invalid Input G, Press Enter to go back" + Fore.RESET)  



def ddos():
  
  links = [
    ('https://icyaf.neocities.org/stresser.html', colorama.Fore.RED + Style.BRIGHT + 'NoName'),
    ('https://www.stressthem.to/', colorama.Fore.RED + Style.BRIGHT + 'Stressthem'),
    ('https://str3ssed.co/index.php', colorama.Fore.RED + Style.BRIGHT + 'Str3ssed'),
    ('https://hardstresser.com/', colorama.Fore.RED + Style.BRIGHT + 'Hard Stresser'),
    ('https://hkstresser.net/', colorama.Fore.RED + Style.BRIGHT + 'HK Stresser'),
    ('https://nightmarestresser.to/', colorama.Fore.RED + Style.BRIGHT + 'NightMare Stresser')
]

  for i, (link, label) in enumerate(links):
    print(Fore.WHITE + f"[{i}] {label}")
  print()
  selected = input(Fore.WHITE + Style.BRIGHT + "[>] Which" + Fore.RED + Style.BRIGHT + " Link" + Fore.WHITE + Style.BRIGHT + " u" + Fore.RED + Style.BRIGHT + " wanna" + Fore.WHITE + Style.BRIGHT + " open" + Fore.RED + Style.BRIGHT + "?")
  selected = int(selected)
  if selected <= 5 and selected < len(links):
    link = links[selected][0]
    webbrowser.open(link)
    input("Press Enter to close this window..." + Fore.RESET)
  else:
    input("Invalid Input G, Press Enter to go back" + Fore.RESET)   



 

def port_scanner():
  host = input('Enter the IP address or hostname to scan(it take some time): ')
  ports = [80, 443, 22, 21, 23, 25]  
  
  for port in ports:
    if port_scan(host, port):
      print(f'Port {port} is open')
    else:
      print(f'Port {port} is closed')

def ping(ip, port):
    response = input(f"Do you want to check if port {port} is open on {ip}? Enter yes or no: ")
    if response.lower() == "yes":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, port))
            print(f"Port {port} is open on {ip}")
        except:
            print(f"Port {port} is closed on {ip}")
        s.close()
    elif response.lower() == "no":
        print("Exiting Port Pinger")
    else:
        print("Invalid response. Exiting Port Pinger") 

def gen():
    upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letter = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    special_characters = '!@#$%^&*()'
    characters = upper_letter + lower_letter + digits + special_characters
    password = ''

    while True:
        password = ''
        for i in range(8):
            password += random.choice(characters)
        print(f"Your Password is: {password}")
        break



print(Style.BRIGHT + Fore.WHITE + "╔═════════════════════════════════════════════════════════════════════════" + Style.BRIGHT + Fore.RED +"════════════════════════════════════════════╗")
print(Style.BRIGHT + Fore.WHITE + "║                                                                          " + Style.BRIGHT + Fore.RED +"                                           ║")
print(Style.BRIGHT + Fore.WHITE + "║" + Style.BRIGHT + Fore.RED +"    ___   __    _  __    _  _______  _______  _______  __    _  _______"  + Style.BRIGHT + Fore.WHITE +"        _______  ___      __   __  _______  " + Style.BRIGHT + Fore.RED +"  ║")
print(Style.BRIGHT + Fore.WHITE + "║" + Style.BRIGHT + Fore.RED +"   |   | |   |_| ||   |_| ||   _   ||       ||    ___||   |_| ||_     _|"  + Style.BRIGHT + Fore.WHITE +"      |       ||   |    |  | |  || |_|   |  " + Style.BRIGHT + Fore.RED +" ║")
print(Style.BRIGHT + Fore.WHITE + "║" + Style.BRIGHT + Fore.RED +"   |   | |       ||       ||  | |  ||       ||   |___||   |   |  |   |"  + Style.BRIGHT + Fore.WHITE +"        |       ||   |    |  |_|  ||       |  " + Style.BRIGHT + Fore.RED +" ║")
print(Style.BRIGHT + Fore.WHITE + "║" + Style.BRIGHT + Fore.RED +"   |   | |  _    ||  _    ||  |_|  ||      _||    ___||  _    |  |   |"  + Style.BRIGHT + Fore.WHITE +"   ___  |      _||   |___ |       ||  _   |   " + Style.BRIGHT + Fore.RED +" ║") 
print(Style.BRIGHT + Fore.WHITE + "║" + Style.BRIGHT + Fore.RED +"   |   | | | |   || | |   ||       ||     |_ |   |___ | | |   |  |   |"  + Style.BRIGHT + Fore.WHITE +"  |   | |     |_ |       ||       || |_|   |  " + Style.BRIGHT + Fore.RED +" ║")
print(Style.BRIGHT + Fore.WHITE + "║" + Style.BRIGHT + Fore.RED +"   |___| |_|  |__||_|  |__||_______||_______||_______||_|  |__|  |___|"  + Style.BRIGHT + Fore.WHITE +"  |___| |_______||_______||_______||_______|  " + Style.BRIGHT + Fore.RED +" ║")
print(Style.BRIGHT + Fore.WHITE + "║                                                                          " + Style.BRIGHT + Fore.RED +"                                           ║")
print(Style.BRIGHT + Fore.WHITE + "╚═════════════════════════════════════════════════════════════════════════" + Style.BRIGHT + Fore.RED +"════════════════════════════════════════════╝")

while True:
  time.sleep(0.5)
  print(f"""\n                ╔═════════════════════════════════════════════════════════════════════════════════════╗
                ║{Back.WHITE + Style.BRIGHT} {Fore.RESET + Back.RESET + Fore.RED } Welcome {username} {Back.WHITE + Style.BRIGHT} {Fore.RESET + Back.RESET}                                                     {Back.WHITE + Style.BRIGHT} {Fore.RESET + Back.RESET + Fore.RED } MAIN SCREEN {Back.WHITE + Style.BRIGHT} {Fore.RESET + Back.RESET}║
                ╠═════════════════════════════════════════════════════════════════════════════════════╣
                ║{Fore.RED + Style.BRIGHT}[01]{Fore.RESET} IP Lookup                          ║ {Fore.RED}[06]{Fore.RESET + Style.BRIGHT} IP Port Pinger                        ║
                ║{Fore.RED}[02]{Fore.RESET + Style.BRIGHT} Pinger                             ║ {Fore.RED}[07]{Fore.RESET + Style.BRIGHT} Discord Nitro Generator               ║
                ║{Fore.RED}[03]{Fore.RESET + Style.BRIGHT} DDOS Tools                         ║ {Fore.RED}[08]{Fore.RESET + Style.BRIGHT} PW Gen                                ║
                ║{Fore.RED}[04]{Fore.RESET + Style.BRIGHT} IP Port Scanner                    ║ {Fore.RED}[09]{Fore.RESET + Style.BRIGHT} Read Me                               ║
                ║{Fore.RED}[05]{Fore.RESET + Style.BRIGHT} IP Logger                          ║ {Fore.RED}[10]{Fore.RESET + Style.BRIGHT} Quit                                  ║
                ╠═════════════════════════════════════════════════════════════════════════════════════╣
                ║{Back.WHITE + Style.BRIGHT} {Fore.RESET + Back.RESET + Fore.RED } author: kuhxrt#5485 {Back.WHITE + Style.BRIGHT} {Fore.RESET + Back.RESET}                             {Back.WHITE + Style.BRIGHT} {Fore.RESET + Back.RESET + Fore.RED } https://discord.gg/FQEa5wmu7e {Back.WHITE + Style.BRIGHT} {Fore.RESET + Back.RESET}║
                ╚═════════════════════════════════════════════════════════════════════════════════════╝

""")
  choice = input(Fore.RED + Style.BRIGHT + "Enter" + Fore.WHITE + Style.BRIGHT + " your" + Fore.RED + Style.BRIGHT + " choice" + Fore.WHITE + Style.BRIGHT + ":" + Style.RESET_ALL)

  if choice == "01":
    ip_address = input(Fore.WHITE + Style.BRIGHT + "Enter the" + Fore.RED + Style.BRIGHT + " IP address" + Fore.WHITE +  Style.BRIGHT + " you want to get" + Fore.RED + Style.BRIGHT + " information about" + Fore.WHITE + Style.BRIGHT + ":" + Fore.RED + Style.BRIGHT)
    ip_info = get_ip_info(ip_address)
    if ip_info:
      print(Fore.WHITE + Style.BRIGHT + "IP Address: " + Fore.RED + Style.BRIGHT + ip_info["ip"])
      print(Fore.WHITE + Style.BRIGHT + "City: " + Fore.RED + Style.BRIGHT + ip_info["city"])
      print(Fore.WHITE + Style.BRIGHT + "Country: " + Fore.RED + Style.BRIGHT + ip_info["country_name"])
      print(Fore.WHITE + Style.BRIGHT + "ISP: " + Fore.RED + Style.BRIGHT + ip_info["isp"])
      print(Fore.WHITE + Style.BRIGHT + "Organization: " + Fore.RED + Style.BRIGHT + ip_info["organization"])
      print(Fore.WHITE + Style.BRIGHT + "Google Maps Location: " + Fore.RED + Style.BRIGHT + ip_info["latitude"], ip_info["longitude"])
      print(Fore.WHITE + Style.BRIGHT + "Calling Code: " + Fore.RED + Style.BRIGHT + ip_info["calling_code"])
      print(Fore.WHITE + Style.BRIGHT + "Postal Code: " + Fore.RED + Style.BRIGHT + ip_info.get("zipcode", "N/A"))
    else:
      print(Fore.RED + Style.BRIGHT + "Error getting IP information. Please check your input and try again.")
  
  if choice == "02":
    pinger()
  
  
  
    
  
  elif choice == "04":
    port_scanner()



  elif choice == "05":
   iplogger()
  
  elif choice == "06":
   ping()
  
  elif choice == "07":
   gen()
  
  elif choice == "08":
    password_length = int(input(Fore.WHITE + Style.BRIGHT + "Enter the desired" + Fore.RED + Style.BRIGHT + " length" + Fore.WHITE + Style.BRIGHT + " of the" + Fore.RED + Style.BRIGHT + " password" + Fore.WHITE + Style.BRIGHT + ": " + Fore.RED + Style.BRIGHT ))
    password = "".join(random.choices(string.ascii_letters + string.digits, k=password_length))
    print(Fore.RED + Style.BRIGHT + "Generated password: " + Fore.WHITE + Style.BRIGHT + password)
  
  
  elif choice == "09":
   print(Fore.RED + Style.BRIGHT + "╔═════════════════════════════════════════════════════════════════════════════════════╗")
   print(Fore.RED + Style.BRIGHT + "║ " + Fore.WHITE + Style.BRIGHT + " This Tool is written in python and its the first tool I made!" + Fore.RED + Style.BRIGHT + "                      ║ " )
   print(Fore.RED + Style.BRIGHT + "║ " + Fore.WHITE + Style.BRIGHT + " This Tool is not finished yet, I just released it too see how many people like it." + Fore.RED + Style.BRIGHT + " ║ " )
   print(Fore.RED + Style.BRIGHT + "║ " + Fore.WHITE + Style.BRIGHT + " I will update it every second day, and ofc it will get better." + Fore.RED + Style.BRIGHT + "                     ║ " )
   print(Fore.RED + Style.BRIGHT + "║ " + Fore.WHITE + Style.BRIGHT + " If u have any wishes like what I should add," + Fore.RED + Style.BRIGHT +  " feel free to join my discord server!" + Fore.RED + Style.BRIGHT + "  ║ " )
   print(Fore.RED + Style.BRIGHT + "╚═════════════════════════════════════════════════════════════════════════════════════╝") 
   Style.RESET_ALL
   time.sleep(0.5)

  elif choice == "10":
    print(Fore.RED + Style.BRIGHT + "Exiting program. Goodbye!")
    sys.exit()
  
  elif choice == "03":
   ddos()
  
  
  


 