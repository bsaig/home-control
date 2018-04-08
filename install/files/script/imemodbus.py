#!/usr/bin/env python

import minimalmodbus
import MySQLdb
import time
import glob

# Open database connection
#Sql = ""
#db = MySQLdb.connect('localhost', 'testuser', 'test123', 'testing');
#cursor = db.cursor()	# Prepare a cursor object using cursor() method

#Setup Modubus Connection 
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 7) # port name, Slave address
#instrument.debug = True        #debug mode

def imeCurrent1():
	current_1 = None
	while current_1 is None:

		try:
			while True:
				current_1 = instrument.read_long(4102)
				current_1 = round(current_1,2)
				print "the current on phase 1 is", current_1,"mA"
				time.sleep(0.11)
		except IOError:
			pass
			#print "ioerror"
		except ValueError:
			time.sleep(0.11)
			#print "value error" 
			pass

def imeVoltage1():
	voltage = None
	while voltage is None:

		try:
			while True:
				voltage = instrument.read_long(4096)
				print "The voltage on phase 1 is", voltage,"mV"
				time.sleep(0.11)
		except IOError:
			#print "IOError"
			pass
		except ValueError:
			#print "Value error" 
			time.sleep(0.11)
			pass

def imeActivePower():
	activepower = None
	while activepower is None:

		try:
			while True:
				activepower = instrument.read_long(4116)
				print "The total power is", activepower,"mkW"
				time.sleep(0.11)
		except IOError:
			pass
			#print "IOError"
		except ValueError:
			#print "Value error" 
			time.sleep(0.11)
			pass
			
def imeOperatingTime():
	operatingTime = None
	while operatingTime is None:

		try:
			while True:
				operatingTime = instrument.read_long(4130)
				print "The time is", operatingTime,"s"
				time.sleep(0.11)
		except IOError:
			#print "IOError"
			pass
		except ValueError:
			#print "Value error" 
			time.sleep(0.11)
			pass

def imePhase1Power():
	phase1power = None
	while phase1power is None:

		try:
			while True:
				phase1power = instrument.read_long(4140)
				print "The power on phase 1 is", phase1power,"mkW"
				time.sleep(0.11)
		except IOError:
			#print "IOError"
			pass
		except ValueError:
			#print "Value error" 
			time.sleep(0.11)
			pass
			
def imeFrequency():
	frequency = None
	while frequency is None:

		try:
			while True:
				frequency = instrument.read_long(1638)
				print "The power on phase 1 is", phase1power,"mkW"
				time.sleep(0.11)
		except IOError:
			#print "IOError"
			pass
		except ValueError:
			#print "Value error" 
			time.sleep(0.11)
			pass
			
			#0x1026 WORD Frequency  #1638 (DEC)
			

while True:

	try:

		imeActivePower()
		imeCurrent1()
		imeOperatingTime()
		imePhase1Power()
		imeVoltage1()
		Sql = "insert into current_mesurement1 (time, pcbCurrent, imeCurrent, temperature) values('%s','%f','%f','%f')" % (Time, current_ime, current_pcb, thermistor)
		with db:

			cursor.execute(Sql)	# Execute the SQL command
			
			print "Database Uploaded"

			db.close()
			
			time.sleep(10)
			
		break
		

	except KeyboardInterrupt:

		print "Stopped"

exit()
