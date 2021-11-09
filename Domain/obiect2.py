def get_new_object(_id: int, _nume: str, _descriere: str, _pret_achizitie: int, _locatie: str):
    if type(_id) is not int:
        raise ValueError('ID-ul trebuie sa fie un numar intreg!')
    if type(_pret_achizitie) is not int:
        raise ValueError('Pretul achizitiei trebuie sa fie un numar intreg!')
    if len(_locatie) != 4:
        raise ValueError('Locatia trebuie sa aiba exact 4 caractere!')
    if _pret_achizitie < 0:
        raise ValueError('Pretul achizitiei trebuie sa fie un numar intreg, pozitiv!')
    obiect = [_id, _nume, _descriere, _pret_achizitie, _locatie]
    return obiect


def get_id(obiect):
    return obiect[0]


def get_nume(obiect):
    return obiect[1]


def get_descriere(obiect):
    return obiect[2]


def get_pret_achizitie(obiect):
    return obiect[3]


def get_locatie(obiect):
    return obiect[4]


def get_object_string(obiect):
    return f'Obiect cu ID-ul {get_id(obiect)}, cu numele {get_nume(obiect)}, decrierea {get_descriere(obiect)}, ' \
           f'pretul achizitiei {get_pret_achizitie(obiect)} si locatia {get_locatie(obiect)}'
