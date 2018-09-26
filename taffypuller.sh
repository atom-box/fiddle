echo "start"
date
i=0
while [ $i -le $2 ]
do
	cat $1 >> b.out
	echo $i
	((i++))
done
echo "end"
date
# trivial test comment