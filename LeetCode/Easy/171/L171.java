import java.util.Scanner;


public class L171 {

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String letras = input.nextLine().toUpperCase();
        int resultado = 0;
        for(int i = 0; i < letras.length();i++){
            char letra = letras.charAt(i);

            if (letra >= 'A' && letra <= 'Z') {
                resultado = resultado * 26 + (letra -  'A' + 1);
            }
        }
        System.out.println(letras + " = " + resultado);
        input.close();
        
    }
}
