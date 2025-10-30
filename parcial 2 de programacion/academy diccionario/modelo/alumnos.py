from . import curso
lista_alumnos=[
    "Miguel Angel:Ingenieria en Sistemas Computacionales",
    "Carla Jimenez:Ingenieria en Gestion Empresarial",
    "Fernando Torres:Ingenieria en Tecnologias de la Informacion",
    "Lucia Fernandez:Ingenieria en Sistemas Computacionales",
    "Jorge Morales:Ningun curso",
    "Sofia Castro:Ingenieria en Gestion Empresarial",
    "Diego Vargas:Ingenieria en Tecnologias de la Informacion",
    "Valeria Rojas:Ingenieria en Sistemas Computacionales",
    ]

def eliminar_alumno():
    print(lista_alumnos)
    nombre_alumno = input("Cual es el nombre del alumno que deseas eliminar?: ").lower()
    alumno_encontrado = None

    for alumno in lista_alumnos:

        nombre_en_lista = alumno.split(":")[0].lower() 
    if nombre_alumno == nombre_en_lista:
        alumno_encontrado = alumno
 
    if alumno_encontrado:
        lista_alumnos.remove(alumno_encontrado)
        print(f"El alumno {nombre_alumno} ha sido eliminado exitosamente")
    else:
        print("El alumno no se encuentra en la lista")
def agregar_alumno():
    nuevo_alumno = input("Cual es el nombre del alumno que deseas agregar?: ")
    curso_alumno = input("Cual es el curso del alumno?: ")
    alumno_completo = f"{nuevo_alumno}:{curso_alumno}"
    lista_alumnos.append(alumno_completo)
    print(f"El alumno {nuevo_alumno} ha sido agregado exitosamente")
    return alumno_completo
def modificar_alumno():
    nombre_alumno = input("Cual es el nombre del alumno que deseas modificar?: ")
    for i, alumno in enumerate(lista_alumnos):
        if nombre_alumno.lower() in alumno.lower():
            nuevo_nombre = input("Cual es el nuevo nombre del alumno?: ")
            curso_alumno = input("Cual es el curso del alumno?: ")
            lista_alumnos[i] = f"{nuevo_nombre}:{curso_alumno}"
            print(f"El alumno {nombre_alumno} ha sido modificado exitosamente")
            return lista_alumnos[i]
    print("El alumno no se encuentra en la lista")
def mostrar_alumnos():
    print("================================")
    for alumno in lista_alumnos:
        print(alumno)
        print("================================")

def mostrar_cursos_y_alumnos():
    print("=============================================")
    curso.mostrar_cursos()
    print ("=============================================")
    mostrar_alumnos()
    print("=============================================")

def contar_alumnos_por_curso():
    ingenieria_sistemas = 0
    ingenieria_gestion = 0
    ingenieria_tecnologias = 0
    for alumno_info in lista_alumnos:
        if "ingenieria en sistemas computacionales" in alumno_info.lower():
            ingenieria_sistemas += 1
        elif "ingenieria en gestion empresarial" in alumno_info.lower():
            ingenieria_gestion += 1
        elif "ingenieria en tecnologias de la informacion" in alumno_info.lower():
            ingenieria_tecnologias += 1
    print("================================")
    print(f"Ingenieria en Sistemas Computacionales: {ingenieria_sistemas}")
    print(f"Ingenieria en Gestion Empresarial: {ingenieria_gestion}")
    print(f"Ingenieria en Tecnologias de la Informacion: {ingenieria_tecnologias}")
    print("================================")