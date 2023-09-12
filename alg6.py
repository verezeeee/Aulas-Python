#Exercício 8 e 9
import math
arr = [float(input('Digite o valor do lado a do triângulo: ')), float(input('Digite o valor do lado b do triângulo: ')), float(input('Digite o valor do lado c do triângulo: '))]

a = arr[0]
b = arr[1]
c = arr[2]

def verificarTriangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
if verificarTriangulo(a, b, c) == True and a == b == c:
    print('O triângulo é equilátero!!!')
elif verificarTriangulo(a, b, c) == True and a == b or b == c or a == c:
    print('O triângulo é isósceles!!!')
elif verificarTriangulo(a, b, c) == True and a != b != c:
    print('O triângulo é escaleno!!!!')
else:
    print('Não é um triângulo!!')
    sp = (a+b+c)/2
    area = math.sqrt(sp * (sp - a) *(sp - b)*(sp - c))
print(f'A área do triangulo = {area}')