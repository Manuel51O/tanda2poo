"""
- Mostrar un menú con las 6 opciones.
1.  Fecha en formato dd/mm/aaaa, en caso contrario mensaje de error.
    Se valida con función booleana.
2.  Añadir días a la fecha. Pide número de días y actualiza su valor, si el
    número es negativo restará los días. Solo podrá realizarse si existe una fecha,
    en caso contrario mensaje de error.
3.  Añadir meses a la fecha.
4.  Añadir años a la fecha.
5.  Comparar la fecha con otra. Pide otra fecha validada con el mismo formato, debe
    mostrar si es anterior, igual o posterior a la que tenemos y número de días
    comprendidos entre ambas.
6.  Mostrar fecha en formato largo.
7.  Terminar.
"""
from typeguard import typechecked


@typechecked
class Menu:
    def __init__(self, *options, title='Menu de opciones'):
        self.__options = list(options)
        self.__title = title

    @property
    def options(self):
        return self.__options

    @property
    def last_options(self):
        return len(self.__options)

    def print_menu(self):
        print(self.__title)
        for option in self.__options:
            print(option, end='')

    def add_options(self, new_option: str):
        self.__options.append(new_option)

    def chosen_option(self):
        while True:
            option = int(input('\nEnter an option: '))
            if 1 <= option <= self.last_options:
                return option
            print(f'Ha introducido una opción incorrecta {self.options}.')
