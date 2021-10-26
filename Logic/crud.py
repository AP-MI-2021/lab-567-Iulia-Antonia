from Domain.obiect import get_new_object, get_id


def create(lista_obiecte: list, _id: int, _nume: str, _descriere: str, _pret_achizitie: int, _locatie: str):
    obiect = get_new_object(_id, _nume, _descriere, _pret_achizitie, _locatie)
    return lista_obiecte + [obiect]


def read(lista_obiecte: list, id_obiect: int = None):
    obiect_gasit = None
    if id_obiect is None:
        return lista_obiecte
    for obiect in lista_obiecte:
        if get_id(obiect) == id_obiect:
            obiect_gasit = obiect
    return obiect_gasit


def update(lista_obiecte, new_object):
    rezultat = []
    for obiect in lista_obiecte:
        if get_id(obiect) == get_id(new_object):
            rezultat.append(new_object)
        else:
            rezultat.append(obiect)
    return rezultat


def delete(lista_obiecte, id_obiect: int):
    rezultat = []
    for obiect in lista_obiecte:
        if get_id(obiect) != id_obiect:
            rezultat.append(obiect)
    return rezultat
