
# MAIN
# Utility to remove lines
# Useage:  enter PYTHON3 FILESPITTER.PY <f8oehaje> <word that identifies which lines to keep.>


import sys 	# Allows argv? Definitely allows sys.exit

if len(sys.argv) < 3:
	print('Enter two command line options.')
	print('Usage: PYTHON3 FILESPITTER <FILENAME> <TERM PRESENT IF LINE IS TO SURVIVE>')
	sys.exit()
print('User chose ' , sys.argv[1] + ' option')

print('You said ' + sys.argv[0])
print('You said ' + sys.argv[1])
print('You said ' + sys.argv[2])
print('Is that correct?')

# READ FILE INTO A COMPLEX AND LARGE LEAGUE-WIDE STRUCTURE IN MEMORY
fout = open ('a.txt', 'w')
try:
	fin = open( sys.argv[1], 'r')
except:
	print('Whoopsies...no file found!')
	sys.exit()
fout.close()
fin.close()
print ('Succesfully opened ', fin.name )