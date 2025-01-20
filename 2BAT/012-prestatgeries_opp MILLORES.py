import os
import platform

# --------------------------------------------------------------------------------------------
# Una biblioteca està formada per les següents entitats: Llibres, estants i prestatgeries.
# La dinànica del programa és:
#   - Afegir prestatgeries a la biblioteca:
# --------------------------------------------------------------------------------------------
def Esborra_la_terminal():
    """Neteja la terminal. Té en compte els sistema operatiu: Windows (cls) o Linux (clear). """
    clear_screen = 'cls' if platform.system() == 'Windows' else 'clear'
    os.system(clear_screen)

# --------------------------------------------

class Prestatgeria_sense_estants(Exception):
    def __init__(self, *args):
        self.missatge_error = 'La prestatgeria no té estants'
        super().__init__(self.missatge_error, *args)

class Prestatgeria_plena(Exception):
    def __init__(self, *args):
        self.missatge_error = 'La prestatgeria està plena'
        super().__init__(self.missatge_error, *args)

class Llibre_no_esta_en_biblioteca(Exception):
    def __init__(self, *args):
        self.missatge_error = 'El llibre no esté es la biblioteca'
        super().__init__(self.missatge_error, *args)

class No_queden_estants_nous_per_a_ubicar(Exception):
    def __init__(self, *args):
        self.missatge_error = 'No queden estants nous per ubicar'
        super().__init__(self.missatge_error, *args)

class ISBN_incorrecte(Exception):
    def __init__(self, *args):
        self.missatge_error = "L'ISBN del llibre és incorrecte"
        super().__init__(self.missatge_error, *args)    

# --------------------------------------------
class Llibre:
    def __init__(self, isbn:str, titol:str) -> None:
        self.isbn = isbn
        self.titol = titol
    
    @classmethod
    def es_isbn_correcte(cls, isbn:str) -> bool:
        return len(isbn) == 6 and isbn[:3].isalpha() and isbn[3:].isdigit()
    
    def __str__(self) -> str:
        return f'Llibre {self.isbn}, {self.titol}'
    
    def __eq__(self, obj) -> bool:
        if isinstance(obj, Llibre):
            return self.isbn == obj.isbn
        return False

# --------------------------------------------
class Estant:
    def __init__(self, capacitat:int) -> None:
        self.capacitat:int = capacitat
        self.llibres:list[Llibre] = []

    def nombre_llibres(self) -> int:
        return len(self.llibres)

    @classmethod
    def es_capacitat_correcta(cls, capacitat:int) -> bool:
        return capacitat>=0 and capacitat<=5
    
    def __str__(self) -> str:
        cadena = f' Estant de {self.capacitat} llibres: '
        for llibre in self.llibres:
            cadena += llibre.isbn + ', '
        return cadena
# --------------------------------------------
class Prestatgeria:
    def __init__(self) -> None:
        global biblioteca
        self.estants:list[Estant] = []
        self.id = biblioteca.nombre_prestatgeries + 1

    def afig_estant(self) -> None:
        if not estants_sense_ubicar:
            raise No_queden_estants_nous_per_a_ubicar
        estant = estants_sense_ubicar.pop()
        self.estants.append(estant)

    def afig(self, llibre: Llibre):
        if not self.estants:
            raise Prestatgeria_sense_estants
        
        for estant in self.estants:
            if estant.nombre_llibres() < estant.capacitat:
                estant.llibres.append(llibre)
                return
 
        raise Prestatgeria_plena
    
# --------------------------------------------
class Biblioteca:
    def __init__(self) -> None:
        self.prestatgeries: list[Prestatgeria] = []

    def afig(self, prestatgeria: Prestatgeria) -> None:
        self.prestatgeries.append(prestatgeria)

    @property
    def nombre_prestatgeries(self) -> int:
        return len(self.prestatgeries)

    def obtin(self, id_prestatgeria: int) -> Prestatgeria|None:
        for prestatgeria in self.prestatgeries:
            if prestatgeria.id == id_prestatgeria:
                return prestatgeria
        return None
    



llibre1 = Llibre(isbn='aaa111', titol='aaa')
llibre2 = Llibre(isbn='bbb222', titol='bbb')
estant1 = Estant(2)

biblioteca = Biblioteca()
llibres_sense_ubicar: list[Llibre] = [llibre1, llibre2]
estants_sense_ubicar: list[Estant] = [estant1]

# --------------------------------------------
def crea_llibre() -> Llibre|None:
    while True:
        print('Introduïx un ISBN o Intro per a eixir')
        isbn = input('ISBN? ')

        if isbn == '':
            return None
        
        if Llibre.es_isbn_correcte(isbn):
            break

        print('Error, ISBN incorrecte')
    
    print('Introduïx el nom del llibre')
    nom = input('Nom? ')
    return Llibre(isbn, nom)

# --------------------------------------------
def crea_estant()-> Estant|None:
    print('Introduïx la quantitat de llibres màxima o Intro per a eixir')
    while True:
        try:
            capacitat = input('Capacitat? (5 màx.)')
            if capacitat == '':
                return None
            capacitat_int = int(capacitat)
            if Estant.es_capacitat_correcta(capacitat_int):
                return Estant(capacitat_int)
            print('Error: capacitat fóra de límits')
        except ValueError:
            print('Error, capacitat incorrecta')

# --------------------------------------------
def input_id_prestatgeria() -> Prestatgeria|None:
    print("Introduïx l'identificador d'una prestatgeria o Intro per a eixir")
    while True:
        id_prestatgeria = input('Identificador? ')
        if id_prestatgeria == '':
            return None
        try:
            id_prestatgeria_int = int(id_prestatgeria)
            prestatgeria = biblioteca.obtin(id_prestatgeria_int)
            if prestatgeria:
                return prestatgeria
            print('Error, la prestatgeria no existix')
        except ValueError:
            print('Error, codi incorrecte')       

# --------------------------------------------
def input_isbn_llibre_sense_ubicar() -> Llibre|None:
    while True:
        print("Introduïx l'isbn d'un llibre sense ubicar o Intro per a eixir")
        isbn = input('ISBN? ')
        if isbn == '':
            return None
        
        for llibre in llibres_sense_ubicar:
            if llibre.isbn == isbn:
                return llibre
        
        print('No existix este isnb en llibres sense ubicar')

def esborra_de_llibres_sense_ubicar(llibre: Llibre) -> None:
    try:
        llibres_sense_ubicar.remove(llibre)
    except ValueError:
        pass

# --------------------------------------------
def input_isbn() -> str|None:
    print("Introduïx l'isbn del llibre a extraure")
    isbn = input('ISBN? ')
    if isbn == '':
        return None
    if Llibre.es_isbn_correcte(isbn):
        return isbn
    
    raise ISBN_incorrecte

# --------------------------------------------
def busca_llibre_i_lleva_de_biblioteca(isbn:str) -> None:
    for prestatgeria in biblioteca.prestatgeries:
        for index,estant in enumerate(prestatgeria.estants):
            for llibre in estant.llibres:
                if llibre.isbn==isbn:
                    llibres_sense_ubicar.append(llibre)
                    estant.llibres.pop(index)
                    return
    raise Llibre_no_esta_en_biblioteca

# --------------------------------------------
def info(msg_error:str|None) -> None:
    print('Llibres sense ubicar:')
    print('--------------------')
    for llibre in llibres_sense_ubicar:
        print(f'  {llibre}')

    print('\nEstants sense ubicar:')
    print('-------------------')
    for estant in estants_sense_ubicar:
        print(f'   {estant}')

    print('\nPrestatgeries:')
    print('---------------')
    for prestatgeria in biblioteca.prestatgeries:
        print(f"  {prestatgeria.id=}")
        for estant in prestatgeria.estants:
            print(f'    {estant}')

    if msg_error is not None:
        print(f'\n*** ERROR: {msg_error}: ')


# --------------------------------------------
# Opcions del menú
# --------------------------------------------

# '1- Afig una prestatgeria nova a la biblioteca'
def crea_i_afig_una_prestatgeria_a_la_biblioteca() -> None:
    prestatgeria = Prestatgeria()
    biblioteca.afig(prestatgeria)

# 2- Crea un llibre nou'
def crea_un_llibre_nou() -> None:
    llibre = crea_llibre()
    if llibre is None:
        return
    llibres_sense_ubicar.append(llibre)

# 3- Crea un estant nou'
def crea_un_estant_nou() -> None:
    estant = crea_estant()
    if estant is None:
        return
    estants_sense_ubicar.append(estant)

# '4- Afig un estant a una prestatgeria'
def afig_un_estant_a_una_prestatgeria() -> None:
    prestatgeria = input_id_prestatgeria()
    if prestatgeria is None:
        return
    try:
        prestatgeria.afig_estant()
    except No_queden_estants_nous_per_a_ubicar as e:
        return e.missatge_error


# '5- Afig un llibre a una prestatgeria'
def afig_un_llibre_a_una_prestatgeria() -> None:
    llibre = input_isbn_llibre_sense_ubicar()
    
    if llibre is None:
        return
    
    while True:
        prestatgeria = input_id_prestatgeria()
        if prestatgeria is None:
            return
        try:
            prestatgeria.afig(llibre)
            esborra_de_llibres_sense_ubicar(llibre)
        except (Prestatgeria_sense_estants,Prestatgeria_plena) as e:
            print(e.missatge_error)

# '6- Busca i lleva un llibre de la biblioteca'
def busca_i_lleva_un_llibre_de_la_biblioteca() -> None:
    while True:
        try:
            isbn = input_isbn()
            if isbn is None:
                return
            busca_llibre_i_lleva_de_biblioteca(isbn)       
        except (Llibre_no_esta_en_biblioteca, ISBN_incorrecte) as e:
            print(e.missatge_error)


# --------------------------------------------
def processa_menu(opcio:str)  -> None:
    if opcio == '1':
        crea_i_afig_una_prestatgeria_a_la_biblioteca()  
    elif opcio == '2':
        crea_un_llibre_nou()
    elif opcio == '3':
        crea_un_estant_nou()   
    elif opcio == '4':
        afig_un_estant_a_una_prestatgeria()
    elif opcio == '5':
        afig_un_llibre_a_una_prestatgeria()
    elif opcio == '6':
        busca_i_lleva_un_llibre_de_la_biblioteca()
    elif opcio == 'Q':
        exit()

# --------------------------------------------
def main() -> None:
    while True:
        Esborra_la_terminal()

        print('\n====== MENÚ ======')
        print('1- Afig una prestatgeria nova a la biblioteca')
        print('2- Crea un llibre nou')
        print('3- Crea un estant nou')
        print('4- Afig un estant a una prestatgeria')
        print('5- Afig un llibre a una prestatgeria')
        print('6- Busca i lleva un llibre de la biblioteca')
        print('Q- Ix del programa')

        opcio = input('Opció? ')
        processa_menu(opcio)

# --------------------------------------------
main()