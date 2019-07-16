from ctypes import py_object


class OrdenacionYBusqueda():
    def insercionDirecta(self, vector):
        aux,posicion=0,0
        for i in range(1, len(vector)):
            aux=vector[i]
            posicion=i
            while(posicion>0 and aux<vector[posicion-1]):
                vector[posicion]=vector[posicion-1]
                posicion=posicion-1
                print("Proceso While:",vector)
            vector[posicion]=aux
            print("Proceso for:", vector)
        return vector

    def insercionDirectaRecur(self, vector, i):
        aux, posicion = 0, 0
        if(i<len(vector)):
            aux=vector[i]
            posicion=i
            while(posicion>0 and aux<vector[posicion-1]):
                vector[posicion]=vector[posicion-1]
                posicion=posicion-1
                print("Proceso While:",vector)
            vector[posicion]=aux
            vector=self.insercionDirectaRecur(vector,i+1)
        return vector

    def ordenacionSortBurbuja(self, vector):
        posicion, aux=0,0
        while(posicion<len(vector)):
            if(posicion==0 or vector[posicion]>=vector[posicion-1]):
                posicion=posicion+1
                print(vector)
            else:
                aux=vector[posicion-1]
                vector[posicion - 1]=vector[posicion]
                vector[posicion]=aux
                posicion=posicion-1
                print(vector)
        return vector

    def ordenacionSortBurbujaRecur(self,vector, posicion):
        if(posicion<len(vector)):
            if(posicion==0 or vector[posicion]>=vector[posicion-1]):
                posicion=posicion+1
                self.ordenacionSortBurbujaRecur(vector, posicion)
            else:
                aux=vector[posicion-1]
                vector[posicion - 1]=vector[posicion]
                vector[posicion]=aux
                posicion=posicion-1
                self.ordenacionSortBurbujaRecur(vector,posicion)
        return vector

    def factorialRecur(self, numero):
        if(numero<=1):
            return 1
        else:
            return numero*self.factorialRecur(numero-1)

    def fibonaciRecur(self, numero):
        if(numero<0):
            return -1
        elif(numero==0):
            return 0
        elif numero==1:
            return 1
        else:
            return self.fibonaciRecur(numero-1)+self.fibonaciRecur(numero-2)

obj=OrdenacionYBusqueda()
print("Factorial:", obj.factorialRecur(5))
print("Fibonaci:", obj.fibonaciRecur(6))