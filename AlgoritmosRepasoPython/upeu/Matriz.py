class OperacionMatrices():

    def sumaValoresMatriz(self):
        M=[[1,2,18,3],[5,6,7,10],[8,9,10,12]]
        sumaTotal, sumPares=0,0
        print("Tamaño X:", len(M))
        print("Tamaño Y:", len(M[0]))
        for x in range(0,len(M)):
            for y in range(0, len(M[0])):
                sumaTotal=sumaTotal+M[x][y]
                if M[x][y]%2==0:
                    sumPares=sumPares+M[x][y]
        print("Suma total de valores de la Matriz :", sumaTotal)
        print("Suma total de valores pares de la Matriz es:", sumPares)

    def transformada04(self, dimension, numInicio):
        M=[[0] * dimension for i in range(dimension)]
        for x in range(0, dimension):
            for y in range(0, dimension):
                if(y<dimension-x):
                    if (x+y)%2==0:
                        M[x][y]=numInicio+((x+y)*(x+y+1)/2)+x
                    else:
                        M[x][y]=numInicio+((x+y)*(x+y+1)/2)+y
                else:
                    M[x][y]=""
        return M

    def transformada17(self, dimension, numInicio):
        M = [[0] * dimension for i in range(dimension)]
        contadorX, contadorY, contGe=0,dimension-1, 0
        while (contadorY >= 0):
            print("Valor Y:", contadorY, " contGe:", contGe, "Valor X", contadorX, "numInicio:", numInicio)
            while(contadorX<dimension-contGe):
                M[contadorX][contadorY]=numInicio
                numInicio = numInicio + 1
                contadorX=contadorX+1
                print("Valor Y:", contadorY, " contGe:", contGe, "Valor X", contadorX, "numInicio:", numInicio)
            contadorY=contadorY-1
            contGe=contGe+1
            contadorX=0
        return M

    def transformada30Caracol(self, dimension, numInicio):
        M = [[0] * dimension for i in range(dimension)]
        for c in range(0,int(dimension/2)):
            for ld in range(c,dimension-c-1):
                M[ld][dimension-1-c]=numInicio
                numInicio=numInicio+1
            li=dimension-1-c
            while(li>c):
                M[dimension - 1 - c][li] = numInicio
                numInicio = numInicio + 1
                li=li-1
            liz=dimension-1-c
            while(liz>c):
                M[liz][c] = numInicio
                numInicio = numInicio + 1
                liz=liz-1
            for ls in range(c,dimension-1-c):
                M[c][ls] = numInicio
                numInicio = numInicio + 1
        if dimension%2!=0:
            M[int(dimension/2)][int(dimension/2)]=numInicio
        return M

    def imprimirMatriz(self, matriz):
        for x in range(0, len(matriz)):
            for y in range(0,len(matriz[0])):
                print(matriz[x][y],"\t",end='')
            print("\n")

obj=OperacionMatrices()
obj.sumaValoresMatriz()
dimension=int(input("Ingrese la dimesion de la Matriz:"))
numInicio=int(input("Ingrese el numero de inicio:"))

#obj.imprimirMatriz(obj.transformada04(dimension, numInicio))
#obj.imprimirMatriz(obj.transformada17(dimension, numInicio))
obj.imprimirMatriz(obj.transformada30Caracol(dimension,numInicio))