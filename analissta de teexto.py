texto=input("ingrese el texto:".lower())
if len(texto)<1:
    print("ingrese al menos una letra")
    texto=input("ingrese el texto:".lower())
palabra1=input("ingrese la letra a buscar: ")
if len(palabra1)>1:
     print("ingrese solo una letra")
     palabra1=input("ingrese la letra a buscar: ")
elif palabra1 is not str:
     print("ingrese solo letras")
     palabra1=input("ingrese la letra a buscar: ")
palabra2=input("ingrese la letra a buscar: ")
if len(palabra2)>1:
     print("ingrese solo una letra")
     palabra2=input("ingrese la letra a buscar: ")
elif palabra2 is not str:
        print("ingrese solo letras")
        palabra2=input("ingrese la letra a buscar: ")
palabra3=input("ingrese la letra a buscar: ")
if len(palabra3)>1:
     print("ingrese solo una letra")
     palabra3=input("ingrese la letra a buscar: ")
elif palabra3 is not str:
        print("ingrese solo letras")
        palabra3=input("ingrese la letra a buscar: ")

contador1=0
contador2=0
contador3=0
for i in texto:
    if i==palabra1:
            contador1+=1
    if i==palabra2:
            contador2+=1
    if i==palabra3:
            contador3+=1
print("la letra", (palabra1)  , "se repite", (contador1), "veces y la letra", (palabra2), "se repite", (contador2), "veces y la letra", (palabra3), "se repite", (contador3), "veces")
espacios=0
if " " in texto:
    for i in texto:
        if i==" ":
            espacios+=1
print("la cantidad de palabras en el texto es de:", (espacios))
if "python" in texto:
    print("la palabra python si aparece en el texto")
else:
    print("la palabra python no aparece en el texto")
textoalreves=texto
textoalreves.reverse()
print("el texto al reves es:", (textoalreves))
