# to do
s = input("Please enter a string of space separated numbers ")
list = []
j = 0
for i in range(0, len(s)):
    if (s[i] == " "):
        num = int(s[j:i])
        list.append(num)
        j = i

last_num = int(s[j:len(s)])
list.append(last_num)

print("Original list:", list)
count = 0
for i in range(0, len(list)):

    if list[i] % 2 == 0:
        list[i] = "EVEN"

while (list.count("EVEN") != 0):
    list.remove("EVEN")

print("Modified list:", list)
