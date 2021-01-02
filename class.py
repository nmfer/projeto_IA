# Classe que vai ser indicada as salas do determinado mundo;
class Rooms:
	# Declaração inicial da classe, com os valores especificados;
	def __init__ (self, XMax, XMin, YMax, YMin, RoomType):
		self.XMax = XMax
		self.XMin = XMin
		self.YMax = YMax
		self.YMin = YMin
		self.RoomType = RoomType
		self.PersonsInRoom = []
		self.ObjectsInRoom = []
		self.DoorsInRoom = []
		
	# Método para verificar se as coordenadas mencionadas, sendo a lista "positions" ([X, Y]), estão dentro da sala;
	def isInside(self, positions):
		if self.XMax >= positions[0] and self.XMin <= positions[0] and self.YMax >= positions[1] and self.YMin <= positions[1]:
			return True
		
		return False
		
	# Método para adicionar uma pessoa numa sala específica;
	def addPerson(self, Person):
		newPerson = Persons(Person["personName"], Person["timeFound"], Person["personType"], Person["coorX"], Person["coorY"])
	
		self.PersonsInRoom.append(newPerson)
	
	# Método para encontrar uma pessoa através do nome e tipo;
	def findPerson(self, PersonName, PersonType):	
		
		# Verifica se a lista de pessoas na sala não é vazia;
		if self.PersonsInRoom:
			for person in self.PersonsInRoom:
				# Caso o tipo de pessoa e o nome desta forem iguais ao pretendido, a pessoa existe na lista;
				if person.getPersonType() == PersonType and person.getPersonName() == PersonName:
					return True
		
		return False
		
	# Método para retornar o número de pessoas na sala com o determinado tipo;
	def getPersonsByType(self, PersonType):
		
		numOfPersonType = []
		# Verifica se a lista de pessoas na sala não é vazia;
		if self.PersonsInRoom:
			for person in self.PersonsInRoom:
				# Caso o tipo de pessoa seja do tipo pretendido, vai ser adicionado a uma lista; 
				if person.getPersonType() == PersonType:
					numOfPersonType.append(person)
					
		return numOfPersonType
		
	# Método para adicionar um objeto numa sala específica;
	def addObject(self, Object):
		newObject = Objects(Object["objectName"], Object["timeFound"], Object["objectType"])
	
		self.ObjectsInRoom.append(newObject)
	
	# Método para encontrar um objeto através do nome e tipo;
	def findObject(self, ObjectName, ObjectType):	
		
		# Verifica se a lista de objetos na sala não é vazia;
		if self.ObjectsInRoom:
			for person in self.ObjectsInRoom:
				# Caso o tipo de objeto e o nome deste forem iguais ao pretendido, o objeto existe na lista;
				if person.getObjectType() == ObjectType and person.getObjectName() == ObjectName:
					return True
		
		return False
	
	# Retorna uma lista das pessoas encontradas na sala;
	def getPersons(self):
		return self.PersonsInRoom
		
	def addDoor(self, Door):
		newDoor = Doors(Door["firstRoom"], Door["lastRoom"], Door["coorX"], Door["coorY"])
		
		self.DoorsInRoom.append(newDoor)
		
	# Método para encontrar uma porta através dos determinados atributos;
	def findDoor(self, Door):	
		
		# Verifica se a lista de portas não é vazia;
		if self.DoorsInRoom:
			for doorTemp in self.DoorsInRoom:
				doorLinks = doorTemp.getDoorLink()
				doorCoor = doorTemp.getDoorCoor()
				
				if doorLinks[0] == Door["firstRoom"] and doorLinks[1] == Door["lastRoom"] and doorCoor[0] == Door["coorX"] and doorCoor[1] == Door["coorY"]:
					return True
		
		return False
		
	# Método para definir o tipo de sala;
	def setRoomType(self, roomType):
		self.RoomType = roomType
		
# Classe que vai ser utilizada para guardar as pessoas que foram guardadas;
class Persons:
	# Declaração inicial da classe, com os valores especificados;
	def __init__ (self, Name, TimeFound, PersonType, CoorX, CoorY):
		self.Name = Name
		self.TimeFound = TimeFound
		self.PersonType = PersonType
		self.CoorX = CoorX
		self.CoorY = CoorY
		
	# Método para retornar o nome da Pessoa;
	def getPersonName(self):
		return self.Name
		
	# Método para retornar o Tipo da Pessoa;
	def getPersonType(self):
		return self.PersonType
		
	# Método para retornar o Tempo que a Pessoa foi encontrada pelo robot;
	def getPersonTimeFound(self):
		return self.TimeFound
		
	def getPersonCoord(self):
		return [self.CoorX, self.CoorY]
		
	def toString(self):
		
		return ('Nome: ' + str(self.Name) + 
		'\nTempo Encontrado: ' + str(self.TimeFound) +
		'\nTipo de Pessoa: ' + str(self.PersonType) +
		'\nCoordenadas: [' + str(self.CoorX) + ', ' + str(self.CoorY) + ']'
		)
		
# Classe que vai ser utilizada para guardar os objetos que foram guardadas;
class Objects:
	# Declaração inicial da classe, com os valores especificados;
	def __init__ (self, Name, TimeFound, ObjectType):
		self.Name = Name
		self.TimeFound = TimeFound
		self.ObjectType = ObjectType
		
	# Método para retornar o nome da Pessoa;
	def getObjectName(self):
		return self.Name
		
	# Método para retornar o Tipo da Pessoa;
	def getObjectType(self):
		return self.ObjectType
		
	# Método para retornar o Tempo que a Pessoa foi encontrada pelo robot;
	def getObjectTimeFound(self):
		return self.TimeFound
		
# Classe que vai ser utilizada para guardar as portas que foram identificadas;
class Doors:
	# Declaração inicial da classe, com os valores especificados;
	def __init__ (self, FirstDoor, LastDoor, CoorX, CoorY):
		self.FirstDoor = FirstDoor
		self.LastDoor = LastDoor
		self.CoorX = CoorX
		self.CoorY = CoorY
		
	# Retorna a linkagem das salas, ou seja, as duas salas que conectam esta;
	def getDoorLink(self):
		return [self.FirstDoor, self.LastDoor]
		
	# Retorna as coordenadas da porta que foram guardadas quando foi identificada;
	def getDoorCoor(self):
		return [self.CoorX, self.CoorY]
	
	def toString(self):
		return ('First Door: ' + str(self.FirstDoor) + 
		'\nLast Door: ' + str(self.LastDoor) +
		'\nCoordenadas: [' + str(self.CoorX) + ', ' + str(self.CoorY) + ']'
		)	












# Simples Booleano para verificar se as salas foram declaradas alguma vez;
roomsAlreadyDeclared = False

# Lista que vai indicar todas os dados das Salas no respetivo mundo;
roomsInWorld = []

# Sala onde o Robô se encontra (-1 significa sala não declarada ou porta);
robotCurrentRoom = -1

robotOldRoom = -1

globalPositions = []

personsFound = []

lastRoomKnown = -1
def declareRooms():
	global roomTemp
		
	# Coordenadas das Salas que serão declaradas;
	# Umas notas:
	# Mínimo Possível de X: 30;
	# Máximo Possível de X: 800;
	# Máximo Possível de Y: 30;
	# Máximo Possível de Y: 570;
	roomsCoordenates = {
		"Corredor-1": {
			"XMax": 540.0,
			"XMin": 110.0,
			"YMax": 135.0,
			"YMin": 30.0,
		},
		"Corredor-2": {
			"XMax": 110.0,
			"XMin": 30.0,
			"YMax": 305.0,
			"YMin": 90.0,
		},
		"Corredor-3": {
			"XMax": 660.0,
			"XMin": 540.0,
			"YMax": 305.0,
			"YMin": 30.0,
		},
		"Corredor-4": {
			"XMax": 770.0,
			"XMin": 30.0,
			"YMax": 415.0,
			"YMin": 305.0,
		},
		"Sala-5": {
			"XMax": 235.0,
			"XMin": 130.0,
			"YMax": 290.0,
			"YMin": 155.0,
		},
		"Sala-6": {
			"XMax": 385.0,
			"XMin": 280.0,
			"YMax": 290.0,
			"YMin": 155.0,
		},
		"Sala-7": {
			"XMax": 520.0,
			"XMin": 430.0,
			"YMax": 290.0,
			"YMin": 155.0,
		},
		"Sala-8": {
			"XMax": 770.0,
			"XMin": 680.0,
			"YMax": 90.0,
			"YMin": 30.0,
		},
		"Sala-9": {
			"XMax": 770.0,
			"XMin": 680.0,
			"YMax": 190.0,
			"YMin": 105.0,
		},
		"Sala-10": {
			"XMax": 770.0,
			"XMin": 680.0,
			"YMax": 290.0,
			"YMin": 205.0,
		}
	}
	
	# Visto ser um "Nested Dictionary", vai verificar todos os valores de cada dicionário, para declarar as salas globalmente;
	for key, value in roomsCoordenates.items():
		
		# Vai verificar se cada divisão corresponde a uma "Sala" ou a um "Corredor"
		if "Corredor" in key:
			roomTemp = Rooms(value["XMax"], value["XMin"], value["YMax"], value["YMin"], "Corredor")
		else:
			roomTemp = Rooms(value["XMax"], value["XMin"], value["YMax"], value["YMin"], "Sala")
			
		# Vai adicionar a Sala à respetiva lista;
		roomsInWorld.append(roomTemp)

#work
global roomsAlreadyDeclared, robotOldRoom, robotCurrentRoom, globalPositions, lastRoomKnown
	
	globalPositions = posicao
	
	# Verifica se as salas já foram declaradas. Caso não tenham, invoca a função que declará as salas pretendidas.
	if roomsAlreadyDeclared == False:
		declareRooms()
		print("O(A)s Corredores/Salas foram adicionado(a)s com sucesso!")
		roomsAlreadyDeclared = True
	
	# Variável para verificar se este se encontra dentro de uma sala. Caso não esteja, pode estar numa porta, ou sala desconhecida;
	isInsideRoom = False
	
	# Verifica se a posição corresponde a alguma sala conhecida;
	for i in range(0, len(roomsInWorld)):
		if roomsInWorld[i].isInside(posicao):
			robotOldRoom = robotCurrentRoom
			robotCurrentRoom = i
			isInsideRoom = True
			break
			
	
	# Caso esteja dentro de uma sala, verifica se entrou noutra sala;
	if isInsideRoom == True:
		# Caso tenha mudado de sala (e não seja no início do mundo), indica que o robô mudou de sala;
		if robotCurrentRoom != robotOldRoom:
			
			# Se a sala anterior for desconhecida, significa que vai ser guardada uma porta!
			if robotOldRoom != -1:
				print("O Robô mudou-se da sala " + str(robotOldRoom+1) + " para a sala " + str(robotCurrentRoom+1))
				lastRoomKnown = -1
			else:
				print("O Robô mudou-se da zona desconhecida para a sala " + str(robotCurrentRoom+1))
				
				if lastRoomKnown != -1:
					print("ISTO É UMA PORTA")
					
					doorTempLastKnown = {
						"firstRoom": lastRoomKnown,
						"lastRoom": robotCurrentRoom,
						"coorX": globalPositions[0],
						"coorY": globalPositions[1],
					}
					
					if roomsInWorld[lastRoomKnown].findDoor(doorTempLastKnown) == False:
						roomsInWorld[lastRoomKnown].addDoor(doorTempLastKnown)
					
						print(doorTempLastKnown)
			
	else:
		if robotCurrentRoom != -1:
			print("O Robot entrou numa zona desconhecida! Será uma porta?")
			lastRoomKnown = robotCurrentRoom
			robotCurrentRoom = -1
			
	
	# Caso a lista não seja vazia, significa que existe algum objeto no "sensor" do robot;
	if objetos:
		# Vai percorrer toda a lista de objetos encontrados pelo sensor;
		for obj in range(0, len(objetos)):
			
			# Caso seja uma pessoa e esta não se encontre na lista de "Pessoas" encontradas, vai ser adicionado;
			if "enfermeiro" in objetos[obj] or "medico" in objetos[obj] or "doente" in objetos[obj]:
				personTemp = {
					"personName": objetos[obj],
					"timeFound": time.time(),
					"coorX": globalPositions[0], 
					"coorY": globalPositions[1]
				}
				
				# Vai definir o tipo de pessoa que encontrou;
				if "enfermeiro" in objetos[obj]:
					personTemp["personType"] = "Enfermeiro"
				elif "medico" in objetos[obj]:
					personTemp["personType"] = "Médico"
				elif "doente" in objetos[obj]:
					personTemp["personType"] = "Doente"
				else:
					personTemp["personType"] = "Outro"
				
				# Caso a pessoa encontrada não tenha sido armazenada na lista de pessoas, vai ser adicionada;
				if roomsInWorld[robotCurrentRoom].findPerson(personTemp["personName"], personTemp["personType"]) == False:
					roomsInWorld[robotCurrentRoom].addPerson(personTemp)
						
					
					print("O(a) " + str(personTemp["personType"]) + " " + str(objetos[obj]) + " foi encontrado(a) na sala " + str(robotCurrentRoom+1))
			# Caso não seja uma pessoa, é um objeto;
			else:
				objectTemp = {
					"objectName": objetos[obj],
					"timeFound": time.time()
				}
				
				if "cama" in objetos[obj]:
					objectTemp["objectType"] = "Cama"
				elif "cadeira" in objetos[obj]:
					objectTemp["objectType"] = "Cadeira"
				elif "livro" in objetos[obj]:
					objectTemp["objectType"] = "Livro"
				elif "mesa" in objetos[obj]:
					objectTemp["objectType"] = "Mesa"
				else:
					objectTemp["objectType"] = "Outro"
					
				# Caso não encontre este objeto  na lista de objetos da sala, significa que vai ser adicionado;
				if roomsInWorld[robotCurrentRoom].findObject(objectTemp["objectName"], objectTemp["objectType"]) == False:
					roomsInWorld[robotCurrentRoom].addObject(objectTemp)
					
					if objectTemp["objectType"] == "Cama":
						roomsInWorld[robotCurrentRoom].setRoomType("Quarto")
					
					print("O(a) " + str(objectTemp["objectName"]) + " " + str(objetos[obj]) + " foi encontrado(a) na sala " + str(robotCurrentRoom+1))
