from Domain.obiect2 import get_new_object, get_locatie
from Logic.sume_pret import location_list, suma_pret_locatie


def get_data():
    return [
        get_new_object(1, 'birou', 'desc 1', 450, 'l111'),
        get_new_object(2, 'scaun', 'desc 2', 100, 'l111'),
        get_new_object(3, 'masa', 'desc 3', 330, 'l121'),
        get_new_object(4, 'frigider', 'desc 4', 2900, 'l112'),
        get_new_object(5, 'cafetiera', 'desc 5', 470, 'l112'),
        get_new_object(6, 'imprimanta', 'desc 6', 890, 'l111')
    ]


def test_location_list():
    lista = get_data()
    locationlist = location_list(lista)

    assert get_locatie(lista[0]) in locationlist
    assert get_locatie(lista[2]) in locationlist
    assert get_locatie(lista[3]) in locationlist
    assert len(locationlist) == 3


def test_sume_pret():
    lista = get_data()
    locatie1 = get_locatie(lista[2])
    locatie2= get_locatie(lista[4])
    assert suma_pret_locatie(lista, locatie1) == 330
    assert suma_pret_locatie(lista, locatie2) == 3370
    assert type(suma_pret_locatie(lista, locatie2)) is int


test_sume_pret()
test_location_list()