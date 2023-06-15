#!/usr/bin/env python3
#      _       ____          
#     (_)___  / __/___  _____
#    / / __ \/ /_/ __ \/ ___/
#   / / / / / __/ /_/ (__  ) 
#  /_/_/ /_/_/  \____/____/  
#                            
#Customize your prints here
#If you want to modify the actual variables/options, check 'config.py'

info(welcome)
info(underline)

info("Host", hostname)
info("Uptime" , uptime)
info("Time" , time_hm)
info("Date" , date_dmy)
#info("Battery", percent + '%' + plugged)
info("Disk" ,  f"{disk.used_gib}/{disk.total_gib} GiB ({disk.used_percert}%)")
info("Local IP" , local_ip)
#info("Public IP" , public_ip)



print_infos()