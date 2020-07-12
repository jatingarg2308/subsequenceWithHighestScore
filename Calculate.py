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
            print("Strinh {} with frequency {}".format(pattern, frequency))
            if frequency>1:
                value = calculateValue(len(pattern), frequency)
                if value > max_value:
                    max_value = value
                    max_string = pattern
            else:
                break
    return [max_value, max_string]



def frequencyStringMatch(pattern, string):
    n=len(string)
    m=len(pattern)
    frequency=0
    for i in range(n-m):
        if string[i:i+m]==pattern:
            frequency+=1
    return frequency


def calculateValue(length, frequency):
    return pow(length, 2) * pow(frequency - 1, 0.33)



