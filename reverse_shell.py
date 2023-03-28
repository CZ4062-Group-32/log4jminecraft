#!/usr/bin/env python3

import subprocess

#1. Install netcat
print("**Installing netcat!**\n")
subprocess.run(["sudo", "apt", "install", "netcat-traditional", "-y"])

#2. Start netcat listener for reserver shell
subprocess.run(["nc", "-lnvp", "9898"])
