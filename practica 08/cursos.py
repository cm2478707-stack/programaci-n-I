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
for alumno_info in alumno:
    if "ingenieria en sistemas computacionales" in alumno_info.lower():
        ingenieria_sistemas += 1
    elif "ingenieria en tecnologias de la informacion" in alumno_info.lower():
        ingenieria_tecnologias += 1
    elif "ingenieria en mecatronica" in alumno_info.lower():
        ingenieria_mecatronica += 1
    else :
        pass
def mostrar_iguales():
    print("================================")  
print ("Estos son los cursos que ofrecemos:")
print ("================================")
print(cursos)
print ("================================")
deseas_modificarlos=input("deseas modificarlos? s/n:").lower()
while deseas_modificarlos=="si" or deseas_modificarlos=="s":
    que_deseas_hacer=input("que deseas hacer? agregar/eliminar/modificar:").lower()
    if que_deseas_hacer=="agregar":
        nuevo_curso=input("cual curso deseas agregar?:")
        cursos.append(nuevo_curso)
        print("El curso ha sido agregado exitosamente")
        print("Los cursos actualizados son:")
        print("===============================")
        print(cursos)
        print("===============================")
    elif que_deseas_hacer=="eliminar":
        curso_a_eliminar=input("cual curso deseas eliminar?: ")
        cursos.remove(curso_a_eliminar)
        print("el curso ha sido eliminado exitosamente ")
        print("Los cursos actualizados son:")
        print("===============================")
        print(cursos)
        print("===============================")
    elif que_deseas_hacer=="modificar":
        curso_a_modificar=input("cual curso deseas modificar?")
        nuevo_nombre_curso=input("cual es el nuevo nombre del curso?:")
        indice=cursos.index(curso_a_modificar)
        print(indice)
        print ("El curso ha sido modificado exitosamente")
        cursos[indice]=nuevo_nombre_curso
        print("Los cursos actualizados son:")
        print("===============================")
        print(cursos)
        print("===============================")
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
        que_deseas_hacer_alumno=input("que deseas hacer? agregar/eliminar/modificar:").lower()
        if que_deseas_hacer_alumno=="agregar":
            nuevo_alumno=input("cual alumno deseas agregar?:")
            alumno.append(nuevo_alumno)
            print("El alumno ha sido agregado exitosamente")
            print("Los alumnos actualizados son:" + str(alumno))
        elif que_deseas_hacer_alumno=="eliminar":
            alumno_a_eliminar=input("cual alumno deseas eliminar?: ")
            alumno.remove(alumno_a_eliminar)
            print("el alumno ha sido eliminado exitosamente ")
            print("Los alumnos actualizados son:" + str(alumno))
        elif que_deseas_hacer_alumno=="modificar":
            alumno_a_modificar=input("cual alumno deseas modificar?")
            nuevo_nombre_alumno=input("cual es el nuevo nombre del alumno?:")
            indice_alumno=alumno.index(alumno_a_modificar)
            print(indice_alumno)
            print ("El alumno ha sido modificado exitosamente")
            alumno[indice_alumno]=nuevo_nombre_alumno
            print("Los alumnos actualizados son:" + str(alumno))
        else:
            print("opcion no valida")
        desesa_modificar_alumnos=input("deseas seguir modificando los alumnos? s/n:").lower()       
else:
    print("Gracias por visitar la lista de alumnos")
print("Conteo de alumnos por curso:")
print("Ingenieria en sistemas computacionales:" + str(ingenieria_sistemas))
print("Ingenieria en tecnologias de la informacion:" + str(ingenieria_tecnologias))
print("Ingenieria en mecatronica:" + str(ingenieria_mecatronica))