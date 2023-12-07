import re

def aufg1():
    filePath = "day07/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    cardval = { 
        "A": 1000000000000,
        "K": 100000000000,
        "Q": 10000000000,
        "J": 1000000000,
        "T": 100000000,
        "9": 10000000, 
        "8": 1000000,
        "7": 100000, 
        "6": 10000, 
        "5": 1000, 
        "4": 100, 
        "3": 10, 
        "2": 1}

    # create a list that contains tha hand and its bid
    hands =  []
    for i in lines:
        hands.append([re.sub(" .*","",i.strip()), re.sub(".* ","",i.strip())])

    # find which hand each hand represents
    tmp = []
    for hand in hands:
        valmap = 0
        for i in hand[0]:
            valmap += cardval[i]

        valmap = str(valmap)
        if '5' in valmap:
            tmp.append([7,hand[0],hand[1]])

        elif '4' in valmap:
            tmp.append([6,hand[0],hand[1]])

        elif '3' in valmap and '2' in valmap:
            tmp.append([5,hand[0],hand[1]])
            
        elif '3' in valmap:
            tmp.append([4,hand[0],hand[1]])

        elif valmap.count('2') == 2:
            tmp.append([3,hand[0],hand[1]])

        elif valmap.count('2') == 1:
            tmp.append([2,hand[0],hand[1]])

        else:
            tmp.append([1,hand[0],hand[1]])

    # replace A,T,J,Q,K with A,B,C,D,E so it can be sorted with .sort()
    for i in range(len(tmp)):
        tmp[i][1] = tmp[i][1].replace('A','E')
        tmp[i][1] = tmp[i][1].replace('T','A')
        tmp[i][1] = tmp[i][1].replace('J','B')
        tmp[i][1] = tmp[i][1].replace('Q','C')
        tmp[i][1] = tmp[i][1].replace('K','D')

    # sort the list
    tmp.sort(key=lambda i: [i[0], i[1]])

    # calculate sum
    summe = 0
    for i in range(len(tmp)):
        summe += (i+1)*int(tmp[i][2])

    return summe

def aufg2():
    filePath = "day07/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()


print(aufg1())
print(aufg2())