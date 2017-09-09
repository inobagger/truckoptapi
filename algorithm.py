import urllib2
import json
import datetime
import sys

priceKm = 0.2
priceHour = 12

def alg(origin, destination, waypoints):
	key = "AIzaSyDLpmbzdP0zZPJsb5LxN6QxEefuSorjRkg"

	#print "Processing route from %s to %s stopping at %s..." % (origin, destination, waypoints)
	link = "https://maps.googleapis.com/maps/api/directions/json?origin="+origin+"&destination="+destination+"&key="+key
	r = urllib2.urlopen(link.replace(" ","%20"))
	a = json.loads(r.read())
	#print "Ruta directa:"
	distancia = a["routes"][0]["legs"][0]["distance"]["value"]
	tiempo = a["routes"][0]["legs"][0]["duration"]["value"]
	distanciaOriginal = distancia
	tiempoOriginal = tiempo

	if waypoints == "":
		wayp = False
		sys.exit(0)

	numberOfWaypoints = len(waypoints.split("|"))
	link = "https://maps.googleapis.com/maps/api/directions/json?origin="+origin+"&destination="+destination+"&waypoints="+	waypoints+"&key="+key
	r = urllib2.urlopen(link.replace(" ","%20"))
	a = json.loads(r.read())
	#print ""
	#print "Debug link: " + link
	#print ""

	totalKm = 0
	totalTime = 0
	for i in range(numberOfWaypoints+1):
		#print "Ruta [%d/%d]" % (i+1, numberOfWaypoints+1)
		#print "From: " + a["routes"][0]["legs"][i]["start_address"]
		#print "To: " + a["routes"][0]["legs"][i]["end_address"]
		distancia = a["routes"][0]["legs"][i]["distance"]["value"]
		tiempo = a["routes"][0]["legs"][i]["duration"]["value"]
		totalKm += distancia
		totalTime += tiempo
		#print str(distancia/1000) + " km"
		#print str(datetime.timedelta(seconds=tiempo))
		#print ""
	timeDifference = totalTime - tiempoOriginal
	distanceDifference = totalKm - distanciaOriginal
	#print "Distancia / tiempo en ruta original: " + str(distanciaOriginal/1000) + " km / " + str(datetime.timedelta(seconds=tiempoOriginal))
	#print "Distancia / tiempo en ruta desviada: " + str(totalKm/1000) + " km / " + str(datetime.timedelta(seconds=totalTime))
	#print "Diferencia de distancia / tiempo: " + str(distanceDifference/1000) + " km / " + str(datetime.timedelta(seconds=timeDifference))
	ganancia = 6000 - (totalKm/1000) *priceKm - totalTime/3600.0*priceHour
	#print "Ganancia neta: "+ str(ganancia) + "E"
	3print ""
	return {"From": origin, "To": destination, "Waypoints": waypoints, "Ganancia": ganancia}