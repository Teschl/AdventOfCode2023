import re

def aufg1():

    filePath = "day01/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()

    sum = 0
    for i in lines:
        i = i.strip()
        i = re.sub("[a-z]", "", i)
        result = i[0] + i[len(i)-1]
        sum = sum + int(result)

    return sum

def aufg2():
    filePath = "day01/input.txt"
    file = open(filePath)
    lines = file.readlines()
    file.close()
    
    sum = 0
    for i in lines:
        i = i.strip()
        
        # added first an last letters to sub so stuff 
        # like "oneight" works as "18" not "1ight"
        i = re.sub("zero","0o",i)
        i = re.sub("one","o1e",i)
        i = re.sub("two","t2o",i)
        i = re.sub("three","t3e",i)
        i = re.sub("four","f4r",i)
        i = re.sub("five","f5e",i)
        i = re.sub("six","s6x",i)
        i = re.sub("seven","s7n",i)
        i = re.sub("eight","e8t",i)
        i = re.sub("nine","n9e",i)

        i = re.sub("[a-z]", "", i)
        result = i[0] + i[len(i)-1]
        sum = sum + int(result)

    return sum

print(aufg1())
print(aufg2())