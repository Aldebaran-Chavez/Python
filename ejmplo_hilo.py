import threading

def calcular_suma(inicio, fin, resultado, index):
    suma = 0
    for i in range(inicio, fin):
        suma += i
    resultado[index] = suma

n = 10
mitad = n // 2

# Usamos una lista para almacenar los resultados de los hilos
resultado = [0, 0]

# Creamos dos hilos
hilo1 = threading.Thread(target=calcular_suma, args=(1, mitad + 1, resultado, 0))
hilo2 = threading.Thread(target=calcular_suma, args=(mitad + 1, n + 1, resultado, 1))

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperamos a que los hilos terminen
hilo1.join()
hilo2.join()

# Obtener los resultados de los hilos y sumarlos
total_suma = sum(resultado)
print(f"La suma total es: {total_suma}")