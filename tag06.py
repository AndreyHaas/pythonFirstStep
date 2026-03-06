numbers = [3, 6, 8, 2, 4, 9, 4, 1, 2]

maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print(f'Max = {maximum}')