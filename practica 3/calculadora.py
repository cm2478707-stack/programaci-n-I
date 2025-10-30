while True:
    print("Bienvenido a la calculadora")
    print("1.sumar")
    print("2.restar")
    print("3.multiplicar")
    print("4.dividir")
    print("5.salir")
    opcion = input("Elige una opcion (1/2/3/4/5): ")
    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        if opcion == '1':
            print(num1, "+", num2, "=", num1 + num2)
        elif opcion == '2':
            print(num1, "-", num2, "=", num1 - num2)
        elif opcion == '3':
            print(num1, "*", num2, "=", num1 * num2)
        elif opcion == '4':
            if num2 != 0:
                print(num1, "/", num2, "=", num1 / num2)
            else:
                print("Error: Division por cero no es permitida.")
    elif opcion == "5":
        print("Saliendo de la calculadora. Adios!")
        break
  

