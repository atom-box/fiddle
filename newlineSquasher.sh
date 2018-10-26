# Enter a filename at commandline, this breaks the line and removes newlines and blank lines.

# Hack #1: it uses both TR and SED because SED seemingly has no ability to recognize newlines but TR seemingly cannot insert NOTHING.
# Hack #2: this will erroneously recognize the equals sign wherever it appears.

#  @MISTERGENEST

#!/bin/bash
if [ -z "$1" ]; then
	echo usage: $0 somefile.txt
	exit
fi

sed 's/^[:space:]*$//g' $1 | #blanklines>noughts
tr "\n" "=" |  #all returns to equals
sed "s/=//g" |  #remove equals
sed "s/\([,.?!]\)/\1=/g" |  # puncs > PUNC-AND-EQUAL
tr "=" "\n"   #EQUAL TO NEWLINE


