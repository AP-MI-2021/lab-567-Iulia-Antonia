from Domain.obiect2 import get_new_object
from Logic.change_location import change_location
from Logic.concatenare import concatenare
from Logic.crud import create, read, update, delete


def handle_add(lista, lista_date):
    try:
        id = int(lista_date[1])
        nume = lista_date[2]
        descriere = lista_date[3]
        pret_achizitie = int(lista_date[4])
        locatie = lista_date[5]
        obiect = get_new_object(id, nume, descriere, pret_achizitie, locatie)
        return create(lista, obiect)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_read(lista, lista_date):
    try:
        read_id = int(lista_date[1])
        if read(lista, read_id) is None:
            return 'Id-ul citit nu corespunde vreunui element din lista!'
        else:
            return read(lista, read_id)
    except ValueError as ve:
        print('Eroare: ', ve)
    return []


def handle_update(lista, lista_date):
    try:
        id = int(lista_date[1])
        nume = lista_date[2]
        descriere = lista_date[3]
        pret_achizitie = int(lista_date[4])
        locatie = lista_date[5]
        update_obiect = get_new_object(id, nume, descriere, pret_achizitie, locatie)
        update_list = update(lista, update_obiect)
        return update_list
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_delete(lista, lista_date):
    try:
        delete_id = int(lista_date[1])
        new_list = delete(lista, delete_id)
        return new_list
    except ValueError as ve:
        print('Eroare:', ve)
    except TypeError as te:
        print('Eroare:', te)
    return lista


def showmenu():
    print('1.Adaugarea unui obiect in lista')
    print('2.Afisarea unui obiect cu id-ul dat de la tastatura')
    print('3.Modificarea unui obiect din lista, care are acelasi id cu un nou obiect dat de la tastatura')
    print('4.Stergerea unui obiect cu id-ul dat de la tastatura')
    print('5.Mutarea unor obiecte dintr-o locatie in alta')
    print('6.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.')
    print('a.Afisarea listei de obiecte')
    print('x.Iesire')


def help():
    print('Cum poti accesa o comanda: ')
    print('1. - exemplu : 1,id(int),nume(str),descriere(str),pret_achizitie(int),locatie(str)')
    print('2. - exemplu : 2,id(int)')
    print('3. - exemplu : 3,id(int),nume(str),descriere(str),pret_achizitie(int),locatie(str)')
    print('4. - exemplu : 4,id(int)')
    print('5. - exemplu : 5,sursa(str-locatia de unde vrem sa mutam),destinatie(str-locatia unde vrem sa mutam)')
    print('6. - exemplu : 6,string(str- stringul pe care dorim sa il adaugam),pret(int-pretul cu care vom compara)')
    print('a. - exemplu : a')
    print('x. - exemplu : x')
    print('Dati comenzile urmate de datele aferente dupa modelul de mai sus separate prin ";"!')
    print('Exemplu: 2,3;a;4,1')


def handle_change_location(lista, lista_date):
    try:
        sursa = lista_date[1]
        destinatie = lista_date[2]
        return change_location(lista, sursa, destinatie)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_concatenare(lista, lista_date):
    try:
        string_citit = lista_date[1]
        pret = int(lista_date[2])
        return concatenare(lista, string_citit, pret)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def header2(lista):
    while True:
        showmenu()
        help()
        obtiuni = input('Dati sirul de obtiuni si date: ')
        lista_obtiune = obtiuni.split(sep=';')
        for element in lista_obtiune:
            lista_date = element.split(sep=',')
            obtiune = lista_date[0]
            if obtiune == '1':
                lista = handle_add(lista, lista_date)
            elif obtiune == '2':
                print(handle_read(lista, lista_date))
            elif obtiune == '3':
                lista = handle_update(lista, lista_date)
            elif obtiune == '4':
                lista = handle_delete(lista, lista_date)
            elif obtiune == '5':
                lista = handle_change_location(lista, lista_date)
            elif obtiune == '6':
                lista = handle_concatenare(lista, lista_date)
            elif obtiune == 'a':
                print(lista)
            elif obtiune == 'x':
                quit
            else:
                print('Obtiune invalida! Incearca altceva!')
        break

    return lista

