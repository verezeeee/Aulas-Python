#Exercício 19
valor = float(input('Digite o valor total em reais: '))
prestacoes = int(input('Digite o número de prestações desejadas: '))
if prestacoes >= 12 and prestacoes < 24:
    print(f'O valor de cada prestação é de R${valor/prestacoes:.2f}')
elif prestacoes >= 24 and prestacoes < 36:
    print(f'O valor de cada prestação é de R${(valor*1.1)/prestacoes:.2f}')
elif prestacoes >= 36:
    print(f'O valor de cada prestação é de R${(valor*1.15)/prestacoes:.2f}')
else:
    print('Número de prestações inválido')
