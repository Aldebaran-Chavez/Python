#Ejemplo de un proceso

def calcular_suma(n):
    suma = 0
    for i in range (1, n+1):
        suma += i
    return suma

resultado = calcular_suma(100000)

print (resultado)