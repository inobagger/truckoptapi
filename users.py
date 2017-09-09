def validateUser(email, password):
	if(email=="a" and password=="b"):
		return True
	if(email=="c" and password=="d"):
		return True
	return False

def getNom(email):
	if(email=="a"):
		return "Pimp";
	return "Kinder"

def getCognom(email):
	if(email=="a"):
		return "Flaco"
	return "Malo"

def getDireccion(email):
	return "Diagonal 203, Barcelona, ES"

def getPedidos(email):
	d = {"1": {"From": "Munich",
						"To": "Barcelona",
						"Notifications": "[9/9/17 13:47] Picked up by driver;[9/9/17 15:59] 2 hours delay;[9/9/17 20:35] Delivered"}}
	return d

def isDriver(email):
	if(email=="a"):
		return True
	else:
		return False

def rutaActual():
	d = {"nextStop": "Paris"}
	return d

def recogidasPendientes():
	d = {"1": {"nomClient": "Johny Sanchez",
				"ciutat": "Lyon",
				"peso": 4300,
				"ocupacio": 4},
		"2": {"nomClient": "George Smith",
				"ciutat": "Milan",
				"peso": 3200,
				"ocupacio": 5}}
	return d