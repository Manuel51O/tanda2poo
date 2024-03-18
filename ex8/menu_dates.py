import locale
from datetime import datetime, date, timedelta
from menu import Menu
from dateutil.relativedelta import relativedelta

user_date = None


def main():
    global user_date
    locale.setlocale(locale.LC_TIME, "es_ES.UTF8")
    menu = Menu('1. Introduce fecha en formato dd/mm/aaaa.\n', '2. Añadir días a la fecha.\n',
                '3. Añadir meses a la fecha.\n', '4. Añadir años a la fecha.\n', '5.Comparar la fecha introducida '
                                                                                 'con otra.\n',
                '6. Mostrar fecha en formato largo.\n', '7. Terminar.')
    menu.print_menu()
    while True:
        option = menu.chosen_option()
        if not user_date and option != 1 and option != menu.last_options:
            print('Primero debes introducir una fecha (opción 1).')
            continue
        match option:
            case 1:
                user_date = input_date()
            case 2:
                add_days()
            case 3:
                add_months()
            case 4:
                add_years()
            case 5:
                print(compare_dates())
            case 6:
                print_date()
            case _:
                break
    print('Terminando programa.')


def input_date():
    global user_date
    date_str = input('Introduce la fecha: ')
    if not check_date(date_str):
        raise ValueError(f'Debes introducir una fecha en formato dd/mm/aaaa.')
    return datetime.strptime(date_str, '%d/%m/%Y').date()


def check_date(date_str):
    if date_str[:2].isdigit() and date_str[3:5].isdigit() and date_str[6:].isdigit() and \
            date(int(date_str[6:]), int(date_str[3:5]), int(date_str[:2])):
        return True
    return False


def add_days():
    global user_date
    days_to_add = int(input('Introduce la cantidad de días a sumar: '))
    user_date += timedelta(days=days_to_add)


def add_months():
    global user_date
    months_to_add = int(input('Introduce la cantidad de meses a sumar: '))
    user_date += relativedelta(months=months_to_add)


def add_years():
    global user_date
    years_to_add = int(input('Introduce la cantidad de años a sumar: '))
    user_date += relativedelta(years=years_to_add)


def compare_dates():
    global user_date
    new_date = input_date()
    if user_date > new_date:
        return f'La fecha introducida es menor que la fecha almacenada. Diferencia de {user_date - new_date}.'
    if user_date < new_date:
        return f'La fecha introducida es mayor que la fecha almacenada. Diferencia de {new_date - user_date}.'
    return f'Ambas fechas son iguales.'


def print_date():
    global user_date
    print(user_date.strftime("%A, %d de %B de %Y"))


if __name__ == '__main__':
    main()
