import re

def aufg1():
    filePath = "day04/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    result = 0

    for card in lines:
        card = card.strip()

        card = re.sub("Card.+: ","",card)
        card = re.split("[|]",card)

        win = re.split(" ",card[0])
        win = list(filter(None, win))

        draw = re.split(" ",card[1])
        draw = list(filter(None, draw))

        score = 0
        for i in draw:
            if i in win:
                if score == 0:
                    score = 1
                else:
                    score = score * 2

        result = result + score

    return result

def aufg2():
    filePath = "day04/input2.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    winTable = []

    for index, card in enumerate(lines):
        card = card.strip()

        card = re.sub("Card.+: ","",card)
        card = re.split("[|]",card)

        win = re.split(" ",card[0])
        win = list(filter(None, win))

        draw = re.split(" ",card[1])
        draw = list(filter(None, draw))


        # find which card produces which other cards
        count = 0
        tmp = []
        for item in draw:
            if item in win:
                count += 1
                tmp.append(index+count)
        winTable.append(tmp)
    print(winTable)
    
    # create List with original wins
    result = []
    for i in range(0,len(winTable)):
        result.append(i)

    # add copies to List
    i = 0
    while i < len(result):
        result = result + winTable[result[i]]
        i += 1

    print(result)
    return len(result)    


print(aufg1())
print(aufg2())