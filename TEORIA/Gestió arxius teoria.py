from pickle import Unpickler
from pickle import Pickler
import pickle, os, sys
#
# font:
# https://realpython.com/read-write-files-python/


# Per a saber el nombre de bytes que ocupa un objecte utilizem sys.getsizeof(objecte)
c1 = 'hola'
print(sys.getsizeof(c1))

# =========================================================================================================================
# bytes i arraybytes
# =========================================================================================================================
# En Python els strings internament sempre estan codificats en UTF-8, independentment de com estos es mostren per pantalla.

obj1 = 'hola ñ'
# obj2 = b'hola ñ'		 # Error només són vàlids caràcters ASCII
obj2 = b'hola \xC3\xB1'  # La ñ en utf-8 és l'hexadecimal C3 B1

# obj1 és un objecte de <class 'str'> que guarda elements que representen caràcters en UTF-8.
# obj2 és de <class 'bytes'> i guarda elements que són bytes.
# Una b en un f-string indica que estem creant un objecte bytes a partir dels codis utf-8 de la cadena.

# Si transformen obj1 i obj2 en un list veem que els caràcter ASCII ocupen un byte mentres que la ñ n'ocupa dos.
list(obj1)  # ['h', 'o', 'l', 'a', ' ', 'ñ'     ]
list(obj2)  # [104, 111, 108, 97,  32,  195, 177]

# Quan llegim/escrivim en un arxiu sempre estem llegint/escrivint una seqüència de bytes.
# Si llegim l’arxiu en mode text, la seqüència de bytes s’ha de descodificar (decoding), és a dir, transformar els bytes en un string seguint una codificació de caràcters determinada, la qual depén de la codificació que utilitza el sistema operatiu.
# De manera anàloga, quan escrivim l’arxiu s’ha de codificar (encoding), és a dir, transformar un string en una seqüència de bytes.
# Se considera una bona pràctica especificar sempre la codificació de caràcters per evitar-nos problemes com quan escrivim en un sistema operatiu i llegim en un altre.

# Per a convertir un objecte de bytes en un strings utilitzem el mètode decode(). Per defecte és utf-8, però com hem dit és preferible especificar sempre la codificació.

data = b"bytes! \xe2\x9c\xa8"   # data és una seqüència de bytes
text1 = data.decode("utf-8")		# convertix de nou els bytes de data en un str codificat en UTF-8: 'bytes! ✨'
# En un únic pas seria:
text2 = b"bytes! \xe2\x9c\xa8".decode('UTF-8')      # text1==text2 és True

# De manera similar, convertim un objetec string en un objecte de bytes amb el mètode encode. Com abans és utf-8 per defecte.
text = 'bytes! ✨'
databytes = text.encode("utf-8")			# és igual a haver fet:   databytes = b'bytes! \xe2\x9c\xa8'

# Un bytearray és una seqüència 'mutable' de bytes (enters en 0 i 255). La diferencia entre bytes i bytearray es que byte és inmutable.
# El creem amb el constructor bytearray(source, encoding, errors)
# Si source és un string, se'l recorre i per cada caràcter fa un str.encode() per a convertir-lo a byte.abs(x)
str = "Prova"
array1 = bytearray(str, 'utf-8')
array2 = bytearray(str, 'utf-16')
print(array1)						# bytearray(b'Prova')
print(array2)						# bytearray(b'\xff\xfeP\x00r\x00o\x00v\x00a\x00')

# Si source és un enter es crea un bytearray de source longitud amb valors null bytes.
size = 3
array1 = bytearray(size)
print(array1)				# bytearray(b'\x00\x00\x00')

# Podem passar un iterable.
list = [1, 2, 3, 4]
array = bytearray(list)
print(array)				# bytearray(b'\x01\x02\x03\x04')

# ----------------------------------------------------------------------------------------------------------
# Definició d'arxiu
# ----------------------------------------------------------------------------------------------------------
# Un arxiu és una sequència de bytes que guarden una informació o el codi d'un programa.
# Les dades d'un arxius s'organitzen en diferents formats, cada format s'identifica per una extensió.
# En general un arxiu es dividix en tres parts:
# - La capçalera (metadades sobre el propi arxiu)
# - dades
# - caràcter especial EOF (End Of File).
#
# ----------------------------------------------------------------------------------------------------------
# Final de línia
# ----------------------------------------------------------------------------------------------------------
# Per a marcar el final de línia tenim els caracteres de retorn de carro (CR o \r) i d'alimentació de línia (LF o \n)
#  - Windows utilitza la combinació CR+LF (o \r\n)
#  - Unix i MacOs només LF (\n)

# ---------------------------------------------------------------------------------------------
#  Obrir i tancar arxius
# ---------------------------------------------------------------------------------------------
# Per a obrir un arxiu utilitzem open(). Els arxius es poden obrir a diferents propòsits (lectura,escriptura, afegir),
# a més hem d'indicar si l'obrir com un arxiu de text o binari:
#
# filename = 'C:/ThisFolder/workData.txt'	# utilitzem /, també podem \\, però no \, que és un 'string literal'.
# file_object = open(filename, mode)
# ...
# file_object.close()

# Modes d'apertura d'arxius de text:
#
# 		Read	Writer	Creates	Remove	Initial
#						file 	file 	position
# 		-----------------------------------------
# 	r	  x								  inici (default)   
# 	r+	  x		  x						  inici             
# 	w	  		  x		   x	  x		  inici
# 	w+	  x		  x		   x	  x		  inici
# 	a	  		  x		   x 			  final # afegir al final sense esborrar l'arxiu
# 	a+	  x		  x	       x			  final
# 	x			  x		   x 			  inici # obrir arxiu creant-lo. Si ja existix falla.
# 	x+	  x	 	  x		   x 			  inici
#
# Create file: 'X' indica que si l'arxiu no existix es crea. ' ' indica que si no existix es llança una excepció.
# Remove file: 'X' indica que s'esborra el contingut de l'arxiu. ' '  que no s'esborra.
# El símbol + indica 'update'. S'actualitza a partir de la posició de l'arxiu.
# Els arxius binaris tenen els mateixos modes. S'identifiquen amb una 'b': rb, rb+, wb, wb+, ab, ab+, xb i xb+.

# r+ permet llegir i escriure en qualsevol posició de l'arxiu. Ens posicionem en la posició que volem amb seek(posició).
#    Inicialment el posicionament és a l'inici de l'arxiu.
#    Podem per exemple llegir uns bytes, actulizar uns altres i tornar a llegir uns altres. Per a fer-ho
#    utilitzem read(n) per allegir n bytes des de la posició actual (el curso avançara després de la lectura),
#    ara podem escriure un bytes amb write(dades), les dades existens seran sobreesctites a partir de la posició del cursor,
#    ara podem llegir novament amb read(n).
#   Nota: si actualitzem dades sense volcar-les al disc, si ens posicionem per a llegir les dades que
#    hem actualitzat llegirem les dades antigues. O siga, la lectura sense volcar a disc llig les dades originals.

# w obri l'arxiu només a per a escritura. L'arxiu, si existix es trunca (o siga, s'esborra),
#   sinó existix es crea. El cursor se situa a l'inici de l'arxiu.
#
# w+ Fa igual que w però, a més. permet també la lectura.
#    Es diferencia amb r+ en que r+ no esborra l'arxiu existent i w+ si que l'esborra.
#    Si per exemple vull afegir al final de l'arxiu farà seek(0,2) i faré write(dades),
#    si volem sobreescriure a partir de qualsevol posició en situem a seek(posició) i utilitzem writer(dades)
#    Si el que volem és inserir podem fer:
#    Suposem un arxiu.txt amb el contingut: "Aixo es un exemple d'arxiu" i fem:
with open("arxiu.txt", "r+") as f:
    dades_originals = f.read(11)            # Llig els 11 primers bytes ('Aixo es un ')
    f.seek(10)                              # Moure el cursor a la posició 11, després de dades_originals
    dades_restants = f.read()
    f.seek(10)
    dades_noves = "noves dades a inserir"
    f.write(dades_noves)
    f.write(dades_restants)
#   L'arxiu contindrà 'Aixo es un noves dades a inserir exemple d'arxiu'
#
# La millor manera de treballar amb arxius és amb el 'with':
with open("workData.txt", "r+") as workData:
    workData.read()
#
# -------------------------------------------------------------------------------------------
#  Lectura de dades amb .read()
# -------------------------------------------------------------------------------------------
#  file_object.read() llig l'arxiu complet (a partir del punter actual)
#  file_object.read(size) llig size bytes cada vegada que l'executem. (a partir del punter actual)
#		Si size excedix l'arxiu torna fins el final de l'arxiu.

with open('workData.txt', 'r+', encoding='utf-8') as work_data:
    print("El nom de l'arxiu és: ", work_data.name)
    line = work_data.read()
    print(line)

# Exemple de lectura d'un arxiu binari png. Llegim els primer bytes de la capçalera:
with open('jack_russell.png', 'rb') as byte_reader:
    print(byte_reader.read(1))
    print(byte_reader.read(3))
    print(byte_reader.read(2))
    print(byte_reader.read(1))
    print(byte_reader.read(1))

# -------------------------------------------------------------------------------------------
# Lectura d'arxiu de text per línia amb readline(size)
# -------------------------------------------------------------------------------------------
# La lectura per línia només aplica a arxius de text.
# file_object.readline() retorna una línia cada vegada.
with open("workData.txt", "r+") as work_data:
    line_data = work_data.readline()
    print(line_data)

# Si indiquem size retorna size "caracters" a partir de la posición actual. No va més enllà de la línia.
# fileobject.readlines() retorna un List amb totes les línies de l'arxiu.
with open("workData.txt", "r+") as work_data:
    for line in work_data.readlines():
        print(line, end='')  			# lleven el \n per què ja el porte l'arxiu

# -------------------------------------------------------------------------------------------
# Escriptura d'arxius de text amb .write() and .writelines()
# -------------------------------------------------------------------------------------------
# He de convertir a String tot allò que vullguem gravar:
values = [1234, 5678, 9012]

with open("workData.txt", "a+") as work_data:
    for v in values:
        str_value = str(v)
        work_data.write(str_value)
        work_data.write("\n")					# Hem d'inserir manualment el \n
    # o també:
    # work_data.write('\n'.join(str_value))

# writelines() es recorre un iterable i inserix cada element en l'arxiu.
# No inserix \n entre linia i linia, tot és un bloc.
lines = ['Readme\n', 'How to write text files in Python\n']
with open('readme.txt', 'w') as f:
    f.writelines(lines)

# -------------------------------------------------------------------------------------------
# Moure el puntes de l'arxiu amb .seek()
# -------------------------------------------------------------------------------------------
# Per a moure el punter de l'arxiu utilitem file_object.seek(offset, posicio_inicial).
# Col·loca el punter 'offset' bytes a partir de 'posicio_inicial', on 'posicio_inicial' pot ser:
#	0 - Inici de l'arxiu (valor per defecte)
# 	1 - Posició actual (només servix per arxius binaris, en arxius de text dona una resultat indefinit)
# 	2 - Final de l'arxiu
# 
# file.seek(0)   col·loca el punter a l'inici.
# file.seek(0,2) col·loca el punter al final.
# file.seek(x,1) només en axius binaris. En arxius de text dona error.
#
# La primera posició de l'arxiu és 0, així seek(3,0) col·loca el punter en el 4a byte.
#
# Per a saber la posició actual del punter fem:
# file_object.tell()
#


# -------------------------------------------------------------------------------------------
# Editar arxius de text
# -------------------------------------------------------------------------------------------
# Si volem inserir/modificar en arxius de text el millor en llegir-lo tot volcant-lo en un List,
# afegir el que siga amb list.insert(), unir tot el text i gravar-lo.

with open("workData.txt", "r") as work_data:		# Open the file as read-only
    llista = work_data.readlines()

llista.insert(1, "This goes between line 1 and 2\n")

with open("workData.txt", "w") as work_data:		# Re-open in write-only format to overwrite old file
    text_complet = "".join(llista)
    work_data.write(text_complet)

# -------------------------------------------------------------------------------------------
# Consells
# -------------------------------------------------------------------------------------------
# __file__
# Este atribut retorna la ruta relativa a on es va cridar l'script Python.
# Si necessitem la ruta completa utilitzarem os.getcwd() per obtenir el directori de treball actual.
#
# Per afefir al final d'un arxiu amb dades utilizem el mode a.
with open('dog_breeds.txt', 'a') as a_writer:
    # NOTA: posar \nBeagle o Beagle\n depen si el final de l'arxiu l'hem acabat amb \n
    a_writer.write('\nBeagle')

#  Per a llegir d'un arxiu i escriu en un altre al mateix temps:
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))

# -------------------------------------------------------------------------------------------
# manejadors de context personalitzats
# -------------------------------------------------------------------------------------------
# Un plantilla per a crear els nostres manejadors de context personalitzats:


class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    # Additional methods implemented below


# L'utilitzarem d'esta manera:
with my_file_reader('dog_breeds.txt') as reader:
    # Perform custom class operations
    pass
# -------------------------------------------------------------------------------------------
# Un exemple de com obrir un arxiu .png
# -------------------------------------------------------------------------------------------


class PngReader():
    # Els arxius .png s'identifiquem amb esta capçalera.
    _expected_header = b'\x89PNG\r\n\x1a\n'

    def __init__(self, file_path):
        if not file_path.endswith('.png'): 		# Verifiquen l'extensió és .png
            raise NameError("L'arxiu no té extensió .png")
        self.__path = file_pathp
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path, 'rb')

        magic = self.__file_object.read(8)
        if magic != self._expected_header:
            raise TypeError("L'arxiu no té format .png")

        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

        # __iter__ i __next__ creen un iterador sobre l'arxiu .png
    def __iter__(self):
        return self

    def __next__(self):
        # Llegirem l'arxiu per trossos
        # Mirar https://en.wikipedia.org/wiki/Portable_Network_Graphics#%22Chunks%22_within_the_file
        initial_data = self.__file_object.read(4)

        # The file hasn't been opened or reached EOF.  This means we
        # can't go any further so stop the iteration by raising the
        # StopIteration.
        if self.__file_object is None or initial_data == b'':
            raise StopIteration
        else:
            # Each chunk has a len, type, data (based on len) and crc
            # Grab these values and return them as a tuple
            chunk_len = int.from_bytes(initial_data, byteorder='big')
            chunk_type = self.__file_object.read(4)
            chunk_data = self.__file_object.read(chunk_len)
            chunk_crc = self.__file_object.read(4)
            return chunk_len, chunk_type, chunk_data, chunk_crc


# Ara podem obrir un arxiu .png d'esta manera:
with PngReader('jack_russell.png') as reader:
    for l, t, d, c in reader:
        print(f"{l:05}, {t}, {c}")

# -------------------------------------------------------------------------------------------
# No reeinventar la roda
# -------------------------------------------------------------------------------------------
# Existixen llibreries pera ha llegir tota classe d'arxius
# 	- wave:		read and write WAV files (audio)
# 	- aifc: 	read and write AIFF and AIFC files (audio)
# 	- sunau: 	read and write Sun AU files
# 	- tarfile: 	read and write tar archive files
# 	- zipfile: 	work with ZIP archives
# 	- configparser: easily create and parse configuration files
# 	- xml.etree.ElementTree: create or read XML based files
# 	- msilib: 	read and write Microsoft Installer files
# 	- plistlib: generate and parse Mac OS X .plist files

# 	- PyPDF2: 	PDF toolkit
# 	- xlwings: 	read and write Excel files
# 	- Pillow: 	image reading and manipulation


# -------------------------------------------------------------------------------------------
#  SERIALITZACIÓ D'OBJECTES AMB EL MÒDUL PICKLE
#	Nota: pickle és insegur. Es pot serialitzar qualsevol objecte com classes malicioses. Mai desresialitzar de fons no fiables.
# -------------------------------------------------------------------------------------------
# La serialització (o marshalling) agafa qualsevol objecte de python i el transforma en un stream de bytes que podem guardar
# en disc o enviar per xarxa. El procés de serialització es pot fer en mode text (txt, xml, json) o en mode binari.
# Per a serialitzar en json tenim el mòdul json i per a mode binari el mòdul pickle (abans s'usava el mòdul marshal)
#
# El mòdul pickle és el més convenient per a guardar objectes en un format no llegible per humans i que només s'utilitzarà
# dins de python (no és un format per a intercanviar dades).
#
# Bàsicament pickel utilita 4 mètodes:
# 	.dump() que serialitza escribint en disc
# 	.load() que deserialitza llegint de disc
# 	.dumps() que serialitza escribint en un string
# 	.loads() que deserialitza llegint d'un string
#
# -------------------------------------------------------------------------------------------
# SERIALITZACIÓ SOBRE STRING
# -------------------------------------------------------------------------------------------
# import pickle
llista = ['Pere', 'Jaume']

# Serialitzar un objecte sobre un string
cadena = pickle.dumps(llista)   # b'\x80\x04\x95\x14\x00\x00\x00\x00\x00\x000\x00]\x94(\x8c\x04Pere\x94\x8c\x05Jaume\x94e.'
                                # <class 'bytes'> 
print(cadena)

# Deserialitzar des d'un string.
# <class 'list'>
llista2 = pickle.loads(cadena)
print(llista2)					# ['Pere', 'Jaume']
# -------------------------------------------------------------------------------------------
# SERIALITZACIÓ SOBRE DISC
# -------------------------------------------------------------------------------------------
name = 'Abder'
website = 'https://abder.io'
english_french = {'pen': 'stylo', 'car': 'voiture'}
tup = (31, 'abder', 4.0)
# ----------------------------------
# OPCIÓ A: fer múltiples dump i load
# ----------------------------------
#
fp = open('arxiu.pkl', 'wb')
pickle.dump(name, fp)
pickle.dump(website, fp)
pickle.dump(english_french, fp)
pickle.dump(tup, fp)
#
fp2 = open('arxiu.pkl','rb')
name = pickle.load(fp2)
website = pickle.load(fp2)
english_french = pickle.load(fp2)
tup = pickle.load(fp2)

# La seqüència de dump i de load ha de ser la mateixa.
# Si pel que siga no volem aixó podríem:
#
fp3 = open('arxiu.pkl', 'wb')
data3 = {'name': name, 'website': website,
        'english_french_dictionary': english_french, 'tuple': tup}
pickle.dump(data3, fp3)
#
fp4 = open('arxiu.pkl','rb')
data4 = pickle.load(fp4)
name = data4['name']
website = data4['website']
english_french = data4['english_french_dictionary']
tup = data4['tuple']

# -----------------------------------------
# OPCIÓ B: amb la class Pickler i Unpickler
# -----------------------------------------
#
# from pickle import Pickler
fp5 = open('arxiu.pkl', 'wb')
p = Pickler(fp5)
p.dump(name)
p.dump(website)
p.dump(english_french)
p.dump(tup)


# from pickle import Unpickler
fp6 = open('arxiu.pkl','rb')
u = Unpickler(fp6)
name = u.load()
website = u.load()
english_french = u.load()
tup = u.load()


#============================================
# Buscar una cadena en una arxiu de text
#============================================
# Opció 1: llegir tot l'arxiu, volcar-lo en una variable i busca en ella.
def busca_cadena(file, cadena):
    with open(ruta, 'r') as f:
        txt = f.read()
        if cadena in txt:
            print("Està en l'arxiu")
        else:
            print("No està en l'arxiu")

busca_cadena(r'C:\demo\files\account\vendes.txt', 'institut')

# Opció 2: llegir tot l'arxiu, volcar-lo en una variable i busca en ella línia a línia.
txt = 'institut'
with open(r'C:\demo\files\account\vendes.txt', 'r') as f:
    for line in f.readlines():
        if line.find(txt) != -1:
            print("Està en l'arxiu en la línia")

# Si l'arxiu de text és molt gran, els mètodes anteriors són ineficient per què lligen l'arxiu sencer.
# En estos casos, millor les següent opcions.
#
# Opció 3:
# enumerate(file_pointer) no carga tot l'arxiu en memòria. En un bucle retorna la línia de text i el seu nombre.a_writer
#
with open(r'C:\demo\files\account\vendes.txt', 'r') as f:
    for no, line in enumerate(f):
        if 'institu' in line:
            print(f"Està en l'arxiu en la línia {no}")

# Opció 4: El més eficient és utilitzar el mòdul mnap (arxiu de mapes de memòria)
# https://rico-schmidt.name/pymotw-3/mmap/index.html
import mmap
with open(r'C:\demo\files\account\vendes.txt', 'rb', 0) as file:
    s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
    if s.find(b'laptop') != -1:
        print('string exist in a file')

# Buffers d'arxius:  MEMÒRIA <-> BÚFER <-> HDD
#
# Un búfer és un nivell intermedi entre les dades en memòria i el disc.
# Si per exemple hem d'escriure un axriu de 100MB i ho fem a 1MB cada vegada, no és
# el mateix fer 100 escriptures de 1MB que una només de 100MB.
#
# Ací és on entra en joc l'opció buffering de la funció open(). La gestió dels búfers no es feina
# de Phyton sinó del sistema operatiu. Phyton fa només d'intermediari amb el SOP.
#
# Segon el tipus d'arxiu (binari o text) el paràmetre buffering pot pendre determinats valors.
# Per defecte està activada.
#
# Ací fem buffering==0 per desactivar-la i que ho gestione d'alguna manera mmap.


#==============================================
# Buscar una cadena en múltiples arxius de text
#==============================================
# os.listdir('ruta') retorna una llista amb els noms d'arxius i directoris en la ruta especificada.

import os
# ruta_directori = r'C:\demos\files_demos\account'
ruta_directori = os.getcwd()
print(ruta_directori)
for arxiu in os.listdir(ruta_directori):
    ruta_arxiu = os.path.join(ruta_directori, arxiu)
    if os.path.isfile(ruta_arxiu) and arxiu.endswith('.py'):
        with open(ruta_arxiu, 'r', encoding='utf-8') as f:
            if 'institut' in f.read():
                print(f'string found in {f.name}')
                break

#============================================
# VERIFICAR SI UN ARXIU I DIRECTORI EXISTIXEN
#============================================
# Una opció és:
try:
    f = open('im-not-here.txt')
    print(file) # File handler
    f.close()
except FileNotFoundError:
    print('Sorry the file we\'re looking for doesn\' exist')

# Una altra, per a verfivar arxius o directoris:
os.path.exists('testfile.txt')
os.path.exists('testdirectory')

# Per a verificar només arxius
os.path.isfile('testfile.txt')

# Per a verificar només directoris
os.path.isdir('testdirectory')





#===========================================
# per a saer el nom del propi programa python el millor es utilitzar sys.argv on està amb la seua ruta completa.
# Exemple: ['g:/Mi unidad/Drive/Documents/IES Ramón Cid 21-22/1r BAT/python/prova2.py']
# Fixemos amb les barres. Sempre són /
nom_programa = sys.argv[0]


# Per a posar les barres correctament (/,\) segons el sistema operatiu fem:
# En el nostre exemple:  g:\Mi unidad\Drive\Documents\IES Ramón Cid 21-22\1r BAT\python\prova2.py
ruta = os.path.abspath(sys.argv[0])



# https://www.youtube.com/watch?v=nwpgOkY69MM&list=PLUbFnGajtZlUl0zYr4crGveP21BbcZG_L&index=23


# https://www.youtube.com/watch?v=59uqAIcEsQc&lis
# 
# º1t=PLheIVUbpfWZ17lCcHnoaa1RD59juFR06C&index=17




# Nombres aleatoris
import random
aleat1 = random.random()    # retorna un float en [0,1]
aleat2 = random.uniform(2.3, 5.8) # retorna un float entre 2.3 i 5.8
aleat3 = random.randint(0, 10)  # retorna un enter entre 0 i 10

# retorna un element a l'atzar d'un iterable
iterable = ('a','b','c','d','e')
element1 = random.choice(iterable)

# desordenar una list
llista1 = ['a','b','c','d']
random.shuffle(llista1)



