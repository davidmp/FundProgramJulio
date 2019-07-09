import java.util.Scanner;

class AlgoritmosScala {
  val sc=new Scanner(System.in)
  
  def tablaMultiplicar1a8(){
    for(i<-1 to 8){
      for(j<-1 to 10){
        println(i+"x"+j+"="+i*j)
      }
      print("\n")
    }
  }
    
  def calcularInteresFinAnho(){
    print("Ingrese el monto Inicial a Invertir:")
    var monto=sc.nextDouble()
    for(mes<-1 to 12){
     var interes=monto*0.02
     monto=monto+interes
     println("Al final del "+mes+ " mes el monto sera :"+ monto)
    }    
  }
  
  def calularSumadeVentas(){
    println("Sistema de Ventas")
    var isCliente: String ="si"
    var montoPagar=0.0
    do{
      println("Ingrese el nombre del Cliente:")  
      var nombrecliente=sc.next()
      println("Ingrese el Monto a Pagar:")  
      montoPagar=montoPagar+sc.nextDouble()
      println("Hay Mas Clientes? SI/NO:")      
      isCliente=sc.next()      
    }
    while(isCliente.toLowerCase().equals("si"))      
    println("Se le Informa al Supervisor que se recaudo al final del día:"+montoPagar)
  }    
}

object AppMain{
  def main(args: Array[String]) {
    var probar=0    
    do{
    println("Bienvenido a Scala")
    println("Que Algoritmo desea Probar?")
    println("1 Tabla de Multiplicar")
    println("2 Calculo de Interes")
    println("3 Suma de Ventas al Final del Dia")    
    val obj=new AlgoritmosScala()
    val sc=new Scanner(System.in)
    var opcion=sc.nextInt()
    opcion match{
      case 1=>obj.tablaMultiplicar1a8()
      case 2=>obj.calcularInteresFinAnho()
      case 3=>obj.calularSumadeVentas()
      case _=>print("No existe la opcion seleccionada")
    }
    println("Desea Continuar ? 1=SI 0=NO")
    probar=sc.nextInt()
    
    }while(probar!=0)
  }
}
