public class Motocicleta extends Vehiculo {
    private int cilindraje;

    // Constructor utilizando super()
    public Motocicleta(String marca, String modelo, double tarifaDiaria, int cilindraje) {
        super(marca, modelo, tarifaDiaria);
        this.cilindraje = cilindraje;
    }

    // Sobrescritura del método
    @Override
    public void mostrarDetalles() {
        System.out.println("--- Detalles de la Motocicleta ---");
        super.mostrarDetalles(); // Llama al método de la clase padre
        System.out.println("Cilindraje: " + cilindraje + "cc");
    }
}