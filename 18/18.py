import math, os

def preprocess(datafile):
    wd = os.getcwd()
    with open(wd + "/18" + datafile, "r") as snailFile:
        snailnums = snailFile.readlines()
        snailnums = [i.rstrip('\n') for i in snailnums]

    return snailnums

def add(snailnums):
    snailnum = '['+ snailnums[0] + ',' + snailnums[1] + ']'   
    return snailnum

def string2list(snailnum):
    snaillist = []
    for i in list(range(len(snailnum))):
        if len(snaillist) > 2 and snailnum[i-1:i+1].isnumeric():
            snaillist[-1] += snailnum[i]
        else: snaillist.append(snailnum[i])

    return snaillist

def explode(snailnum):
    snailnum = string2list(snailnum)
    boom = False; nest = 0; i = 0

    while True:

        if snailnum[i] == '[': nest += 1
        elif snailnum[i] == ']': nest -= 1
        
        if nest == 5: # Explode
            
            pair = [i+1,i+3]
            l = pair[0]-1; r = pair[1]+1

            while True:
                if l == 0: break
                if snailnum[l].isnumeric():
                    snailnum[l] = str(int(snailnum[pair[0]]) + int(snailnum[l])); break
                l-=1

            while True:
                if r == len(snailnum)-1: break
                if snailnum[r].isnumeric():
                    snailnum[r] = str(int(snailnum[pair[1]]) + int(snailnum[r])); break
                r+=1

            snailnum[pair[0]-1:pair[1]+2] = '0'

            boom = True
            break

        i+=1

        if i == len(snailnum)-1: break # End of snailnum

    return ''.join(snailnum), boom

def split(snailnum):
    snailnum = string2list(snailnum)
    crack = False; i = 0

    while True:
        if snailnum[i].isnumeric(): # Split
            if int(snailnum[i]) >= 10: 
                half = int(snailnum[i])/2
                snailnum[i] = '['+ str(math.floor(half)) + ',' + str(math.ceil(half)) + ']'

                crack = True
                break 

        i+=1

        if i == len(snailnum)-1: break # End of snailnum

    return ''.join(snailnum), crack

def snailmath(snailnums):

    while True:
        if len(snailnums) > 1: snailnum = add(snailnums)
        else: snailnum = snailnums[0]
    
        while True:
            snailnum, boom = explode(snailnum)

            if not boom: 
                snailnum, crack = split(snailnum)

            if not boom and not crack: break

        snailnums[0] = snailnum; snailnums.pop(1)
        
        if len(snailnums) == 1: break

    return snailnum

def magnitude(snailnum):
    snailnum = string2list(snailnum); i = 0

    while True:
        if snailnum[i] == ']':

            pair = [i-3,i-1]
            mag = 3*int(snailnum[pair[0]]) + 2*int(snailnum[pair[1]])

            snailnum[pair[0]-1:pair[1]+2] = '0'
            snailnum[pair[0]-1] = str(mag)

            i = 0
        
        if len(snailnum) == 1: break

        i+=1

    return ''.join(snailnum)    

print('Part 1:', magnitude(snailmath(preprocess('/input18.txt'))))
