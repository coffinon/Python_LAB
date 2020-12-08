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


x = Complex(2.0, 2.0)
y = Complex(3.0, 3.0)

sum_x_y = x.sum(y)
diff_x_y = x.diff(y)
multi_x_y = x.multi(y)

print("x + y = ", sum_x_y.get_real(), " + ", sum_x_y.get_imag(), " i")
print("x - y = ", diff_x_y.get_real(), " + ", diff_x_y.get_imag(), " i")
print("x * y = ", multi_x_y.get_real(), " + ", multi_x_y.get_imag(), " i")
print("abs(x) = ", x.abs())
print("abs(y) = ", y.abs())
