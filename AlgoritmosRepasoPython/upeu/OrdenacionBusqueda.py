from ctypes import py_object


class OrdenacionYBusqueda():
    def insercionDirecta(self, vertor):
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



obj=OrdenacionYBusqueda()
vector=[4,10,1,8,3]
print("Antes:", vector)
#print("Ordenado:",obj.insercionDirecta(vector))
print("Ordenar Burbuja", obj.ordenacionSortBurbuja(vector))