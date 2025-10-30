def new_func():
    nombre= input("ingresa tu nombre: ")
    print("bienvenido a tu examen de programacion basica ", nombre)

    opcion = int(input("""Que estructura de control es mas adecuado para iterar sobre una secuencia de elementos un numero de vecs 
conocido : 
1) Bucle \"para"\  2) Setencia condicional \"Si"\ 3) Bucle \"mientras"\ 4) Ninguna de las anteriores
        """))
    incorrecto = 0
    Correcto = 0
    match opcion:
        case 1:
            print("Correcto")
        case 2:
            print("Incorrecto")
        case 3:
            print("Incorrecto")
        case 4:
            print("Incorrecto")
    if opcion == 1:
        Correcto += 1
    else:
        incorrecto += 1

    opcion2 = int(input("""Que es un algoritmo : 
1) Un conjunto de instrucciones escritas en codigo binario   2) un lenguaje de programacion especifico  3)el codigo fuent de un programa especifico 
 4) una secuencia de pasos ordenados y finitos para resolver un problema
        """))
    match opcion2:
        case 1:
            print("Incorrecto")
        case 2:
            print("Incorrecto")
        case 3:
            print("Incorrecto")
        case 4:
            print("Correcto")
    if opcion2 == 4:
        Correcto += 1
    else:
        incorrecto += 1

    opcion3 = int(input("""el lenguaje maquina esta compuesto por : 
1)simbolos logicos y matematicos  2)pseudocodigo 3)instrucciones en ingles abreviadas  4)codigo binario
        """))
    match opcion3:
        case 1:
            print("Incorrecto")
        case 2:
            print("Incorrecto")
        case 3:
            print("Incorrecto")
        case 4:
            print("Correcto")
    if opcion3 == 4:
        Correcto += 1
    else:
        incorrecto += 1

    opcion4 = int(input("""cual de los siguientes NO es parte fundamental de la aquitectura de von neumann : 
1) memoria  2)CPU 3)Tarjeta Grafica   4)sistema de entrada y salida
        """))
    match opcion4:
        case 1:
            print("Incorrecto")
        case 2:
            print("Incorrecto")
        case 3:
            print("Correcto")
        case 4:
            print("Incorrecto")
    if opcion4 == 3:
        Correcto += 1
    else:
        incorrecto += 1

    opcion5 = int(input("""un lenguaje de programacion de alto nivel es : 
1)ser dificil de aprender y leer 2)ser el mas rapido 3)tener control directo 4)ser independiente de la arquitectura de la computadora
        """))
    match opcion5:
        case 1:
            print("Incorrecto")
        case 2:
            print("Incorrecto")
        case 3:
            print("Incorrecto")
        case 4:
            print("Correcto")
    if opcion5 == 4:
        Correcto += 1
    else:
        incorrecto += 1
    opcion6 = int(input("""el lenguaje java es considerado un lenguaje de nivel:
1)medio 2)bajo 3)muy alto 4)alto
        """))
    match opcion6:
        case 1:
            print("Incorrecto")
        case 2:
            print("Incorrecto")
        case 3:
            print("Incorrecto")
        case 4:
            print("Correcto")
    if opcion6 == 4:
        Correcto += 1
    else:
        incorrecto += 1
    opcion7 = int(input("""un programa de una computadora es esencialmente:
1)una coleccio0n de algoritmos 2)el sistea operativo de una computadora 3)un dispositivo de hardware 
4)una secuencia  de instrucciones que la computadora ejecuta
        """))
    match opcion7:
        case 1:
            print("Incorrecto")
        case 2:
            print("Incorrecto")
        case 3:
            print("Incorrecto")
        case 4:
            print("Correcto")
    if opcion7 == 4:
        Correcto += 1
    else:
        incorrecto += 1
    opcion8 = int(input("""en pseudocodigo, que estructura de control se utiliza para ejecutar un bloque de codigo solo si se cumple 
                    una condcion especifica:
1) condicional o de seleccion 2)repetitiva \"para\" 3)s3ecuencial d)repetitva \"mientras\"
        """))
    match opcion8:
        case 1:
            print("Correcto")
        case 2:
            print("Incorrecto")
        case 3:
            print("Incorrecto")
        case 4:
            print("incorrecto")
    if opcion8 == 1:
        Correcto += 1
    else:
        incorrecto += 1
    opcion9 = int(input("""el proposito principal del pseudocodigo es:
1)traducir automaticamente codigo de alto nivel a lenguaje maquina
2)ejecutar programas mas eficientemente que un lenguaje compilado
3) planificar y describir la logica de un algoritmo de forma legible para los humanos
4) proporcionar un control directo sobre los registros del procesador 
        """))
    match opcion9:
        case 1:
            print("Incorrecto")
        case 2:
            print("Incorrecto")
        case 3:
            print("correcto")
        case 4:
            print("Incorrecto")
    if opcion9 == 3:
        Correcto += 1
    else:
        incorrecto += 1
    opcion10 = int(input("""cual es la principal diferencia entre un bucle \"mientras\" y un bucle \"repetir\" :
1)el bucle \"repetir\" se ejecuta al menos una vez, mientras que el bucle \"mientras\" puede no ejecutarse nunca
2)no hay diferencia, son intercambiables
3)el bucle \"mientras\" es mas rapido que el bucle \"repetir\"
4)el bucle \"repetir\" solo usa numeros, mientras que el bucle \"mientras\" puede usar cualquier tipo de dato
        """))
    match opcion10:
        case 1:
            print("Correcto")
        case 2:
            print("Incorrecto")
        case 3:
            print("Incorrecto")
        case 4:
            print("incorrecto")
    if opcion10 == 4:
        Correcto += 1
    else:
        incorrecto += 1
    print("has tenido ", (Correcto), " respuestas correctas y ", (incorrecto), " respuestas incorrectas")
    calificacion = (Correcto / 10) * 100
    print("tu calificacion es de : ", (calificacion))
    if calificacion >= 70:
        print("Felicidades has aprobado el examen", nombre)
    else:   
        print("Lo siento, has reprobado el examen", nombre)

new_func()