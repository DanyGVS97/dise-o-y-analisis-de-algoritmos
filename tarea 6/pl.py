# gregory_leibnitz.py
# Aproximación de pi usando la serie de Gregory-Leibnitz

# Pedir al usuario el número de términos
N = int(input("Ingresa el número de términos: "))

# Inicializar la suma
pi_aprox = 0

# Calcular la serie
for n in range(N):
    pi_aprox += ((-1) ** n) / (2 * n + 1)

# Multiplicar por 4
pi_aprox *= 4

# Mostrar el resultado
print(f"Aproximación de pi con {N} términos: {pi_aprox}")