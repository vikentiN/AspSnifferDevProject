import os
import sys
import time
import shutil
import serial
import re

from datetime import datetime
from PyCRC.CRCCCITT import CRCCCITT

pathToLog = os.path.realpath("buffRawHex.log")
print(pathToLog)

# ====================================================================================================
# Sniffer Class Constructor
# ====================================================================================================
class SnifferBase(object):
    
    #define constants
	#PARAM_RE_PATTERN = ''
	logFile				   = (os.getcwd() + '\\log.log')
	logAsString       = ''
    #end constants

    # ====================================================================================================
    # Sniffer Constructor
    # ====================================================================================================
	def __init__(self):
		self.buffRawHex  = None	
		

    # ====================================================================================================
    # Function Print
    # ====================================================================================================
	def printActivity(self,msg):
		try:
			print(msg)
		except BaseException as e:
			print('SnifferBase:printActivity - ' + str(e))

    # ====================================================================================================
    # Function - Open Log File
    # ====================================================================================================
	def openLogFile(self, logFile="test7.txt"):
		try:
			if(None == self.buffRawHex or True == self.buffRawHex.closed):
				self.printActivity("Path to log file is:\n" + os.path.abspath(logFile))
				self.buffRawHex = open(logFile, 'r')
		except BaseException as e:
			self.printActivity("Failed to open " + "(" + str(logFile) + ")")
		else:
			self.printActivity("File is opened succeesfully!\n")
		return True

    # ====================================================================================================
    # Function Print File content
    # ====================================================================================================
        ##Way 1
	def printFileContent(self):
	    
	    self.printActivity('----WAY 1----')
	    
	    for line in self.buffRawHex:
	    	self.printActivity(line)
	    
	    
	    
	    #Way 2
	    #self.printActivity('----WAY 2----')
	    #self.buffRawHex.seek(0)
	    #
	    #for i in range(0,7):
	    #	line = self.buffRawHex.readline()
	    #	self.printActivity(line)
	    #
	    #self.printActivity('----WAY 3----')
	    
	    #Way3, put all data in RAM
	    #self.buffRawHex.seek(0)
	    #
	    #allLines = self.buffRawHex.readlines()
	    #for line in allLines:
	    #	self.printActivity(line)
	    #self.buffRawHex.flush()
	    #
	    #self.printActivity('----WAY 4----')
	    
	    #Way4
	    #self.buffRawHex.seek(0)
	    #
	    #data = self.buffRawHex.read(4) #will reads just the 1st 2 characters
	    #self.printActivity(data)
	    #data = self.buffRawHex.read(2) #will reads just the next 2 characters
	    #self.printActivity(data)
	    #
	    #
	    #self.printActivity('----WAY 5----')
	    
	    #self.buffRawHex.seek(0)
	    
	    with open("test.txt", "a", encoding = "utf-8") as f:
	    	f.write("\nVichka i Elenka")
	    	self.printActivity("Add Elenka to file")
	# ====================================================================================================
	# Function RegularExpression
	# ====================================================================================================
	def RegEx(self):
	    try:
	        self.printActivity('Start using RegEx...' + str(self.buffRawHex))
	
	        pattern = re.compile(r'[a-zA-Z\.-]')
	        self.logAsString = ''.join(line for line in self.buffRawHex)
	                  
	        matches = pattern.findall(self.logAsString)
	        for match in matches:
	                 self.printActivity('We have a match: ' + match)
	    except BaseException as e:
	        self.printActivity("RegEx:Error:  " + "(" + str(e) + ")")
