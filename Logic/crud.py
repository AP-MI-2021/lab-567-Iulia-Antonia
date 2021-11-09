from Domain.obiect2 import get_id, get_locatie, get_pret_achizitie


def create(lista_obiecte: list, obiect: list):
    """
    Adauga in lista un nou obiect
    :param lista_obiecte: lista existenta
    :param obiect: obiectul de adaugat
    :return: - lista_obiecte in care a adaugat obiectul obiect
             - eroarea si motivul ei
    """
    if type(get_id(obiect)) is not int:
        raise ValueError('ID-ul trebuie sa fie un numar intreg!')
    if len(get_locatie(obiect)) != 4:
        raise ValueError('Locatia trebuie sa fie formata din exact 4 caractere')
    if get_pret_achizitie(obiect) < 0:
        raise ValueError('Pretul achizitiei trebuie sa fie un numar intreg, pozitiv!')
    for element in lista_obiecte:
        if get_id(element) == get_id(obiect):
            raise ValueError(f'Elementul cu id-ul {get_id(obiect)} exista deja in lista')
    return lista_obiecte + [obiect]


def read(lista_obiecte: list, id_obiect: int = None):
    """
    Verifica daca un obiect dat printr-un id este in lista, si il transmite
    :param lista_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului cautat
    :return: - obiect_gasit - obiectul cu id_obiect din lista, daca acesta exista
             - lista intreaga daca id_obiect nu are data o valoare
             - eroarea si tipul ei - daca nu exista niciun obiect cu id_obiect in lista
    """
    if id_obiect is None:
        return lista_obiecte
    obiect_gasit = None
    for obiect in lista_obiecte:
        if get_id(obiect) == id_obiect:
            obiect_gasit = obiect
    if obiect_gasit is None:
        raise ValueError(f'Nu exista niciun element cu id-ul {id_obiect} in lista')
    return obiect_gasit


def update(lista_obiecte, new_object):
    """
    Modifica un obiect din lista
    :param lista_obiecte: lista de obiecte
    :param new_object: obiectul pe care dorim sa il modificam
    :return: lista cu obiectul actualizat
    """
    gasit = False
    for element in lista_obiecte:
        if get_id(element) == get_id(new_object):
            gasit = True
    if not gasit:
        raise ValueError(f'Elementul cu id-ul {get_id(new_object)} nu exista in lista')
    rezultat = []
    for obiect in lista_obiecte:
        if get_id(obiect) == get_id(new_object):
            rezultat.append(new_object)
        else:
            rezultat.append(obiect)
    return rezultat


def delete(lista_obiecte, id_obiect: int):
    """
    Sterge obiectul cu un id dat din lista
    :param lista_obiecte: lista de obiecte
    :param id_obiect: id-ul obiectului pe care vrem sa il stergem
    :return: lista fara obiectul cu id-ul id_obiect
    """
    if type(id_obiect) is not int:
        raise TypeError('Dati id-ul un numar intreg!')
    gasit = True
    for element in lista_obiecte:
        if get_id(element) == id_obiect:
            gasit = True
    if gasit is False:
        raise ValueError(f'Elementul cu id-ul {id_obiect} nu exista in lista')
    rezultat = []
    for obiect in lista_obiecte:
        if get_id(obiect) != id_obiect:
            rezultat.append(obiect)
    return rezultat
