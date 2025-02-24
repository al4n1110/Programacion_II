import java.text.DecimalFormat;

public class Punto {
    float x;
    float y;
    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }
    public String coord_cartesianas(){
        DecimalFormat df = new DecimalFormat();
        return "Las coordenadas en x:"+ df.format(this.x) +", Las coordenadas en y:"+ df.format(this.y);
    }
    public String coord_polares(){
        float radio = (float) Math.sqrt(Math.pow(this.x, 2)  + Math.pow(this.y, 2));
        float angulo = (float) (Math.toDegrees(Math.atan2(this.y, this.x )));
        return "Radio:"+String.format("%.2f", radio)+", Angulo:"+angulo;
    }
    public String toString(){
        DecimalFormat df = new DecimalFormat();
        return "Punto:"+"("+ df.format(this.x) +","+ df.format(this.y) +")";
    }
}
