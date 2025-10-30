def calcular_año(e):
    elt=e%10
    if elt==0:
        print("tu elemento es agua")
    elif elt==1:
        print("tu elemento es fuego")
    elif elt==2:
        print("tu elemento es tierra")
    elif elt==3:
        print("tu elemento es aire")
    elif elt==4:
        print("tu elemento es luz")
    else:
        print("tu elemento es oscuridad")
    return elt

def generador_predicciones(n,ns,):
    match ns:
        case 1:
            print(n, "tendras un gran dia lleno de energia y vitalidad")
        case 2:
            print(n, "tendras un dia tranquilo y pacifico")
        case 3:
            print(n, "tendras un dia lleno de retos y aprendizajes")
        case 4:
            print(n, "tendras un dia lleno de sorpresas y emociones")
        case _:
            print(n, "tu numero de la suertre es postivo, y hermoso sigue asi")

print("bienvenido al oraculo")
continuar=input("deseas saber tu suerte? ")
if continuar == "si"  or continuar == "Si" or continuar == "SI":
        n=input("cual es tu nombre? ",)
        if n.isnumeric():
            print("error, ingresa un nombre valido")
        else:
            print ("")
        e=int(input ("cual es tu año de nacimiento? "))
        print("")
        ns=int(input("cual es tu numero de la suerte? (1-4)"))
        print ("")
        elt = calcular_año(e)
        print("tu elemento es: ", elt)
        print("")
        print("tu prediccion es: ", generador_predicciones(n,elt,ns))
else:
     print("adios")
