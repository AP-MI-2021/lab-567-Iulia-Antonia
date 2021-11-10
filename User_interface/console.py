from Domain.obiect2 import get_new_object
from Logic.change_location import change_location
from Logic.concatenare import concatenare
from Logic.crud import create, read, update, delete
from Logic.ordonare import ordonare_lista
from Logic.pret_maxim import location_list, pret_maxim_locatie
from Logic.sume_pret import suma_pret_locatie
from Logic.undo_redo import list_versions, undo, redo


def handle_undo(current_version):
    current_version = undo(current_version)
    if current_version > 1:
        return current_version
    else:
        print('Ati ajuns la prima versiune!')
    return current_version


def handle_redo(versions_list, current_version):
    current_version = redo(versions_list, current_version)
    if current_version != len(versions_list):
        return current_version
    else:
        print('Ati ajuns la ultima versiune!')
    return current_version


def crudmenu():
    print('1.Adaugarea unui obiect in lista')
    print('2.Afisarea unui obiect cu id-ul dat de la tastatura')
    print('3.Modificarea unui obiect din lista, care are acelasi id cu un nou obiect dat de la tastatura')
    print('4.Stergerea unui obiect cu id-ul dat de la tastatura')
    print('a.Afisarea listei de obiecte')
    print('x.Iesire din crud')


def handle_add(lista):
    try:
        id1 = int(input('Dati id-ul obiectului de adaugat in sir: '))
        nume = input('Dati numele obiectului de adaugat in sir: ')
        descriere = input('Dati descrierea obiectului de adaugat in sir: ')
        pret_achizitie = int(input('Dati pretul achizitiei obiectului de adaugat in sir: '))
        locatie = input('Dati locatia (formata din 4 caractere) obiectului de adaugat in sir: ')
        obiect = get_new_object(id1, nume, descriere, pret_achizitie, locatie)
        print('Obiect adaugat cu succes!')
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
        id1 = int(input(f'Dati id-ul obiectului pe care doriti sa il modificati: '))
        nume = input(f'Dati numele obiectului: ')
        descriere = input(f'Dati descrierea obiectului: ')
        pret_achizitie = int(input(f'Dati pretul achizitiei obiectului: '))
        locatie = input(f'Dati locatia (formata din 4 caractere) obiectului: ')
        update_obiect = get_new_object(id1, nume, descriere, pret_achizitie, locatie)
        update_list = update(lista, update_obiect)
        print('Obiect modificat cu succes!')
        return update_list
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def handle_delete(lista):
    try:
        delete_id = int(input('Dati id-ul obiectului pe care doriti sa il stergeti: '))
        new_list = delete(lista, delete_id)
        print('Obiect sters cu succes!')
        return new_list
    except ValueError as ve:
        print('Eroare:', ve)
    except TypeError as te:
        print('Eroare:', te)
    return lista


def showmenu():
    print('1.Crud')
    print('2.Mutarea unor obiecte dintr-o locatie in alta.')
    print('3.Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.')
    print('4.Determinarea celui mai mare pret pentru fiecare locatie.')
    print('5.Ordonarea obiectelor crescător după prețul de achiziție.')
    print('6.Afișarea sumelor prețurilor pentru fiecare locație.')
    print('7.Undo.')
    print('8.Redo.')
    print('a.Afisarea listei.')
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


def handle_pret_max_locatii(lista):
    try:
        lista_locatii = location_list(lista)
        pret_max_list = pret_maxim_locatie(lista)
        for pozitie in range(len(lista_locatii)):
            print(f'Cel mai mare pret din locatia {lista_locatii[pozitie]} este {pret_max_list[pozitie]}')
    except ValueError:
        print('Eroare: ', 'Dati o lista corecta!')
    return lista


def handle_ordonare(lista):
    try:
        return ordonare_lista(lista)
    except ValueError:
        print('Eroare: ', 'Dati o lista corecta')
    return lista


def handle_sume_preturi(lista):
    try:
        lista_locatii = location_list(lista)
        for locatie in lista_locatii:
            print(f'Suma preturilor din locatia {locatie} este {suma_pret_locatie(lista, locatie)}.')
    except ValueError as ve:
        print('Eroare: ', ve)
    return lista


def header_crud(lista, versions_list, current_version):
    while True:
        crudmenu()
        obtiune = input('Dati obtiunea: ')
        if obtiune == '1':
            lista = handle_add(lista)
            versions_list, current_version = list_versions(versions_list, current_version, lista)
        elif obtiune == '2':
            print(handle_read(lista))
        elif obtiune == '3':
            lista = handle_update(lista)
            versions_list, current_version = list_versions(versions_list, current_version, lista)
        elif obtiune == '4':
            lista = handle_delete(lista)
            versions_list, current_version = list_versions(versions_list, current_version, lista)
        elif obtiune == 'a':
            print(lista)
        elif obtiune == 'x':
            break
        else:
            print('Obtiune invalida. Incercati altceva!')
    return lista, versions_list, current_version


def header(lista):
    versions_list = [lista]
    current_version = 1
    while True:
        showmenu()
        obtiune = input('Alegeti obtiunea: ')
        if obtiune == '1':
            lista, versions_list, current_version = header_crud(lista, versions_list, current_version)
        elif obtiune == '2':
            lista = handle_change_location(lista)
            print('Locatiile au fost schimbate cu succes!')
            versions_list, current_version = list_versions(versions_list, current_version, lista)
        elif obtiune == '3':
            lista = handle_concatenare(lista)
            print('Lista a fost modificata cu succes!')
            versions_list, current_version = list_versions(versions_list, current_version, lista)
        elif obtiune == '4':
            handle_pret_max_locatii(lista)
            print('Cerinta a fost indeplinita cu succes!')
        elif obtiune == '5':
            lista = handle_ordonare(lista)
            print('Lista a fost ordonata cu succes!')
            versions_list, current_version = list_versions(versions_list, current_version, lista)
        elif obtiune == '6':
            handle_sume_preturi(lista)
            print('Cerinta a fost indeplinita cu succes!')
        elif obtiune == '7':
            current_version = handle_undo(current_version)
            lista = versions_list[current_version - 1]
            print('Undo efectuat cu succes!')
        elif obtiune == '8':
            current_version = handle_redo(versions_list, current_version)
            lista = versions_list[current_version - 1]
            print('Redo efectuat cu succes!')
        elif obtiune == 'a':
            print(lista)
        elif obtiune == 'x':
            break
        else:
            print('Obtiune invalida! Incearca altceva!')
    return lista
