# Save a file to Writing, Dropbox folders

import os, shutil

# TODO: Take user input for directories

# Navigate to folder on hard drive
os.chdir('C:\\Users\\Caroline\\Documents\\Writing')

# Copies a given file to Dropbox
def copyToDropbox(file):
	# TODO: Maybe add a first-time prompt?
	shutil.copy(filename, 'C:\\Users\\Caroline\\Dropbox\\Fanfiction and Writing')
	print("\n\x1b[1;32mSuccessfully copied\x1b[0m " + filename + " \x1b[1;32mto Dropbox.\x1b[0m\n")

firstHit = 0
	
print("Enter anything, or hit ENTER to quit: \n>> ", end="")
while input() != "":

	# If firstHit == 0, ask for filename
	if firstHit == 0:
		print("What file would you like to save to Dropbox? \n>> ", end="")
		saveFile = input() # Regex to search for containment?
		firstHit = 1 # Prevents return

	for filename in os.listdir():
		
		if filename.startswith('TEST'):
			print("\x1b[1;32mFILE: \x1b[0m" + filename) # Linux-specific
			copyToDropbox(filename)
			break
		else:
			print("FILE: " + filename)
			
	print("Enter anything, or hit ENTER to quit: \n>> ", end="")