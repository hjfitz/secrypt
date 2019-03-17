import re

# ciphertexts go here
c = [
	"07611d1e0f02076b0413031c08610a041e61061e0b111f6b091709196615040e660d0d111f61080401610d070a61080a1f",
	"1e0e1e6b0f126c0d14041d1e030f18071f61010215141f0e02610505660e0a0d6615040e6612040e0a076c180907181c071309"
]

# xor two strings of different lengths
def strxor(a, b):    
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


# probably mega inefficient but strxor() removed any bonus chars
def xorrep(cipher, attempt):
	repeated = attempt.replace('\r\n', '') * 100 
	return strxor(cipher, repeated)


# check readability (allow only alphanumeric chars and some punctiation)
def isreadable(str): 
	return bool(re.search('^[a-zA-Z0-9\., \'\"\-_\:\(\)]+$', str))

def main():
	with open("words_alpha.txt") as file:
		wordlist = file.readlines()
		print(len(wordlist))
		for idx, cipher in enumerate(c):
			print('Cipher number [{0}] - {1}'.format(idx, cipher))
			for word in wordlist:
				word = word.replace('\r\n', '')
				# check upper and lowercase
				attempt = xorrep(cipher.decode('hex'), word)
				attemptupper = xorrep(cipher.decode('hex'), word.upper())
				if isreadable(attempt):
					print('Key: [{0}] decodes to: {1}'.format(word, attempt)) # heard u like tabs
				if isreadable(attemptupper):
					print('Key [{0}] decodes to: {1}'.format(word.upper(), attemptupper))

if (__name__ == '__main__'):
	main()

