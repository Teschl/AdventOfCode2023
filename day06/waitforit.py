import re

def aufg1():
    filePath = "day06/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    time = re.split(" +", re.sub("Time: *","",lines[0].strip()))
    distance = re.split(" +", re.sub("Distance: *","",lines[1].strip()))

    time = list(map(int, time))
    distance = list(map(int, distance))

    # time      = hold + move
    # distance  < hold * move
    # distance  < hold * (t - hold)

    result = 1
    for i in range(0,len(time)):
        wins = 0
        for hold in range(0,time[i]):
            if distance[i] < hold * (time[i] - hold):
                wins += 1
        result = result*wins

    return result

def aufg2():
    filePath = "day06/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()
    
    time = int(re.sub("Time:| *","",lines[0].strip()))
    distance = int(re.sub("Distance:| *","",lines[1].strip()))

    # time      = hold + move
    # distance  < hold * move
    # distance  < hold * (t - hold)

    wins = 0
    for hold in range(0,time):
        if distance < hold * (time - hold):
            wins += 1

    return wins


print(aufg1())
print(aufg2())