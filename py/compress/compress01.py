#!/usr/bin/python

import sys

nome_file_input = sys.argv[1]

fi = open(nome_file_input,"rb") 

		
byte = byte_da_fi = fi.read(1)
molteplicita = 1

while byte_da_fi != ""  :
	
	
	if byte_da_fi == byte :
		molteplicita += 1
	else :
		
		print( byte )
		print( molteplicita )
		byte = byte_da_fi
		molteplicita = 1
	
	byte_da_fi = fi.read(1)		

fi.close()
	
