    def iterative(a,b):
        remainder = 0
        while b != 0:
            remainder = a%b
            a = b
            b = remainder
        return a
    
    def recursive(a,b):
        if b == 0:
            return a
        else:
            return RSA.recursive(b,a%b)

d = ((T)+1)/e
        i = 0
        while d%1 != 0.0:
            i += 1
            d = ((T*i)+1)/e
        #print(d)

    sdef toHex(string):
        #addition = []
        for i in range(len(string)):
            AES.linesIN.append(hex(ord(string[i])))
        #AES.linesIN.append(addition)
    
    def fromHex(array):
        for i in range(len(array)):
            #array[i] = chr(int(array[i],16))
            array[i] = int(array[i],16)
        return array