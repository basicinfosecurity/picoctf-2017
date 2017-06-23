#!/usr/bin/python -u
import random,string

#~ flag = "FLAG:"+open("flag", "r").read()[:-1]
flag = "BNZQ:jn0y1313td7975784y0361tp3xou1g44"
encflag = ""
random.seed("random")
for c in flag:
	if c.islower():
		#rotate number around alphabet a random amount
		t = (ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a')
		print t
		encflag += chr(t)
	elif c.isupper():
		t = (ord(c)-ord('A')-random.randrange(0,26))%26 + ord('A')
		print t
		encflag += chr(t)
	elif c.isdigit():
		t = (ord(c)-ord('0')-random.randrange(0,10))%10 + ord('0')
		print t
		encflag += chr(t)
	else:
		print c
		encflag += c
print "Unguessably Randomized Flag: "+encflag
