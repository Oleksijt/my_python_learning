# import os
# import re
import time
# import sys
import telnetlib
# from threading import Thread


def router_reboot(HOST, user, password):
    tn = telnetlib.Telnet(HOST)
    tn.read_until('BCM96348 ADSL Router'.encode())
    tn.read_until('Login:'.encode())
    tn.write(user + "\n")
    tn.read_until('Password: '.encode())
    tn.write(password + "\n")
    time.sleep(5)
    # tn.write(«ifconfig ppp_0_1_32_1\n»)
    tn.write('reboot\n')
    time.sleep(5)
    tn.write('logout\n')
    time.sleep(60)


ip = '8.8.8.8'
HOST = '192.168.1.1'
user = 'admin'.encode('utf8')
password = 'W7TyhF7C3GxkJJj'



router_reboot(HOST, user, password)