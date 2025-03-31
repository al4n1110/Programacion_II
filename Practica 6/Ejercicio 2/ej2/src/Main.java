public class Main {
    public static void main(String[] args) throws Exception {
        Vector3D a = new Vector3D(1, 2, 3);
        Vector3D b = new Vector3D(4, 5, 6);

        // Sumar los vectores
        Vector3D sumaResultado = a.suma(b);
        System.out.println("Suma de a y b: " + sumaResultado);

        // Multiplicar el vector a por un escalar
        Vector3D multiplicacionResultado = a.multiplicacion(2);
        System.out.println("Multiplicación de a por 2: " + multiplicacionResultado);

        // Longitud del vector a
        double longitudA = a.longitud();
        System.out.println("Longitud de a: " + longitudA);

        // Normalizar el vector a
        Vector3D normalA = a.normal();
        System.out.println("Normalización de a: " + normalA);

        // Producto escalar de a y b
        double productoEscalar = a.productoEscalar(b);
        System.out.println("Producto escalar de a y b: " + productoEscalar);

        // Producto vectorial de a y b
        Vector3D productoVectorial = a.productoVectorial(b);
        System.out.println("Producto vectorial de a y b: " + productoVectorial);

        // Proyección de a sobre b
        Vector3D proyeccion = a.proyeccionOrtogonal(b);
        System.out.println("Proyección de a sobre b: " + proyeccion);

        // Componente de a en la dirección de b
        double componente = a.componente(b);
        System.out.println("Componente de a en la dirección de b: " + componente);
    }
}
