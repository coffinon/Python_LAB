import math


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag

    def conj(self):
        self.imag = -self.imag

    def sum(self, b):
        return Complex(self.real + b.real, self.imag + b.imag)

    def diff(self, b):
        return Complex(self.real - b.real, self.imag - b.imag)

    def multi(self, b):
        return Complex(self.real * b.real - self.imag * b.imag, self.real * b.imag + self.imag * b.real)

    def abs(self):
        return math.sqrt(self.real * self.real + self.imag * self.imag)


while 1:
    print("_-_-_-_-_ WYBIERZ OPERACJE MATEMATYCZNA _-_-_-_-_")
    print("\t 1.DODAWANIE")
    print("\t 2.ODEJMOWANIE")
    print("\t 3.MNOZENIE")
    print("\t 4.MODUL")
    print("\t 5.SPRZEZENIE")
    print("\t 6.KONIEC")

    n = int(input("\nWYBOR : "))
    print("FORMAT WPISYWANIA : RE + IM\n")

    if n == 1:
        re, im = input("PIERWSZA LICZBA : ").split(" + ")
        x = Complex(float(re), float(im))
        re, im = input("DRUGA LICZBA : ").split(" + ")
        y = Complex(float(re), float(im))
        sum_x_y = x.sum(y)
        print("x + y = ", sum_x_y.get_real(), " + ", sum_x_y.get_imag(), " i\n")
    elif n == 2:
        re, im = input("PIERWSZA LICZBA : ").split(" + ")
        x = Complex(float(re), float(im))
        re, im = input("DRUGA LICZBA : ").split(" + ")
        y = Complex(float(re), float(im))
        diff_x_y = x.diff(y)
        print("x - y = ", diff_x_y.get_real(), " + ", diff_x_y.get_imag(), " i\n")
    elif n == 3:
        re, im = input("PIERWSZA LICZBA : ").split(" + ")
        x = Complex(float(re), float(im))
        re, im = input("DRUGA LICZBA : ").split(" + ")
        y = Complex(float(re), float(im))
        multi_x_y = x.multi(y)
        print("x * y = ", multi_x_y.get_real(), " + ", multi_x_y.get_imag(), " i\n")
    elif n == 4:
        re, im = input("LICZBA : ").split(" + ")
        x = Complex(float(re), float(im))
        print("abs(x) = ", x.abs(), "\n")
    elif n == 5:
        re, im = input("LICZBA : ").split(" + ")
        x = Complex(float(re), float(im))
        x.conj()
        print("conj(x) = ", x.get_real(), " + ", x.get_imag(), " i\n")
    elif n == 6:
        break
    else:
        print("NIE ROZPOZNANO KOMENDY")
