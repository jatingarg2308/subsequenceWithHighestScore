import Calculation
import FileOperations

#################{ configurations }#########################################
max_subsequence_size = 2
number_of_char_in_file=30000
############################################################################

main_string=FileOperations.gettingString(0,max_subsequence_size)
max_frequency=Calculation.frequencyCalculation(main_string, number_of_char_in_file)
max_string=main_string
max_value=pow(max_subsequence_size,2)*pow(max_frequency-1,0.33)
previous_strings={main_string: max_frequency}
print("For Length {} Maximum Frequency is {} for string {}".format(max_subsequence_size, max_frequency, max_string))
prev_length=max_subsequence_size
while prev_length>1:
    if max_value<pow(prev_length - 1, 2)*pow(number_of_char_in_file - prev_length - 2, 0.33):
        current_string={}
        max_frequency_in_length=0
        max_frequency_string_in_length=""
        for key in previous_strings:
            string=""
            for i in range(prev_length):
                if i==0:
                    string=key[i+1:]
                if i==prev_length-1:
                    string=key[:i]
                if i!=0 and i!=prev_length-1:
                    string=key[:i]+key[i+1:]

                if string not in current_string:
                    frequency_in_length=Calculation.frequencyCalculation(string, number_of_char_in_file)
                    current_string[string]=frequency_in_length
                if frequency_in_length>max_frequency_in_length:
                    max_frequency_in_length=frequency_in_length
                    max_frequency_string_in_length=string
        print("For Length {} Maximum Frequency is {} for string {}".format(prev_length-1, max_frequency_in_length, max_frequency_string_in_length))
        if max_frequency<max_frequency_in_length:
            temp=pow(prev_length-1,2)*pow(max_frequency_in_length-1,0.33)
            if max_value<temp:
                max_value=temp
                max_frequency=max_frequency_in_length
                max_string=max_frequency_string_in_length
        prev_length -= 1
        previous_strings = current_string
    else:
        break
print()
print("value:{}  frequency:{} string:{}".format(max_value, max_frequency, max_string))






# print(main_string)
# print()
# print(Calculation.frequencyCalculation(main_string, number_of_char_in_file))

