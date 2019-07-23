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

obj=OperacionMatrices()
obj.sumaValoresMatriz()