from Domain.obiect2 import get_new_object, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        get_new_object(1, 'birou', 'desc 1', 450, 'l111'),
        get_new_object(2, 'scaun', 'desc 2', 100, 'l111'),
        get_new_object(3, 'masa', 'desc 3', 330, 'l121'),
        get_new_object(4, 'frigider', 'desc 4', 2900, 'l112'),
        get_new_object(5, 'cafetiera', 'desc 5', 470, 'l112'),
        get_new_object(6, 'imprimanta', 'desc 6', 890, 'l111')
    ]


def test_create():
    lista = get_data()
    new_object = get_new_object(7, 'dulap', 'desc 7', 90, 'l111')
    new_list = create(lista, new_object)
    assert len(lista) + 1 == len(new_list)
    assert new_object in new_list
    new_object2 = get_new_object(7, 'dulap7', 'desc 77', 90, 'l111')
    try:
        _ = create(new_list, new_object2)
        assert False
    except ValueError:
        assert True
    try:
        new_object3 = get_new_object(7, 'dulap7', 'desc 77', 90, 'l11')
        _ = create(new_list, new_object3)
        assert False
    except ValueError:
        assert True


def test_read():
    lista = get_data()
    random_object = lista[5]
    assert read(lista, get_id(random_object)) == random_object
    assert read(lista) == lista
    try:
        _ = read(lista, 10)
        assert False
    except ValueError:
        assert True


def test_update():
    lista = get_data()
    new_object = get_new_object(3, 'masa lemn', 'desc 3', 400, 'l121')
    update_list = update(lista, new_object)
    assert len(lista) == len(update_list)
    assert new_object in update_list
    assert update_list[2] != lista[2]
    new_object2 = get_new_object(12, 'masa lemn', 'desc 3', 400, 'l121')
    try:
        _ = update(update_list, new_object2)
        assert False
    except ValueError:
        assert True


def test_delete():
    lista = get_data()
    delete_id = 2
    delete_object = read(lista, delete_id)
    new_list = delete(lista, delete_id)
    assert len(new_list) == len(lista) - 1
    assert delete_object not in new_list
    delete_id3 = 19
    try:
        _ = delete(new_list, delete_id3)
    except ValueError:
        assert True
    delete_id2 = 'iu'
    try:
        _ = delete(new_list, delete_id2)
        assert False
    except TypeError:
        assert True


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()

test_crud()