climas={
    "soleado",
    "nublado",
    "lluvioso"
}
w=input("el clima de hoy es: ")
if w in climas:
    print("clima registrado")
else:
    print("clima no registrado")
    
ds=input("a que dia estamos? ")
dis={
    "lunes",
    "martes",
    "miercoles",
    "jueves",
    "viernes",
    "sabado",
    "domingo" 
}
if ds in dis:
    print("dia registrado")
else :
    print("dia no registrado")

if ds=="lunes" or ds=="martes" or ds=="miercoles" or ds=="jueves" or ds=="viernes" and w!="lluvioso":
    print("hoy toca ir a trabajar pero con cuidado de no resbalar")
elif ds=="sabado" or ds=="domingo" or w=="lluvioso":
    print("hoy no toca ir a trabajar disfruta de tu dia lluvioso con una cafe")
else:
    pass

if ds=="lunes" or ds=="martes" or ds=="miercoles" or ds=="jueves" or ds=="viernes" and w=="soleado":
    print("hoy toca ir a trabajar y disfrutar del sol")
elif ds=="sabado" or ds=="domingo" and w =="soleado":
    print("hoy no toca ir a trabajar disfruta de tu dia soleado en el parque")
else:
    pass

if ds=="lunes" or ds=="martes" or ds=="miercoles" or ds=="jueves" or ds=="viernes" and w=="nublado":
    print("hoy toca ir a trabajar y disfrutar del clima nublado")
elif ds=="sabado" or ds=="domingo" and w=="nublado":
    print("hoy no toca ir a trabajar disfruta de tu dia nublado en casa")
pass 