import time
class AES:
    Rcon = [ 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a ]
#    mixArray = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
#    mixArray_inv = [[0xe,0xb,0xd,0x9],[0x9,0xe,0xb,0xd],[0xd,0x9,0xe,0xb],[0xb,0xd,0x9,0xe]]

    SboxSide = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    Sbox = [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
            [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
            [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
            [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
            [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
            [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
            [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
            [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
            [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
            [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
            [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
            [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
            [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
            [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
            [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
            [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
            ]
    Sbox_inv = [[0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
            [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
            [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
            [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
            [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
            [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
            [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
            [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
            [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
            [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
            [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
            [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
            [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
            [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
            [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
            [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
            ]
    
    fileIN = ""
    fileOUT = ""
    linesIN = []
    linesOUT = []
    key = []

    def rotate(array, n):
        return array[n:] + array[:n] 
    #Initialize
    def toAscii(text):
        final = []
        for ch in range(len(text)):
            final.append(ord(text[ch]))
        return final
    def makeBlocks(array):
        block = [[],[],[],[]]
        complete = []
        for i in range(len(array)):
            block[i%4].append(array[i])
            if i%16 == 15:# and i != 0:
                complete.append(block)
                block = [[],[],[],[]]
        return complete
    #Substitute Bytes
    def subBytes(value, encrypted):
        #x determines row
        #y determines column
        if len(value) == 3:
            x = AES.SboxSide.index('0')
            y = AES.SboxSide.index(value[2])
        elif len(value) > 4:
            print(value)
        else:
            x = AES.SboxSide.index(value[2])
            y = AES.SboxSide.index(value[3])
        
        if encrypted:
            return AES.Sbox[x][y]
        else:
            return AES.Sbox_inv[x][y]
    #Shift Rows
    def shiftRows(block, encrypted):
        if encrypted:
            for i in range(3):
                block[i+1] = AES.rotate(block[i+1], i+1)
        else: 
            for i in range(3):
                block[i+1] = AES.rotate(block[i+1], i-1)
        return block
    #Mix columns
    def gmul(a, b):
        if b == 1:
            return a
        tmp = (a << 1) & 0xff
        if b == 2:
            return tmp if a < 128 else tmp ^ 0x1b
        if b == 3:
            return AES.gmul(a, 2) ^ a
    def matMult(array, encryption):
        final = []
        mixArray = [[0x2,0x3,0x1,0x1],[0x1,0x2,0x3,0x1],[0x1,0x1,0x2,0x3],[0x3,0x1,0x1,0x2]]
        for i in mixArray:
            temp = 0
            for j in range(len(array)):
                temp ^= AES.gmul(array[j],i[j])
            final.append(temp)
        return final
    #Inverse Mix Columns
    def inv_mix_columns(s):
        # learned from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c
        xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)
        print(s)
        # see Sec 4.1.3 in The Design of Rijndael
        for i in range(4):
            u = xtime(xtime(s[i][0] ^ s[i][2]))
            v = xtime(xtime(s[i][1] ^ s[i][3]))
            s[i][0] ^= u
            s[i][1] ^= v
            s[i][2] ^= u
            s[i][3] ^= v

        AES.matMult(s)
    #Add Round Key
    def keyGen(original, round, encrypted):
        #print(round)
        g = original[3]
        #Byte shift
        g = AES.rotate(g, 1)
        #Byte substitution
        for j in range(4):
            g[j] = AES.subBytes(hex(g[j]),encrypted)
        #Adding round constant
        g[0] ^= AES.Rcon[round]
        #Adding to Key
        for i in range(len(original)):
            temp = []
            for j in range(4):
                if i == 0:
                    temp.append(original[i][j]^g[j])
                else:
                    temp.append(AES.key[i-1][j]^original[i][j])
            AES.key.append(temp)

#Handling input/output
    def takeIn(IN, encrypt):
        AES.fileIN = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\{IN}.txt", "r")
        AES.linesIN = AES.fileIN.readlines()
        AES.fileIN.close()
        AES.linesIN = AES.linesIN[0]
        if encrypt:
            if len(AES.linesIN)%16 != 0:
                for i in range(16-len(AES.linesIN)%16):
                    AES.linesIN += " "
        else:
            AES.linesIN = AES.linesIN.split(" ")
            print(AES.linesIN)
            AES.linesIN = AES.linesIN[:len(AES.linesIN)-1]
            print(AES.linesIN)
        
    def putOut(OUT):
        AES.fileOUT = open(f"C:\\Users\\Ryan Krasinski\\2122\\SRIP\\AES\\{OUT}.txt", "w")
        #for i in AES.linesOUT:
        #    AES.fileOUT.writelines(i)
        AES.fileOUT.writelines(AES.linesOUT)
        AES.fileOUT.close()
        AES.linesOUT = []
        AES.linesIN = []
    
    def encrypt(text):
        #Prep Text
        AES.linesIN = AES.toAscii(text)
        AES.linesIN = AES.makeBlocks(AES.linesIN)
        #Divide blocks
        for h in range(len(AES.linesIN)):
            current = AES.linesIN[h]
        #Start Rounds
            for i in range(16):
                #Round 0
                if i == 0:
                    AES.keyGen(current, i, True)
                    final = []
                    for j in range(4):
                        temp = []
                        for k in range(4):
                            temp.append(AES.key[j][k]^current[j][k])
                        final.append(temp)
                    current = final
                #Round 1+
                else:
                    #Substitute Bytes
                    final = []
                    for j in range(4):
                        temp = []
                        for k in range(4):
                            temp.append(int(AES.subBytes(hex(current[j][k]),True)))
                        final.append(temp)
                    current = final
                    #Shift Rows
                    current = AES.shiftRows(current, True)
                    #Shift Columns
                    if round != 15:
                        temp = []
                        for l in current:
                            temp.append(AES.matMult(l,True))
                        current = temp
                    #Add Round Key
                    AES.keyGen(current, i, True)
                    final = []
                    for j in range(4):
                        temp = []
                        for k in range(4):
                            temp.append(AES.key[j][k]^current[j][k])
                        final.append(temp)
                    current = final
            #Add to linesOUT
            final = []
            for j in range(4):
                for k in range(4):
                    final.append(hex(current[j][k]) + " ")
            AES.linesOUT.append(final)

    def decrypt(text):
        #Prep text
        for i in range(len(AES.linesIN)):
            AES.linesIN[i] = int(AES.linesIN[i],16)
        AES.linesIN = AES.makeBlocks(AES.linesIN)
        #Divide blocks
        for h in range(len(AES.linesIN)):
            current = AES.linesIN[h]
            #Start Rounds
            for i in range(16):
                #For Round 0
                if i == 0:
                    AES.keyGen(current, i, False)
                    final = []
                    for j in range(4):
                        temp = []
                        for k in range(4):
                            temp.append(AES.key[j][k]^current[j][k])
                        final.append(temp)
                    current = final
                #For round 1+
                else:
                    #Shift rows
                    current = AES.shiftRows(current, False)
                    #Sub Bytes
                    final = []
                    for j in range(4):
                        temp = []
                        for k in range(4):
                            temp.append(int(AES.subBytes(hex(current[j][k]),False)))
                        final.append(temp)
                    current = final
                    #Mix Columns
                    if round != 15:
                    #    temp = []
                    #    for l in current:
                    #        temp.append()
                        AES.inv_mix_columns(current)
                    #Add Round Key
                    AES.keyGen(current, i, False)
                    final = []
                    for j in range(4):
                        temp = []
                        for k in range(4):
                            temp.append(AES.key[j][k]^current[j][k])
                        final.append(temp)
                    current = final
            #Add final to lines out
            final = []
            for j in range(4):
                for k in range(4):
                    final.append(hex(current[j][k]) + " ")
            AES.linesOUT.append(final)

    def main():
        
        #text = "Cheesey Cheddar!"
        times = " "
        timearray = []
        for i in range(100):
            AES.takeIn("tenThousand",True)
            timing = time.time()
            AES.encrypt(AES.linesIN)
            timing = time.time()-timing
            times += str(timing) + " "
            timearray.append(timing)
            #print(f"timing: {timing}")
        print(times)
        print(len(timearray))
        AES.linesOUT = times
        #AES.putOut("aesFINAL")
        
        return
        AES.takeIn("aesOUT", False)
        AES.decrypt(AES.linesIN)
        return
        zero = [[0x54,0x68,0x61,0x74],[0x73,0x20,0x6d,0x79],[0x20,0x4b,0x75,0x6e],[0x67,0x20,0x46,0x75]]
        AES.keyGen(zero, 1)
        print(AES.key)
        hexxed = []
        for i in AES.key:
            temp = []
            for j in i:
                temp.append(hex(j))
            hexxed.append(temp)
        print(hexxed)
AES.main()