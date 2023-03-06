import sys

# Declaramos los datos que tenemos que ingresar en forma de variables
# Varaible para introducir la IP
ip = sys.argv[1]
# Variable para introducir la MAC
mac = sys.argv[2]

# Preguntamos si la IP esta completa, en caso de que no, nos dira que
# que esta incompleta. Hacemos lo mismo para la MAC.

if(len(sys.argv[1]) != 15):
	print ("La direccion IP esta incompleta")
if(len(sys.argv[2]) != 17):
	print ("La direccion MAC esta incompleta")

file=open("nodos_seguros.dat","w")
file.write(str(+ip";"+mac\n))
