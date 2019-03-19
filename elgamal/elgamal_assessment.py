from owenpki import *

# The group (in decimal)
g = 2 #(generator)
p = 325855202898362731857657541823885506361
# Your public and private key (in decimal)
a = 78034
A = 267713271561576086494922371249863614351
# Bob's public key (in decimal)
B = 315246492100613680079784766866257858908

# The message is an ASCII string (a dictionary word). 
# Once you think you've reversed the ElGamal encryption, convert the number to hexadecimal 
# and then convert every two numbers to their respective ASCII characters to get the message. 
# e.g., if your plaintext is 448378203247, that number in hex is 68656c6c6f and so 68 is h in ASCII, 65 is e, etc spelling 'hello'

C = 72821501740447505083615864623094012061

# To calculate the modular inverse, you can use the modinv() function from the owenpki.py python library in the RSA lab.

# Now calculate the plain-text message 

# First, calculate the shared secret = A^b mod p
S = pow(B, a, p)

print('S: {0}'.format(S))

# Next, calculate the inverse
S_1 =  modinv(S, p)
print('S_1: {0}'.format(S_1))

# Finally, decode the message
M = S_1 * C % p
print('Message (int): {0}'.format(M))

# Convert the message to hex
M_hex = hex(M)
print('Message (hex): {0}'.format(M_hex))

# Convert the message to string?
M_str = M_hex.replace('0x', '').replace('L', '').decode('hex')
print('Message: {0}'.format(M_str))