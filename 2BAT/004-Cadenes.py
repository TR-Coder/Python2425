# ----------
# ENUNCIATS
# ----------
# EXERCICI 1: Demanar un nombre i repetir la paraula 'casa' eixe nombre de vegades en diferents línies.

# EXERCICI 2: Demanar el teu nom complet i reescriure'l 3 vegades. La 1a tot en majúscules,
# 	la 2a tot en minúscules i una 3a la 1a lletra de cada paraula està en majúscula.

# EXERCICI 3: Els telèfons d'una empresa tenen el format país-telèfon-extensió, com en: +034-643534992-45
# 	Separar i mostrar per pantalla el país, el telèfon i l'extensió.

# EXERCICI 4: Demanar un frase i un vocal. Substituir en la frase les ocurrències de la vocal en majúscula.

# EXERCICI 5: Demanar un correu (amb @) i substituir el domini per edu.gva.es

# EXERCICI 6: Demanar el preu d'un producte amb 2 decimals i mostre el nombre d'euros i el nombre de centims per separat.

# EXERCICI 7: Demanar la data de naixement en format dd/mm/aaaa i separar els camps per pantalla.
# 	Fer el mateix considerant la possibilitat que el dia i el mes ocupen un sol caràcter.

# EXERCICI 8: Introduix per pantalla una llista de noms separats per coma. Mostra els nom per pantalla cadascun en una línia.


# ----------
# SOLUCIONS
# ----------
# EXERCICI 1
nom1: str = 'casa'
vegades: int = int(input('Digues un enter: '))
print((nom1 + '\n') * vegades)

# EXERCICI 2
nom2: str = input('Introduïx el teu nom complet: ')
print(nom2.lower())
print(nom2.upper())
print(nom2.title())

# EXERCICI 3
telefon: str = input('Introduïx un telèfon amb el format +xxx-yyyyyyyyy-zz')
print(f'El país és {telefon[:4]}, el telèfons és {telefon[5:14]} i l\'extensió {telefon[-2:]}')

# EXERCICI 4
frase: str = input('Introduïx una frase: ')
vocal: str = input('Introduïx una vocal: ')
print(frase.replace(vocal, vocal.upper()))

# EXERCICI 5
correu: str = input('Introduïx el teu correu electrónic: ')
print(correu[:correu.find('@')] + '@edu.gva.es')

# EXERCICI 6
preu: str = input("Introduïx un preu amb 2 decimals:  ")
print(preu[:preu.find('.')], 'euros i', preu[preu.find('.')+1:], 'cèntims.')

# EXERCICI 7
data1 = input("Introduïx la data de naixement amb el format dd/mm/aaaa: ")
print('Día', data1[:2])
print('Mes', data1[3:5])
print('Año', data1[6:])

data2 = input("Introduïx la data de naixement amb el format dd/mm/aaaa: ")
dia = data2[:data2.find('/')]
mesany = data2[data2.find('/')+1:]
mes = mesany[:mesany.find('/')]
any = mesany[mesany.find('/')+1:]
print('Dia', dia)
print('Mes', mes)
print('Any', any)

# EXERCICI 8
# SOLUCIO 1:
noms = input('Introduïx una llista de noms separats per coma: ')
print(noms.replace(',', '\n'))
# SOLUCIÓ 2:
print('\n'.join(noms.split(',')))
