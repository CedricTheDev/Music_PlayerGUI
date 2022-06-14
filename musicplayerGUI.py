
"""
Program: GUItemplate.py (page 251)
Author: George 6/2/2022
Template code for all GUI-based applications
"""
from breezypythongui import EasyFrame
from pygame import mixer
from tkinter import PhotoImage
from tkinter.font import Font
# other imports
# Must install the pygame package by running : pip install pygame
class MusicPlayerGUI(EasyFrame):

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Music Player GUI", background = "black")
		self.addLabel(text = " Python Music Player", row = 0, column = 0, columnspan = 3, background = "black", foreground = "orange", sticky = "NSEW")
		# Create a label variable for the image label
		self.imageLabel = self.addLabel(text = "", row = 1, column = 0, columnspan = 3, sticky = "NSEW")

		#set background to label

		self.image = PhotoImage(file = "music_player.png")
		self.imageLabel["image"] = self.image

		self.addLabel(text = "Enter the file name to load", row = 2, column = 0, background = "black", foreground = "orange")
		self.musicFile = self.addTextField(text = "", row = 2, column = 1, width = 35)
		self.addButton(text = "Load", row = 2, column = 2, command = self.loadFile)

		#3 buttons for the music player functions
		self.playButton = self.addButton(text = "Play", row = 3, column = 0, state = "disabled", command = self.playMusic)
		self.pauseButton = self.addButton(text = "pause", row = 3 , column = 1, state = "disabled" , command = self.pauseMusic)
		self.resumeButton = self.addButton( text = "resume", row = 3, column = 2, state = "disabled", command = self.resumeMusic)

	# Event handling methods for the comannd button
	def loadFile(self):
		#initialize the pygame mixer
		mixer.init()
		songFile = self.musicFile.getText()
		mixer.music.load(songFile)
		self.playButton["state"] = "normal"

	def playMusic(self):
		# play the previously loaded file
		mixer.music.play()
		self.pauseButton["state"] = "normal"

	def pauseMusic(self):
		# Pause the current song
		mixer.music.pause()
		self.pauseButton["state"] = "disabled"
		self.resumeButton["state"] = "normal"

	def resumeMusic(self):
		#take song out of pause mode
		mixer.music.unpause()
		self.pauseButton["state"] = "normal"
		self.resumeButton["state"] = "normal"


# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	MusicPlayerGUI().mainloop()

# global call to the main() method
main()
