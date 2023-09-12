import random
population = 3
generations = 0

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

def genetic(length):
    score = 0
    ab = []
    while score < 95:#while score is under 90%
        for i in range(population):
            ab.append([random.uniform(1,4), random.uniform(0,4)])
            gt.keyGen(length,ab[i][0],ab[i][1])

def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a

def matMult(array):
    final = []
    mixArray = [[0x2,0x3,0x1,0x1],[0x1,0x2,0x3,0x1],[0x1,0x1,0x2,0x3],[0x3,0x1,0x1,0x2]]
    for i in mixArray:
        temp = 0
        for j in range(len(array)):
            temp ^= gmul(array[j],i[j])
        final.append(temp)
    return final
x = [0x63,0x2F,0xAF,0xA2]
x = matMult(x)
print(x)
y = []
for i in x:
    y.append(hex(i))
print(y)

z = ((0x02*0x2f)^0x2f)^(0x2*0x63)^(0x1*0xaf)^(0x1*0xA2)
z = (1*0x63)^(2*0x2f)^(1*0xa2)^234#^(((0x02*0xaf)^0xaf))

print(hex(z))

#print(0x03*0x2f)
#print((0x02*0x2f)^0x2f)
#print((0x03*0x2f)-((0x02*0x2f)^0x2f))