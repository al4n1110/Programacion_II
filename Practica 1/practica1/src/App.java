public class App {
    public static void main(String[] args) throws Exception {
        Punto p1 = new Punto(5, 5);
        System.out.println(p1.coord_cartesianas());
        System.out.println(p1.coord_polares());
        System.out.println(p1.toString());
    }
}
