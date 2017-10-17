
# TITLE
# This is a small utility to remove lines from a file.  
# ( Really just a SED imitator. )
# Useage:  enter PYTHON3 FILESPITTER.PY <f8oehaje> <word that identifies which lines to keep.>
# by Evan Genest twitter@mistergenest Oct 10, 2017

import sys 	# Allows argv? Definitely allows sys.exit
import re # allows RegEx

def askWhichMode():
	if ( len(sys.argv) < 2 ): # user entered not even a file name
		print('User did not enter correct command line arguments.')
		print('Please re-start, with correct syntax.')
		print('Manual Mode\ncommand line syntax: PYTHON3 FILESPIT <FILENAME> <criterion word> <maximum line length wanted>')
		print('Prompt Mode\ncommand line syntax: PYTHON3 FILESPIT <FILENAME>')
	if ( len(sys.argv) = 2 ): # user entered not even a file name
		
		print('Do you wish to run with prompts (y/n)')

	print('User chose ' , sys.argv[1] + ' option')


criticalString = ""
biggestLineWanted = 10000
settings = ()
settings.push(criticalString, biggestLineWanted) # initialize with defaults

# SECTION ONE - CHECK COMMAND LINE, THEN OPEN R, W FILES
if len(sys.argv) != 4:
	answeredWhichMode = False # initialize
	userWantsQuit = askWhichMode() # function will ask user to confirm 'prompt mode'
	if ( userWantsQuit ):
		sys.exit()

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