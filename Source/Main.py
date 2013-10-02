#!/usr/bin/python

#################################################
## Main
## Rotina principal
## 
## v2.0.0
## for ticket 
## 
## Rodrigo Nobrega
## 20131002-
#################################################



# import classes
from tkinter import *
# from Prote import *
from TimeshiftGUI import *


# main loop
def main():  
	root = Tk()
	#root.geometry('700x400+100+100')
	root.title('Timeshift')
	app = TimeshiftGUI(master=root)
	app.mainloop()
 

# main, calling main loop
if __name__ == '__main__':
    main()  










