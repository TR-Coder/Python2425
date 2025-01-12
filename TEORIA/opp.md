# Introducció
De moment hem aprés a programar d'una manera estrucutrada però sense aplicar cap metodologia en particular. Disposem d'unes eines que el Python proporciona i hem aprés a utilitzar-les encara que no d'una manera conjunta per a resoldre problemes. La OPP proporciona un conjunt d'estratègies per a crear la millor solució per a resoldre un problema.

Amb programes xicotes la programació seqüèncial que hem estudiat es suficient però esdevé inmanejable davant programes grans. Es tractar de buscar un paradigma que permeta estructurar el codi d'una manera senzilla, que siga escalable, mantenible, que facilite la lectura, la depuració, la correcció d'errors, etc. Ací és on entra en joc la POO.

En POO un objecte és una entitat abstracta que representa un objecte del món real.  

# Conceptes programació orientada a objectes (OPP)

Entendre, mantindre i actualitzar un programa format per una gran col·lecció de funcions és díficil.

La descomponsició dels programes en funcions no és suficient per aconseguir la reusabilitat del codi.

L'OPP intenta superar les limitacions de la programació estructurada mitjançant un estil de programació en què les tasques es fan mitjançant la col·laboració d'objectes.

Un objecte encapsula una atributs i uns mètodes que els manipulen. Els atributs són les propietats (variables) de l'objecte i els mètodes les funcions per a manipular-les.


Una classe és com una plantilla del mateix tipus.
El procés de crear un objecte a partir de la classe es un procés anomenat _instanciar_. Tot objecte pertany sempre a una determinada classe.

Per a instanciar s'usa un mètode especial anomenat _constructor_ que crea l'objete i inicialitza els atributs als seua valors inicials. En Python és el mètode \___init___()

Una vegada crear un objecte utilitzem l'operador punt per accedir i modificar el seus atributs, així com executar els seus mètodes.



## Abstracció
Una classe en una abstracció de la realitat. Hem de seleccionar aquells atributs i mètodes que representen les dades i el comportament de la realitat que volem modelar.

## Encapsulació
Cada classe s'encarrega del seu propi estat i oferirà aquells mètodes necessaris per a manipular-los.

Una classe no ha de permetre que es puguen modificar els seus atributs perquè pot causar inconsistència en el seu estat, els atributs s'han de canviar d'una manera controlada.

Una classe ha de declarar quin dels seus atributs i mètodes són publics i podran ser accedits per codi de fora de la classe. Això és el que es coneix com encapsulació.

A aquells atributs que només són accessibles des de mètodes de la pròpia classe es coneixen com _atributs privats_. Si volem que un atribut siga _public_, és habitual que el seu accés no es faça de manera directa a través de l'operador punt sinó a través d'un mètode específic que garantix un accés controlat. Estos mètodes se'ls coneix com a getter i setter. El _getter_ permet llegir el valor de l'atribut i el _setter_ de modificar-lo.

## Herència
L'herència permet que una classe puga ampliar el comportament d'una altra classe.

L'herència fa que una classe (anomenada filla o subclasse) herede les propietats i mètodes d'un altra classe (anomenada padre o superclasse) i afegisca els seus propis.

Les classes es relacionen entre elles forman una jerarquia de classes.

Els constructors no s'hereden, cada subclasse ha de definir el seu.
Una subclasse por redefinir un mètode de la classe pare, es diu que _sobreescriu_ el mètode.
Una classe abstracta és aquella que té un o més mètodes sense implementar.

Una _classe abstracta_ no permet crear objectes, servix com a superclasse d'altres classes. El mètodes sense implementar s'anomenen _mètodes abstractes_ i s'han de redefinir en les classes filles.
En alguns llenguatges es permet l'herència múltiple (com Python) que permet crear una subclasse a partir de més d'una classe pare.


## Polimorfisme
En una herència de classes diferents classes poden tindre un mètode amb el mateix nom però que fan operacions diferents. Cridar a un mètode o un altre depen de l'objecte amb què invoquen el mètode.


# POO en Python

## Constructor __init__(self)
Un constructor és un mètode especial que crea un objecte (instància d'una classe) i inicialitza les seues variables d'instància. En Python és el mètode \_\_init\_\_(self).

\_\_init\_\_(self) no retorna mai cap valor. També és opcional i es pot ometre si no hi ha variables d'instància.

El primer paràmetre ha de ser sempre self i fa referència al propi objecte que s'està inicialitzant.

Per instanciar un objecte cridem al nom de la classe i entre parèntesis els arguments que li passen al constructor \_\_init\_\_().

self se passa automàticament a init().

Per a accedir a una propietat o un invocar un mètode s'usa l'operador punt a través del nom de l'objecte.


## Atributs de classe i d'instància
Els atributs poden ser:
* __Atributs d'instància__: Són atributs particulars de cada instància.
* __Atributs de classe__: Són atributs que pertanyen a la pròpia classe i són comuns per a tots els objectes que la instancien. Es declaren al mateix nivell que els mètodes.

```python
class Gos:
    especie = 'mamífer'				# Atribut de classe
    def __init__(self, nom, raça):
        self.nom = nom				# Atribut d'instància
        self.raça = raça

g = Gos('trufa', 'xarnego')

g.nom			# Accés a atribut d'instància.
g.especie		# Accés a atribut de classe a través de l'objecte.
Gos.especie		# Accés a atribut de classe a través de la classe.
```

Quan un atribut d'instància té el mateix nom que un atribut de classe, l'atribut d'instància tapa al de classe.

__EXEMPLES:__

No hem d'oblidar self a l'hora de crear atributs d'instància, si l'oblidem estarem creant variables locals.

```python
class Base:
    n = 0					# Atribut de classe
    def __init__(self):
        n = 2				# Variable local a __init__() ja que no hem utilitzat self.n

b = Base()
Base.n			# 0		Accés a l'atribut de classe n
b.n				# 0		No es pot accedir a n d'init() ja que és una variable local en init(). Accedirem a l'atribut de classe n
```

```python
class Base:
    n = 0					# Atribut de classe
    def __init__(self):
        self.n = 2			# Atribut d'instància

b = Base()
Base.n			# 0		Accés a l'tribut de classe n
b.n				# 2		Accés a l'atribut d'instància n
```

No hem d'intentar utilitzar una variable d'instància abans de crear-la.
```python
class Base:
    n = 9					# Atribut de classe
    def __init__(self):
        print(self.n)		# Com no hi ha atribut d'instància n mira si hi ha atribut de classe n.

b = Base()			# 9
```

```python
class Base:
    def __init__(self):
        self.n = self.n + 1  # ERROR, intentem un self.n abans que existica.
							 # AttributeError: 'Base' object has no attribute 'n'
b = Base()
```

```python
class Base:
    n = 9					# Atribut de classe
    def __init__(self):
        self.n = self.n + 1  # ERROR, intentem un self.n abans que existica.

b1 = Base()
Base.n			# 9
b1.n			# 10

b2 = Base()
Base.n			# 9
b2.n			# 10
```

L'accés a un atribut de classe es fa a través del nom de la classe o de qualsevol instància seua.

```python
class Base:
    n = 0						# Atribut de classe

    def __init__(self):
        Base.n = Base.n + 1  	# Accés a l'atribut de classe n.

Base.n				# 0
b1 = Base()
Base.n				# 1
b1.n				# 1

b2 = Base()
Base.n				# 2
b1.n				# 2
b2.n				# 2
```

## Atributs privats
Python no té atributs privats i deixa la responsabilitat de l'accés als atributs al programador.

Per convenció aquells atributs que volem fer «ocults» han de començar amb un doble guió. Com vorem, això no impedix que siguem capaços d'accedir a estos atributs. El doble guió és com un avís de que la variable ha de ser considera oculta i no es convenient accedir a ella directament.

Quan posem un doble guió, el que ocorre és el que es coneix com a «name mangling» que consistix en modificar el nom de l'atribut amb un prefix _Classe, on Classe és el nom de la classe. En el següent exemple es veu com sabent com s'reanomenen les variables som capaços d'accedir a ella. 

```python
class Base:
    def __init__(self, nom):
        self.__nom = nom

b = Base('ordinador')		# ordinador
print(b._Base__nom)
```

## Setter i Getter
Per a implementar setter i getter s'usen els decoradors @property i @nom.setter. En el següent exemple fixem-nos amb la coincidència en el nom de les funcions ff(self) i def ff(self), i també en el decorador @ff.setter. S'han posat estos noms tant estranys per qüestions didàtiques.

```python
class Base:
    def __init__(self, n):
        self.nom_ocult = n

    @property
    def ff(self):
        print('Dins getter')
        return self.nom_ocult

    @ff.setter
    def ff(self, x):
        print('Dins setter')
        self.nom_ocult = x

base = Base('ordinador')
print(base.ff)				# Dins getter	ordinador
base.ff = 'impressora'		# Dins setter
print(base.ff)				# Dins getter	impressora
```

Reescrivim el codi anterior amb un nom de les variables i les funcions més significatiu. Res impedix puguem accedir i canviar directament la variable nom_ocult. 

```python
class Base:
    def __init__(self, nom):
        self.nom_ocult = nom

    @property
    def nom(self):
        print('Dins getter')
        return self.nom_ocult

    @nom.setter
    def nom(self, nom):
        print('Dins setter')
        self.nom_ocult = nom

base = Base('ordinador')
print(base.nom)				# Dins getter	ordinador
base.nom= 'impressora'		# Dins setter
print(base.nom)				# Dins getter	impressora
```

## Atributs calculats
Per a crear un atribut calculat utilitzem el decorador @property. Per exemple:

```python
class Base:
    def __init__(self, nom, pes):
        self.nom = nom
        self.pes = pes

    @property
    def variacio_pes(self):
        return 0.3 * self.pes


base = Base('base', 1)
print(base.variacio_pes)		# 0.3
```
## Mètodes d'instància, de classe i estàtics

### Mètodes d'instància
Els mètodes d'instància són els mès habituals, reben self com a primer argument i això els permet accedir als atributs d'instància i altres mètodes d'instància.

Els mètodes de classe (classmethod) reben cls com a primer argument i això els permet accedir als atributs de classe però no als atributs d'instància. Se declaren amb el decorador @classmethod.

```python
class Base:
    n = 30
    def __init__(self, n):
        self.n = n

    @classmethod
    def get_pes(cls):
        return cls.n

b = Base(1)
b.n				# 1
b.get_pes()		# 30
Base.n			# 30
```

__EXEMPLES:__

Els mètodes d'instància reben self com a primer paràmetre, encara que es pot utilitzar qualsevol nom.
```python
class A:
    def f(a, b):
        print(a, b)		# a rep self i b rep 99
a = A()
a.f(99)					# OK
a.f(99, 88)				# ERROR, massa arguments
```

Encara que funciona, este codi és incorrecte ja que estem accedir a un mètode d'instància a través del nom de la classe, per la qual cosa a rep 99 i no self.
```python
class A:
    def f(a, b):
        print(a, b)		# 99	88

A.f(99, 88)
```

Quan utilitzem mètodes de classe no necessitem cap instància, accedim a través del nom de la classe.

```python
class A:
    @classmethod
    def f(a, b):		# a rep cls, b 99 i faltaria un paràmetre c per a rebre el 88
        print(a, b)

a = A()
a.f(99, 88)				# Error, massa arguments, sobra el 88
						# Com és un mètode de classe seria millor fer A.f(99, 88)
						# encara que es pot accedir a través d'una instància.

class B:
    @classmethod
    def f(cls, b, c):		# a rep cls, b 99 i c 88
        print(cls, b, c)

B.f(99, 88)					# OK, accedim amb B. No necessitem cap instància.
b = B()
b.f(99, 88)					# OK, accedim a través d'una instància.
							# Com hem ficat @classmethod rebrem cls i no self.
```

### Mètodes estàtics
En Phyton els mètodes estàtics (staticmethod) són similars als de classe. Al contrari que amb mètodes de classe, els estàtics no reben cls com a primer argument, això fa que per accedir als atributs de classe hagem de fer-ho a través del nom de classe. Se declaren amb el decorador @staticmethod.

```python
class Base:
    n = 30
    def __init__(self, n):
        self.n = n

    @staticmethod
    def get_pes():
        return Base.n		# Enlloc de cls.n fem Base.n

b = Base(1)
b.n				# 1
b.get_pes()		# 30
Base.n			# 30
```

En realitat, els mètodes estàtics i de classe es comporten de manera diferent quan hi ha herència. Vegem-ho amb un exemple:

En este codi la funció sum() és una @classmethod.

```python
class Number:
    def __init__(self, value):
        self.value = value

    @classmethod
    def sum(cls, value1, value2):
        return cls(value1+value2)
        
    def print(self):
        print(str(self.value))
        
class Float(Number):
    def print(self):
        print(f'{self.value:.2}')
        
n = Number(0.15647)
n.print()						# 0.15647

f = Float(0.15647)
f.print()						# 0.16

f = Float.sum(0.11, 0.1593)
print(type(f))					<class '__main__.Float'>
f.print()						# 0.27
```

El següent codi és com l'anterior amb la diferència que sum() passa a ser un @staticmethod.

```python
class Number:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def sum(value1, value2):
        return Number(value1+value2)
    def print(self):
        print(str(self.value))

class Float(Number):
    def print(self):
        print(f'{self.value:.2}')

n = Number(0.15647)
n.print()						# 0.15647

f = Float(0.15647)
f.print()						# 0.16

f = Float.sum(0.11, 0.1593)
print(type(f))					# <class '__main__.Number'>
f.print()						# 0.2693
```

Com observem, els resultats no són iguals. Quan fem un Float.sum(), en el cas de @classmethod el print que es crida és el de la classe derivada Float ja que f és un Float. En canvi, en el cas de @staticmethod es crida el de la classe Number ja que f és de tipus Number.

### Mètode dir()
El mètode dir() retorna una llista dels atributs i mètodes de l'objecte que li passem. Exemple:

```python
class Cercle:
    
    pi = 3.141592
    
    def __init__(self, radio):
        self.radio = radio
        self.__color = "roig"
    
    def area(self):
        return Cercle.pi * (self.radio ** 2)

cercle = Cercle(6)
print(dir(cercle))
```

A continuació el resultat del dir(cercle). Entre altres observem: _Cercle__color, area, pi i radio.
```python
['_Cercle__color', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'pi', 'radio']
```


## slots
https://towardsdatascience.com/understand-slots-in-python-e3081ef5196d


## Simular una Struct
Encara que Python no permet crear estructures, podem simular-les amb una classe buida i la creació dinàmica d’atributs. Python guarda els atributs dels objectes en el diccionari \_\_dict__.

```python
class Base:
    pass

b = Base()

b.atr1 = 'atribut 1'
b.atr2 = 'atribut 2'
b.atr3 = 'atribut 3'
print(b.__dict__)		# {'atr1': 'atribut 1', 'atr2': 'atribut 2', 'atr3': 'atribut 3'}
```

Este sistema pot suposar un desperdici d’espai per als objectes en el cas d’herències i, sobre tot, si hem de crear un gran nombre d’instàncies. Per a evitar-lo utilitzarem un slot. 

```python
class Base:
    __slots__ = ['atr1', 'atr2', 'atr3']

b = Base()

b.atr1 = 'atribut 1'
b.atr2 = 'atribut 2'
b.atr3 = 'atribut 3'
```

Al fer-ho l’objecte que crearem no disposarà del diccionari \_\_dict__, per la qual cosa no admetrà la creació dinàmica d’atributs, i només podrem crear els que apareixen en la llista \_\_slots__.

```python
b.atr4 = 'atribut 4'	# AttributeError: 'Base' object has no attribute 'atr4'
print(b.__dict__)   	# AttributeError: 'Base' object has no attribute '__dict__'
```
## Atributs incorporats en les classes
Les classes disposen dels següents atributs incorporats a què podem accedir com qualsevol altre atribut.
* \_\_dict__ :	Diccionari que conté l'espaci de noms de la classe
* \_\_doc__	Cadena de documentació de la classe.
* \_\_name__	Nom de la classe
* \_\_module__	Nom del mòdul en què es definix la classe
* \_\_bases__	Tupla que conté les classes base, en l'ordre de la seua aparició en la llista de classes base

```python
class Classe:
    '''Documentació de la classe'''
    def __init__(self):
        pass
        
print(Classe.__doc__)		# Documentació de la classe
print(Classe.__name__)		# Classe
print(Classe.__module__)	# __main__
print(Classe.__bases__)		# (<class 'object'>,)

print(Classe.__dict__)		# {'__module__': '__main__',
							#  '__doc__': 'Documentació de la classe',
							#  '__init__': <function Classe.__init__ at 0x7f2f23b8fdc0>,
							#  '__dict__': <attribute '__dict__' of 'Classe' objects>,
							#  '__weakref__': <attribute '__weakref__' of 'Classe' objects>}
```


## Mètodes especials
Són un conjunt de mètodes predefinits que permeten afegir certes funcionalitats a les classes. Totes ells comencen i acaben amb un doble guión baix, per la qual cosa també se'ls coneix com a dunders (double underline). També se'ls coneix com a mètodes màgics. El més conegut és el mètode \_\_init__()

http://www.tugurium.com/python/index.php?C=PYTHON.11

## Recolecció de brossa


## Herència
Amb l'herència una classe filla (o subclasse) hereta els atributs i mètodes de la classe pare (o base). Estos atributs/mètodes poden ser sobreescrits per la classe filla que, a més, pot afegir els seus propis. 

Per a coneixer la classe pare d'una classe fem:
_ClasseFilla.\_\_bases___

Per a coneixer le classes que deriven d'una classe fem:
_ClassePare.\_\_subclasses___()

```python
class Animal:
    pass

class Gos(Animal):
    pass


class Gat(Animal):
    pass

print(Gat.__bases__)				# (<class '__main__.Animal'>,)
print(Animal.__subclasses__())		# [<class '__main__.Gos'>, <class '__main__.Gat'>]
```	

Per a saber si un objecte és una instància d'un classe utilitzem isinstance(obj, classe).
```python
a = Animal()
g = Gat()
print(isinstance(g, Animal))	# True
```

Per a verificar si una classe1 és una subclasse d'una classe2 utilitzem issubclass(classe1, classe2). Es considera que una classe és sempre una subclasse d'ella mateixa.
```python
a = Animal()
g = Gat()
print(issubclass(Gat, Animal))		# True
```

## super().metode()
La funció super() permet accedir als mètodes i atributs de la classe pare des d'una classe filla. Amb super() evitem especificar implicitament el nom de la classe pare, pel que si la canvien la classe super() apuntarà a la nova classe pare.


## Constructor init()
En el següent exemple com la classe Filla no ha redefinit el mètode init() sinó que hereta el de la classe Pare.

```python
class Pare:
    def __init__(self,num):
        print('constructor Pare')
        self.n = num

class Filla(Pare):
    def mostra(self):
        print(self.n)

f = Filla(8)        # constructor Pare
f.mostra()          # 8
```

Ara redefinim init() en la classe Filla. Obtenim un error ja que com no hem cridat explícitament a l'init() de Pare no s'ha creat l'atribut n.

```python
class Filla(Pare):
    def __init__(self, num):
        self.n = num
        
    def mostra(self):
        print(self.n)       AttributeError: 'Filla' object has no attribute 'n'
```

Ara ho fem bé.

```python
class Filla(Pare):
    def __init__(self, num):
        super().__init__(num)
        self.m = num
        
    def mostra(self):
        print(self.n)  
```

## Herència múltiple
Si cridem a un mètode que totes les classes tenen en comú, a quin es crida? 
La manera de saber-ho és cridar l'MRO (Method Order Resolution) que retorna una tupla amb l'ordre de busca de les classes. Este ordre comença sempre en la pròpia classe i va pujant fins la classe pare, d'esquerra a dreta.

```python
class Classe1:
    pass
class Classe2:
    pass
class Classe3(Classe1, Classe2):
    pass

print(Classe3.__mro__)	# (<class '__main__.Classe3'>, <class '__main__.Classe1'>, <class '__main__.Classe2'>, <class 'object'>)
```

https://www.python.org/download/releases/2.3/mro/
https://www.youtube.com/watch?v=IqwWxZrMcx4



# Interfícies i classes abstractes



https://ellibrodepython.com/metodos-estaticos-clase-python

http://www.tugurium.com/python/index.php?C=PYTHON.11





