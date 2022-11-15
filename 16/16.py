
def preprocessData(datafile):
    with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/16" + datafile, "r") as hexFile:
        hex = hexFile.readlines()[0]
        hex = hex.rstrip('\n')
    return hex

# hex = preprocessData('/input16.txt')

hex = '8A004A801A8002F478'

def hex2bin(hex: str, bin = '') -> str:
    for i in hex: bin+=str("{0:04b}".format(int(i, 16)))
    return bin

bin = hex2bin(hex)

print(bin)

def unpacking(bin, versionCount):
    version = int(bin[:3],2) # First three numbers is the version
    packet = int(bin[3:6],2) # Second three numbers is the packet
    remfromBin = 0
    bin = bin[6:]; remfromBin += 6
    # print('hello')
    versionCount += version # Add this number to the version count 

    if packet == 4: # Literal
        last = False
        while not last:
            next = bin[:5]
            if next[0] == '1': # remove this number & continue
                bin = bin[5:];  
            elif next[1] == '0': # remove this number & stop
                bin = bin[5:]; last = True
            remfromBin += 5

    else: # Operator
        lenTypeID = bin[0]
        bin = bin[1:]; remfromBin += 1

        if lenTypeID == '0': # Next 15 = len sub-packets
            lenSubPackets = int(bin[:15],2)
            bin = bin[15:]; remfromBin += 15

            while remfromBin < lenSubPackets:
                versionCount = unpacking(bin, versionCount)

        if lenTypeID == '1': # Next 11 = num of subpackets
            numSubPackets = int(bin[:11],2)
            bin = bin[11:]; remfromBin += 11
            i = 0
            while i < numSubPackets:
                versionCount = unpacking(bin, versionCount)
                i+=1

    return versionCount

versionCount = unpacking(bin, versionCount=0)
print(versionCount)