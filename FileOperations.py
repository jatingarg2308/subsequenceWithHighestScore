def gettingString(From, To):
    file=open("temp.txt", "r")
    file.seek(From)
    string=file.read(To)
    return string

def createHashingOfString(From, To):
    string=gettingString(From, To)
    lookup={}
    for i in range(To-From):
        if string[i] not in lookup:
            lookup[string[i]]=[]
        lookup[string[i]].append(i)
    return lookup