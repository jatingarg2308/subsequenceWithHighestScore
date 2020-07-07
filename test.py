
file=open("temp.txt", 'r')
string=file.read()
file.close()
locationInString={}

for i in range(len(string)):
    if string[i] not in locationInString:
        locationInString[string[i]]=[]
    locationInString[string[i]].append(i)

file=open('test.json', 'w')
file.write(str(locationInString))
file.close()