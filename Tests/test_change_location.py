from Domain.obiect2 import get_new_object, get_locatie
from Logic.change_location import change_location


def test_change_location():
    obiect1 = get_new_object(1, 'birou', 'desc 1', 450, 'l111')
    obiect2 = get_new_object(2, 'scaun', 'desc 2', 100, 'l111')
    obiect3 = get_new_object(3, 'masa', 'desc 3', 330, 'l121')
    lista = [obiect1, obiect2, obiect3]
    new_list = change_location(lista, get_locatie(obiect1), get_locatie(obiect3))
    assert len(lista) == len(new_list)
    assert get_locatie(new_list[0]) == get_locatie(obiect3)
    assert get_locatie(new_list[2]) == get_locatie(obiect3)
    sursa = 'lna'
    destinatie = ''
    try:
        _ = change_location(lista, sursa, destinatie)
        assert False
    except ValueError:
        assert True

