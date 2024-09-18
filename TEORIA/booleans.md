https://www.pythontutorial.net/advanced-python/python-bool/

https://realpython.com/python-or-operator/#using-or-with-boolean-expressions


# BOOLEANS
Per a representar els booleans Python utilitza la classe _bool_ la qual és una subclasse de la classe _int_.
```python
issubclass(bool, int)		# True
```

_True_ i _False_ són objectes de la classe _bool_
```python
isinstance(True, bool)  	# True
```

Com _True_ i _False_ són objectes _int_, els podem convertir a _int_.
```python
int(True)					# 1
```

## Booleans amb expressions
Funcionen segons les taules de veritat:
```python
expr = 7 > 3  				# expr = True
```
## Booleans amb objectes
Tot objecte pot ser avaluat com a True o False. Açò permet que es puguen utlitzar en sentències condicionals (if-else) i en espressions booleanes.

Per defecte, un objecte es considera True a no ser que la seua classe definisca o bé un mètode __bool__() que retorna False o un mètode __len__() que retorna zero quan s'invoque des d'este objecte.

Els objectes predifinits que s'avaluen com False són:
   - None i False
   - zero. En qualsevolt tipus numèric: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
   - qualsevol col·lecció o seqüència buida: '', (), [], {}, set(), range(0)


 El constructor bool() accepta un objecte i retorna True o False.
 Quan passem un objecte al constructor de bool() este retorna el resultat del mètode __bool__() d'eixe objecte. Així bool(200) equival a 200.__bool_()
 Si no existix el mètode __bool__() es retornarà el resultat del mètode __len__(). Si el resultat de __len__() es 0, bool() retorna False, en cas contrari retorna True.
 Esta és la rao per a qual una llista buida retorna False i retorna True si té algun element.



```python
my_list: list = []

#  Este codi:
if my_list is not None and len(my_list) > 0:
    pass

# Equival a:
if my_list:
    pass
```
```python
# Este codi:
object1 and object2

# Equival a:
bool(object1) and bool(object2)
```
## Operador __and__
L'operador _and_ treballa amb curtcircuit. O siga:

* X and Y
	* retorna X si bool(x) és _False_
	* sinó retorna Y.

```python
# Este codi:
c = b and a/b

# Equival a:
if b:
    c = a / b
else:
    c = b

# Per exemple:
a = 10
b = 0
c = b and a/b		# c=0, ja que com b és 0, i bool(0) és False, això fa que no s'avalue a/b i retorne b.
```

```python
condicio = True
condicio and funcio()   #  if condicio:
                        #     funcio()
```

```python
cadena = 'adeu'
resultat = cadena and cadena[0]         # cadena[0] if cadena else ''
```

## Operadors __or__ i __and__
Els operadors 'or' i 'and' treballen amb curtcircuit.
* x or y  :   if x is true, then x, else y
* x and y :   si x is false, then x, else y
* not x   :   si x is false, then True, else False


Generalitzant:
* a or b or c or d retorna el primer operand _True_ que troba.

Podem aprofitat esta característica per assignar a una variable un valor per defecte.

```python
var_name = value or default		# Si bool(value) és False l'operador or retornarà default.
```

```python
# Exemple: este codi demana una entrada per teclat i si nó s'introduïx res a lang se li assignarà 'Python':
lang = input('Enter your language:') or 'Python'
```
```python

# Exemple: suposem esta funció:
def get_data(args=None):
    if args:
        return [1, 2, 3]
    return []

# Si la cridem fent...
lowest = min(get_data(args=True))  		# ...lowest = 1

# Si la cridem fent...
lowest = min(get_data())				# ...dona error, ja que get_data() retorna [] i min([]) provoca un error.

# Ho solucionem fent:
lowest = min(get_data() or [0])  		# ara lowest valdrà 0.
```

```python
# Exemple:
x = a or b or None
# Si 'a' s'avalua a True (o siga no és ni 0 ni None) x valdrà 'a'.
# Si 'a' és 0 o None, s'avalua b, i si b s'avalua a True x valdrà 'b', sinó x valdrà None.
```

## Arguments per defecte mutables !!
Els valors dels arguments predeterminats s'avaluen i es guarden només una vegada, quan s'executa la instrucció def i no cada vegada que es crida a la funció.

```
def mutable_default0(lst=[]):	# Try to use a mutable value as default
    lst.append(1)				# Change same object each time
    print(lst)
```

Solució:
```python
def mutable_default1(lst=None): # Use None as formal default
    lst = lst or []				# Default used? Then lst gets an empty list.
    lst.append(1)
    print(lst)
```
## Prioritat
L'operador not té menys prioritat que els operadors no boolenas.

* not a == b  s'interpreta com  not(a == b)
* a == not b  és un error de sintàxi. Hem d'escriure a == (not b)



# ENCADENAMENT D'OPERADORS DE COMPARACIÓ
Hi ha 8 operadors de comparació que tenen el mateix nivell de prioritat.
Els operadors de comparació tenen més prioritat que els operadors booleans

Els operadors són: <, <=, >, >=, ==, !=, is, is not.


Els operadors de comparació es poden encadenar. S'avaluen d'esquerra a dreta i s'utilitza implícitament l'operador AND.
*   a < b > c   equival a:  (a < b) and (b > c)
*   a < b < c   equival a:  (a < b) and (b < c)
*   a < b == c  equival a:  (a < b) and (b == c)


## OPERADOR == VS is
Els operadors '==' i 'is' tenen diferent propòsit:
* ==  comparara els valors de dos objectes per a comprovar si són iguals.
* is  compara les identitats de dos objectes per a comprovar si són el mateix objecte en memòria.

Si:
a = [1,2,3]
b = [1,2,3]

* a == b  és True perquè les llistes tenen els mateixos valors.
* a is b  és False perquè a i b són objectes diferents en memòria.


En realitat, si comparem dos instancies (amb ==) que no tenen definides el mètode __\__eq__\__() retorna False si no són la mateixa instància (funció id).

Els operadors 'is' i 'is not' verifiquen la identitat de dos objectes usant al funció id(). Estos operadors no es poden personalitar i mai provoquen una exepció.

En general les instàncies d'una classe no es poden ordenar respecte altres instàncies de la mateixa classe.

Si volem fer-ho haurem de definir els criteris d'ordenació amb __\__lt__\__() i __\__eq__\__().