public class FiguraGeometrica {
    //Area de un circulo
    public double area(double radio){
        return (Math.PI * (Math.pow(radio, 2)));
    }
    //Area de un rectangulo
    public double area(double base , double altura){
        return base * altura;
    }
    //Area de un Triangulko rectangulo
    public double area(double base , float altura){
        return (base * altura)/2;
    }
    //Area de un trapecio
    public double area(double base_M , double base_m, double altura){
        return ((base_M + base_m)*altura)/2;
    }
    //Area de un pentagono
    public double area(float Perimetro , double apotema){
        return (Perimetro * apotema)/2;
    }
}
