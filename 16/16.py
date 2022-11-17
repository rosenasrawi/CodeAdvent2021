# REAL DATA

def preprocessData(datafile):
    with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/16" + datafile, "r") as hexFile:
        hex = hexFile.readlines()[0]
        hex = hex.rstrip('\n')
    return hex

hex = preprocessData('/input16.txt')
print(hex)

# hex = 'D2FE28' # literal
# hex = '38006F45291200' # operator ltype 0
# hex = 'EE00D40C823060' # operator ltype 1

# hex = 'A0016C880162017C3686B18A3D4780' # example 1

def hex2bin(hex: str, packet = '') -> str:
    for i in hex: packet += str("{0:04b}".format(int(i, 16)))
    return packet

packet = hex2bin(hex)
version = 0
pos = 0

def unpack(packet, version, pos):
    
    version += int(packet[pos:pos+3],2) # Get version
    type = int(packet[pos+3:pos+6],2) # Get type
    pos += 6

    if type == 4: # Literal
        
        start = int(packet[pos])

        while start == 1: # Keep parsing if starts with 1
            pos += 5
            start = int(packet[pos])

        pos += 5

    else: # Operator
        
        ltype = int(packet[pos]) # Length type ID
        pos += 1

        if ltype == 0: # Length of subpackets

            lsubpack = int(packet[pos:pos+15],2)
            pos += 15; oldpos = pos
            readlength = 0

            while readlength < lsubpack:

                version, pos = unpack(packet, version, pos)
                diff = pos - oldpos
                readlength += diff

        elif ltype == 1: # Number of subpackets
            
            nsubpack = int(packet[pos:pos+11],2)
            pos += 11

            while nsubpack > 0:
                version, pos = unpack(packet, version, pos)
                nsubpack -= 1

    return version, pos

version, pos = unpack(packet, version, pos)

print(version)


# LOGIC

# def unpack(bin):
# if literal: 
    # 1+4 nums repeat till 0
# if operator:
    # ltID = 0: 
        # lSubpack
        # unpack(packet)
    # ltID = 1:
        # nSubpack
        # unpack(packet)

