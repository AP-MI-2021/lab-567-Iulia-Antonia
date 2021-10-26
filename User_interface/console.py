from Domain.obiect import  get_new_object
from Logic.crud import create, read, update, delete


def showmenu():
    print('1.Citirea unei liste noi')
    print('2.Adaugarea de elemente in lista')
    print('3.Citirea unui obiect cu id-ul dat de la tastatura')
    print('4.Modificarea unui obiect din lista, care are acelasi id cu un nou obiect dat de la tastatura')
    print('5.Stergerea unui obiect cu id-ul dat de la tastatura')
    print('x.Iesire')


def header():
    lista = []
    while True:
        showmenu()
        obtiune = input('Dati obtiunea: ')

        if obtiune == '1':
            lista = []
            numar = int(input('Dati numarul de obiecte ale listei: '))
            for pozitie in range(numar):
                id1 = int(input(f'Dati id-ul obiectului {pozitie}: '))
                nume = input(f'Dati numele obiectului {pozitie}: ')
                descriere = input(f'Dati descrierea obiectului {pozitie}: ')
                pret_achizitie = int(input(f'Dati pretul achizitiei obiectului {pozitie}: '))
                locatie = input(f'Dati locatia (formata din 4 caractere) obiectului {pozitie}: ')
                lista = create(lista, id1, nume, descriere, pret_achizitie, locatie)
            print(lista)

        elif obtiune == '2':
            numar = int(input('Dati numarul de obiecte pe care doriti sa le adaugati: '))
            for pozitie in range(numar):
                id2 = int(input(f'Dati id-ul obiectului {pozitie}: '))
                nume = input(f'Dati numele obiectului {pozitie}: ')
                descriere = input(f'Dati descrierea obiectului {pozitie}: ')
                pret_achizitie = int(input(f'Dati pretul achizitiei obiectului {pozitie}: '))
                locatie = input(f'Dati locatia (formata din 4 caractere) obiectului {pozitie}: ')
                lista = create(lista, id2, nume, descriere, pret_achizitie, locatie)
            print (lista)

        elif obtiune == '3':
            read_id = int(input('Dati id-ul obiectului pe care doriti sa il vedeti: '))
            if read(lista, read_id) is None:
                print('Id-ul citit nu corespunde vreunui element din lista!')
            else:
                print(read(lista, read_id))

        elif obtiune == '4':
            id = int(input(f'Dati id-ul obiectului pe care doriti sa il modificati: '))
            nume = input(f'Dati numele obiectului: ')
            descriere = input(f'Dati descrierea obiectului: ')
            pret_achizitie = int(input(f'Dati pretul achizitiei obiectului: '))
            locatie = input(f'Dati locatia (formata din 4 caractere) obiectului: ')
            update_obiect = get_new_object(id, nume, descriere, pret_achizitie, locatie)
            update_list = update(lista, update_obiect)
            print(update_list)

        elif obtiune == '5':
            delete_id = int(input('Dati id-ul obiectului pe care doriti sa il stergeti: '))
            new_list = delete(lista, delete_id)
            print(new_list)

        elif obtiune == 'x':
            break
        else:
            print ('Obtiune invalida. Incercati altceva!')


header()