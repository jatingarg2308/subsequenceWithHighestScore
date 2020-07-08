import FileOperations
import HashingOfSubString


def calculate(count, max_subsequence_size):
    string=FileOperations.gettingString(count, count+2*max_subsequence_size)
    locationInString=FileOperations.createHashingOfString(count, count+2*max_subsequence_size)
    masterLookupSubstring={}
    for length in range(max_subsequence_size, 0, -1):
        print("Working on Length: " + str(length))
        lookupSubString=HashingOfSubString.creatingHashing(length, max_subsequence_size)

        print("Finding the Substring that match the above hashes key created")
        for key in lookupSubString:
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


