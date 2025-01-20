import pickle
# --------------------------------------------------------------------------------------------
# Manteniment d'un diccionari.
# --------------------------------------------------------------------------------------------

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


def demana_assignatura(txt: str) -> str:
    contestacio = input(f'{txt} ? ').strip().title()
    return contestacio

def demana_nota(txt: str) -> float:
    return float(input(f'{txt} ? '))

def esta_en_qualificacions(nom_assignatura: str) -> bool:
    return nom_assignatura in qualificacions

def mostrar_missatge_error(txt: str) -> None:
    print(f'\n***** ERROR: {txt} *****\n')


def afegix_qualificacio() -> None:
    print('Acabar la introducció amb <intro>')
    while True:
        nom = demana_assignatura('Nom assignatura')
        if nom == '':
            break

        if esta_en_qualificacions(nom):
            mostrar_missatge_error("l'assignatura ja existix")
            continue

        nota = demana_nota('Nota')
        qualificacions[nom] = nota


def esborra_assignatura() -> None:
    nom = demana_assignatura("Esborrar l'assignatura")
    try:
        qualificacions.pop(nom)
    except KeyError:
        mostrar_missatge_error("l'asignatura no està creada")


def modifica_nota_assignatura() -> None:
    nom = demana_assignatura('Nom assignatura a modificar? ')
    if not esta_en_qualificacions(nom):
        mostrar_missatge_error("l'assignatura no existix")
        return

    nota = demana_nota('Nota')
    qualificacions[nom] = nota    

def modifica_nom_assignatura():
    nom_antic = demana_assignatura('Nom assignatura a canviar')

    if not esta_en_qualificacions(nom_antic):
        mostrar_missatge_error("l'assignatura no existix")
        return

    nom_nou = demana_assignatura('Nom nou assignatura: ')
    if esta_en_qualificacions(nom_nou):
        mostrar_missatge_error("l'assignatura ja existix")
        return

    valor = qualificacions.pop(nom_antic)
    qualificacions[nom_nou] = valor


def grava_qualificacions(nom_arxiu:str, qualificacions:dict) -> None:
    with open(nom_arxiu, 'wb') as fd:
        pickle.dump(qualificacions, fd)


qualificacions:dict = {}
nom_arxiu = 'qualificacions.pkl'

try:
    with open(nom_arxiu, 'rb') as fd1:
        qualificacions = pickle.load(fd1)
except FileNotFoundError:
    pass
    # with open(nom_arxiu, 'wb') as fd2:
    #     pickle.dump(qualificacions, fd2)

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
    
    grava_qualificacions(nom_arxiu, qualificacions)


