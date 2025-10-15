def calcular_año(e):
    et=e%10
    if et==0:
        print("tu elemento es agua")
    elif et==1:
        print("tu elemento es fuego")
    elif et==2:
        print("tu elemento es tierra")
    elif et==3:
        print("tu elemento es aire")
    elif et==4:
        print("tu elemento es luz")
    else:
        print("tu elemento es oscuridad")
    return et

def generador_predicciones(n,et,ns):
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
continuar=input("deseas saber tu suerte?")
if continuar == "si"  or continuar == "Si" or continuar == "SI":
        n=input("cual es tu nombre? ",)
        e=int(input ("cual es tu año de nacimiento? "))
        ns=int(input("cual es tu numero de la suerte? (1-4)"))
        et = calcular_año(e)
        print("tu elemento es: ", et)
        print("tu prediccion es: ", generador_predicciones(n,et,ns))
else:
     print("adios")
