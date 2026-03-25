import java.util.Scanner;

public class numerocorrecto{
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);

        while(true){
            System.out.println("ingresa un numero: ");
            try{
                long numero= Long.parseLong(scanner.nextLine());

                if (numero>2_147_483_647){
                    throw new ArithmeticException("El numero supera el valor maximo (2,147,483,647");
                }

                System.out.println("numero valido "+numero);
                break;

            }catch (NumberFormatException e){
                System.out.println("Errorrrrrr solo se pueden numeros no letras");
            }catch (ArithmeticException e){
                System.out.println("Error");
            }finally {
                System.out.println(("bye bye bye mpgger"));
            }
        }

        scanner.close();

    }
}