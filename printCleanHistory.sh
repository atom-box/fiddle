 sed 's_......__' myHistory.txt |
 sed 's_sudo.*__' |
 sed 's_ssh.*__'  |
 sed 's_.*ftp.*__' |
 sort |
 uniq

#########
# Purpose: Redact personal data from a BASH history listing
# Useage: 
# $ history > myHistory.txt
# $ ./printCleanHistory.sh > outfile.txt
#########