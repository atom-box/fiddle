# USEAGE: ./indentAdjuster.sh infilename(string) factor(integer)

# This script will adjust the indenting of SPACE indented files.  If tabbed, resave your files as spaced before using this script.  To save to an outfile, use UNIX redirect at the CLI.
# FACTOR is an integer by which to multiply (+) or divide(-) the current spacing on indents
#  @MISTERGENEST

#!/bin/bash
echo ":::::::::::"
date

# PRINT READOUT OF LEADING SPACES, rest OF LINE REMOVED
sed 's_\ _=_g' $1 

# in one line grab leading spaces CAPTURE OTROS CHARS. count LEADINGS
# calculation: FACTOR,  EXISTINGSPACES,  OUTSPACES
# loop BUILD A STRING OF APPROPRIATE NUMBER OF SPACES
# outline the SPACESSTRING and the CAPTUREDSTRING
