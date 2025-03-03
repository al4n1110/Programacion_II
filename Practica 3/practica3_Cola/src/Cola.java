public class Cola {
    private long [] arreglo;
    private int inicio;
    private int fin;
    private int n;
    public Cola(int n){
        this.n = n;
        this.arreglo = new long[n];
        this.inicio = -1;
        this.fin = -1;
    }
    public void insert(long e){
        if(!this.isFull()){
            this.fin++;
            this.arreglo[this.fin] = e;
        }else{
            System.out.println("Cola llena");
        }
    }
    public long remove(){
        if(!isEmpty()){
            this.inicio++;
            long elemento = this.arreglo[this.inicio];
            return elemento;
        }else{
            System.out.println("Cola vacia");
            return -1;
        }
    }
    public long peek(){
        return this.arreglo[this.inicio+1];
    }
    public boolean isEmpty(){
        return this.inicio == this.fin;
    }
    public boolean isFull(){
        return this.fin == this.n-1;
    }
    public int size(){
        if(!isEmpty()){
            this.fin++;
            return this.fin;
        }else{
            System.out.println("Cola vacia");
            return -1;
        }
    }
    
}
