import Calculation

max_subsequence_size = 50
# lookup={}
max_value = 0
max_string = ""
# count=0
# while count<max_subsequence_size*30:
#     arr=Calculation.calculate(count, max_subsequence_size)
#     for key in arr:
#         if key in lookup:
#             lookup[key]+=arr[key]
#         else:
#             lookup[key]=arr[key]
#
#     count+=max_subsequence_size
# for key in lookup:
#     if lookup[key]>1:
#         if pow(len(key), 2) * pow(lookup[key] - 1, 0.33) > max_value:
#             max_value = pow(len(key), 2) * pow(lookup[key] - 1, 0.33)
#             max_string=key
#
# print(max_value)
# print(max_string)
number_of_char_in_file=30000
max_string_frequency=1
for length in range(max_subsequence_size, 0, -1):
    if max_value <= pow(length, 2) * pow(number_of_char_in_file - length - 1, 0.33):
        lookUpSubString = Calculation.calculate2(length, max_subsequence_size, number_of_char_in_file)
        for key in lookUpSubString:
            if lookUpSubString[key] > max_string_frequency:
                if pow(len(key), 2) * pow(lookUpSubString[key] - 1, 0.33) > max_value:
                    max_value = pow(len(key), 2) * pow(lookUpSubString[key] - 1, 0.33)
                    max_string = key
                    max_string_frequency=lookUpSubString[key]
    else:
        break
print(max_value)
print(max_string)
print(max_string_frequency)

