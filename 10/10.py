with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/10/input10.txt", "r") as syntaxFile:
    syntax = syntaxFile.readlines()
    syntax = [i.rstrip("\n") for i in syntax]

# syntax = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','{([(<{}[<>[]}>{[]{[(<()>','(((({<>}<{<{<>}{[]{[]{}','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','{<[[]]>}<{[{[{[]{()[[[]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{','<{([{{}}[<[[[<>{}]]]>[]]']

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

totalScore = 0
for line in syntax:
    totalScore += firstWrongSyntax(line)

print(totalScore)
