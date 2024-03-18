from __future__ import annotations
from typeguard import typechecked


@typechecked
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError(f'Una fracción no puede tener 0 como denominador.')
        self.__numerator, self.__denominator = self.__simplify(numerator, denominator)

    @staticmethod
    def __simplify(new_numerator, new_denominator):
        mcd = 1
        for divider in range(2, new_denominator + 1):
            if new_numerator % divider == 0 and new_denominator % divider == 0:
                mcd = divider
        return new_numerator // mcd, new_denominator // mcd

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def result(self):
        return self.__numerator / self.__denominator

    def __mul__(self, other: (int, Fraction)):
        if isinstance(other, int):
            return Fraction(self.__numerator * other, self.__denominator)
        return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return self * -1

    def __truediv__(self, other: Fraction):
        return Fraction(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other: Fraction):
        return Fraction(self.__numerator * other.__denominator + self.__denominator * other.__numerator,
                        self.__denominator * other.__denominator)

    def __sub__(self, other: Fraction):
        return Fraction(self.__numerator * other.__denominator - self.__denominator * other.__numerator,
                        self.__denominator * other.__denominator)

    def __eq__(self, other: (int, Fraction)):
        if isinstance(other, Fraction):
            return self.__numerator == other.__numerator and self.__denominator == other.__denominator
        return self.__numerator == other * self.__denominator

    def __lt__(self, other: (int, Fraction)):
        if isinstance(other, Fraction):
            return self.__numerator * other.__denominator < self.__denominator * other.__numerator
        return self.__numerator < other * self.__denominator

    def __le__(self, other: (int, Fraction)):
        if isinstance(other, Fraction):
            return self.__numerator * other.__denominator <= self.__denominator * other.__numerator
        return self.__numerator <= other * self.__denominator

    def __gt__(self, other: (int, Fraction)):
        if isinstance(other, Fraction):
            return self.__numerator * other.__denominator > self.__denominator * other.__numerator
        return self.__numerator > other * self.__denominator

    def __ge__(self, other: (int, Fraction)):
        if isinstance(other, Fraction):
            return self.__numerator * other.__denominator >= self.__denominator * other.__numerator
        return self.__numerator >= other * self.__denominator

    def __ne__(self, other: Fraction):
        return not (self == other)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        return f'{self.__class__.__name__} {self.numerator} / {self.denominator}'
