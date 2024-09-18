
# FLOTANTS
Ocupen 64 bits segons l'estànrd IEEE754
```python
a1 = 1.794e10
a2 = 1.123e-12
```


# __trunc__, __round__, __floor__ i __ceil__.

* Les 4 funcions retornen un _int_. Operen tant amb enters com amb flotants.
* Excepte round, s'han d'importar del mòdul _math_.

```python
from math import floor,ceil, trunc
```
* __trunc(x)__\
Elimina la parte decimal (no hi ha cap tipus de redondeig).

* __round(x, n)__ \
Arredonix a l'enter més pròxim. Açò funciona tant per a nombres positius com a negatius. Si s'aplica a enters retorna un int. Si s'aplica a flotants, un float. Per defecte n=0.

* __math.floor(x)__ \
Retorna l'enter més menut que és menor o igual a x.

* __math.ceil(x)__\
Retorna l'enter més menut que és major o igual a x.


```python
int(a) == trunc(a) #  Eliminen la part decimal i retornen la part entera.

# trunc() és més _específica_ per a truncar decimals.
# int() permet també convertir cadenes en enters.
```



# ENTERS
La majoria de llenguatges tenen un nombre fix de bits per a representar un integer. Per exemple, C# utilitza 32 bits per el tipus int i 64 bits per al tipus long. Pre contra, Python utilitza un nombre variable de bits (8, 16, 32, 64, 128...) segons el nombre que emmagatzema. L'enter més gran depen de la memòria disponible. A major longitud major lentitud de càlcul.

Els enters són objectes:
```python
counter = 10
print(type(counter))  # <class 'int'>
```

Per a saber el nombre de bytes que ocupa un enter:
```python
from sys import getsizeof
counter = 0
size = getsizeof(counter)
print(size)  # 24 bytes
```

Quan escrivim un enter podem utilitzar un _ como a separador:
```python
a = 1_000
```

Podem expressar els enters en diferents bases
```python
a = 0b11111     # binari
a = 0o1234      # octat
a = 0xAF42      # hexadecimal
```

* La +, -, * i ** d'enters sempre dóna un enter.
* En canvi, la divisió / de dos enters dóna sempre un flotant, encara que el resultat siga enter.

## Divisió entera

```python
# ATENCIÓ:
a//b = int(a/b) = trunc(a/b)

# 4.1/2=4.01
a = 4.1//2      # 2.0       
b = -4.1//2     # -3.0 

# Donen el mateix ressultat, peró:
#   - La funció int() retorna sempre un int.
#   - L'operador // retorna un int si els dos operands són int. Si algun d'ells és un float retorna un float.

# Si els a i b són enters possitius:
a//b = int(a/b) = math.trunc(a/b) = floor(a/b)

# Però si són enters negatius:
print(floor(3.4), floor(3.9), floor(3))  		# 3   3  3
print(floor(-3.4), floor(-3.9), floor(-3))		# -4 -4 -3

# ATENCIÓ:
# Però si a o b són flotants, a causa de la precissió dels nombres en coma flotant:
floor(a/b) != a//b  
```

## Dividend i residu
En una divisió ( / ) sempre s'ha de complir (tant en nombres positius com negatius) que:
* N  = D * (N//D) + (N%D)
    * Residu = N % D
    * Cocient = N // D

L'operador %, en quant a tipus, es comporta com //. Operar amb enters retorna un enter, però un flotant si algun dels operands en float.

Amb els nombres positius tot és fàcil:
```python
a = 16
b = 5
cocient = a // b  # cocient = 3
residu = a % b 	  # residu = 1      # Es complix que: 5*3+1=16
```

Amb nombre negatius és més laboriós:
```python
a = -16
b = 5
cocient = a // b  # cocient = -4,  ja que -16/5=-3.2 i floor(-3.2)=-4
residu = a % b 	  # residu = 4, ja que -4*5 + residu = -16 --> residu=4
print(cocient, residu)
```


```python
# divmod(x, y) retorna una tupla amb // i %
divmod(10, 3)  #  (3, 1)
divmod(2.6, 0.5) =  (5.0, 0.10000000000000009)
```


