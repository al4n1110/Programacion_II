public class App {
    public static void main(String[] args) throws Exception {
        Cola cola1 = new Cola(5);
        cola1.insert(12);
        cola1.insert(15);
        cola1.insert(20);
        cola1.insert(30);

        System.out.println(cola1.peek());
        System.out.println(cola1.isEmpty());
        System.out.println(cola1.isFull());
        System.out.println(cola1.size());
        System.out.println(cola1.remove());
    }
}
