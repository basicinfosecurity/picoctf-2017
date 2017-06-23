import fractions
import sys

#~ from math import gcd as bltin_gcd

def phi(x, y):
	amount = 0

	#~ for k in range(1, x*y + 1):
	for k in xrange(1, x*y + 1):
		if fractions.gcd(x*y, k) == 1:
			amount += 1
	return amount
	
def lcm(x, y):
	if x > y:
		greater = x
	else:
		greater = y
		
	while(True):
		if((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break
		greater += 1
	return lcm

def coprime(n):
	tmp = list()
	for k in range(1, n):
		if fractions.gcd(k, n) == 1:
			tmp.append(k)
	return tmp
	
def mmi(l, c):
	return pow(c, l-1, l)

def main():
	x = int(sys.argv[1])
	y = int(sys.argv[2])
	msg = int(sys.argv[3])
	#~ enc = int(sys.argv[3])
	p = phi(x, y)
	l = lcm(x -1, y -1)
	c = coprime(l)
	#~ c = 17
	print 'totient %s' %p
	print 'lcm %s ' % l
	print 'coprime %s' % c
	for i in c:
		m = mmi(l, i)
		enc = encrypt(msg, i, x * y)
		dec = decrypt(enc, m, x * y)
		print 'mmi %s' % m
		print 'encrypted %s' % enc
		print 'decrypted %s' % dec
	
def encrypt(msg, c, n):
	return msg**c % n
	
def decrypt(enc, m, n):
	return enc**m % n

if __name__ == "__main__":
	exit(main())
