echo "Begin..."
echo "clear" > dogtown.csv
date
x=0
while [ $x -le 200 ]
do
	echo "apples, peaches, pumpkin pie, Green Day, limestone, travertine, doctor, lawyer, indian chief, sherman alexie, philip roth, henry aaron, o henry, baby ruth" >> dogtown.csv
	date | tr ' :' ',' >> dogtown.csv
	ls -lrt | tr ' '  ',' >> dogtown.csv
	((x++))
done
echo "Finished!"
date
