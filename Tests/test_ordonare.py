from Domain.obiect2 import get_new_object
from Logic.ordonare import ordonare_lista


def get_data():
    return [
        get_new_object(1, 'birou', 'desc 1', 450, 'l111'),
        get_new_object(2, 'scaun', 'desc 2', 100, 'l111'),
        get_new_object(3, 'masa', 'desc 3', 330, 'l121'),
        get_new_object(4, 'frigider', 'desc 4', 2900, 'l112'),
        get_new_object(5, 'cafetiera', 'desc 5', 470, 'l112'),
        get_new_object(6, 'imprimanta', 'desc 6', 890, 'l111')
    ]


def test_ordonare():
    lista = get_data()
    lista_ordonata = ordonare_lista(lista)
    assert lista[4] in lista_ordonata
    assert len(lista) == len(lista_ordonata)
    assert lista[1] == lista_ordonata[0]


test_ordonare()
