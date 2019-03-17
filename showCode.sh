
#!/bin/bash
if (($# < 3)); then
	echo
	echo ----UNCOOL SYNTAX -----
	echo You gave $# arguments.  Function expects three arguments.
	echo ----YOU GIVE ME-----
	echo Better syntax would be similar to: $0 myfile.HTML! lineStart lineStop
	echo ----I GIVE YOU -----
	echo Your requested lines of html will have all problematic angle brackets replaced with a displayable symbol.
	echo
	exit
fi

# Syntax to remember: DOUBLE parens, no dollar sign until dereferencing
((SPAN = $3 - $2))
# Syntax you never knew $# is the length of args array   --devnotes
head -n $3 $1 | tail -n $SPAN | sed 's/</\&lt/g' | sed 's/>/\&gt/g'

# go to alice server and make things nice write actual content TODAY