public class D implements A,B {
    private int x,y,z;
    
    public D(int x, int y , int z){
        this.x = x;
        this.y = y;
        this.z = z;
    }

    @Override
    public void incrementarXZ(){
        this.x ++;
        this.z ++;
        System.out.println("x: " + this.x + ", z: " + this.z);
    }

    @Override
    public void incrementarYZ(){
        this.y ++;
        this.z ++;
        System.out.println("y: " + this.y + ", z: " + this.z);
    }
    
    @Override
    public void incrementarZ(){
        this.z ++;
        System.out.println("z:"+ this.z);
    }

    public void incrementarXYZ(){
        this.x ++;
        this.y ++;
        this.z ++;
        System.out.println("x: " + this.x + ", y:" + this.y  + ", z: " + this.z);
    }
}
