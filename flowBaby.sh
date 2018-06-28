# Thanks, http://tldp.org/howto for the syntax help

#!/bin/bash
if [ -z "$1" ]; then
	echo usage: $0 somefile.txt
	exit
fi
SRCd=$1
TGTd="./a.txt"
sed 's/a/-/g' SRCd > TGTd

