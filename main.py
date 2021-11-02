from Domain.obiect2 import get_new_object
from Logic.crud import create, delete
from Tests.test_concatenare import test_concatenare
from Tests.test_crud import test_crud
from Tests.test_change_location import test_change_location
from User_interface.console import header, handle_delete


def main():
    lista = []
    obiect1 = get_new_object(1, 'birou', 'desc 1', 450, 'l111')
    lista = create(lista, obiect1)
    obiect2 = get_new_object(2, 'scaun', 'desc 2', 100, 'l111')
    lista = create(lista, obiect2)
    obiect3 = get_new_object(3, 'masa', 'desc 3', 330, 'l121')
    lista = create(lista, obiect3)
    obiect4 = get_new_object(4, 'frigider', 'desc 4', 2900, 'l112')
    lista = create(lista, obiect4)
    obiect5 = get_new_object(5, 'cafetiera', 'desc 5', 470, 'l112')
    lista = create(lista, obiect5)
    obiect6 = get_new_object(6, 'imprimanta', 'desc 6', 890, 'l111')
    lista = create(lista, obiect6)
    lista = header(lista)


if __name__ == '__main__':
    test_crud()
    test_change_location()
    test_concatenare()
    main()