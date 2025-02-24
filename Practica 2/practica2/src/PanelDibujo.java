import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JPanel;

class PanelDibujo extends JPanel {
    private Linea linea;
    private Circulo circulo;

    public PanelDibujo(Linea linea) {
        this.linea = linea;
    }
    
    public PanelDibujo(Circulo circulo) {
        this.circulo = circulo;
    }
    
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        if (linea != null) {
            linea.dibujarLinea(g2d);
        }
        if (circulo != null) {
            circulo.dibujarCirculo(g2d); 
        }
    }
}
