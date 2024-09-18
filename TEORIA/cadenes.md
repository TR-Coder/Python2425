# Cadenes o strings

## Delimitadors
Els strings es delimiten per cometes simples ' ' o dobles " ".


## Concatenar strings amb l'operador + i *
```python
'hola ' + 'i adeu'		# Hola i adeu
'hola ' * 3				# hola hola hola
```


## Cadenes multilínia amb  cometes triples '''
```python
s3 = ''' Això és una cadena
que ocupa tres
línies'''
```

## Cadenes sense processar (rawdata)
```python
s4 = r'abc\n123'  	# abc\n123
```


## Els strings estan indexats
```python
 	 H	 O	 L	 A
 	 0	 1	 2	 3
 	-4	-3	-2	-1
```
```python
s5 = 'hola'		 # s5[0]='H'  s5[-1]='A'
```

## Els string són __immutables__
```python
s5[0] = 'x'					# Error! No podem canviar un string

s5 = s5 + ' i adeu' 		# Correcte ja que s5 + 'i adeu' crea un nou string
```

## Substrings  __[inici, final, increment]__
```python
s6 = '0123456789'

s6[4:]		# 456789        Descarta els 4 primers
s6[:4]		# 0123          Selecciona els 4 primers
s6[1:4]		# 123           Selecciona de la posició 1 a la 4-1
s6[1:8:2]	# 1357          Selecciona de la posició 1 a la 8-1 de 2 en 2
s6[::-1]	# 9876543210    Invertix l'string
s6[-8:-2]	# 234567
s6[-2:]		# 89            Selecciona els 2 últims caràcters
s6[:-2]		# 01234567      Descarta els 2 últims caràcters
```

## Dividir una cadena: __split__
```python
s7 = 'Això és una cadena'
s7.split()					# Retorna un List: ['Això', 'és', 'una', 'cadena']

s8 = '54;34;56;23;53;;34'
s8.split(';')  				# Retorna un List: ['54', '34', '56', '23', '53', '', '34']
```

## Eliminar caràcters inicials i finals: __strip__
```python
s9 = '   usuari   '
s9.strip()					# Esborra espais en blanc inicials i finals

s10 = '***<usuari>***'
s10.strip('*')				# Esborra els * inicials i finals

s11 = 'hola\n'
s11.split('\n')				# Esborra els salts de línia inicials i finals
```


## Busca en cadenes: __startswith__, __endswith__, __find__ i operador __in__
```python
'cad' in 'cadena'			# True

s13 = 'ABCDEF'
s13.startswith('AB')		# True
s13.endswith('EF')			# True

s14 = '---hola----hola---'
s14.find('hola')			# Retorna la posició on comença la 1a ocurrència, -1 si no la troba
s14.count('hola')			# Nombre d'ocurrències, 0 sinó n'hi ha.
```

## Reemplaçament de cadenes: __replace__
replace retorna una 'nova cadena', no modifica l'original.
```python
s15 = 'Això està bé i bé'
s15.replace('bé', 'malament')			# Això està malament i malament.

# Podem indicar el nombre d'ocurrències a canviar:
s15.replace('bé', 'malament', 1)		# Això està malament i bé
```



## Majúscules i minúscules: __capitalize__, __title__, __upper__, __lower__
```python
s16 = 'Antonio José'
s16.capitalize()	# Antonio josé: posa la 1a lletra en majúscula
s16.title()			# Antonio José:	posa en majúscula la 1a lletra de cada paraula
s16.upper()			# ANTONIO JOSÉ:	pasa a majúscules tota la cadena
s16.lower()			# antonio josé:	pasa a minúscules tota la cadena
```

## Identificació de caràcters: __isalnum__, __isnumeric__, __isalpha__, __isupper__, __islower__, __istitle__
```python
'C3-PO'.isalnum()			# False  Tots els caràcters són nombres o lletres?
'314'.isnumeric()    		# True   Tots els caràcters són nombres?
'a-b-c'.isalpha()    		# False  Tots els caràcters són lletres?
'B16'.isupper()				# True   Tots els caràcters són majúscules?
'small'.islower()			# True   Tots els caràcters són minúscules?
'First Heading'.istitle() 	# True	 És la 1a lletra de cada paraula majúscula?
```


## Seqüències d'escape
```python
s17 = ' L \' alumne '
s18 = " L \" alumne "
s19 = a = "hola,\
    què tal?"						# hola,    què tal?
s20 = " això és una barra \\"
s21 = "Salt de \n línia"			# ASCII Linefeed (LF)
s22 = "Retorno de \r carro"			# ASCII Carriage return (CR)
s23 = "tabulacio1 \t tabulació2"	# ASCII Horizontal tab (TAB)
s24 = " \u3245 "					# Unicode expressat en hexadecimal XXXX (16bits) 
s25 = " \U00003245"					# Unicode expressat en hexadecimal XXXXXXXX (32bits) 
```







	