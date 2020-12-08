import math

a = float(input("A : "))
b = float(input("B : "))
c = float(input("C : "))

delta = b ** 2 - 4 * a * c

print("\nDelta : ", delta, "\n")

if delta > 0:
    x1 = ((-1) * b - math.sqrt(delta)) / (2 * a)
    x2 = ((-1) * b + math.sqrt(delta)) / (2 * a)
    print("Delta > 0 \t ==> x = ", "{:.2f}".format(x1), " lub x = ", "{:.2f}".format(x2))
elif delta == 0:
    x0 = ((-1) * b) / (2 * a)
    print("Delta = 0 \t ==> x = ", "{:.2f}".format(x0))
else:
    print("Delta < 0 \t ==> brak rozwiazan")
