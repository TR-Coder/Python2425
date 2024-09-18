# https://realpython.com/sort-python-dictionary/

#-------------
# EXERCICI 1
#-------------
# Crear un diccionari on les claus van de l'1 al 10 i el valor és quadrat de la clau.
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100} 
# Fes-ho de 5 maneres diferents.

# quadrat = {}

# Solució 1
# quadrat = { i:i**2 for i in range(1, 11)}


# Solució 2
# for i in range(1,11):
#     quadrat[i] = i*i

# Solució 3
# for i in range(1,11):
#     quadrat.setdefault(i, i*i)

# Solució 4
# iterable = [(i,i*i) for i in range(1,11)]
# quadrat = dict(iterable)

# Solució 5
# for i in range(1, 11):
#     quadrat.update({i: i**2})

# Solució 6
# claus = range(1, 11)
# valors = [i**2 for i in claus]
# quadrat = dict(zip(claus, valors))


# Solució 7
# quadrat = dict(map(lambda i: (i, i**2), range(1, 11)))

# Solució 8
quadrat:dict = {}
for x in range(1,11):
    quadrat = {**quadrat,  **{x:x*x}}


    # quadrat = quadrat | {x:x*x}


# print(quadrat)


#-------------
# EXERCICI 2
#-------------
# multiplicar tots els valors d'un diccionari
#

# diccionari = {'k1': 10, 'k2': 20, 'k3': 30}
# resultat = 1

# Solució 1
# for valor in diccionari.values():
#     resultat *= valor

# Solució 2
# for clau in diccionari:
#     resultat *= diccionari[clau]


#-------------
# EXERCICI 3
#-------------
# Tenim una llista de noms i una llista de notes. Al nom en la posició i de la llista de noms li correspon la posicio i en la llista de notes.
#
# noms = ['Carles', 'Pere', 'Jaume']
# notes = [7,6,9]

# diccionari = dict(zip(noms, notes))

#-------------
# EXERCICI 4
#-------------
# Nota: a partir de la versió 3.7 els diccionaris matenen l'ordre d'inserció.
#
# Eliminar els valors duplicats d'un diccionari. Deixar la primera clau del valor duplicat.
# diccionari = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 3}

# resultat:dict = {}
# for clau, valor in diccionari.items():
#     if valor not in resultat.values():
#         resultat[clau] = valor
# print(resultat)



# El mateix, però deixar l'última clau del duplicat.
#   Pista:reversed()
#   diccionari = { key:diccionari[key] for key in reversed(diccionari)}

# resultat:dict = {}
# for clau, valor in reversed(diccionari.items()):
#     if valor not in resultat.values():
#         resultat[clau] = valor

# resultat = { key:resultat[key] for key in reversed(resultat)}
# print(resultat)

#-------------
# EXERCICI 5
#------------- 
# A l'igual que passa amb les llistes, no poden anar esborrant elements mestres estem recorrent el diccionari.
# Per exemple, el següent codi genera l'excepció: RuntimeError: dictionary changed size during iteration
# diccionari = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for k,v in diccionari.items():
#     if v%2==0:
#         diccionari.pop(k)

# -----------
# Solució 1
# -----------
# La solució és fer una còpia de les claus diccionari. Recorrerem la còpia, però esborrem del diccionari original.
# diccionari = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for key in list(diccionari.keys()):
#     if diccionari[key] % 2 == 0:
#         diccionari.pop(key)
# print(diccionari)

# -----------
# Solució 2
# -----------
# Anotem les claus que hem d'esborrar en una llista que després recorrem per esborrar del diccionari les claus.
#
# diccionari = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# claus_a_esborrar = []
# for clau in diccionari:
#     if diccionari[clau] % 2 == 0:
#         claus_a_esborrar.append(clau)
        
# for clau in claus_a_esborrar:
#     diccionari.pop(clau)

# print(diccionari)

# -----------
# Solució 3
# -----------
# Crear un diccionari nou que continga només els elements que ens interessen.
# diccionari_original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# diccionari_copia = {k:v for k,v in diccionari_original.items() if v % 2 != 0}

# diccionari_original = diccionari_copia
# diccionari_copia = {}
# print(diccionari_original)


#-------------
# EXERCICI 6
#------------- 
# Partin d'este diccionari:
# ies = {
#     '1ESO': {
#         'alumnes': 140,
#         'grups': 4
#     },
#     '2ESO': {
#         'alumnes': 160,
#         'grups': 5
#     }
#  }

# Mostrar (print) la informació de la següent manera:
# --- 1ESO ---
# alumnes=140
# grups=4
# --- 2ESO ---
# alumnes=160
# grups=5

# for nivell in ies:
#     print(f'--- {nivell} ---')
#     for dades in ies[nivell]:
#         print(f'{dades}={ies[nivell][dades]}')




#-------------
# EXERCICI 7
#------------- 
# sum(iterable, start) recorre iterable i suma els seus elements. start és el valor inicial de la suma inicial (per defecte 0)
# Sumar el valors d'un diccionari. Després la multiplicaió.
#
# SUMA
# diccionari = {'a': 1, 'b': 2, 'data3': 4}
# suma = sum(diccionari.values())
# print(suma)

# MULTIPLICACIÓ. Solució 1
# producte = 1
# for valor in diccionari.values():
#     producte *= valor
# print(producte)

# MULTIPLICACIÓ. Solució 2
# producte = 1
# [producte:=producte*valor for valor in diccionari.values()]
# print(producte)

# MULTIPLICACIÓ. Solució 3
# from functools import reduce
# producte = 1
# resultado = reduce(lambda x, y: x*y, diccionari.values())
# print(producte)


#-------------
# EXERCICI 8
#-------------
# Solució 1
# # Crear un diccionari que a partir d'un string indique el nombre de vegades que apareix cada lletra.
# str = 'AABCCC5'
# diccionari:dict = {}
# for lletra in str:
#     diccionari[lletra] = diccionari.get(lletra, 0 ) + 1
# print(diccionari)


# Solució 2
# str = 'AABCCC5'
# diccionari:dict = {}
# for lletra in str:
#     if lletra not in diccionari:
#         diccionari[lletra]=0
#     else:
#         diccionari[lletra] = diccionari[lletra] + 1
# print(diccionari)


#-------------
# EXERCICI 9
#------------- 
# Tenim una llista formada per tuples on cada tupla representa (nom_atleta, distancia_salt)
# Obtindre un dicciori que indique per cada nom una llista dels salts que ha fet.
# Exemple:
# de          [('Pere', 7.8), ('Carles', 7.7), ('David', 7.9), ('Carles', 7.8), ('Carles', 7.7), ('David', 7.8)]
# obtindre:   {'Pere': [7.8], 'Carles': [7.7, 7.8, 7.7], 'David': [7.9, 7.8]}

# Solució 1
# llista = [('Pere', 7.8), ('Carles', 7.7), ('David', 7.9), ('Carles', 7.8), ('Carles', 7.7), ('David', 7.8)]
# diccionari:dict = {}
# for nom, distancia in llista:
#     diccionari.setdefault(nom, []).append(distancia)
# print(diccionari)

# Solució 2
# llista = [('Pere', 7.8), ('Carles', 7.7), ('David', 7.9), ('Carles', 7.8), ('Carles', 7.7), ('David', 7.8)]
# for nom, distancia in llista:
#     if nom not in diccionari:
#         diccionari[nom]=[distancia]
#     else:
#         diccionari[nom].append(distancia)
# print(diccionari)






#-------------
# EXERCICI 
#-------------
# Funció que rep diccionaris com arguments i retorna un diccionari que els unix tots.
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'c': 5, 'd': 6}

# def unix_diccionaris_1(*dict_in: dict) -> dict:
#     dict_out = {}
#     for d in dict_in:
#         dict_out.update(d)
#     return dict_out

# print(unix_diccionaris_1(dict1, dict2, dict3))

# def unix_diccionaris_2(dict_1: dict, *dict_resta) -> None:
#     dict_out = dict_1.copy()
#     dict_out.update(dict_resta)
#     print(dict_1, dict_resta, dict_out)

# print(unix_diccionaris_2(dict1,dict2))????????



# https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php


#'F'nció que rep una cadena i retorna un diccionari amb les paraules que
# conté i la seua longitut.
# def funcio1(cadena: str) -> dict[str, int]:
#     llista_paraules = cadena.split()
#     llista_longituds = map(len, llista_paraules)
#     return dict(zip(llista_paraules, llista_longituds))


# def funcio2(cadena: str) -> dict[str, int]:
#     return {item: len(item) for item in cadena.split()}


# txt = 'Prova de diccionaris y de llistes'
# print(funcio2(txt))


# ====================================================================
# ====================================================================
# Tornar una llista dels alumnes (diccionari) que estan per davall d'una nota de tall.

# from typing import Callable
# Tipus_Notes_Alumnes = dict[str, list[int]]
# Tipus_Alumne = dict[str, str | list[int] | bool]
# Tipus_Llista_Alumnes = list[Tipus_Alumne]

# # Solució 1: amb filter

# alumnes: Tipus_Llista_Alumnes = [
#     {'dni': '1', 'nom': 'A1', 'notes': [5, 5, 5]},
#     {'dni': '2', 'nom': 'A2', 'notes': [6, 6, 6, 6]},
#     {'dni': '3', 'nom': 'A3', 'notes': [2, 2, 2, 2]},
# ]


# TALL: float = 6


# def filtre_alumnes(tall: float) -> Callable:
#     def f(alumne: Tipus_Notes_Alumnes) -> bool:
#         return sum(alumne['notes']) / len(alumne['notes']) >= tall
#     return f


# def Nota_Tall(alumnes: Tipus_Llista_Alumnes, tall: float) -> Tipus_Llista_Alumnes:
#     filtre: Callable = filtre_alumnes(tall)
#     return list(filter(filtre, alumnes))


# print(Nota_Tall(alumnes, TALL))

# # Solució 2
# filtre: Callable = filtre_alumnes(TALL)
# llista = [item for item in alumnes if filtre(item)]
# print(llista)

# # Solucio 3


# def Tall_Alumnes(alumne: Tipus_Notes_Alumnes, tall: float):
#     mitjana: float = sum(alumne['notes']) / len(alumne['notes'])
#     return mitjana >= tall


# llista = [alumne for alumne in alumnes if Tall_Alumnes(alumne, TALL)]
# print(llista)


# ===============================================================
# Calcular el mòdul d'un vector
#
# def Modul_Vector(vector: list[float]):
#     return sum([x ** 2 for x in vector]) ** 0.5  # sqrt

# =================================================================
# Dades atípiques: implementar una funció que rep una llista de nombres
# i retorna aquells que estàn per davall de la mitjana.

# from statistics import mean


# dades: list[float] = [1, 2, 3, 4]


# Solució 1
# def Filtre_Atipic(dades):
#     mitjana: float = mean(dades)

#     def f(dada: float):
#         return dada < mitjana
#     return f

# def Dades_Atipiques(dades: list[float]):
#     return list(filter(Filtre_Atipic(dades), dades))

# print(Dades_Atipiques(dades))

# Solució 2
# def Dades_Atipiques(dades: list[float]):
#     mitjana: float = mean(dades)
#     return [dada for dada in dades if dada < mitjana]


# print(Dades_Atipiques(dades))


# =================================================================
# import os
# import platform

# LINE_UP = '\033[1F'
# LINE_CLEAR = '\x1b[2K'

# etiquetes: list[str] = ['nom', 'telefon']
# contactes: list[dict[str, str]] = []
# filtre_contactes: str = ''


# def neteja_pantalla():
#     """Neteja la terminal. Té en compte els sistema operatiu (Windows,Linux)"""
#     if platform.system() == 'Windows':
#         os.system('cls')
#     else:
#         os.system('clear')


# def opcio_menu(text: str, valors_valids: str) -> str:
#     """Fa un input() mostrant text.
#         Admet i retorna només intro i els caràcters que estan en valors_valids.
#                 Si el caràcter és invàlid mostra un missagte d'opció incorrecta."""
#     print()
#     while True:
#         opcio: str = input(text).upper()
#         if opcio in valors_valids:
#             return opcio
#         print(LINE_CLEAR+'Error, opció incorrecta' +
#               LINE_UP, end=LINE_CLEAR)


# def opcio_entera(text: str, maxim: int) -> int:
#     """Fa un input() mostrant text. Admet i retorna valors enters entre [0, maxim].
#         Si el valor introduït no és un enter o esta fora del rang [0,maxim] mostra
#         un missatge d'error de valor fora de rang o valor incorrecte"""
#     while True:
#         try:
#             opcio: str = input(text)
#             if opcio == '':
#                 return -1
#             if 0 <= int(opcio) < maxim:
#                 return int(opcio)
#             print(LINE_CLEAR+'Error, valor fora de rang' +
#                   LINE_UP, end=LINE_CLEAR)
#         except ValueError:
#             print(LINE_CLEAR+'Error, valor incorrecte' +
#                   LINE_UP, end=LINE_CLEAR)


# def mostra_menu_principal() -> str:
#     """Mostra les opcions del menú principal i retorna l'opció seleccionada (Crida opcio_menu())
#         Les opcions són: 1-Contactes i 2-Etiquetes.
#         """
#     print('- MENÚ PRINCIPAL -')
#     print('1- Contactes')
#     print('2- Etiquetes')
#     return opcio_menu('Opció? ', '12')


# def mostra_llista_etiquetes():
#     print("- LLISTA D'ETIQUETES -")

#     if len(etiquetes) == 0:
#         print(' -- No hi ha etiquetes --')
#         return

#     for n, etiqueta in enumerate(etiquetes):
#         print(f'({n})- {etiqueta.capitalize()}')


# def filtra_contactes() -> list[dict[str, str]]:
#     if filtre_contactes == '':
#         return contactes

#     return [contacte for contacte in contactes if [
#         valor for valor in contacte.values() if filtre_contactes in valor]]


# def mostra_llista_contactes():
#     neteja_pantalla()
#     print(f'- LLISTA DE CONTACTES - Filtre: {filtre_contactes}')

#     contactes_filtrats = filtra_contactes()

#     if len(contactes_filtrats) == 0:
#         print('\n- No hi ha contactes -')
#         return

#     for n, contacte in enumerate(contactes_filtrats):
#         print(f'({n})- {contacte}')


# def gestiona_etiquetes():
#     while True:
#         neteja_pantalla()
#         mostra_llista_etiquetes()
#         opcio = opcio_menu(
#             '(C)rea, (E)sborra, (M)odifica? ', 'CEMF')
#         if opcio == '':
#             break
#         elif opcio == 'C':
#             etiqueta: str = input('\nNom de la nova etiqueta: ').lower()
#             if etiqueta in etiquetes:
#                 print('Error, la etiqueta ja existix')
#                 continue
#             etiquetes.append(etiqueta)
#         elif opcio == 'E':
#             posicio: int = opcio_entera(
#                 'Etiqueta a esborrar? ', len(etiquetes))
#             if posicio == -1:
#                 continue
#             etiquetes.pop(posicio)
#         elif opcio == 'M':
#             posicio: int = opcio_entera(
#                 'Etiqueta a modificar? ', len(etiquetes))
#             if posicio == -1:
#                 continue
#             etiqueta = input('Nou nom de la etiqueta: ').lower()
#             if etiqueta in etiquetes:
#                 print('Error, la etiqueta ja existix')
#                 continue
#             if etiqueta != '':
#                 etiquetes[posicio] = etiqueta


# def demana_llista_etiquetes() -> list[int]:
#     while True:
#         nombre_etiquetes: str = input(
#             'Indica les etiquetes a aplicar (Intro totes)? ')
#         conjunt = set()
#         try:
#             for item in nombre_etiquetes.split():
#                 if int(item) < 0 or int(item) >= len(etiquetes):
#                     print(LINE_CLEAR+'Error, etiqueta fora de límit' +
#                           LINE_UP, end=LINE_CLEAR)
#                     break
#                 conjunt.add(int(item))
#             else:
#                 return(sorted(conjunt))
#         except:
#             print(LINE_CLEAR+'Etiqueta incorrecta' +
#                   LINE_UP, end=LINE_CLEAR)


# def crea_contacte():
#     print()
#     mostra_llista_etiquetes()
#     llista_etiquetes: list[int] = demana_llista_etiquetes()

#     contacte: dict[str, str] = {}

#     if not llista_etiquetes:
#         for etiqueta in etiquetes:
#             valor = input(f'{etiqueta}? ')
#             contacte[etiqueta] = valor
#     else:
#         for item in llista_etiquetes:
#             clau = etiquetes[item]
#             valor = input(f'{clau}? ')
#             contacte[clau] = valor

#     contactes.append(contacte)


# def modifica_contacte(posicio: int):
#     print(LINE_CLEAR, end='')
#     contacte = contactes[posicio]
#     for clau in contacte.keys():
#         valor = input(LINE_CLEAR + f'{clau}? ')
#         if valor != '':
#             contacte[clau] = valor


# def gestiona_contactes():
#     while True:
#         mostra_llista_contactes()
#         opcio = opcio_menu(
#             '(C)rea, (E)sborra, (M)odifica, (F)iltra? ', 'CEMF')
#         if opcio == '':
#             break
#         elif opcio == 'C':
#             crea_contacte()
#         elif opcio == 'E':
#             posicio: int = opcio_entera(
#                 'Contacte a esborrar? ', len(contactes))
#             if posicio == -1:
#                 continue
#             contactes.pop(posicio)
#         elif opcio == 'M':
#             posicio: int = opcio_entera(
#                 'Contacte a modificar? ', len(contactes))
#             if posicio == -1:
#                 continue
#             modifica_contacte(posicio)
#         elif opcio == 'F':
#             global filtre_contactes
#             filtre_contactes = input('Filtre a aplicar (Intro=cap filtre)? ')


# gestiona_contactes()
# while True:
#     neteja_pantalla()
#     opcio = mostra_menu_principal()
#     if opcio == '1':
#         gestiona_contactes()
#     elif opcio == '2':
#         gestiona_etiquetes()
