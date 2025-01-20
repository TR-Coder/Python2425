# --------------------------------------------------------------------------------------------
# Manteniment d'un diccionari.
# --------------------------------------------------------------------------------------------
#
#  Modificar el programa anterior utilitzant estes funcions:
#   Afegir_qualificació

def mostra_menu() -> str:
    print()
    print(qualificacions)
    print('    MENU')
    print('-------------')
    print('A- afegir')
    print('E- esborrar')
    print('M- modificar nota')
    print('C- modificar nom assignatura')
    print('Q- Acabar')

    return input('Opció? ').upper()


def input_assignatura(txt: str) -> str:
    '''Fa un input(txt). Elimina espais en blanc i posa caracter en majúscula'''

def input_nota(txt: str) -> float:
    '''Fa un input(txt)'''

def esta_en_qualificacions(nom_assignatura: str) -> bool:
    '''Comprobar si nom_assignatura està en el diccionari de qualificacions'''


def mostrar_missatge_error(txt: str) -> None:
    '''Mostra el missatge txt per pantalla (un print)'''


def afegix_qualificacio() -> None:
    '''Afegix al diccionari un nom d'assignatura i la nota. Demana nom i nota.
    Podem introduir multiples assignatures/nota (bucle) fins polsar INTRO.
    No podem repetir el nom d'una assignatura. Si ho intentem mostra un missatge d'error.
    '''


def esborra_assignatura() -> None:
    '''Demana el nom d'una assignatura i l'esborra del diccionari.
    No podem esborrar una assignatura que no existix.  Si ho intentem mostra un missatge d'error.
    '''



def modifica_nota_assignatura() -> None:
    ''' Modifica la nota d'una assignatura.
    Demana el nom d'una assignatura i una nota.
    Si l'assignatura no existix mostra un missatge d'error.
    '''
   

def modifica_nom_assignatura():
    '''Permet canviar el nom d'una assignatura.
    Demana el nom actual d'una assignatura i el nou nom.
    Si l'assignatura no existix mostra un missatge d'error.
    No podem canviar el nom si eixe nom ja està en el diccionari.
    '''


qualificacions:dict = {}

while True:

    opcio = mostra_menu()

    if opcio == 'Q':
        break
    elif opcio == '':
        pass
    elif opcio == 'A':
        afegix_qualificacio()
    elif opcio == 'E':
        esborra_assignatura()
    elif opcio == 'M':
        modifica_nota_assignatura()
    elif opcio == 'C':
        modifica_nom_assignatura()
    else:
        mostrar_missatge_error("opció incorrecta")








