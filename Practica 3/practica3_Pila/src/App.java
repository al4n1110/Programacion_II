public class App {
    public static void main(String[] args) throws Exception {
        Pila p1 = new Pila(5);
        p1.push(3);
        p1.push(1);
        p1.push(5);
        p1.push(10);

        System.out.println(p1.peek());
        System.out.println(p1.isEmpty());
        System.out.println(p1.isFull());
        System.out.println(p1.pop());
    }
}
