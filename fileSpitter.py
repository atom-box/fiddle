
# TITLE
# This is a small utility to remove lines from a file.  
# ( Really just a SED imitator. )
# Useage:  enter PYTHON3 FILESPITTER.PY <f8oehaje> <word that identifies which lines to keep.>
# by Evan Genest twitter@mistergenest Oct 10, 2017

import sys 	# Allows argv? Definitely allows sys.exit
import re # allows RegEx

# SECTION ONE - CHECK COMMAND LINE, THEN OPEN R, W FILES
if len(sys.argv) < 3:
	print('Enter two command line options.')
	print('Usage: PYTHON3 FILESPITTER <FILENAME> <TERM PRESENT IF LINE IS TO SURVIVE>')
	sys.exit()
print('User chose ' , sys.argv[1] + ' option')
print('You said ' + sys.argv[0])
print('You said ' + sys.argv[1])
print('You said ' + sys.argv[2])
print('Is that correct?')
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
# make the regEx 
# The above regEx will test the line

#read lines from the file
while True:
	furrow = fin.readline()
	if ( '' == furrow ):
		break
	countRead += 1

	countWrite += 1
	fout.write(furrow)


print( "Read ", countRead, " lines." )
print( "Wrote ", countWrite, " lines." )

fout.close()
fin.close()
print ('Succesfully opened ', fin.name )


#  TO DO LIST:
# make the file read a line, then write that line
#  create the regex MACHINE
#  todo  syntax for a boolean 'line contains' 
