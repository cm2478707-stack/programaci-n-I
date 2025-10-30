cursos=[
    "Ingenieria en Sistemas Computacionales-Aula 101-maestro: Carlos Ramirez",
    "Ingenieria en Gestion Empresarial-Aula 305-maestro: Ana Maria Gutierrez",
    "Ingenieria en Tecnologias de la Informacion-Aula 420-maestro: Luis Fernando Lopez",
]
alumnos=[
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
    nombre_alumno=input("Cual es el nombre del alumno que deseas eliminar?: ")
    for alumno in alumnos:
        if nombre_alumno.lower() in alumno.lower():
            alumnos.remove(alumno)
            print(f"El alumno {nombre_alumno} ha sido eliminado exitosamente")
            return
    print("El alumno no se encuentra en la lista")

def agregar_alumno():
    nuevo_alumno=input("Cual es el nombre del alumno que deseas agregar?: ")
    curso_alumno=input("Cual es el curso del alumno?: ")
    alumno_completo=f"{nuevo_alumno}:{curso_alumno}"
    alumnos.append(alumno_completo)
    print("El alumno {nuevo_alumno} ha sido agregado exitosamente")
    return alumno_completo

def modificar_alumno():
    nombre_alumno=input("Cual es el nombre del alumno que deseas modificar?: ")
    for i, alumno in enumerate(alumnos):
        if nombre_alumno.lower() in alumno.lower():
            nuevo_nombre=input("Cual es el nuevo nombre del alumno?: ")
            curso_alumno=input("Cual es el curso del alumno?: ")
            alumnos[i]=f"{nuevo_nombre}:{curso_alumno}"
            print(f"El alumno {nombre_alumno} ha sido modificado exitosamente")
            return alumnos[i]
    print("El alumno no se encuentra en la lista")

def agregar_curso():
    nuevo_curso=input("Cual curso deseas agregar?: (nombre de la materia,aula y nombre del maestro) ")
    cursos.append(nuevo_curso)
    print("El curso ha sido agregado exitosamente")
    print("======================================")
    print(cursos)
    print("=======================================")
    return nuevo_curso
def eliminar_curso(cursos):
    curso_a_eliminar=input("Cual curso deseas eliminar?: ")
    if curso_a_eliminar in cursos:
        cursos.remove(curso_a_eliminar)
        print("El curso ha sido eliminado exitosamente")
    else:
        print("El curso no se encuentra en la lista")
    return curso_a_eliminar
def modificar_curso(cursos):
    curso_a_modificar=input("Cual curso deseas modificar?: ")
    if curso_a_modificar in cursos:
        nuevo_nombre_curso=input("Cual es el nuevo nombre del curso?: ")
        indice=cursos.index(curso_a_modificar)
        cursos[indice]=nuevo_nombre_curso
        print("El curso ha sido modificado exitosamente")
    else:
        print("El curso no se encuentra en la lista")
    return curso_a_modificar
def eliminar_alumno():
    nombre_alumno=input("Cual es el nombre del alumno que deseas eliminar?: ")
    for alumno in alumnos:
        if nombre_alumno.lower() in alumno.lower():
            alumnos.remove(alumno)
            print(f"El alumno {nombre_alumno} ha sido eliminado exitosamente")
            return
    print("El alumno no se encuentra en la lista")

def agregar_alumno():
    nuevo_alumno=input("Cual es el nombre del alumno que deseas agregar?: ")
    curso_alumno=input("Cual es el curso del alumno?: ")
    alumno_completo=f"{nuevo_alumno}:{curso_alumno}"
    alumnos.append(alumno_completo)
    print("El alumno {nuevo_alumno} ha sido agregado exitosamente")
    return alumno_completo

def modificar_alumno():
    nombre_alumno=input("Cual es el nombre del alumno que deseas modificar?: ")
    for i, alumno in enumerate(alumnos):
        if nombre_alumno.lower() in alumno.lower():
            nuevo_nombre=input("Cual es el nuevo nombre del alumno?: ")
            curso_alumno=input("Cual es el curso del alumno?: ")
            alumnos[i]=f"{nuevo_nombre}:{curso_alumno}"
            print(f"El alumno {nombre_alumno} ha sido modificado exitosamente")
            return alumnos[i]
    print("El alumno no se encuentra en la lista")