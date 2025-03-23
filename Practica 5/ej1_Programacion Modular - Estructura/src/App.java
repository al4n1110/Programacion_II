//Algebra:Ecuaciones cuadraticas
import java.util.Scanner;
public class App {
    public static float getDiscriminante(double a , double b , double c){
        float res = (float)(Math.pow(b, 2) - (4 * a * c));
        return res;
    }
    public static double getRaiz1(double a , double b , double c , double discriminante){
            return ((- b + (Math.sqrt(discriminante)))/ 2 * a);
    }

        public static double getRaiz2(double a , double b , double c , float discriminante){
                return ((- b - (Math.sqrt(discriminante))) / 2 * a );

}
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        double a,b,c;
        System.out.println("Ingrese el valor de a:");
        a = sc.nextDouble();
        System.out.println("Ingrese el valor de b:");
        b= sc.nextDouble();
        System.out.println("Ingrese el valor de c:");
        c = sc.nextDouble();
        if(getDiscriminante( a, b, c) > 0 ){
            System.out.println("La ecuacion tiene dos raices:"+String.format("%.2f",  getRaiz1(a, b, c, getDiscriminante(a, b, c))) + " y "+ String.format("%.2f",  getRaiz2(a, b, c, getDiscriminante(a, b, c))));
        }else if(getDiscriminante(a, b, c) == 0 ){
            if(getRaiz1(a, b, c, getDiscriminante(a, b, c)) <= 0 ){
                System.out.println("La ecuacion solo tiene una raiz" + String.format("%.2f", getRaiz1(a, b, c, getDiscriminante(a, b, c))));
            }else if(getRaiz2(a, b, c, getDiscriminante(a, b, c)) <= 0 ){
                System.out.println("La ecuacion solo tiene una raiz:" + String.format("%.2f", getRaiz2(a, b, c, getDiscriminante(a, b, c))));
            }
        }else{
            System.out.println("La ecuacion no tiene soluciones reales");
        }
    }
}
