#Exercício 7
arr = [int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: '))]
        

if arr[0] != 0 and (arr[0] % arr[1] == 0):
    print(f'{arr[0]} é múltiplo de {arr[1]}')
            
if arr[1] != 0 and arr[1] % arr[2] == 0:
    print(f'{arr[1]} é múltiplo de {arr[2]}')

if arr[2] != 0 and arr[2] % arr[0] == 0:
    print(f'{arr[2]} é múltiplo de {arr[0]}')
            

if arr[0] != 0 and (arr[1] % arr[0] == 0):
    print(f'{arr[1]} é múltiplo de {arr[0]}')
            
if arr[1] != 0 and arr[2] % arr[1] == 0:
    print(f'{arr[2]} é múltiplo de {arr[1]}')

if arr[2] != 0 and arr[0] % arr[2] == 0:
    print(f'{arr[0]} é múltiplo de {arr[2]}')
            

