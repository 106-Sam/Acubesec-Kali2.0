#!/usr/bin/python3

import os
from tqdm import tqdm
from time import sleep

# Constants
NUM_COPY_ITERATIONS = 20
NUM_SERVICE_START_ITERATIONS = 10

def copy_files(source_file):
    for _ in tqdm(range(NUM_COPY_ITERATIONS), colour="#00ffff", desc="Copying files: "):
        sleep(.1)
        cmd = f"sudo cp {source_file} /bin/acube-startapps"
        os.system(cmd)
        cmd = "sudo cp acubesec.service acubesec.timer /etc/systemd/system/"
        os.system(cmd)

def start_service():
    print("\nreloading daemon ...")
    cmd = "sudo systemctl daemon-reload"
    os.system(cmd)
    print("")
    for _ in tqdm(range(NUM_SERVICE_START_ITERATIONS), colour="#00ffff", desc="Starting Service: "):
        sleep(.1)
    cmd = "sudo systemctl disable acubesec.service"
    os.system(cmd)
    cmd = "sudo systemctl enable acubesec.timer"
    os.system(cmd)
    print("\nSuccessfully made changes! ✔ ✔ ✔")
    print("Dude ♜ ! restart your machine ...")

if __name__ == '__main__':
    ch = input("Are you using AcubeOS on VM?❥ [Y/N] : ").lower()

    if ch == 'y' or ch == 'yes':
        source_file = "acube-startapps"
    elif ch == 'n' or ch == 'no':
        source_file = "acube-startapps.blue"
    else:
        print("Please answer in Y=Yes and N=No")
        exit(1)

    copy_files(source_file)
    start_service()
 
