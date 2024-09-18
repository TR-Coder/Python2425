# ===============================
# EXERCICI 1: calcular la mediana
# ===============================
# La mediana es calcula ordenant els elements de llista. Si la longitud de la llista es parella la
# mediana és l'element que està enmig, si es imparella és el promedia dels dos elements centrals.
#

# llista: list[int] = [7, 2, 5, 8, 9, 1]
# mediana: float = 0

# llista_ordenada = sorted(llista)
# mitat: int = len(llista_ordenada) // 2

# if len(llista_ordenada) % 2 == 0:
#     mediana = (llista_ordenada[mitat-1] + llista_ordenada[mitat]) / 2
# else:
#     mediana = llista_ordenada[mitat]

# print(f'La mediana és {mediana}')


# =========================
# EXERCICI 2: rang de notes
# =========================
# En una llista tenim la nota de N alumnes.
# Volem saber quants estan suspesos, aprovats [5,7), notable [7,9) i excel·lent [9,10]
#
# SUSPESOS: int = 0
# APROVATS: int = 1
# NOTABLES: int = 2
# EXCELENTS: int = 3

# notes: list[float] = [10, 3, 5, 6, 7, 8, 9.5]
# rang: list[int] = [0] * 4

# for nota in notes:
#     if nota < 5:
#         rang[SUSPESOS] += 1
#     elif nota >= 5 and nota < 7:
#         rang[APROVATS] += 1
#     elif nota >= 7 and nota < 9:
#         rang[NOTABLES] += 1
#     else:
#         rang[EXCELENTS] += 1

# print(notes)
# print(f'Suspesos: {rang[SUSPESOS]}')
# print(f'Aprovats: {rang[APROVATS]}')
# print(f'Notables: {rang[NOTABLES]}')
# print(f'Excel·lents: {rang[EXCELENTS]}')


# =========================
# EXERCICI 3: Pasar un nombre a text.
# Separar per comes i posar la conjunció 'i' al final.
# =========================
# -----------
# Solució 1:
# -----------
# lletra: list[str] = ['zero', 'un', 'dos', 'tres', 'quatre', 'cinc', 'sis', 'set', 'huit', 'nou']

# nombre = input('Introduïx un nombre: ')

# if len(nombre) == 0:
#     txt = 'Error'
# elif len(nombre)==1:
#     txt = lletra[int(nombre)]
# else:
#     llista_lletres: list[str] = [lletra[int(x)] for x in nombre]
#     txt = ', '.join(llista_lletres[:-1]) + ' i ' + llista_lletres[-1]

# print(txt)

# ----------
# Solució 2:
# ----------
# lletra: list[str] = ['zero', 'un', 'dos', 'tres', 'quatre', 'cinc', 'sis', 'set', 'huit', 'nou']

# nombre:str = input('Introduïx un nombre: ')

# txt: str = 'Error' if nombre=='' else lletra[int(nombre[0])] 

# if len(nombre)>1:
#     for digit in nombre[1:-1]:              # Si len(nombre)==2 no entra en el bucle
#         txt += ', ' + lletra[int(digit)]
#     txt += ' i ' + lletra[int(nombre[-1])]

# print(txt)

# =====================
# EXERCICI 4: ELIMINAR DUPLICATS D'UN LIST
# =====================
# import random
# import time

# Generar nombres aleatoris (20s)
# temps_inicial = time.time()
# dades = [random.randint(0, 100) for _ in range(100000000)]
# temps_final = time.time()
# print(f'TEMPS GENERAR NOMBRES ALEATORIS: {temps_final - temps_inicial}')

# temps_inicial = time.time()

# -----------------
# Solució 1 (0.3s)
# -----------------
# conjunt = set(dades)


# -----------------
# Solució 2 (19s)
# -----------------
# llista = []
# temps_inicial = time.time()
# for item in dades:
#     if item not in llista:
#         llista.append(item)

# -----------------
# Solució 3 (12s)
# -----------------
# llista = sorted(dades)
# resultat = []
# item_anterior = -1
# for item in dades:
#     if item != item_anterior:
#         resultat.append(item)

# temps_final = time.time()
# print(f'TEMPS: {temps_final - temps_inicial}')

# =====================
# EXERCICI 5: llista paraules prohibides
# =====================
# Tinc una llista de paraules prohibides i un altra de paraules substitutes.
# He de fer la substitució en un text.
#

# import functools
# llista_prohibida = ['dispositius', 'tercera']
# llista_substituta = ['equips', '3a']

# txt: str = '''L'USB 3.0 és la tercera revisió important del Bus Sèrie Universal
# (USB-Universal Serial Bus en Anglès) actual estàndard per a la connectivitat
# de dispositius informàtics.'''

# # -----------------------
# # Solució 1: amb replace
# # -----------------------
# for paraula_prohibida, paraula_substituta in zip(llista_prohibida, llista_substituta):
#     txt = txt.replace(paraula_prohibida, paraula_substituta)
# print(txt)

# #----------------------------------
# # Solució 2: amb operador morsa :=
# #----------------------------------
# [txt := txt.replace(paraula_prohibida, paraula_substituta) for paraula_prohibida,
#  paraula_substituta in zip(llista_prohibida, llista_substituta)]
# print(txt)

# #----------------------------------
# # Solució 3: amb funció reduce
# #----------------------------------
# x = functools.reduce(lambda x, y: x.replace(
#     *y), zip(llista_prohibida, llista_substituta), txt)

# #----------------------------------
# # Solució 4: split i enumerate
# #----------------------------------

# text = txt.split()

# for i, paraula in enumerate(text):
#     try:
#         posicio = llista_prohibida.index(paraula)
#         text[i] = llista_substituta[posicio]
#     except ValueError:
#         pass
# print(' '.join(text))

# ---------------------
# EXERCICI 6: EL PENJAT
# ---------------------
# import os

# --------------------------------------------------------------------------------------------
# JOC DEL PENJAT
# --------------------------------------------------------------------------------------------


# Afegim els espais en blanc que hi ha en la paraula a endevinar.
# for c in paraula_secreta:
#     x = ' ' if c == ' ' else '-'
#     cadena.append(x)
#

# dibuix: list = ['''
#       +---+
#       |   |
#           |
#           |
#           |
#           |
#     =========''', '''
#       +---+
#       |   |
#       O   |
#           |
#           |
#           |
#     =========''', '''
#       +---+
#       |   |
#       O   |
#       |   |
#           |
#           |
#     =========''', '''
#       +---+
#       |   |
#       O   |
#      /|   |
#           |
#           |
#     =========''', '''
#       +---+
#       |   |
#       O   |
#      /|\  |
#           |
#           |
#     =========''', '''
#       +---+
#       |   |
#       O   |
#      /|\  |
#      /    |
#           |
#     =========''', '''
#       +---+
#       |   |
#       O   |
#      /|\  |
#      / \  |
#           |
#     =========''']


# class bg:
#     black = '\033[40m'
#     red = '\033[41m'
#     green = '\033[42m'
#     orange = '\033[43m'
#     blue = '\033[44m'
#     purple = '\033[45m'
#     cyan = '\033[46m'
#     lightgrey = '\033[47m'


# def pinta_pantalla():
#     os.system('cls')
#     print(f'{bg.blue}JOC DEL PENJAT{bg.black}')
#     print(f'==============')
#     print(
#         f'{errors} errors. Et queden {INTENTS-errors} intents. {bg.red}Lletres incorrectes: {lletres_incorrectes}{bg.black}')
#     print()
#     print(''.join(cadena))
#     print(dibuix[errors])


# paraula_a_endevinar: str = 'VELOCITAT RAPIDA'
# paraula_secreta: list = list(paraula_a_endevinar)
# INTENTS: int = 6
# errors: int = 0
# lletres_incorrectes: str = ''

# cadena: list = [' ' if c == ' ' else '-' for c in paraula_secreta]

# while (errors < INTENTS) and (cadena != paraula_secreta):
#     pinta_pantalla()
#     lletra_entrada = input('Lletra? ')
#     if lletra_entrada == '':
#         continue

#     lletra_entrada = lletra_entrada[0].capitalize()
#     if lletra_entrada in lletres_incorrectes:
#         continue

#     has_encertat = False
#     for i, caracter in enumerate(paraula_secreta):
#         if caracter == lletra_entrada:
#             cadena[i] = lletra_entrada
#             has_encertat = True

#     if not has_encertat:
#         lletres_incorrectes += lletra_entrada
#         errors += 1
#         if errors == INTENTS:
#             pinta_pantalla()
#             print(
#                 f'{bg.red}Has perdut, la paraula era {paraula_a_endevinar}{bg.black}')
#             break
# else:
#     print(f'{bg.green}Molt bé, la paraula és {paraula_a_endevinar}{bg.black}')

# print(bg.black)



# # --------------------------------------------------------------------------------------------
# # EXERCICI 7: CREAR UNA GRAELLA FILA-COLUMNA 
# # --------------------------------------------------------------------------------------------
# # vector[fila1, fila2...]
# # vector[0] = [A1,A2,A3,A4,A5,A6,A7,A8]
# # vector[1] = [B1,B2,B3,B4,B5,B6,B7,B8]
# #       . . . . . . . .
# # vector[7] = [H1,H2,H3,H4,H5,H6,H7,H8]
# #
# # [fila][columna]
# #
# # |A1|A2|A3|A4|A5|A6|A7|A8|
# # |B1|B2|B3|B4|B5|B6|B7|B8|
# # |C1|C2|C3|C4|C5|C6|C7|C8|
# # |D1|D2|D3|D4|D5|D6|D7|D8|
# # |E1|E2|E3|E4|E5|E6|E7|E8|
# # |F1|F2|F3|F4|F5|F6|F7|F8|
# # |G1|G2|G3|G4|G5|G6|G7|G8|
# # |H1|H2|H3|H4|H5|H6|H7|H8|

# #
# # vector = []
# # for caracter in 'ABCDEFGH':
# #     fila = []
# #     for nombre in '12345678':
# #         fila.append(caracter+nombre)
# #     vector.append(fila) 

# # print(vector[1][3]) 

# # for f in vector:
# #     print('|' + '|'.join(f) + '|')



# vector= [[x+y for y in '12345678'] for x in 'ABCDEFGH']
# print(vector)

# for f in vector:
#     print('|' + '|'.join(f) + '|')


# Tot en una línia
# [print('|' + '|'.join(f) + '|') for f in [[x+y for y in '12345678'] for x in 'ABCDEFGH']]


# --------------------------------------------------------------------------------------------
# Exercici de funcions:
# --------------------------------------------------------------------------------------------
# Generar la seqüència: A-B-C-D, AA-AB-AC-AD,   AAA-ABA-AAC-ADA
#                                BA-BB-BC-BD    BAA-BBA-BCA-BDA
#                                CA-CB-CC-CD    CAA-CBA-CCA-CDA
#                                DA-DB-DC-DD    DAA-DBA-DCA-DDA
#                                                 . . . . 
#                                               AAD-ABD-ACD-ADD
#                                               BAD-BBD-BCD-BDD
#                                               CAD-CBD-CCD-CDD
#                                               DAD-DBD-DCD-DDD

# De manera recursiva

def f(i,ant):
    if i==0:
        print(ant)
        return
    for x in 'ABCD':
        f(i-1,ant+x)

for i in range(1,4):
    f(i,'')



