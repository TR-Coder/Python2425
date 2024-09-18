# ----------
# EXERCICI 1
# ----------
# Introduir una frase i indicar el nombre de lletres majúscules i minúscules.

cadena: str = input('Introduïx una frase: ')
i: int = 0
nombreLletresMajuscula: int = 0
nombreLletresMinuscula: int = 0

# while i < len(cadena):
#     if cadena[i].isalpha():
#         if cadena[i].isupper():
#             nombreLletresMajuscula += 1
#         else:
#             nombreLletresMinuscula += 1
#     i += 1

for caracter in cadena:
    if caracter.isalpha():
        if caracter.isupper():
            nombreLletresMajuscula += 1
        else:
            nombreLletresMinuscula += 1

print(f'Nombre de majúscules: {nombreLletresMajuscula}')
print(f'Nombre de minúscules: {nombreLletresMinuscula}')

# ----------
# EXERCICI 2
# ----------
# Tens un pes màxim que no pots superar.
# S'acaba la introducció de pes amb un 0 o quan s'ha arribat al pes màxim.
# Durant la introducció has d'indicar quant et queda per arribar al pes màxim.
# En acabar el programa has d'indicar el total de pesos que has introduït.

PES_MAXIM: int = 100
suma_total: int = 0
pes: int = 0

while True:
    pes = int(input('Introduïx el pes: '))
    if (pes == 0) or (pes + suma_total == PES_MAXIM):
        suma_total = PES_MAXIM
        break
    elif pes + suma_total > PES_MAXIM:
        print('ERROR: has superat el pes màxim')
        continue
    suma_total += pes
    print(f'Et queden, {PES_MAXIM - suma_total} kg.')

print(f'Has introduït {suma_total} kg.')

# ----------
# EXERCICI 3
# ----------
# Crear un programa que mostre els divisors d'un nombre.
# Nota1: Un nombre és divisible per un altre quan el residu de la seua divisió es 0. a%b==0.
# Nota2: No cal provar tots els nombres entre 1 i el propi nombre ja que els divisors són
# 	sempre menors o iguals que la mitat del nombre (excepte el propi nombre que és divisor d'ell mateix
#   i cal incloure en la llista)
nombre: int = int(input('Introduïx un nombre: '))
print(f'Els divisors de {nombre} són: ', end='')
for i in range(1, 1 + nombre//2):                   # Sumem 1 perquè range no inclou el valor final.
    if nombre % i == 0:
        print(i, end=' ')
print(nombre)

# ----------
# EXERCICI 4
# ----------
# Calcular el factorial d'un nombre. No deixar introduir nombre negatius.
# L'eixida per pantalla ha de tindre la forma: 5! = 5*4*3*2*1 = 120
while True:
    nombre = int(input('Introduïx un nombre: '))
    if nombre >= 0:
        break
    print('Error: el nombre ha de ser positiu')     # Podem millorar el codi amb except ValueError:

factorial = 1
print(f'{nombre}! = ', end='')
for i in range(nombre, 1, -1):
    print(f'{i}*', end='')
    factorial *= i
print(f'1 = {factorial}')

# ----------
# EXERCICI 5
# ----------
# Demanar l'ample d'un triangle i pintar-lo d'esta manera:
# *
# **
# ***
# ****
# ***
# **
# *

ample: int = int(input('Introduïx l\'ample: '))
for i in range(1, ample+1):
    print('*' * i)
for i in range(ample-1, 0, -1):
    print('*'*i)

# ----------
# EXERCICI 6
# ----------
# Demanar l'ample i l'alt d'un rectangle, dibuixar-lo amb esta forma:
# El mínim d'ample i alt és 0
# *****
# *   *
# *   *
# *****

ample_: int = 5
altura: int = 6

if ample_ > 0 and altura > 0:
    asterisc = '*' if ample_ >= 2 else ''

    print('*'*ample_)
    for i in range(altura-2):
        print('*' + ' '*(ample_-2) + asterisc)

    if altura >= 2:
        print('*'*ample_)


# ----------
# EXERCICI 7
# ----------
# Escriure un programa que pinte un triangle amb la següent forma:
# L'altura mínima és zero.
#     *
#    ***
#   *****
#  *******
# *********
# Fórmula progressió aritmètica: an = a1 + (n-1)·d

altura_: int = int(input('Altura del triangle: '))
for n in range(altura_+1):
    asteriscos = 1 + (n-1)*2
    espais = altura_ - n
    print(' ' * espais + '*' * asteriscos)


# -----------
# EXERCICI 8
# -----------
# Barra de progrés
#
import time
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

LONGITUD: int = 20
cadena_: str = '-' * LONGITUD
percentatge: int = 0

print('Iniciant-se procés...')
print(f'{cadena_} ({percentatge}%)')
time.sleep(2)

for i in range(1, LONGITUD+1):
    print(LINE_UP, end=LINE_CLEAR)
    time.sleep(.1)
    percentatge = i * 100 // LONGITUD
    cadena_ = cadena_[:i-1] + '*' + cadena_[i:]
    # cadena = '*' * i + '-' * (LONGITUD-i)
    print(f'{cadena_} ({percentatge}%)')

print('Procés complet!')
