a = [1, 2, 12, 4]
b = [2, 4, 2, 8]
result = 0

for i in range(len(a)):
    result += a[i] * b[i]

print(a, " o ", b, " = ", result)
