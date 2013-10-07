#################################################
## Timeshift
## Python Class
## 
## v2.0.0
## for ticket 
## 
## Rodrigo Nobrega
## 20131002-20131007
#################################################

# import modules
import datetime
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


	# method adjust()
	def adjust(self, timeList, delta):
		return datetime.datetime(datetime.datetime.today().year
			, datetime.datetime.today().month
			, datetime.datetime.today().day
			, int(timeList.split(':')[0])
			, int(timeList.split(':')[1])
			, int(float(timeList.split(':')[2]))
			, int((str(float(timeList.split(':')[2])).split('.')[1] + '000000')[0:6])
			) + datetime.timedelta(seconds = 1, microseconds = 500000)
		#return datetime.datetime(datetime.datetime.today().year
		#	,datetime.datetime.today().month
		#	,datetime.datetime.today().day
		#	,0,2,51,456000)



	# method parsefile()











