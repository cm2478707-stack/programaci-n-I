import java.util.Random;
public class Reloj extends Dispositivo {
    private float calibracion;
    public Reloj(Dispositivo dispositivo) {
        super(dispositivo.getSerie(), dispositivo.getModelo());
        if(dispositivo.getEncendido()) this.encender();
        this.calibracion = 0.0f;
    }
    public Reloj(float calibracion, String serie, String modelo) {
        super(serie, modelo);
        this.calibracion = calibracion;
    }
    public float getCalibracion() {
        return this.calibracion;
    }
    public void setCalibracion(float calibracion) {
        this.calibracion = calibracion;
    }
    public void setCalibracion() {
        if (this.getEncendido()) {
            Random rand = new Random();
            this.calibracion = rand.nextFloat() * 10;
            System.out.println("Reloj calibrado a: " + this.calibracion);
        } else {
            System.out.println("Error: No se puede calibrar el reloj porque está apagado.");
        }
    }
    public int medirRitmoCardiaco() {
        if (!this.getEncendido()) {
            System.out.println("Error: No se puede medir el ritmo cardiaco, el reloj está apagado.");
            return 0;
        }
        Random rand = new Random();
        int lpm = rand.nextInt(31) + 80;
        System.out.println("Medición de ritmo cardiaco " + lpm + " LPM desde " + this.getModelo());
        return lpm;
    }
    public String toString() {
        return super.toString() + " [Reloj -> Calibración: " + this.calibracion + "]";
    }
}