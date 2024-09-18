
# ====================
# ENUNCIAT A
# ====================
# Passar de segons a anys, dies, hores, minuts i segons. EXEMPLE:
#
#   300.000 segons són 3 díes, 11 hores, 20 minuts i 0  segons.
#   7.400   segons són 0 díes, 2  hores, 3  minuts i 20 segons.
#
# Assumim anys de 365 dies.



# ====================
# TEORIA
# ====================
# Per a eliminar la part decimal:
#   int(variable)
#   math.trunc(variable)

# No val:
#   print(f'{variable:.0f}) ja que arredonix.



# SOLUCIÓ A1

segons: float = float(input('Introduïx els segons: '))

minuts: float = segons // 60
segons = segons % 60

hores: float = minuts // 60
minuts = minuts % 60

dies: float = hores // 24
hores = hores % 24

anys = dies // 365
dies = dies % 365

print(f'Són {int(anys)} anys, {int(dies)} dies, {int(hores)} hores, {int(minuts)} minuts i {int(segons)} segons')


# SOLUCIÓ A2

segons = float(input('Introduïx els segons: '))

SEGONS_PER_MINUT:int = 60
SEGONS_PER_HORA:int = 60*SEGONS_PER_MINUT
SEGONS_PER_DIA:int = 24*SEGONS_PER_HORA
SEGONS_PER_ANY:int = 365*SEGONS_PER_DIA

anys = segons // SEGONS_PER_ANY
segons %= SEGONS_PER_ANY

dies = segons // SEGONS_PER_DIA
segons %= SEGONS_PER_DIA

hores = segons // SEGONS_PER_HORA
segons %= SEGONS_PER_HORA

minuts = segons // SEGONS_PER_MINUT
segons %= SEGONS_PER_MINUT

print(anys, dies, hores, minuts, segons)



# ====================
# ENUNCIAT B
# ====================
# Ara no assumim anys de 365 dies, poden ser bixestos o no.
# Passar de segons a anys, dies, hores, minuts i segons a partir de l'any 1.970
#
# Nota:
# Un any és bixest si és divisible per 4 i no és divisible per 100.
# Excepció: Tot any divisible per 400 també és bixest.

# Exemple:
# - 2.024 és bixest    perquè és divisible per 4 i no és divisible per 100.
# - 1.900 no és bixest perquè és divisible per 4 i és divisible per 100. Tampoc ho es per 400.
# - 2.000 és bixest    perquè, tot i ser divisible per 4 i divisible per 100 que el faria no bixet, és divisible per 400 que el fa bixest.
# - 200   no és bixest perquè és divisible per 4 i és divisible per 100. Tampoc ho es per 400.


# any_bixest = (any%4 == 0 and any%100 != 0) or (any%400 == 0)
# any bixest té 31.622.400
# any no bixest té 31.536.000

# Any	Segons per any
# 1970	31.536.000
# 1971	31.536.000
# 1972	31.622.400
# 1973	31.536.000
# 1974	31.536.000
# 1975	31.536.000
# 1976	31.622.400
# 1977	31.536.000
# 1978	31.536.000
# 1979	31.536.000
# 1980	31.622.400



segons = 94694401  # 3 anys i 1 segon

ANY_INICIAL = 1970
SEGONS_PER_MINUT = 60
SEGONS_PER_HORA = 60*SEGONS_PER_MINUT
SEGONS_PER_DIA = 24*SEGONS_PER_HORA
SEGONS_PER_ANY = 365*SEGONS_PER_DIA 
SEGONS_PER_ANY_BIXEST = 366*SEGONS_PER_DIA 

any = ANY_INICIAL
while True:
    es_bixest = (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0)
    segons_per_any = SEGONS_PER_ANY_BIXEST if es_bixest else SEGONS_PER_ANY

    if segons < segons_per_any:
        break

    segons -= segons_per_any
    any += 1


anys = any - ANY_INICIAL

dies = segons // SEGONS_PER_DIA
segons %= SEGONS_PER_DIA

hores = segons // SEGONS_PER_HORA
segons %= SEGONS_PER_HORA

minuts = segons // SEGONS_PER_MINUT
segons %= SEGONS_PER_MINUT

print(anys, dies, hores, minuts, segons)