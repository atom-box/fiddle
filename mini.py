
# noNewLines.py  
# A pre-processor to strip (1) whitespace and (2) newlines if given a text file.  
# Useage:  enter PYTHON3 FILESPITTER.PY <f8oehaje> <word that identifies which lines to keep.>
# Infile.txt can be any text file
# Outfile.txt will be a monoline, with no tabs or spaces
# by Evan Genest twitter@mistergenest Oct 10, 2017



#  MODULES
import sys 	# Allows argv? DeFINitely allows sys.exit
import re # allows RegEx

#  FUNCTION *asker*
def starting():
	temp = ""
	maxLine = ""
	searchTerm = ""
	if ( len(sys.argv) == 1 ): # user entered not even a file name
		print('Please enter a file name from the command line and try again.')
		sys.exit()
	# #  Ask for input: line size?
	# print('Reject lines longer than? (Recommended is 160.)')
	# while ( False == maxLine.isnumeric() ):
	# 	maxLine = input()
	# 	if ( False == maxLine.isnumeric()  ):
	# 		print("Please enter an integer")
	# print('Search term? (Lines will only be copied if they include this term.)')
	# while ( "" == searchTerm ):
	# 	searchTerm = input()
	# 	if (  "" == searchTerm   ):
	# 		print("Please enter a search term.")
	return 
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

starting()
FOUT = open ('a.txt', 'w')
fileToOpen = sys.argv[1]
print('Opening ', fileToOpen)
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
print("Now opening ", fileToOpen)


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
