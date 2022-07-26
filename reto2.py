"""
Es igual que el reto 1, la diferencia es que necesitamos contar cuantos hay de cada uno
y así entonces, con un ciclo del total de veces que se indique, leer cada nivel de riesgo
y contarlo por cuanto se detecte la digitación deuno de ellos
El número de lecturas que el dispositivo tendrá en cuenta debe ser una variable de entrada.

       Clasificación 
    IRCA (%) 	            Nivel de riesgo	
    80 - 100	         INVIABLE SANITARIAMENTE	
    35 - 80	                    ALTO	
    14 - 35	                    MEDIO	
    5 - 14	                    BAJO		
    0 - 5	                 SIN RIESGO	

"""
# Variables de control de la solución
lecturas = int(input()) # Número de lecturas del dispositivo
i = 1 # Iterador desde 1 para evitar una iteración de más
inviable, alto, medio, bajo, sin_riesgo = 0, 0, 0, 0, 0  # Acumuladores de los niveles de riesgo
nivel = ""

while (i <= lecturas):
    nivel = input()
    nivel = nivel.lower()  # Función para convertir a minúscula
    if nivel == "inviable sanitariamente":
        inviable += 1
    elif nivel == "alto":
        alto += 1
    elif nivel == "medio":
        medio += 1
    elif nivel == "bajo": 
        bajo += 1
    elif nivel == "sin riesgo":
        sin_riesgo += 1
    
    i += 1 # Para avanzar en el ciclo y las veces de lectura

# Imprimir los resultados finales
print("0-5 ", sin_riesgo)
print("5-14 ", bajo)
print("14-35 ", medio)
print("35-80 ", alto)
print("80-100 ", inviable)