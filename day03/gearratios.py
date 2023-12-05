numbers = ["1","2","3","4","5","6","7","8","9","0"]

def aufg1():
    filePath = "day03/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    # contains pionter to all numbers in matrix
    # [(numVal, lineIdx, cellIdx, numLen)]
    pointer = []
    numVal = ""
    # iterate over al lines
    for lineIdx, line in enumerate(lines):

        inNumber = False
        # iterate over all cells i a line
        for cellIdx, cell in enumerate(line):

            # Wenn in Zahl und Zahl geht weiter
            if inNumber and cell in numbers:
                numVal = numVal + cell

            # wenn in Zahl und Zahl vorbei
            elif inNumber:
                inNumber = False
                pointer.append((numVal, lineIdx, Idx, cellIdx-Idx))
                cellIdx = 0

            # wnn Zahl beginnt
            elif not inNumber and cell in numbers:
                Idx = cellIdx
                numVal = cell
                inNumber = True

            # wenn in keiner Zahl (muss nichts getan werden)
            elif not inNumber:
                pass
            
     # [(numVal, lineIdx, cellIdx, numLen)]
    # check for tool neighbours
    '''
    part = False
    result = 0
    poggers = numbers.append(".")
    for i in pointer:
        if lines[i[1]][i[2]-1] not in poggers:
            part = True
        if lines[i[1]][i[2]+i[3]] not in poggers:
            part = True

        if part:
            result = result + i[0]

    '''


    print(pointer)
                



def aufg2():
    filePath = "day03/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()


print(aufg1())
print(aufg2())