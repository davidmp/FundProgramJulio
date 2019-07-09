
import java.util.Scanner

class AlgoritmosScalax{
  val s = new Scanner(System.in)
  
  def tablaMultiplicar(){
     for(i<-1 to 8){
       for(j<-1 to 10){
         println(i+"*"+j+"="+i*j)
       }
       println("\n")
     }
   }
   
  def calcularInteresFinAnho(){
       println("Ingrese el monto Inicial a Invertir:")
       var monto=s.nextDouble()
       var interes: Double=0       
       for (i<-1 to 12){
         interes=monto*0.02
         monto=monto+interes
         println("Al final del "+ i+ " mes el monto sera :"+ monto)         
       }
       print ("El monto que la persona entra al final del año sera:"+monto)       
  }    
}

object AppRun{
   def main(args: Array[String]) {
      println("Bienvenido a Scala");  
      
      val car = new AlgoritmosScalax()
      val s = new Scanner(System.in)
      
      var isConinue: Int=0
        do{
            println("Menu de Opciones ") 
            
            isConinue match{
              case 1 => car.tablaMultiplicar()
              case 2 => car.calcularInteresFinAnho()
              case _ => "Opcion desconocida"
            }
            
            println("Seleccion una Opcion")
            println("1=Tabla Muntiplicar ") 
            println("2=Calcular Interes ")
            println("0=Salir ")
            
            isConinue=s.nextInt()
        }  
        while (isConinue != 0)                   
   }
}