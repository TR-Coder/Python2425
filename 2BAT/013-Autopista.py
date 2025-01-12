from __future__ import annotations

# Enunciat
# Una Persona s'identifica pel seu dni
# Un Cotxe s'identifica per una matrícula i una capacitat d'ocupants (per defecte 4) i per una llista dels seus ocupants (persones)
#   Mètodes:
#       - def entra(self, persona). Error si la persona ja està en el cotxe i se supera la capacitat del Cotxe.
#       - def ix(self, persona). Error si la persona no està en el cotxe.
#       - Mètode per a mostrar els dni dels ocupants del cotxe.
# Una Autopista queda definida per una llista dels cotxes que circulen per ella.
#   Mètodes:
#       - def entra(self, cotxe).
#       - def ix(self, cotxe). Error si intenta traure un cotxe que no està en la autopista.
#       - Mètode per a mostrar la matrícula dels cotxes que estan en l'autopista.


#==================================================================================
class Cotxe_no_en_autopista(Exception):
    pass

class Cotxe_ple(Exception):
    pass

class Persona_ja_està_en_cotxe(Exception):
    pass

class Persona_no_este_cotxe(Exception):
    pass


#==================================================================================
class Autopista:
    def __init__(self) -> None:
        self.vehicles:list[Cotxe] = []

    def entra(self, cotxe:Cotxe) -> None:
        self.vehicles.append(cotxe)

    def ix(self, cotxe:Cotxe) -> None:
        try:
            self.vehicles.remove(cotxe)
        except ValueError:
            raise Cotxe_no_en_autopista
        
    def __str__(self) -> str:
        matricula_cotxes = [str(vehicle.matricula) for vehicle in self.vehicles]
        return ' '.join(matricula_cotxes)

#==================================================================================
class Persona:
    def __init__(self, dni:str) -> None:
        self.dni = dni

    def __eq__(self, persona) -> bool:
        if isinstance(persona, Persona):
            return self.dni == persona.dni
        return False
    

#==================================================================================
class Cotxe:
    def __init__(self, matricula:str, capacitat:int=4) -> None:
        self.matricula:str = matricula
        self.ocupants:list[Persona] = []
        self.capacitat:int = capacitat
    
    def entra(self, persona:Persona) -> None:
        if len(self.ocupants)>self.capacitat:
            raise Cotxe_ple
        if persona in self.ocupants:
            raise Persona_ja_està_en_cotxe
        self.ocupants.append(persona)

    def ix(self, persona:Persona) -> None:
        try:
            self.ocupants.remove(persona)
        except ValueError:
            raise Persona_no_este_cotxe

    def __eq__(self, cotxe) -> bool:
        if isinstance(cotxe, Cotxe):
            return self.matricula == cotxe.matricula
        return False

    def __str__(self) -> str:    
        dni_ocupants = [str(ocupant.dni) for ocupant in self.ocupants]
        return ' '.join(dni_ocupants)
    

#==================================================================================

p1 = Persona('111')
p2 = Persona('222')
p3 = Persona('222')

c1 = Cotxe('2341DFF')
c2 = Cotxe('21354FW')

c1.entra(p1)
c1.entra(p2)
# c1.entra(p3)
print(c1)
c1.ix(p3)
print(c1)

a7 = Autopista()
a7.entra(c1)
print(a7)



#==================================================================================
# Avançat. Com podríem evitar crear persones amb el mateix dni.
#==================================================================================

class Persona:
    _instancia:dict[str,Persona] = {}         # Diccionari per a emmagatzemar instàncies.

    def __new__(cls, dni: str, *args, **kwargs):
        if dni in cls._instancia:           # Si ja existeix una instància amb el mateix dni, es retorna l'existent.
            return cls._instancia[dni]
        
        instancia = super().__new__(cls)    # Si no existix, es crea una nova instància
        cls._instancia[dni] = instancia     # Guarda la nova instància
        return instancia

    def __init__(self, dni: str) -> None:
        if hasattr(self, 'dni'): # Comprovació per a evitar la reinicialització d'atributs.
            return
        self.dni = dni

    @classmethod
    def totes_les_instancies(cls):
        return list(cls._instancia.values())  # Retorna totes les instàncies creades.

    def __del__(self):
        if self.dni in self._registre:         # Eliminem la instància quan es destruix.
            del self._registre[self.dni]

# PROBLEMA: Python no garantix quan es cride a __del__ ja que això depén de recolector
# de brossa. Ni tan sols si eliminen un objecte explícitament un 'del'.
# Una solució és gestionar explícitament l'eliminació del dni des d'un mètode dedicat, com esborra_instancia
    @classmethod
    def esborra_instancia(cls, dni: str):
        if dni in cls._instancia:        # Elimina una instància del registre.
            del cls._instancia[dni]

p1 = Persona('1')
p2 = Persona('1')
print(p1==p2)       # True