import subprocess

subprocess.call("cd /mnt/tmp",shell=True)
subprocess.call("mkdir p2",shell=True)
subprocess.call("cd p2", shell=True)

subprocess.call("cp /mnt/vnx/repo/cdps/cdps-vm-base-p3.qcow2.bz2 .",shell=True)
subprocess.call("bunzip2 cdps-vm-base-p3.qcow2.bz2",shell=True)

subprocess.call("HOME=/mnt/tmp sudo virt-manager",shell=True)

