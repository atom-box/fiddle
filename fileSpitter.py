
# MAIN
# Utility to remove lines
# Useage:  enter PYTHON3 FILESPITTER.PY <f8oehaje> <word that identifies which lines to keep.>

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