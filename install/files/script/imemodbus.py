#!/usr/bin/env python

import minimalmodbus
import MySQLdb
import time
import glob

# Open database connection
Sql = ""
# Modify the following line with your mysql credentials
db = MySQLdb.connect('localhost', 'testuser', 'test123', 'test');
cursor = db.cursor()	# Prepare a cursor object using cursor() method

#Setup Modubus Connection
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 7) # port name, Slave address
#instrument.debug = True        #debug mode

def imeCurrent1():
	current1 = None
	while current1 is None:

		try:
			while True:
				current1 = instrument.read_long(4102)
				current1 = round(current1,2)
				current1 = current1/1000
				print "The current on phase 1 is", current1,"A"
		except IOError:
			pass
			#print "ioerror"
		except ValueError:
			#print "value error"
			pass
	return current1

def imeVoltage1():
	voltage1 = None
	while voltage1 is None:

		try:
			while True:
				voltage1 = instrument.read_long(4096)
				voltage1 = round(voltage1,2)
				voltage1 = voltage1/1000
				print "The voltage on phase 1 is", voltage1,"V"
				#time.sleep(0.11)
		except IOError:
			#print "IOError"
			pass
		except ValueError:
			#print "Value error"
			#time.sleep(0.11)
			pass
	return voltage1

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
			#time.sleep(0.11)
			pass
	return activepower

def imeOperatingTime():
	operatingTime = None
	while operatingTime is None:

		try:
			while True:
				operatingTime = instrument.read_long(4130)
				print "The time is", operatingTime,"s"
				#time.sleep(0.11)
		except IOError:
			#print "IOError"
			pass
		except ValueError:
			#print "Value error"
			time.sleep(0.11)
			pass
	return operatingTime

def imePhase1Power():
	phase1power = None
	while phase1power is None:

		try:
			while True:
				phase1power = instrument.read_long(4140)
				print "The power on phase 1 is", phase1power,"mkW"
				#time.sleep(0.11)
		except IOError:
			#print "IOError"
			pass
		except ValueError:
			#print "Value error"
			#time.sleep(0.11)
			pass

def imeFrequency():
	frequency = None
	while frequency is None:

		try:
			while True:
				frequency = instrument.read_register(4134)
				frequency = round(frequency, 1)
				frequency = frequency/10
				print "The frequency is", frequency,"Hz"
		except IOError:
			#print "IOError"
			pass
		except ValueError:
			#print "Value error"
			pass

	return frequency

while True:

	try:
		activepower = imeActivePower()
		current1 = imeCurrent1()
		imeOperatingTime()
		imePhase1Power()
		voltage1 = imeVoltage1()
		frequency = imeFrequency()
		#Create Table "meter" with the bellow columns
		Sql = "INSERT INTO meter (Current1, Voltage1, Frequency, Energy) VALUES ('%f','%f','%f','%f')" % (current1, voltage1, frequency, activepower)
		with db:

			cursor.execute(Sql)	# Execute the SQL command
			print "Database Uploaded"
		db.close()
		break


	except KeyboardInterrupt:

		print "Stopped"

exit()
