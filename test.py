import random
file=open('temp.txt', 'a')
string=""
for i in range(10000000):
    string+=chr(random.randint(0,25)+ord('a'))
file.write(string)
file.close()


# checklength=3000
# substring=string[:checklength]
#
# lookup={}
#
# for length in range(1,checklength+1):
#     for start in range(checklength-length+1):
#         str1=string[start:start+length]
#         if str1 not in lookup:
#             lookup[str1]=0
#         lookup[str1]+=1
#     for start in range(checklength, 100000-length+1):
#         str2=string[start: start+length]
#         if str2 in lookup:
#             lookup[str2]+=1
#
#
# max_product=0
# max_string=""
# for key in lookup:
#     product=pow(len(key), 2)*pow(lookup[key]-1, 0.33)
#     if max_product<=product:
#         max_product=product
#         max_string=key
#
# print(str(checklength)+ " :"+str(max_string)+ ":"+str(max_product))