file=open('temp.txt', 'r')
string=file.read()

checklength=3000
substring=string[:checklength]

frequencyInString={}

for i in range(len(string)):
    if string[i] not in frequencyInString:
        frequencyInString[string[i]]=0
    frequencyInString[string[i]]+=1

print(frequencyInString)