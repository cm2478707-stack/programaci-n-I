import java.util.Scanner;

public class tabla {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero;

        while (true) {
            System.out.print("\nIngrese un numero entre 1 y 99 (o introduzca -1 para salir): ");
            numero = scanner.nextInt();
            if (numero == -1) {
                System.out.println("Saliendo del programa... ¡Hasta luego!");
                break;
            }


            if (numero < 1 || numero > 99) {
                System.out.println("Error: El numero esta fuera del rango permitido. Intente nuevamente.");
            } else {
                // 3. Generación de la tabla de multiplicar hasta el 10
                System.out.println("\n--- Tabla de multiplicar del " + numero + " ---");
                for (int i = 1; i <= 10; i++) {
                    System.out.println(numero + " x " + i + " = " + (numero * i));
                }
            }
        }

        scanner.close();
    }
}