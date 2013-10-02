#!/usr/bin/python

#################################################
## Timeshift GUI
## Interface gráfica para Timeshift
## 
## v2.0.0
## for ticket 
## 
## Rodrigo Nobrega
## 20131002-
#################################################


# import modules
from tkinter import *
from tkinter.filedialog import *
from Prote import *


# GUI class
class ProteGUI(Frame):
	# constructor method
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
	
	# createWidgets() method
	def createWidgets(self):
		
		# labelName Title
		self.labelName = Label(self, text='Protê', font=('Verdana', 28), fg='#AAAAFF')
		self.labelName.grid(row=1, column=3)
		
		# fileName Label & Entry
		self.labelFileName = Label(self, text='File name', justify=LEFT)
		self.entryFileName = Entry(self, width=50)
		self.labelFileName.grid(row=3, column=0, columnspan=2)
		self.entryFileName.grid(row=3, column=2, columnspan=4)
		
		# button & file dialog
		self.buttonFileDialog = Button(self, text='Choose', padx=20, command=self.chooseFile)
		self.buttonFileDialog.grid(row=3, column=6, columnspan=2, padx=20)
		
		# inputString Label & Entry
		self.labelinputString = Label(self, text='Original String', padx=20, justify=LEFT)
		self.entryinputString = Entry(self, width=50)
		self.labelinputString.grid(row=4, column=0, columnspan=2)
		self.entryinputString.grid(row=4, column=2, columnspan=4)		

		# outputString Label & Entry
		self.labeloutputString = Label(self, text='New String', justify=LEFT)
		self.entryoutputString = Entry(self, width=50)
		self.labeloutputString.grid(row=5, column=0, columnspan=2)
		self.entryoutputString.grid(row=5, column=2, columnspan=4)	
		
		# OK Button
		self.buttonOK = Button(self, text='OK', width=10, padx=20, command=self.OK)
		self.buttonOK.grid(row=7, column=2, pady=20)

		# Cancel Button
		self.buttonCancel = Button(self, text='Cancel', width=10, padx=20, command=self.quit)
		self.buttonCancel.grid(row=7, column=4)
	
	# OK method
	def OK(self):
		Prote(self.entryFileName.get(),self.entryinputString.get(),self.entryoutputString.get())
	
	# choose file method
	def chooseFile(self):
		arquivo = askopenfilename(master=self)
		self.entryFileName.delete(0, END)
		self.entryFileName.insert(0, arquivo)

		
		
# Notes to Debugger
# For tkinter, steps:
# 2. create top level windowing system
	#root = Tk()
	#root.geometry('700x400+100+100')
	#app = ProteGUI(master=root)
# and
# 5. enter the main event loop
	#app.mainloop()
# were moved to Main.py




