import Calculation

max_subsequence_size=500
lookup={}
max_value=0
max_string=""
count=0
while count<max_subsequence_size*30:
    arr=Calculation.calculate(count, max_subsequence_size)
    for key in arr:
        if key in lookup:
            lookup[key]+=arr[key]
        else:
            lookup[key]=arr[key]

    count+=max_subsequence_size
for key in lookup:
    if lookup[key]>1:
        if pow(len(key), 2) * pow(lookup[key] - 1, 0.33) > max_value:
            max_value = pow(len(key), 2) * pow(lookup[key] - 1, 0.33)
            max_string=key

print(max_value)
print(max_string)


