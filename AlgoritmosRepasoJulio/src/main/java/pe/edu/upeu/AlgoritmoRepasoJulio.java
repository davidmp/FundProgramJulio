/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pe.edu.upeu;

import java.util.Scanner;

/**
 *
 * @author Software Student
 */
public class AlgoritmoRepasoJulio {
    //Variables Globales
    double resultPerimetro=0, restultArea=0;
    private static double contador;
    Scanner sc;
    
    //Metodo/Funcion
    void calcularAreaCuadro(){
        //Definir Variables
        System.out.print("Ingrese el Lado del Cuadrado:");
        sc=new Scanner(System.in);
        //Varible Local y Lectura de Valores
        double lado=sc.nextDouble();
        //Proceso
        restultArea=lado*lado;
        /*Imprimir Resultado*/
        System.out.println("El area del cuadrado es:"+restultArea);
        }
    
    void calcularAreaTriangulo(){
        System.out.println("Ingrese la Base del triangulo:");
        double base=sc.nextDouble();
        System.out.println("Ingrese la altura del triangulo:");
        double altura=sc.nextDouble();
        restultArea=(base*altura)/2;
        System.out.println("El area del Triangulo es: "+restultArea);    
    }
    
   void calcularAreaTrapacio(){
        System.out.println("Ingrese Base Mayor del Trapecio:");
        double baseMa=sc.nextDouble();
        System.out.println("Ingrese Base Menor del Trapecio:");
        double baseMe=sc.nextDouble();
        System.out.println("Ingrese Altura del Trapecio:");
        double altura=sc.nextDouble();
        restultArea=((baseMa+baseMe)*altura)/2;
        System.out.println("El area del Trapecio es: "+restultArea);     
    }
   
   static void saludo(){
       System.out.println("Hola Mundo");
   }
   
    public void calcularAreaFiguraForm2(String tipoFigura){
        //Estructura selecctiva multiple
        switch(tipoFigura.toLowerCase()){
        case "cuadrado":{ calcularAreaCuadro(); break;}
        case "triangulo":{ calcularAreaTriangulo(); break;}
        case "trapecio":{ calcularAreaTrapacio(); break;}
        case "saludo":{ saludo(); break;}
        default:{System.out.println("Figura no Encontrada!");}
        }    
    }    
    public void calcularAreaFigura(String tipoFigura){
        sc=new Scanner(System.in);
        if(tipoFigura.toLowerCase().equals("cuadrado")){
        System.out.println("Ingrese el Lado del Cuadrado:");
        double lado=sc.nextDouble();
        restultArea=lado*lado;
        System.out.println("El area del cuadrado es: "+restultArea);
        }else if(tipoFigura.toLowerCase().equals("triangulo")){
        System.out.println("Ingrese la Base del triangulo:");
        double base=sc.nextDouble();
        System.out.println("Ingrese la altura del triangulo:");
        double altura=sc.nextDouble();
        restultArea=(base*altura)/2;
        System.out.println("El area del Triangulo es: "+restultArea);
        }else if(tipoFigura.toLowerCase().equals("trapecio")){
        System.out.println("Ingrese Base Mayor del Trapecio:");
        double baseMa=sc.nextDouble();
        System.out.println("Ingrese Base Menor del Trapecio:");
        double baseMe=sc.nextDouble();
        System.out.println("Ingrese Altura del Trapecio:");
        double altura=sc.nextDouble();
        restultArea=((baseMa+baseMe)*altura)/2;
        System.out.println("El area del Trapecio es: "+restultArea);        
        }else{
            System.out.println("Figura no encontrada!!");
        }
    }  
    
    public static void main(String[] args){
        System.out.println("Hola Mundo");
        String continuaSalir="Continuar";
        AlgoritmoRepasoJulio arj=new AlgoritmoRepasoJulio();
        //arj.calcularAreaCuadro();
        
        do{
        arj.sc=new Scanner(System.in);
        System.out.println("Ingrese un tipo de Figura:");
        String figura=arj.sc.nextLine();
        //arj.calcularAreaFigura(figura);
        arj.calcularAreaFiguraForm2(figura);   
        
        System.out.println("Desea Continuar? ...Si desea salir coloque exit:");
        arj.sc=new Scanner(System.in);
        continuaSalir=arj.sc.nextLine();        
        
        }while(!continuaSalir.toLowerCase().equals("exit"));
        
       
    }
 
}
