def mixColumns(a, b, c, d):
    print(hex(gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1)))
    print((gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1)))
    #printHex(gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1))
    #printHex(gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1))
    #printHex(gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3))
    #printHex(gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2))
    print()

def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a

def printHex(val):
    return print('{:02x}'.format(val), end=' ')


def main():
    
    mixColumns(0x63,0x2F,0xAF,0xA2)
    return
    # test vectors from https://en.wikipedia.org/wiki/Rijndael_MixColumns#Test_vectors_for_MixColumn()
    mixColumns(0xdb, 0x13, 0x53, 0x45) # 0x8e 0x4d 0xa1 0xbc
    mixColumns(0xf2, 0x0a, 0x22, 0x5c) # 0x9f 0xdc 0x58 0x9d
    mixColumns(0x01, 0x01, 0x01, 0x01) # 0x01 0x01 0x01 0x01 
    mixColumns(0xc6, 0xc6, 0xc6, 0xc6) # 0xc6 0xc6 0xc6 0xc6 
    mixColumns(0xd4, 0xd4, 0xd4, 0xd5) # 0xd5 0xd5 0xd7 0xd6 
    mixColumns(0x2d, 0x26, 0x31, 0x4c) # 0x4d 0x7e 0xbd 0xf8

    # example from question
    mixColumns(0, 17, 34, 51) # 0x22 0x77 0x00 0x55 = 34 119 0 85
main()