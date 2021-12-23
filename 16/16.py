
hex = '38006F45291200'

def hex2bin(hex: str, bin = '') -> str:
    for i in hex: bin+=str("{0:04b}".format(int(i, 16)))
    return bin

print(hex2bin(hex))


