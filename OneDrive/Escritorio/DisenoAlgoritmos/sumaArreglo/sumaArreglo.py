def sumArray(arr, n):
    # Inicializar la suma en 0
    suma = 0
    
    # Iterar desde i = 0 hasta n - 1
    for i in range(n):
        suma = suma + arr[i]
    
    # Devolver el resultado
    return suma

# Ejemplo de uso
numeros = [3, -2, 5, 0, 1]
print(sumArray(numeros, len(numeros)))  # Resultado: 7
