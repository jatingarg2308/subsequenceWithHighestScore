
def creatingHashing(forLength):
    file=open("temp.txt", 'r')
    string=file.read(3000)
    print("Hashing the String of the above length")
    lookUpSubString={}
    for start in range(3000 - forLength + 1):
        if string[start: start + forLength] not in lookUpSubString:
            lookUpSubString[string[start: start + forLength]] = 0

    return lookUpSubString

