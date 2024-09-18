# Diccionaris

 Els diccionaris són una estructura de dades ordenada, mutable i de clau única.


## Creació
```python
diccionari_buit = {}
diccionari_buit = dict()
diccionari = {'a':1 , 'b':2, 'c':3}
```

Amb el constructor dict() podem ometre les cometes en les claus, estes han de ser identificadors vàlids de Python (no es permeten els espais en blanc).
```python
dict(nom='Pere', edat=0)  				# {'nom':'Pere', 'edat':0}
dict(a=1, b=2, c=3, d=4)  				# {'a':1, 'b':2, 'c':3, 'd':4}
dict({'a':1, 'b':2, 'c':3})  			# {'a':1, 'b':2, 'c':3, 'd':4}
```

Creació a partir d'un iterable de dos elements (clau i valor):
```python
dict([('a', 1), ('b', 2)], d=4)			# {'a': 1, 'b': 2, 'd': 4}
```

Creació a partir d'un iterable de claus:
```python
iter = ('A', 'B', 'C')
d = dict.fromkeys(iter, 1)				# {'A':1, 'B':1, 'C':1}
d = dict.fromkeys(iter)					# {'A':None, 'B':None, 'C':None}
```


## Lectura
### Indexant la clau
```python
d['clau']    							# Si la clau no existix dóna error
```
### get()
Si la clau existix retorna el valor associat a _clau_, si no existix retorna _defecte_ (del tipus que siga)
```python
d.get('clau', defecte)
d.get('clau')  							# Si la clau no existix retorna None
```

## Afegir/Modificar

* Si la clau existix 'subtituix' el seu valor pel nou 'valor'.

* Si la clau no existix s'afegix al diccionari clau:valor
```
d['clau'] = 'valor'
```

## __setdefault__(_clau_, _valor_defecte_): afegir només nous elements 

* Si la clau existix:
	* _Retorna_ el valor de la clau existent. No s'afegix res.
* Si la clau no existix:
	* Afegix al diccionari __clau__ : __valor_defecte__. Retorna el __valor_defecte__
	* Si no s'indica _valor_defecte_ se li assigna None. __clau__ : __None__. Retorna __None__
```python
d = {'a': 1, 'e': 2}
res = d.setdefault('a', 'X')  		# res=1		d no es modifica.
res = d.setdefault('b',6)			# res=6		{'a': 1, 'e': 2, 'b': 6}
res = d.setdefault('c')				# res=None 	{'a': 1, 'e': 2, 'b': 6, 'c': None}
```


## __update()__: actualitza/afegix elements a partir d'un diccionari o iterable.

update() actualitza o afegix elements a un diccionari a partir d'un altre diccionari o d'un iterable format per parelles clau:valor (normalment una tupla).

Si cridem a update() sense paràmetres el diccionari no es modifica i
retorna _None_

update() afegix un element al diccionari si la seua clau no està en el diccionari. Si la clau ja està en el diccionari actualitza el seu valor pel nou.

```python
d1 = {'a':1, 'e':2}
d2 = {'a':'A', 6:'SIS'}			# Actualitza el valor de la clau 'a' i afegix 6:'SIS'
d1.update(d2)					# d1 = {'a':'A', 'e':2, 6:'SIS'}. 
```

update() a partir d'una llista (iterable) de tuples (clau,valor)
```python
d2 = [('a', 'A'), (6, 'SIS')]
d1.update(d2)								# d1 = {'a': 'A', 'e': 2, 6: 'SIS'}
```


## len(): nombre d'elements: 
```python
d1 = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5}
len(d1)										# 5
```


## Patró de creació
```python
vocals = 'aeiou'
d = {}
for i, vocal in enumerate(vocals):
    d[vocal] = i+1              			# 'a':1, 'e':2, 'i':3, 'o':4, 'u':5}
```

## Pertinença: in
```python
'clau' in d									# True o False
```

## Comparació amb ==

Dos diccionaris són iguals si contenen el mateix nombre de parells _clau:valor_. No cal que estiguen en el mateix ordre.


## Recuperar claus i valors: _keys(), values() i items()_

```python
d = {'a': 1, 'e': 2, 'i': 3}
```

* __keys()__ retorna les claus en forma d'un _iterable_ del tipus _dict_keys_.
```python
x = d.keys() 				#  x = dict_keys([ 'a', 'e', 'i' ])
```

* __values()__ retorna els valors en forma d'un iterable del tipus _dict_values_.
```python
x = d.values()  			#  x = dict_values([ 1, 2, 3 ])
```

* __items()__ retorna tuples (clau,valor) en froma d'un __iterable__ del tipus _dict_items_. 
```python
x = d.items()				#  x = dict_items([ ('a',1), ('e',2), ('i',3) ])
```

## Iterar sobre un diccionari
```python
d = {'a': 1, 'e': 2, 'i': 3}
```
```python
for clau in d:
    print(clau)					# a e i

for valor in d.values():
    print(valor)				# 1 2 3

for clau in d:
    print(d[clau])				# 1 2 3

for clau, valor in d.items():
    print(clau, valor)			# a 1   e 2   i 3
```

## Convertir les claus i els valors en una llista.
Els tipus _dict_keys_ i _dict_values_ són iterables però no es podem indexar com en x[0]. Per a fer-ho hem de convertir-los en una llista:
```python
list(d.keys()) 		# ['a', 'e', 'i', 'o', 'u']
list(d)				# ['a', 'e', 'i', 'o', 'u']
[key for key in d]  # ['a', 'e', 'i', 'o', 'u']
[*d]  				# ['a', 'e', 'i', 'o', 'u']		Operador desempaquetador * sobre llistes
*d,  				# ('a', 'e', 'i', 'o', 'u')		Operador desempaquetador * sobre tuples
{*d}  				# {'o', 'e', 'i', 'u', 'a'}		Operador desempaquetador * sobre conjunts
```


## Esborrar
```python
d = { 'a': 1, 'e': 2, 'i': 3 }
```
```python
d.clear()				# Esborra tot el diccionari d={}
```

### d.pop(clau, valor_defecte)
* Si la clau existix s'esborra i retorna el seu valor.
* Si la clau no existix retorma el _valor_defecte_. Si no s'especifica _valor_defecte_ llança una excepció _KeyError_.
```python
res = d.pop('a')		# res=1	 d={'e': 2, 'i': 3}
res = d.pop('z', 0)		# res=0	 d={'a': 1, 'e': 2, 'i': 3}
res = d.pop('z')		# KeyError: 'z'
```

### popitem(clau)
Esborrar l'últim element _clau:valor_ del diccionari i el retorna la tupla _(clau,valor)_. Si el diccionari està buit llança una excepció KeyError.
```python
res = d.popitem()  		# res=('i',3)   d={'a': 1, 'e': 2}
```

##  Còpia superficial: copy()
Com en les llistes tenim deepcopy() del mòdul copy.
```python
d2 = d1.copy()
```

## Combinar diccionaris
```python
d1 = {'a': 1, 'e': 2}
d2 = {'A': 10, 'U': 11}
```
SENSE modificar els diccionaris originals. Desempaquetament amb l'operador **
```python
d3 = {**d1, **d2}		# {'a':1, 'e':2, 'A':10, 'U':11}
d3 = d1 | d2			# L'operador | és com + en les llistes
```

```python
# Si hi ha claus repetides, els valors de més a la dreta prevaleixen,
nombres = { 'un':1, 'dos':2, 'tres':3 }
lletres = { 'a':'A', 'tres':999}
combinar = {**nombres, **lletres}			# {'un': 1, 'dos': 2, 'tres': 999, 'a': 'A'}
```

MODIFICANT els diccionaris originals (mirar l'apartat d'update)
```python
d1.update(d2)			# d1 = {'a':1, 'e':2, 'A':10, 'U':11}
```


## Creació de diccionaris per compressió
```python
d1 = ('A', 'BC', 'DEF')
d2 = {x: len(x) for x in d1}							# d2 = {'A':1, 'BC':2, 'DEF':3}
d2 = {x: len(x) for x in d1 if x[0] not in 'ABC'}		# d2 = {'DEF':3}
```
