def calcularAreaCuadro():
    lado=float(input("Ingrese el Lado del Cuadrado:"))
    resulArea=lado*lado
    print("El area del cuadrado es:", resulArea)

def calacularAreaTriangulo():
    base = float(input("Ingrese la Base del triangulo:"))
    altura = float(input("Ingrese la altura del triangulo:"))
    resulArea = (base * altura) / 2
    print("El area del Triangulo es:", resulArea)

def calcularAreaTrapecio():
    baseMayor = float(input("Ingrese la Base Mayor del Trapecio:"))
    baseMenor = float(input("Ingrese la Base Menor del Trapecio:"))
    altura = float(input("Ingrese la Altura del Trapecio:"))
    resulArea = ((baseMayor + baseMenor) * altura) / 2

def calcularAreaFiguraForm2(tipoFigura):
    if(tipoFigura.lower()=="cuadrado"):
        calcularAreaCuadro()
    elif(tipoFigura.lower()=="triangulo"):
        calacularAreaTriangulo()
    elif(tipoFigura.lower()=="trapecio"):
        calcularAreaTrapecio()
    else:
        print("Figura no encontrada!!")

def calcularAreaFigura(tipoFigura):
    if(tipoFigura.lower()=="cuadrado"):
        lado = float(input("Ingrese el Lado del Cuadrado:"))
        resulArea = lado * lado
        print("El area del cuadrado es:", resulArea)
    elif(tipoFigura.lower()=="triangulo"):
        base = float(input("Ingrese la Base del triangulo:"))
        altura = float(input("Ingrese la altura del triangulo:"))
        resulArea = (base * altura)/2
        print("El area del Triangulo es:", resulArea)
    elif(tipoFigura.lower()=="trapecio"):
        baseMayor = float(input("Ingrese la Base Mayor del Trapecio:"))
        baseMenor = float(input("Ingrese la Base Menor del Trapecio:"))
        altura = float(input("Ingrese la Altura del Trapecio:"))
        resulArea = ((baseMayor + baseMenor)*altura)/2
        print("El area del Trapecio es:", resulArea)
    else:
        print("Figura no encontrada!!")


def imprimirTablaMultiplicar1a8():
    for i in range(1, 9):
        for j in range(1, 11):
            print (i, "x", j, "=", i * j)
        print ("\n")

#calcularAreaCuadro()
opcion = "continuar"
while (opcion != "exit"):
    figura = input("Ingrese la Figura para calcular el area:")
    if (figura.lower() == "cuadrado"):
        calcularAreaCuadro()
    elif (figura.lower() == "triangulo"):
        calacularAreaTriangulo()
    elif (figura.lower() == "trapecio"):
        calcularAreaTrapecio()
    else:
        imprimirTablaMultiplicar1a8()
        print("Figura no encontrada!!")

    opcion = input("Desea continuar? si desea salir coloque exit:")
# calcularAreaFiguraForm2(figura)
