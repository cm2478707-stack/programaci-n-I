public class Main {
    public static void main(String[] args) {
        System.out.println("--- PASO 2: Creando dispositivos ---");
        Dispositivo dispositivo1 = new Dispositivo("111", "Samsung Watch");
        Dispositivo dispositivo2 = new Dispositivo("222", "iPhone 12");
        System.out.println("\n--- PASO 3 y 4: Encender/Apagar ---");
        dispositivo1.encender();
        dispositivo2.apagar();
        System.out.println("\n--- PASO 5: Comparación ---");
        System.out.println("¿Dispositivo 1 y 2 son iguales?: " + dispositivo1.equals(dispositivo2));

        System.out.println("\n--- PASO 6, 7 y 8: Dispositivo 3 ---");
        Dispositivo dispositivo3 = new Dispositivo();
        dispositivo3.setSerie("333");
        dispositivo3.setModelo("Apple Watch ");
        System.out.println(dispositivo3);
        System.out.println("\n--- PASO 9: Dispositivo 4 ---");
        Dispositivo dispositivo4 = new Dispositivo("444", "Samsung Galaxy S24");
        System.out.println("\n--- PASO 11: Creando Relojes ---");
        Reloj reloj1 = new Reloj(7.0f, "555", "Huawei W1");
        Reloj reloj2 = new Reloj(9.0f, "777", "Apple Watch 7");
        System.out.println("\n--- PASO 12 y 13: Encender/Apagar Relojes ---");
        reloj1.encender();
        reloj2.apagar();
        System.out.println("\n--- PASO 14, 15 y 16: Reloj 3 ---");
        Reloj reloj3 = new Reloj(dispositivo3);
        reloj3.encender();
        reloj3.setCalibracion();
        System.out.println(reloj3);
        System.out.println("\n--- PASO 17 y 18: Comparaciones de Relojes ---");
        System.out.println("¿Reloj 1 y Reloj 2 son iguales?: " + reloj1.equals(reloj2));
        System.out.println("¿Dispositivo 3 y Reloj 3 son iguales?: " + dispositivo3.equals(reloj3));
        System.out.println("\n--- PASO 20: Creando Teléfonos ---");
        Telefono telefono1 = new Telefono("6441998877", "888", "Samsung Galaxy S23 uLTRA");
        Telefono telefono2 = new Telefono("6447551122", "999", "Apple iPhone 16 PRO");
        System.out.println("\n--- PASO 21 y 22: Encender/Apagar Teléfonos ---");
        telefono1.encender();
        telefono2.apagar();
        System.out.println("\n--- PASO 23 y 24: Teléfono 3 ---");
        Telefono telefono3 = new Telefono(dispositivo4, "6444887744");
        System.out.println(telefono3);
        System.out.println("\n--- PASO 25, 26 y 27: Funciones de Llamada ---");
        telefono1.llamar("1234567890");
        telefono1.llamar("0987654321");
        telefono1.colgar();

        System.out.println("\n--- PASO 28: Comparación final ---");
        System.out.println("¿Dispositivo 4 y Telefono 3 son iguales?: " + dispositivo4.equals(telefono3));
        System.out.println("\n--- PASO 29 y 30: Arreglo y Polimorfismo ---");
        Dispositivo[] todosLosDispositivos = {
                dispositivo1, dispositivo2, dispositivo3, dispositivo4,
                reloj1, reloj2, reloj3,
                telefono1, telefono2, telefono3
        };
        for (Dispositivo d : todosLosDispositivos) {
            System.out.println(d.toString());
        }
    }
}