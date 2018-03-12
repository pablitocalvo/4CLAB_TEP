#!/usr/bin/python

import sys,getopt

#nome_file = sys.argv[1]

nome_file="prova"
print (nome_file) 

blocksize = 1024
with open(nome_file,"rb") as f:
	
	while  1  : 
		byte = f.read(1)
		if byte==""  : break
		print( ord(byte) )
	
	
