
cursos=[
    "Ingenieria en Sistemas Computacionales-Aula 101-maestro: Carlos Ramirez",
    "Ingenieria en Gestion Empresarial-Aula 305-maestro: Ana Maria Gutierrez",
    "Ingenieria en Tecnologias de la Informacion-Aula 420-maestro: Luis Fernando Lopez",
]
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
    nombre_alumno = input("Cual es el nombre del alumno que deseas eliminar?: ")
    for alumno in lista_alumnos:
        if nombre_alumno.lower() in alumno.lower():
            lista_alumnos.remove(alumno)
            print(f"El alumno {nombre_alumno} ha sido eliminado exitosamente")
            mostrar_menu()
    print("El alumno no se encuentra en la lista")
def agregar_alumno():
    nuevo_alumno = input("Cual es el nombre del alumno que deseas agregar?: ")
    curso_alumno = input("Cual es el curso del alumno?: ")
    alumno_completo = f"{nuevo_alumno}:{curso_alumno}"
    lista_alumnos.append(alumno_completo)
    print(f"El alumno {nuevo_alumno} ha sido agregado exitosamente")
    mostrar_menu()
    return alumno_completo
def modificar_alumno():
    nombre_alumno = input("Cual es el nombre del alumno que deseas modificar?: ")
    for i, alumno in enumerate(lista_alumnos):
        if nombre_alumno.lower() in alumno.lower():
            nuevo_nombre = input("Cual es el nuevo nombre del alumno?: ")
            curso_alumno = input("Cual es el curso del alumno?: ")
            lista_alumnos[i] = f"{nuevo_nombre}:{curso_alumno}"
            print(f"El alumno {nombre_alumno} ha sido modificado exitosamente")
            mostrar_menu()
            return lista_alumnos[i]
    print("El alumno no se encuentra en la lista")
def agregar_curso():
    nuevo_curso = input("Cual curso deseas agregar?: (nombre de la materia,aula y nombre del maestro) ")
    cursos.append(nuevo_curso)
    print("El curso ha sido agregado exitosamente")
    print("======================================")
    print(cursos)
    print("=======================================")
    mostrar_menu()
    return nuevo_curso
def eliminar_curso():
    curso_a_eliminar = input("Cual curso deseas eliminar?: ")
    if curso_a_eliminar in cursos:
        cursos.remove(curso_a_eliminar)
        print("El curso ha sido eliminado exitosamente")
    else:
        print("El curso no se encuentra en la lista")
    mostrar_menu()
    return curso_a_eliminar
def modificar_curso():
    curso_a_modificar = input("Cual curso deseas modificar?: ")
    if curso_a_modificar in cursos:
        nuevo_nombre_curso = input("Cual es el nuevo nombre del curso?: ")
        indice = cursos.index(curso_a_modificar)
        cursos[indice] = nuevo_nombre_curso
        print("El curso ha sido modificado exitosamente")
    else:
        print("El curso no se encuentra en la lista")
    mostrar_menu()
    return curso_a_modificar
def mostrar_cursos():
    print("================================")
    for curso in cursos:
        print(curso)
    print("================================")
    menu_principal = input("Desea regresar al menu principal? (si/no): ")
    if menu_principal.lower() == "si":
        mostrar_menu()
def mostrar_alumnos():
    print("================================")
    for alumno in lista_alumnos:
        print(alumno)
    print("================================")
    menu_principal = input("Desea regresar al menu principal? (si/no): ")
    if menu_principal.lower() == "si":
        mostrar_menu()
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
def mostrar_cursos_y_alumnos():
    print("=============================================")
    mostrar_cursos()
    print ("=============================================")
    mostrar_alumnos()
    print("=============================================")
def mostrar_menu():
    print("Seleccione una opcion:")
    print("1. Mostrar cursos")
    print("2. Agregar curso")
    print("3. Eliminar curso")
    print("4. Modificar curso")
    print("5. Mostrar alumnos")
    print("6. Agregar alumno")
    print("7. Eliminar alumno")
    print("8. Modificar alumno")
    print("9. Contar alumnos por curso")
    print("10. Mostrar cursos y alumnos")
    print("11. Salir")
    opcion = int(input("que opcion desea el ejecutar? "))
    if opcion == "":
        print("Opcion no valida, por favor intente de nuevo.")
        mostrar_menu()
        return
    if opcion>11 or opcion<1:
        print("Opcion no valida, por favor intente de nuevo.")
        mostrar_menu()
        return
    if opcion < 1 or opcion > 11:
        print("Opcion no valida, por favor intente de nuevo.")
        mostrar_menu()
        return

    if opcion == 1:
        mostrar_cursos()
    elif opcion == 2:
        agregar_curso()
    elif opcion == 3:
        eliminar_curso()
    elif opcion == 4:
        modificar_curso()
    elif opcion == 5:
        mostrar_alumnos()
    elif opcion == 6:
        agregar_alumno()
    elif opcion == 7:
        eliminar_alumno()
    elif opcion == 8:
        modificar_alumno()
    elif opcion == 9:
        contar_alumnos_por_curso()
    elif opcion == 10:
        mostrar_cursos_y_alumnos()
    elif opcion == 11:
        salir()
def salir():
    print("Saliendo del programa...")
print("""//////////////////////////////////
      Bienvenido al menu
      /////////////////////////////////////""")
mostrar_menu()
print("///////////////////////////////////////////////////")