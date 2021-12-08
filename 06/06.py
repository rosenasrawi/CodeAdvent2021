# Open & read data
with open("/Users/rosenasrawi/Documents/VU PhD/Side projects/CodeAdvent2021/06/input06.txt", "r") as fishFile:
    lanternFish = fishFile.readlines()

lanternFish = list(map(int, lanternFish[0].split(',')))

def lanternfishMakeBabies(days):

    # Change fish ages to count per age
    fishAges = [0]*9

    for i in range(len(fishAges)):
        fishAges[i] = lanternFish.count(i)

    # Count how the amount of fish grows over days    
    for day in range(days):

        babies = fishAges[0]

        for i in range(8): 
            fishAges[i] += fishAges[i+1]; fishAges[i+1] = 0

        fishAges[6] += babies
        fishAges[8] += babies
        fishAges[0] -= babies
    
    return sum(fishAges)

# Part 1: after 80 days
print('After 80 days there are ' + str(lanternfishMakeBabies(days = 80)) + ' fish')

# Part 2: after 256 days
print('After 256 days there are ' + str(lanternfishMakeBabies(days = 256)) + ' fish')
