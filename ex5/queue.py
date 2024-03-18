from __future__ import annotations
from typing import List
from typeguard import typechecked


@typechecked
class Queue:
    def __init__(self, values: (List, Queue) = []):
        if isinstance(values, Queue):
            self.__values = values.__values[:]
        elif isinstance(values, List):
            self.__values = values[:]
        else:
            try:
                self.__values = list(values)[:]
            except ValueError:
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

    def empty_queue(self):
        return self.__values.clear()

    def enqueue(self, new_value):
        self.__values.append(new_value)

    def dequeue(self):
        if not self.is_empty:
            return self.__values.pop(0)
        raise IndexError(f'La cola está vacía.')

    def front(self):
        if not self.is_empty:
            return self.__values[0]
        raise IndexError(f'La cola está vacía.')

    def __str__(self):
        return f'{self.values}.'
