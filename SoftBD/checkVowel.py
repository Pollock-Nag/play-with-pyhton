import re
# ? zero or 1 occurance
# ! not
#^ starts with   ! ends with

regex = '(?!^)[aeiouAEIOU](?!$)'
string = "eello"
li = re.findall(regex, string)
print(len(li))


