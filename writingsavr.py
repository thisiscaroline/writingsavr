# Save a file to two folders

import os, shutil, sys

# Global variables
saveFile, sourceDir, destDir = "", "", ""

# Main loop
def main():
	
	print("Lazy option (Y/N)?\n>> ", end="")
	lazy(input())
	
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
			# Choose directory
			chooseDir()
		elif option == 4:
			# Displays current variables
			displayStats()
		elif option == 5:
			# Quit
			sys.exit()
		else:
			print("Invalid response. Please enter a number!\n")

# Lazy variable fill, hard-code your file paths here
def lazy(ans):

	global saveFile, sourceDir, destDir

	if ans.lower() == 'y':
		# saveFile, sourceDir, destDir = "", "", ""
		return
			
# Prints a menu of options and returns user's choice
def menu():

	print('''\nChoose an option from below:
	
	1. Copy file to directory
	2. Choose file
	3. Choose directory
	4. Display current locations
	5. Quit''')
	
	print("\n>> ", end="")
	return input()
			
# Copies a given file to another directory
def copyToDir():
	
	global saveFile, sourceDir, destDir

	# Check saveFile, sourceDir, destDir
	if saveFile == "":
		return print("Please choose a file to save!\n")
		
	if sourceDir == "":
		return print("Please choose a directory to save your work from!\n")
		
	if destDir == "":
		return print("Please choose a directory to save your work to!\n")
	
	# Navigate to source directory on hard drive
	os.chdir(sourceDir)
	
	print("\nBeginning to search directory...\n")
	
	# Search the source directory
	for filename in os.listdir():
		
		if filename.find(saveFile) != -1: 					# Found a match
			print("\t\x1b[1;32mFILE: \x1b[0m" + filename)
			shutil.copy(filename, destDir)					# Doing the copying
			print("\n\t\t\x1b[1;32mSuccessfully copied\x1b[0m " + filename + " \x1b[1;32mto new directory.\x1b[0m\n")
			return
		else:
			print("\tFILE: " + filename)
	
	# If you are here, the file was not found
	print("\nError 404: File not found!\n")

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
	
# Sets or changes the directory
def chooseDir():
	
	global sourceDir, destDir
	
	print("Would you like to change the SOURCE or DESTINATION directory, or quit?\n>> ", end="")
	ans = input()
	
	if ans.lower() == "quit":
		return
	else:
		print("Enter in the directory's full path name.\n>> ", end="")
		tempPath = input()
		print("All right, your new directory is " + tempPath + ".\n")

	if ans.lower() == "source":
		sourceDir = tempPath
	elif ans.lower() == "dest" or ans.lower() == "destination":
		destDir = tempPath
	else:
		return "Invalid option entered!\n"
	
# Displays what the current variables are set to
def displayStats():
	print("\n\x1b[1;33mFILE\x1b[0m: " + saveFile + "\n\x1b[1;33mSOURCE DIR\x1b[0m: " + sourceDir + "\n\x1b[1;33mDEST DIR\x1b[0m: " + destDir)

# Start program from main
if __name__ == '__main__':
	main()