public class Dispositivo {
  private String serie;
  private String modelo;
  private boolean encendido;
  public Dispositivo() {
    this.serie = "";
    this.modelo = "";
    this.encendido = false;
  }
  public Dispositivo(String serie, String modelo) {
    this.serie = serie;
    this.modelo = modelo;
    this.encendido = false;
  }
  public String getSerie() {
    return this.serie;
  }
  public String getModelo() {
    return this.modelo;
  }
  public boolean getEncendido() {
    return this.encendido;
  }
  public void setSerie(String serie) {
    this.serie = serie;
  }
  public void setModelo(String modelo) {
    this.modelo = modelo;
  }
  public void encender() {
    if (this.encendido) {
      System.out.println("El dispositivo " + this.modelo + " ya se encuentra encendido.");
    } else {
      this.encendido = true;
      System.out.println("Encendiendo... " + this.toString());
    }
  }
  public void apagar() {
    if (!this.encendido) {
      System.out.println("El dispositivo " + this.modelo + " ya se encuentra apagado.");
    } else {
      this.encendido = false;
      System.out.println("Apagando... " + this.toString());
    }
  }
  public boolean equals(Object otroObjeto) {
    if (otroObjeto == null || getClass() != otroObjeto.getClass()) return false;
    Dispositivo otro = (Dispositivo) otroObjeto;
    return this.serie.equals(otro.serie);
  }
  public int hashCode() {
    return serie != null ? serie.hashCode() : 0;
  }
  public String toString() {
    return "[Dispositivo -> Serie: " + serie + ", Modelo: " + modelo + ", Estado: " + (encendido ? "Encendido" : "Apagado") + "]";
  }
}