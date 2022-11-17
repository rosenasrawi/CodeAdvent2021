# Preprocess data

def preprocessData(datafile):
    with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/16" + datafile, "r") as hexFile:
        hex = hexFile.readlines()[0]
        hex = hex.rstrip('\n')
    return hex

# Turn hexadecimal into binary

def hex2bin(hex: str, packet = '') -> str:
    for i in hex: 
        packet += str("{0:04b}".format(int(i, 16)))
    return packet

# Function to unpack binary

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

            while lsubpack > 0:

                version, pos = unpack(packet, version, pos)
                lsubpack -= pos - oldpos
                oldpos = pos

        elif ltype == 1: # Number of subpackets
            
            nsubpack = int(packet[pos:pos+11],2)
            pos += 11

            while nsubpack > 0:

                version, pos = unpack(packet, version, pos)
                nsubpack -= 1

    return version, pos

# Get data & run

# hex = 'D2FE28' # literal
# hex = '38006F45291200' # operator ltype 0
# hex = 'EE00D40C823060' # operator ltype 1
# hex = 'A0016C880162017C3686B18A3D4780' # example
# packet = hex2bin(hex)

packet = hex2bin(preprocessData('/input16.txt'))
version, pos = unpack(packet, version = 0, pos = 0)

print(version)
