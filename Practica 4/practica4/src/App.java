public class App {
    public static void main(String[] args) throws Exception {
        FiguraGeometrica f1 = new FiguraGeometrica();
        FiguraGeometrica f2 = new FiguraGeometrica();
        FiguraGeometrica f3 = new FiguraGeometrica();
        FiguraGeometrica f4 = new FiguraGeometrica();
        FiguraGeometrica f5 = new FiguraGeometrica();
        System.out.println("Area del circulo:" +f1.area(25));
        System.out.println("Area del rectangulo:" +f2.area(15.5 , 20));
        System.out.println("Area de triangulo rectangulo:" +f3.area(25.6 , 12.7));
        System.out.println("Area de trapecio:" +f4.area(10,30,25));
        System.out.println("Area del pentagono:" +f5.area(32,33));
    }
}
