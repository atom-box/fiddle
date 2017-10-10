#		March 26, 2017 (April 3, 5, 8, 10.)
#		Took eight days!  My first ever file-to-twoDim-array, with dictionary in list!  
#		data input is baseball statistics
#		showcase chaps 2 through 6 with the output

#  Succesfully does 2 things:
#			prints stats for a single player
#			prints a chosen stat for all players with their positions, using DICTIONARY

# Learned: 1- its called sys.argv[0], not argv[0], requires import sys.  Or sys.exit() might require it.
# Learned: 2 calling help
# Learned: 3 Sorter was easy to write in Python
# Victory:  Quora EOF solution is straightforward
# VictoryMinor Resisting the urge to make little things work.  Plowing on WITHOUT looking up.
# Victory: When in doubt, its easy to go to interactive and do a DATA = READ(FILEPOINTER) !!!!!!!
# Victory 4/10: don't iterate as the list grows, APPEND.  NO need to index.
# Going to guineas-pig this to GIT 5/11

import sys 	# Allows argv? Definitely allows sys.exit

# returns true if x, y not in order
def unOrderedInt( x, y ):
	if x < y :
		return False
	return True

# RETURNS TRUE IF s1 s2 NOT IN ORDER
def unOrderedStr( s1, s2 ):
	shortieChars = 0
	needToSwap = False
	if ( len(s1) > len(s2) ):
		shortieChars = len(s2)
	else:
		shortieChars = len(s1)
	for i in range( 0, shortieChars ):
		print( s1[i], s2[i])
		if ( s1[i] > s2[i] ):
			needToSwap = True
			break
	if ( needToSwap == False and (len(s1) > len(s2) )):
		print( 'Tell MAIN true, so it swaps tie for shorter first')
		needToSwap = True
	return needToSwap
	""" Why not more  comments!"""

def listPrinter( list ):
	j = 0
	for i in list:
		print( str(j), '--', str(i) )
		j = j +1

# MAIN

# COMMAND LINE
if len(sys.argv) < 3:
	print('Enter two command line options')
	sys.exit()
print('User chose ' , sys.argv[1] + ' option')
if ( sys.argv[1].isnumeric() == 0  ):
	print('Useage: baseball.py player wanted , stat wanted (starting from zero lowest)')
	sys.exit()

# READ FILE INTO A COMPLEX AND LARGE LEAGUE-WIDE STRUCTURE IN MEMORY
try:
	fp = open( '/home/atom_box/Dropbox/code/data/tigers2016.csv', 'r')
except:
	print('Whoopsies...no file found!')
	sys.exit()

print ('Succesfully opened ', fp.name )

playersL = []
while True:
	line = fp.readline()
	if ( '' == line ):
		break
	playersL.append( line.split(sep=',') )


labels = playersL[0] 	# store header
del playersL[0]				# remove header
nameWants = int( sys.argv[1] ) # rename argv's to improve code readability
statWants = int( sys.argv[2] ) # make integer because will be used as list index

# Prints the asked for name AND asked for stat
print( 'User entered ', nameWants , ' and ',	statWants )

# TO DO make this dictionaryish
playersD = []
for i in range( len(playersL) ):
	lineD = {}
	for j in range( len( playersL[i] ) ):
		lineD[ labels[j] ] = playersL[i][j]
	playersD.append( lineD )
x = 3.1415
print( 'Congratulations.  Dictionary formed okay!  Proof...the second player named ', playersL[2][2], ' has these HR: ', end='' )
print( playersD[2][ 'HR' ] )

# CLEAN THE NAME, 2 LINES OF CODE:
nameFields = (playersL[nameWants][2]).split( sep='\\' )
name = nameFields[0]
print('='*5, name , '='*10 )
howManyFields = 0;
howManyFields = len(labels) - 1
# Next two lines are to force columnar printing
returnYet = 0 #  don't adjust this.  It just starts at zero and continually grows; it's an iterator
howManyColumns = 3  # adjust THIS to set how many columns you want!   

for i in 	range(howManyFields)  :
	print( '\t', labels[i] , ': ', playersL[ nameWants ][i], end='' )
	returnYet += 1
	if not ( returnYet % howManyColumns ):
		print()


# print requested stat for all players
columnBreakEvery = 3 # Set number of columns here
columnIterator = 0 # Don't change this
for i in playersD:
	print( '\t',  (i['Name'])[0:13], i['Pos']  , labels[statWants],    i[ labels[statWants ] ] , end='' )
	columnIterator += 1
	if not( columnIterator % columnBreakEvery ):
		print()
nameFields = (playersL[nameWants][2]).split( sep='\\' )
name = nameFields[0]





# Next two lines are to force columnar printing
returnYet = 0 #  don't adjust this.  It just starts at zero and continually grows; it's an iterator
howManyColumns = 3  # adjust THIS to set how many columns you want!   

for i in 	range(howManyFields)  :
	print( '\t', labels[i] , ': ', playersL[ nameWants ][i], end='' )
	returnYet += 1
	if not ( returnYet % howManyColumns ):
		print()


fp.close()

"""DevLog
#Devlog 4 10
1.  made print out use range in the FOR loop
2.  made columnar printout of player stat table
3.  multiline comment DOES work.  Demands a word on first line of comment, tho!
#Devlog 4/5 40 min.
#1. learned shebang running is chmod +x test.py
#		then ./test.py
#2.  Learned use this slash:  \ 
#		to continue on next line (tutorialspoint)
#3.  And learned if inside braces, any multiline is allowed
#4.  Didn't get a chance to try this syntax:
#		line = fo.readlines()
#		print "Read line: %s"(line)  p. 105
#Devlog 4/3  1 hr
#1. Got the splitting to fields working.  Left off while trying to build a 
#	multidimensional storer
#Devlog 3/29
#1.  wrote a func by hand to alphabetize.
#2.  Add a 'sort by field number x'  at the command line
#Devlog 3/27
#1.  using help, help(var1.split)
#2.  splitting the csv to fields
"""


