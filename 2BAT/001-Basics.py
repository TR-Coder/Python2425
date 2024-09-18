# ===============
# Temes a tractar
# ===============
# 	- tipus bàsics: int, float, str, bool
# 	- f-strings

# ====
# Nota
# ====
# import és una paraula reservada. Podem utilitzar enlloc import_
# Per concenció, les constants es declaren en majúscula.


# ==========
# FORMATACIÓ
# ==========
# {variable: 7}		7 espais
# {variable: .3f}	3 decimals (sinó poses la f es mostra en format exponencial)
# {variable: 7.3f}	7 espais, d'ells 3 són per a decimals
# {variable: 07.3f}	0 és un caràcter d'emplenament
# {variable:^07.3f}	^ alineament centrat, < esquerra i > dreta



# ====================
# Convencions de noms:
# ====================
# CAPSLOCK    ->  Tot en majúscules   PI=3.14
# snake_case	->	tot en minúscules separades per _   (el de Python)
# PascalCase	->	tot junt i la primera en majúscules
# camelCase	->	com PascalCase per la primera de totes en minúscula



# ====================
# ENUNCIAT
# ====================
# Factura: demanar una quantitat i un preu, l'IVA és del 21%
IVA: int = 21
quantitat: int = int(input('Quantitat: '))
preu: float = float(input('Preu: '))

base_IVA: float = quantitat * preu
import_IVA: float = base_IVA * IVA / 100
import_total: float = base_IVA + import_IVA     # És més clar fer els càlculs en variable que en el print. A banda, podem reutilitar els càlculs.

print(f'Has de pagar {base_IVA: .2f} € y un IVA de {import_IVA: .2f} €. \nEn total són {import_total: .2f} €')



