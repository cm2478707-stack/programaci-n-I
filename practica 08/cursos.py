print("bienvenido a los cursos de itson")
cursos=[
    "Ingenieria en sistemas computacionales",
    "Ingenieria en tecnologias de la informacion",
    "Ingenieria en mecatronica",
]
cursos_explicitos=[
    """Ingenieria en sistemas computacionales:
    -Duracion: 9 semestres
    -aula: 405
    maestro:Juan perez""",
    """Ingenieria en tecnologias de la informacion:
    -Duracion: 9 semestres
    -aula: 410
    maestro: Maria lopez""",
    """Ingenieria en mecatronica:
    -Duracion: 9 semestres
    -aula: 420
    maestro: Carlos Sanchez""",
]
alumno=[
    "Ana Gomez:ingenieria en sistemas computacionales",
    "Luis Martinez:ingenieria en tecnologias de la informacion",
    "Sofia Hernandez:ingenieria en mecatronica",
    "Diego Ramirez: inegenieria en sistemas computacionales",
    "Isaias Torres:Ningun curso",
]
ingenieria_sistemas=0
ingenieria_tecnologias=0
ingenieria_mecatronica=0
if "ingenieria en sistemas computacionales" in alumno:
    ingenieria_sistemas+=1
if "ingenieria en tecnologias de la informacion" in alumno:
    ingenieria_tecnologias+=1
if "ingenieria en mecatronica" in alumno:
    ingenieria_mecatronica+=1
enumerated_cursos=list(enumerate(cursos))

print ("Estos son los cursos que ofrecemos:"  + str(cursos))
deseas_modificarlos=input("deseas modificarlos? s/n:").lower()
while deseas_modificarlos=="si" or deseas_modificarlos=="s":
    que_deseas_hacer=input("que deseas hacer? agregar/eliminar/modificar:").lower()
    if que_deseas_hacer=="agregar":
        nuevo_curso=input("cual curso deseas agregar?:")
        cursos.append(nuevo_curso)
        print("El curso ha sido agregado exitosamente")
        print("Los cursos actualizados son:" + str(cursos))
    elif que_deseas_hacer=="eliminar":
        curso_a_eliminar=input("cual curso deseas eliminar?: ")
        cursos.remove(curso_a_eliminar)
        print("el curso ha sido eliminado exitosamente ")
        print("Los cursos actualizados son:" + str(cursos))
    elif que_deseas_hacer=="modificar":
        curso_a_modificar=input("cual curso deseas modificar?")
        nuevo_nombre_curso=input("cual es el nuevo nombre del curso?:")
        indice=cursos.index(curso_a_modificar)
        print(indice)
        print ("El curso ha sido modificado exitosamente")
        cursos[indice]=nuevo_nombre_curso
        print("Los cursos actualizados son:" + str(cursos))
    else:
        print("opcion no valida")
    deseas_modificarlos=input("deseas seguir modificando los cursos? s/n:").lower()
deseas_conocer_cursos=input("deseas conocer los maestros y el aula de los cursos? s/n:").lower()
if  deseas_conocer_cursos=="si" or deseas_conocer_cursos=="s":
    print((cursos_explicitos))
else:
    print("Gracias por visitar la lista de cursos")
deseas_conocer_alumnos=input("deseas conocer los alumnos inscritos en los cursos? s/n:").lower()
if deseas_conocer_alumnos=="si" or deseas_conocer_alumnos=="s":
    print((alumno))
    desesa_modificar_alumnos=input("deseas modificar algun alumno? s/n:").lower()
    while desesa_modificar_alumnos=="si" or desesa_modificar_alumnos=="s":
        alumnos_modicador=input("cual alumno deseas modificar?:")
        if alumnos_modicador in alumno:
            nuevo_alumno=input("cual es el nuevo nombre del alumno y su curso?:")
            indice_alumno=alumno.index(alumnos_modicador)
            alumno[indice_alumno]=nuevo_alumno
            print("El alumno ha sido modificado exitosamente")
            print("Los alumnos actualizados son:" + str(alumno))
            desea_agregar_alumno=input("deseas agregar un nuevo alumno? s/n:").lower()
            if desea_agregar_alumno=="si" or desea_agregar_alumno=="s":
                nuevo_alumno_agregar=input("cual es el nombre del nuevo alumno y su curso?:")
                alumno.append(nuevo_alumno_agregar)
                print("El alumno ha sido agregado exitosamente")
                print("Los alumnos actualizados son:" + str(alumno))
            else:
                print("Gracias por visitar la lista de alumnos")
        else:
            print("El alumno no se encuentra en la lista")
        desesa_modificar_alumnos=input("deseas seguir modificando algun alumno? s/n:").lower()
else:
    print("Gracias por visitar la lista de alumnos")
print("Conteo de alumnos por curso:")
print("Ingenieria en sistemas computacionales:" + str(ingenieria_sistemas))
print("Ingenieria en tecnologias de la informacion:" + str(ingenieria_tecnologias))
print("Ingenieria en mecatronica:" + str(ingenieria_mecatronica))