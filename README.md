# log4jminecraft
This code *DOES NOT* promote or encourage any illegal activities!
The content in this document is provided solely for educational purposes and to create awareness!

Watch a video showing the process here: https://youtu.be/efnluUK_w_U

This PDF shows you how to setup a Minecraft server for this demonstration: https://davidbombal.wiki/minecraftw11log4j
* https://sourceforge.net/projects/portableapps/files/JDK/jdk-8u181-windows-x64.exe is an alternative link to the JDK on the PDF.
* Use https://launcher.mojang.com/v1/objects/5fafba3f58c40dc51b5c3ca72a98f62dfdae1db7/server.jar which is a vanilla Minecraft server if PaperMC throws errors.
* Link to download Windows 11 ISO: https://www.microsoft.com/software-download/windows11
* Link to download VMware Workstation: https://www.vmware.com/go/getworkstation-win
* Link to Kali Linux WSL: https://www.kali.org/docs/wsl/win-kex/

Pre-requisite:
* Ensure that Real-time protection is switched off on the Windows Minecraft server machine.
* Install Minecraft Client 1.8.8 on another machine to run the command.
* ```sudo apt install git -y``` - Git is required to clone this repository.
* ```sudo apt install python3 -y``` - Python3 is required to run the scripts.

To run this project follow the following steps:
1. Clone the repository: 
```git clone https://github.com/CZ4062-Group-32/log4jminecraft.git```
2. Run the script log4j.py (```python3 log4j.py```). This installs the prerequisite software, and also starts up the LDAP server.
3. Run the script jcomp_pyserv.py (```python3 jcomp_pyserv.py```). This compiles the Java payload to be ran, and also starts a python3 http.server. 
4. Run the script reverse_shell.py (```python3 reverse_shell.py```). This starts the netcat listener for reverse shell.
5. Type the commands from the output of log4j.py. This will launch the attack, and the reverse shell will be spawned on the netcat listener.

# Useful commands
* ```ip a s eth0``` - Check IP address of linux machine.
* https://amsi.fail/ - Link to generate obfuscated PowerShell snippets that break or disable AMSI for the current process.
* https://gist.github.com/TanJunHong/09c8ac11802daafdddf29a4a2d60a8ec - PowerShell reverse shell one-liner (Remember to change IP address).
* https://gchq.github.io/CyberChef/#recipe=Encode_text('UTF-16LE%20(1200)')To_Base64('A-Za-z0-9%2B/%3D') - Encodes text to base64 PowerShell format.
* ```powershell.exe -exec bypass -enc``` - Execute encoded powershell.
* ```cd log4jminecraft``` - Change directory to the GitHub repository root folder.



# Acknowledgement for contributions: 
* John Hammond : https://youtu.be/7qoPDq41xhQ
* Moritz Bechler (For creating the Java Unmarshaller Security - MarshalSec) : https://github.com/mbechler/marshalsec
* xiajun325 for clear instruction on how to use the MarshalSec tool : https://github.com/xiajun325/apache-log4j-rce-poc
* David Bombal for the orignal fork of this repo : https://github.com/davidbombal/log4jminecraft
* egre55 for the PowerShell one liner : https://gist.github.com/egre55/c058744a4240af6515eb32b2d33fbed3
