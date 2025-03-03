
import java.awt.Graphics2D;
import java.awt.geom.Line2D;

public class Linea {
    public Punto p1;
    public Punto p2;
    public Linea(Punto p1, Punto p2){
        this.p1 = p1;
        this.p2 = p2;
    }
    public String toString(){
        return"Punto1:"+this.p1+","+"Punto2:"+this.p2;
    }
    public void dibujarLinea(Graphics2D g2d) {
        g2d.draw(new Line2D.Float(p1.x, p1.y, p2.x, p2.y));
    }
    
}
