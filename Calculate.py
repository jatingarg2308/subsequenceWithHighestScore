def maxSubstringwithValue(filename, number_of_initial_characters):
    file=open(filename,"r")
    string=file.read()
    file.close()
    if number_of_initial_characters>len(string):
        print("Error: The number of characters are not there in the string")
    else:
        ans=maxValueCalculator(string, number_of_initial_characters)
        print("The Substring with value: {} is :'{}'".format(ans[0],ans[1]))


def maxValueCalculator(string, number_of_initial_characters):
    sub_string = string[:number_of_initial_characters]
    max_value = 0
    max_string = ""

    for index in range(number_of_initial_characters - 1):
        for j in range(index + 1, number_of_initial_characters + 1):
            pattern = sub_string[index: j]
            frequency = frequencyStringMatch(pattern, string)
            if frequency>1:
                value = calculateValue(len(pattern), frequency)
                if value > max_value:
                    max_value = value
                    max_string = pattern
            else:
                break
    return [max_value, max_string]



def frequencyStringMatch(pattern, string):
    lps = computeLPSArray(pattern)
    i = 0  # index of string
    j = 0  # index of pattern
    result = 0  # number of times string matched
    next_i = 0

    while i < len(string):
        if string[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            j = lps[j - 1]
            result += 1

            if lps[j] != 0:
                next_i += 1
                i = next_i
            j = 0
        elif i < len(string) and pattern[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


def computeLPSArray(pattern):
    n = len(pattern)
    lps = [0 for i in range(n)]
    i = 0
    j = 1

    while j < n:
        if pattern[i] == pattern[j]:
            i += 1
            lps[j] = i
            j += 1
        else:
            if i != 0:
                i = lps[i - 1]
            else:
                lps[j] = i
                j += 1
    return lps


def calculateValue(length, frequency):
    return pow(length, 2) * pow(frequency - 1, 0.33)



