import random

posibles_respuestas = {
    "tal vez",
    "definitivamente",
    "no lo creo",
    "sin duda",
    "es cierto",
    "no cuentes con ello",
    "puedes confiar en ello",
    "mi respuesta es no",}

print("¡Bienvenido a la Bola Mágica!")
desea=input("¿Deseas conocer tu suerte? (si/no): ").lower()
while desea == "si":
    pregunta = input("Escribe tu pregunta: ")
    respuesta = random.choice((posibles_respuestas))
    print("La Bola Mágica dice:", respuesta)
    desea = input("¿Quieres hacer otra pregunta? (si/no): ").lower()
    