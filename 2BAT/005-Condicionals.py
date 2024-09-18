# --------------
# TEORIA
# --------------
# Tots els objectes són True excepte: None, False i 0 (i altres casos que vorem)
# L'operador AND treballa amb curtcircuit, o siga: X and Y, retorna X si bool(x) és fals, sinó retorna Y.

# Este codi:
# c = b and a/b

# Equival a:
# if b:
#     c = a / b
# else:
#     c = b

# per la qual cosa podem escriure:
a = 10
b = 0
# c=0, ja que com b és 0, i bool(0) és False, això fa que no s'avalue a/b i retorne b.
c = b and a/b
print(c)

# L'operador OR treballa amb curtcircuit, o siga: X or Y, retorna X si bool(x) és veritat, sinó retorna Y
#
# Generalitzant: a or b or c or d retorna el primer operand True que troba.
#
# Podem aprofitat esta característica per assignar a una variable un valor per defecte:
# Si bool(value) és False l'operador or retornarà default.

# var_name = value or default

# Per exemple, este codi demana una entrada per teclat i si nó s'introduïx res a lang se li assignarà 'Python':
lang = input('Enter your language:') or 'Python'

# ================================
# ENUNCIATS
# ================================

# EXERCICI 1
# Introduir la temperatura de l'aigua i indicar si està en estat sòlid, líquid o gasós.
#
# EXERCICI 2
# Demanar un nom d'usuari i verificar si coincidix amb el que teníem guardat en una variable.
# Eliminar els espais en blancs i passar-lo a mínúscules.
#
# EXERCICI 3
# Les notes poden ser:
# 	Un 10 és matricula, igual o superior a 9 sobresalient, igual o superior a 7 notable,
# 	igual o superior a 6 aprovat, menys a 6 suspés.
# 	Cada 4 possitius la nota es puja un punt. Si sobren possitius no es tenen en compte.

# EXERCICI 4
# Hem dividit els alumnes d'una classe en 2 grups. Al grup A pertanyen dones amb un nom
# 	anterior a la M i els homes amb nom posterior a la N. En el grup B la resta.
# 	Demanar el nom i el sexe, i indicar el grup a què pertanyen.
#
# EXERCICI 5
# Demanar les longituts del costats d'un suposat triangle.
# 	- Perquè siga un triangle s'ha de complir que el costat major ha de ser menor que la suma dels altres 2 costats.
# 	- Si és un triangle determinar si és equilater (els 3 costats iguals), isòsceles (2 costats iguals)
#     o escalé (3 costats diferents)
#
# EXERCICI 6
# Tens una pizzeria on pots triar entre pizzes vegetarianes i no vegetarianes.
#  A les vegetarianes els pots afegir entre pebrera o tofu. A les no vegetarianes pernil o salmó.
#  Si l'opció de la pizza o l'ingredient addicional és incorrecte, donar error i acabar el programa.
#
# EXERCICI 7
# Demana un enter de 3 dígits i forma el major nombre possible amb les xifres introduïdes.
# El nombre format ha de tindre el mateix signe que el nombre original.

# EXERCICI 8
# Introduir un data amb el format DDMMYYYY i indicar si és una data vàlida.


# --------------------------
# Esborrar pantalla terminal
# --------------------------
import os

if os.name == 'posix':
    os.system('clear')  # Linux, MacOs
elif os.name == 'nt':
    os.system('cls')  	# Windows


# ----------
# EXERCICI 1
# ----------
temperatura : float = float(input('Introduïx la temperatura: '))
estat : str = ''
if temperatura < 0:
    estat = 'SÒLIDA'
elif temperatura >= 100:
    estat = 'GASOSA'
else:
    estat = 'LÍQUIDA'

print(f"L'estat de l'aigua és {estat}")

# ----------
# EXERCICI 2
# ----------
usuari_guardat : str = 'usuari'
usuari_introduit: str = input('Introduïx l\'usuari: ').strip().lower()

# SOLUCIÓ 1
usuari_es_correcte : bool = (usuari_guardat == usuari_introduit)
if usuari_es_correcte:
    print('Usuari correcte')
else:
    print('Usuari incorrecte')

# SOLUCIÓ 2
missatge : str = 'Usuari correcte' if (usuari_guardat == usuari_introduit) else 'Usuari incorrecte'
print(missatge)

# ----------
# EXERCICI 3
# ----------
nota : float = float(input('Nota: '))
possitius : int = int(input('Possitius: '))
qualificacio : str = ''

nota = nota + possitius % 4

if (nota == 10):
    qualificacio = 'una matrícula'
elif (nota >= 9):
    qualificacio = 'un sobresalient'
elif (nota >= 7):
    qualificacio = 'un notable'
elif (nota >= 6):
    qualificacio = 'un aprovat'
else:
    qualificacio = 'un suspés'

print(f'Has tret {qualificacio}')

# ----------
# EXERCICI 4
# ----------
grup: str = ''
nom: str = input('Digues el teu nom: ')
sexe : str = input('Indica el teu sexe (H/D): ')
if (sexe == 'D' and nom.lower() < 'm') or (sexe == "H" and nom.lower() > 'n'):
    grup = 'A'
else:
    grup = 'B'

# ----------
# EXERCICI 5
# ----------
# Demanar les longituts del costats d'un suposat triangle.
# - Perquè siga un triangle s'ha de complir que el costat major ha de ser menor que la suma dels altres 2 costats.
# - Si és un triangle determinar si és equilater (els 3 costats iguals), isòsceles (2 costats iguals)
#   o escalé (3 costats diferents)


costat1: float = float(input('Costat 1: '))
costat2: float = float(input('Costat 2: '))
costat3: float = float(input('Costat 3: '))

costat_major : float = costat1

if costat2 > costat_major:
    costat_major = costat2
if costat3 > costat_major:
    costat_major = costat3

suma_costats_menors: float = costat1 + costat2 + costat3 - costat_major

if costat_major >= suma_costats_menors:
    print('No és un triangle')
    exit()

if costat1 == costat2 == costat3:
    print('Triangle equilàter')
elif (costat1 == costat2) or (costat1 == costat3) or (costat2 == costat3):
    print('Triangle isòsceles')
else:
    print('Triangle escalè')

# ----------
# EXERCICI 6
# ----------
ingredient_addicional: str = 'ERROR'
opcio_ingredient_addicional: str = ''
tipus_pizza: str = ''

print('-- MENÚ --')
print('Indica el tipus de pizza:')
print(' 1- Vegerariana')
print(' 0- No vegetariana')
print('\nTotes les pizzes tenen mozarrella i tomata')

opcioPizza: str = input('Tipus de pizza? ')

if opcioPizza != '0' and opcioPizza != '1':
    print('Tipus de pizza incorrecta')
    exit()

if opcioPizza == '1':
    print(' 1- Pebrera')
    print(' 2- Tofu')

    tipus_pizza = 'vegetariana'
    opcio_ingredient_addicional = input('Indica l\'ingredient addicional: ')

    if opcio_ingredient_addicional == '1':
        ingredient_addicional = 'Pebrera: '
    elif opcio_ingredient_addicional == '2':
        ingredient_addicional = 'Tofu'
    else:
        print('Ingredient addicional incorrecte \n')
        exit()

elif opcioPizza == '0':
    print(' 1- Pernil')
    print(' 2- Salmó')
    
    tipus_pizza = 'no vegetariana'
    opcio_ingredient_addicional = input('Indica l\'ingredient addicional: ')

    if opcio_ingredient_addicional == '1':
        ingredient_addicional = 'Pernil: '
    elif opcio_ingredient_addicional == '2':
        ingredient_addicional = 'Salmó'
    else:
        print('Ingredient addicional incorrecte! \n')
        exit()

print(f'Has triat una pizza {tipus_pizza} amb {ingredient_addicional}')

# ----------
# EXERCICI 7
# ----------
nombre: int = int(input('Introduïx un nombre: '))

if nombre > 999 or nombre < -999 or (nombre > -100 and nombre < 100):
    print('Error: el nombre no té 3 xifres')
    exit()


es_negatiu: bool = nombre < 0

if es_negatiu:
    nombre *= -1

centenes: int = nombre // 100
desenes: int = (nombre % 100) // 10
unitats: int = (nombre % 100) % 10

xifra_menor: int = centenes
if desenes < xifra_menor:
    xifra_menor = desenes
if unitats < xifra_menor:
    xifra_menor = unitats

xifra_major: int = centenes
if desenes > xifra_major:
    xifra_major = desenes
if unitats > xifra_major:
    xifra_major = unitats

xifra_enmmig: int = centenes + desenes + unitats - xifra_major - xifra_menor
nombre_mes_gran_possible = xifra_major*100 + xifra_enmmig*10 + xifra_menor

if es_negatiu:
    nombre_mes_gran_possible *= -1

print(f'El nombre més gran possible és {nombre_mes_gran_possible}')

# ----------
# EXERCICI 8
# ----------
GENER: int = 1
FEBRER: int = 2
DESEMBRE: int = 12

data: str = input('introduïx una data (DDMMAA) ')

# extraure dia mes i any de data
dia: int = int(data[:2])
mes: int = int(data[2:4])
any: int = int(data[-2:])

if (mes < 1) or (mes > 12):
    print('ERROR: mes incorrecte\n')
    exit()

# El mesos tenen 30 o 31 dies. Febrer en té 28 excepte els anys bixestos que en tenen 29.
es_un_mes_de_30: bool = (mes == 4) or (mes == 6) or (
    mes == 7) or (mes == 9) or (mes == 11)
es_un_any_bixest: bool = (any % 4 == 0)  # Els anys bixestos són múltiples de 4

# if es_un_mes_de_30:
#     ultim_dia_del_mes = 30
# elif mes == FEBRER:
#     ultim_dia_del_mes = 29 if es_un_any_bixest else 28
# else:
#     ultim_dia_del_mes = 31

ultim_dia_del_mes: int = 30 if es_un_mes_de_30 else 29 if mes == FEBRER and es_un_any_bixest else 28 if mes == FEBRER and not es_un_any_bixest else 31

if (dia < 1) or (dia > ultim_dia_del_mes):
    print("ERROR: dia incorrecte")
    exit()

print(f'La data {dia:02}/{mes:02}/{any:02} és correcta')
