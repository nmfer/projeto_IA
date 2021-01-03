"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar



"""
import time
# Import necessário para calcular a distancia vectorial;
import math




def work(posicao, bateria, objetos):
    # esta função é invocada em cada ciclo de clock
    # e pode servir para armazenar informação recolhida pelo agente
    # recebe:
    # posicao = a posição atual do agente, uma lista [X,Y]
    # bateria = valor de energia na bateria, um número inteiro >= 0
    # objetos = o nome do(s) objeto(s) próximos do agente, uma string

    # podem achar o tempo atual usando, p.ex.
    # time.time()
		menu()
		list_people(objetos)
		
	#pass

#----------------------------------funções auxiliares---------------------------------------------------------------------------	
def Person(personName, personType):
	
	Persons = {
		"personName": personName,
		"personType": personType
	}
	
	def toString():
		return (str(Persons["personName"]) + str(Persons["personType"]))	


def list_people(objetos): #objetos -> lista
	 	
	if objetos is not None:
		for i in range(len(objetos)):
			if("medico" in objetos[i]) or ("doente" in objetos[i]) or ('enfermeiro' in objetos[i]):
				pessoaTemp ={
					"Nome": objetos[i]
				}	
				if "enfermeiro" in objetos[i]:
					pessoaTemp["Tipo"] = "Enfermeiro"
				elif "medico" in objetos[i]:
					pessoaTemp["Tipo"] = "Médico"
				elif "doente" in objetos[i]:
					pessoaTemp["Tipo"] = "Doente"
				else:
					pessoaTemp["Tipo"] = "Outro"
				 	
			
			#pergunta1
			Person(pessoaTemp["Nome"], pessoaTemp["Tipo"])
			print(Person)	
			
	pass
	
	
#---------------------------------- end funções auxiliares---------------------------------------------------------------------------	
		
def resp1():
	
	pass

def resp2():
	pass

def resp3():
	pass

def resp4():
	pass
	
def resp5():
    pass

def resp6():
    pass

def resp7():
    pass

def resp8():
    pass

def menu():
	i = int(input())
	if i == 1:
		resp1()
		
