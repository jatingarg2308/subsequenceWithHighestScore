import Calculation

lookup={}
max_value=0
count=0
while count<3000*4:
    arr=Calculation.calculate(3000)[1]
    for key in arr[0]:
        if key in lookup:
            lookup[key]+=arr[0][key]
        else:
            lookup[key]=arr[key]

    count+=3000
for key in lookup:
    if lookup[key]>1:
        if pow(len(key), 2) * pow(lookup[key] - 1, 0.33) > max_value:
            max_value = pow(len(key), 2) * pow(lookup[key] - 1, 0.33)
print(max_value)



