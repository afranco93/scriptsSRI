contadorIP = 10
with open('IP_Fijas_19102022_c.txt','r') as f:
    for host_name in f:
        host_name_replace = host_name.replace("----------",";")
        datos_host = host_name_replace.split(";")
        print("Host",datos_host[0],"{")
        print("\t # Asignacion estatica")
        print("\t hardware ethernet",datos_host[1],"; # Direccion MAC del host")
        print('\t fixed-address 192.168.100.%d'%contadorIP,"; # IP asignada al host")
        print("}")
        contadorIP = contadorIP+1