#script to remove capitalized words
# and nonalpha




sed 's/[^A-z]/+/g' $1 |
tr '+' '\n' |
sed 's/[A-Z][A-z]*//g' |
sed '/^\ *$/d'
