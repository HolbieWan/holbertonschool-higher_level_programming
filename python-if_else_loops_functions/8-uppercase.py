#!/usr/bin/python3
c = "test"
def uppercase(str):
	if (ord(c) > 96 and ord(c) < 123):
		c = chr(ord(c) - 32)
	print("{}" .format(c))
