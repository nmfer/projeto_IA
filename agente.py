"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
39392, Joana Elias Almeida
39341, Nuno Miguel da Silva Coelho Fernandes

"""
import time
import math

sala_atual = ''

X_ant = 0

Y_ant = 0

#Lista com todos as Salas Visitadas e o qual é o seu tipo de sala (Sala, Tipo de Sala)
Tipos_Sala = [] 

#Lista de obejtos e a sala onde forma encontrados (Nome Objeto, Sala onde foi visto)
Objetos_Vistos = []

#Lista de Medicos encontrados e as suas coordenadas (Nome do Medico, X, Y)
Medicos_Vistos = []

#Lista de Pessoas encontradas e as salas onde as mesmas foram encontradas (Pessoa, Sala)
Pessoas_Encontradas = []

#Lista com todas as divisões encontradas
Divisoes_Encontradas = []

a = time.time()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def work(posicao, bateria, objetos):
    # esta função é invocada em cada ciclo de clock
    # e pode servir para armazenar informação recolhida pelo agente
    # recebe:
    # posicao = a posição atual do agente, uma lista [X,Y]
    # bateria = valor de energia na bateria, um número inteiro >= 0
    # objetos = o nome do(s) objeto(s) próximos do agente, uma lista

    # podem achar o tempo atual usando, p.ex.
    # time.time()
    
	global X, Y, X_ant, Y_ant, objeto, objetos_sala, sala_atual, lista_objetos, bat, b
	
	#X e Y atuais :
	X = posicao[0]
	Y = posicao[1]
			
	objeto = objetos
	
	objetos_sala = []
	
	lista_objetos = []
	
	bat = bateria
	
	#tempo atual
	b = time.time()
	
	#Quando o agente se está a mover, verificar as salas e os objetos dentro das mesmas
	if (X != X_ant) or (Y != Y_ant):

		#Cada Sala/Corredor é atribuida pelas cordenadas
		if (85 <= X and X <= 565) and (30 <= Y and Y <= 135):
			sala_atual = 'Corredor 1'
		elif (30 <= X and X <= 85) and (90 <= Y and Y <= 330):
			sala_atual = 'Corredor 2'
		elif (565 <= X and X <= 635) and (30 <= Y and Y <= 330):
			sala_atual = 'Corredor 3'
		elif (30 <= X and X <= 770) and (330 <= Y and Y <= 410):
			sala_atual = 'Corredor 4'	
		elif (130 <= X and X <= 235) and (180 <= Y and Y <= 285):
			sala_atual = 'Sala 5'
		elif (280 <= X and X <= 385) and (180 <= Y and Y <= 285):
			sala_atual = 'Sala 6'
		elif (430 <= X and X <= 520) and (180 <= Y and Y <= 285):
			sala_atual = 'Sala 7'
		elif (680 <= X and X <= 770) and (30 <= Y and Y <= 85):
			sala_atual = 'Sala 8'
		elif (680 <= X and X <= 770) and (130 <= Y and Y <= 185):	
			sala_atual = 'Sala 9'
		elif (680 <= X and X <= 770) and (230 <= Y and Y <= 285):
			sala_atual = 'Sala 10'
		elif (30 <= X and X <= 235) and (455 <= Y and Y <= 570):
			sala_atual = 'Sala 11'
		elif (280 <= X and X <= 385) and (455 <= Y and Y <= 570):
			sala_atual = 'Sala 12'
		elif (430 <= X and X <= 570) and (455 <= Y and Y <= 570):
			sala_atual = 'Sala 13'
		elif (615 <= X and X <= 770) and (455 <= Y and Y <= 570):
			sala_atual = 'Sala 14'
		else :
			sala_atual = ''	
		
		#Adiciona só a divisão quando esta ainda não foi adicionada
		if ((sala_atual not in Divisoes_Encontradas) and sala_atual != '') :
				Divisoes_Encontradas.append(sala_atual)
				
		
		
		#Só adiciona quando vê que todos os objetos ainda não foram registados
		if (bool(set(objetos).intersection(Objetos_Vistos)) == False) :
			#Objetos encontrados nas salas são adicionados a lista Objetos_Vistos tal como as mesmas
			for i in range (len(objetos)):
				Objetos_Vistos.append(objetos[i])
				Objetos_Vistos.append(sala_atual)
		
		
		
		#Só adciona a lista de médicos quando o mesmo ainda não foi registado
		if (bool(set(objetos).intersection(Medicos_Vistos)) == False) :
			for i in range (0, len(objetos)):
				#Problema com o if não encontra o medico mesmo que já tenha sido encontrado
				if ('medico' in objetos[i]):
					Medicos_Vistos.append(objetos[i])
					Medicos_Vistos.append(X)
					Medicos_Vistos.append(Y)

#--------------------------------------------------------------------------------------------------------------------		
		#só adiciona à lista de pessoas encontradas quando o mesmo ainda não foi registado
		if (bool(set(objetos).intersection(Pessoas_Encontradas)) == False):
			for i in range(len(objetos)):
				#Objetos encontrados nas salas são adicionados a lista Objetos_Vistos tal como as mesmas
				if(('medico' in objetos[i]) or ('doente' in objetos[i]) or ('enfermeiro' in objetos[i])):		
					Pessoas_Encontradas.append(Objetos_Vistos[i])

#--------------------------------------------------------------------------------------------------------------------	

	Tipos_de_Sala(sala_atual)
	
	Y_ant = Y
	
	X_ant = X
	
	Probabiliade_Condicionada ()
	#caso o agente tenha sido carregado o tempo tem que começar de novo
	if bat == 100 :
		a = time.time()

	pass
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Ver qual é o tipo da sala atual 	
def Tipos_de_Sala(sala):

	cama = 0 
	cadeira = 0
	mesa = 0
	
	aux_obj = []

	#corre a lista de Objetos vistos só nas salas e não corredores
	if ('Sala' in sala):
		for i in range (0, len(Objetos_Vistos)):
			if (Objetos_Vistos[i] == sala):
				if('cama' in Objetos_Vistos[i-1]):
					cama = cama + 1
				elif('cadeira' in Objetos_Vistos[i-1]):
					cadeira = cadeira + 1
				elif('mesa' in Objetos_Vistos[i-1]):
					mesa = mesa + 1	
	
	#Apenas entra no ciclo quando a sala já consegue ser identificada
	if (cama > 0 or cadeira > 2 or mesa > 0 ):
		#Só adiciona a sala quando vê que a mesma ainda não foram registados
		if (sala not in Tipos_Sala) :
			#Sala adicionada a lista Tipos_Sala
			#Tipo de sala adicionado
			if (cama > 0 ):
				Tipos_Sala.append(sala)
				Tipos_Sala.append('Quarto')
			elif (cama == 0 and cadeira > 0 and mesa > 0):
				Tipos_Sala.append(sala)
				Tipos_Sala.append('Sala de Enfermeiros')
			elif (cadeira > 2 and cama == 0 and mesa == 0):
				Tipos_Sala.append(sala)
				Tipos_Sala.append('Sala de Espera')
	
	#Se numa sala de espera uma mesa for encontrada (ou seja passar a ser uma sala de Enfermeiros)
	for i in range (0, len(Tipos_Sala)):
		#Se a sala for a atual e a mesma for uma Sala de Espera
		if (Tipos_Sala[i] == sala and Tipos_Sala[i+1] == 'Sala de Espera'):
			if (mesa > 0):
				Tipos_Sala[i+1] = 'Sala de Enfermeiros'
	pass
	
#Fazer a média dos segundos para perder 1 de bateria
def Media_Perda_Bateria (bateria, tempo) :
	
	media = 0
	
	#A bateria perdida é 100(bateria inicial) - a bateria atual
	e = 100 - bateria 
	
	#time.time() dá nos os segundos desde que o tempo começo, para UNIX Janeiro 1, 1970, 00:00:00 
	#Para saber quanto tempo passou desde que a bateria foi 100 temos que fazer o tempo atual menos o time.time() de quando a bateria era 100
	tem = tempo - a
	
	#Mostra quantos segundos foram necessários para perder 1 de bateria
	media =  tem / e
	
	return media
	
	pass
	
#Probabilidade de encontrar um objeto sendo que o outro já foi encontrado
def Probabiliade_Condicionada ():
	
	cont_obj1 = 0

	cont_reuniao = 0
	
	salas = []
	
	for i in range (0, len(Objetos_Vistos)):
		if ('enfermeiro' in Objetos_Vistos[i]):
			#Só é contado quando os enfermeiros estão em salas diferentes
			if (Objetos_Vistos[i+1] not in salas):
				cont_obj1 = cont_obj1 + 1
				aux = 0
				#Ver se nessa sala está um Doente
				for j in range (0, len(Objetos_Vistos)):
					# A sala tem que ser igual a sala do enfermeiro
					if (Objetos_Vistos[i+1] == Objetos_Vistos[j]):
						#Só se conta a reunião uma vez por cada sala
						if (aux == 0):
							if ('mesa' in Objetos_Vistos[j-1]):
								cont_reuniao = cont_reuniao + 1
								aux = 1
			#Sempre que exite um enfermeiro a sala onde o mesmo foi encontrado 	
			salas.append(Objetos_Vistos[i+1])
		
	#resultado = (cont_reuniao / len(Divisoes_Encontradas)) / (cont_obj1/ len(Divisoes_Encontradas))
	
	print(cont_obj1, cont_reuniao, len(Divisoes_Encontradas))
	
	pass

#-------------------------------------------------------------------------------------------------------
#ver o tipo de pessoa -> médico/doente/enfermeiro




#-------------------------------------------------------------------------------------------------------

#Qual foi a penúltima pessoa que viste?
def resp1():
	if Pessoas_Encontradas is None:
		print("O Robô ainda não entrou em contacto com nenhuma pessoa")
	elif Pessoas_Encontradas == 1:
		print("O Robô apenas encontrou uma pessoa")
	else:
		print("maior que  2", Pessoas_Encontradas[len(Pessoas_Encontradas) - 1])		
	
	pass

#Em que tipo de sala estás agora?
#Feito
def resp2():
	
	if sala_atual == '':
		print ("O agente de momento não se encontra em nenhuma sala.")
	else :
		for i in range (0, len(Tipos_Sala)):
			if (Tipos_Sala[i] == sala_atual):
				print ('A sala onde o agente se encontra de momento é ', Tipos_Sala[i+1], ".")
		
	pass

#Qual o caminho para a sala de enfermeiros mais próxima?
def resp3():
	
	
	pass

#Qual a distância até ao médico mais próximo?
#Feito
def resp4():
	
	aux = []
	
	aux_int = []
	
	dist = 0
	
	nome = ''
	
	if not Medicos_Vistos:
		print ("Ainda nenhum médico foi encontrado")
	else:	
		#For para o Medicos_Vistos [i] ser sempre o nome do medico !
		for i in range (0, len(Medicos_Vistos), 3):
			X_aux = Medicos_Vistos[i+1]
			Y_aux = Medicos_Vistos[i+2]
			a = (X_aux - X)**2 + (Y_aux - Y)**2
			dist = math.sqrt(a)
			aux.append(Medicos_Vistos[i])
			aux_int.append(dist)
		#menor valor da lista min(aux)			
		for i in range (0, len(aux_int)):
			if (min(aux_int) == aux_int[i]):
				print('O medico que se encontra mais perto é', aux[i])	

	pass

#Quanto tempo achas que demoras a ir de onde estás até as escadas?
def resp5():
	
	
    pass

#Quanto tempo achas que falta até ficares sem bateria?
#Feito
def resp6():
	
	#segundos necessários para perder 1 de bateria
	media = Media_Perda_Bateria (bat, b)
	
	tempo_medio = media * bat
	
	print ('Falta aproximadamente ', tempo_medio, 'sergundos para ficar sem bateria (margem de erro de menos de 2 segundos)') 
	
	pass

#Qual a probabilidade de encontrar um livro numa divisão, se já encontraste uma cadeira?
def resp7():
	
	
    pass

#Se encontrares um enfermeiro numa divisão, qual é a probabilidade de estar lá um doente?
def resp8():
	
	
    pass
