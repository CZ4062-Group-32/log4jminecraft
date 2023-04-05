#!/usr/bin/env python3

import json
import subprocess

if __name__ == "__main__":
    with open("config.json", "r") as f:
        config = json.load(f)

    print("**Installing netcat!**\n")
    subprocess.run(["sudo", "apt", "install", "netcat-traditional", "-y"])

    subprocess.run(["nc", "-lnvp", config["shell_port"]])
