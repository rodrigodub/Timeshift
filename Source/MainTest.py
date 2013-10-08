#!/usr/bin/python

#################################################
## Main
## Rotina principal
## 
## v2.0.0
## for ticket 
## 
## Rodrigo Nobrega
## 20131002-20131007
#################################################



# import classes
#from tkinter import *
from Timeshift import *
#from TimeshiftGUI import *


# main loop
def main():  
	#root = Tk()
	#root.geometry('700x400+100+100')
	#root.title('Timeshift')
	#app = TimeshiftGUI(master=root)
	#app.mainloop()
	# on mac
	#srt = Timeshift('/Users/Rodrigo/Documents/GitHub/Timeshift/Test/Agents.of.S.H.I.E.L.D.S01E01.Pilot.WEB-DL.x264.AAC.srt',3.12)
	# on win
	srt = Timeshift(r'C:\Users\rnobrega.METECH\Documents\GitHub\Timeshift\Test\Agents.of.S.H.I.E.L.D.S01E01.Pilot.WEB-DL.x264.AAC.srt',-6)
	#l1 = '00:09:41,211 --> 00:09:43,999' 
	#print 'ENTRADA: ', l1
	#print 'DELTA T: ', srt.deltaTime
	#print 'SAIDA: ', srt.transformLine(l1, srt.deltaTime)
	#print srt.outputFileName()
	print 'Done.'



# main, calling main loop
if __name__ == '__main__':
    main()  










