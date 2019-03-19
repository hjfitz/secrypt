from owenpki import *

# Diffie-Hellman Parameters
g = 2
p = 21182426194288297187

# Alice's Public Key
A = 36028797018963968

# Your private and public key:
B = 298981775934706214
b = 77

# And the cipher-text:
C = 5603862463347581580

# Now calculate the plain-text message 

# First, calculate the shared secret = A^b mod p
S = pow(A, b, p)

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
M_str = M_hex.decode('hex')
print('Message: {0}'.format(M_str))