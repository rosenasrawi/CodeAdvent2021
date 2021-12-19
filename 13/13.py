coordinates = [[6,10],[0,14],[9,10],[0,3],[10,4],[4,11],[6,0],[6,12],[4,1],[0,13],[10,12],[3,4],[3,0],[8,4],[1,10],[2,14],[8,10],[9,0]]

def coordinatesFill(coordinates, x = [], y = []):
    for i in coordinates:
        x += [i[0]]; y += [i[1]]    

    paper = [['.' for col in range(max(x)+1)] for row in range(max(y)+1)]

    for coor in coordinates:
        i = coor[0]; j = coor[1]
        paper[j][i] = '#'
    
    return paper

paper = coordinatesFill(coordinates)

def foldPaper(paper, countOverlap = 0, foldY = []):
    if foldY != []:
        paper1 = paper[:foldY]; paper2 = paper[foldY+1:]

        r1 = list(range(len(paper1)))           # 0 to end
        r2 = list(range(len(paper2)-1,-1,-1))   # end to 0

        for r in r1:
            row1 = paper1[r]; row2 = paper2[r2[r]]

            for n in range(len(row1)):
                if row2[n] == '#': row1[n] = '#'
            paper1[r] = row1

        for row in paper1:
            countOverlap += row.count('#')
        
        return countOverlap

print(foldPaper(paper, foldY = 7))