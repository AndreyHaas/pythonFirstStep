numbers = [3, 2, 8, 2, 4, 9, 4, 1, 7]
numbers2 = []
for number in numbers:
    if numbers not in numbers2:
        numbers2.append(number)
print(numbers2)