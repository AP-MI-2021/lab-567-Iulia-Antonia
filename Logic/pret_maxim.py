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


def pret_maxim_locatie(lista: list):
    """
    Creeaza o lista formata din preturile maxime ale locatiilor din lista
    :param lista: lista
    :return: lista de preturi maxime ale locatiilor
    """
    lista_pret_max = []
    locatii = location_list(lista)
    for locatie in locatii:
        pret_maxim = -1
        for element in lista:
            if get_locatie(element) == locatie:
                if pret_maxim < get_pret_achizitie(element):
                    pret_maxim = get_pret_achizitie(element)
        lista_pret_max.append(pret_maxim)
    return lista_pret_max
