

# syntax = '{([(<{}[<>[]}>{[]{[(<()>'
syntax = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','{([(<{}[<>[]}>{[]{[(<()>','(((({<>}<{<{<>}{[]{[]{}','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','{<[[]]>}<{[{[{[]{()[[[]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{','<{([{{}}[<[[[<>{}]]]>[]]']

def firstWrongSyntax(line):
    open = '([{<'
    close = ')]}>'
    points = [3,57,1197,25137]

    started = []
    firstFound = []
    score = 0
    for i in line:
        if firstFound != []: break
    
        if i in open:
            started.append(i)
        elif i in close:
            if close.index(i) != open.index(started[-1]):
                firstFound = i
            started.pop()        

    # return firstFound
    if firstFound != []:
        score = points[close.index(firstFound)]
    return score

totalScore = 0
for line in syntax:
    totalScore += firstWrongSyntax(line)

print(totalScore)
