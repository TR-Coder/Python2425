# Tuples
Una tupla és com una llista però __immutable__. Permet les mateixes operacions que les llistes excepte les que impliquen modificacions com reverse(), append(), extend(), remove(), clear() i sort().


## Creació
Una vegada creada no es pot modificar. Els parèntesis són opcionals.
```python
tupla_buida = ()
tupla_un_element = (1,)
tupla_sense_parentesis = 1,2,3
```

## Conversió a tupla: _tuple()_
Per a convertir un iterable a tupla usem tuple()
```python
tuple('hola') 		# ('h', 'o', 'l', 'a')
```

## DESEMPAQUETAMENT D'ITERABLES
A la dreta de l'operador = ha d'haver un iterable i a l'esquerra una tupla o un list.

### Desempaquetament de tuples, strings i llistes:
```python
a,b,c = 1,2,3       # a=1	b=2	  c=3
a,b,c = "123"
a,b,c = [1,2,3]
```

### El nombre de variables i valors ha de coincidir:

```python
a,b,c = 1,2,3,4		# ValueError: too many values to unpack (expected 3)
a,b,c,d = 1,2,3		# ValueError: not enough values to unpack (expected 4, got 3)
```

### Desempaquetament d'un diccionari: claus, valors i items.
```python
dict = {'un':1, 'dos':2, 'tres':3}
a,b,c = dict				# a='un'		b='dos'			c='tres'
a,b,c = dict.values()		# a=1			b=2				c=3
a,b,c = dict.items()		# a=('un',1)	b=('dos',2) 	c=('tres',3)
```

### Desempaquetament d'un range()
```python
a,b,c = range(3)			# a=0	a=1   a=2
```

### Desempaquetador de generadors
Mentres que els tipus mutables (llistes, diccionaris i conjunts) es poden crear per comprensió, no passa el mateix amb els tipus immutables.

Si intentem crear un tupla per compressió obtindrem una funció generadora.
```python
gen = (i**2 for i in range(3))			# <class 'generator'>
a,b,c = gen								# a=0	b=1	  c=4
```

### Desempaquetament en bucles for
```python
vendes = [('llapis',0.22,1500),('llibreta',1.30,550)]

for producte,preu,quantitat in vendes:
    print(producte,preu,quantitat)			# llapis 0.22 1500	llibreta 1.3 550
```
```python
for primer, *resta in vendes:
    print(primer,resta)						# llapis [0.22, 1500]	llibreta [1.3, 550]
```
L'estructura de l'iterable ha de casar amb les variables de blucle
```python
dades = [ ((1,2),3), ((4,5),6) ]

for a,b,c in dades:
    print(a,b,c)					# ValueError: not enough values to unpack (expected 3, got 2)
    
for (a,b),c in dades:				#  1 2 3   4 5 6
    print(a,b,c)
```

## EMPAQUETAMENT AMB L'OPERADOR *
L'operador * permet empaquetar múltiples valors en una variable.
```python
*a, = 1,2           # a=[1,2]   	Atenció amb la coma!
a,*b = 1,2,3        # a=1 			b=[2,3]
*a,b = 1,2,3        # a=[1,2]		b=3
*a,b,c = 1,2,3      # a=[1] 		b=2		c=3
*a,b,c,d = 1,2,3    # a=[]			b=1		c=2		d=3
*a,= range(3)		# a=[0, 1, 2]	Atenció amb la coma!
```
Les variables sense * han de prendre un valor obligatoriament
```python
*a,b,c,d,e = 1,2,3	# a=[]		b=1		c=2		d=3		e=?¿
#ValueError: not enough values to unpack (expected at least 4, got 3)
```

## Asignació en paral·lel
```python
a,b,c = 1,2,3		# a=1	b=2   c=3
```

## Intercanvi de variables
```python
a,b = b,a
```

## Recopilació de valors
```python
seq = [1,2,3,4]
primer, enmig, ultim = seq[0], seq[1:3], seq[3]
# primer=1	enmig=[2, 3]  ultim=4
primer, *enmig, ultim = seq
```

## Eliminar valors innecessaris
```python
a,b,*c = 1,2,0,0,0,0,0			# a=1	b=2   c=[0, 0, 0, 0, 0]
```

## Funcions: retorn de tuples
```python
def potencia(n):
    return n, n**2, n**3

a,b,c = potencia(2)			# a=2	b=4	  c=8
```

## Fusió d'iterables
```python
tupla = (1,2)
llista = [1,2]
conjunt = {1,2}
cadena = "12"

(0, *tupla, 4)				# (0, 1, 2, 4)
[0, *llista, 4]				# [0, 1, 2, 4]
{0, *conjunt, 4}			# {0, 1, 2, 4}
```

Enlloc de fer:
```python
list(conjunt) + llista + list(tupla) + list(range(1,3)) + list(cadena)
# [1, 2, 1, 2, 1, 2, 1, 2, '1', '2']
```
És millor fer:
```python
[*conjunt, *llista, *tupla, *range(1,3), *cadena]
# [1, 2, 1, 2, 1, 2, 1, 2, '1', '2']
```