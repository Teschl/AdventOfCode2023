import re

def aufg1():
    filePath = "day05/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    # get seeds from input
    seeds = re.split(" ", re.sub("seeds: ","", lines[0].strip()))

    
        


def aufg2():
    filePath = "day05/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()



print(aufg1())
print(aufg2())