from Domain.obiect2 import get_locatie, get_pret_achizitie


def location_list(lista: list):
    """
    Formeaza o lista ce contine doar locatiile diferite ale obiectelor dintr-o lista
    :param lista: lista
    :return: lista de locatii
    """
    rezultat_final = []
    for element in lista:
        if get_locatie(element) not in rezultat_final:
            rezultat_final.append(get_locatie(element))
    return rezultat_final


def suma_pret_locatie(lista: list, locatie: str):
    """
    Calculeaza suma preturilor dintr-o anumita locatie data, ale unei liste
    :param lista: lista data
    :param locatie: locatia preturilor de insumat
    :return: suma preturilor obiectelor din lista care au locatia locatie
    """
    if len(locatie) != 4:
        raise ValueError('Locatia trebuie sa fie un sir de exact 4 caractere!')
    suma = 0
    for element in lista:
        if get_locatie(element) == locatie:
            suma = suma + get_pret_achizitie(element)
    return suma
