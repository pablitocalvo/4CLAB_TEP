#!/usr/bin/python

import sys

nome_file_input = sys.argv[1]

fi = open(nome_file_input,"rb")

byte_da_fi = fi.read(1)

while byte_da_fi !="" :
	print( byte_da_fi )
	byte_da_fi = fi.read(1)

fi.close()

