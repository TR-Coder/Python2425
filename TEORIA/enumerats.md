https://realpython.com/python-enum/
https://docs.python.org/3/howto/enum.html#enum-class-differences


# Enumerats
Un enumerat, o un enum, és un conjunt de constants relacionades entre elles que s'accedixen a través del propi enum.

Python suporta els enum, però, no disposa d’una sintaxi pròpia dedicada a ells. Els enum es creen com una subclasse de la classe Enum del mòdul enum.

Encara que és una classe, és una classe un tant especial, ja que:
* No es poden instanciar
* No es poden crear subclasses d'ell (a no ser que la classe base estiga buida)
* Són iterables retorna els seus membres en una seqüència.
* Els seus membres són hashables i es poden utilitar com a claus en un diccionari.
* Els seus membres es poden accedir amb notació punt i claudator.
* El valor dels seus membres no es poden canviar.

```python
from enum import Enum

class Day(Enum):
    DILLUNS = 1
    DIMARTS = 2
    DIMECRES = 3
    DIJOUS = 4
    DIVENDRES = 5
    DISSABTE = 6
    DIUMENGE = 7
```
* Cada membre de l'enum es declara amb majúscules i els valor de cada membre és una constant.

* Podem accedir a l'enumerat per nom i per valor (el primer valor)

```python
    Day.DILLUNS o  Day['DILLUNS']
    Day(2)                          # Day.DIMARTS
```

```python
    type(Day)		    # <class 'enum.EnumType'>
    type(Day.DILLUNS	# <enum 'Day'>
```

```python
for item in Day:
    print(item.name, item.value, type(item.name),type(item.value))

DILLUNS 1 <class 'str'> <class 'int'>
DIMARTS 2 <class 'str'> <class 'int'>
DIMECRES 3 <class 'str'> <class 'int'>
DIJOUS 4 <class 'str'> <class 'int'>
DIVENDRES 5 <class 'str'> <class 'int'>
DISSABTE 6 <class 'str'> <class 'int'>
DIUMENGE 7 <class 'str'> <class 'int'>		
```

____list()__ crea una llista amb els membres de l'enum:

```python
llista = list(Day)
print(llista[0],llista[0].name, llista[0].value, type(llista[0]))   # Day.DILLUNS    DILLUNS    1     <enum 'Day'>
```

El normal és que el valor dels membres de l'enum siguen tot del mateix tipus.
```python
class Grade(Enum):
	A = 90
	B = 80
	C = 70
	D = 60
	F = 0
```

```python
class Talla(Enum):
	S = 'small'
	M = 'medium'
	L = 'large'
	XL = 'extra large'
```

```python
class Switch(Enum):
	ON = True
	OFF = False
```

Podem crear enumerats buits. 

Els enumerats no permeten ser heretats excepte en el cas de que estiguen buits. Encara que un enumerat estiga buit permet que es creen mètodes.
Aleshores, podem crear una jerarquia de classes enum que reutilitzen al funcionalitat d’estos mètodes.

```python
class BaseEnum(Enum):
    def llista(self):
        try:
            return list(self.value)
        except TypeError:
            return [str(self.value)]


class Vocals(BaseEnum):
    MINUSCULES = 'aeiou'
    MAJUSCULES = 'AEIOU'


print(Vocals.MINUSCULES.llista())		# ['a', 'e', 'i', 'o', 'u']
```




