#!/usr/bin/python

import datetime
import time
import random
import sys
import operator
from math import sqrt


args=sys.argv[1:]
print args[0]
print args[1]
print args[2]

id_carro = args[0]
pos_orig = [float(x) for x in args[1].split(',')]
speed = [float(x) for x in args[2].split(',')]
bitacoraCarro = {"id_carro": id_carro, "posicion": pos_orig, 
				 "velocidad": speed, "destinoFinal": 600}

lst_interseccion = "0.0.0.0"


def rcvInterseccion ():
	return "0.0.0.0"

def reportaEstatus (bitacoraCarro, lst_interseccion):
	print "Enviando estatus..."

def rcvRespuesta():
	print "Recibiendo estatus..."
	return {'id_carro': id_carro, 'posicion': 
	random.randrange(0, 11, 2), 'velocidad': random.randrange(0, 20, 2)}

def updEstatus(d, bitacoraCarro):
	print "Actualizando estatus..."
	
	bitacoraCarro['velocidad'] = speed	
	print "velocidad=" + str(bitacoraCarro['velocidad'])

	return bitacoraCarro
	


while True:
	lst_interseccion = rcvInterseccion ()

	t1 = int(round(time.time() * 1000))
	print "t1= " + str(t1)  
	reportaEstatus(bitacoraCarro, lst_interseccion)

	time.sleep(1)
	
	#Recibe respuesta 
	dd = rcvRespuesta()

	t2 = int(round(time.time() * 1000))
	print "t2= " + str(t2)
	tspent = ( t2 - t1 ) / 1000
	print "t2=" + str(t2) + ", t1=" + str(t1) + "= tspent=" + str(tspent)

	print "Posicion inicial =" + str(bitacoraCarro.get("posicion"))
	print "velocidad=" + str(bitacoraCarro.get("velocidad"))
	speed = bitacoraCarro['velocidad']
	coord = bitacoraCarro['posicion']
	#bitacoraCarro['posicion']
	pos = map( operator.add,  coord, [ tspent * x for x in speed] ) 

	#pos = bitacoraCarro['posicion'] + ( operator.add( bitacoraCarro['velocidad'] * tspent )

	print "Velocidad=" + str(bitacoraCarro['velocidad']) + ", Posicion final =" + str(pos)
	bitacoraCarro['posicion'] = pos

	#y actualiza diccionario
	bitacoraCarro = updEstatus(dd, bitacoraCarro)

	#time.sleep(3)

	distancia = sqrt ( (pos [0] - pos_orig[0])  ** 2 + (pos [1] - pos_orig[1]) ** 2 )

	print ("distancia=" + str(distancia) + ", destinoFinal= " + str(bitacoraCarro['destinoFinal'] ) )
	if distancia > bitacoraCarro['destinoFinal']:
		print "*** Hemos llegado!"
		sys.exit(0)

	print "--------------------------------"
print "***Fin"