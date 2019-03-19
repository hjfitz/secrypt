from owenpki import *

def elgamal_decode(B, a, p, C):
	# First, calculate the shared secret = A^b mod p
	S = pow(B, a, p)

	# Next, calculate the inverse
	S_1 =  modinv(S, p)

	# Finally, decode the message
	M = S_1 * C % p

	# Convert the message to hex
	M_hex = hex(M)

	# Convert the message to string?
	return M_hex.replace('0x', '').replace('L', '').decode('hex')


# usage:
# print(elgamal_decode(315246492100613680079784766866257858908, 78034, 325855202898362731857657541823885506361, 72821501740447505083615864623094012061))
# elgamal_decode(their_public, our_private, prime_generator, cipher_text)