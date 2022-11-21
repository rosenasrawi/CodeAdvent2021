# Preprocess input

import os

def preprocess(datafile):
    wd = os.getcwd()
    with open(wd + "/17" + datafile, "r") as xyFile:

        xy = xyFile.readline(); xy = xy.rstrip('\n')
        i = [i for i in list(range(len(xy))) if xy[i] in ['x', 'y', ',', '.']]

        x = list(map(int, [xy[i[0]+2:i[1]], xy[i[2]+1:i[3]]]))
        y = list(map(int, [xy[i[4]+2:i[5]], xy[i[6]+1:]]))

    return x, y

# Probe launcher dynamics

def probeStep(pos, vel, yvals):

    pos[0] += vel[0]; pos[1] += vel[1] # velocity
    
    if vel[0] > 0: vel[0] -= 1 # drag
    elif vel[0] < 0: vel[0] += 1

    vel[1] -= 1 # gravity

    yvals.append(pos[1])

    return pos, vel, yvals

# Find highest y with different velocities

def findMaxy(x,y):
    ymax = []; vels = 0

    for xv in list(range(x[1]+1)):
        for yv in list(range(-1000,1000+1)):
            pos = [0,0]; vel = [xv,yv]; yvals = []

            while True:

                target = x[0] <= pos[0] <= x[1] and y[0] <= pos[1] <= y[1]
                missed = pos[0] > x[1] or pos[1] < y[0]

                if target: 
                    ymax.append(max(yvals))
                    vels+=1
                    break
                
                if missed: break

                pos, vel, yvals = probeStep(pos, vel, yvals)

    return max(ymax), vels

# Data & run

x,y = preprocess('/input17.txt')
part1, part2 = findMaxy(x,y)

print('Part 1:', part1)
print('Part 2:', part2)
