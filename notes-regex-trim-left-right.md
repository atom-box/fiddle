# This will take a list and winnow it to a single alpha word from its interior
Not optimized.  Worked on January 9, 2021.
## TRIM LINE NUMBERS AND SPACES FROM LEFT
`cat notes-TESTING-every-Assert-in-DOI.txt | sed 's_[0-9]\+[\ :]\+[\ :]\+\(.*\)_\1_' | sort  > ASSERT-cleaned-list-DOI.txt`
## FURTHER TRIM LEFT UP UNTIL EXACT STRING "assert" BEGINS
`cat ASSERT-cleaned-list-DOI.txt  |  sed 's_.*->\(assert.*\)_\1_' | sort  >  ASSERT-1000sorted-raggedrightmargin.txt`
## GIMME NOTHIN BUT A SINGLE "WORD"
`cat ASSERT-1000sorted-raggedrightmargin.txt   |  sed 's_\([[:alpha:]]\+\)(.*_\1_'     |  sort |  uniq  > ASSERT-3000-verbs-allTrimmed.txt`
