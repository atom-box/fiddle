
#!/bin/bash
if [ -z "$1" ]; then
	echo usage: $0 somefile.txt
	exit
fi
SRCd="macBeth.txt"
TGTd="./a.txt"
echo "You're bringing $SRCd and sending it to $TGTd"
cat $1 

