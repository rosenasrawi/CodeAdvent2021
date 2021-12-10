with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/10/input10.txt", "r") as syntaxFile:
    syntax = syntaxFile.readlines()
    syntax = [i.rstrip("\n") for i in syntax]

from statistics import median

# Part 1 - Find first incorrect item in syntax

def firstWrongSyntax(line):
    open = '([{<'; close = ')]}>'; points = [3,57,1197,25137]
    started = []; firstFound = []; score = 0
    
    for i in line:
        if firstFound != []: break
    
        if i in open:
            started.append(i)
        elif i in close:
            if close.index(i) != open.index(started[-1]):
                firstFound = i
            started.pop()        

    if firstFound != []:
        score = points[close.index(firstFound)]
    return score

totalScore = 0; lineScores = []
for line in syntax:
    score = firstWrongSyntax(line); lineScores.append(score)
    totalScore += score

print(totalScore)

# Part 2 - complete the incomplete syntax

incomplete = [syntax[i] for i in range(len(lineScores)) if lineScores[i] == 0]

def fixIncompleteSyntax(line):
    open = '([{<'; close = ')]}>'; points = [1,2,3,4]
    started = []

    for i in line:
        if i in open:
            started.append(i)
        elif i in close:
            if close.index(i) == open.index(started[-1]):
                started.pop()               

    score = 0; started.reverse()
    for i in started:
        p = points[open.index(i)]
        score = score*5+p
    return score      

lineScores = []
for line in incomplete:
    lineScores.append(fixIncompleteSyntax(line))

print(median(lineScores))
