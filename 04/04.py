# Open & read data
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/04/input04.txt", "r") as bingoFile:
    bingo = bingoFile.readlines()

bingoNums = bingo.pop(0); bingoNums = list(map(int,bingoNums.split(',')))

for bin in range(len(bingo)):
    x = bingo[bin]; x = list(map(int, x.split()))
    if bin == 0: y = x
    else: y.append(x)

bingo = y.copy(); bingo = [x for x in bingo if x] # remove empty spaces
numRows = int(len(bingo)); numCols = len(bingo[0])

# Part 1: find out which card has bingo first 

BINGO = False; indices = [0]

for num in range(len(bingoNums)): # Pick a number for bingo

    if BINGO == True: break# But only if not yet a bingo found
    else: thisNum = bingoNums[num]

    # Check if this num occurs in any of the rows in bingo, and in which position
    for bin in range(len(bingo)): 
        index = [i for i, value in enumerate(bingo[bin]) if value == thisNum]

        if num == 0:
            if bin == 0: indices[0] = index.copy()
            else:indices.append(index)
        else: indices[bin] += index.copy()

    # Check if a card has bingo
    for card in range(0, numRows, numCols):

        if BINGO == True: break

        thisIndex = indices[card:card+5]; thisCard = bingo[card:card+5]
        
        # Check for vertical bingo
        commonInCol = list(set.intersection(*map(set, thisIndex)))
        if len(commonInCol) > 0: BINGO = True

        # Check for horizontal bingo
        for row in range(numCols):
            if len(thisIndex[row]) == 5: BINGO = True

# Sum of total unmarked * the number that gave the bingo
totalUnmarked = 0

for row in range(len(thisCard)): 
    thisCardRow = thisCard[row]; thisIndexRow = thisIndex[row]

    x = [thisCardRow[i] for i in thisIndexRow]
    y = [i for i in thisCardRow if i not in x]

    totalUnmarked += sum(y)

print(totalUnmarked*thisNum)

# Part 2: find out which card has bingo last 

indices = [0]; BINGO = False; cardsWithBingo = list(range(0, numRows, numCols))

for num in range(len(bingoNums)): # Pick a number for bingo

    if BINGO == True: break
    else: thisNum = bingoNums[num] # But only if not yet last bingo found

    # Check if this num occurs in any of the rows in bingo, and in which position
    for bin in range(len(bingo)): 
        index = [i for i, value in enumerate(bingo[bin]) if value == thisNum]

        if num == 0:
            if bin == 0: indices[0] = index.copy()
            else:indices.append(index)
        else: indices[bin] += index.copy()

    # Check if a card has bingo
    for card in range(0, numRows, numCols):
        if BINGO == True: break
        else: thisIndex = indices[card:card+5]; thisCard = bingo[card:card+5]
        
        # Check for vertical bingo
        commonInCol = list(set.intersection(*map(set, thisIndex)))
        if len(commonInCol) > 0 and card in cardsWithBingo: 
            cardsWithBingo.remove(card)
            if len(cardsWithBingo) == 0: BINGO = True

        # Check for horizontal bingo
        for row in range(numCols):
            if len(thisIndex[row]) == 5 and card in cardsWithBingo: 
                cardsWithBingo.remove(card)
                if len(cardsWithBingo) == 0: BINGO = True

# Sum of total unmarked * the number that gave the bingo
totalUnmarked = 0

for row in range(len(thisCard)): 
    thisCardRow = thisCard[row]; thisIndexRow = thisIndex[row]

    x = [thisCardRow[i] for i in thisIndexRow]
    y = [i for i in thisCardRow if i not in x]

    totalUnmarked += sum(y)

print(totalUnmarked*thisNum)