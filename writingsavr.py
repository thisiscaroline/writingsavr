# Save a file to two folders

import os, shutil, sys

# Global variables
saveFile, sourceDir, destDir = "", "", ""

# Copies a given file to another directory
def copyToDir():
	
	global saveFile, sourceDir, destDir

	# Check saveFile, sourceDir, destDir
	if saveFile == "":
		return "Please choose a file to save!\n"

	if sourceDir == "":
		return "Please choose a directory to save your work from!\n"
		
	if destDir == "":
		return "Please choose a directory to save your work to!\n"
	
	# Navigate to source directory on hard drive
	os.chdir(sourceDir)
	
	print("\nBeginning to search directory...\n")
	
	# Search the source directory
	for filename in os.listdir():
		
		if filename.find(saveFile) != -1: 					# Found a match
			print("\t\x1b[1;32mFILE: \x1b[0m" + filename) 	# Linux-specific
			shutil.copy(filename, destDir)					# Does the copying
			print("\n\t\t\x1b[1;32mSuccessfully copied\x1b[0m " + filename + " \x1b[1;32mto new directory.\x1b[0m\n")
			break
		else:
			print("\tFILE: " + filename)
	
	# If you are here, the file was not found
	print("\nError 404: File not found!\n")

###
# TODO: Combine both directory functions, since they're basically the same thing
###

# Sets or changes source directory
def chooseSourceDir():
	
	global sourceDir
	
	print("Your source directory is currently \x1b[1;33m" + sourceDir + "\x1b[0m. Would you like to change it?\n>> ", end="")
	ans = input()
	
	if ans.lower() == "no" or ans.lower() == "n":
		return
	else:
		print("Enter in the full path name of the directory you want to save FROM.\n>> ", end="")
		sourceDir = input()
		print("All right, your new source directory is " + sourceDir + ".\n")
	
# Sets or changes destination directory
def chooseDestDir():

	global destDir
	
	print("Your destination directory is currently \x1b[1;33m" + destDir + "\x1b[0m. Would you like to change it?\n>> ", end="")
	ans = input()
	
	if ans.lower() == "no" or ans.lower() == "n":
		return
	else:
		print("Enter in the full path name of the directory you want to save TO.\n>> ", end="")
		destDir = input()
		print("All right, your new destination directory is " + destDir + ".\n")

# Sets or changes the target file
def chooseFile():

	global saveFile

	print("Your file is currently \x1b[1;33m" + saveFile + "\x1b[0m. Would you like to change it?\n>> ", end="")
	ans = input()
	
	if ans.lower() == "no" or ans.lower() == "n":
		return
	else:
		print("Enter the filename you want saved.\n>> ", end="")
		saveFile = input()
		print("All right, your file is " + saveFile + ".\n")
	
# Displays what the current variables are set to
def displayStats():
	print("\n\x1b[1;33mFILE\x1b[0m: " + saveFile + "\n\x1b[1;33mSOURCE DIR\x1b[0m: " + sourceDir + "\n\x1b[1;33mDEST DIR\x1b[0m: " + destDir)

# Prints a menu of options and returns user's choice
def menu():

	print('''\nChoose an option from below:
	
	1. Copy file to directory
	2. Choose file
	3. Choose source directory
	4. Choose destination directory
	5. Display current locations
	6. Quit''')
	
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
	elif option == 2:
		# Choose file
		chooseFile()
	elif option == 3:
		# Choose source directory
		chooseSourceDir()
	elif option == 4:
		# Choose dest directory
		chooseDestDir()
	elif option == 5:
		# Displays current variables
		displayStats()
	elif option == 6:
		# Quit
		sys.exit()
	else:
		print("Invalid response. Please enter a number!\n")
		break