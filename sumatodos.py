def sumaTodo(limit):
    resultado = 0
    for i in range (0,limit +1):
        resultado +=i
    return resultado

def sumaTodoCuadrado(limit):
    result = 0
    for i in range (0,limit +1):
        result += i*i
    return result

print(sumaTodo(100))
print(sumaTodoCuadrado(3))