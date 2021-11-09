from Domain.obiect2 import get_pret_achizitie


def ordonare_lista(lista: list):
    return sorted(lista, key=get_pret_achizitie)
