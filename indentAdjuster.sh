# USEAGE: ./indentAdjuster.sh infilename(string) factor(integer)

# This script will adjust the indenting of SPACE indented files.  If tabbed, resave your files as spaced before using this script.  To save to an outfile, use UNIX redirect at the CLI.
# FACTOR is an integer by which to multiply (+) or divide(-) the current spacing on indents
#  @MISTERGENEST

#!/bin/bash
echo ":::::::::::"
date
if [ -z "$2" ]; then
	echo Correct usage: $0 somefile.txt factor 
	echo Where FACTOR is positive or negative for multiplying or dividing the leading spaces on each line
	exit
fi

original_line_str=""
trimmed_line_str=""
original_spaces_int=0

# NOTE -LT IS LESS THAN. NOTE SEMICOLON.
if [$2 -lt 0];
then
	FACTOR_int=-1/$2
else
	FACTOR_int=$2
fi

altered_spaces_int=0


file=$1
while read line; do

echo "mush" $line $1
done < $file




# in one line grab leading spaces CAPTURE OTROS CHARS. count LEADINGS
# calculation: FACTOR,  EXISTINGSPACES,  OUTSPACES
# loop BUILD A STRING OF APPROPRIATE NUMBER OF SPACES
# outline the SPACESSTRING and the CAPTUREDSTRING

