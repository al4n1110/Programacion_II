import javax.swing.JFrame;

public class Main {
    public static void main(String[] args) {
        /* Iniciando PUNTO */
        Punto punto1 = new Punto((float) 2.5, (float) 3.2);
        System.out.println("----PUNTO");
        System.out.println(punto1.coord_cartesianas());
        System.out.println(punto1.coord_polares());
        System.out.println(punto1.toString());

        /* Iniciando LINEA */
        JFrame frame = new JFrame("LINEA");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 800);

        Punto p1 = new Punto(360, (float) 70.5);
        Punto p2 = new Punto(550, 400);
        Linea linea = new Linea(p1, p2);

        System.out.println("---LINEA");
        System.out.println(linea.toString());

        PanelDibujo panelLinea = new PanelDibujo(linea);
        frame.add(panelLinea);
        frame.setVisible(true);

        /* Iniciando CIRCULO */
        JFrame frame2 = new JFrame("CIRCULO");
        frame2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame2.setSize(800, 800);

        Punto centro = new Punto(300, 250);
        Circulo circulo = new Circulo(centro, 100);

        System.out.println("---CIRCULO");
        System.out.println(circulo.toString());

        PanelDibujo panelCirculo = new PanelDibujo(circulo);
        frame2.add(panelCirculo);
        frame2.setVisible(true);
    }
}
