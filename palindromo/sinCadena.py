def esPalindromoSinCadena(x):
    if x < 0:
        return False
    
    arr = []
    temp = x
    
    while temp > 0:
        digito = temp % 10
        arr.append(digito)
        temp = temp // 10
    
    i = 0
    j = len(arr) - 1
    
    while i <= j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    
    return True


print(esPalindromoSinCadena(121))   # True
