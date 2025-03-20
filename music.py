"""
program: music.py
3/6/2025

simple command-lined based player that can play standard .mp3 audio file 

*** MUST INSTALL PYGAME before running this app!!!!

at command prompt run: pip install pygame --pre
"""

# import statement for the pygame mixer module 
from pygame import mixer


# initialize the mixer module 
mixer.init()

# display a menu for the user interface 
print("\nWelcome to the Python Music PLayer!")
print("Enter 1 to select a song file.")
print("Enter 2 to play the chosen song.")
print("Enter 3 to pause an active song.")
print("Enter 4 to unpause the song.")
print("Press any other key to exit the program.")


# logic statements that determine which option was entered and what to do
while True:
	menuChoice = input("Please select a menu option >>")

	# decision making that triggers each feature 
	if menuChoice == "1":
		songFile = input("Please enter the song's file name >>")
		mixer.music.load(songFile)
	elif menuChoice == "2":
		mixer.music.play()
	elif menuChoice == "3":
		mixer.music.pause()
	elif menuChoice == "4":
		mixer.music.unpause()
	else:
		input("Thank you for using the music player. Press ENTER to exit...")
		break