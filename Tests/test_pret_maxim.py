from Domain.obiect2 import get_new_object, get_locatie, get_pret_achizitie
from Logic.pret_maxim import location_list, pret_maxim_locatie


def get_data():
    return [
        get_new_object(1, 'birou', 'desc 1', 450, 'l111'),
        get_new_object(2, 'scaun', 'desc 2', 100, 'l111'),
        get_new_object(3, 'masa', 'desc 3', 330, 'l121'),
        get_new_object(4, 'frigider', 'desc 4', 2900, 'l112'),
        get_new_object(5, 'cafetiera', 'desc 5', 470, 'l112'),
        get_new_object(6, 'imprimanta', 'desc 6', 890, 'l111')
    ]


def test_pret_max_per_location():
    lista = get_data()
    locationlist = location_list(lista)

    assert get_locatie(lista[0]) in locationlist
    assert get_locatie(lista[2]) in locationlist
    assert get_locatie(lista[3]) in locationlist
    assert len(locationlist) == 3

    lista_preturi = pret_maxim_locatie(lista)

    assert get_pret_achizitie(lista[5]) in lista_preturi
    assert get_pret_achizitie(lista[3]) in lista_preturi
    assert get_pret_achizitie(lista[1]) not in lista_preturi
    assert len(lista_preturi) == len(locationlist)


test_pret_max_per_location()
