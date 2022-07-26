"""
Reto 3 corrección
En esta corregiré el error que tenía de no poder calcular la porción porcental para eso se usará listas dentro de listas
Para facilitar el programa, usaremos funciones mejor definidas
"""

# Función para pedir el número de sucursales y número de pacientes

def pedirSucursalesyPacientes():
    # Usaremos las variables globales para facilitar el proceso
    global num_sucursales, num_pacientes
    while True:
        # print("Digite el número de sucursales y el número de pacientes")
        cadena = input()  # El ejercicio requiere leer todo en una sola línea, ejemplo: 3 5
        if separarEntradaSyP(cadena):  # En caso de que sea True, ya podemos continuar
            break
        else:
            continue


# Función para separar valores de sucursal y pacietnes
def separarEntradaSyP(cadena):

    # Usaremos las variables globales para facilitar el proceso
    global num_sucursales, num_pacientes
    lista = cadena.split(" ")  # Separamos ambos valores entre el espacio
    num_sucursales = int(lista[0])
    num_pacientes = int(lista[1])

    if num_sucursales <= 0:  # Validamos de una vez de que las sucursales no sean menor o igual a 0
        # print("La cantidad de sucursales no puede ser menor o igual a cero")
        return False
    else:
        return True

# Función para soliciar los medicamentos para cada sucursal


def llenarSucursalesMed():

    global lista_sucursales  # Usaremos las variables globales para facilitar el proceso
    i = 1  # Iterador

    while (i <= num_sucursales):

        # print("Digite la cantidad de medicamentos en existencia para la sucursal", i)
        cant = int(input())

        while (cant < 1):
            # print("La cantidad de medicamentos a entregar no puede ser menor a 1, digite otra vez")
            cant = int(input())

        # Obtener los valores de índice de sucursal y su cantidad de medicamentos, el tercero solo lo rellenamos
        sucursal = [i, cant, 0]
        # Al principio cada sucursal manejará los dos valores anteriores, el tercero se actulizará más adelente
        lista_sucursales.append(sucursal)
        i += 1


# Función para atender a los pacientes (asignar sucursal y solicitar presion asistólica y distólica)
def atenderPacientes():

    global lista_sucursales
    sucursal, p_asistolica, p_distolica, num_dosis = 0, 0, 0, 0
    i = 1  # Iterador

    while (i <= num_pacientes):

        # print("Digite la sucursal, presión asistólica y distólica del paciente",i)
        num_dosis = 0  # Si no reiniciamos el valor, los demás casos podrían tomarlo y sería información falsa
        cadena = input()
        sucursal, p_asistolica, p_distolica = separarValoresPaciente(cadena)  # Obtenemos cada valor ya casteado

        # Ahora debemos evaluar la asignación de medicamentos por cada paciente para cada sucursal
        if(p_asistolica < 70 and p_distolica < 50):  # Categoría Hipotensión
            num_dosis = 5
        elif((p_asistolica >= 70 and p_asistolica < 110) and (p_distolica >= 50 and p_distolica < 70)):  # Categoría Óptima
            num_dosis = 0
        elif((p_asistolica >= 110 and p_asistolica < 120) and (p_distolica >= 70 and p_distolica < 75)):  # Categoría Normal
            num_dosis = 0
        elif((p_asistolica >= 120 and p_asistolica < 130) and (p_distolica >= 75 and p_distolica < 80)):  # Categoría Prehipertensión
            num_dosis = 10
        elif((p_asistolica >= 130 and p_asistolica < 150) and (p_distolica >= 80 and p_distolica < 90)):  # Categoría Hipertensión grado 1
            num_dosis = 15
        elif((p_asistolica >= 150 and p_asistolica < 170) and (p_distolica >= 90 and p_distolica < 100)):  # Categoría Hipertensión grado 2
            num_dosis = 25
            # print("Entré en Hipertension Grado 2")
        elif(p_asistolica >= 170 and p_distolica >= 100):  # Categoría Hipertensión grado 3
            num_dosis = 45
        elif(p_asistolica >= 130 and p_distolica < 80):  # Categoría Solo Sistolica
            num_dosis = 25
            # print("Entré en solo sistólica")

        # print("Numéro de dosis para ese paciente", num_dosis) 
        # Ahora toca ir añadiendo los medicamentos que cada sucursal debe entregar (acumular valores)
        completarOrdenesSucursales(sucursal, num_dosis)
        i += 1   

# Función para separar la entrada de sucursal, presión asitóluca y distólica
def separarValoresPaciente(cadena):
    
    lista = cadena.split(" ")
    sucursal = int(lista[0])
    p_asistolica = int(lista[1])
    p_distolica = int(lista[2])
    
    return sucursal, p_asistolica, p_distolica

# Función para llenar el total de medicamentos que deben entregar las sucursales
def completarOrdenesSucursales(sucursal, num_dosis):
    
    global lista_sucursales

    # Por cada sucursal debo llenar la última posición de la lista global de sucursales, ahí debo llenar la cantidad de medicamentos a entregar
    for sucur in lista_sucursales:
    
        sublista = sucur  # Así obtenemos cada lista de la lista de sucursales (la lista dentro de la lista por cada posición)
        
        if(sublista[0] == sucursal):  # Debo evaluar a que sucursal le debo ir llenando la orden de medicamentos totales
            sublista[2] += num_dosis  # En la posición 2 porque ahí es donde reservé el espacio para los medicamentos a entregar
            break  # Ya no necesito recorrer más el ciclo

# Función para mostar la sucursal con la menor cantidad de medicamentos después de entrega
def mostrarSucursalMenor():
    global lista_sucursales
    menor = 9999  # Usamos un valor alto para efectuar el algoritmo
    sucursal = 0  # Para el número de la sucursal

    for sucur in lista_sucursales:
        
        sublista = sucur
        total_medicamentos = sublista[1]  # En esta posición está el total de medicamentos de la sucursal
        total_entregas =sublista[2]  # En esta posición están el total de medicamentos que se deben entregar
        restante = total_medicamentos - total_entregas
        if(restante < menor):
            menor = restante
            sucursal = sublista[0]  # En esta posición tenemos el número de la sucursal
    
    # print("La sucursal con menor cantidad de existencias luego de la entrega es: ")
    cadena = str(sucursal) + " " + str(menor)
    print(cadena)


# Función para mostar la sucursal con la mayor cantidad de medicamentos después de entrega
def mostrarSucursalMayor():
    global lista_sucursales
    mayor = 0  # Usamos un valor bajo para efectuar el algoritmo
    sucursal = 0  # Para el número de la sucursal

    for sucur in lista_sucursales:
        
        sublista = sucur
        total_medicamentos = sublista[1]  # En esta posición está el total de medicamentos de la sucursal
        total_entregas =sublista[2]  # En esta posición están el total de medicamentos que se deben entregar
        restante = total_medicamentos - total_entregas
        if(restante > mayor):
            mayor = restante
            sucursal = sublista[0]  # En esta posición tenemos el número de la sucursal
    
    # print("La sucursal con mayor cantidad de existencias luego de la entrega es: ")
    cadena = str(sucursal) + " " + str(mayor)
    print(cadena)

# Función para mostar la porción porcentual de cada sucursal en su entrega de medicamentos

# Es importante tener en cuenta que esa porción corresponde a la cantidad de medicamentos a entregar respecto a la cantidad total
def mostrarPorcionPorcentual():
    global lista_sucursales

    for sucur in lista_sucursales:
        
        sublista = sucur
        num_sucursal = sublista[0]  # Posición que contiene el número de sucursal
        total_medicamentos = sublista[1]  # Posición que contiene el numero de medicamentos totales
        total_medicamentos_entrega = sublista[2]  # Posición que contiene el número de medicametos totales que debe entregar la sucursal
        # Para hallar la porción porcentual debemos usar regla de 3 y hallar que porcentaje son los medicamentos de entrega respecto a los totales
        porcentaje = (total_medicamentos_entrega * 100) / total_medicamentos
        # print("El porcentaje es:",porcentaje,"y si fuera redondeado el valor sería", f"{porcentaje:.2f}%")
        porcentaje = round(porcentaje, 2)  # Ahora resulta que se quiere es el resultado redondeado
        # Se nos pide delimitar la cantidad de cifras decimales, no usaré format de Python porque lo redonda y no sirve ese caso, usaré una función propia
        # cantidad = delimitarDecimal(porcentaje)
        # cantidad = str(num_sucursal) + " " + cantidad + "%"
        # cantidad = str(num_sucursal) + " " + str(porcentaje) + "%"
        # print(cantidad)  # Aquí ahora es donde imprimo la sucursal y la cantidad porcentual correspondiente
        print(f"{num_sucursal} {porcentaje:.2f}%")  # la otra parte es un redondea que se puede hacer directamente a la variable y 2f quiere decir que redondee a 2 decimales


# Función para delimitar los decimales de la parte porcentual

def delimitarDecimal(decimal):
    cadena = str(decimal)
    aux = ""
    lista = cadena.split(".")
    parte_entera = str(lista[0])  # La parte entera se asegura
    # El problema es la parte decimal
    parte_decimal = str(lista[1])
    longitud = len(parte_decimal) # Necesito saber la cantidad de decimales
    # print("La longitud es de:",longitud) 
    if(longitud >= 2):  # En caso de ser 2 o más pues solo agrego los dos primeros
        aux = str(parte_decimal[0]) + str(parte_decimal[1])  # Así obtengo los primeros dos decimales
    elif(longitud < 2):  # Puede darse el caso de que pueda aparecer solo un decimal (mejor prevenir y colocar ese solo decimal)
        aux = str(parte_decimal[0])
    
    cadena = parte_entera + "." + aux
    
    return cadena

"""Inicio del programa (main)"""

# Variables globales
num_sucursales, num_pacientes = 0, 0
# La idea de esta lista es que reciba listas, donde estas últimas manejen tres valores
lista_sucursales = []
# El primero el número de la sucursal, el segundo la cantidad de medicamentos totales y el tercero la cantidad de medicamentos que deberá entregar (luego de pedirlas al usuario)

""" Inicio de procesos """

pedirSucursalesyPacientes()
# print(num_sucursales, num_pacientes)
llenarSucursalesMed()
# print(lista_sucursales)
atenderPacientes()
# print(lista_sucursales)
mostrarSucursalMenor()
mostrarSucursalMayor()
mostrarPorcionPorcentual()