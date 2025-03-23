import java.util.Scanner;
public class EcuacionCuadratica {
    Scanner sc = new Scanner(System.in);
    public double a;
    public double b;
    public double c;
    public EcuacionCuadratica(){
        System.out.println("Ingrese el valor de a:");
        this.a = sc.nextDouble();
        System.out.println("Ingrese el valor de b:");
        this.b = sc.nextDouble();
        System.out.println("Ingrese el valor de c:");
        this.c = sc.nextDouble();
    }
    public  float getDiscriminante(){
        float res = (float)(Math.pow(this.b, 2) - (4 * this.a * this.c));
        return res;
    }
    public  double getRaiz1(double discriminante){
        return ((- this.b + (Math.sqrt(discriminante)))/ 2 * this.a);
    }

    public  double getRaiz2(float discriminante){
        return ((- this.b - (Math.sqrt(discriminante))) / 2 * this.a );
}
}
