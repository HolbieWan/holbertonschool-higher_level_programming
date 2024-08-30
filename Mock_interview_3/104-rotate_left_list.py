def rotate_left_list(my_list=[], number_rotation=0):
    new_list_1 = []
    new_list_2 = my_list.copy()
    new_list_3 = []
    for i in range(number_rotation):
        new_list_1.append(new_list_2[i])
    for i in range(number_rotation):
        new_list_2.pop(0)

    new_list_3 = new_list_2 + new_list_1

    print(new_list_1)
    print(new_list_2)

    return new_list_3

print(rotate_left_list([1, 2, 3, 4, 5], 2))