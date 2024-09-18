https://realpython.com/python-enum/

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

# Cada membre de l'enum es declara amb majúscules i els valor de cada membre és una constant.

# Podem accedir a l'enumerat com:
Day.DILLUNS o  Day['DILLUNS']

type(Day)				# <class 'enum.EnumMeta'>
type(Day.DILLUNS)		# <enum 'Day'>
```

Estacions.__members__.items() és un iterable on cada element és un tupla de dos elements. El primer element és una cadena amb el nom del membre de l'enum, i el segon és el propi enum (de tipus enum).

```python
for item in Estacions.__members__.items():
    print(item, type(item))

('PRIMAVERA', <Estacions.PRIMAVERA: 1>) <class 'tuple'>
('ESTIU', <Estacions.ESTIU: 2>) 		
('TARDOR', <Estacions.TARDOR: 3>) 		
('HIVERN', <Estacions.HIVERN: 4>) 		
```

```python
for clau, valor in Estacions.__members__.items():
    print(clau, valor.value, type(valor))

PRIMAVERA 	1 	<enum 'Estacions'>
ESTIU 		2 	
TARDOR 		3 	
HIVERN 		4 	
```

list(Day) crea una llista amb els membres de l'enum:

```python
[<Day.DILLUNS: 1>, <Day.DIMARTS: 2>, <Day.DIMECRES: 3>, <Day.DIJOUS: 4>, <Day.DIVENDRES: 5>, <Day.DISSABTE: 6>, <Day.DIUMENGE: 7>]

llista[1]			Day.DIMARTS 	<enum 'Day'>
llista[1].value		2				int
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




