import random
import math
from math import gcd
from MillerRabin import is_probable_prime
import time
class RSA:
    public = []
    private = []
    timing = ""

    def toAscii(text):
        final = []
        for ch in range(len(text)):
            final.append(ord(text[ch]))
        return final
    
    #Extended Euclidean Algorithm
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = RSA.egcd(b % a, a)
            return (g, x - (b // a) * y, y)
    
    #Solving for D?
    def modinv(e, n):
        g, x, y = RSA.egcd(e, n)
        if g != 1:
            return ''
        else:
            return x % n
    
    def encrypt(num):
        return pow(num, RSA.public[1], RSA.public[0])
    
    def decrypt(num):
        return pow(num, RSA.private[1], RSA.private[0])

    def GenKeys(selection):
        #Adapting bits
        options = [10,100,1000]
        bits = options[int(selection)]

        #Variables
        p = random.getrandbits(bits)
        q = random.getrandbits(bits)
        while is_probable_prime(p) == False:
            p = random.getrandbits(bits)
        while is_probable_prime(q) == False:
            q = random.getrandbits(bits)
        N = p*q
        T = (p-1)*(q-1)
        sample = []

        #Personal Additions to algorithm. Compresses options for keys
        if bits != 10:
            skip = random.randint(pow(bits,3),pow(bits,4))
        else:
            skip = 1
        
        #Makeshift for loop?
        i = 3
        while i < T and len(sample) < 20:
            if is_probable_prime(i):
                if math.gcd(i,T) == 1 and math.gcd(i,N) == 1:
                    sample.append(i)
            i = i+skip
        e = sample[random.randint(0,len(sample)-1)]
        d = RSA.modinv(e,T)*random.randint(1,skip)
        RSA.public = [N,e]
        RSA.private = [N,d]

    def cipher(option, textIN, textOUT):
        fileIN = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\{textIN}.txt", "r")
        linesIN = fileIN.readlines()
        fileIN.close()
        
        times = time.time()

        linesIN = RSA.toAscii(linesIN[0])
        RSA.GenKeys(option)
        
        linesOUT = []
        for i in linesIN:
            x = RSA.encrypt(i)
            linesOUT.append(str(x)+" ")
        
        times = time.time()-times
        RSA.timing += str(times) + " "
        
        fileOUT = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\Quadratic-Sieve-Algorithm-master\\src\\{textOUT}.txt", "w+")
        fileOUT.writelines(linesOUT)
        fileOUT.close()

    def decipher(key1, key2, textIN, textOUT):
        RSA.public = key1
        RSA.private = key2
        fileIN = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\Quadratic-Sieve-Algorithm-master\\src\\{textIN}.txt", "r")
        linesIN = fileIN.readlines()
        fileIN.close()
        linesIN = linesIN[0].split(" ")
        linesOUT = ""
        for i in linesIN:
            if i.isdigit():
                x = RSA.decrypt(int(i))
                linesOUT += chr(x)
        fileOUT = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\Quadratic-Sieve-Algorithm-master\\src\\{textOUT}.txt", "w+")
        fileOUT.writelines(linesOUT)
        fileOUT.close()
    def main():
        bits = 0#input("Enter option: ")
        textIN = "tenThousand"#input("Enter text in name: ")
        textOUT = "tenOUT"#input("Enter text out name: ")
        textFinal = "test"
        for i in range(100):
            RSA.cipher(bits, textIN, textOUT)
        print(RSA.timing)
        #RSA.decipher(RSA.public, RSA.private, textOUT, textFinal)
RSA.main()