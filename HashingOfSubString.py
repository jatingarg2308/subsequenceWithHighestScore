
def creatingHashing(forLength, max_subsequence_size):
    file=open("temp.txt", 'r')
    string=file.read(max_subsequence_size)
    print("Hashing the String of the above length")
    lookUpSubString={}
    for start in range(max_subsequence_size - forLength + 1):
        if string[start: start + forLength] not in lookUpSubString:
            lookUpSubString[string[start: start + forLength]] = 0

    return lookUpSubString

