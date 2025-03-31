public class App {
    public static void main(String[] args) throws Exception {
        AlgebraVectorial av = new AlgebraVectorial();
        AlgebraVectorial av2 = new AlgebraVectorial(new double[]{1, 0, 0}, new double[]{0, 1, 0});
        av2.perpendicular();
        av.perpendicular(new double[]{1,1, 1}, new double[]{2, 3, 4});
        av.perpendicular(new float[]{3, -2, 1}, new float[]{2, 3, 4});
        av.perpendicular(new double[]{1, 2, 4}, new float[]{2, 4, 8});
        av.paralela(new double[]{2,4,6}, new double[]{1,2,3});
        av.paralela(new float[]{1,1,1}, new double[]{1,2,3});
        av.proyeccion(new double[]{3,4,5}, new double[]{1,2,3});
        av.componente(new double[]{3,4,5}, new double[]{1,2,3});
    }
}
