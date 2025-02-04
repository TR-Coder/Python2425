https://aprendepython.es/core/controlflow/conditionals/#la-sentencia-if


# FUNCIONS

La guia d’estil de Python recomana escriure els noms de les funcions en minúscula separant les paraules amb un guió baix.

No podem utilitzar les funcions abans d'haver-les definit.

## OBJECTES MUTABLES I IMMUTABLES
Python és un lleguatge orientat a objectes. Tots els tipus de dades generen objectes els quals queden definits per un identificador (id), un tipus de dada (type) i un valor.
```python
enter = 10
print(id(enter))    # 9789280	
print(type(enter))  # <class 'int'>
print(enter)        # 10
```

Els objectes poden ser:

* __Mutables__: Poden ser modificats una vegada creats. Són: _list, dict, set, classes definides pel programador,  bytearray, memoryview_. Corresponen als tipus de dades compostos. Quan passem un tipus immutable a una funció, la variable creada fa referència a l'objete original i qualsevol canvi dins de la funció modificarà este objecte original, encara que estiga fora de la funció. Tradicionalment correspon al passe de paràmentres per referència.

* __Immutables__: No es poden modificar una vegada creats. Són: _bool, int, float, string, tuple, range, complex, byte, frozenset_. Si volem modificar el seu contingut s'ha de crear un objecte. Corresponen a tipus de dades bàsics. Quan passem un tipus immutable a una funció es crea variable que és còpia de l'original. Qualsevol canvi es fa sobre la copia de dins de la funció i no afecta a l'objecte original de fora de la funció. Tradicionalment correspon al passe de paràmentres per valor.

```python
-- EXEMPLES AMB TIPUS IMMUTABLES --
a = 1           # id(a)=9788992.  a és un enter (immutable). Apunta un objecte amb valor 1
a = a + 1       # id(a)=9789024.  a apunta un nou objecte enter amb valor 2

s = 'hola'      # id(s)=41854512. s és un string (immutable). Apunta un objecte amb valor 'hola'
s = 'adeu'      # id(s)=41854576. s apunta un nou string amb valor 'adeu'
s = s + '-siau' # id(s)=41855344. s apunta un nou string amb valor 'adeu-siau'
```

```python
-- EXEMPLES AMB TIPUS MUTABLES --
v = [1, 2, 3]
d = { 'un':1,'dos':2 }

				# id(v)=3574016. v és mutable.
v[0] = 999		# v continuarà apuntant a la mateixa llista.
				# id(v)=3574016

				# id(d)=263778432. d és mutable.
d['tres']=3		# d continuarà apuntant al mateix diccionari.
				# id(d)=263778432
```

### Operador is
L’operador d’identitat ___is___ permet comprovar si dos variables fan referència al mateix objecte.
```python
a = 4
b = 4
a is b		# True	id(a)=9789088	id(b)=9789088	id(4)=9789088

b = 5
a is b		# False	id(a)=9789088	id(b)=9789120	id(5)=9789120

v1 = [1,2]
v2 = v1
v1 is v2	# True	id(v1)=61310528	id(v2)=61310528

```

## ÀMBIT LOCAL I GLOBAL DE LES VARIABLES
L’àmbit d’una variable és el context en què esta variable existix. Pot ser _local_ o _global_.

* __Variables locals__
	* Es definixen dins de les funcions i són accessibles només des de la pròpia funció
	* Es creen quan s'invoca la funció i deixen d’existir quan la funció acaba la seua execució.
* __Variables globals__
	* Es definixen en el programa principal, fora de qualsevol funció, i són accessibles des de qualsevol part del programa.

En el següent exemple, utilitzem la variable global ___v___ des de dins de la funció.

```python
v = [1,2]		# v=[1,2] 		id(v)=8600896

def g():
    v[0]=999	# v=[999,2] 	id(v)=8600896

g()				# v=[999,2] 	id(v)=8600896
```

### Variable local amb el mateix nom que una variable global
En el següent exemple, la variable local _d_ tapa la variable global _d_. Són variables distintes.
```python
a = 10			# a=10	id(a)=9789280

def f():
    a = 2		# a=2 	id(a)=9789024

f()				# a=10 	id(a)=9789280
```

### Modificador __global__
__global__ permet treballar directament amb la referència de la variable global dins de la funció, evitant que crear una variable local.

```python
# Amb dades immutables canvie la referència exterta de b
b = 10			# b=10 	id(b)=9789280

def h():
    global b
    b = 5		# b=5 	id(b)=9789120

h()				

print(b)        # id(b)=9789120

```




## PASSE D'ARGUMENTS
Quan cridem a un funció els _arguments_ es copien als corresponents _paràmetres_ de la funció.

En Python quan s’envia una variable com a argument s’envia la referència a l’objecte a què fa referència la variable. Depenent de si l’objecte és mutable o immutable, la funció podrà modificar o no l’objecte.

En el següent exemple la variable _a_ és global i immutable. La funció _f_ no pot canviar la referència cap l’objecte _4_ ni canviar el seu valor. 

```python
b=4			# b=4 id(b)=9789088

def f(x):
    x=7		# x és una variable local

f(b)		# b=4 id(b)=9789088

```

En el següent exemple, les variables _a_ i _b_ són globals i mutables. La funció _f_ no pot modificar la referència de la llista que li passem però si els valors de la pròpia llista. El que és immutable és la referència, no els valors. Que el paràmetre tinga el mateix nom _b_ que una de les llistes globals no afecta en res.

```python
a, b = [1], [2]		# a=[1]		  b=[2]			id(a)=847808  id(b)=223808

def f(b):
    b += [999]  	# No canvia x (és immutable) però si els seus valors.

f(a)				# a=[1, 999]  b=[2]		 	id(a)=847808  id(b)=223808
f(b)				# a=[1, 999]  b=[2, 999]	id(a)=847808  id(b)=223808

```

## Arguments posicionals i nominals
Els arguments poden ser _posicionals_ i _nominals_.
* Els _posicionals_ es copien als corresponents paràmetres per ordre de col·locació.
* Els _nominals_ s’assignen per nom i no han d’estar en ordre.

Si els barregem, els posicionals van primer i, a continuació, els nominals.

## Paràmetres obligatoris i opcionals
En Python els paràmetres poden ser:
* Els _paràmetres obligatoris_ no tenen un valor per defecte i es col·locaran sempre al principi
* Els _paràmetres opcionals_ tenen un valor per defecte que sempre van al final.

En el següent exemple x, y, z son paràmetres obligatoris. Sempre que cridem a la 
funció f se'ls ha de passar arguments, que podran ser posicionals o nominals.
 Per altra banda, a i b són paràmetres opcionals que poden rebre argumemts tant 
posicionals com nominals.
```python
def f(x,y,z, a=1, b='text'):    # x,y,z són obligatoris. a, b opcionals.
    print(x,y,z,a,b)

f(1, 2, 4, 5, 6)    	# 1 2 4 5 6		arguments posicionals
f(1, 2, 4)        		# 1 2 4 1 text	arguments posicionals
f(x=1, y=2, z=4) 		# 1 2 4 1 text	arguments nominals
f(1, 2, z=4)      		# 1 2 4 1 text	arguments posicionals i nominals
f(1, 2, 4, 5, b=6) 		# 1 2 4 5 6		arguments posicionals i nominals
```

En resum:
```python
def f(paràmetres_obligatoris, paràmetres_opcionals):

f(arguments_posicionals, arguments_nominals)
```


## RETORN DE RESULTATS
La sentència __return__ acaba la funció i transferix la seqüència d’execució al punt de cridada.

Les funcions poden retornar un o múltiples valors. En el cas de múltiples valors s’empaqueten tots junts en una n-tupla. La quantitat de variables que reben la tupla ha de coincidir amb el nombre de valors retornats.

```python
def f():
    return 1,2,3
    
x, y, z = f()
(x, y, z) = f()			#  x=1  y=2  z=3
```

## Documentació: docstrings
La documentació se col·loca en la primera línia del codi (funció, mètode, classe, mòdul o paquet) a documentar. Els comentaris es posen entre cometes triples simples o dobles (el més habitual).

```python
def suma(a, b):
"""
Retorna la suma de dos nombres.

Args:
    a: primer nombre a sumar
    b: segon nombre a sumar

Returns:
    retorna la suma de a i b

Raises:
    No llança cap excepció
"""
    return a + b

```

## NOMBRE VARIABLES D'ARGUMENTS
Quan invoquen una funció, Python permet empaquetar i desempaquetar els arguments posicionals i els nominals. Això permet que puguem enviar un nombre d’arguments variable a les funcions.

## Arguments posicionals variables: *args
L’operador * davant un paràmetre __empaqueta__ en una __tupla__ els arguments __posicionals__ rebuts. Per convenció el nom del paràmetre és ___*args___.

El següent exemple suma un nombre variable de valors.
```python
def suma(*args):
    s = 0
    for valor in args:  # args és una tupla
        s+= valor
    return s

suma(4, 3, 2, 1)

```
Quan cridem la funció podem utilitzar l’operador * per a __desempaquetar__ les arguments __posicionals__.

Seguint amb el mateix exemple:

```python
sumands = (1,2,3,4)
suma(*sumands)
```

## Arguments nominals variables: **kargs
L’operador ** davant un paràmetre __empaqueta__ en un __diccionari__ els arguments __nominals__. Per convenció el nom del paràmetre és ___**kargs___.

El següent exemple suma un nombre variable de valors.

```python
def suma(**kargs):
    print(kargs)                		# {'s1':3, 's2':10, 's3':3}
    s = 0
    for clau,valor in kargs.items():	# kargs és un diccionari
        s+= valor
    return s

suma(s1=3, s2=10, s3=3)
```
Quan cridem la funció amb l’operador ** podem __desempaquetar__ els arguments __nominals__.

Seguint amb el mateix exemple:

```python
sumands = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
suma(**sumands)
```

## Arguments posicionals i nominals variables al mateix temps

Dins de la mateixa funció podem barrejar arguments posicionals normals i variables.
```python
def f(a,b,*args):
f(1)    		# Error, b és obligatori
f(1,2)			# 1  2  ()
f(1,2,3)		# 1  2  (3,)
f(1,2,3,4)		# 1  2  (3, 4)

x = [1,2,3,4]	# 1  2  (3, 4)
f(*x)
```

Quan utilitzem *args els arguments que van després s'han de pasar de manera nominal.

```python
def f(a,b,*c,d,e):
f(1,2,3,4,5)    		# 1 2 (3,4,5) ¿? ¿? Error, d i e han de prendre valors nomimalment
f(1,2,3,d=4,e=5)		# 1 2 (3,) 4 5
f(1,2,d=4,e=5)			# 1 2 () 4 5

f(1,2,3,4,5,6,7,8) 		# Error, d i e han de prendre valors nomimalment
f(1,2,3,4,5,6,d=7,e=8)	# 1 2 (3, 4, 5, 6) 7 8

x = [1,2,3,4,5]
f(*d)					# Error, d i e han de prendre valors nomimalment
f(*x,d=-1,e=-2)			# 1 2 (3, 4, 5) -1 -2
```

Quan utilitzem **kargs primer van els arguments posicionals, després el nominals i després el nominals variables.
```python
def f(a,b,**kargs):
f(1,2)					# 1 2 {}
f(1,2,3) 				# Error el 3 s'ha de passar per nom
f(1,2,c=3)				# 1 2 {'c': 3}
f(1,2,c=3, d=4)			# 1 2 {'c': 3, 'd': 4}
f(a=1,2,c=3)  			# Error, primer el posicional i després el nominal
f(1, b=2, c=3, d=4)		# 1 2 {'c': 3, 'd': 4}
f(a=1, b=2, c=3, d=4)	# 1 2 {'c': 3, 'd': 4}
f(d=4, c=3, b=2, a=1)   # En els nominals l'ordre no importa
						# 1 2 {'d': 4, 'c': 3}
```

Quan utilitzem al mateix temps *args i **kargs, **kargs seguirà sempre a *args. L’ordre dels arguments serà el de primer els arguments posicionals i després el nominals.
```python
def f(a,b,*args, **kargs):
    print(a,b,args,kargs)
    
f(1,2)					# 1 2 () {}
f(1,2,3,4)				# 1 2 (3, 4) {}
f(1,2,3,4,c=5)			# 1 2 (3, 4) {'c': 5}
f(1,2,3,4,a=4) 			# error, dos paràmetres amb el mateix nom a.
f(1,b=2,3,4) 			# Error hi ha posicionals després dels nominals,
f(1,b=2,c=3,d=4)			# 1 2 () {'c': 3, 'd': 4}
```

Com hem comentat, si utilitzem *args els arguments que van després s'han de pasar de manera nominal.
```python
def f(a,b,*args,c,**kargs):
    print(a,b,args,c,kargs)
    
f(1,2,3,4) 				# 1 2 (3,4) ¿?Error, faltaria assignar c
f(1,2,3,4,c=5)			# 1 2 (3, 4) 5 {}
f(1,2,3,4,c=5,d=6)		# 1 2 (3, 4) 5 {'d': 6}
```

# Arguments per defecte d'objectes mutables
Els arguments per defecte d'una funció es calculen i assignen només una vegada, en el moment en què es defineix la funció,
no cada vegada que es crida. Això és especialment rellevant quan l'argument per defecte és un objecte mutable com una llista o un diccionari.
Això pot portar a comportaments inesperats si es modifica este valor mutable, ja que el canvi es manté per a totes les cridades futures.
Per exemple: 

```python
def afegir_element(llista=[]):
    llista.append(1)
    return llista

# Crides a la funció:
print(afegir_element())  # [1]
print(afegir_element())  # [1, 1]
print(afegir_element())  # [1, 1, 1]
```

Per evitar este comportament, s'utilitza None com a valor per defecte i crea l'objecte dins de la funció.

```python
def afegir_element(llista=None):
    if llista is None:
        llista = []  # Crear una llista nova
    llista.append(1)
    return llista

# Crides a la funció:
print(afegir_element())     # [1]
print(afegir_element())     # [1]
print(afegir_element([10])) # [10, 1]
```

# Programació funcional
Podem assignar una funció a una variable i usar esta variable com si fóra la pròpia funció.
```python
    a = funcio()
    a()
```

Podem passar una funció a una altra funció.
```python
    def interior():
        print('interior')
    
    def exterior(f):
        f()
    
    exterior(interior)
```

## Funcions lambda
La sintaxi d'una expressió lambda és:
    lambda <parameter_list>: <expression>

Per exemple:
```python

f1 = lambda s: s[::-1]                          # 1 argument
f2 = lambda x1, x2, x3: (x1 + x2 + x3) / 3      # n arguments

animals = ["ferret", "vole", "dog", "gecko"]
res1 = sorted(animals)
res2 = sorted(animals, key=len)
res3 = sorted(animals, key=lambda x: -len(x))

b1 = lambda x: "parell" if x % 2 == 0 else "imparell"
t2 = lambda x: (x, x ** 2, x ** 3)                      # retorna múltiples valors
```

## map()
La sintaxi de la funció map és:
    map(<f>, <iterable>)

map s'aplica sobre un iterable i retorna un iterador. Quan recorrem este iterador
que fa yield al resultat d'aplicar la funció f sobre cada element de l'iterable.
Realment, retorma un map objet el qual és un iterator. Per a obtindre els valots de
l'iterador cal iterar sobre ell o fer un list().

```python
animals = ["cat", "dog", "hedgehog", "gecko"]
it = map(reverse, animals)

for animal in it:
    print(animal)

list(it)      ['tac', 'god', 'gohegdeh', 'okceg']
```

Exemples:

```python
# Quan usem str.join() l'iterable que es concatena ha de ser un string,
# per la qual cosa no podem fer directament un:

"+".join([1, 2, 3, 4, 5])

# Una solució seria:
cadena1 = "+".join(map(str, [1, 2, 3, 4, 5]))

# Encara que correcta, en Python es preferix usar les llistes de compressió:
cadena2 = '+'.join((str(e) for e in [1,2,3,4,5]))
```

```python
def quadrat(n):
    return n*n
    
squared1 = map(quadrat, [1,2,3,4,5])
print(list(squared))

# o
squared2 = map(lambda n: n*n, [1,2,3,4,5])
```

```python
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
```

```python
numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))
float_values = list(map(float, numbers))

words = ["Welcome", "to", "Real", "Python"]
len_values = list(map(len, words))
```


Podem utilitzar map amb múltiples iterabes. Aleshores, la funció de transformació
ha de prendre tants arguments com iterables. Cada iteració de map() passarà un valor
de cada iterable com a argument per a la funció. La iteració s'atura al final de l'iterable més curt.
Exemples:

```python
base = [1, 2, 3]
exponent = [4, 5, 6, 7]
print(list(map(pow, base, exponent)))   # [1, 32, 729]


print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))  # [1, 1, 1]

string_it = ["processing", "strings", "with", "map"]
print(list(map(str.upper, string_it)))                # ['Processing', 'Strings', 'With', 'Map']
```

## Filter
La funció filter() filtra elements d'un iterable segons una funció condicional que retorna True o False.
Només els elements que complixen la condició (per als quals la funció retorna True) es mantenen.

```python
import math

def is_positive(num):
    return num >= 0

numbers = [25, 9, 81, -16, 0]
res = filter(is_positive, numbers)
print(list(res))                    # [25, 9, 81, 0]
```


Podem combinar filter i map:

```python
import math

def is_positive(num):
    return num >= 0

def sanitized_sqrt(numbers):
    cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
    return list(cleaned_iter)

res = sanitized_sqrt([25, 9, 81, -16, 0])
print(list(res))
```

https://realpython.com/python-map-function/#using-map-with-different-kinds-of-functions


# Composició de funcions
Un exemple de composició de dos funcions és g(f(x)). Una manera senzilla d'implementar està composició és:

```python

def f(x):
    return 2*x

def g(x):
    return x+10

def composicio(x):
    return f(g(x))

resultat = composicio(5)
```

Una altra manera, com vorem més versàtil, és definint una funció nova que combina dos o més funcions per crear una funció composta.
```python
def f(x):
    return 2*x

def g(x):
    return x+10

def composicio(g,f):
    def interna(x:int):
        return g(f(x))
    return interna

gf = compile(g,f)
resultat = gf(5)
```

La funció 'composició' que acabem de definir només permet funcions d'un sol argument. La composició de 2 funcions amb múltiples arguments seria:

```python
def doble(a,b) -> float:
    return (a+b)*2

def avalua(x:float) -> str:
    if x>=0:
        return 'positiu'
    return 'negatiu'

def composicio(g,f):
    def interna(*args, **kwargs) -> str:
        return avalua(doble(*args, **kwargs))
    return interna

gf = composicio(avalua, doble)
resultat = gf(1,2)
```

Si volem fer una composició de múltiples funcions podem fer:
```python
def saluda(nom, salutacio='Hola'):
    return f'{salutacio} {nom}', {'modificador':'exclamació'}


def emfasi(text, modificador='emfasi'):
    print('-------',text,  modificador)
    if modificador == 'exclamació':
        print(f'{text}!!!')
    else:
        print(text)


def composicio(*funcions):
    def interna(*args, **kwargs):
        arguments = args if args else ()            # Manté múltiples args en una tupla, però si només n'hi ha un, el tracta com a valor únic.
        kw_arguments = kwargs if kwargs else {}     # Manté els kwargs per transmetre'ls a les funcions següents.
        
        for funcio in reversed(funcions):
            if isinstance(arguments, tuple):                                                               # Si tenim múltiples valors de retorn...
                arguments = funcio(*arguments, **kw_arguments) if arguments else funcio(**kw_arguments)    # ...passem els args i els kwargs.
            else:
                arguments = funcio(arguments, **kw_arguments)
            
            if arguments is None:
                arguments = ()
           
            if isinstance(arguments, tuple) and arguments and isinstance(arguments[-1], dict):  # Si la funció retorna múltiples valors, però alguns són kwargs...
                *arguments, kw_arguments = arguments                                            # ...separa els args dels kwargs retornats.
        
        return arguments if arguments else None         # Si hi ha un únic element, el retorna directament
    
    return interna

gf = composicio(emfasi, saluda)
gf('Pere', salutacio='Hello')

```



```python

```


