


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]


duplicate_values = list(set(list1).symmetric_difference(set(list2)))
print(duplicate_values)
