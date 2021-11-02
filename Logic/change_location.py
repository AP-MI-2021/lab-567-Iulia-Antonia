from Domain.obiect2 import get_locatie, get_new_object, get_id, get_nume, get_descriere, get_pret_achizitie


def change_location(lista: list, sursa: str, destinatie: str):
    """
    Muta obiectele dintr-o anumita locatie, intr-o alta locatie
    :param lista: lista ce contine obiectele
    :param sursa: locatia de unde vrem sa mutam
    :param destinatie: locatia unde vrem sa mutam
    :return: lista cu obiectele mutate din locatia sursa, in locatia destinatie
    """
    if sursa == '' or destinatie == '' or len(sursa) != 4 or len(destinatie) != 4:
        raise ValueError('Dati locatiile sursa si destinatie nenule, de exact 4 caractere')
    rezultat = []
    for element in lista:
        if get_locatie(element) != sursa:
            rezultat.append(element)
        else:
            id = get_id(element)
            nume = get_nume(element)
            descriere = get_descriere(element)
            pret_achizitie = get_pret_achizitie(element)
            obiect = get_new_object(id, nume, descriere, pret_achizitie, destinatie)
            rezultat.append(obiect)
    return rezultat