import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
public class Circulo {
    public Punto centro;
    public float radio;
    public Circulo(Punto centro , float radio){
        this.centro = centro;
        this.radio = radio;
    }
    @Override
    public String toString(){
        return "Centro:"+this.centro+","+" Radio:"+this.radio;
    }
    public void dibujarCirculo(Graphics2D g2d) {
        g2d.draw(new Ellipse2D.Float(centro.x - radio, centro.y - radio, radio * 2, radio * 2));
    }
}
