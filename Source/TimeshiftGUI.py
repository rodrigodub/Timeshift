#!/usr/bin/python

#################################################
## Timeshift GUI
## Interface grafica para Timeshift
##
## v2.1.0
## for ticket - move to Python 3
##
## Rodrigo Nobrega
## 20131002-20180428
#################################################


# import modules
from tkinter import *
#from Tkinter.tkFileDialog import *
# from tkFileDialog import *
from tkinter.filedialog import *
from Timeshift import *


# GUI class
class TimeshiftGUI(Frame):
	# constructor method
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	# createWidgets() method
	def createWidgets(self):

		# labelName Title
		self.labelName = Label(self, text='Timeshift', font=('Verdana', 28), fg='blue')
		self.labelName.grid(row=1, column=3)

		# fileName Label & Entry
		self.labelFileName = Label(self, text='File name', justify=LEFT)
		self.entryFileName = Entry(self, width=50)
		self.labelFileName.grid(row=3, column=0, columnspan=2)
		self.entryFileName.grid(row=3, column=2, columnspan=4)

		# button & file dialog
		self.buttonFileDialog = Button(self, text='Choose', padx=20, command=self.chooseFile)
		self.buttonFileDialog.grid(row=3, column=6, columnspan=2, padx=20)

		# timeDelta Label & Slider
		self.labelTimeDelta = Label(self, text='Time Delta (s)', padx=20, justify=LEFT)
		self.entryTimeDelta = Scale(self, from_=-10., to=10., length=400, orient=HORIZONTAL
			, resolution=0.01, troughcolor='white', activebackground='blue')
		self.labelTimeDelta.grid(row=4, column=0, columnspan=2)
		self.entryTimeDelta.grid(row=4, column=2, columnspan=4)

		# OK Button
		self.buttonOK = Button(self, text='OK', width=10, padx=20, command=self.OK)
		self.buttonOK.grid(row=7, column=2, pady=20)

		# Cancel Button
		self.buttonCancel = Button(self, text='Cancel', width=10, padx=20, command=self.quit)
		self.buttonCancel.grid(row=7, column=4)

	# OK method
	def OK(self):
		Timeshift(self.entryFileName.get(),self.entryTimeDelta.get())

	# choose file method
	def chooseFile(self):
		arquivo = askopenfilename(master=self)
		self.entryFileName.delete(0, END)
		self.entryFileName.insert(0, arquivo)
