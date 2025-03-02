public class Pila {
    private long [] arreglo;
    private int top;
    private int n;
    public Pila(int n){
        this.n = n;
        this.arreglo = new long[n];
        this.top = -1;
    }
    public void push(long e){
        if(!this.isFull()){
            this.top++;
            this.arreglo[this.top] = e;
        }else{
            System.out.println("Pila llena");
        }
    }
    public long pop(){
        if(!isEmpty()){
            long elemento = this.arreglo[this.top];
            return elemento;
        }else{
            System.out.println("Pila vacia");
            return -1;
        }
    }
    public long peek(){
        return this.arreglo[this.top];
    }
    public boolean isEmpty(){
        return this.top == -1;
    }
    public boolean isFull(){
        return this.top == n-1;
    }
}
