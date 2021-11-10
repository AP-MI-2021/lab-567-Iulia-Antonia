from Domain.obiect2 import get_new_object
from Logic.crud import create
from Tests.test_concatenare import test_concatenare
from Tests.test_pret_maxim import test_pret_max_per_location
from Tests.test_crud import test_crud
from Tests.test_change_location import test_change_location
from Tests.test_ordonare import test_ordonare
from Tests.undo_redo import test_undo_redo
from Tests.test_sume_pret import test_sume_pret
from User_interface.console import header
from User_interface.console2 import header2


def main():
    lista = []
    lista = header(lista)


def main2():
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
    lista = header2(lista)


def obtiuni():
    print('Alege cum vrei sa dai comenzile: ')
    print('1 - daca vrei sa dai pe rand comenzile')
    print('2 - daca vrei sa dai toate comenzile o data(neactualizata cu ultimele cerinte)')


if __name__ == '__main__':
    test_crud()
    test_change_location()
    test_concatenare()
    test_ordonare()
    test_pret_max_per_location()
    test_sume_pret()
    test_undo_redo()
    obtiuni()
    obtiune = input('Alege cum vrei sa dai comenzile: ')

    if obtiune == '2':
        main2()
    elif obtiune == '1':
        main()
    else:
        print('Poti alege doar 1 sau 2!')
