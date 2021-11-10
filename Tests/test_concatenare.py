from Domain.obiect2 import get_new_object
from Logic.concatenare import concatenare


def test_concatenare():
    obiect1 = get_new_object(1, 'birou', 'desc 1', 450, 'l111')
    obiect2 = get_new_object(2, 'scaun', 'desc 2', 100, 'l111')
    obiect3 = get_new_object(3, 'masa', 'desc 3', 330, 'l121')
    lista = [obiect1, obiect2, obiect3]
    string_citit = 'REUSIT'
    pret = 100
    new_list = concatenare(lista, string_citit, pret)
    assert len(lista) == len(new_list)
    assert obiect2[2] == new_list[1][2]
    assert obiect1[2] != new_list[0][2]
    pret2 = 'dj'
    try:
        _ = concatenare(new_list, string_citit, pret2)
        assert False
    except ValueError:
        assert True
