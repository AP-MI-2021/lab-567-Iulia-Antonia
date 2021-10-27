from Domain.obiect2 import get_new_object, get_id
from Logic.crud import create, read, update, delete


def get_data():
    return [
        get_new_object(1, 'birou', 'desc 1', 450, 'l111'),
        get_new_object(2, 'scaun', 'desc 2', 100, 'l111'),
        get_new_object(3, 'masa', 'desc 3', 330, 'l121'),
        get_new_object(4, 'frigider', 'desc 4', 2900, 'l112'),
        get_new_object(5, 'cafetiera', 'desc 5', 470, 'l112'),
        get_new_object(6, 'imprimanta', 'desc 6', 890, 'l111'),
    ]


def test_create():
    lista = get_data()
    new_object = get_new_object(7, 'dulap', 'desc 7', 90, 'l111')
    new_list = create(lista, 7, 'dulap', 'desc 7', 90, 'l111')
    print(lista)
    print(new_list)
    assert len(lista) + 1 == len(new_list)
    assert new_object in new_list


def test_read():
    lista = get_data()
    random_object = lista[5]
    assert read(lista, get_id(random_object)) == random_object
    assert read(lista) == lista


def test_update():
    lista = get_data()
    new_object = get_new_object(3, 'masa lemn', 'desc 3', 400, 'l121')
    update_list = update(lista, new_object)
    assert len(lista) == len(update_list)
    assert new_object in update_list
    assert update_list[2] != lista[2]


def test_delete():
    lista = get_data()
    delete_id = 2
    delete_object = read(lista, delete_id)
    new_list = delete(lista, delete_id)
    assert len(new_list) == len(lista) - 1
    assert delete_object not in new_list


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


test_crud()