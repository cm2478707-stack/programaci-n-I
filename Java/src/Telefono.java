public class Telefono extends Dispositivo {
    private String numeroTelefonico;
    private boolean ocupado;
    private String numeroEnLlamada;
    public Telefono(Dispositivo dispositivo, String numeroTelefonico) {
        super(dispositivo.getSerie(), dispositivo.getModelo());
        if(dispositivo.getEncendido()) this.encender();
        this.numeroTelefonico = numeroTelefonico;
        this.ocupado = false;
        this.numeroEnLlamada = "";
    }
    public Telefono(String numeroTelefonico, String serie, String modelo) {
        super(serie, modelo);
        this.numeroTelefonico = numeroTelefonico;
        this.ocupado = false;
        this.numeroEnLlamada = "";
    }
    public String getNumeroTelefonico() {
        return this.numeroTelefonico;
    }
    public void setNumeroTelefono(String numeroTelefonico) {
        this.numeroTelefonico = numeroTelefonico;
    }
    public void llamar(String numero) {
        if (!this.getEncendido()) {
            System.out.println("Error: No se puede llamar, el teléfono está apagado.");
            return;
        }
        if (this.ocupado) {
            System.out.println("Error: No se puede llamar, el teléfono ya está ocupado.");
            return; // Termina la ejecución del método
        }
        this.ocupado = true;
        this.numeroEnLlamada = numero;
        System.out.println("Llamando a " + numero + " desde " + this.getModelo());
    }
    public void colgar() {
        if (!this.getEncendido()) {
            System.out.println("Error: No se puede colgar, el teléfono está apagado.");
            return;
        }
        if (!this.ocupado) {
            System.out.println("Error: No se puede colgar porque el teléfono no está ocupado.");
            return;
        }
        System.out.println("Llamada a " + this.numeroEnLlamada + " finalizada");
        this.ocupado = false;
        this.numeroEnLlamada = "";
    }
    public String toString() {
        return super.toString() + " [Teléfono -> Número: " + this.numeroTelefonico + ", Ocupado: " + this.ocupado + "]";
    }
}