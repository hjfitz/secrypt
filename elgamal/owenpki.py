# Gareth Owen, gareth.owen@port.ac.uk, University of Portsmouth
# RSA / Public Key utility functions

import random

# fermat - probably prime - false positive less than 2^-60
def isPrime(p, a=2):
    if(p==2): return True
    if(not(p&1)): return False
    return pow(a,p-1,p)==1

# get prime +/- 1 bit of desired bits
def getPrime(bits):
    global rnd
    while True:
        # uses os.urandom() - should be cryptographically secure
        rnd = random.SystemRandom().getrandbits(bits+1)
        if rnd < 2**(bits-1): #avoid numbers too small
            continue
        if rnd & 1 == 0:  # if not odd, let's make it odd
            rnd += 1
        if isPrime(rnd):  #got a potential prime
            fail = False
            for i in range(10):   # check with different bases
                a = random.randint(2,rnd-1)
                if not isPrime(rnd, a):
                    fail = True
                    print "[note] Candidate Prime (",rnd,") failed second safety check (a=",a,") - searching for a new prime"
                    break
            if fail:
                continue
            return rnd #probably a prime

def findPrimes(x):
  return filter(isPrime, xrange(2,x))

# extended Euclidean Algorithm
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

# modular inverse, find ? such that a*?=1 mod m
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

# generate, test and output an RSA key
def genKey(bits):
    p = getPrime(bits)
    q = p
    while q==p:
        q = getPrime(bits)

    n = p*q
    phin = (p-1)*(q-1)
    e=65537
    d=modinv(e, phin)

    print "p=",p
    print "q=",q
    print "n=",n
    print "phin=",phin
    print "e=",e
    print "d=",d
    for i in range(2,min(500,n-1)):
        testEncDec = pow(i, e*d, n)
        if testEncDec != i:
            print "Checked encryption / decryption [FAILED***]: ",i
            break

#genKey(16)
#print findPrimes(1900)

#Diffe Hellman implementation
#p = getPrime(1024)
#print "Prime length ", len(str(p)), " digits"
#g = 5
#a=random.randint(2**500, 2**512) #Alice's PrivKey
#print "A length ", len(str(a)), " digits"
#b=random.randint(2**500, 2**512) #Bob's PrivKey
#print "B length ", len(str(b)), " digits"
#
#A = pow(g, a, p) #Alice's PubKey
#B = pow(g, b, p) #Bob's PubKey
#
#x = pow(B, a, p) #Alice calc shared secret
#y = pow(A, b, p) #Bob calc shared secret
#
#print "Shared Secret (ALICE): ",hex(x)
#print "Shared Secret (BOB): ",hex(y)
#if x != y:
#    print "Something went wrong :-("
#
