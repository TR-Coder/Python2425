import os
import platform
import pickle

LINE_UP = '\033[1F'
LINE_CLEAR = '\x1b[2K'
LINE_DOWN = '\033[1E'

etiquetes: list[str] = ['nom', 'telefon']
contactes: list[dict[str, str]] = []
filtre_contactes: str = ''
nom_arxiu = 'contactes.pkl'

# --------------------------------------------------------------------------------------------
def Esborra_la_terminal():
    """Neteja la terminal. Té en compte els sistema operatiu: Windows (cls) o Linux (clear).
    """
    clear_screen = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(clear_screen)
    
# --------------------------------------------------------------------------------------------
def mostra_menu(text: str, valors_valids: str, missatge_abans_input = '') -> str:
    """Fa un input(text) que admet només un caràcter. Este caracter ha de coincidir amb un
    dels caràcters en 'valors_valids'. Si no coincidix mostra el missagte de 'Error, opció incorrecta'.
    Si coincidix retorna el caràcter introduit. Addicionalment, permet mostrar el text 'missatge_abans_input'
    abans de mostrar fer l'input.
    """
    print()
    while True:
        print(LINE_DOWN + missatge_abans_input, end='')
        opcio:str = input(LINE_UP + LINE_CLEAR + text).upper()
        if opcio in valors_valids:
            return opcio
        missatge_abans_input = LINE_UP + 'Error, opció incorrecta'


# --------------------------------------------------------------------------------------------
def input_int(text: str, maxim_enter: int) -> int|None:
    """Fa un input(text). Admet i retorna valors enters entre [0, maxim].
        Si el valor introduït no és un enter o esta fora del rang [0,maxim] mostra
        el missatge d'error 'valor fora de rang' o 'valor incorrecte'.
        Retorna -1 si polsem Intro.
    """
    while True:
        try:
            opcio: str = input(LINE_CLEAR + text)
            
            if opcio.strip() == '':
                return None
            
            if 0 <= int(opcio) < maxim_enter:
                return int(opcio)
            
            print(LINE_CLEAR + 'Error, valor fora de rang' + LINE_UP, end=LINE_CLEAR)
            
        except ValueError:
            print(LINE_CLEAR + 'Error, valor incorrecte' + LINE_UP, end=LINE_CLEAR)


# --------------------------------------------------------------------------------------------
def mostra_el_menu_principal() -> str:
    """Mostra el menú principal i retorna l'opció seleccionada.
       Les opcions són: 1-Contactes i 2-Etiquetes.
    """   
    print('- MENÚ PRINCIPAL -')
    print('1- Contactes')
    print('2- Etiquetes')
    
    return mostra_menu(text='Opció? ', valors_valids='12')


# --------------------------------------------------------------------------------------------
def mostra_la_llista_etiquetes():
    """Mostra la llista de les etiquetes. Si no n'hi ha etiquetas mostra: -- No hi ha etiquetes ---
       El format de l'eixida és:
       - LLISTA D'ETIQUETES -
        (n)- nom de la etiqueta.    on n indica la posició dins de la llista.
    """
    print("- LLISTA D'ETIQUETES -")

    if not etiquetes:
        print(' -- No hi ha etiquetes --')
        return

    for n, etiqueta in enumerate(etiquetes):
        print(f'({n})- {etiqueta.capitalize()}')


# --------------------------------------------------------------------------------------------
def filtra_els_contactes() -> list[dict[str, str]]:
    """Retorna una llista dels contactes que complixen amb filtre_contactes.
    """
    if filtre_contactes == '':
        return contactes

    return [contacte for contacte in contactes if [
        valor for valor in contacte.values() if filtre_contactes in valor]]


# --------------------------------------------------------------------------------------------
def mostra_la_de_llista_contactes():
    """Mostra per pantalla la llita de contactes. Mostra també el filtre aplicat.
        Si no hi ha contactes indica -- No hi ha contactes --.
        El format de l'eixida és:
        - LLISTA DE CONTACTES - Filtre:
        (n)- {'clau1': 'valor1', 'clau2': 'valor2'}
    """
    Esborra_la_terminal()
    
    print(f'- LLISTA DE CONTACTES - Filtre: {filtre_contactes}')
    print('==============================================')

    contactes_filtrats = filtra_els_contactes()

    if not contactes_filtrats:
        print('\n- No hi ha contactes -')
        return

    for n, contacte in enumerate(contactes_filtrats):
        print(f"({n})- ", end='')
        for k,v in contacte.items():
            print(f'{k}:{v}, ', end='')
        print('')

# --------------------------------------------------------------------------------------------
def canvia_etiqueta_en_tots_els_contactes(etiqueta_antiga:str, etiqueta_nova:str) -> list[dict[str, str]]:
    
    contactes_nous: list[dict[str, str]] = []

    for contacte in contactes:
        contacte_nou: dict[str, str] = {}
        for etiqueta,valor in contacte.items():
            etq = etiqueta_nova if etiqueta == etiqueta_antiga else etiqueta
            contacte_nou[etq]=valor
        contactes_nous.append(contacte_nou)
            
    return contactes_nous
  
# --------------------------------------------------------------------------------------------
def esta_en_us(etiqueta) -> bool:
    for contacte in contactes:
        for etiqueta_contacte in contacte:
            if etiqueta_contacte == etiqueta:
                return True
    return False

# --------------------------------------------------------------------------------------------
def gestiona_les_etiquetes() -> None:
    """Esta funció es qui fa la feina de crear, esborrar i modificar etiquetes.
    mostra_llista_etiquetes() i mostra el menú d'etiquetes: (C)rea, (E)sborra, (M)odifica.
    """
    msg_error:str = ''
    
    while True:
        Esborra_la_terminal()
        
        mostra_la_llista_etiquetes()
        
        opcio = mostra_menu(text='(C)rea, (E)sborra, (M)odifica? ', valors_valids='CEM', missatge_abans_input=msg_error)
        
        msg_error = ''

        if opcio == '':
            break
        
        if opcio == 'C':
            etiqueta: str = input(LINE_CLEAR + 'Nom de la nova etiqueta: ').lower()
            
            if etiqueta in etiquetes:
                msg_error =  'Error, la etiqueta ja existix'
                continue
            
            if etiqueta.strip() == '':
                msg_error = "Error, el nom de l'etiqueta no pot estar en blanc"
                continue
            
            etiquetes.append(etiqueta)
            
        elif opcio == 'E':
            posicio:int|None = input_int('Etiqueta a esborrar? ', maxim_enter=len(etiquetes))
            
            if not posicio:
                continue
            
            if esta_en_us(etiqueta=etiquetes[posicio]):
                msg_error = 'Error, etiqueta en ús en algun contacte'
                continue
            
            etiquetes.pop(posicio)
            
        elif opcio == 'M':
            posicio = input_int(text='Etiqueta a modificar? ', maxim_enter=len(etiquetes))
            
            if not posicio:
                continue
            
            etiqueta = input(LINE_CLEAR + "Nou nom de l'etiqueta: ").lower()
            
            if etiqueta in etiquetes:
                msg_error =  "Error, l'etiqueta ja existix"
                continue
            
            if etiqueta.strip() == '':
                msg_error = "Error, el nom de l'etiqueta no pot estar en blanc"
                continue
            
            global contactes
            contactes = canvia_etiqueta_en_tots_els_contactes(etiqueta_antiga=etiquetes[posicio], etiqueta_nova=etiqueta)
            etiquetes[posicio] = etiqueta
        
        grava_en_disc()

# --------------------------------------------------------------------------------------------
def demana_llista_etiquetes_contacte() -> list[int]:
    """ Pregunta a l'usuari les etiquetes que volem aplicar a un contacte. Retorna una llista amb el nombre de cadascuna
    d'este etiquetes, per exemple [0,2]. Elimina les duplicitats [2,2] és [2]. Retorna la llista en ordre.
    """
    while True:
        
        etiquetes_aplicar: str = input(LINE_CLEAR + 'Indica les etiquetes a aplicar (Intro totes)? ')
        
        # Polsar intro indica que volem aplicar totes les etiquetes. Retornarem una llista amb la numeració
        # de totes les etiquetes, per explemple [0,1,2,3,4].
        if not etiquetes_aplicar.strip():
            return list(range(len(etiquetes)))
        
        conjunt = set()     # Creem un conjunt per a eliminar possibles duplicitats.
        
        try:
            for item in list(etiquetes_aplicar):
                if int(item) < 0 or int(item) >= len(etiquetes):
                    print(LINE_CLEAR + 'Error, etiqueta fora de límit' + LINE_UP, end=LINE_CLEAR)
                    break
                conjunt.add(int(item))
            else:
                return(sorted(conjunt))
        except:
            print(LINE_CLEAR + 'Etiqueta incorrecta' + LINE_UP, end=LINE_CLEAR)


# --------------------------------------------------------------------------------------------
def crea_un_contacte() -> None:
    """mostra_llista_etiquetes(), demana a l'usuari que d'indique les etiquetes del nou contacte
    i per cada una d'este etiquetes li demana un valor.
    """
    contacte: dict[str, str] = {}       # Nou contacte
    
    print()
    mostra_la_llista_etiquetes()
    
    llista_etiquetes: list[int] = demana_llista_etiquetes_contacte()
    
    for item in llista_etiquetes:
        clau = etiquetes[item]
        valor = input(LINE_CLEAR + f'{clau}? ')
        contacte[clau] = valor

    contactes.append(contacte)

# --------------------------------------------------------------------------------------------
def modifica_el_contacte(posicio: int):
    """Modifica el contacte situat en posicio. Recorre les etiquetes i demana un nou valor.
        Si polsem Intro no modifica el seu valor i passa a la següent etiqueta.
    """
    print(LINE_CLEAR, end='')
    contacte = contactes[posicio]
    for clau in contacte.keys():
        valor = input(LINE_CLEAR + f'{clau}? ')
        if valor != '':
            contacte[clau] = valor


# --------------------------------------------------------------------------------------------
def gestiona_els_contactes() -> None:
    """ Esta funció es qui fa la feina de crear, esborrar, modificar i filtrar els contactes.
    mostra_llista_contactes() i mostra el menú de contactes: (C)rea, (E)sborra, (M)odifica, (F)iltra?
    """
    while True:
        
        mostra_la_de_llista_contactes()
        
        opcio = mostra_menu(text='(C)rea, (E)sborra, (M)odifica, (F)iltra? ', valors_valids='CEMF')
       
        if opcio == '':
            break
        
        elif opcio == 'C':
            crea_un_contacte()
            
        elif opcio == 'E':
            posicio: int|None = input_int(text='Contacte a esborrar? ', maxim_enter=len(contactes))
            if not posicio:
                continue
            contactes.pop(posicio)
            
        elif opcio == 'M':
            posicio = input_int(text='Contacte a modificar? ', maxim_enter=len(contactes))
            
            if not posicio:
                continue
            
            modifica_el_contacte(posicio)
            
        elif opcio == 'F':
            global filtre_contactes
            filtre_contactes = input(LINE_CLEAR + 'Filtre a aplicar (Intro=Esborra filtre)? ')
        
        grava_en_disc()

# --------------------------------------------------------------------------------------------
def llig_de_disc():
    """LLig de la memòria secundària les etiquetes i els contactes
    """
    global etiquetes
    global contactes
    try:
        with open(nom_arxiu, 'rb') as fd1:
            etiquetes = pickle.load(fd1)
            contactes = pickle.load(fd1)
    except FileNotFoundError:
        with open(nom_arxiu, 'wb') as fd2:
            pickle.dump(etiquetes, fd2)
            pickle.dump(contactes, fd2)    

# --------------------------------------------------------------------------------------------
def grava_en_disc():
    """Grava en la memòria secundària les etiquetes i els contactes
    """
    global etiquetes
    global contactes
    with open(nom_arxiu, 'wb') as fd:
        pickle.dump(etiquetes, fd)
        pickle.dump(contactes, fd)

# --------------------------------------------------------------------------------------------
# Mostra el menu principal cridant a gestiona_contactes() i gestiona_etiquetes().
# Inicialment entre en el menú de contactes directament.
# --------------------------------------------------------------------------------------------

llig_de_disc()
    
while True:
    Esborra_la_terminal()
    opcio = mostra_el_menu_principal()
    if opcio == '1':
        gestiona_els_contactes()
    elif opcio == '2':
        gestiona_les_etiquetes()
