
#!/bin/bash
if [ -z "$1" ]; then
	echo Syntax for this is: $0 myfile.txt lineStart lineStop
	exit
fi

head -n $3 $1 | tail -n ($3 - $2) | sed 's/</\&lt/g' | sed 's/>/\&gt/g'

#  finish this script (look up the BASH subtraction syntax)
# go to alice server and make things nice write actual content TODAY