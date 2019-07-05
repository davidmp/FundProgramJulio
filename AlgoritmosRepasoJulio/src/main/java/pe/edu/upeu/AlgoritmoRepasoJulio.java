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
        }
    }
    
    public static void main(String[] args){
        System.out.println("Hola Mundo");
        AlgoritmoRepasoJulio arj=new AlgoritmoRepasoJulio();
        arj.calcularAreaCuadro();
    }
 
}
