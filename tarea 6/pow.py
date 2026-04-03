# pow.py
# Este programa calcula la potencia de un número

# Pedir al usuario la base y el exponente
base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

# Calcular la potencia usando el operador **
resultado = base ** exponente

# Mostrar el resultado
print(f"{base} elevado a la {exponente} es: {resultado}")