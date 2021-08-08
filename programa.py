import diario

def main():
	print_header()
	run_event_loop()

def print_header():
	print('--------------------------------')
	print('            Diario')
	print('--------------------------------')
	
def run_event_loop():
	print("¿Que quieres hacer con tu diario?")
	cmd=None
	nombre_diario="default"
	datosDiario=diario.load(nombre_diario) #list()
	
	while cmd!="s":
		cmd=input("[L]ista de entradas, [A]gregar una entrada, [S]alir: ")
		cmd=cmd.lower().strip()
		
		if cmd=="l":
			lista_de_entradas(datosDiario)
		elif cmd=="a":
			agregar_entrada(datosDiario)
		elif cmd!="s":
			print("No entiendo '{}'.".format(cmd))
			
	print("Proceso terminado, adiosito")
	diario.save(nombre_diario,datosDiario)
	
def lista_de_entradas(datos):
	print("Entradas del diario")
	entradas=reversed(datos)
	for index, entrada in enumerate(entradas):
		print("* [{}] {}".format(index+1, entrada))

def agregar_entrada(datos):
	print("Agregando...")
	texto=input("Escribe tu entrada, <enter> para salir: ")
	diario.agregar_entrada(texto,datos)
	#datos.append(texto)
	
	
main()
