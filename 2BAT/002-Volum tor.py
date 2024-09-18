# ====================
# ENUNCIAT
# ====================
# Volum d'un tor: 2 * pi^2 * R * r^2


# ====================
# TEORIA
# ====================
# import math 				Importem tots els mòduls i altres components del paquet math. Hem d'usar el namespace com pe: math.pi, math.pow
# from math import pi		Importem nomes la constant pi del paquet math.


from math import pi as PI                           # Importem i renomenem pi per PI

radi_major: float = float(input('Radi major: '))
radi_menor: float = float(input('Radi menor: '))
volum_tor: float = 2 * PI**2 * radi_major * pow(radi_menor, 2)
print(f'El volum del tor és {volum_tor:.2f}')  # dos decimal .2f

print(type(PI))     # La funció type() permet verificar el tipus.
