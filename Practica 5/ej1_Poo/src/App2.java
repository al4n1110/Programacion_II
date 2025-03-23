public class App2 {
    public static void main(String[] args) throws Exception {
        EcuacionCuadratica ecuacion1 = new EcuacionCuadratica();
        if(ecuacion1.getDiscriminante() > 0 ){
            System.out.println("La ecuacion tiene dos raices:"+String.format("%.2f", ecuacion1.getRaiz1(ecuacion1.getDiscriminante())) + " y "+ String.format("%.2f",  ecuacion1.getRaiz2(ecuacion1.getDiscriminante())));
        }else if(ecuacion1.getDiscriminante() == 0 ){
            if(ecuacion1.getRaiz1(ecuacion1.getDiscriminante()) <= 0 ){
                System.out.println("La ecuacion solo tiene una raiz" + String.format("%.2f", ecuacion1.getRaiz1(ecuacion1.getDiscriminante())));
            }else if(ecuacion1.getRaiz2(ecuacion1.getDiscriminante()) <= 0 ){
                System.out.println("La ecuacion solo tiene una raiz:" + String.format("%.2f", ecuacion1.getRaiz2(ecuacion1.getDiscriminante())));
            }
        }else{
            System.out.println("La ecuacion no tiene soluciones reales");
        }
    
    }
}
