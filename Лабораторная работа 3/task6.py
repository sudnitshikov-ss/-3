list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = max(list_numbers)
i = list_numbers.index(max_number)
last_number = list_numbers[len(list_numbers)-1]
k = list_numbers.index(last_number)
o = max_number
list_numbers[i] = list_numbers[k]
list_numbers[k] = o
print(list_numbers)
