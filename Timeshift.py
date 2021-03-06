#################################################
# Timeshift
# Script to adjust SRT subtitle file timestamps
#
# v3.02
# for ticket #2
#
# Rodrigo Nobrega
# 20131002-20180501
#################################################

# import modules
import datetime
import os


# define Timeshift class
class Timeshift(object):
	"""
	Timeshift is a Python script to adjust
	timestamps of SRT subtitle files.
	"""

	# constructor with attributes
	# and execute
	def __init__(self, fileName, deltaTime):
		super(Timeshift, self).__init__()
		self.inputFileName = fileName
		self.deltaTime = deltaTime
		self.replaceTime()
		self.renaming()

	# method timeList()
	# to convert SRT ascii timestamps to a list of two string times
	# Parameters:
	# line - ex: '00:17:00,748 --> 00:17:02,648'
	def timeList(self, line):
		return line.replace(',','.').split(' --> ')

	# method adjustTime()
	# to take one string time, convert it to datetime, increase/decrease
	# 	with self.deltaTime, and return a string version
	# Parameters:
	# timeValue - ex: '00:17:00,748'
	def adjustTime(self, timeValue):
		adj = datetime.datetime(datetime.datetime.today().year
			, datetime.datetime.today().month
			, datetime.datetime.today().day
			, int(timeValue.split(':')[0])
			, int(timeValue.split(':')[1])
			, int(float(timeValue.split(':')[2]))
			, int((str(float(timeValue.split(':')[2])).split('.')[1] + '000000')[0:6])
			) + datetime.timedelta(seconds = int(float(self.deltaTime)) , microseconds = int((str(float(self.deltaTime)).split('.')[1] + '000000')[0:6]))
		# output with english number notation / saida com ponto
		#return ('00'+str(adj.hour))[-2:] + ':' + ('00'+str(adj.minute))[-2:] + ':' + ('00'+str(adj.second))[-2:] + '.' + str(int(adj.microsecond/1000))
		# output with portuguese number notation / saida com virgula
		return ('00'+str(adj.hour))[-2:] + ':' + ('00'+str(adj.minute))[-2:] + ':' + ('00'+str(adj.second))[-2:] + ',' + str(int(adj.microsecond/1000))

	# method transformLine()
	# to adjustTime of an entire timestamp line, and return the line
	# 	with the same format
	# Parameters:
	# line - ex: '00:17:00,748 --> 00:17:02,648'
	def transformLine(self, line):
		return self.adjustTime(self.timeList(line)[0]) + ' --> ' + self.adjustTime(self.timeList(line)[1])

	# method outputFileName()
	# reused from Prote.
	# to take the same name of the self.inputFileName, remove extension
	# 	and append '_temp'
	def outputFileName(self):
		return self.inputFileName[:-4] + '_temp'

	# method replaceTime()
	# reused/refactored from Prote.replaceString().
	# to parse self.inputFileName and process time stamps, and
	# output another file with same format, but modified timestamps
	def	replaceTime(self):
		# open files
		inputFile = open(self.inputFileName,'r', encoding = "ISO-8859-1")
		outputFile = open(self.outputFileName(),'w', encoding = "ISO-8859-1")
		# iterate
		for eachLine in inputFile:
			if eachLine.find(' --> ') == -1:
				outputFile.write(eachLine)
			else:
				outputFile.write(self.transformLine(eachLine) + '\n')
				#outputFile.write('\n')
		# close files
		outputFile.close()
		inputFile.close()

	# method timecomb()
	# reused from Prote.
	# to create a timestamp of transform time, to append to the backup SRT file name
	def timecomb(self):
		comb = str(datetime.datetime.now().year) + ('0' + str(datetime.datetime.now().month))[-2:] + ('0' + str(datetime.datetime.now().day))[-2:] + ('0' + str(datetime.datetime.now().hour))[-2:] + ('0' + str(datetime.datetime.now().minute))[-2:] + ('0' + str(datetime.datetime.now().second))[-2:]
		return comb

	# method renaming()
	# reused from Prote.
	# to exchange file names - use original self.inputFileName as the new
	# 	transformed file, and rename the original file with <timecomb>.bak
	def renaming(self):
		os.rename(self.inputFileName, self.inputFileName[:-4] + '_' + self.timecomb() + '.bak')
		os.rename(self.outputFileName(), self.inputFileName)


# function to convert a 'hh:mm:ss' string to a datetime
def timestringconvert(timestring):
	# count colon and validate
	try:
		timestring.count(':') == 2
	except:
		print('Time string format should be HH:MM:SS')
		break
	n = datetime.datetime.now()
	a = [int(i) for i in timestring.spli[':']]
	b = datetime.datetime(n.year, n.month, n.day, a[0], a[1], a[2])
	return b


# main loop
def main():
	print('\n=============================================================================')
	print('                   Adjust SRT Subtitles timestamps')
	print('=============================================================================\n')
	id = input('Subtitle file location directory: ')
	print(id)


# main, calling main loop
if __name__ == '__main__':
    # test()
    main()