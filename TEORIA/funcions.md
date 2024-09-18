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

* __Mutables__: poden ser modificats una vegada creats. Són: _list, dict, set, classes definides pel programador,  bytearray, memoryview_.
* __Immutables__: no es poden modificar una vegada creats. Són: _bool, int, float, string, tuple, range, complex, byte, frozenset_.

```python
-- EXEMPLES AMB TIPUS IMMUTABLES --
a = 1           # id(a)=9788992.  a és un enter (immutable). Apunta un objecte amb valor 1
a = a + 1       # id(a)=9789024.  a apunta un nou objecte enter amb valor 2

s = 'hola'      # id(s)=41854512. s és un string (immutable). Apunta un objecte amb valor 'hola'
s = 'adeu'      # id(s)=41854576. s apunta un nou string amb valor 'adeu'
s = s + '-siau' # id(s)=41855344. s apunta un nou string amb valor 'adeu-siau'
```

```python
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
Com a mecanisme de seguretat, des de dins d’una funció no podem canviar una variable global. Si volem fer-ho utilitzarem el modificador __global__.

```python
b = 10			# b=10 	id(b)=9789280

def h():
    global b
    b = 5		# b=5 	id(b)=9789120

h()				# b=5 	id(b)=9789120
b = 6			# b=6 	id(b)=9789152
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

