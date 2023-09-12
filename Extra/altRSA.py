bits = 2048 # the bit length of the rsa key, must be multiple of 256 and >= 1024
E = 65537 # (default) the encryption exponent to be used [int]
from Crypto.PublicKey import RSA
key = RSA.generate(bits,E)
with open('my_key.pem','w') as file:
    file.write(key.exportKey())
    file.write(key.publickey().exportKey())