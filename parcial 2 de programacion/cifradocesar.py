print("Cifrado César")
texto_a_cifrar = input("Ingrese el texto a cifrar: ").lower()
if " " in texto_a_cifrar:
    print("Los espacios serán cambiados por guiones bajos")
    texto_a_cifrar = texto_a_cifrar.replace(" ", "_")
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_desplazado = "defghijklmnopqrstuvwxyzabc"
tabla_de_traduccion = str.maketrans(alfabeto,alfabeto_desplazado)
texto_cifrado = texto_a_cifrar.translate(tabla_de_traduccion)
print("El texto cifrado es:", texto_cifrado)
