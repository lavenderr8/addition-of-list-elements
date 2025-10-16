list_1 = [0, 2, 2, 4, 4]
list_2 = [9, 6, 7, 4, 5]
list_3 = []
i = 0
n = len(list_1)

for i in range(n):
    item = list_1[i] + list_2[i]
    list_3.append(item)
    i += 1

print(list_3)
