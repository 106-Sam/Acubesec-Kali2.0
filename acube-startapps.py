#!/usr/bin/python3 

import os
from tqdm import tqdm 
from time import sleep


def VM(ch):
    if ch == 'Y' or ch == 'Yes' or ch == 'yes':
        for i in tqdm(range(0,20), colour="#00ffff", desc="Copying files: "):
            sleep(.1)
            cmd = "sudo cp acube-startapps /tmp/acube-startapps"
            os.system(cmd)
            cmd = "sudo cp acubesec.service acubesec.timer /tmp/"
            os.system(cmd)

        print("")
        print("reloading daemon ...")
        cmd = "sudo systemctl daemon-reload"
        os.system(cmd)
        print("")
        for i in tqdm(range(0,10), colour="#00ffff", desc="Starting Service: "):
            sleep(.1)
        cmd = "sudo systemctl disable acubesec.service"
        os.system(cmd)
        cmd = "sudo systemctl enable acubesec.timer"
        os.system(cmd)
        print("")
        print("Successfully made changes ! ✔ ✔ ✔")
        print("Dude ♜  ! restart your machine ...")
            
    elif ch == 'N' or ch == 'No' or ch == 'no':
        for i in tqdm(range(0,20),colour="#00ffff", desc="Copying files: "):
            sleep(.1)
            cmd = "sudo cp acube-startapps.blue /tmp/acube-startapps"
            os.system(cmd)
            cmd = "sudo cp acubesec.service acubesec.timer /tmp/"
            os.system(cmd)

        print("")
        print("reloading daemon ...")
        cmd = "sudo systemctl daemon-reload"
        os.system(cmd)
        print("")
        for i in tqdm(range(0,10),colour="#00ffff", desc="Starting Service: "):
            sleep(.1)
        cmd = "sudo systemctl disable acubesec.service"
        os.system(cmd)
        cmd = "sudo systemctl enable acubesec.timer"
        os.system(cmd)
        print("")
        print("Successfully made changes! ✔ ✔ ✔")
        print("Dude ♜ ! restart your machine ...")

    else:
        print("Please answer in Y=Yes and N=No")


if __name__ == '__main__':
    ch = input("Are you using AcubeOS on VM?❥ [Y/N] : ")
    VM(ch)
