fruit_list = {'orange': (8, 7, 12), 'coconut': (10, 20, 30), 'dragonfruit': (6, 12, 14)}
n = int(input())
matched = []
for i in fruit_list.items():
    for j in i[1]:
        if (j == n):
            matched.append(i[0])

result = {}

for i in matched:
    sum = 0
    for j in i:
        if (j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u'):
            sum += ord(j)
    result[i] = sum * n
print(result)