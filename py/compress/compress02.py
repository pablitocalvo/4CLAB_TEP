#!/usr/bin/python

import sys

nome_file_input = sys.argv[1]
nome_file_output= nome_file_input + ".compress"

fo = open(nome_file_output,"wb")

with open(nome_file_input,"rb") as fi:

		
	byte = byte_da_fi = fi.read(1)
	molteplicita = 1
	
	while byte_da_fi != ""  :
		
		
		if byte_da_fi == byte :
			molteplicita += 1
		else :
			
			fo.write(byte)
			fo.write(chr(molteplicita))
			byte = byte_da_fi
			molteplicita = 1
		
		byte_da_fi = fi.read(1)		


	fi.close()
	fo.close()
	
