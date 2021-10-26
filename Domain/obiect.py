
def get_new_object(_id: int, _nume: str, _descriere: str, _pret_achizitie: int, _locatie: str):
    obiect = {
        'id': _id,
        'nume': _nume,
        'descriere': _descriere,
        'pret_achizitie': _pret_achizitie,
        'locatie': _locatie.zfill(4)
    }
    return obiect


def get_id(obiect):
    return obiect['id']


def get_nume(obiect):
    return obiect['nume']


def get_descriere(obiect):
    return obiect['descriere']


def get_pret_achizitie(obiect):
    return obiect['pret-achizite']


def get_locatie(obiect):
    return obiect['locatie']


def get_object_string(obiect):
    return f'Obiect cu ID-ul {get_id(obiect)}, cu numele {get_nume(obiect)}, decrierea {get_descriere(obiect)}, ' \
           f'pretul achizitiei {get_pret_achizitie(obiect)} si locatia {get_locatie(obiect)}'
