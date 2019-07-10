class RepasoPreExmaen():
    def resultadoCenso(self):
        print ("Censo Nacional de Vivienda")
        isVivienda=1
        primaria, secundaria, carrTecnica, carrProfesional, postgrado=0,0,0,0,0
        while(isVivienda):
            nombrePersona=input("Ingrese el Nombre de la Persona:")
            print ("1=Primaria\n2=Secundaria\n3=Carrera Tecnica\n4=Carrera Profesional\n5=Postgrado")
            nivelEstudio=int(input("Ingrese el Nivel de Estudio:"))
            if(nivelEstudio==1):
                primaria=primaria+1
            elif (nivelEstudio==2):
                secundaria=secundaria+1
            elif(nivelEstudio==3):
                carrTecnica=carrTecnica+1
            elif(nivelEstudio==4):
                carrProfesional=carrProfesional+1
            else:
                postgrado=postgrado+1
            isVivienda=int(input("Hay Mas viviendas ? 1=True, 0=False"))
        print ("Los resultados de la encuesta en cuanto a nivel de estudio es la siguiente:")
        totalPersonasEncuestadas=primaria+secundaria+carrTecnica+carrProfesional+postgrado
        print ("Personas con nivel de estudio Primario representan un: ", (primaria*100)/totalPersonasEncuestadas, "%")
        print ("Personas con nivel de estudio Secundario representan un: ", (secundaria * 100) / totalPersonasEncuestadas, "%")
        print ("Personas con nivel de estudio de Carrera tecnica representan un: ", (carrTecnica * 100) / totalPersonasEncuestadas, "%")
        print ("Personas con nivel de estudio de Carrera Profesional representan un: ", (carrProfesional * 100) / totalPersonasEncuestadas, "%")
        print ("Personas con nivel de estudio de Postgrado representan un: ", (postgrado * 100) / totalPersonasEncuestadas, "%")

    def calcularPromedioPonderado(self):
        print ("Matricula Cursos Estudiante")
        isCurso = 1
        nCursos = 10
        contador=0
        sumCreditos=0
        multCredCalif=0
        multCredCalifX = 0
        matriz = [[0] * nCursos for i in range(nCursos)]
        while(isCurso):
            matriz[contador][0]=input("Ingrese el codigo del curso:")
            if(matriz[contador][0]!="9999"):
                matriz[contador][1]=input("Ingrese el Nombre del Curso:")
                matriz[contador][2]=float(input("Ingrese la calificacion del curso:"))
                matriz[contador][3] = int(input("Ingrese el numero de Creditos:"))
                multCredCalif=matriz[contador][2]*matriz[contador][3]
                multCredCalifX=multCredCalifX+multCredCalif
                sumCreditos=sumCreditos+matriz[contador][3]
                contador = contador + 1
            else:
                if(sumCreditos>=25 and sumCreditos<=50):
                    isCurso=0
                    for i in range(0,contador):
                        print (matriz[i][0], "\t", matriz[i][1], "\t", matriz[i][2], "\t", matriz[i][3])
                    print ("Cantidad de Cursos Matriculados es:", contador)
                    print ("Promedio Ponderado es:", multCredCalifX/sumCreditos)
                else:
                    print ("Ingrese Nuevamente los Cursos:")
                    isCurso = 1
                    contador = 0
                    sumCreditos = 0

    def calcularPeso(self):
        pesoBascula, estadoPeso, diferenciaPeso=0, "", 0
        for i in range(1,6):
            pesoInit=float(input(f"Ingrese el Peso Inicial de Persona {i} :"))
            for j in range(1, 11):
                pesoReal=float(input(f"Ingrese el peso calculado de la Bascula {j} :"))
                pesoBascula=pesoBascula+pesoReal
                if(j==10):
                    if(pesoBascula/j>pesoInit):
                        estadoPeso="SUBIDO"
                        diferenciaPeso=(pesoBascula/j)-pesoInit
                    else:
                        estadoPeso="BAJADO"
                        diferenciaPeso = pesoInit-(pesoBascula / j)
                    print ("Su peso es:", pesoBascula/j, " Ud. a:", estadoPeso, " en ", diferenciaPeso, " Kilos")
            pesoBascula=0


if __name__ == '__main__':
    obj=RepasoPreExmaen()
    #obj.resultadoCenso()
    #obj.calcularPromedioPonderado()
    obj.calcularPeso()

    print ("Hola mundo")