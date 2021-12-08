# Open & read data
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/08/input08.txt", "r") as sevenSegmentsFile:
    sevenSegments = sevenSegmentsFile.readlines()

input = [sevenSegments[i].split('|')[0] for i in range(len(sevenSegments))]
input = [list(map(str,i.split())) for i in input]

output = [sevenSegments[i].split('|')[1] for i in range(len(sevenSegments))]
output = [list(map(str,i.split())) for i in output]

segmentLengths = [len(i) for i in input[0]] # How many different letters in each seven-segment digit
uniqueLengths = [i for i in segmentLengths if segmentLengths.count(i)==1] # Which of these have a unique length

def countOutput():
    occurance = 0

    for out in output: 
        for num in out:
            numLen = len(num)
            if numLen in uniqueLengths: occurance+=1

    return occurance

def totalOutput():
    total = 0

    for n in range(len(input)):
        inp = input[n]; inpLengths = [len(i) for i in inp]
        knownNums = ['']*10; nums = [7,4,8,1]

        for l in inpLengths:
            for i in range(len(uniqueLengths)):
                knownNums[nums[i]] = inp[inpLengths.index(uniqueLengths[i])]

        len5 = [inp[i] for i in [i for i, value in enumerate(inpLengths) if value == 5]]
        len6 = [inp[i] for i in [i for i, value in enumerate(inpLengths) if value == 6]]

        for i in len5:
            if len(set(knownNums[1]).intersection(i)) == 2:
                knownNums[3] = i
            elif len(set(knownNums[4]).intersection(i)) == 3 and len(set(knownNums[1]).intersection(i)) != 2:
                knownNums[5] = i
            else: knownNums[2] = i

        for i in len6:
            if len(set(knownNums[1]).intersection(i)) != 2:
                knownNums[6] = i
            elif len(set(knownNums[1]).intersection(i)) == 2 and len(set(knownNums[4]).intersection(i)) == 4:
                knownNums[9] = i
            else: knownNums[0] = i

        knownNums = [''.join(sorted(i)) for i in knownNums]

        num = ''
        for i in output[n]:
            num +=str(knownNums.index(''.join(sorted(i))))
        total+=int(num)

    return total

# Part 1 - find numbers with unique length 
print(countOutput())
# Part 2: count the full output
print(totalOutput())
