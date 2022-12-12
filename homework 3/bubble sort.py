def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]
    return list


a = [3, 5, 1, 2, 0, -5]
print(bubble_sort(a))
