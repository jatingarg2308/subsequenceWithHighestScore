import FileOperations
import HashingOfSubString


def calculate1(count, max_subsequence_size):
    string=FileOperations.gettingString(count, count+2*max_subsequence_size)
    locationInString=FileOperations.createHashingOfString(count, count+2*max_subsequence_size)
    masterLookupSubstring={}
    for length in range(max_subsequence_size, 0, -1):
        print("Working on Length: " + str(length))
        lookupSubString=HashingOfSubString.creatingHashing(length, max_subsequence_size)

        print("Finding the Substring that match the above hashes key created")
        for key in lookupSubString:
            if key[0] in locationInString:
                for location in locationInString[key[0]]:
                    if count == 0 and location+length<=max_subsequence_size:
                        if string[location: location + length] in lookupSubString:
                            lookupSubString[string[location: location + length]] += 1
                    if count>0 and location+length>max_subsequence_size:
                        if string[location: location + length] in lookupSubString:
                            lookupSubString[string[location: location + length]] += 1
        for key in lookupSubString:
            if key not in masterLookupSubstring:
                masterLookupSubstring[key]=lookupSubString[key]

    return masterLookupSubstring

def calculate2(length, max_subsequence_size, number_of_char_in_file):
    print("Working on Length: " + str(length))
    string=""
    lookupSubString = HashingOfSubString.creatingHashing(length, max_subsequence_size)
    for count in range(0, number_of_char_in_file-max_subsequence_size+1, max_subsequence_size):
        string =FileOperations.gettingString(count, count+2*max_subsequence_size)
        locationInString = FileOperations.createHashingOfString(count, count + 2 * max_subsequence_size)

        # print("Finding the Substring that match the above hashes key created")

        for key in lookupSubString:
            if key[0] in locationInString:
                locations=locationInString[key[0]]
                for index in range(len(locations)-1, -1, -1):
                    if count == 0 and locations[index]<=max_subsequence_size:
                        if string[locations[index]: locations[index] + length] in lookupSubString:
                            lookupSubString[string[locations[index]: locations[index] + length]] += 1

                    if count>0 and locations[index]+length>max_subsequence_size:
                        if string[locations[index]: locations[index] + length] in lookupSubString:
                            lookupSubString[string[locations[index]: locations[index] + length]] += 1
                    if count>0 and locations[index]+length<=max_subsequence_size:
                        break


    return lookupSubString

def frequencyCalculation(lookupString, number_of_char_in_file):
    frequency=0
    length=len(lookupString)
    for count in range(0, number_of_char_in_file-2*length, length):
        string=FileOperations.gettingString(count, count+2*length)
        locationInString=FileOperations.createHashingOfString(count, count+2*length)

        if lookupString[0] in locationInString:
            locations = locationInString[lookupString[0]]
            for index in range(len(locations) - 1, -1, -1):
                if count == 0 and locations[index] <= length:
                    if string[locations[index]: locations[index] + length]== lookupString:
                        frequency += 1

                if count > 0 and locations[index] + length > length:
                    if string[locations[index]: locations[index] + length]== lookupString:
                        frequency += 1
                if count > 0 and locations[index] + length <= length:
                    break

    return frequency

def getFrequencies(json, number_of_char_in_file):
    for key in json:
        json[key]=frequencyCalculation(key, number_of_char_in_file)
