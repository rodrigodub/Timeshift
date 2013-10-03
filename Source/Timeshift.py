#################################################
## Timeshift
## Python Class
## 
## v2.0.0
## for ticket 
## 
## Rodrigo Nobrega
## 20131002-
#################################################

# import modules
from datetime import *
import os



# define class
class Timeshift(object):
	"""docstring for Timeshift"""
	def __init__(self, fileName, deltaTime):
		super(Timeshift, self).__init__()
		self.fileName = fileName
		self.deltaTime = deltaTime
		







# define class
class Prote:

	# documentation
	"""\
	A simple text processor
	Usage: Prote(<filepath/filename>,<original string>,<new string>)
	"""

	
	# constructor with attributes
	def __init__(self, pathfilename, string1, string2):
		self.inputFileName = pathfilename
		self.inputString = string1
		self.outputString = string2
		self.replaceString()
		self.renaming()
	

	
	# methods
	
	def autoIncrement(self):
		if self.inputFileName[ self.inputFileName.rfind('.')-3 : self.inputFileName.rfind('.') ].isdigit():
			return ('00' + str(int(self.inputFileName[self.inputFileName.rfind('.')-3:self.inputFileName.rfind('.')]) + 1))[-3:]
		else:
			return '001'
			
	
	def outputFileName(self):
		return self.inputFileName[:-4] + '_temp'


	def	replaceString(self):
		# open files
		inputFile = open(self.inputFileName,'r')
		outputFile = open(self.outputFileName(),'w')
		# iterate
		for eachLine in inputFile:
			outputFile.write(eachLine.replace(self.inputString,self.outputString))
		# close files
		outputFile.close()
		inputFile.close()

		
	def timecomb(self):
		comb = str(datetime.now().year) + ('0' + str(datetime.now().month))[-2:] + ('0' + str(datetime.now().day))[-2:] + ('0' + str(datetime.now().hour))[-2:] + ('0' + str(datetime.now().minute))[-2:] + ('0' + str(datetime.now().second))[-2:]
		return comb
	
	
	def renaming(self):
		os.rename(self.inputFileName, self.inputFileName[:-4] + '_' + self.timecomb() + '.bak')
		os.rename(self.outputFileName(), self.inputFileName)
		
		







