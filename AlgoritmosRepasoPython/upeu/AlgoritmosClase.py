class AlgoritmosClaseRep(object):
    def calcularAreaCuadro(self):
        lado = float(input("Ingrese el Lado del Cuadrado:"))
        resulArea = lado * lado
        print("El area del cuadrado es:", resulArea)

    def calacularAreaTriangulo(self):
        base = float(input("Ingrese la Base del triangulo:"))
        altura = float(input("Ingrese la altura del triangulo:"))
        resulArea = (base * altura) / 2
        print("El area del Triangulo es:", resulArea)

    def calcularAreaTrapecio(self):
        baseMayor = float(input("Ingrese la Base Mayor del Trapecio:"))
        baseMenor = float(input("Ingrese la Base Menor del Trapecio:"))
        altura = float(input("Ingrese la Altura del Trapecio:"))
        resulArea = ((baseMayor + baseMenor) * altura) / 2

    def calcularAreaFiguraForm2(tipoFigura):
        if (tipoFigura.lower() == "cuadrado"):
            calcularAreaCuadro()
        elif (tipoFigura.lower() == "triangulo"):
            calacularAreaTriangulo()
        elif (tipoFigura.lower() == "trapecio"):
            calcularAreaTrapecio()
        else:
            print("Figura no encontrada!!")

    def imprimirTablaMultiplicar1a8(self):
        for i in range(1, 9):
            for j in range(1, 11):
                print (i, "x", j, "=", i * j)
            print ("\n")

    def main(self):
        obj = AlgoritmosClaseRep()
        opcion = "continuar"
        while (opcion != "exit"):
            figura = input("Ingrese la Figura para calcular el area:")
            if (figura.lower() == "cuadrado"):
                obj.calcularAreaCuadro()
            elif (figura.lower() == "triangulo"):
                obj.calacularAreaTriangulo()
            elif (figura.lower() == "trapecio"):
                obj.calcularAreaTrapecio()
            else:
                print("Figura no encontrada!!")
                if (figura=="tablamul"):
                    obj.imprimirTablaMultiplicar1a8()
                elif (figura=="interes"):
                    obj.calcularInteresFinAnho()
                else:
                    print ("No existe esa opcion")
            opcion = input("Desea continuar? si desea salir coloque exit:")

    def calcularInteresFinAnho(self):
        monto = float(input("Ingrese el monto Inicial a Invertir:"))
        for i in range(1,13):
            interes=monto*0.02
            monto=monto+interes
            print ("Al final del ", i, " mes el monto sera :", monto)
        print ("El monto que la persona entra al final del año sera:",monto)

if __name__ == '__main__':
    obj = AlgoritmosClaseRep()
    obj.main()
