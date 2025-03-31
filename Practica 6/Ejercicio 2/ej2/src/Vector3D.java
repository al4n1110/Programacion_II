public class Vector3D {
    private double a1;
    private double a2;
    private double a3;

    // Constructor
    public Vector3D(double a1, double a2, double a3) {
        this.a1 = a1;
        this.a2 = a2;
        this.a3 = a3;
    }

    // Método para obtener la suma de dos vectores
    public Vector3D suma(Vector3D otro) {
        return new Vector3D(this.a1 + otro.a1, this.a2 + otro.a2, this.a3 + otro.a3);
    }

    // Método para multiplicar un vector por un escalar
    public Vector3D multiplicacion(double escalar) {
        return new Vector3D(this.a1 * escalar, this.a2 * escalar, this.a3 * escalar);
    }

    // Método para obtener la longitud de un vector
    public double longitud() {
        return Math.sqrt(a1 * a1 + a2 * a2 + a3 * a3);
    }

    // Método para normalizar un vector
    public Vector3D normal() {
        double longitud = this.longitud();
        return new Vector3D(a1 / longitud, a2 / longitud, a3 / longitud);
    }

    // Método para obtener el producto escalar de dos vectores
    public double productoEscalar(Vector3D otro) {
        return this.a1 * otro.a1 + this.a2 * otro.a2 + this.a3 * otro.a3;
    }

    // Método para obtener el producto vectorial de dos vectores
    public Vector3D productoVectorial(Vector3D otro) {
        double nuevoA1 = this.a2 * otro.a3 - this.a3 * otro.a2;
        double nuevoA2 = this.a3 * otro.a1 - this.a1 * otro.a3;
        double nuevoA3 = this.a1 * otro.a2 - this.a2 * otro.a1;
        return new Vector3D(nuevoA1, nuevoA2, nuevoA3);
    }

    // Método para obtener la proyección ortogonal de un vector sobre otro
    public Vector3D proyeccionOrtogonal(Vector3D otro) {
        double punto = this.productoEscalar(otro);
        double magnitudCuadrado = otro.longitud() * otro.longitud();
        return otro.multiplicacion(punto / magnitudCuadrado);
    }

    // Método para obtener la componente 
    public double componente(Vector3D otro) {
        return this.productoEscalar(otro) / otro.longitud();
    }

    public String toString() {
        return "("+ a1 + ", " + a2 + ", " + a3 +")";
    }

    // Métodos de acceso (getters) para las componentes
    public double getA1() {
        return a1; 
    }
    public double getA2() {
        return a2; 
    }
    public double getA3() {
        return a3; 
    }
}
