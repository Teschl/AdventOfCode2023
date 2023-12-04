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
    filePath = "day04/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    weight = []

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
                score += 1
        # hier dann in gewichts liste eintagen wie viel wer wert ist
        # damit dann summe berchnet werden kann
        for i in range(0,score):
            pass


print(aufg1())
print(aufg2())