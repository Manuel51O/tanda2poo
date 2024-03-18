from __future__ import annotations
from typeguard import typechecked


@typechecked
class Duration:
    def __init__(self, hours: (int, Duration), minutes=0, seconds=0):
        if isinstance(hours, Duration):
            self.__hours, self.__minutes, self.__seconds = hours.__hours, hours.__minutes, hours.__seconds
        elif isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
            self.__hours, self.__minutes, self.__seconds = hours, minutes, seconds
        else:
            raise TypeError(f'El objeto debe recibir argumentos de tipo entero o Duration.')
        self.__simplify()

    def total_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    def __simplify(self):
        seconds = self.total_seconds()
        self.__hours = seconds // 3600
        self.__minutes = seconds % 3600 // 60
        self.__seconds = seconds % 3600 % 60

    @staticmethod
    def check_if_new_hours_is_negative(new_value):
        if 0 <= new_value:
            return True
        return False

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @hours.setter
    def hours(self, value: int):
        self.__hours = value

    @minutes.setter
    def minutes(self, value: int):
        self.__minutes = value

    @seconds.setter
    def seconds(self, value: int):
        self.__seconds = value

    def __add__(self, other: (Duration, int), new_minutes=0, new_seconds=0):
        if isinstance(other, Duration):
            return Duration(self.__hours + other.__hours, self.__minutes + other.__minutes,
                            self.__seconds + other.__seconds)
        self.__hours, self.__minutes, self.__seconds = (self.__hours + other, self.__minutes + new_minutes,
                                                        self.__seconds + new_seconds)
        self.__simplify()
        return self

    def __sub__(self, other: (Duration, int), new_minutes=0, new_seconds=0):
        if isinstance(other, Duration):
            return Duration(self.__hours - other.__hours, self.__minutes - other.__minutes,
                            self.__seconds - other.__seconds)
        self.__hours, self.__minutes, self.__seconds = (self.__hours - other, self.__minutes - new_minutes,
                                                        self.__seconds - new_seconds)
        self.__simplify()
        return self

    def __str__(self):
        return f'{self.hours:02}h {self.minutes:02}m {self.seconds:02}s.'
