"""
Reto 4 - Programa a la solución de la problemática
Consideraciones:
N = cantidad de sucursales
K = cantidad de los tipos de medicamento
M = cantidad de pacientes a atender
"""
# Función para recibir N, M Y K
from ast import Return


def obtenerNMK():
    
    global cant_sucursales, cant_tipos_medicamento, cant_pacientes # Para facilitar asignación
    
    while True:
        #print("Digite la cantidad de sucursales, tipos de medicamento y cantidad de pacientes")
        cadena = input()
        arregloAux = cadena.split(" ")
        # Se toma en cuenta entonces que N es [0], K es [1] y M es [2]
        cant_sucursales = int(arregloAux[0])
        cant_tipos_medicamento = int(arregloAux[1])
        if (cant_sucursales <= 0) or (cant_tipos_medicamento <= 0):
            #print("La cantidad de sucursales/tipos de medicamentos no puede ser menor a 1")
            continue
        else:
            cant_pacientes = int(arregloAux[2])
            break

def llenarMatrizSucursalMed():

    global matriz_sucursal_medicamento, cant_sucursales, cant_tipos_medicamento

    cant_med = 0

    #print("Ahora vamos a digitar la cantidad de medicamentos totales de cada tipo por cada sucursal")
    for i in range(1, (cant_sucursales + 1), 1):  # Filas que son las sucursales

        #print("Digte la cantidad de medicamentos cada tipo (desde el 1 hasta", cant_tipos_medicamento,") en una sola línea de la sucursal", i)
        cadena = input()
        arregloColMedic = separarValoresLista(cadena)  # Corresponde a las columnas (tipos de medicamento) 

        # Como son cadenas, debo hacer una conversion de cada valor a enteros
        for x in range(0, len(arregloColMedic), 1):
            arregloColMedic[x] = int(arregloColMedic[x])

        matriz_sucursal_medicamento.append(arregloColMedic)  # Se agrega la lista de los medicamentos por cada sucursal


# Función para separa los valores 
def separarValoresLista(cadena):
    arreglo = cadena.split(" ")  # Me retorna un arreglo con todos los valores que hayan sido pasados
    return arreglo


# Función para mostrar la matriz de las sucursales con sus medicamentos
def mostrarMatriz(matriz):
    
    for i in range(0, len(matriz), 1):
        print(matriz[i])

# Función para solicitar datos de los pacientes
def pedirDatosPaciente():

    global cant_sucursales, cant_tipos_medicamento, matriz_pacientes_atender, matriz_medicamentos_entrega

    # Llenar matriz de pacientes atendidos en sucursales
    matriz_pacientes_atender = llenarMatricesCero(cant_sucursales, cant_tipos_medicamento)
    #print("Vamos a mirar si se llenó la matriz")
    #mostrarMatriz(matriz_pacientes_atender)
    # Llenar matriz de medicamentos programados para entregar
    matriz_medicamentos_entrega = llenarMatricesCero(cant_sucursales, cant_tipos_medicamento)

    i = 1  # Iterador
    while (i <= cant_pacientes):

        #print("Digite la sucursal, tipo de medicamentos solicitado, número de existencias solicitadas, presión sistólica y distólica para el paciente",i)
        cadena = input()
        arreglo = separarValoresLista(cadena)
        num_sucursal = int(arreglo[0])
        tipo_medicamento = int(arreglo[1])
        num_solicitados = int(arreglo[2])
        pre_sistolica = int(arreglo[3])
        pre_distolica = int(arreglo[4])
        
        if(num_sucursal > cant_sucursales or tipo_medicamento > cant_tipos_medicamento):  # Validemos y descartemos de una vez si este paciente corresponde o nó a una sucursal, a la vez de que digite un tipo de medicamento válido
            break
        else:
            #print("Ok, es válido")
            # Primero, saber si es atendido o no porque habrán cosas distintas a realizar
            if(definirAtencion(pre_sistolica, pre_distolica)):  # En caso de que sea atendido (True)
                #print("El paciente",i,"será atendido")
                # Como debe atenderse, se debe de acumular el valor de medicamentos que la sucursal debe entregar
                # Algo interesante que noté, es que no es necesario recorrer el arreglo, ya que en teoría conocemos la posición del arreglo a modificar
                pos_sucursal = num_sucursal - 1  # Debido a las posiciones naturales de las listas; pero se garantiza acceder a lista correspondiente (ejemplo: si el número es 3, debo ir a la fila 2 de la matriz porque ahí está la sucursal 3)
                pos_medicamento = tipo_medicamento - 1
                matriz_pacientes_atender[pos_sucursal][pos_medicamento] += 1
                
                # Ahora es necesario hacer la sustracción de los medicamnentos totales que tiene la sucursal con los que el paciente solicita
                sustraerSolicitados(num_sucursal, tipo_medicamento, num_solicitados)
                # Luego debemos llevar un conteo de los medicamentos que se deben entregar por cada tipo y por sucursal
                agregarSolicitados(num_sucursal, tipo_medicamento, num_solicitados)

            else:
                #print("El paciente",i,"NO será atendido")
                pos_sucursal = num_sucursal - 1  # Debido a las posiciones naturales de las listas; pero se garantiza acceder a lista correspondiente (ejemplo: si el número es 3, debo ir a la fila 2 de la matriz porque ahí está la sucursal 3)
                pos_medicamento = tipo_medicamento - 1
                matriz_pacientes_atender[pos_sucursal][pos_medicamento] += 1

        i += 1

# Función para agregar a la matriz del conteo de medicamentos a entregar
def agregarSolicitados(num_sucursal, tipo_medicamento, num_solicitados):
    
    global matriz_medicamentos_entrega

    matriz_medicamentos_entrega[num_sucursal - 1][tipo_medicamento - 1] += num_solicitados

# Función para descontar los medicamentos que son solicitados de la sucursal
def sustraerSolicitados(num_sucursal, tipo_medicamento, num_solicitados):
    
    global matriz_sucursal_medicamento

    matriz_sucursal_medicamento[num_sucursal - 1][tipo_medicamento - 1] -= num_solicitados


# Función para saber si el paciente debe atenderse o no
def definirAtencion(presion_sistolica, presion_distolica):

    # True es que se programa la entrega, False es que no
    if(presion_sistolica < 70 and presion_distolica < 50):
        return True
    elif((presion_sistolica >= 70 and presion_sistolica < 110) and (presion_distolica >= 50 and presion_distolica < 70)):
        return False
    elif((presion_sistolica >= 110 and presion_sistolica < 120) and (presion_distolica >= 70 and presion_distolica < 75)):
        return False
    elif((presion_sistolica >= 120 and presion_sistolica < 130) and (presion_distolica >= 75 and presion_distolica < 80)):
        return True
    elif((presion_sistolica >= 130 and presion_sistolica < 150) and (presion_distolica >= 80 and presion_distolica < 90)):
        return True
    elif((presion_sistolica >= 150 and presion_sistolica < 170) and (presion_distolica >= 90 and presion_distolica < 100)):
        return True
    elif(presion_sistolica >= 170 and presion_distolica >= 50):
        return True
    elif(presion_sistolica >= 130 and presion_distolica < 80):
        return True
    else:
        return False  # Debemos pensar en caso de que no sea ninguno, pues se descarta también ese caso
    


# Esta función la tengo para rellanar las otras matrices para medicamentos de entrega y total de pacientes
def llenarMatricesCero(cantidad_filas, cantidad_columnas):
    matriz = []
    
    for i in range(0, (cantidad_filas), 1):
        
        columnas = []
        
        for j in range(0, (cantidad_columnas), 1):
            columnas.append(0)
        
        matriz.append(columnas)

    return matriz


# Función para hallar el menor número en cada sucursal
def hallarMenor(lista):

    cant_menor = 9999  # La cantidad de medicamentos que sea menor
    pos = 0  # La posición de ese medicamento, que sería el número del tipo de medicamento

    for i in range(0, len(lista), 1):
        
        if lista[i] < cant_menor:
            cant_menor = lista[i]
            pos = i
    
    # pos += i  # Para que se acomode al valor del tipo de medicamento y no de la posición

    return pos, cant_menor


# Función para hallar el mayor número en cada sucursal
def hallarMayor(lista):

    cant_mayor = 0  # La cantidad de medicamentos que sea mayor
    pos = 0  # La posición de ese medicamento, que sería el número del tipo de medicamento

    for i in range(0, len(lista), 1):
        
        if lista[i] > cant_mayor:
            cant_mayor = lista[i]
            pos = i
    
    # pos += i  # Para que se acomode al valor del tipo de medicamento y no de la posición

    return pos, cant_mayor

# Función para hallar el promedio de la lista para los medicamentos de entrega 
def hallarPromedio(lista):

    promedio = 0

    for valor in lista:
        promedio += valor
    
    promedio /= len(lista)

    return promedio
        

# Función para obtener la sumatoria de los medicamentos solicitados a entregar para cada sucursal y los pacientes a atender también por cada sucursal
# Es decir, es dinámico porque me sirve tanto para el primero caso de los medicamentos como para el de la matriz de los pacientes atendidos en cada sucursal
def obtenerSumatoria(lista):
    sumatoria = 0

    for valor in lista:
        sumatoria += valor
    
    return sumatoria

# Función especializada para el mínimo de medicamentos por cada sucursal
def hallarMenorMed(lista):
    cant_menor = 9999  # La cantidad de medicamentos que sea menor

    for i in range(0, len(lista), 1):
        
        if lista[i] < cant_menor:
            cant_menor = lista[i]

    return cant_menor

# Función especializada para el máximo de medicamentos por cada sucursal
def hallarMayorMed(lista):
    cant_mayor = 0  # La cantidad de medicamentos que sea menor

    for i in range(0, len(lista), 1):
        
        if lista[i] > cant_mayor:
            cant_mayor = lista[i]

    return cant_mayor


# Función para mostrar los resultados finales que se solicitan
def mostrarResultados():

    global matriz_sucursal_medicamento, matriz_pacientes_atender, matriz_medicamentos_entrega
    i = 1  # Iterador para cada sucursal
    pos = 0  # para cada posición de la sucursal

    while(i <= cant_sucursales):
        
        print(i)  # Número de la sucursal
        arreglo_sucursal = matriz_sucursal_medicamento[pos]
        tipo_med, cant = hallarMenor(arreglo_sucursal)  # Mostrar el tipo de medicamento con la menor cantidad de existencias luego de entrega
        tipo_med += 1 # Por tema de posición y necesito es el número del tipo de medicamento
        print(tipo_med, cant)
        tipo_med, cant = hallarMayor(arreglo_sucursal)  # Mostrar el tipo de medicamento con la mayor cantidad de existencias luego de entrega
        tipo_med += 1  # Por tema de posición y necesito es el número del tipo de medicamento
        print(tipo_med, cant)
        arreglo_medicamentos_entrega = matriz_medicamentos_entrega[pos]
        minimo = hallarMenorMed(arreglo_medicamentos_entrega)  # El valor mínimo de existencias programadas para entrega
        maximo = hallarMayorMed(arreglo_medicamentos_entrega)  # El valor máximo de existencias programadas para entrega
        promedio = hallarPromedio(arreglo_medicamentos_entrega)  # El valor promedio de las existencias programads para entrega
        print(f"{minimo:.2f} {promedio:.2f} {maximo:.2f}")
        total_med_entrega = obtenerSumatoria(arreglo_medicamentos_entrega)  # Sumatoria de los medicamentos de entrega por cada sucursal
        arreglo_pacient_atender = matriz_pacientes_atender[pos]  # Para obtener la sucursal de los pacientes a atender
        total_pacientes_atendidos = obtenerSumatoria(arreglo_pacient_atender)  # Sumaotira de los pacientes a atender por cada sucursal
        
        if(total_pacientes_atendidos == 0):  # Debo validar que no se divida entre cero
            promedio_exis_progra = 0
        else:
            promedio_exis_progra = total_med_entrega / total_pacientes_atendidos

        print(f"{promedio_exis_progra:.2f}")  # Promedio de existencias programadas para entrega por paciente de la sucursal
        
        if(i == cant_sucursales):  # En la última parte, debo mostrar los siguientes valores

            # Número de sucursal con la menor cantidad de existencias programadas para el medicamento de tipo 1
            num_sucursal, menor = hallarMenorTipo1()
            num_sucursal += 1  # Por tema de posición y necesito es el número de la sucursal
            print(num_sucursal, menor)

            # Número de sucursal con la mayor cantidad de existencias programadas para el medicamento de tipo 1
            num_sucursal, mayor = hallarMayorTipo1()
            num_sucursal += 1  # Por tema de posición y necesito es el número de la sucursal
            print(num_sucursal, mayor)

        i += 1
        pos += 1  # Para avanzar en cada sucursal


# Función única para hallar la sucursal con la menor cantidad de existencias programadas para entrega del medicamento de tipo 1
def hallarMenorTipo1():
    global matriz_medicamentos_entrega, cant_sucursales

    menor = 9999
    i = 0
    num_sucursal = 0

    while(i < cant_sucursales):
        
        valor_sucursal = matriz_medicamentos_entrega[i][0]  # Posición cero porque siempre será el de tipo 1 y solo necesito avanzar de fila
        
        if(valor_sucursal < menor):
            menor = valor_sucursal
            num_sucursal = i
        
        i += 1

    return num_sucursal, menor


# Función única para hallar la sucursal con la mayor cantidad de existencias programadas para entrega del medicamento de tipo 1
def hallarMayorTipo1():
    global matriz_medicamentos_entrega, cant_sucursales

    mayor = 0
    i = 0
    num_sucursal = 0

    while(i < cant_sucursales):
        
        valor_sucursal = matriz_medicamentos_entrega[i][0]  # Posición cero porque siempre será el de tipo 1 y solo necesito avanzar de fila
        
        if(valor_sucursal > mayor):
            mayor = valor_sucursal
            num_sucursal = i
        
        i += 1

    return num_sucursal, mayor



"""Main"""

# Variables de control
cant_sucursales, cant_tipos_medicamento, cant_pacientes = 0, 0, 0
matriz_sucursal_medicamento = []  # Esta matriz contendrá las sucursales y la cantidad de medicamentos que tienen por tipo
matriz_pacientes_atender = []  # Esta matriz contendrá los pacientes que fueron atendidos en las sucursales
matriz_medicamentos_entrega = []  # Esta matriz contendrá el total de medicamentos a entregar por cada tipo y en cada sucursa

obtenerNMK()
#print("Resultados de N, M Y K:", cant_sucursales, cant_tipos_medicamento, cant_pacientes)
llenarMatrizSucursalMed()
#print("Ahora vamos a mostrar la matriz de medicamentos totales")
#mostrarMatriz(matriz_sucursal_medicamento)
# matriz = llenarMatricesCero(5, 5)
# mostrarMatriz(matriz)
#lamatriz = []
#lamatriz = llenarMatricesCero(3, 4)
#mostrarMatriz(lamatriz)
#print("Ahora veamos algo")
#print(lamatriz[2][1])
#print("cambiamos su valor")
#lamatriz[2][1] = lamatriz[2][1] + 1
#print("Ahora veamos algo")
#print(lamatriz[2][1])
#mostrarMatriz(lamatriz)
pedirDatosPaciente()
#mostrarMatriz(matriz_pacientes_atender)
#print("Ahora vamos a mostrar la matriz de medicamentos luego de ser entregados los medicamentos")
#mostrarMatriz(matriz_sucursal_medicamento)
#print("Ahora vamos a mostrar la matriz de la cantidad de medicamentos que son solicitados por cada tipo a las sucursales")
#mostrarMatriz(matriz_medicamentos_entrega)
#print("Y ahora la matriz de los pacientes atendidos")
#mostrarMatriz(matriz_pacientes_atender)
#print("Resultado finales:")
mostrarResultados()