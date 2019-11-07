# Paragraph to csv, to make lorem ipsum

tr " " "\n" < $1 
sed '/^$/d' 
sort  
uniq 
tr "[A-Z]" 
"[a-z]" 
tr "\n" "," 
sed 's/,/, /g'
