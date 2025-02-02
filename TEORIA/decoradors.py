# ======  DECORADORS ======

# -----------------------------------------------------------------------------------------------------
# El nom d'una funcio és una referència a una funció i podem assignar diversos noms a la mateixa funció:
# -----------------------------------------------------------------------------------------------------
def saluda():
    print('hola')

greet = saluda
greet()


# ---------------------------------------------------
# Podem definir i utilitzar funcions dins de funcions
# ---------------------------------------------------
def externa():
    def interna():
        print('Funció interna')
    interna()
   
externa()


# ---------------------------------------------------
# Podem passar funcions com a paràmentres
# ---------------------------------------------------
def angles():
    print('Hello')

def frances():
    print('Bonjour')


def saluda(idioma):
    idioma()

saluda(angles)
saluda(frances)


# ---------------------------------------------------
# Podem fer un return d'una funció:
# ---------------------------------------------------
def traduix(txt, diccionari):
    diccionari(txt)


def obtin_diccionari(idioma:str):
    def diccionari_frances(txt:str):
        print(f'{txt} en francés')

    def diccionari_angles(txt:str):
        print(f'{txt} en anglés')

    if idioma == 'fr':
        return diccionari_frances
    elif idioma == 'en':
        return diccionari_angles
    else:
        raise Exception('Idioma incorrete')

diccionari = obtin_diccionari('en')
traduix('hola', diccionari)

# -------------------
# Clausures (Closure)
# -------------------
def connecta(url:str):
    def envia(missatge:str):
        print(f'Enviant un "{missatge}" a {url}')
    return envia

envia_missatge = connecta('https:\\servidor.com')
envia_missatge('Hola, salutacions des de la terra')

# ------------------------------------------------------------------------------------------------------------------------------
# Quan creem una funció dins d'una funció, per a la funció interna l'àmbit creat en la funció externa no és 
# és ni àmbit local ni àmbit global, s'anomena àmbit nonlocal.
# Des de la funció interna podem accedir a l'àmbit nonlocal peró per a modificar-la hem de declarar que la variable és nonlocal.
# ------------------------------------------------------------------------------------------------------------------------------
def connecta(url:str):
    comptador = 1
    def envia(missatge:str):
        nonlocal comptador
        print(f'Enviant un "{missatge}" a {url}. (No missatge:{comptador})')
        comptador += 1


    return envia


envia_missatge = connecta('https:\\servidor.com')
envia_missatge('Hola, salutacions des de la terra')
envia_missatge('Us donem la benvinguda')

# ----------------------------------------------------------------------------------------------------
# Suposem que tenim una funciò f() i que no podem/volem modificar-la.
# Un decorador és una funció que permet que permet executar un codi abans i/o després de cridar a f().
# ----------------------------------------------------------------------------------------------------
def externa(func):
    def interna(txt):
        print(f'Abans de cridar a {func.__name__}')
        func(txt)
        print(f'Després de cridar a {func.__name__}')
    return interna

def saluda(nom:str):
    print(f'Hola: {nom}')


saluda('Pere')

decorador = externa(saluda)
decorador('Pere')

# ---------------------------------
# Exemple: Conversor de temperatura
# ---------------------------------
def obtin_temperatura():
    return 50               # Són 50 graus celsiu
    

def conversor_graus(func):
    def calcula(unitats:str='C'):
        graus = func()
        if unitats == 'C':
            return graus
        if unitats == 'F':
            return (graus*9/5) + 32
        if unitats == 'K':
            return graus + 273.15
    return calcula


obtin_temperatura = conversor_graus(obtin_temperatura)

print(obtin_temperatura())
print(obtin_temperatura('K'))
print(obtin_temperatura('F'))

# =============================
# Sintaxi Python d'un decorador
# =============================
def externa(func):
    def interna(txt):
        print(f'Abans de cridar a {func.__name__}')
        func(txt)
        print(f'Després de cridar a {func.__name__}')
    return interna


@externa
def saluda(nom:str):
    print(f'Hola: {nom}')

saluda('Pere')      # Realment estem fent externa(saluda)

# ---------------------------------
# Exemple: Conversor de temperatura
# ---------------------------------
@conversor_graus
def obtin_temperatura():
    return 50               # Són 50 graus celsiu

print(obtin_temperatura('F'))



# ------------------------------------------------
# Exemple: modificar funcions de Python: sin, cos
# -----------------------------------------------
from math import sin, cos, pi

def decorador_angles(func):
    
    def calcular(x, mode='R'):
        if mode == 'G':
            x = x * pi / 180
        return func(x)
    
    return calcular

sin = decorador_angles(sin)
cos = decorador_angles(cos)


r1 = sin(50)
r2 = sin(50,'G')
print(r1, r2)


# ----------------------------------------------------------
# Exemple: Modificar funcions Python random, randint, choice
# ----------------------------------------------------------
# Estes funcions admetens arguments genèrics (*args, **kwargs)

from random import random, randint, choice

def decorador_aleatori(func):
    def calcular(*args, **kwargs):
        print(f'Abans de {func.__name__}')
        res = func(*args, **kwargs)             # No faig el return ara perquè abans he de fer més coses.
        print(f'Després de {func.__name__}')
        return res                              # Faig ara el return amb el valor que m'havia guardat.
    return calcular

random = decorador_aleatori(random)
randint = decorador_aleatori(randint)
choice = decorador_aleatori(choice)

r1 = random()
r2 = randint(10, 20)
r3 = choice([2, 4, 8, 10])

print(r1,r2,r3)



# ----------------------------------------------------------
# Encadenament de decoradors
# ----------------------------------------------------------

def descompte(func): 
    print('********** descompte del 5 %')
    def calcular(valor):
        print('Aplicant un descompte del 5 %')
        aux = func(valor)                               # 3) aux = comprar(1)
        return aux - aux * 0.5                          # 4) return 1-1*0.5 = 0.5
    return calcular
    
def iva(func):  
    print('********** iva del 21%')
    def calcular(valor):
        print('Aplicant un iva del 21 %')
        aux = func(valor)                               # 2) aux = descompte(1)
        return aux + aux * 0.21                         # 5) return 0.5 + 0.5*0.21 = 0.605
    return calcular
    
def taxa(func):             
    print('********** taxa del 10%')                    
    def calcular(valor):
        print('Aplicant una taxa del 10 %')
        aux = func(valor)                               # 1) aux = iva(1)
        return aux + aux * 0.1                          # 6) return 0.605 + 0.605* 0.1 = 0.6655
    return calcular


print('\n-- Generant funcions decoradores --')

@taxa
@iva
@descompte
def comprar(import_):
    return import_                # f = taxa(iva(descompte(comprar)))
                                  # x1 = comprar(1), x2=descompte(x1), x3=iva(x2), x4=taxa(x3)


print("\n -- Els print ixen en ordre invers de l'aplicació del càlcul que s'està aplicant.")
res = comprar(1)                  # f(1) o taxa(1)    
print(res)

# ----------------------------------------------------------
# Utilitzar decoradors per a verificar tipus de dades
# ----------------------------------------------------------

def verificar_enter(func):
    def calcula(n):
        if isinstance(n,int) and n>0:           # Curtcircuit d'operadors. NO és correcte fer l'and al revés: n>0 and isinstance(n,int) 
            return func(n)
        raise ValueError("L'argument ha de ser un enter i positiu")
    return calcula

@verificar_enter
def es_parell(n):
    return n%2 == 0

try:
    print(es_parell('3'))
except ValueError:
    print('Error')


# --------------------------------------------------------------------
# Utilitzar decorador per a comptar el nombre de cridades a una funció
# --------------------------------------------------------------------
# Utilitzem la capatitat de crear directament un atribut sobre qualsevol objecte
def comptador(func):
    def interna(*args, **kwargs):
        interna.cridades += 1
        return func(*args, **kwargs)
    interna.cridades = 0
    return interna

@comptador
def seguent(x):
    return x + 1

print(seguent.cridades)
for i in range(10):
    seguent(i)   
print(seguent.cridades)

# --------------------------------------------------------------------
# Decoradors amb parámetres
# --------------------------------------------------------------------
def descompte(percentatge):
    def externa(func): 
        def calcular(valor):
            aux = func(valor)
            return aux - aux * percentatge/100
        return calcular
    return externa

@descompte(5)               # Crida la funció descompte(5) que retorna externa.
def comprar(import_):       # Ara ja es fa externa(comprar) que retorna calcular.
    return import_

print(comprar(10))



# --------------------------------------------------------------------
# functools import wraps
# --------------------------------------------------------------------
# L'ús d'un decorador té com a efecte secundari que els atributs __name__ (nom de la funció),
# __doc__ (el docstring) y __module__ (el mòdul en què la funció es definix) prenga un valor incorrecte. 
#
# Per exemple:

def externa(func):
    def interna(x):
        """ Comentaris d'interna(x)"""
        print(f"Hola, {func.__name__} retorna:")
        return func(x)
    return interna 

@externa
def f(x):
    """ Comentaris de f(x) """
    return x + 4

f(10)

print("Nom de la funció: " + f.__name__)    # Nom de la funció: interna. Hauria de ser 'f'
print("Docstring: " + f.__doc__)            # Docstring:  Comentaris d'interna(x). Hauria de ser 'Comentaris de f(x)'
print("Nom del mòdul: " + f.__module__)     # Nom del mòdul: __main__. És correcte, però si el decorador estigara definit
                                            # en una altre mòdul seria el nom d'eixe mòdul

# Solució manual:
def externa(func):
    def interna(x):
        """ Comentaris d'interna(x)"""
        print(f"Hola, {func.__name__} retorna:")
        return func(x)
    
    interna.__name__ = func.__name__            # Canviem manualment els atributs
    interna.__doc__ = func.__doc__
    interna.__module__ = func.__module__

    return interna 

@externa
def f(x):
    """ Comentaris de f(x) """
    return x + 4

f(10)

print("Nom de la funció: " + f.__name__)    # Nom de la funció: f
print("Docstring: " + f.__doc__)            # Docstring: Comentaris de f(x)
print("Nom del mòdul: " + f.__module__)     # Nom del mòdul: __main__


# Solució automàtica: utilitzar el decorador wraps de functools.

from functools import wraps

def externa(func):

    @wraps(func)
    def interna(x):
        """ Comentaris d'interna(x)"""
        print(f"Hola, {func.__name__} retorna:")
        return func(x)
    return interna 

@externa
def f(x):
    """ Comentaris de f(x) """
    return x + 4

f(10)

print("Nom de la funció: " + f.__name__)    # Nom de la funció: f
print("Docstring: " + f.__doc__)            # Docstring: Comentaris de f(x)
print("Nom del mòdul: " + f.__module__)     # Nom del mòdul: __main__


# =========================================================
# Decoradors amb classes
# =========================================================
# Es tracta d'usar el mètode __call__ d'una classe.
#  __call__() és un mètode que s'invoca directament sense l'operador punt. Exemple:

class Persona:
    def __init__(self, nom):
        self.nom = nom
    
    def __call__(self):
        print(f'Hola, sóc {self.nom}')


p = Persona('Pere')
p()


# Com a exemple, partirem de la següent funció decoradora:
def descompte(func):
    def calcular(valor):
        aux = func(valor)
        return aux - aux * 0.1
    return calcular

@descompte                  
def comprar(import_):       # descompte(comprar)
    return import_

print(comprar(10))


# Ara, la convertirem en una classe decoradora.
class Descompte:
    def __init__(self, funcio):
        self.funcio = funcio

    def __call__(self, valor):
        print('abans')
        self.funcio(valor)
        print('després')

@Descompte
def comprar(import_):   
    return import_

print(comprar(10))

# El mateix exemple però ara un decorador amb arguments:
class Descompte:
    def __init__(self, percentatge):
        self.percentatge = percentatge

    def __call__(self, func):
        def calcular(valor):
            aux = func(valor)
            return aux - aux * self.percentatge * 0.01
        return calcular

@Descompte(5)
def comprar(import_):
    return import_

print(comprar(10))

#=======================================
# Memoization 
#=======================================
def memoize(f):
    memo = {}
    def helper(*args):
        if args not in memo:            
            memo[args] = f(*args)
        return memo[args]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(40))


























