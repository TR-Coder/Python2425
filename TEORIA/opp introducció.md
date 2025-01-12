# Introducció
De moment, hem aprés a programar d'una manera estructurada on no estem aplicant cap metodologia en particular. Disposem unes eines que el Python proporciona i hem aprés a utilitzar-les. La OPP proporciona un conjunt d'estratègies per a crear la millor solució per a resoldre un problema.

Amb programes xicotes la programació seqüèncial que hem estudiat es suficient però esdevé inmanejable davant programes grans.
Es tractar de buscar un paradigma que permeta estructurar el codi d'una manera senzilla, que siga escalable, mantenible, que facilite la lectura, la depuració, la correcció d'errors, etc. Ací és on entra en joc la POO.

En POO un objecte és una entitat abstracta que representa un objecte del món real.  

# Atributs

Nota: al expressar el nom d'una classe utilitzem PascalCase.

```python
class Mobil():
    marca = 'Samsumg'       # Atributs: variables d'una classe
    model = 'S24'
    camera = '48MP'
```
Un objecte és una instància d'una classe. La classe és un plantilla i els objectes són els casos particulars creats a partir de la plantilla de la classe.

```python
mobil_1 = Mobil()       # l'objecte mobil_1 és una instància de la classe Mobil.
print(mobil_1.marca)    # Utilitzem l'operador punt per a accedir a propietats i...
mobil_1.camera = '52MP' # ...per a modificar-les.
```

En la definicó de classe Mobil anterior, els atributs són atributs de classe. Qualsevol objecte que instanciem tindran estos atributs amb el valor indicat e la classe. Cada atribut és propi de la instància i no es compartix amb la resta d'instàncies.

```python
# Podem accedir als atributs de classe a través del nom de la classe i a través de qualsevol instància de la classe.
a1 = Alumne()
a2 = Alumne()

print(a1.ies)       # RC
print(a2.ies)       # RC
print(Alumne.ies)   # RC

a1.poblacio = 'Benicarló'  # poblacio és un atribut d'instància de l'objete a1.

print(a1.poblacio)
# print(a2.poblacio)      AttributeError: 'Alumne' object has no attribute 'poblacio'

# Si creem un atribut d'intància amb el mateix nom que un atribut de classe el d'instància tapa al de classe.

a1.ies = 'CO'       # ies és un atribut d'instància de a1.
print(a1.ies)       # CO
print(a2.ies)       # RC
print(Alumne.ies)   # RC
```

# Constructors
Enlloc de crear els atributs amb uns valors fixos, els podem crear de manera dinàmica assignant-los el valor inicial. Es fa amb un mètodes especial anomenat __constructor__ i que sempre es diu __init__.

Cada vegada que instanciem un objecte es crida de manera automàtica al constructor de la classe. 

Exemple:

```python
class Mobil:
    def __init__(self, marca:str, model:str, camera:str) -> None:
        self.marca = marca
        self.model = model
        self.camera = camera


m1 = Mobil('Samsung', 'S24', '24Mpx')   # self seria m1 i se pasa automàticament. 
```

* Primera aproximació del qué fa el constructor:

    __self__ és una referència a l'objecte que s'està instaciant, en este cas _m1_.

    A l'instanciar la classe es crida al constructor. Este rep estos arguments:
__init__(m1, 'Samsung', 'S24', '24Mpx')

    El __self__ es el propi objecte _m1_ que estem instanciant:  self = m1

    Com en qualsevol funció els arguments es convertixen en 'variables locals':
    - marca  = 'Samsung'
    - model  = 'S24'
    - camera = '24Mpx'


    Fer, __self.marca = marca__ equival a fer __m1.marca = 'Samsung'__.
    Estem creant l'atribut _marca_ en l'objete _m1_ amb el valor inicial _Samsung_.

    De manera similar:
    - m1.model = 'S24'
    - m1.camera = '24Mpx'


    No hi ha cap raó que obligue que el nom dels arguments coincidisca amb el nom dels atributs, però és l'habitual. Per exemple:

```python
class Mobil:
    def __init__(self, p1:str, p2:str, p3:str) -> None:
        self.marca = p1
        self.model = p2
        self.camera = p3
```

* Segona aproximació del qué fa el constructor:

Realment self no es _m1_. _m1_ és una referència a l'objecte que s'ha creat. 

Abans de cridar a __init__, Python reserva una zona de memòria i fa el procés de construir l'objecte. El self és una referència a este objecte nou acabat de crear i és el que rep l'__init__(self).



# Mètodes
Un __mètode__ és una funció interna a un objecte i que interactua amb els seus atributs. Els mètodes sempre tenen self com a primer argument.

```python
class Mobil:
    def __init__(self, marca:str, model:str, camera:str) -> None:
        self.marca = marca
        self.model = model
        self.camera = camera

    def crida(self):
        print('Estàs cridant)
        print(f'Sóc un {self.marca}')

m1 = Mobil('Samsung', 'S24', '24Mpx')
m1.crida()

```

# Herència jeràrquica

Exemple 1:

```python
class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        
    def saluda(self):
        print('Hola')

class Empleat(Persona):
    pass

e1 = Empleat('Jaume',20)
e1.saluda()
```

Exemple 2:

```python
class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        
    def saluda(self):
        print('Hola')

class Empleat(Persona):
    def __init__(self, nom, edat, sou):
        super().__init__(nom, edat)
        self.sou = sou

p1 = Persona('Jaume',20)
e1 = Empleat('Carles',21,2000)
p1.saluda()
e1.saluda()
```

La classe _Empleat_ és una especialització de la _Persona_ amb els seus atributs i mètodes particulars.
Una classe pot *sobreescriure* (_substituir_) els mètodes de la *classe Pare*.


# Herència múltiple

```python
Exemple 1:
class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
        
    def saluda(self):
        print('Hola')

class Artista:
    def __init__(self, habilitat):
        self.habilitat = habilitat
        
    def mostra_habilitat(self) -> str:
        return f'La meua habilitat és {self.habilitat}'


class EmpleatArtista(Persona, Artista):
    def __init__(self, nom, edat, habilitat, sou):
        Persona.__init__(self, nom, edat)
        Artista.__init__(self, habilitat)
        self.sou = sou
        

e = EmpleatArtista('Pere',20,'saltar',1000)
e.mostra_habilitat()
```

Exemple 2:

+ __super()__ fa referència a qualsevol de les classes pare.

```python
class EmpleatArtista(Persona, Artista):
    def __init__(self, nom, edat, habilitat, sou):
        Persona.__init__(self, nom, edat)
        Artista.__init__(self, habilitat)
        self.sou = sou

    def mostra_habilitat(self):
        return f'Sóc un empleat i artista amb esta habilitat: {self.habilitat}'

    def presentat(self):
        print(self.mostra_habilitat())      # mètode local
        print(super().mostra_habilitat())   # mètode classe pare


e = EmpleatArtista('Pere',20,'saltar',1000)
e.presentat()           # Sóc un empleat i artista amb esta habilitat: saltar
                        # La meua habilitat és saltar

sino = issubclass(EmpleatArtista, Persona)  # True
instancia1 = isinstance(e,EmpleatArtista)   # True
instancia2 = isinstance(e,Artista)          # True
instancia3 = isinstance(e,Persona)          # True
```


En herència múltiple, si dos classes tenen el mateix atribut o el mateix mètode, s'agafarà a partir del que definisca el *MRO* (_Method Resolution order_).

L'_MRO_ indica l'ordre en què Python busca atributs i mètodes en les classes.Sinó s'especifica és per ordre d'aparició en la declaració:

```python
Exemple:
class A:
    def saluda(self):
        print('Hola, sóc A')

class B(A):
    def saluda(self):
        print('Hola, sóc B')
    
class C(A):
    def saluda(self):
        print('Hola, sóc C')
    
class D(B,C):       # Com l'ordre de declaració és B,C es mira primer
    pass            # els atributs/mètodes de B (de la rama de B)

hola = D().saluda() # 'Hola, sóc B'
```

Exemple:
```python
class A1:
    def saluda(self):
        print('Hola, sóc A1')

class A2:
    def saluda(self):
        print('Hola, sóc A2')

class B1(A1):
    pass
        
class B2(A2):
    pass
    
class C(B1,B2):     # Com l'ordre de declaració és B1,B3 es mira primer
    pass            # la rama de B1  

hola = C().saluda()     # 'Hola, sóc A1'
```

Per a vore la seqüència de busca:
```python
print(C.mro())
```

# Encapsulament
L'encapsulament permet protegir l'accés de propietats i mètodes.

En altres llenguatges, s'usen modificadors d'accés: _public_, _protected_ i _private_. Però Python delega en el programador la responsabilitat d'accés.

En Python es marca un atribut privat posant-li un *guió baix* al seu nom. És només una convenció (realment si podem accedir a l'atribut). Amb els mètodes passa igual.

Si posem *doble guió baix*, a banda d'indicar la intenció de fer-lo privat, Python no permet el seu accés.

```python
class MyClass:
    def __init__():
        self.__atributPrivat = 1
    
    def __saludaprivat():            # Mètode privat
        pass
```

# Setter i getter

Si volem accedir a propietats privades s'ha de fer de manera controlada a través d'un *getter* i *setter*.

```python
class Persona:
    def __init__(self,nom):
        self._nom = nom
        
    @property
    def nom(self):          # getter
        return self._nom

    @nom.setter             # setter
    def nom(self, nou):
        self._nom = nou


p = Persona('Joan')
p.nom = 'Joan2'
print(p.nom)
```

# Abstracció
En general abstracció és ocultar el funcionament intern d'un sistema.


Una *classe abstracta* és aquella que definix el seu comportament però sense implementar-lo, deixant esta tasca a les subclasses.

Una classe abstracta no es pot instanciar. Exemple:

```python
from abc import ABC, abstractclassmethod

class Persona(ABC):             # ABC fa que la classe siga abstracta
    def __init__(self,nom):
        self._nom = nom
        
    @abstractclassmethod
    def saluda(self):
        pass

# TypeError: Can't instantiate abstract class Persona without an implementation for abstract method 'saluda'
p = Persona('Joan')

```

No tots els mètodes d'una classe abstracta han de ser abstractes.
Al derivar d'una classe abstracta és obligatori implementar els mètodes abstractes:

```python
from abc import ABC, abstractclassmethod

class Persona(ABC):             # ABC fa que la classe siga abstracta
    def __init__(self,nom):
        self._nom = nom
        
    @abstractclassmethod
    def saluda(self):
        pass

class Estudiant(Persona):
    pass


TypeError: Can't instantiate abstract class Estudiant without an implementation for abstract method 'saluda'
e = Estudiant('pere')
```

Una classe on tots els seus mètodes són abstractes s'anomena *interfície*.

Que una classe implemente una interfíce és una manera d'assegurar que eixa classe disposa dels mètodes que implementen la funcionalitat que la interfície manifesta.


```python
class TargetaCredit(ProcessamentPagament):
    def paga(self, quantitat:float) -> None:
        print(f'Has pagat amb targeta de crèdit {quantitat} euros')

class PayPal(ProcessamentPagament):
    def paga(self, quantitat:float) -> None:
        print(f'Has pagat amb Paypal {quantitat} euros')
        
class Efectiu(ProcessamentPagament):
    def paga(self, quantitat:float) -> None:
        print(f'Has pagat en efectiu {quantitat} euros')        
        

def pagar_factura(metode_pagament: ProcessamentPagament, quantitat:float ) -> None:
    metode_pagament.paga(quantitat)

tc = TargetaCredit()
pp = PayPal()
ef = Efectiu()

pagar_factura(tc, 100)
pagar_factura(pp, 200)
pagar_factura(ef, 50)
```

# Mètodes especials
Un mètode especial és un mètode que és propi de Python i s'identifica perquè els seu nom comença i acaba amb doble guió baix. Per exemple: __\_\_init\_\_()__

```python
from abc import ABC, abstractclassmethod

class Persona:
    def __init__(self, nom):
       self.nom = nom
       
    def __str__(self):
        return f'El nom és {self.nom}'


p = Persona('Pere')
print(p)
```

# Sobrecàrrega d'operadors
```python
class Persona:
    def __init__(self, nom):
       self.nom = nom
       
    def __str__(self):
        return f'El nom és {self.nom}'
        
    def __add__(self, other):
        nom = self.nom + ' y ' + other.nom
        return Persona(nom)


p1 = Persona('Pere')
p2 = Persona('carles')

print(p1+p2)
```

# ------------------------------------------------------------------------
# Principis SOLID
# ------------------------------------------------------------------------
Una aplicacií ha de tindre estes característiques.

- __Mantenibilitat__: facilitat de canvi al llarg del temps. L'estructura ha de permetre modificar una part del programa sense que n'afecta a altres.

- __Reusabilitat__: Crear components de codi que es puguen reutilitzar en el mateix i altre projectes.

- __Legibilitat__: El codi ha de ser fàcil d'entendre per a tot desenvolupador que el llisca.

- __Extensibilitat__: Capacitat d'ampliar la funcionalitat sense afectar l'actual.


Tot l'anterior s'aconseguix seguint els principis __SOLID__:

- __SRP__: _Principi de responsabilitat única_:

    Cada classe fa una sola tasca. Si en fan més d'una hem de separar la funcionalitat en diferents classes.


- __OCP__: _Principi obert/tancat_:

    Les classes ha d'estar obertes per a l'extensió però tancades per a la modificació.

- __LSP__: _Principi de substitució de Liskov_:

    Les classe derivades han de poder ser substituides per les classes base.


- __ISP__: _Principi de segregació d'interfície_:
    
    Una classe no ha implementar una interfície en què hi haja mètodes que no pot implementar.


- __DIP__: Principi d'inversió de dependències.


from abc import ABC, abstractclassmethod

class Diccionari:
    def verifica_paraula(self, paraula:str) -> bool:
        pass    # Lògica per a verificar paraula

class CorrectorOrtogràfic:
    def __init__(self) -> None:
        self.diccionari = Diccionari()
    
    def corregix_tex(self, text:str) -> None:
        pass   # Lògica que usa Diccionari() per a corregir un text.

# Problema. El corrector ortogràfic està fortament acoblat a Diccionari el qual és una entitat meys important. Si pel que siga volem canviar de diccionari, el canvi d'un component menor entitat obliga a canviar un component que és de major entitat.

```python
from abc import ABC, abstractclassmethod

class IDiccionari(ABC):
    @abstractclassmethod
    def verifica_paraula(self, paraula:str) -> bool:
        pass

class Diccionari(IDiccionari):
    def verifica_paraula(self, paraula:str) -> bool:
        pass    # Lògica per a verificar paraula
    

class CorrectorOrtogràfic:
    def __init__(self, diccionari:IDiccionari) -> None:
        self.diccionari = diccionari
    
    def corregix_tex(self, text:str) -> None:
        pass   # Lògica que usa un IDiccionariper a corregir un text.
```

















 






















