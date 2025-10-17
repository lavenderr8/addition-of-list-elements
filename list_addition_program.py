list_1 = [0, 2, 2, 4, 4]
list_2 = [9, 6, 7, 4, 5]


def get_element_or_0(lst, index):
    if index >= len(lst):
        return 0
    return lst[index]


list_3 = []
n = len(list_1)
l = len(list_2)
m = max(n, l)

for i in range(m):
    item = get_element_or_0(list_1, i) + get_element_or_0(list_2, i)
    list_3.append(item)

print(list_3)
print(m)
