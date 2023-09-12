#Exercício 16
temperatura = int(input('Digite a temperatura: '))
unidade = int(input('Selecione a unidade de medida: \n 1-Celsius \n 2-Fahrenheit \n'))

if unidade == 1:
    print(f'{temperatura}°C equivale a {(temperatura * 9/5) + 32}°F')
elif unidade == 2:
    print(f'{temperatura}°F equivale a {(temperatura - 32) * 5/9}°C')
else:
    print('Unidade inválida')