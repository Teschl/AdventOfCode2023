import re

def aufg1():
    filePath = "day02/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    maxR = 12
    maxG = 13
    maxB = 14
    result = 0 

    # i is a game
    for i in lines:
        possible = True
        i = i.strip()

        # get id and cleanup string
        i = re.sub("Game ","",i)
        id = re.sub(":.*","",i)
        i = re.sub(".*: ","",i)
        i = re.split("; ",i)

        # j is a set
        for j in i:
            red, green, blue  = 0, 0, 0
            j = re.split(", ",j)
            # get values for red, green, bue
            for k in j:
                if k[-3] == 'r':
                    red = int(re.sub(" red","",k))
                elif k[-5] == 'g':
                    green = int(re.sub(" green","",k))
                elif k[-4] == 'b':
                    blue = int(re.sub(" blue","",k))
            # are any constraints violated?
            if red > maxR or green > maxG or blue > maxB:
                possible = False

        # when game possible, add its id to sum
        if possible == True:
            result = result + int(id)
    return result

def aufg2():
    filePath = "day02/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    result = 0 

    # i is a game
    for i in lines:
        i = i.strip()

        # split and cleanup string
        i = re.sub("Game .+:","",i)
        i = re.split("; ",i)

        power, minR, minG, minB = 0, 0, 0, 0
        # j is a set
        for j in i:
            red, green, blue  = 0, 0, 0
            j = re.split(", ",j)

            # get values for red, green, bue
            for k in j:
                if k[-3] == 'r':
                    red = int(re.sub(" red","",k))
                elif k[-5] == 'g':
                    green = int(re.sub(" green","",k))
                elif k[-4] == 'b':
                    blue = int(re.sub(" blue","",k))

            # adjust min values
            if red > minR:
                minR = red
            if green > minG:
                minG = green
            if blue > minB:
                minB = blue

        # clac power and add to sum
        power = minR*minG*minB
        result = result + power

    return result

print(aufg1())
print(aufg2())