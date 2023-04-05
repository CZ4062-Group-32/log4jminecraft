# log4jminecraft

This code *DOES NOT* promote or encourage any illegal activities!
The content in this document is provided solely for educational purposes and to create awareness!

Watch a video showing the process here: https://youtu.be/efnluUK_w_U

This PDF shows you how to setup a Minecraft server for this demonstration: https://davidbombal.wiki/minecraftw11log4j

* https://sourceforge.net/projects/portableapps/files/JDK/jdk-8u181-windows-x64.exe is an alternative link to the JDK on
  the PDF.
* Use https://launcher.mojang.com/v1/objects/5fafba3f58c40dc51b5c3ca72a98f62dfdae1db7/server.jar which is a vanilla
  Minecraft server if PaperMC throws errors.
* Link to download Windows 11 ISO: https://www.microsoft.com/software-download/windows11
* Link to download VMware Workstation: https://www.vmware.com/go/getworkstation-win
* Link to Kali Linux WSL: https://www.kali.org/docs/wsl/win-kex/

Pre-requisite:

* Install Minecraft Client 1.8.8 on another machine to run the command.
* ```sudo apt install git -y``` - Git is required to clone this repository.
* ```sudo apt install python3 -y``` - Python3 is required to run the scripts.

To run this project follow the following steps:

1. Clone the repository:
   ```git clone https://github.com/CZ4062-Group-32/log4jminecraft.git```
2. Run the script log4j.py (```python3 log4j.py```). This installs the prerequisite software, and also starts up the
   LDAP server.
3. Run the script jcomp_pyserv.py (```python3 jcomp_pyserv.py```). This modifies and compiles the Java payload to be
   run, creates the shell code, and also
   starts a python3 http.server.
4. Run the script reverse_shell.py (```python3 reverse_shell.py```). This starts the netcat listener for reverse shell.
5. Type the commands from the output of log4j.py. This will launch the attack, and the reverse shell will be spawned on
   the netcat listener.

# Useful items

* Decodes base64 PowerShell
  format - https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)Decode_text('UTF-16LE%20(1200)')
* ```cd log4jminecraft``` - Change directory to the GitHub repository root folder.

# Acknowledgement for contributions:

* John Hammond : https://youtu.be/7qoPDq41xhQ
* Moritz Bechler (For creating the Java Unmarshaller Security - MarshalSec) : https://github.com/mbechler/marshalsec
* xiajun325 for clear instruction on how to use the MarshalSec tool : https://github.com/xiajun325/apache-log4j-rce-poc
* David Bombal for the orignal fork of this repo : https://github.com/davidbombal/log4jminecraft
* Nol White Hat for guide on how to use
  powercat : https://systemweakness.com/evade-windows-defender-reverse-shell-detection-6fa9f5eee1d1
* besimorhino for powercat : https://github.com/besimorhino/powercat
