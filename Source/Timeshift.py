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
#from time import * 
import os



# define class
class Timeshift(object):
	"""docstring for Timeshift"""

	# constructor with attributes
	def __init__(self, fileName, deltaTime):
		super(Timeshift, self).__init__()
		self.fileName = fileName
		self.deltaTime = deltaTime
		

	# method timeList()
	def timeList(self, line):
		return line.replace(',','.').split(' --> ')


	# method timeShift()
	def timeShift(self, timeList, delta):
		#return datetime.time(int(timeList[0].split(':')[0])
		#	, int(timeList[0].split(':')[1])
		#	, int(float(timeList[0].split(':')[2]))) 
		return datetime.time(0,2,51)



	# method parsefile()











