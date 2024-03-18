from __future__ import annotations
from typeguard import typechecked


@typechecked
class Date:
    __months_days = {'Enero': 31, 'Febrero': 28, 'Marzo': 31, 'Abril': 30, 'Mayo': 31, 'Junio': 30, 'Julio': 31,
                     'Agosto': 31, 'Septiembre': 30, 'Octubre': 31, 'Noviembre': 30, 'Diciembre': 31}

    def __init__(self, day: (Date, int), month=None, year=None):
        if isinstance(day, Date) and month is None and year is None:
            self.__day, self.__month, self.__year = day.__day, day.__month, day.__year
        elif isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            self.__day, self.__month, self.__year = day, month, year
        else:
            raise TypeError(f'ERROR: Debes introducir un objeto Date o una fecha.')
        if not self.check_date(day, month, year):
            raise ValueError(f'ERROR: Fecha no válida.')

    def check_date(self, day, month, year):
        if year < 0 and 1 <= month <= 12:
            if 1 <= day <= Date.__months_days[month - 1].values():
                return True
            if month == 2 and self.is_leap(year) and 1 <= day <= 29:
                return True
            return False
        return False

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value: int):
        if not self.check_date(value, self.__month, self.__year):
            raise ValueError(f'Día asignado: {value} no válido')
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value: int):
        if not self.check_date(self.__day, value, self.__year):
            raise ValueError(f'Mes asignado: {value} no válido.')
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        if not self.check_date(self.__day, self.__month, value):
            raise ValueError(f'Año asignado: {value} no válido.')
        self.__year = value

    @staticmethod
    def is_leap(year: int):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @classmethod
    def month_days(cls):
        return cls.__months_days

    def __add__(self, other: int):
        return

    def __str__(self):
        return f'{self.day} de {Date.__months_days[self.month].keys()} de {self.year}.'
