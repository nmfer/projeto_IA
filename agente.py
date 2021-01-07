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

#Iniciação da sala atual
sala_atual = ''

#Iniciação das cordenadas anteriores
X_ant = 0
Y_ant = 0

#Lista com todos as Salas Visitadas e o qual é o seu tipo de sala (Sala, Tipo de Sala)
Tipos_Sala = [] 

#Lista de obejtos e a sala onde forma encontrados (Nome Objeto, Sala onde foi visto)
Objetos_Vistos = []

#Lista de Medicos encontrados e as suas coordenadas (Nome do Medico, X, Y)
Medicos_Vistos = []

#Lista com todas as divisões encontradas
Divisoes_Encontradas = []

#Lista de Pessoas encontradas e as salas onde as mesmas foram encontradas (Pessoa, Sala)
Pessoas_Encontradas = []

Divisoes = []

#Iniciação do tempo
a = time.time()

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
		#Caso se encontre numa porta
		else :
			sala_atual = ''	
		
		#Adiciona só a divisão quando esta ainda não foi adicionada
		if ((sala_atual not in Divisoes_Encontradas) and sala_atual != '') :
				Divisoes_Encontradas.append(sala_atual)
				
		#Um objeto só é adicionado à lista Objetos_Vistos quando o mesmo ainda não se encontra na mesma
		if (bool(set(objetos).intersection(Objetos_Vistos)) == False) :
			#Objetos encontrados nas salas são adicionados à lista Objetos_Vistos tal como as salas onde se encontram 
			for i in range (len(objetos)):
				Objetos_Vistos.append(objetos[i])
				Objetos_Vistos.append(sala_atual)
		
		#Só adiciona o médico à lista Medicos_Vistos quando o mesmo ainda não se encontra na lista
		if (bool(set(objetos).intersection(Medicos_Vistos)) == False) :
			for i in range (0, len(objetos)):
				#Adiciona o nome do medico e as suas cordenadas (X, Y)
				if ('medico' in objetos[i]):
					Medicos_Vistos.append(objetos[i])
					Medicos_Vistos.append(X)
					Medicos_Vistos.append(Y)
		
		#só adiciona à lista de Pessoas_Encontradas quando o mesmo ainda não foi registado
		if (bool(set(objetos).intersection(Pessoas_Encontradas)) == False):
			for i in range(0, len(objetos)):
				#Se a condição de médico, doente ou enfermeiro se verificar adiciona o objeto à lista das Pessoas_Encontradas
				if(('medico' in objetos[i]) or ('doente' in objetos[i]) or ('enfermeiro' in objetos[i])):		
					Pessoas_Encontradas.append(objetos[i])			

		#só adiciona à lista das Divisões quando a sala_atual não se encontra na lista e quando a mesma é tem é uma 'Sala' e não Corredor ou porta
		if ((sala_atual not in Divisoes) and 'Sala' in sala_atual):
				#adiciona a sala
				Divisoes.append(sala_atual)
				#adiciona a coordenada X em que a sala é encontrada
				Divisoes.append(X)
				#adiciona a coordenada Y em que a sala é encontrada
				Divisoes.append(Y)		
				
	
	#As cordenadas anteriores passam a ser iguais às cordenadas atuais
	Y_ant = Y
	X_ant = X
	
	#Caso o robô tenha sido carregado o tempo tem que começar de novo
	if bat == 100 :
		a = time.time()
		
	pass


#Ver qual é o tipo da sala atual 	
def Tipos_de_Sala():
	
	
	#Sempre que esta função é chamada, ou seja sempre que se quer saber o tipo de sala onde se encontra o agente a contagem de cadeira, mesas e camas recomeça
	cama = 0 
	cadeira = 0
	mesa = 0

	#Corre a lista de Objetos_Vistos só nas salas e não corredores ou portas
	if ('Sala' in sala_atual):
		for i in range (0, len(Objetos_Vistos)):
			#Sempre que é encontrada uma cama, uma cadeira ou uma mesa o valor das mesmas incrementa
			if (Objetos_Vistos[i] == sala_atual):
				if('cama' in Objetos_Vistos[i-1]):
					cama = cama + 1
				elif('cadeira' in Objetos_Vistos[i-1]):
					cadeira = cadeira + 1
				elif('mesa' in Objetos_Vistos[i-1]):
					mesa = mesa + 1	
	
	#Apenas entra no ciclo quando a sala já pode ser identificada
	if (cama > 0 or cadeira > 0 or mesa > 0 ):
		#Só adiciona a sala quando vê que a mesma ainda não foi registada
		if (sala_atual not in Tipos_Sala) :
			#Sala adicionada à lista Tipos_Sala
			#Tipo de sala adicionado
			if (cama > 0 ):
				Tipos_Sala.append(sala_atual)
				Tipos_Sala.append('um quarto')
			elif (cama == 0 and cadeira > 0 and mesa > 0):
				Tipos_Sala.append(sala_atual)
				Tipos_Sala.append('uma sala de enfermeiros')
			elif (cadeira > 2 and cama == 0 and mesa == 0):
				Tipos_Sala.append(sala_atual)
				Tipos_Sala.append('uma sala de espera')
	
	#Se numa sala de espera uma mesa for encontrada (ou seja passar a ser uma sala de enfermeiros)
	for i in range (0, len(Tipos_Sala)):
		#Se a sala for a atual e a mesma for uma Sala de Espera
		if (Tipos_Sala[i] == sala_atual and Tipos_Sala[i+1] == 'uma sala de espera'):
			if (mesa > 0):
				Tipos_Sala[i+1] = 'uma sala de enfermeiros'
	pass


#Fazer a média dos segundos para perder um por cento de bateria
def Media_Perda_Bateria (bateria, tempo) :
	
	media = 0
	
	#A bateria perdida é 100(bateria inicial) - a bateria atual
	e = 100 - bateria 
	
	#time.time() dá nos os segundos desde que o tempo começo, para UNIX Janeiro 1, 1970, 00:00:00 
	#Para saber quanto tempo passou desde que a bateria carregada temos que subtrair o tempo atual ao time.time() de quando a bateria estava totalmente carregada
	tem = tempo - a
	
	#Mostra quantos segundos foram necessários para perder um por cento de bateria
	media =  tem / e
	
	return media
	
	pass


#Probabilidade de encontrar um objeto sendo que o outro já foi encontrado
def Probabiliade_Condicional (obj1, obj2):
	
	cont_obj1 = 0

	cont_reuniao = 0
	
	salas = []
	
	for i in range (0, len(Objetos_Vistos)):
		if (obj1 in Objetos_Vistos[i]):
			#Só é contado quando o obj1 está em salas diferentes
			if (Objetos_Vistos[i+1] not in salas):
				cont_obj1 = cont_obj1 + 1
				aux = 0
				#Ver se nessa sala se encontra um obj2
				for j in range (0, len(Objetos_Vistos)):
					# A sala tem que ser igual a sala do obj1
					if (Objetos_Vistos[i+1] == Objetos_Vistos[j]):
						#Só se conta a reunião uma vez por cada sala
						if (aux == 0):
							if (obj2 in Objetos_Vistos[j-1]):
								cont_reuniao = cont_reuniao + 1
								aux = 1
			#Sempre que exite um obj1 a sala onde o mesmo foi encontrado 	
			salas.append(Objetos_Vistos[i+1])
	
	#Apenas pode ser calculada se o obj_1 já tiver sido encontrado pelo menos uma vez
	if (cont_obj1 > 0):	
		resultado = (cont_reuniao / len(Divisoes_Encontradas)) / (cont_obj1/ len(Divisoes_Encontradas))
	else :
		resultado = -1
	
	print(len(Divisoes_Encontradas))
	
	return resultado	
	
	pass


#calcular a distância até à sala de enfermeiro mais próxima
def Distancia_sala_Enfermeiro():
	
	#variaveis auxiliares
	count = 0
	distancia = 0
	aux_sala = ''
	aux_distancia = 0
	X_sala = 0
	Y_sala = 0

	#listas auxiliar
	salas_enfermeiros = []
	sala_aux = []

	#percorre a lista dos Tipos de Sala que existem
	for i in range(0, len(Tipos_Sala), 2):
		#se Sala Enfermeiros estiver na lista dos tipos de Sala, algo que  tem que acontecer, pois caso não estivesse o mesmo não "acionava" a função
		if 'Sala de Enfermeiros' in Tipos_Sala[i+1]: 
			#caso a condição se verifique, adiciona +1 à variável count
			count = count + 1
			#percorre a lista das Divisões
			for j in range(0, len(Divisoes), 3):
				#se a sala dos enfermeiros se encontrar nas divisões, vai adicionar à lista sala_aux, a sala e as coordenadas X e Y
				if(Tipos_Sala[i] in Divisoes[j]):
					sala_aux.append(Divisoes[j])
					sala_aux.append(Divisoes[j+1]) #X
					sala_aux.append(Divisoes[j+2]) #Y

	#se só existe 1 sala de enfermeiros
	if count == 1:

		#variáveis tomam os valores de X e Y, correspondentes à posição 1 e 2 da lista da sala_aux
		X_sala = sala_aux[1]
		Y_sala = sala_aux[2]

		#como só existe 1 sala de enfermeiro, não é necessário calcular a distância à mais próxima
		#chama-se a função Caminho_sala_Enfermeiro, enviando o parâmetro da sala_aux[0], que corresponde à sala
		Caminho_sala_Enfermeiro(sala_aux[0])
	
	#se existir mais que 1 sala de enfermeiros	
	else:
		#percorre a lista sala_aux, 3 em 3, devido às coordenadas que se encontram na lista
		for i in range(0, len(sala_aux),3):
			
			#calcula a distância da posição em que o robô se encontra até às salas existentes, através do X e Y da posição atual e da sala
			distancia = math.sqrt((sala_aux[i+1] - X_ant)**2 + (sala_aux[i+2] - Y_ant)**2)
			
			salas_enfermeiros.append(sala_aux[i])
			salas_enfermeiros.append(distancia)
		
		#sala
		aux_sala = salas_enfermeiros[0]
		#distancia da posição atual até sala
		aux_distancia = salas_enfermeiros[1]
		
		#percorre a lista da salas_enfermeiros, começando em 2, de 2 em 2
		for i in range(2, len(salas_enfermeiros),2):
			#se a distancia_aux for maior que a distancia da posição i+1 da sala de enfermeiros, aux_sala toma o valor de i da lista
			if(distancia_aux > salas_enfermeiros[i+1]):
				#sala
				aux_sala = salas_enfermeiros[i]
			#caso contrário mantém aux_sala	
			else:
				#sala
				aux_sala = aux_sala

		Caminho_sala_Enfermeiro(aux_sala)
		
	pass


#definir o caminho/instruções que o robô deve seguir
def Caminho_sala_Enfermeiro(aux_distancias):

	if 'Corredor' in sala_atual:
		print('Desloque-se para a ', aux_distancias)
	elif aux_distancias == sala_atual:
		print('Já se encontra na Sala dos Enfermeiros')		
	else:	
		for i in range (0, len(Divisoes), 3):
			if (Divisoes[i] == sala_atual):
				print('Saia da sala atual para o corredor mais próximo e desloque-se para a ', aux_distancias)


#calcular a distância do robô às escadas
def Calcula_Distancia_Escadas():
	#Variáveis auxiliares
	distancia = 0
	#escadas encontram-se estáticas
	X_escadas = 180
	Y_escadas = 40

	distancia = math.sqrt((X_escadas - X)**2 + (Y_escadas - Y)**2)

	return distancia

	pass
	 

#calcular a média do tempo em relação à distância percorrida
def Media_Tempo_Deslocamento(b):
	#variáveis auxiliares
	media = 0
	tempo_final = time.time()
	distancia = 0
	tempo_des = 0

	distancia = math.sqrt((X - 100)**2 + (Y - 100)**2)
	
	if(distancia == 0):
		return 0
	else:
		tempo_des = tempo_final - b

		media =  tempo_des/distancia

	return media

	pass


#-----------------------PERGUNTAS-------------------------
#Qual foi a penúltima pessoa que viste?
#Feito - Nuno Fernandes
def resp1():

	#Se a lista, apenas tem uma pessoa apresenta uma mensagem a informar
	if len(Pessoas_Encontradas) == 1:
		print("O Robô apenas encontrou uma pessoa")
	#Se a lista das Pessoas Encontradas tiver mais que uma pessoa, apresenta a penultima vista
	elif len(Pessoas_Encontradas) > 1:
		print("A Penultima pessoa encontrada -> ", Pessoas_Encontradas[len(Pessoas_Encontradas) - 2])		
	#Caso a lista Pessoas_Encontradas se encontre vazia
	else:
		print("O Robô ainda não encontrou nenhuma pessoa")	
	
	
	pass

#Em que tipo de sala estás agora?
#Feito - Joana Almeida
def resp2():
	
	#Chama a função que vai buscar os tipos de sala
	Tipos_de_Sala()
	
	#Se não existir sala atual, por exemplo se encontrar numa porta
	if sala_atual == '':
		print ("O agente de momento não se encontra em nenhuma sala.")
	#Se de momento o agente se encontrar num corredor
	elif ('Corredor' in sala_atual):
		print("O agente encontra-se num corredor e não numa sala.")
	#Se o tipo de sala ainda não se consegue descobrir
	elif (sala_atual not in Tipos_Sala):
		print ("Ainda não foram encontrados pelo agente objetos suficientes para definir o tipo de sala.")
	#Caso a sala já tenha um tipo definido
	else :
		for i in range (0, len(Tipos_Sala)):
			if (Tipos_Sala[i] == sala_atual):
				print ('A sala onde o agente se encontra de momento é ', Tipos_Sala[i+1], ".")
		
	pass

#Qual o caminho para a sala de enfermeiros mais próxima?
#Feito - Nuno Fernandes
def resp3():
	
	#caso ainda não tenha sido registada nenhuma sala
	if len(Tipos_Sala) == 0:
		print("Ainda não existem salas registadas")	
	#se ainda não tiver sido registada uma sala de enfermeiros	
	elif 'Sala de Enfermeiros' not in Tipos_Sala:
		print("Ainda não foi registada uma sala de enfermeiros")
	else:		
		Distancia_sala_Enfermeiro()
	
	pass

#Qual a distância até ao médico mais próximo?
#Feito - Joana Almeida
def resp4():
	
	#Lista onde são armazenados os nomes dos médicos
	aux = []
	
	#Lista onde são armazenadas as distâncias
	aux_int = []
	
	#Distância do médico começa a 0
	dist = 0
	
	#Caso ainda nenhum médico tenha sido reconhecido pelo robô
	if not Medicos_Vistos:
		print ("Ainda nenhum médico foi reconhecido pelo robô")
	else:	
		#For para o Medicos_Vistos [i] ser sempre o nome do medico !
		for i in range (0, len(Medicos_Vistos), 3):
			#Posiçoes do médico guardadas em auxiliares
			X_aux = Medicos_Vistos[i+1]
			Y_aux = Medicos_Vistos[i+2]
			#Distância vetorial
			a = (X_aux - X)**2 + (Y_aux - Y)**2
			dist = math.sqrt(a)
			#O nome do médico é adicionado ao aux
			aux.append(Medicos_Vistos[i])
			#A distancia do médico é adicionada ao aux_init
			aux_int.append(dist)
		#Menor valor da lista min(aux)			
		for i in range (0, len(aux_int)):
			if (min(aux_int) == aux_int[i]):
				#Para aparecer apenas o nome do medico
				nome = aux[i].split('_')
				print('O medico que se encontra mais perto é Dr.', nome[1])	

	pass

#Quanto tempo achas que demoras a ir de onde estás até as escadas?
#Feito - Nuno Fernandes
def resp5():
	
	deslocamento = Calcula_Distancia_Escadas()
	
	#calcular a média do tempo de deslocamento
	media = Media_Tempo_Deslocamento(b)

	des_med = deslocamento * media
	if ((X <= 180) and (30 <= Y and Y <= 45)):
		print('O robô encontra-se nas escadas')
	elif (des_med == 0):
		print('Mova o robô')
	else:	
		print('Falta aproximadamente ', des_med, ' segundos para chegar às escadas (margem de erro de menos de 2 segundos)')
	
	pass


#Quanto tempo achas que falta até ficares sem bateria?
#Feito - Joana Almeida
def resp6():
	
	#Segundos necessários para perder 1 de bateria
	media = Media_Perda_Bateria (bat, b)
	
	#Tempo medio que será necessário para ficar com bateria a 0
	tempo_medio = media * bat
	
	print ('Falta aproximadamente ', "%.2f" %tempo_medio, 'segundos para ficar sem bateria.') 
	
	pass

#Qual a probabilidade de encontrar um livro numa divisão, se já encontraste uma cadeira?
#Feito - Joana Almeida
def resp7():
	
	obj1= 'cadeira'
	obj2 = 'livro'
	
	#Vai buscar o resultado
	resultado = Probabiliade_Condicional (obj1, obj2)
	
	if (resultado == -1):
		print('Ainda não foram encontrados cadeiras ou livros suficentes para calcular a probabilidade.')
	elif (resultado == 0):
		print('De momento a probabilidade é nula, o agente ainda não encontrou nenhum livro na mesma divisão que uma cadeira.')
	else :	
		print ('A probabilidade é', resultado, '.') 
	
	pass

#Se encontrares um enfermeiro numa divisão, qual é a probabilidade de estar lá um doente?
#Feito - Joana Almeida
def resp8():
	
	obj1= 'enfermeiro'
	obj2 = 'doente'
	
	#Vai buscar o resultado
	resultado = Probabiliade_Condicional (obj1, obj2)
	
	if (resultado == -1):
		print('Ainda não foram encontrados enfermeiros suficentes para calcular a probabilidade.')
	elif (resultado == 0):
		print('De momento a probabilidade é nula, o agente ainda não encontrou nenhum doente na mesma divisão que um enfermeiro.')
	else :	
		print ('A probabilidade é', resultado, '.') 
	
	pass
