# Save a file to Writing, Dropbox folders

import os, shutil, sys

# Global variables
fileInit = 0
dirInit = 0

# Navigate to folder on hard drive
print("Enter a directory to get files from. \n>> ", end="")
sourceDir = input()
os.chdir(sourceDir)

# Copies a given file to Dropbox
def copyToDropbox(file):
	
	global dirInit
	
	if dirInit == 0:
		print("Where would you like to save this? Enter in the full path name.\n>> ", end="")
		saveDir = input()
		dirInit = 1 # One-time prompt
	
	shutil.copy(filename, saveDir)
	print("\n\x1b[1;32mSuccessfully copied\x1b[0m " + filename + " \x1b[1;32mto Dropbox.\x1b[0m\n")

print("Press any key, or hit ENTER to quit: \n>> ", end="")
while input() != "":

	# If fileInit == 0, ask for filename
	if fileInit == 0:
		print("What file would you like to save to Dropbox? \n>> ", end="")
		saveFile = input() # Regex to search for containment?
		print("Okay, you've entered in \x1b[1;32m" + saveFile + "\x1b[0m.\n")
		fileInit = 1 # Prevents return

	print("\nBeginning to search directory...")
	for filename in os.listdir():
		
		#if filename.startswith('TEST'):
		if filename.find(saveFile) != -1: # Found a match
			print("\x1b[1;32mFILE: \x1b[0m" + filename) # Linux-specific
			copyToDropbox(filename)
			break
		else:
			print("FILE: " + filename)
			
	print("Press any key, or hit ENTER to quit: \n>> ", end="")