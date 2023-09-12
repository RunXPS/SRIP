import math
import random
import time
class gt:
    x = 0
    y = 0
    a = random.uniform(1,4)
    b = random.uniform(0,4)
    initialX = 0
    initialY = 0
    length = 0
    fileIN = None
    fileOut = None
    linesIN = []
    linesOUT = []

    def Combmap(n,a,b,Xi,Yi):
        Sx = []
        Sy = []
        Sx.append(Xi)
        Sy.append(Yi)
        for i in range(n-1):
            Sx.append((Sx[i] + b + (a*math.sin(2*math.pi*Sy[i])))%1)
            Sy.append(1 - a*(Sx[i]**2) + Sy[i])
        return [Sx, Sy]
    
    def score(plain,encrypted):
        pbit = plain
        ebit = encrypted
        pbit = set(pbit)
        ebit = set(ebit)
        intersection = (pbit & ebit)
        union = (pbit|ebit)
        return 100 - (len(intersection)/len(union))

    def keyGen(a,b):    
        S = gt.Combmap(gt.length,a,b,gt.x,gt.y)
        keyFinal = []
        xIndex = sorted(S[0], reverse = True)
        yIndex = sorted(S[1], reverse = True)
        xRand = []
        yRand = []
        for i in S[0]:
            xRand.append(xIndex.index(i))
        for i in S[1]:
            yRand.append(yIndex.index(i))
        for i in xRand:
            keyFinal.append(yRand[i])
        return keyFinal
    
    def rotate(array, n):
        return array[n:] + array[:n]
    
    def mutation(set):
        for pair in set:
            if random.randint(1,1000) == 1:
                set.append([random.uniform(-0.2,0.2), random.uniform(-0.2,0.2)])
        return set
    
    def newGen(population, parent):
        #print(parent)
        child = []
        for _ in range((population - len(parent)) // 2):
            parent1 = random.choice(parent)
            parent2 = random.choice(parent)
            child.append([parent1[0],parent2[1]])
            child.append([parent2[0],parent1[1]])
        return child

    def genetic(population):
        ab = []
        percent = int(population*.2)
        threshhold = 99
        generation = 1
        
        #Initial population
        for i in range(percent):
            ab.append([random.uniform(1,4), random.uniform(0,4)])

        #Generations
        while True:
            #Generate pairs of AB
            ab = gt.newGen(population, ab)
            for i in ab:
                gt.a = i[0]
                gt.b = i[1]
                i.append(gt.keyGen(gt.a,gt.b))
                gt.encrypt(i[2])
                nums = []
                for j in range(len(gt.linesOUT)):
                    nums += (gt.toAscii(gt.linesOUT[j]))
                ab[ab.index(i)].append(gt.score(gt.linesIN,nums))
                if len(i)>=4:
                    ab[ab.index(i)] = i[:4]
            
            for i in range(len(ab)):
                ab[i] = gt.rotate(ab[i],3)
            ab.sort(reverse = True)
            ab = ab[:percent]
            if ab[0][0] >= threshhold:
                break
            for i in range(len(ab)):
                ab[i] = gt.rotate(ab[i],1)
                ab[i] = ab[i][:2]
        return(ab[0])
        

########################################################################
                        #VVV Mess with Text VVV#                        
    
    def toAscii(text):
        final = []
        for ch in range(len(text)):
            final.append(ord(text[ch]))
        return final

    def takeIn(IN):
        gt.fileIN = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\GeneticText\\{IN}.txt", "r")
        gt.linesIN = gt.fileIN.readlines()
        gt.fileIN.close()
        #temp = []
        #for i in gt.linesIN:
            #temp.append(gt.toAscii(i))
        #gt.linesIN = temp
        gt.linesIN = gt.toAscii(gt.linesIN[0])
        gt.length = len(gt.linesIN)
        gt.x = (sum(gt.linesIN)/gt.length)/max(gt.linesIN)
        gt.y = 1-gt.x
        gt.initialX = gt.x
        gt.initialY = gt.y
    
    def putOut(OUT):
        gt.fileOUT = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\GeneticText\\{OUT}.txt", "w+")
        gt.fileOUT.writelines(gt.linesOUT)
        gt.fileOUT.close()
        gt.linesOUT = []
        gt.linesIN = []

    def decrypt(key,Xi,Yi):
        #Variables
        gt.x = Xi
        gt.y = Yi
        #Convert to numbers and decrypt
        for i in range(len(gt.linesIN)):
            gt.linesOUT.append(gt.linesIN[i]^key[i])
        #Convert to char
        for i in gt.linesOUT:
            gt.linesOUT[gt.linesOUT.index(i)] = chr(i)
    
    def encrypt(key):
        #Variables
        gt.linesOUT = []
        #keyGen and Bitwise
        for i in range(gt.length):
            gt.linesOUT.append(gt.linesIN[i]^key[i])
        #To char
        for i in gt.linesOUT:
            gt.linesOUT[gt.linesOUT.index(i)] = chr(i)
    
    def main():
        gt.takeIn("genIN")
        everything = gt.genetic(100)
        key = everything[3]
        #Encrypt       
        gt.takeIn("genIN")
        gt.encrypt(key)
        gt.putOut("genOUT")
        #Decrypt
        gt.takeIn("genOUT")
        gt.decrypt(key,gt.initialX,gt.initialY)
        gt.putOut("genFinal")
        return
        file = "thousand"
        times = ""
        for i in range(1):
            gt.takeIn(file)
            timing = time.time()
            everything = gt.genetic(100)
            key = everything[3]
            #Encrypt       
            #gt.takeIn(file)
            gt.encrypt(key)
            timing = time.time()-timing
            times += str(timing) + " "
        print(times)
gt.main()