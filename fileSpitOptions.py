
# TITLE
# This is a small utility to remove lines from a file.  
# ( Really just a SED imitator. )
# Useage:  enter PYTHON3 FILESPITTER.PY <f8oehaje> <word that identifies which lines to keep.>
# by Evan Genest twitter@mistergenest Oct 10, 2017

import sys 	# Allows argv? Definitely allows sys.exit
import re # allows RegEx

# This function gives a menu in response to what was
# entered or not entered on the command line.  
#


#  FUNCTION TO GET INPUT FROM USERS THAT ENTERED NO FILE OR NO SEARCH TERM
def asker():
	temp = ""
	maxLine = ""
	searchTerm = ""
	if ( len(sys.argv) == 1 ): # user entered not even a file name
		print('Please enter a file name from the command line and try again.')
		sys.exit()
	#  Ask for input: line size?
	print('Reject lines longer than? (Recommended is 160.)')
	while ( False == maxLine.isnumeric() ):
		maxLine = input()
		if ( False == maxLine.isnumeric()  ):
			print("Please enter an integer")
	print('Search term? (Lines will only be copied if they include this term.)')
	while ( "" == searchTerm ):
		searchTerm = input()
		if (  "" == searchTerm   ):
			print("Please enter a search term.")
	return maxLine, searchTerm




# declare some variables
fileToOpen = ""
criticalString = ""
biggestLineWanted = 10000
settings = ()


# SECTION ONE - CHECK COMMAND LINE, THEN OPEN R, W FILES
if len(sys.argv) > 1:
	fileToOpen = sys.argv[1]
if len(sys.argv) > 2:
	criticalString = sys.argv[2]
if len(sys.argv) < 3:
	biggestLineWanted, criticalString = asker()

fout = open ('a.txt', 'w')
try:
	fin = open( fileToOpen, 'r')
except:
	print('Whoopsies...no file found!')
	sys.exit()
#  END ONE ###



#   SECTION TWO - READ A LINE AT A TIME, REGEX TEST FOR 'THE WORD', WRITE TO 2ND FILE
furrow = "" # holds 'a row' of file line.  Get it?
countRead = 0
countWrite = 0
shiboleth = re.compile(criticalString) # make the regEx 
# The above regEx will test the line

#read lines from the file, check vs RegEx ('SHIBOLETH'), then write to FOUT
print("Will include any lines from file [", fileToOpen, "]")
print("that include the search term [", criticalString, "]")
print("and are smaller than [", biggestLineWanted, "] characters.")


while True:
	furrow = fin.readline()
	if ( '' == furrow ):
		break
	countRead += 1
	if ( shiboleth.search(furrow) and
		(len(furrow) < biggestLineWanted)
		): 
		countWrite += 1
		fout.write(furrow)

print( "Read ", countRead, " lines." )
print( "Wrote ", countWrite, " lines." )

fout.close()
fin.close()
print ('Succesfully opened ', fin.name )


#  TO DO LIST:
#  todo  change printout order a bit
#  todo print the outfile name
#  todo add an example in the usage notes