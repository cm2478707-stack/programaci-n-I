public class Vehiculo {
    // Atributos  privados (Encapsulamiento)
    private String marca;
    private String modelo;
    private double tarifaDiaria;

    public Vehiculo(String marca, String modelo, double tarifaDiaria) {
        this.marca = marca;
        this.modelo = modelo;
        // Validamos desde la creación del objeto
        if (tarifaDiaria >= 0) {
            this.tarifaDiaria = tarifaDiaria;
        } else {
            System.out.println("Error: La tarifa inicial no puede ser negativa. Se establecerá en 0.0");
            this.tarifaDiaria = 0.0;
        }
    }

    public String getMarca() { return marca; }
    public String getModelo() { return modelo; }
    public double getTarifaDiaria() { return tarifaDiaria; }

    public void setMarca(String marca) { this.marca = marca; }
    public void setModelo(String modelo) { this.modelo = modelo; }

    // Setter con regla de validación
    public void setTarifaDiaria(double tarifaDiaria) {
        if (tarifaDiaria < 0) {
            System.out.println("Error: La tarifa diaria no puede ser negativa. Se mantiene el valor actual ($" + this.tarifaDiaria + ").");
        } else {
            this.tarifaDiaria = tarifaDiaria;
        }
    }

    // Método para imprimir detalles
    public void mostrarDetalles() {
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Tarifa Diaria: $" + tarifaDiaria);
    }
}