from Domain.obiect2 import  get_new_object
from Logic.change_location import change_location
from Logic.concatenare import concatenare
from Logic.crud import create, read, update, delete


def crudmenu():
    print('1.Adaugarea unui obiect in lista')
    print('2.Afisarea unui obiect cu id-ul dat de la tastatura')
    print('3.Modificarea unui obiect din lista, care are acelasi id cu un nou obiect dat de la tastatura')
    print('4.Stergerea unui obiect cu id-ul dat de la tastatura')
    print('a.Afisarea listei de obiecte')
    print('x.Iesire din crud')


def handle_add(lista):
    try:
        id = int(input('Dati id-ul obiectului de adaugat in sir: '))
        nume = input('Dati numele obiectului de adaugat in sir: ')
        descriere = input('Dati descrierea obiectului de adaugat in sir: ')
        pret_achizitie = int(input('Dati pretul achizitiei obiectului de adaugat in sir: '))
        locatie = input('Dati locatia (formata din 4 caractere) obiectului de adaugat in sir: ')
        obiect = get_new_object(id, nume, descriere, pret_achizitie, locatie)
        return create(lista, obiect)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_read(lista):
    try:
        read_id = int(input('Dati id-ul obiectului pe care doriti sa il vedeti: '))
        if read(lista, read_id) is None:
            return 'Id-ul citit nu corespunde vreunui element din lista!'
        else:
            return read(lista, read_id)
    except ValueError as ve:
        print('Eroare: ', ve)
    return []


def handle_update(lista):
    try:
        id = int(input(f'Dati id-ul obiectului pe care doriti sa il modificati: '))
        nume = input(f'Dati numele obiectului: ')
        descriere = input(f'Dati descrierea obiectului: ')
        pret_achizitie = int(input(f'Dati pretul achizitiei obiectului: '))
        locatie = input(f'Dati locatia (formata din 4 caractere) obiectului: ')
        update_obiect = get_new_object(id, nume, descriere, pret_achizitie, locatie)
        update_list = update(lista, update_obiect)
        return update_list
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_delete(lista):
    try:
        delete_id = int(input('Dati id-ul obiectului pe care doriti sa il stergeti: '))
        new_list = delete(lista, delete_id)
        return new_list
    except ValueError as ve:
        print('Eroare:', ve)
    except TypeError as te:
        print('Eroare:', te)
    return lista


def showmenu():
    print('1.Crud')
    print('2.Mutarea unor obiecte dintr-o locatie in alta')
    print('3.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.')
    print('x.Iesire')


def handle_change_location(lista):
    try:
        sursa = input('Dati locatia sursa din care doriti sa mutati obiectele: ')
        destinatie = input('Dati locatia destinatie unde doriti sa mutati obiectele: ')
        return change_location(lista, sursa, destinatie)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_concatenare(lista):
    try:
        string_citit = input('Dati stringul pe care doriti sa il concatenati descrierilor obiectelor: ')
        pret = int(input('Dati pretul fata de care trebuie sa fie mai mare pretul obiectelor: '))
        return concatenare(lista, string_citit, pret)
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def header_crud(lista):
    while True:
        crudmenu()
        obtiune = input('Dati obtiunea: ')
        if obtiune == '1':
            lista = handle_add(lista)
        elif obtiune == '2':
            print(handle_read(lista))
        elif obtiune == '3':
            lista = handle_update(lista)
        elif obtiune == '4':
            lista = handle_delete(lista)
        elif obtiune == 'a':
            print(lista)
        elif obtiune == 'x':
            break
        else:
            print ('Obtiune invalida. Incercati altceva!')
    return lista


def header(lista):
    while True:
        showmenu()
        obtiune = input('Alegeti obtiunea: ')
        if obtiune == '1':
            header_crud(lista)
        elif obtiune == '2':
            lista = handle_change_location(lista)
        elif obtiune == '3':
            lista = handle_concatenare(lista)
        elif obtiune == 'x':
            break
        else:
            print('Obtiune invalida! Incearca altceva!')
    return lista