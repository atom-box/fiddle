 sed 's_......__' history2000.txt | sed 's_sudo.*__' | sed 's_ssh.*__' | sed 's_.*ftp.*__' | sort | uniq
