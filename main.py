import os
import threading


def contar(ip_address, **datos):
	contador = datos['inicio']
	incremento = datos['incremento']
	limite = datos['limite']
	while contador<=limite:

		command= "ping -c 4 " + ip_address + ' | grep "4 packets"' + " | awk '{print $4,$5}'"
		response= os.popen(command).read()
		info= [ip_address]
		if "4 received" in response:
			# extraer mac
			command_mac= "nmap " + ip_address + ' | grep "MAC Address"' + " | awk '{print $3}'"
			response_mac= os.popen(command_mac).read()
			info.append(response_mac)
			# extraer marca
			command_device= "nmap " + ip_address + ' | grep "MAC Address"' + " | awk '{print $4,$5,$6,$7,$8,$9}'"
			response_device= os.popen(command_device).read()
			info.append(response_device)
			# imprimir lista con info de ip´s activas
			print(info)

		contador+=incremento

for ip in range(1,255):
	current_ip= "10.0.2." + str(ip) #range ip

	hilo = threading.Thread(target=contar,
							args=(current_ip,),
							kwargs={'inicio':1,
									'incremento':1,
									'limite':1})
	hilo.start()
