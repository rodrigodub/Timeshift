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
	ts = Timeshift('/Users/Rodrigo/Documents/GitHub/Timeshift/Test/Agents.of.S.H.I.E.L.D.S01E01.Pilot.WEB-DL.x264.AAC.srt',4)
	l1 = ts.timeList('00:02:51,326 --> 00:02:53,821') 
	print l1
	print ts.deltaTime
	print ts.adjust(l1[0], ts.deltaTime)
	print ts.adjust(l1[1], ts.deltaTime)



# main, calling main loop
if __name__ == '__main__':
    main()  










