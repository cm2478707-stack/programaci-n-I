from modelo import curso
from modelo import alumnos 
def mostrar_menu():
    while True: 
        print("Seleccione una opcion:")
        print("1. Mostrar cursos")
        print("2. Agregar curso")
        print("3. Eliminar curso")
        print("4. Modificar curso")
        print("5. Mostrar alumnos")
        print("6. Agregar alumno")
        print("7. Eliminar alumno")
        print("8. Modificar alumno")
        print("9.mostrar cursos y alumnos")
        print("10. salir")
        entrada = input("que opcion desea el ejecutar? ")
        try:
            opcion = int(entrada)
        except ValueError:
            print("Opcion no valida, por favor intente de nuevo.")
            continue 
        if opcion < 1 or opcion > 11:
            print("Opcion no valida, por favor intente de nuevo.")
            continue 
        if opcion == 1:
            curso.mostrar_cursos()
        elif opcion == 2:
            curso.agregar_curso()
        elif opcion == 3:
            curso.eliminar_curso()
        elif opcion == 4:
            curso.modificar_curso()
        elif opcion == 5:
            alumnos.mostrar_alumnos()
        elif opcion == 6:
            alumnos.agregar_alumno()
        elif opcion == 7:
            alumnos.eliminar_alumno()
        elif opcion == 8:
            alumnos.modificar_alumno()
        elif opcion == 9:
            alumnos.mostrar_cursos_y_alumnos()
        elif opcion == 10:
            print("Saliendo del programa...")
            break 
print("""//////////////////////////////////
      Bienvenido al menu nuevo super good meow
      /////////////////////////////////////""")
mostrar_menu()
print("///////////////////////////////////////////////////")