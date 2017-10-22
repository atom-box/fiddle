
# TITLE
# This is a small utility to remove lines from a file.  
# ( Really just a SED imitator. )
# Useage:  enter PYTHON3 FILESPITTER.PY <f8oehaje> <word that identifies which lines to keep.>
# by Evan Genest twitter@mistergenest Oct 10, 2017


# WISH LIST: COMMAND LINE FLAG OPTION FOR LINE BY LINE CONFIRM.   
# CONFIRM OPTION TO SHOW REGEX BEHAVIOR.  'FOUND ABC!'  'TOTAL OF XX ABC!'

#  MODULES
import sys 	# Allows argv? DeFINitely allows sys.exit
import re # allows RegEx

#  FUNCTION *asker*
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
# END ASKER FUNCTION
#   *ASKER* GETS INPUT FROM USERS THAT ENTERED NO FILE OR NO SEARCH TERM


# DECLARE
fileToOpen = ""
criticalString = ""
biggestLineWanted = 300
settings = ()
showsWords = False # enter debug mode
showsNumbers = False # enter debug mode
# FIN is file in
# FOUT is file out
# END DECLARE

# MAIN - CHECK COMMAND LINE, THEN OPEN R, W FILES
if ( (len(sys.argv) >4)  and (sys.argv[4].lower() == 'w')  ):
	showsWords = True
if ( (len(sys.argv) >4)  and (sys.argv[4].lower() == 'n')  ):
	showsNumbers = True
if len(sys.argv) > 1:
	fileToOpen = sys.argv[1]
if len(sys.argv) > 2:
	criticalString = sys.argv[2]
if len(sys.argv) > 3:
	biggestLineWanted = int(sys.argv[3])
if len(sys.argv) < 3:
	biggestLineWanted, criticalString = asker()
FOUT = open ('a.txt', 'w')
try:
	FIN = open( fileToOpen, 'r')
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

"""     JUST CHECKS LENGTHS
while True:
	furrow = FIN.readline()
	if ( '' == furrow ):
		break
	countRead += 1
	if  	(len(furrow) <  int(biggestLineWanted )  ): 
		countWrite += 1
		FOUT.write(furrow)
		if (showsNumbers): #debug mode
			print("line size is ", len(furrow), " comparing it versus ", biggestLineWanted )
			print( "success!")
	else:
		if (showsNumbers):
			print("line size is ", len(furrow), " comparing it versus ", biggestLineWanted )
			print("rejection.")
"""
wordFound = False
lengthOkay = False

while True:
	furrow = FIN.readline()
	if ( '' == furrow ):
		break
	countRead += 1
	lengthOkay = bool( len(furrow) < biggestLineWanted) # seems okay Sunday AM
	wordFound = bool( shiboleth.search( furrow ) )   #seems okay Sunday AM



	if  	( wordFound ) and (lengthOkay): # MATCH!
		countWrite += 1
		FOUT.write(furrow)
		if (showsNumbers): #debug mode
			print("line size is ", len(furrow), " comparing it versus ", biggestLineWanted )
			print( "success!")
	else:     #  NO MATCH ...
		if (showsNumbers):
			print("line size is ", len(furrow), " comparing it versus ", biggestLineWanted )
			print("rejection.")



print( "Read ", countRead, " lines." )
print( "Wrote ", countWrite, " lines." )

FOUT.close()
FIN.close()
print( 'Biggest line wanted was ', biggestLineWanted )
print ('Succesfully opened ', FIN.name )
if ( len(sys.argv) >4):
	print ( "Requested debug mode " , sys.argv[4] )

"""
#### debug voidstar
	print("Length was okay? ", lengthOkay)
	print("Word was found? ", wordFound)
	print("Peace, out.")
	sys.exit()
#### debug voidstar
"""

#  TO DO LIST:
#  todo add an example in the usage notes
# Make generally useful by having it recognize the header and footer 
# of std MOzilla bkmks, preserve them, and then pakcage the output as a nice static web page.
