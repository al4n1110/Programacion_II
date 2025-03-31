public class AlgebraVectorial {
    private double[] vecA;
    private double[] vecB;

    public AlgebraVectorial(double[] vecA, double[] vecB) {
        this.vecA = vecA;
        this.vecB = vecB;
    }

    public AlgebraVectorial() {
        this.vecA = new double[] { 0, 0, 0 };
        this.vecB = new double[] { 0, 0, 0 };
    }

    // a)
    public void perpendicular() {
        System.out.println("---------(A)-----------");

        System.out.println("Si el vector a es ortogonal o perpendicular a b:");

        double moduloSuma = 0;
        double moduloResta = 0;

        //Calculando el módulo de A + B y A - B
        for (int i = 0; i < vecA.length; i++) {
            moduloSuma += Math.pow(this.vecA[i] + this.vecB[i], 2);
            moduloResta += Math.pow(this.vecA[i] - this.vecB[i], 2);
        }

        moduloSuma = Math.sqrt(moduloSuma);
        moduloResta = Math.sqrt(moduloResta);

        System.out.println("Módulo de A + B: " + moduloSuma);
        System.out.println("Módulo de A - B: " + moduloResta);

        if (moduloSuma == moduloResta) {
            System.out.println("Los vectores son perpendiculares.");
        } else {
            System.out.println("Los vectores no son perpendiculares.");
        }
    }

    // b)
    public void perpendicular(double[] vecA, double[] vecB) {
        System.out.println("---------(B)-----------");

        double moduloA_B = 0;
        double moduloB_A = 0;

        for (int i = 0; i < vecA.length; i++) {
            moduloA_B += Math.pow(vecA[i] - vecB[i], 2);
            moduloB_A += Math.pow(vecB[i] - vecA[i], 2);
        }

        moduloA_B = Math.sqrt(moduloA_B);
        moduloB_A = Math.sqrt(moduloB_A);

        System.out.println("Módulo de A - B: " + moduloA_B);
        System.out.println("Módulo de B - A: " + moduloB_A);

        if (moduloA_B == moduloB_A) {
            System.out.println("Los módulos son iguales, por lo tanto son perpendicualres.");
        } else {
            System.out.println("No son perpendiculares");
        }
    }

    // c)
    public void perpendicular(float[] vecA, float[] vecB) {
        System.out.println("---------(C)-----------");
        System.out.println("Si a es ortogonal a b:");
        double productoEscalar = 0;
        for (int i = 0; i < vecA.length; i++) {
            productoEscalar += this.vecA[i] * this.vecB[i];
        }

        System.out.println("Producto escalar A · B: " + productoEscalar);

        if (productoEscalar == 0) {
            System.out.println("Los vectores son perpendiculares.");
        } else {
            System.out.println("Los vectores no son perpendiculares.");
        }
    }

    // d)
    public void perpendicular(double[] vecA, float[] vecB) {
        System.out.println("---------(D)-----------");
        System.out.println("Si a es ortogonal a b:");

        double modulo = 0;
        double mult = 0;

        for (int i = 0; i < vecA.length; i++) {
            modulo = Math.pow(2, (Math.sqrt(Math.pow(2, vecA[i]) - Math.pow(2, vecB[i]))));
            mult = Math.pow(Math.pow(Math.sqrt(vecA[i]), 2) + Math.pow(Math.sqrt(vecB[i]), 2), 2);
        }
        if (modulo == mult) {
            System.out.println("Los vectores son perpendiculares");
        } else {
            System.out.println("Los vectores no son perpendiculares");
        }
    }

    // e)
    public void paralela(double[] vecA, double[] vecB) {
        System.out.println("---------(E)-----------");
        System.out.println("Verificando si los vectores son paralelos:");

        Double r = null;
        boolean sonParalelos = true;

        for (int i = 0; i < vecA.length; i++) {
            if (vecB[i] == 0) {
                if (vecA[i] != 0) {
                    sonParalelos = false;
                    break;
                }
            } else {
                double cociente = vecA[i] / vecB[i];
                if (r == null) {
                    r = cociente;
                } else if (Math.abs(cociente - r) > 1e-6) {
                    sonParalelos = false;
                    break;
                }
            }
        }
        if (sonParalelos) {
            System.out.println("Los vectores son paralelos con un factor escalar r = " + r);
        } else {
            System.out.println("Los vectores no son paralelos.");
        }
    }

    // f)
    public void paralela(float[] vecA, double vecB[]) {
        System.out.println("---------(F)-----------");
        System.out.println("Verificando si los vectores son paralelos usando el producto vectorial:");

        if (vecA.length != 3 || vecB.length != 3) {
            System.out.println("Ambos vectores deben ser en R^3 (tener 3 componentes).");
            return;
        }

        double[] productoVectorial = new double[3];

        productoVectorial[0] = vecA[1] * vecB[2] - vecA[2] * vecB[1];
        productoVectorial[1] = vecA[2] * vecB[0] - vecA[0] * vecB[2];
        productoVectorial[2] = vecA[0] * vecB[1] - vecA[1] * vecB[0];

        if (productoVectorial[0] == 0 && productoVectorial[1] == 0 && productoVectorial[2] == 0) {
            System.out.println("Los vectores son paralelos.");
        } else {
            System.out.println("Los vectores no son paralelos.");
        }
    }

    // g)
    public void proyeccion(double[] vecA, double[] vecB) {
        System.out.println("---------(G)-----------");

        double productoEscalar = 0;
        for (int i = 0; i < vecA.length; i++) {
            productoEscalar += vecA[i] * vecB[i];
        }

        // Módulo de B 
        double moduloB2 = 0;
        for (int i = 0; i < vecB.length; i++) {
            moduloB2 += Math.pow(vecB[i], 2);
        }

        // Proyección de A sobre B
        double[] proyeccion = new double[vecB.length];
        for (int i = 0; i < vecB.length; i++) {
            proyeccion[i] = (productoEscalar / moduloB2) * vecB[i];
        }

        System.out.print("La proyección ortogonal de A sobre B es: (");
        for (int i = 0; i < proyeccion.length; i++) {
            System.out.print(proyeccion[i]);
            if (i < proyeccion.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println(")");
    }

    // h)
    public void componente(double[] vecA, double[] vecB) {
        System.out.println("---------(H)-----------");
        // Producto escalar de A y B
        double productoEscalar = 0;
        for (int i = 0; i < vecA.length; i++) {
            productoEscalar += vecA[i] * vecB[i];
        }
    
        // Módulo de B
        double moduloB = 0;
        for (int i = 0; i < vecB.length; i++) {
            moduloB += Math.pow(vecB[i], 2);
        }
        moduloB = Math.sqrt(moduloB);
    
        // Componente de A en la dirección de B
        double componente = productoEscalar / moduloB;
    
        System.out.println("La componente de A en la dirección de B es: " + componente);
    }
}
