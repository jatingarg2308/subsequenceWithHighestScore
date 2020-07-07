import json

file=open("test.json", 'r')
temp=file.read()
file.close()
temp=temp.replace("\'", "\"")

locationInString=json.loads(temp)

file=open("temp.txt",'r')
string=file.read()
subString=string[:3000]
file.close()


max_score=0
max_string=""

for length in range(3000,0,-1):
    print("Working on Length: " + str(length))
    lookUpSubString = {}
    print("Hashing the String of the above length")
    for start in range(0,3000-length+1,1):
        if subString[start: start+length] not in lookUpSubString:
            lookUpSubString[subString[start: start+length]]=0
    print("Finding the Substring that match the above hashes key created")
    for key in lookUpSubString:
        for location in locationInString[key[0]]:
            if string[location: location+length] in lookUpSubString:
                lookUpSubString[string[location: location+length]]+=1
    print("Finding the maximum value")
    for key in lookUpSubString:
        if pow(length,2)*pow(lookUpSubString[key]-1,0.33)>max_score:
            max_score=pow(length,2)*pow(lookUpSubString[key]-1,0.33)
            max_string=key
            print("Actually the looping should Stop here")
    print("For length: "+ str(length)+ ": " + "max value is :" + str(max_score))
    print()

print(max_string+": "+ str(max_score))