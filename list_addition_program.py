def sum_of_list_elements(list_one, list_two):
    list_3 = []
    min_len_list = min(list_1, list_2, key=len)
    max_len_list = max(list_1, list_2, key=len)
    min_len = len(min_len_list)

    for i in range(min_len):
        list_3.append(list_1[i] + list_2[i])

    list_3.extend(max_len_list[min_len:])
    print(list_3)


list_1 = [0, 0, 1, 1, 2, 2, 6]
list_2 = [0, 1, 1, 2, 2, 3]
sum_of_list_elements(list_1, list_2)
