# Save a file to two folders

import os, shutil, sys

# Global variables
# fileInit, dirInt = 0, 0
saveFile, sourceDir, destDir = "", ""

# Copies a given file to another directory
def copyToDir():
	
	global saveFile, destDir

	# Check to see if saveFile has been filled in
	if saveFile == "":
		# Have not entered in a file
		print("Please enter in a file to save!\n")
		return

	# Check to see if destDir has been filled in
	if destDir == "":
		# Have not entered in a directory
		print("Please choose a directory to save your work!\n")
		return
	
	# Navigate to directory on hard drive
	os.chdir(sourceDir)
	
	print("\nBeginning to search directory...")
	
	# Search the source directory
	for filename in os.listdir():
		
		if filename.find(saveFile) != -1: 				# Found a match
			print("\x1b[1;32mFILE: \x1b[0m" + filename) # Linux-specific
			shutil.copy(filename, destDir)				# Does the copying
			print("\n\x1b[1;32mSuccessfully copied\x1b[0m " + filename + " \x1b[1;32mto new directory.\x1b[0m\n")
			break
		else:
			print("FILE: " + filename)
	
	
	'''
	global dirInit, destDir
	
	if dirInit == 0:
		print("Where would you like to save this? Enter in the full path name.\n>> ", end="")
		destDir = input()
		dirInit = 1 # One-time prompt
	'''

# TODO: Combine both directory functions, since they're basically the same thing
	
# Sets or changes source directory
def chooseSourceDir():
	
	global sourceDir
	
	print("Your source directory is currently \x1b[1;33m" + sourceDir + "\x1b[0m. Would you like to change it?\n>> ", end="")
	ans = input()
	
	if ans.lower() == "no" or ans.lower() == "n":
		return
	else:
		print("Enter in the full path name of the directory you want to save from.\n>> ", end="")
		sourceDir = input()
		print("All right, your new source directory is " + sourceDir + ".\n")
	
# Sets or changes destination directory
def changeDir():

	global destDir
	
	print("Your destination directory is currently \x1b[1;33m" + destDir + "\x1b[0m. Would you like to change it?\n>> ", end="")
	ans = input()
	
	if ans.lower() == "no" or ans.lower() == "n":
		return
	else:
		print("Enter in the full path name of the directory you want to save to.\n>> ", end="")
		destDir = input()
		print("All right, your new destination directory is " + destDir + ".\n")

# Changes the target file to be saved
def chooseFile():

	global saveFile

	print("Your file is currently \x1b[1;33m" + saveFile + "\x1b[0m. Would you like to change it?\n>> ", end="")
	ans = input()
	
	if ans.lower() == "no" or ans.lower() == "n":
		return
	else:
		print("Enter in the full path name of the file you want to save.\n>> ", end="")
		saveFile = input()
		print("All right, your new file is " + saveFile + ".\n")
	

# Prints a menu of options and returns user's choice
def menu():

	print('''\nChoose an option from below:
	
	1. Copy file to directory
	2. Choose file
	3. Choose source directory
	3. Choose destination directory
	4. Quit''')
	
	print("\n>> ", end="")
	return input()	

# Runs until option for Quit is returned
while True:
	
	# Show the menu
	option = int(menu())
	
	# Remove breaks after testing
	if option == 1:
		# Copy file to directory
		copyToDir()
		break
	elif option == 2:
		# Choose file
		chooseFile()
		break
	elif option == 3:
		# Choose source directory
		break
	elif option == 4:
		# Choose dest directory
		break
	elif option == 5:
		# Quit
		sys.exit()
	else:
		print("Invalid response. Please enter a number!\n")
		break