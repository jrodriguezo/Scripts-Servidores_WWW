import subprocess

#1 instalacion 
subprocess.call("sudo apt-get install apache2",shell=True)
subprocess.call("sudo apt-get install lynx",shell=True)
subprocess.call("sudo apt-get install wget",shell=True)
subprocess.call("sudo apt-get install curl",shell=True)

#2
fin = open("/etc/network/interfaces", 'r') 
fout = open("/etc/network/interfaces_Edited", 'w') 
for line in fin:
	if "source /etc/network/interfaces.d/*.cfg" in line :
   		fout.write("auto eth0\n")
   		fout.write("iface eth0 inet static\n")
   		fout.write("address 192.168.122.241\n")
   		fout.write("netmask 255.255.255.0\n")
   		fout.write("gateway 192.168.122.1\n")
   		fout.write("dns-nameservers 192.168.122.1\n")
	else:
		fout.write(line)


fin.close()
fout.close()

subprocess.call(['cp','/etc/network/interfaces_Edited','/etc/network/interfaces'])

#3
subprocess.call(['sudo','reboot'])



print("Completed")




