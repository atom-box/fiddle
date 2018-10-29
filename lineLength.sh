# enter filename as commandline arg
# USEAGE: ./lineLength.sh yourFileName.txt numbOfLines
#  @MISTERGENEST

#!/bin/bash
echo ":::::::::::"
date
if [ -z "$1" ]; then
	echo usage: $0 somefile.txt numbOfLines
	exit
fi

i=1
stop=$2
while [ $i -le $stop ]
do
	head -n $i $1  | tail -n 1 | wc | sed  -e 's/\(.*\)\(.*\)\(......\)$/\3/g'  | sed 's/\ *//g'
  	((i++))
done
echo "Finished!"
date
echo ":::::::::::"

