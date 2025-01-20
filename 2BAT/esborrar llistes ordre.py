        

etiqueta=str(input("Tria la etiqueta (n��mero): "))

etiqueta=etiqueta.split()

e=0

for posicio,x in enumerate(etiquetes):
    for etiq in etiqueta:
        etiq=int(etiq)
        etiq= etiq-e
        
        
        eliminar=False
        if posicio==etiq:
            if contactes==[]:
                eliminar=True
            for contacte in contactes:
                if etiquetes[etiq] in contacte:
                    print(f"La etiqueta {x} est�� en ��s")
                    input()
                else:
                    eliminar=True
        
        if eliminar:
            etiquetes.pop(etiq)
            e+=1
            # if x not in contactes:
            #     etiquetes.pop(etiq)
            #     e+=1
