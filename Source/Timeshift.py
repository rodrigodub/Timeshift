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


	# method adjustTime()
	def adjustTime(self, timeValue, delta):
		adj = datetime.datetime(datetime.datetime.today().year
			, datetime.datetime.today().month
			, datetime.datetime.today().day
			, int(timeValue.split(':')[0])
			, int(timeValue.split(':')[1])
			, int(float(timeValue.split(':')[2]))
			, int((str(float(timeValue.split(':')[2])).split('.')[1] + '000000')[0:6])
			) + datetime.timedelta(seconds = int(float(delta)) , microseconds = int((str(float(delta)).split('.')[1] + '000000')[0:6]))
		# saida com ponto
		#return ('00'+str(adj.hour))[-2:] + ':' + ('00'+str(adj.minute))[-2:] + ':' + ('00'+str(adj.second))[-2:] + '.' + str(int(adj.microsecond/1000))
		# saida com virgula
		return ('00'+str(adj.hour))[-2:] + ':' + ('00'+str(adj.minute))[-2:] + ':' + ('00'+str(adj.second))[-2:] + ',' + str(int(adj.microsecond/1000))


	# method transformLine()
	def transformLine(self, line, delta):
		return self.adjustTime(self.timeList(line)[0], delta) + ' --> ' + self.adjustTime(self.timeList(line)[1], delta)


	# method parsefile()











