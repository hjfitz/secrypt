# C-1: 25
# C-2: 13
# C-3: 16

def main():
	brute = False
	filename = input('Enter filename: ')
	shift = input('Enter shift: ')
	brute = not shift
	with open(filename) as f:
		cipher = f.read()
		if brute:
			for i in range(1,26):
				print('Shift of: ', i)
				print(''.join(list(map(lambda x: translate(x, i), cipher))))
				print('\n\n')
		else :
			transposed = ''.join(list(map(lambda x: translate(x, int(shift)), cipher)))
			print(transposed)

def translate(char, shift):
	if char.isalpha():
		return chr((((ord(char.lower()) - 97) + shift) % 26) + 97)
	return char

if (__name__ == '__main__'):
	main()