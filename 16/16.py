# Preprocess data

import os

def preprocessData(datafile):
    wd = os.getcwd()
    with open(wd + "/16" + datafile, "r") as hexFile:
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

        value = ''
        start = int(packet[pos])

        while start == 1: # Keep parsing if starts with 1
            value += packet[pos+1:pos+5]
            pos += 5
            start = int(packet[pos])

        if start == 0:
            value += packet[pos+1:pos+5]

        pos += 5
        value = int(value, 2)
        
    else: # Operator
        
        ltype = int(packet[pos]) # Length type ID
        pos += 1
        values = []

        if ltype == 0: # Length of subpackets

            lsubpack = int(packet[pos:pos+15],2)
            pos += 15; oldpos = pos

            while lsubpack > 0:

                version, pos, subval = unpack(packet, version, pos)
                values.append(subval)

                lsubpack -= pos - oldpos
                oldpos = pos

        elif ltype == 1: # Number of subpackets
            
            nsubpack = int(packet[pos:pos+11],2)
            pos += 11

            while nsubpack > 0:
                version, pos, subval = unpack(packet, version, pos)
                values.append(subval)

                nsubpack -= 1    

        if type == 0:
            value = sum(values)
        elif type == 1:   
            value = 1
            for i in values:
                value = value * i
        elif type == 2:
            value = min(values)
        elif type == 3:
            value = max(values)
        elif type == 5:
            value = int(values[0] > values[1])
        elif type == 6:
            value = int(values[0] < values[1])
        elif type == 7:
            value = int(values[0] == values[1])

    return version, pos, value

# Get data & run

packet = hex2bin(preprocessData('/input16.txt'))
version, pos, value = unpack(packet, version = 0, pos = 0)

print('Part 1:', version)
print('Part 2:', value)