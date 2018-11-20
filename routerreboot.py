import os
import re
import time
import sys
import telnetlib
from threading import Thread


class testit(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip
        self.status = -1

    def run(self):
        pingaling = os.popen('ping - q - c2 '+self.ip,'r')
        while 1:
            line = pingaling.readline()
            if not line: break
            igot = re.findall(testit.lifeline, line)
            if igot:
                self.status = int(igot[0])
                if self.status == 0:
                    tn = telnetlib.Telnet(HOST)
                    tn.read_until('BCM96348 ADSL Router')
                    tn.read_until('Login:')
                    tn.write(user + "\n")
                    tn.read_until('Password: ')
                    tn.write(password + "\n")
                    time.sleep(5)
                    # tn.write(«ifconfig ppp_0_1_32_1\n»)
                    tn.write('reboot\n')
                    time.sleep(5)
                    tn.write('logout\n')
                    time.sleep(60)


testit.lifeline = re.compile(r"(\d) received")

ip = '8.8.8.8'
HOST = '192.168.1.1'
user = 'admin'
password = 'W7TyhF7C3GxkJJj'

current = testit(ip)
current.start()