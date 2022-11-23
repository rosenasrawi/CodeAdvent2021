import math

# Add two snailnumbers
def add(snailnums):
    snailnum = '['+ snailnums[0] + ',' + snailnums[1] + ']'   
    return snailnum

# Snailnumber string to list
def string2list(snailnum):
    snaillist = []
    for i in list(range(len(snailnum))):
        if len(snaillist) > 2 and snailnum[i-1:i+1].isnumeric():
            snaillist[-1] += snailnum[i]
        else: snaillist.append(snailnum[i])

    return snaillist

# Reduce snailnum
def reduce(snailnum):
    snailnum = string2list(snailnum)
    boom = False; crack = False
    nest = 0; i = 0

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

        if snailnum[i].isnumeric(): # Split
            if int(snailnum[i]) >= 10: 
                half = int(snailnum[i])/2
                snailnum[i] = '['+ str(math.floor(half)) + ',' + str(math.ceil(half)) + ']'

                crack = True
                break 

        i+=1

        if i == len(snailnum)-1: break # End of snailnum

    return ''.join(snailnum), boom, crack

# Reduce snailnum with explosions & splits
def snailmath(snailnums):

    while True:
        if len(snailnums) == 1: break
        snailnum = add(snailnums)
        print(snailnum)
    
        while True:
            snailnum, boom, crack = reduce(snailnum)

            if not boom and not crack: break

        print(snailnum)
        snailnums[0] = snailnum; snailnums.pop(1)

    return snailnum


snailnums = ['[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]' , '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]']

snailmath(snailnums)

# def sum(snailnums):
    # while pair:
        # magnitude = pair[0]*3 + pair[1]*2
    # return magnitude

# def mathhomework(snailnums)
    # while len(snailnums) > 1
        # snailnum = add(snailnums[0], snailnums[1])
        # snailnum = reduce(snailnum)
        
        # snailnums.pop(0,1)
        # snailnums = [snailnum, snailnums]

    # magnitude = sum(snailnums)    
        

    # return magnitude

# magnitude = mathhomework(snailnums)

# print('Part 1:', magnitude)


