
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
def askWhichMode():
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

	"""
	userSays = raw_input('Enter a number: ')
	try:
		maxLine = int(userSays)
	except:
		print ("Using default; lines longer than 160 will be ignored.")
		maxLine = 160
	print('Enter search term that all retained lines should have.')
	searchTerm = input()
  return 5
	"""	


# declare some variables
criticalString = ""
biggestLineWanted = 10000
settings = ()



# SECTION ONE - CHECK COMMAND LINE, THEN OPEN R, W FILES
if len(sys.argv) != 4:
	biggestLineWanted, criticalString = askWhichMode() 

fout = open ('a.txt', 'w')
try:
	fin = open( sys.argv[1], 'r')
except:
	print('Whoopsies...no file found!')
	sys.exit()
#  END ONE ###



#   SECTION TWO - READ A LINE AT A TIME, REGEX TEST FOR 'THE WORD', WRITE TO 2ND FILE
furrow = "" # holds 'a row' of file line.  Get it?
countRead = 0
countWrite = 0
soughtWord = sys.argv[2]
shiboleth = re.compile(soughtWord) # make the regEx 
# The above regEx will test the line

#read lines from the file, check vs RegEx ('SHIBOLETH'), then write to FOUT
while True:
	furrow = fin.readline()
	if ( '' == furrow ):
		break
	countRead += 1
	if ( shiboleth.search(furrow) ): 
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