
# EXCEPCIONS

Llista d'excepcions predefinides en Python: https://docs.python.org/3/library/exceptions.html#concrete-exceptions

Jerarquia de la classe Exception en Python: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

## Llançar excepcions: raise i assert

La classe Exception permet manejar errors que es poden preveure durant l'execució d'un programa. Amb els blocs try..except podem capturar una excepció per a manejar-la de manera controlada i evitar així que el programa es detinga abruptament.


```python
x = 6
if x > 5:
    raise Exception('x és major que 5')			# Exception: x és major que 5
```
Una cas particular d'Exception és AssertionError. Les declaracions assert s'utilitzen per a depuració i proves. Si la condició de l'assert és False es llança una AssertionError i el programa es deté. Com AssertionError és una subclasse d'Exception la podríem capturar en try..except.

Per desactivar els assert hem d'executar Pyhton amb l'opció -O(optimize):
```python
python -O mi_script.py
```
__assert__: L'execució del programa pot continuar si la condició és True sinó es genera un AssertionError
```python
assert x <= 5, 'La condició es False'			# AssertionError: La condició és False
```


El mètode \_\_init\_\_() d'Exception accepta arguments *args, el que implica que podem passar-li qualsevol nombre d'arguments. Excepction té l'atribut args, el qual és una tupla amb les arguments que hem passat al
constructor de l'excepció.

Si assignem l'excepció a una variable podrem recuperar-los amb .args:

```python		
try:
    raise ValueError('The value error exception', 1, 2.0)
except ValueError as ex:
    a,b,c = ex.args             # 'The value error exception', 1, 2.0
```

Si volem imprimir directament tots els arguments podem fer:
print(ex.args), o directament print(ex) ja que el __str__() de les excepcions està definit així.

##  Excepcions personalitzades
Per a crear una excepció personalitzada deriven d'Exception. També podem passar-li qualsevol nombre d'arguments.

```python
class ExcepcioPersonalitzada(Exception):
    pass

raise ExcepcioPersonalitzada()

```

Si en la instància de l'excepció definim el mètode \_\_str\_\_() podrem imprimir directament l'error sense haver de fer referència a _.args_

```python
class FileExtensionError(Exception):
    def __init__(self, filename, desired_ext):
        self.filename = filename
        self.desired_ext = desired_ext

    def __str__(self):
        return f"File {self.filename} should have the extension: {self.desired_ext}."

try:
    raise FileExtensionError("test.xls", "csv")
except FileExtensionError as ex:
    print(ex.filename, ex.desired_ext)      # File test.xls should have the extension: csv.
    print(ex)                               # Sense args.
```

##  try...except
Hem d'evitar un _except generic_ ja que captura totes les excepcions i les oculta. No codificar mai alguna cosa com:
```python
try:
    print('Codi')
except:             # HORROR, TERROR I PAVOR!
    pass
```

Dins del bloc _try_, l'execució continua fins trobar la primera excepció.
Podem capturar múltiples excepcions i tractar-les específicament.
```python
try:
    print('codi')
except FileNotFoundError as error:
    print(error)
except AssertionError as error:
    print(error)
except NameError:
    print("NameError occurred. Some variable isn't defined")
except:
    print('ERROR INESPERAT')
    exit()
```

Si volem capturar una excepció inesperada, enlloc d'un simple "except :" possarem un "except Exception as err:".
Normalment per a gestionar este Exception s'imprimix o registra l'excepció i es rellança per a permetre que qui crida la funció puga manejar-la.
Exemple:
```python
try:
    pass
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

El patrón más común para gestionar Exception es imprimir o registrar la excepción y luego volver a re-lanzarla (permitiendo a un llamador manejar la excepción también):


Podem capturar més d'una excepció en la mateixa clausula except (Només pot hi haver una excepció activa.). Hem de posar les possibles excepcions en una tupla. 
```python
number = 0
try:
    formatted_number = int(number)
    result = 6/formatted_number
except (ValueError, ZeroDivisionError) as e:
    print(f"Error {type(e)}: {e}")
```

## Maneig d'Excepcions de funcions cridades des d'un try

Les excepcions no només es manegen si es produixen immediatament dins de la clàusula try, sinó també si es produixen dins de funcions que són cridades (fins i tot indirectament) dins de la clàusula try.

```python
def f(i):
    try:
        g(i)
    except IndexError:
        print("Please enter a valid index")


def g(i):
    a = "Hello"
    return a[i]


f(50)			# Please enter a valid index
```

##  try...except...else...finally
Si dins del bloc _try_ no es poduïx cap excepció entrarem dins de l'_else_.
Dins del bloc de l'_else_ podem utilitzar també altres try...except

El codi del _finally_ sempre s'executarà, independement de si han hagut errors o no. Este codi podrà fer tasques de neteja o alliberament de recursos.

L'ús de la clàusula else és millor que afegir codi addicional a la clàusula try perquè evita detectar accidentalment una excepció que no s'ha generat
pel codi protegit per la instrucció try... except.

_else_ i _finally_ són opcionals. Si s'utilitzen les dos finally ha de ser sempre l'última clausula.

```python
try:
    print('codi')
except AssertionError as error:
    print(error)
else:
    print('Cap error error en try, el codi continua ací')
finally:
    print('Cleaning up, irrespective of any exceptions.')
```

## Rellançar una excepció

 Es ocasions, volem logejar una excepció i tornar a llançar-la de nou. Ho farem amb simple __raise__.

No hem d'especificar cap objecte Exception() després de raise, Pyhton ja sap que es tracta de la mateixa excepció que ha sigut capturada per la clausula except.
```python
a = b = 0
try:
    a / b
except ZeroDivisionError as ex:
    print('Logging exception:', str(ex))
    raise ex                                # posar 'ex' mostra la pila de cridades (traceback).
```

Podem llançar un altre tipus d'excepció durant el maneig d'una excepció.
```python
try:
    a / b
except ZeroDivisionError as ex:
    raise ValueError('b must not zero')
```


# Mòdul looging

```python
import logging
import logging.config
```

Hi ha 5 nivells d'entrades en el log. De menor a major grau de severitat són: DEBUG, INFO, WARNING. ERROR i CRITICAL

```python
import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

El codi anterior genera per pantalla el següents avisos. Observem que _debug()_ i _Info()_ no generen missatges:
* WARNING:root:This is a warning message
* ERROR:root:This is an error message
* CRITICAL:root:This is a critical message

El mètode __logging.basicConfig()__ permet configurar les entrades del log a través dels arguments que li passem. La llista completa de paràmentres està en: https: // docs.python.org/3/library/logging.html.

Els més comuns són:
* __level__: Indica el nivell de severitat a partir del qual es genererarà una entrada de log, els inferiors s'ignoren.
* __filename__ i __filemode__: Permeten rederigir l'eixida de la consola cap un arxiu. Si filemode val 'w' (mode d'escriptura), cada vegada
 	  que es crida a basicConfig() i en cada execució del programa se reescriurà de nou l'arxiu. El valor per defecte val 'a' (append)
*  __format__: Format dels missatges de log.


Només podrem cridar una vegada a __basicConfig()__. Els mètodes _debug()_, _info()_, _warning()_, _error()_ i _critical()_ criden internament a __basicConfig()__ sense arguments (si no l'hem cridat prèviament), per tant si volen configurar el log ha de ser abans de cridar estos mètodes.

Per defecte __basicConfig()__ està configurat a escriure per la consola i amb el següent format:

 	ERROR:root:This is an error message

### EXEMPLES:
```python
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')			# 18472-WARNING-This is a Warning

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')					# 2018-07-11 20:12:06,288 - Admin logged in

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')				# 12-Jul-18 20:53:19 - Admin logged out
```

## Captura de la traça de la pila amb logging.exception()
En cas d'una excepció podem capturar la traça de la pila amb el paràmetre exc_info=True

Podem substituir un logging.error(exc_info=True) per un logging.exception()

```python
try:
    c = 5 / 0
except Exception as e:
    logging.exception("Exception occurred")
```

Generarà:

        ERROR:root:Exception occurred
        Traceback (most recent call last):
        File "exceptions.py", line 6, in <module>
            c = a / b
        ZeroDivisionError: division by zero
        [Finished in 0.2s]


Analitzem la traça de cridades de l'exepció del següent programa:

```python
1 def func1():
2    raise ValueError("Error original en func1")
3
4 def func2():
5    try:
6        func1()
7    except ValueError as e:
8        e.add_note("S'ha produït un error durant l'execució de func2") # add_note() afegix informació a una excepció.
9        raise e
10 func2()
```

L'error generat és:

    ERROR!
    Traceback (most recent call last):
    File "<main.py>", line 10, in <module>
    File "<main.py>", line 9, in func2                      <- Apareix perquè hem posat "raise e"
    File "<main.py>", line 6, in func2
    File "<main.py>", line 2, in func1
    ValueError: Error original en func1
    S'ha produït un error durant l'execució de func2.       <- add_note()



# import traceback

try:
    func2()
except Exception as e:
    print(e.__traceback__)
    import traceback
    traceback.print_exception(type(e), e, e.__traceback__)

https://www.qodo.ai/blog/6-best-practices-for-python-exception-handling/
https://docs.python.org/3/reference/simple_stmts.html#raise
https://realpython.com/python-lbyl-vs-eafp/
https://realpython.com/python-raise-exception/




