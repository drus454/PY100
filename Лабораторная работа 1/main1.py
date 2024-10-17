numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_1 = sum(numbers[0:4])
numbers_2 = sum(numbers[5:])
sum_all = numbers_1 + numbers_2
len = len(numbers)
new_numbers = round(sum_all / len, 2)

numbers[4] = new_numbers
print("Измененный список:", numbers)
