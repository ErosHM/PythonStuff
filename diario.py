import os

def load(nombre):
	# todo: llenar desde archivo si existe
	return[]
	
def save(nombre,datos):
	filename=os.path.abspath(os.path.join('.','diarios',nombre+'.jrl'))
	print("guardando en: {}".format(filename))
	
	#fout=open(filename,'w')
	
	with open(filename,'w') as fout:
		for entrada in datos:
			fout.write(entrada+"\n")
		
	#fout.close() #no es necesario, al terminar el ciclo for automaticamente llama .close
	
 
 
def agregar_entrada(texto,datos):
	datos.append(texto)
