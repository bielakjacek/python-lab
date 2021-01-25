import numpy


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def add(self, number):
        result_real = self.r + number.r
        result_imaginary = self.i + number.i
        return ComplexNumber(result_real, result_imaginary)

    def subtract(self, number):
        result_real = self.r - number.r
        result_imaginary = self.i - number.i
        return ComplexNumber(result_real, result_imaginary)

    def abs(self):
        return numpy.sqrt(self.r ** 2 + self.i ** 2)

    def multiplication(self, number):
        result_real = self.r * number.r - self.i * number.i
        result_imaginary = self.i * number.r + self.r * number.i
        return ComplexNumber(result_real, result_imaginary)

    def conjugate(self):
        result_real = self.r
        result_imaginary = -1 * self.i
        return ComplexNumber(result_real, result_imaginary)
