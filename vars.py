#!/usr/bin/env python3                         
#   _   ______ ___________
#  | | / / __ `/ ___/ ___/
#  | |/ / /_/ / /  (__  ) 
#  |___/\__,_/_/  /____/  
#                        
#DON'T CHANGE THIS SCRIPT UNLESS YOU KNOW WHAT YOU ARE DOING!
#Customization options are at 'config.py' and 'infos.py'

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

#Info Function
def info(text = "", info = "" , suffix = default_suffix):
   if not text or not info:
      suffix = ""

   print(text + suffix + info)