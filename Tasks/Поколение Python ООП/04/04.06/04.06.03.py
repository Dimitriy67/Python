# Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
# При создании экземпляра класс должен принимать три аргумента в следующем порядке:

# a — коэффициент a квадратного трехчлена
# b — коэффициент b квадратного трехчлена
# c — коэффициент c квадратного трехчлена

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    @property
    def d(self):
        return self.b ** 2 - 4 * self.a * self.c

    @property
    def x1(self):
        return (-self.b - self.d ** 0.5) / (2 * self.a) if self.d >= 0 else None

    @property
    def x2(self):
        return (-self.b + self.d ** 0.5) / (2 * self.a) if self.d >= 0 else None

    @property
    def view(self):
        b, sign_b = abs(self.b), '-' if self.b < 0 else '+'
        c, sign_c = abs(self.c), '-' if self.c < 0 else '+'
        return f'{self.a}x^2 {sign_b} {b}x {sign_c} {c}'

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coeff):
        a, b, c = coeff
        self.a, self.b, self.c = a, b, c
