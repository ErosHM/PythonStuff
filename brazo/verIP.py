import socket
nombre_equipo = socket.gethostname()
print("El nombre del equipo es: %s" %nombre_equipo)
direccion_equipo = socket.gethostbyname(nombre_equipo)
print ("La IP es: %s" %direccion_equipo)
