# --------------------------------------------------------------------------------------------
# Manteniment d'un diccionari.
# --------------------------------------------------------------------------------------------

# qualificacions:dict = {}

# while True:
#     print()
#     print(qualificacions)
#     print('    MENU')
#     print('-------------')
#     print('A- afegir')
#     print('E- esborrar')
#     print('M- modificar nota')
#     print('C- modificar nom assignatura')
#     print('Q- Acabar')

#     opcio = input('Opció? ').upper()

#     if opcio == 'Q':
#         break

#     elif opcio == '':
#         pass

#     elif opcio == 'A':
#         print('Acabar la introducció amb <intro>')
#         while True:
#             nom = input('Nom assignatura: ').strip().title()

#             if nom == '':
#                 break

#             if nom in qualificacions:
#                 print("\n ***** ERROR, l'assignatura ja existix *****\n")
#                 continue

#             nota = float(input('Nota: '))
#             qualificacions[nom] = nota

#     elif opcio == 'E':
#         nom = input("Esborrar l'assignatura: ").strip().title()
#         try:
#             qualificacions.pop(nom)
#         except KeyError:
#             print("\n ***** ERROR, l'asignatura no està creada *****\n")

#     elif opcio == 'M':
#         nom = input('Nom assignatura a modificar? ').strip().title()
#         if nom not in qualificacions:
#             print("\n *****ERROR, l'assignatura no existix *****\n")
#             continue

#         nota = float(input('Nota: '))
#         qualificacions[nom] = nota

#     elif opcio == 'C':
#         nom_antic = input('Nom assignatura a canviar? ').strip().title()
#         if nom_antic not in qualificacions:
#             print("\n ***** ERROR, l'assignatura no existix *****\n")
#             continue

#         nom_nou = input('Nom nou assignatura: ').strip().title()
#         if nom_nou in qualificacions:
#             print("\n ***** ERROR, l'assignatura ja existix *****\n")
#             continue

#         valor = qualificacions.pop(nom_antic)
#         qualificacions[nom_nou] = valor

#     else:
#         print('\n***** ERROR: opció incorrecta *****\n')



# --------------------------------------------------------------------------------------------
# Manteniment d'un diccionari.
# --------------------------------------------------------------------------------------------
#
# Modificar el programa anterior utilitzant estes funcions:
#

# def mostra_menu() -> str:
#     print()
#     print(qualificacions)
#     print('    MENU')
#     print('-------------')
#     print('A- afegir')
#     print('E- esborrar')
#     print('M- modificar nota')
#     print('C- modificar nom assignatura')
#     print('Q- Acabar')

#     return input('Opció? ').upper()


# def demana_assignatura(txt: str) -> str:
#     contestacio = input(f'{txt} ? ').strip().title()
#     return contestacio

# def demana_nota(txt: str) -> float:
#     return float(input(f'{txt} ? '))

# def esta_en_qualificacions(nom_assignatura: str) -> bool:
#     return nom_assignatura in qualificacions

# def mostrar_missatge_error(txt: str) -> None:
#     print(f'\n***** ERROR: {txt} *****\n')



# qualificacions:dict = {}

# while True:

#     opcio = mostra_menu()

#     if opcio == 'Q':
#         break

#     elif opcio == '':
#         pass

#     elif opcio == 'A':
#         print('Acabar la introducció amb <intro>')
#         while True:
#             nom = demana_assignatura('Nom assignatura')
#             if nom == '':
#                 break

#             if esta_en_qualificacions(nom):
#                 mostrar_missatge_error("l'assignatura ja existix")
#                 continue

#             nota = demana_nota('Nota')
#             qualificacions[nom] = nota

#     elif opcio == 'E':
#         nom = demana_assignatura("Esborrar l'assignatura")
#         try:
#             qualificacions.pop(nom)
#         except KeyError:
#             mostrar_missatge_error("l'asignatura no està creada")

#     elif opcio == 'M':
#         nom = demana_assignatura('Nom assignatura a modificar? ')
#         if not esta_en_qualificacions(nom):
#             mostrar_missatge_error("l'assignatura no existix")
#             continue

#         nota = demana_nota('Nota')
#         qualificacions[nom] = nota

#     elif opcio == 'C':
#         nom_antic = demana_assignatura('Nom assignatura a canviar')

#         if not esta_en_qualificacions(nom_antic):
#             mostrar_missatge_error("l'assignatura no existix")
#             continue

#         nom_nou = demana_assignatura('Nom nou assignatura: ')
#         if not esta_en_qualificacions(nom_nou):
#             mostrar_missatge_error("l'assignatura ja existix")
#             continue

#         valor = qualificacions.pop(nom_antic)
#         qualificacions[nom_nou] = valor

#     else:
#         mostrar_missatge_error("opció incorrecta")



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
    if not esta_en_qualificacions(nom_nou):
        mostrar_missatge_error("l'assignatura ja existix")
        return

    valor = qualificacions.pop(nom_antic)
    qualificacions[nom_nou] = valor



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


