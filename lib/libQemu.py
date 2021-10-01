import sys
sys.path.append('.')
sys.path.append('lib/')

import urllib
import urllib.request
import subprocess
import admin
from os import path
import os
from time import sleep as delay

class Qemu():
    def run(self,name):
        name = path.relpath(name, os.getcwd())
        cmd = f'& "C:\Program Files\qemu\qemu-system-aarch64" -drive file={name},format=raw,if=sd,id=hd-root  -kernel lib/kernel/Kernel_Custom -M raspi3b -m 1024 -append "rw console=tty0 loglevel=8 root=/dev/mmcblk0p2 fsck.repair=yes net.ifnames=0 rootwait memtest=1 dwc_otg.lpm_enable=0 earlyprintk" -netdev user,id=net0,hostfwd=tcp::8080-:80 -no-reboot -usb -device usb-mouse -device usb-kbd -device usb-net,netdev=net0 -dtb lib/kernel/bcm2710-rpi-3-b.dtb '
        #print(cmd)
        p = subprocess.Popen(["powershell.exe", cmd], stdout=sys.stdout)
        p.communicate()
        delay(1)
        #p.communicate('\r\n')
        
    def checkDep(self):
        return path.exists(self.path)

    def install(self,handle=False):
        if not admin.isUserAdmin():
            admin.runAsAdmin()
        if handle:
            urllib.request.urlretrieve('https://qemu.weilnetz.de/w64/2021/qemu-w64-setup-20210810.exe' , 'com/qemu.exe',handle)
        else:
            urllib.request.urlretrieve('https://qemu.weilnetz.de/w64/2021/qemu-w64-setup-20210810.exe' , 'com/qemu.exe')
        p = subprocess.Popen('com/qemu.exe')
        p.wait()
        return self.checkDep()

    def __init__(self):
        self.path = "\Program Files\qemu" 
