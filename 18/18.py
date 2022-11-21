
# def add(snailnum1, snailnum2):
    # snailnum = [snailnum1, snailnum2]
    # return snailnum

# def reduce(snailnum): 
    # while True:
        
        # restart = False

        # If pair nested inside four pares:
            # snailnum = explode(leftmost pair):
            # restart = True  

        # elif any number >= 10 and not restart:
            # snailnum = split(leftmost such number):

        # else: break

        # only the first in the list that applies, then back to while loop
    
    # return snailnum

# def explode(snailnum):
    # pair[0] + first regular number to the left (if any)
    # pair[1] + first regular number to the right (if any)
    # pair becomes a zero

    #[[6,[5,[4,[3,2]]]],1] -> [3,2] = nested pair
    #[[6,[5,[4+3,0]]]],1+2] -> 3 to the 3, 2 to the 1, pair = 0
    # return snailnum

# def split(snailnum)
    # num = [num/2 (rounded down), num/2 (rounded up)]
    # return snailnum

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


