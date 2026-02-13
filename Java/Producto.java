import java.util.Scanner;

public class Producto{
    static void main(String[] args) {

        
        //  Scanner para leer datos
        Scanner entrada = new Scanner(System.in);

        // Declaración de variables
        String nombre;
        int existencias;
        double precio;

        //aqui se busca que ingrese el nombre del producto
        System.out.print("Ingresa el nombre del producto: ");

        //aqui se toma lo que escribio y se manda a la variable

        nombre = entrada.nextLine();

        System.out.print("Ingresa el número de existencias: ");
        //lo mimso pero ahora se pone int por que es un valor numerico
        existencias = entrada.nextInt();

        System.out.print("Ingresa el precio del producto: ");
        //se usa double por si se utilizan centavos
        precio = entrada.nextDouble();

        // Mostrar información
        System.out.println("\nInformación de producto registrado");
        //aqui se concatena bro
        System.out.println("Nombre: " + nombre);
        System.out.println("Existencias: " + existencias);
        System.out.println("Precio: $ " + precio);

        entrada.close();
    }
}
