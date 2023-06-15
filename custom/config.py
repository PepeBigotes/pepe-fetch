#!/usr/bin/env python3
#                      _____      
#    _________  ____  / __(_)___ _
#   / ___/ __ \/ __ \/ /_/ / __ `/
#  / /__/ /_/ / / / / __/ / /_/ / 
#  \___/\____/_/ /_/_/ /_/\__, /  
#                        /____/   
#
#Customize your options here
#If you want to modify the actual prints, check 'infos.py'

#Color Class
# See https://pypi.org/project/colored/ for more info
class color:
   c0 = colored.fg('#FFFFFF')
   c1 = colored.fg('#A0FFA0')
   c2 = colored.fg('#A9DFA9')
   
   bold = colored.attr("bold") #Leave this one alone
   reset = colored.attr("reset") #Leave this one alone


#Ascii text path
ascii_path = "./asciis/pepefetch.txt"


#Username
username = None #Default is your system's login
#Hostname
hostname = None #Default is your system's hostname


#Welcome Parts (useless if 'welcome' is not None)
welcome_p = None #Default is [username, "@", hostname]

#Welcome
welcome = None #Default is 'welcome_p' colored


# Underline
underline_symbol = "="
# Suffix
default_suffix = ": "