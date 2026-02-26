public class Main {
    public static void main(String[] args) {
        // 1. Instanciar objetos
        Auto miAuto = new Auto("Toyota", "Corolla", 45.50, 4);
        Motocicleta miMoto = new Motocicleta("Kawasaki", "H2R", 65.00, 1000);

        // 2. Verificar la herencia (mostrarDetalles funciona para ambos adaptándose a su tipo)
        miAuto.mostrarDetalles();
        System.out.println(); // Salto de línea por estética
        miMoto.mostrarDetalles();
        System.out.println();

        // 3. Comprobar la validación de la regla de negocio (Encapsulamiento)
        System.out.println(">>> Intentando modificar la tarifa de la moto a un valor negativo (-15.0)...");
        miMoto.setTarifaDiaria(-15.0);
        System.out.println("\n>>> Verificando que el valor no cambió:");
        miMoto.mostrarDetalles();
    }
}