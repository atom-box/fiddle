# Enter a filename at commandline, this breaks the line 
# just for commas.

#  @MISTERGENEST

#!/bin/bash
if [ -z "$1" ]; then
	echo usage: $0 somefile.txt
	exit
fi
tr "\(,:;!.?\)" "\1\n" < $1
