import java.util.Scanner;

public class Venta {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n;
        String nombre;
        double totalCompra;
        double totalConDescuento;
        double totalGeneral = 0;

        String clienteMayor = "";
        double mayorPago = 0;

        System.out.print("¿Cuántos clientes son?: ");
        n = sc.nextInt();
        sc.nextLine();

        System.out.println("\n--- LISTADO DE CLIENTES ---");

        for (int i = 1; i <= n; i++) {

            System.out.println("\nCliente #" + i);

            System.out.print("Nombre: ");
            nombre = sc.nextLine();

            System.out.print("Total de la compra: ");
            totalCompra = sc.nextDouble();
            sc.nextLine();
            totalConDescuento = totalCompra * 0.80;

            System.out.println("Total a pagar con descuento: $" + totalConDescuento);

            totalGeneral = totalGeneral + totalConDescuento;

            if (totalConDescuento > mayorPago) {
                mayorPago = totalConDescuento;
                clienteMayor = nombre;
            }
        }

        System.out.println("\n--- RESULTADOS FINALES ---");
        System.out.println("Total a pagar entre todos los clientes: $" + totalGeneral);
        System.out.println("Cliente que pagó más: " + clienteMayor);
        System.out.println("Monto pagado: $" + mayorPago);


    }
}