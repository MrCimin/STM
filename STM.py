#Search Page Admin Login
#python/python3

#Import Module

import os, sys
import requests
import termcolor
os.system('pip install --upgrade pip')
os.system('pip install requests')
os.system('pip install termcolor')
from termcolor import colored

#Banner

os.system('clear')
baner="""

 _____ ________  ___  
/  ___|_   _|  \/  |  | Author    : MR.C1M1N
\ `--.  | | | .  . |  | Facebook  : Davit_ex
 `--. \ | | | |\/| |  | Instagram : Davit_abdi
/\__/ / | | | |  | |  | Github    : https://github.com/MrCimin
\____/  \_/ \_|  |_/  | Program   : python/python3"""

#Coloring And Script System

print(colored(baner,'blue'))

print()
print()
print(colored('='*30,'yellow'))
print()
link=str(input(colored('Masukan Website: ','magenta')))
print()
print(colored('='*30,'yellow'))
list_page=open('word.txt','r')
page_list=list_page.readlines()
list_page.close()

for page in page_list:
  admin=page.strip()
  adminn='/'+admin
  URL=link+adminn
  
  x=requests.get(URL)
  if x.status_code == 200:
    print(colored('_'*70,'green'))
    print()
    print(colored('Found: '+URL,'green'))
    print(colored('_'*70,'green'))
    break
  else:
    print(colored('Not Found: '+URL,'red'))
