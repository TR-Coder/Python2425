import os
import platform

# https://www.geeksforgeeks.org/ordereddict-in-python/
# https://realpython.com/python-ordereddict/
from collections import OrderedDict

LINE_UP = '\033[1F'
LINE_CLEAR = '\x1b[2K'
LINE_DOWN = '\033[1E'

etiquetes: list[str] = ['nom', 'telefon']
contactes: list[dict[str, str]] = []
filtre_contactes: str = ''


def neteja_pantalla():
    """Neteja la terminal (cls o clear). Té en compte els sistema operatiu (Windows,Linux)"""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def opcio_menu(text: str, valors_valids: str, msg_error = '') -> str:
    """Fa un input(text). Admet i retorna Intro o un dels caràcters que estan en valors_valids.
    Si el caràcter és invàlid mostra un missagte d'opció incorrecta. Permet mostrar un missatge 
    que li passem que es mostrarà daval de l'input."""
    print()
    while True:
        print(LINE_DOWN + msg_error, end='')
        opcio: str = input(LINE_UP + LINE_CLEAR + text).upper()
        if opcio in valors_valids:
            return opcio
        msg_error = LINE_UP + 'Error, opció incorrecta'


def opcio_entera(text: str, maxim: int) -> int:
    """Fa un input(text). Admet i retorna valors enters entre [0, maxim].
        Si el valor introduït no és un enter o esta fora del rang [0,maxim] mostra
        un missatge d'error de valor fora de rang o valor incorrecte si no és un nombre.
        Retorna -1 si polsem Intro.
    """
    while True:
        try:
            opcio: str = input(LINE_CLEAR + text)
            if opcio == '':
                return -1
            if 0 <= int(opcio) < maxim:
                return int(opcio)
            print(LINE_CLEAR + 'Error, valor fora de rang' + LINE_UP, end=LINE_CLEAR)
        except ValueError:
            print(LINE_CLEAR + 'Error, valor incorrecte' + LINE_UP, end=LINE_CLEAR)


def mostra_menu_principal() -> str:
    """Mostra el menú principal i retorna l'opció seleccionada.
        Les opcions són: 1-Contactes i 2-Etiquetes.
        """
    print('- MENÚ PRINCIPAL -')
    print('1- Contactes')
    print('2- Etiquetes')
    return opcio_menu('Opció? ', '12')


def mostra_llista_etiquetes():
    """Mostra la llista de les etiquetes. Si no n'hi ha etiquetas mostra: -- No hi ha etiquetes ---
       El format de l'eixida és:
       - LLISTA D'ETIQUETES -
        (n)- nom de la etiqueta.    on n indica la posició dins de la llista.
    """
    print("- LLISTA D'ETIQUETES -")

    if len(etiquetes) == 0:
        print(' -- No hi ha etiquetes --')
        return

    for n, etiqueta in enumerate(etiquetes):
        print(f'({n})- {etiqueta.capitalize()}')


def filtra_contactes() -> list[dict[str, str]]:
    """
        Retorna una llista dels contactes que complixen amb filtre_contactes.
    """
    if filtre_contactes == '':
        return contactes

    return [contacte for contacte in contactes if [
        valor for valor in contacte.values() if filtre_contactes in valor]]


def mostra_llista_contactes():
    """Mostra per pantalla la llita de contactes. Mostra també el filtre aplicat.
        Si no hi ha contactes indica -- No hi ha contactes --.
        El format de l'eixida és:
        - LLISTA DE CONTACTES - Filtre:
        (n)- {'clau1': 'valor1', 'clau2': 'valor2'}
    """
    neteja_pantalla()
    print(f'- LLISTA DE CONTACTES - Filtre: {filtre_contactes}')

    contactes_filtrats = filtra_contactes()

    if len(contactes_filtrats) == 0:
        print('\n- No hi ha contactes -')
        return

    # Per al print hem de traure la informació del OrderedDict
    for n, contacte in enumerate(contactes_filtrats):
        print(f"({n})- ", end='')
        for k,v in contacte.items():
            print(f'{k}:{v}, ', end='')
        print()


def canviar_etiqueta_en_contactes(etiqueta_canviar:str, etiqueta_nova:str) -> list[dict[str, str]]:
    contactes_nous: list[dict[str, str]] = []

    for i, contacte in enumerate(contactes):
        contacte_nou: dict[str, str] = OrderedDict()
        for etq,valor in contacte.items():
            etiqueta = etiqueta_nova if etq == etiqueta_canviar else etq
            contacte_nou[etiqueta]=valor
        contactes_nous.append(contacte_nou)
            
    return contactes_nous

  
def etiqueta_en_us(etiqueta_buscar) -> bool:
    for contante in contactes:
        for etiqueta in contante:
            if etiqueta == etiqueta_buscar:
                return True
    return False

def gestiona_etiquetes():
    """
    Neteja_pantalla(), mostra_llista_etiquetes() i mostra el menú d'etiquetes cridant
    a opcio_menu(). Les opcions són: (C)rea, (E)sborra, (M)odifica.
    Esta funció es qui fa la feina de crear, esborrar i modificar etiquetes.
    """
    msg_error:str = ''
    while True:
        neteja_pantalla()
        mostra_llista_etiquetes()

        opcio = opcio_menu('(C)rea, (E)sborra, (M)odifica? ', 'CEMF', msg_error)
        msg_error = ''

        if opcio == '':
            break
        elif opcio == 'C':
            etiqueta: str = input(LINE_CLEAR + 'Nom de la nova etiqueta: ').lower()
            if etiqueta in etiquetes:
                msg_error =  'Error, la etiqueta ja existix'
                continue
            if etiqueta.strip() == '':
                msg_error = "Error, el nom de l'etiqueta no pot estar en blanc"
                continue
            etiquetes.append(etiqueta)
        elif opcio == 'E':
            posicio: int = opcio_entera('Etiqueta a esborrar? ', len(etiquetes))
            if posicio == -1:
                continue
            if etiqueta_en_us(etiquetes[posicio]):
                msg_error = 'Error, etiqueta en ús en algun contacte'
                continue
            etiquetes.pop(posicio)
        elif opcio == 'M':
            posicio: int = opcio_entera('Etiqueta a modificar? ', len(etiquetes))
            if posicio == -1:
                continue
            etiqueta = input(LINE_CLEAR + 'Nou nom de la etiqueta: ').lower()
            if etiqueta in etiquetes:
                msg_error =  'Error, la etiqueta ja existix'
                continue
            if etiqueta.strip() == '':
                msg_error = "Error, el nom de l'etiqueta no pot estar en blanc"
                continue
            
            global contactes
            contactes = canviar_etiqueta_en_contactes(etiquetes[posicio], etiqueta)
            etiquetes[posicio] = etiqueta


def demana_llista_etiquetes() -> list[int]:
    """
     Pregunta per pantalla: Indica les etiquetes a aplicar (Intro totes)? 
     Retorna una llista amb el nombre de les etiquetes, per exemple [0,2] o
     [] en el cas d'Intro. Elimina les duplicitats [2,2] és [2]. 
     Retorna la llista en ordre.
    """
    while True:
        nombre_etiquetes: str = input(LINE_CLEAR + 'Indica les etiquetes a aplicar (Intro totes)? ')
        conjunt = set()
        try:
            for item in list(nombre_etiquetes):
                if int(item) < 0 or int(item) >= len(etiquetes):
                    print(LINE_CLEAR + 'Error, etiqueta fora de límit' + LINE_UP, end=LINE_CLEAR)
                    break
                conjunt.add(int(item))
            else:
                return(sorted(conjunt))
        except:
            print(LINE_CLEAR + 'Etiqueta incorrecta' + LINE_UP, end=LINE_CLEAR)


def crea_contacte():
    """crida a mostra_llista_etiquetes(). Recorre la llista que retorna i
       crea el contacte només amb les etiquetes indicades per l'usuari.
       o si ha si ha retornat [] el contacte tidrà totes les etiquetes.
    """
    print()
    mostra_llista_etiquetes()
    llista_etiquetes: list[int] = demana_llista_etiquetes()

    contacte: dict[str, str] = OrderedDict()

    if not llista_etiquetes:
        for etiqueta in etiquetes:
            valor = input(LINE_CLEAR + f'{etiqueta}? ')
            contacte[etiqueta] = valor
    else:
        for item in llista_etiquetes:
            clau = etiquetes[item]
            valor = input(LINE_CLEAR + f'{clau}? ')
            contacte[clau] = valor

    contactes.append(contacte)


def modifica_contacte(posicio: int):
    """Modifica el contacte situat en posicio. Recorre les etiquetes i demana un nou valor.
        Si polsem Intro no modifica el seu valor i passa a la següent etiqueta.
    """
    print(LINE_CLEAR, end='')
    contacte = contactes[posicio]
    for clau in contacte.keys():
        valor = input(LINE_CLEAR + f'{clau}? ')
        if valor != '':
            contacte[clau] = valor


def gestiona_contactes():
    """crida a mostra_llista_contactes() i mostra el menú de contactes cridant
        a opcio_menu(): (C)rea, (E)sborra, (M)odifica, (F)iltra?
        Esta funció es qui fa la feina de crear, esborrar, modificar i filtrar etiquetes.
    """
    while True:
        mostra_llista_contactes()
        opcio = opcio_menu('(C)rea, (E)sborra, (M)odifica, (F)iltra? ', 'CEMF')
        if opcio == '':
            break
        elif opcio == 'C':
            crea_contacte()
        elif opcio == 'E':
            posicio: int = opcio_entera('Contacte a esborrar? ', len(contactes))
            if posicio == -1:
                continue
            contactes.pop(posicio)
        elif opcio == 'M':
            posicio: int = opcio_entera('Contacte a modificar? ', len(contactes))
            if posicio == -1:
                continue
            modifica_contacte(posicio)
        elif opcio == 'F':
            global filtre_contactes
            filtre_contactes = input(LINE_CLEAR + 'Filtre a aplicar (Intro=cap filtre)? ')


# Mostra el menu principal cridant a gestiona_contactes() i gestiona_etiquetes().
# Inicialment entre en el menú de contactes directament.
while True:
    neteja_pantalla()
    opcio = mostra_menu_principal()
    if opcio == '1':
        gestiona_contactes()
    elif opcio == '2':
        gestiona_etiquetes()


# def neteja_pantalla():

# def opcio_menu(text: str, valors_valids: str, msg_error: str) -> str:

# def opcio_entera(text: str, maxim: int) -> int:

# def mostra_menu_principal() -> str:
# 	opcio_menu()


# def mostra_llista_etiquetes():

# def filtra_contactes() -> list[dict[str, str]]:


# def mostra_llista_contactes():
# 	neteja_pantalla()
# 	filtra_contactes()


# def gestiona_etiquetes():
# 	neteja_pantalla()
# 	mostra_llista_etiquetes()
# 	opcio_entera()

# def demana_llista_etiquetes() -> list[int]:

# def crea_contacte():
# 	mostra_llista_etiquetes()
# 	demana_llista_etiquetes()

# def modifica_contacte(posicio: int):
	
	
# def gestiona_contactes():
# 	mostra_llista_contactes()
# 	opcio_menu()
# 	crea_contacte()
# 	opcio_entera()
# 	modifica_contacte()

# Punt entrada programa
#     neteja_pantalla()
#     mostra_menu_principal()
#     gestiona_contactes()
#     gestiona_etiquetes()


# ----------------------------------------
# EXEMPLE DE FUNCIONAMENT DE OrderedDict()
# ----------------------------------------

# d = {'a':1, 'b':2, 'c':3}
# d2 = {('xxx', v) if k == 'a' else (k, v) for k, v in d.items()}
# print(d,d2)

# d = OrderedDict([('a', 1), ('c', 3), ('b', 2)])
# d = OrderedDict({'a':1, 'b':2, 'c':3})
# d2 = OrderedDict([('xxx', v) if k == 'a' else (k, v) for k, v in d.items()])
# print(d,d2)

# # Per a mostrar els valors de diccionari en un print:
# for k,v in d2.items():
#     print(k,v)
