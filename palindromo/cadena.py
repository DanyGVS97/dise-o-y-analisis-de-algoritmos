def esPalindromoConCadena(x):
    if x < 0:
        return False
    
    cadena = str(x)
    i = 0
    j = len(cadena) - 1
    
    while i <= j:
        if cadena[i] != cadena[j]:
            return False
        i += 1
        j -= 1
    
    return True


print(esPalindromoConCadena(121))   # True
