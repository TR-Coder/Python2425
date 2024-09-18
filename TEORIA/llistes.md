import sys
import copy
# Llistes

## Crear llistes
```python
llista = []
llista = list()

# list() crea una llista a partir d'un iterable:
llista = list('HOLA')       # llista = ['H', 'O', 'L', 'A']

llista1 = [1, 2, 3, 4]
llista2 = list(llista1)     # llista1 i llista2 són llistes diferents.

# Atenció! Si fem:
llista1 = llista2           # ...llista1 i llista2 apunten a la mateixa llista.

                            # Inicialitzar els elements d'una llista amb el mateix valor
llista = ['-'] * 5          # ['-', '-', '-', '-', '-']
```

## Longitud d'una llista: len()
```python
llista = [0, 1, 2, 3, 4]
resultat = len(llista)		# resultat = 5
```

## Iterar: for, enumerate i zip

### for
Amb un __for__ no tenim accés a l'índex.

```python
llista = ['A', 'B', 'C', 'D', 'E']
for element in llista:
    print(element)			    # A B C D E
```

### enumerate()
La funció __enumerate()__ rep com argument un iterable i retorna un iterable, els elements del qual són tuples de dos elements,
on el 1r és la posicío i el 2n el valor de la llista en eixa posició.

```python
llista = ['A', 'B', 'C', 'D', 'E']
print(list(enumerate(llista)))	    # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
for i, element in enumerate(llista):
    print(i, element)				# 0 A   1 B   2 C   3 D   4 E

# Nota: és millor utilitzar enumerate que fer alguna cosa com:
for i in range(len(llista)):
    print(i, llista[i])				# 0 A   1 B   2 C   3 D   4 E
```

### zip()
La funció __zip()__ retorna un iterador de tuples. Zip combina les llistes fins que s'acava la més curta.

```python
llista1 = ['A', 'B', 'C', 'D', 'E']
llista2 = [4,   5,   9,   3]

print(list(zip(llista1, llista2)))	            # [('A', 4), ('B', 5), ('C', 9), ('D', 3)]
for element1, element2 in zip(llista1, llista2):
    print(element1, element2)					# A 4   B 5   C 9   D 3
```


## Afegir elements

Afegir un element al final de la llista amb __append()__:
```python
llista = []
llista.append(1)        # llista = [1]
llista.append('A')      # llista = [1,'A']
```

__insert()__ afig un element en la posició indicada:
```python
llista = [1, 2, 3, 4, 5]
llista.insert(1, 'A')
```

Si la posició indicada està fora dels límits no dóna error sinó que s'afegix al principi o al final:
```python
llista = [1, 2, 3, 4, 5]
llista.insert(100, 'A')     # llista = [1, 2, 3, 4, 5, 'A']

llista = [1, 2, 3, 4, 5]    
llista.insert(-50, 'A')     # llista = ['A', 1, 2, 3, 4, 5]
```

## Combinar llistes amb + i *

Crear una llista nova combinació d'altres llistes amb l'operador +
```python
llista1 = [1, 2, 3]
llista2 = [4, 5, 6]
llista_combinada = llista1 + llista2    # llista_combinada = [1, 2, 3, 4, 5, 6]
```
```python
# Enlloc de...
llista1 = [1, 2, 3]
resultat = llista1 + llista1 + llista1  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# ...podem fer-ho amb l'operador *
resultat = llista1 * 3                  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## Ampliar una llista amb .extend()

Amb l'operador + es crea una llista nova. Si volem modificar la llista original utilitzem __extend()__.

```python
llista1 = [1, 2, 3]
llista2 = [4, 5, 6]
llista1.extend(llista2)  # llista1 = [1, 2, 3, 4, 5, 6]
```

__extend()__ no crea cap llista sinó que retorna None
```python
resultat = llista1.extend(llista2)      # resultat=None
```

En realitat __extend()__ rep un iterador:
```python
llista1 = [1, 2, 3]
llista2 = 'HOLA'
llista1.extend(llista2)  # [1, 2, 3, 'H', 'O', 'L', 'A']
```

ATENCIÓ: Si utilitzem __append()__ per afegir al final d'una llista ja que:
```python
llista1 = [1, 2, 3]
llista2 = [4, 5]
llista1.append(llista2)  # llista = [1, 2, 3, [4, 5]]
```

## Modificar una llista
Per a modificar una posició la indiquem entre []. Si està fora de límits dóna error.
```python
llista = [1, 2, 3, 4, 5]
llista[1] = 'A'		# llista = [1, 'A', 3, 4, 5]
llista[4] = 'A'		# ERROR, IndexError: list assignment index out of range
```

## Modificar o substituir trossos complets de llista
```python
llista[1:4] = 'A'			# llista = [1, 'A', 5]
llista[1:4] = ['A', 'B']	# llista = [1, 'A', 'B', 5]
```

## Esborrar elements

__.pop()__ esborra la posició indicada i retorna el valor esborrat. Si no indiquem una posició esborra l'últim element.
```python
llista = [1, 2, 3, 4, 5]
resultat = llista.pop(2)    # llista = [1, 2, 4, 5]		resultat = 3
resultat = llista.pop()     # llista = [1, 2, 3, 4]		resultat = 5
```

Amb __del__ podem esborrar també per posició i per rang. No retorna res.
```python
llista = [1, 2, 3, 4, 5]
del llista[2]				# llista = [1, 2, 4, 5]
del llista[2:4]				# llista = [1, 2, 5]
```

També podem esborrar un rang així:
```python
llista = [1, 2, 3, 4, 5]
llista[2:4] = []			# llista = [1, 2, 5]		Nota: la posició 4 no s'inclou
```

Peró, NO pòdem esborrar un element així:
```python
llista[2] = []				# llista = [1, 2, [], 4, 5]
```

__.remove()__ esborra la primera ocurrència del valor que indiquem. Retorna None. Si no trobar res dóna Error
```python
llista = ['A', 'B', 'C', 'D', 'E', 'F', 'D']
resultat = llista.remove('D')			        # llista = ['A', 'B', 'C', 'E', 'F', 'D']
```

Per a esborrar una llista completa farem:
```python
llista.clear()
llista = []
```

## Buscar elements amb index()

__index()__ retorna la posició de la primera ocurrència de l'element indicat.
```python
llista = ['A', 'B', 'C', 'D', 'E', 'D']
resultat = llista.index('D')    # resultat = 3
                            	# Si no el troba dona error: ValueError: 'Z' is not in list
```

__index()__ permet limitar la busca en un rang.
```python
resultat = llista.index('D', 0, 4)		# resultat = 3
```

Podem capturar _ValueError_ amb try
```python
try:
    resultat = llista.index('Z')
except ValueError:
    resultat = None						# resultat = None
```

Si volem buscar totes les ocurrences podem fer, per exemple:
```python
item_a_buscar = 'D'
resultat = [index for index, item in enumerate(
    llista) if item == item_a_buscar]		    # resultat = [3, 5]
```

## Operador in
```python
llista = [1, 2, 3, 4, 5]
resultat = 2 in llista			# resultat = True
```

## Comptar el nombre d'occurrències
```python
llista = ['A', 'B', 'C', 'D', 'E', 'D']
resultat = llista.count('D')				# resultat = 2
```


## Conversió d'una llista en un string amb join()

__.join()__ recorre els element d'un iterable i els unix en únic string. Només funciona si tots els elements de l'iterable són strings.
Hem d'especificar un string com a separador.
```python
llista = ['H', 'O', 'L', 'A']
resultat = ''.join(llista)			# resultat = 'HOLA'
resultat = '-'.join(llista)			# resultat = 'H-O-L-A'
```

## Ordenar una llista
__sorted()__ retorna una llista nova ordenada a partir de la llista que li passem. No modifica la llista original.
```python
llista = [6, 3, 5, 6, 7, 3, 2, 0]
resultat = sorted(llista)					# [0, 2, 3, 3, 5, 6, 6, 7]
resultat = sorted(llista, reverse=True)		# [7, 6, 6, 5, 3, 3, 2, 0]
```
Addicionalment __sorted()__ té un paràmetre on especificarem una funció que serà cridada per cada element de la llista abans de fer les comparacions durant l'ordenació.
```python
llista = ['Castelló', 'valencia', 'alacant']

resultat = sorted(llista)                   # ['Castelló', 'alacant', 'valencia']
                                            # En ASCII les majúscules van primer
resultat = sorted(llista, key=str.lower)    # ['alacant', 'Castelló', 'valencia']
```

__sort()__ modifica la llista original i retorna None. Funciona igual que __sorted()__.
```python
llista.sort()				# ['Castelló', 'alacant', 'valencia']
llista.sort(key=str.lower)	# ['alacant', 'Castelló', 'valencia']
```

## Llistes per compressió

Enlloc de...
```python
valors = '65,23,51,24,81,87, 32'
resultat = []
for valor in valors.split(','):
    enter = int(valor)
    resultat.append(enter)			# resultat = [65, 23, 51, 24, 81, 87, 32]
```
...podem fer:
```python
resultat = [int(valor) for valor in valors.split(',')]
```

Podem afegir un if:
```python
resultat = [int(valor) for valor in valors.split(
    ',') if int(valor) >= 50]		# resultat = [65, 51, 81, 87]
```

El que hem fet abans crea una llista nova sense modificar l'original. Sin volem modificar la llista original podem fer:
Rendiment? internament remove() canvia les posicions dels elements de tota la llista.
```python
llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
for element in llista:
    if (element % 2) != 0:
        llista.remove(element)		# llista = [2, 4, 6, 8, 10, 20]
```

## Còpia de llistes
El nom d'una llista no és més que un alias, una referència a la llista.
```python
llista1 = ['A', 'B', 'C', 'D', 'E']
llista2 = llista1		# llista2 i llista1 són referències a la mateixa llista.
print(id(llista2), id(llista1))

llista1[0] = 1			# modificar llista1 és le mateix que modificar llista2
print(llista2)
```

Crear una llista nova copia d'un altra llista amb __.copy()__
```python
llista1 = ['A', 'B', 'C', 'D', 'E']		# llista2 = ['A', 'B', 'C', 'D', 'E']
llista2 = llista1.copy()
```

__.copy()__ pareix que funciona però es una copia superficial al primer nivell
```python
llista1 = ['A', 'B', [1, 2], 'D', 'E']
llista2 = llista1.copy()

llista1[2][1] = 7
print(llista2)			# llista1 = ['A', 'B', [1, 7], 'D', 'E']		# HORROR!!!
```

Per a fer una còpia en profunditat el millor és utilitzar el modul __copy__.
amb __copy.copy()__ fem una còpia superficial (_shallow copy_) i amb __copy.deepcopy()__ fem una còpia en profunditat (_deep copy_).

```python
import copy
llista1 = ['A', 'B', [1, 2], 'D', 'E']
llista2 = copy.deepcopy(llista1)

llista1[2][1] = 7
print(llista2)			# llista1 = ['A', 'B', [1, 2], 'D', 'E']	# UFF!! Ara si.
```

## Invertir una llista

Amb [: :-1] obtenim una llista nova invertida. L'original no es modifica.
```python
llista = ['A', 'B', 'C', 'D', 'E']
print(llista[::-1])					# ['E', 'D', 'C', 'B', 'A']
```

Amb __.reverse()__ modifiquen la llista original, retorna None.
```python
llista.reverse()				# llista = ['E', 'D', 'C', 'B', 'A']
```

Per temes de rendiment potser millor iterar sobre una llista que fer una còpia d'ella. 
__.reversed()__ retorna un iterador que recorre la llista en ordre invers.
```python
llista1 = ['A', 'B', 'C', 'D', 'E']
llista2 = reversed(llista1)		# llista2 = ['E', 'D', 'C', 'B', 'A']

for x in reversed(llista1):
    print(x)				    # E  D  C  B  A
```

## Subllistes (slicing)
llista[inici, final, increment]

```python
llista = [0, 1, 2, 3, 4]
llista[0:3]				# [0,1,2]
llista[:3]				# [0,1,2]
llista[-4:-1]			# [1, 2, 3]
llista[-1: -4]			# []
llista[-1: -4: -1]		# [4,3,2]
llista[::-1]			# [4,3,2,1,0]	Invertix tota la llista
```
De manera idiomàtica:
```python
s = 'CLASSE'
s[:2]  		# obté els dos primers elements			'CL'
s[-2:]		# obté els dos últims elements			'SE'
s[2:]		# descarta els dos primers elements		'ASSE'
s[:-2]		# descarta els dos últims elements		'CLASS'
```

Les subllistes no donen error si els índexs no estan bé. Retorna al valor que millos s'ajusta.
```python
llista = [0, 1]
llista[-5:7]    # [0,1]
llista[4:7]		# []
llista[-4:-7]   # []
llista[-7:-4]   # []
llista[0:2]		# [0,1]
llista[2, 0]	# []
llista[50:]		# []
```

## Paràmetres des de la línia de comandos
Per a poder llegir el paràmetres passats des de la línia de comandos hem de fer un import sys

__$__ _python3 programa.py parm1 parm2_
```python
import sys
nom_programa = sys.argv[0]
parametre_1 = sys.argv[1]
parametre_2 = sys.argv[2]
```