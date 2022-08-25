import os
import threading

def search(ip_address):
	# enviar ping
	command= "ping -c 4 " + ip_address + ' | grep "4 packets"' + " | awk '{print $4,$5}'"
	response= os.popen(command).read()
	info= [ip_address]
	if "4 received" in response:
		# extraer mac
		command_mac= "sudo nmap " + ip_address + ' | grep "MAC Address"' + " | awk '{print $3}'"
		response_mac= os.popen(command_mac).read()
		info.append(response_mac)
		# extraer marca
		command_device= "sudo nmap " + ip_address + ' | grep "MAC Address"' + " | awk '{print $4,$5,$6,$7,$8,$9}'"
		response_device= os.popen(command_device).read()
		info.append(response_device)
		# imprimir lista con info de ip´s activas
		print(info)

for ip in range (1,255):
	current_ip= "192.168.100." + str(ip) #range ip

	run=threading.Thread(target=search, args=(current_ip,))
	run.start()
