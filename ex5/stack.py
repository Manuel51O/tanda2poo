from __future__ import annotations
from typing import List
from typeguard import typechecked


@typechecked
class Stack:
    def __init__(self, values: (List, Stack) = []):
        if isinstance(values, Stack):
            self.__values = values.__values[:]
        elif not isinstance(values, List):
            self.__values = list(values)[:]
        elif isinstance(values, List):
            self.__values = values[:]
        else:
            raise ValueError(f'Error: Debes introducir una lista o otra cola.')

    @property
    def values(self):
        return self.__values

    @property
    def size(self):
        return len(self.__values)

    @property
    def is_empty(self):
        return self.size == 0

    def empty_stack(self):
        return self.__values.clear()

    def push(self, new_value):
        self.__values.append(new_value)

    def pop(self):
        if not self.is_empty:
            return self.__values.pop(self.size - 1)
        raise IndexError(f'La pila está vacía.')

    def top(self):
        if not self.is_empty:
            return self.__values[self.size - 1]
        raise IndexError(f'La pila está vacía.')

    def __str__(self):
        return f'{self.values}.'
