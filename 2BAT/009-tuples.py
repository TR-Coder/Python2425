
# <!-- https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-47.php -->



# =====================
# Booleans amb objectes
# =====================
# El constructor bool() accepta un objecte i retorna True o False.
# Tots els objectes són True execepte: None, False, 0 i variants, seqüències buides (list, tuple, string),
# mapes buits (diccionaris, sets) i objectes que implementen __bool__() o __len__() i que retornen False o 0.

# Quan passem un objecte al constructor de bool() este retorna el resultat del mètode __bool__() d'eixe objecte.
# Així bool(200) equival a 200.__bool_()
# Si no existix el mètode __bool__() es retornarà el resultat del mètode __len__(). Si el resultat de __len__() es 0,
# bool() retorna False, en cas contrari retorna True.
# Esta és la rao per a qual una llista buida retorna False i retorna True si té algun element.

#-----------
# EXERCICI 1
#-----------

# Donada una llista de tuples ,algunes d'elles buides, o siga (). Crear una llista que elimine les lliste buides.
# Nota (de moment): Si un objecte de longitud 0 s'avalua com a False.
# 
# llista = [ (1,3), (3,5,3), (), (7,2), (), (5,2,1), (45,)]
# llista_nova = [element for element in llista if element]
# print(llista_nova)

#-----------
# EXERCICI 2
#-----------
# Donat la següent llista de noms, crea una llista que indique les posicios d'aquelles paraules que comencen i acaben en la mateixa lletra.
noms = [ 'Antena', 'Arbre', 'Teulat', 'ordinador' ]
posicions = [i for i, (a,*b,c) in enumerate(noms) if a.lower()==c.lower()]  # type: ignore
print(posicions)

#-----------
# EXERCICI 3
#-----------
# Donat la següent llista. 
dades = {'t': [30, 35, 37, 38], 'p': [800, 900, 1200, 1800], 's': [2,4,6,8]}
# crea una llista de la forma:
#  [  (30, 800, 2),  (35, 900, 4),  (37, 1200, 6),  (38, 1800, 8)]
#
# Pista:
# - primer generar una llista de la forma: [[30, 35, 37, 38], [800, 900, 1200, 1800], [2, 4, 6, 8]]

# valors = [v for v in dades.values()]
# print(valors)

# tuples = [k for k in zip(*valors)]
# print(tuples)


#-----------
# EXERCICI 4
#-----------
# A partir del següent diccionari:
# dades = {'temperatura': [30, 35, 37, 38], 'pressio': [800, 900, 1200, 1800], 'temps': [2,4,6,8]}
#
# Obtindre la llegüent llista:
# [ 
#   {'temperatura': 30, 'pressio': 800,  'temps': 2},
#   {'temperatura': 35, 'pressio': 900,  'temps': 4},
#   {'temperatura': 37, 'pressio': 1200, 'temps': 6},
#   {'temperatura': 38, 'pressio': 1800, 'temps': 8}
# ]
#
# Nota: És com l'exercici anterior a què afegim un pas més.

# valors = [v for v in dades.values()]      # [[30, 35, 37, 38], [800, 900, 1200, 1800], [2, 4, 6, 8]]
# tuples = [k for k in zip(*valors)]        # [(30, 800, 2), (35, 900, 4), (37, 1200, 6), (38, 1800, 8)]
                   
# Pas addicional. Opció 1)
# llista = [dict(zip(dades.keys(), v)) for v in tuples]
# print(llista)                             # [{'temperatura': 30, 'pressio': 800, 'temps': 2}, {'temperatura': 35, 'pressio': 900, 'temps': 4}, {'temperatura': 37, 'pressio': 1200, 'temps': 6}, {'temperatura': 38, 'pressio': 1800, 'temps': 8}]

# Pas addicional. Opció 2)
# llista = []
# for v in tuples:
#     dict = {}
#     for a,b in zip(dades.keys(), v):
#             dict[a]=b
#     llista.append(dict)
# print(llista)






# =============================================================================================
# Posar les funcions anteriors amb una funció.
# =============================================================================================

# https://mypy.readthedocs.io/en/stable/kinds_of_types.html

# En version 3.8 i anteriors es necessita:
# from typing import Tuple



# ---------------------------------------------------------------------------------------------

llista = [ (1,3), (3,5,3), (), (7,2), (), (5,2,1), (45,)]


def esborra_tuples_buides(llista_in: list[tuple[int,...]]) -> list[tuple[int,...]]:
    """
    Rep una llista de tuples i esborra aquelles que estan buides.
    """
    return [element for element in llista_in if element]


resultat1 = esborra_tuples_buides(llista)
print(resultat1)


# ---------------------------------------------------------------------------------------------

dades = {'temperatura': [30, 35, 37, 38], 'pressio': [800, 900, 1200, 1800], 'temps': [2,4,6,8]}

# valors = [v for v in dades.values()]      # [[30, 35, 37, 38], [800, 900, 1200, 1800], [2, 4, 6, 8]]
# tuples = [k for k in zip(*valors)]        # [(30, 800, 2), (35, 900, 4), (37, 1200, 6), (38, 1800, 8)]
#
# [ 
#   {'temperatura': 30, 'pressio': 800,  'temps': 2},
#   {'temperatura': 35, 'pressio': 900,  'temps': 4},
#   {'temperatura': 37, 'pressio': 1200, 'temps': 6},
#   {'temperatura': 38, 'pressio': 1800, 'temps': 8}
# ]

def formata_dades_entrada(dades: dict[str,list[int]]) -> list[dict[str,int]]:
    valors: list[list[int]] = [v for v in dades.values()]
    tuples: list[tuple[int, ...]] = [k for k in zip(*valors)]        
    llista: list[dict[str,int]] = [dict(zip(dades.keys(), v)) for v in tuples]
    return llista


resultat2 = formata_dades_entrada(dades)
print(resultat2)