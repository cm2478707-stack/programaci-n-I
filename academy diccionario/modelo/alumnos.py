from modelo import curso
lista_alumnos={
    '8671':{
        "nombre":"Jose Torre Armando",
        "Edad" : 18,
        "semestre":1,
        "carrera": "Ingenieria en Sistemas Computacionales"
    },
    '8134':{
        "nombre":"Monge Velazquez",
        "edad":18,
        "semestre":1,
        "carrera":"Ingenieria en Tecnologias de la Informacion"
    },
    '7124':{
        "nombre":"Isaias Quintero",
        "edad":18,
        "semestre":1,
        "carrera":"Ingenieria en Gestion Empresarial"
    },
    '1734':{
        "nombre":"Gerardo Martinez",
        "edad":18,
        "semestre":1,
        "carrera":"Ingenieria en Sistemas Computacionales"
    },
}
def eliminar_alumno():
    print(lista_alumnos)
    nombre_alumno = int(input("Cual es el id del alumno que deseas eliminar?: "))
    id_eliminar=(nombre_alumno)
    if id_eliminar in lista_alumnos:
        del lista_alumnos[id_eliminar]
        print("====EXITOSO=======")
        print(lista_alumnos)
        print("=======================================")
    else:
        print("No se encontro el alumno")       
def agregar_alumno():
    uid=int(input("ingrese el uid: "))
    nombres=input("ingrese el nombre sin numerO: ")
    edads=int((input("ingrese el edad del alumno: ")))
    semestres=int(input("semestre: "))
    carreras=input("ingrese la carrera: ")
    datos_nuevo_alumno={    
        "nombre":nombres,
        "edad":edads,
        "semestre":semestres,
        "carrera":carreras
    }
    lista_alumnos[uid]=datos_nuevo_alumno
    print(lista_alumnos)
def modificar_alumno():
    id=int(input("ingrese el ID del alumno: "))
    if id in lista_alumnos:
        nombre=input("ingrese el nuevo nombre del alumno: ")
        edad=int(input("ingrese la edad del alumno: "))
        semestre=int(input("ingrese el semestre del alumno: "))
        carrera=input("ingrese la carrera del alumno: ")
        nuevo_alumno_modificado={
            "nombre":nombre,
            "edad":edad,
            "semestre":semestre,
            "carrera":carrera
        }
        lista_alumnos[id] = nuevo_alumno_modificado
        print("""==========A SDO MODIFICADO==============""")
        print(lista_alumnos)
        print("===========================================")
    else:
        print("No se encontro el usuario ")
def mostrar_alumnos():
    print("================================")
    print(lista_alumnos)
    print("================================")
def mostrar_cursos_y_alumnos():
    print("=============================================")
    curso.mostrar_cursos()
    print ("=============================================")
    mostrar_alumnos()
    print("=============================================")