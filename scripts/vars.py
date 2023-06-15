#!/usr/bin/env python3                         
#   _   ______ ___________
#  | | / / __ `/ ___/ ___/
#  | |/ / /_/ / /  (__  ) 
#  |___/\__,_/_/  /____/  
#                        
#DON'T CHANGE THIS SCRIPT UNLESS YOU KNOW WHAT YOU ARE DOING!
#Customization options are in the 'custom' folder

#Terminal size
rows, columns = os.popen('stty size', 'r').read().split()

#Username
if not username:
   username = os.getlogin()
#Hostname
if not hostname:
   hostname = socket.gethostname()

#Time
time_hm = time.strftime("%H:%M") #hour/minute

#Date
datetimenow = datetime.datetime.now()
date_dmy = datetimenow.strftime("%d/%m/%y") #day/month/year

#Uptime
uptime_secs = time.time() - psutil.boot_time()
uptime = str(datetime.timedelta(seconds=uptime_secs)) #Formated uptime: day, hh:mm:ss

#Battery
battery = psutil.sensors_battery()
if battery: #Device has battery sensors (laptop, phone, ...)
   percent = str(int(battery.percent))
   plugged = " (Charging...)" if battery.power_plugged else ""
else: #Device does NOT have battery sensors (desktop PC)
   percent = "100"
   plugged = " (Plugged)"

#IPs
local_ip = socket.gethostbyname(socket.gethostname())
public_ip = requests.get('https://ident.me/').content.decode('utf8')

#Disk Class
class disk:
   total, used, free = shutil.disk_usage("/")
   total_gib = total // (2**30)
   used_gib = used // (2**30)
   free_gib = free // (2**30)
   used_percert = round((used_gib / total_gib) * 100)
   free_percert = round((free_gib / total_gib) * 100)

#Welcome
if not welcome_p:
   welcome_p = [username, "@", hostname]

if not welcome:
   welcome = ""
   welcome += color.bold + color.c1 + welcome_p[0] + color.reset
   welcome += color.bold + color.c0 + welcome_p[1] + color.reset
   welcome += color.bold + color.c2 + welcome_p[2] + color.reset

welcome_sum = "".join(map(str, welcome_p))
welcome_len = len(welcome_sum)

#Underline
underline = underline_symbol * welcome_len

#Read ascii art
ascii_file = open(ascii_path, "r")
data = ascii_file.read()
  
ascii_lines = data.split("\n")
ascii_file.close()


info_lines = []

#Info Function
def info(text = "", info = "" , suffix = default_suffix):
   if not text or not info:
      suffix = ""
   info_lines.append(text + suffix + info)


#Print Infos Function
def print_infos():
   if len(ascii_lines) >= len(info_lines): numof_lines = len(ascii_lines)
   if len(ascii_lines) <= len(info_lines): numof_lines = len(info_lines)
   
   for line in ascii_lines:
      ascii_len = len(line)
      break
   
   for i in range(0, numof_lines):
      try: ascii_line = ascii_lines[i] 
      except: ascii_line = " " * ascii_len
      try: info_line = info_lines[i] 
      except: info_line = ""
      print(f"{ascii_line}  {info_line}")