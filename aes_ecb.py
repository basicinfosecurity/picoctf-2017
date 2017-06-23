import sys

from base64 import b64decode
from Crypto.Cipher import AES

def main():
	passphrase = b64decode(sys.argv[2])
	msg = b64decode(sys.argv[1])
	aes = AES.new(passphrase, AES.MODE_ECB)
	print aes.decrypt(msg)
	
if __name__ == "__main__":
	exit(main())
