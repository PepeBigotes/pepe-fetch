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
# See https://pypi.org/project/colored/ for more details
class color:
   c0 = colored.fg('#FFFFFF')
   c_welcome = colored.fg('#00FF00')
   c_underline = c0
   c_info = colored.fg('#B6FFB6')
   c_ascii = colored.fg('#00FF00')
   
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

# Horizontal margins
left_margin = " "
middle_margin = "   "
right_margin = " "

#Vertical margins
top_margin = 1
bottom_margin = 1

#Ascii art color/format
ascii_color = f"{color.bold}{color.c_ascii}"