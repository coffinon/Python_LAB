import random

random.seed()
numbers = []

for i in range(0, 50):
    numbers.append(int(random.random() * 100))

print(numbers)

for i in range(len(numbers) - 1):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
