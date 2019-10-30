# This script will read a text file,
# strip its punctuation and
# proper nouns (if capitalized)
# and empty lines.
# It will output all of the words,
# and append NEWLINE after each word.
# I use it as a preprocessor before
# https://www.wordclouds.com/ 

if [ -z "$1" ]; then
	echo You must specify a file name. 
	echo Please type a filename as a command line argument.
	exit
fi


sed 's/[^A-z]/+/g' $1 |
tr '+' '\n' |
sed 's/[A-Z][A-z]*//g' |
sed '/^\ *$/d'
