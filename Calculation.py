import FileOperations
import HashingOfSubString


def calculate(count):
    max_score=0
    max_string=""
    string=FileOperations.gettingString(count, count+6000)
    locationInString=FileOperations.createHashingOfString(count, count+6000)
    for length in range(3000, 0, -1):
        print("Working on Length: " + str(length))
        lookupSubString=HashingOfSubString.creatingHashing(length)

        print("Finding the Substring that match the above hashes key created")
        for key in lookupSubString:
            for location in locationInString[key[0]]:
                if count == 0:
                    if string[location: location + length] in lookupSubString:
                        lookupSubString[string[location: location + length]] += 1
                if count>0 and location+length>count+3000:
                    if string[location: location + length] in lookupSubString:
                        lookupSubString[string[location: location + length]] += 1
        for key in lookupSubString:
            if lookupSubString[key]>1:
                if pow(length, 2) * pow(lookupSubString[key] - 1, 0.33) > max_score:
                    max_score = pow(length, 2) * pow(lookupSubString[key] - 1, 0.33)
                    max_string = key
                    return [lookupSubString,max_score, max_string]


