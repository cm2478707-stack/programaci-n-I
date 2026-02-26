public class Auto extends Vehiculo {
    private int numeroPuertas;

    // Constructor utilizando super()
    public Auto(String marca, String modelo, double tarifaDiaria, int numeroPuertas) {
        super(marca, modelo, tarifaDiaria);
        this.numeroPuertas = numeroPuertas;
    }

    // Sobrescritura del método (Polimorfismo)
    @Override
    public void mostrarDetalles() {
        System.out.println("--- Detalles del Auto ---");
        super.mostrarDetalles(); // Llama al método de la clase padre
        System.out.println("Número de puertas: " + numeroPuertas);
    }
}