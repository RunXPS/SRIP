import math
import random
from telnetlib import ENCRYPT
class gt:
    #Range for a (1,4)
    #Range for b (0,4)
    x = 0#avg of ascii values in plaintext / total of ascii values
    y = 1-x
    a = random.uniform(1,4)
    b = random.uniform(0,4)
    population = 5
    Sy = []
    Sx = []
    keyFinal = []
    linesOUT = []

    def toAscii(text):
        final = []
        for ch in range(len(text)):
            final.append(ord(text[ch]))
        return final

    def Combmap(n,a,b,Xi,Yi):
        gt.Sx.append(Xi)
        gt.Sy.append(Yi)
        for i in range(n-1):
            gt.Sx.append((gt.Sx[i] + b + (a*math.sin(2*math.pi*gt.Sy[i])))%1)
            gt.Sy.append(1 - a*(gt.Sx[i]**2) + gt.Sy[i])
        #return [gt.x, gt.y] 
    
    def score(plain,encrypted):
        union = len(plain)
        intersection = 0
        for i in plain:
            if i in encrypted:
                intersection += 1
        return 100 - (intersection/union)

    def keyGen(length,a,b):    
        gt.Combmap(length,a,b,gt.x,gt.y)
        xIndex = sorted(gt.Sx, reverse = True)
        yIndex = sorted(gt.Sy, reverse = True)
        xRand = []
        yRand = []
        for i in gt.Sx:
            xRand.append(xIndex.index(i))
        for i in gt.Sy:
            yRand.append(yIndex.index(i))
        for i in xRand:
            gt.keyFinal.append(yRand[i])
        
    def decrypt(IN,OUT,a,b,Xi,Yi):
        #File IN
        fileIN = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\{IN}.txt", "r")
        linesIN = fileIN.readlines()
        fileIN.close()
        #Variables
        length = len(linesIN)
        gt.x = Xi
        gt.y = Yi
        gt.keyGen(length,a,b)
        gt.linesOUT = []
        #Convert to numbers and decrypt
        linesIN = gt.toAscii(linesIN[0])
        for i in range(len(linesIN)):
            gt.linesOUT.append(linesIN[i]^gt.keyFinal[i])
        #Convert to char
        for i in gt.linesOUT:
            gt.linesOUT[gt.linesOUT.index(i)] = chr(i)
        #File out
        fileOUT = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\{OUT}.txt", "w+")
        fileOUT.writelines(gt.linesOUT)
        fileOUT.close()

    def encrypt(IN, OUT):
        #Take in text
        fileIN = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\{IN}.txt", "r")
        linesIN = fileIN.readlines()
        fileIN.close()
        #Variables
        length = len(linesIN[0])
        linesIN = gt.toAscii(linesIN[0])
        gt.x = (sum(linesIN)/length)/max(linesIN)
        gt.y = 1-gt.x
        gt.a = random.uniform(0,4)
        gt.b = random.uniform(1,4)
        #keyGen and Bitwise
        gt.keyGen(len(linesIN),gt.a,gt.b)
        for i in range(length):
            gt.linesOUT.append(linesIN[i]^gt.keyFinal[i])
        for i in gt.linesOUT:
            gt.linesOUT[gt.linesOUT.index(i)] = chr(i)
        #Fileout
        fileOUT = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\{OUT}.txt", "w+")
        fileOUT.writelines(gt.linesOUT)
        fileOUT.close()
    def main():
        gt.encrypt("genIN","genOUT")
        gt.decrypt("genOUT","genFinal",gt.a,gt.b,gt.Sx[0],gt.Sy[0])
gt.main()