#Exercício 17 e 18
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and ano > 0 and ano <= 2023:

    print(f'O próximo dia é {dia+1}/{mes}/{ano}')
    print(f'O dia anterior é {dia-1}/{mes}/{ano}')
else:
    print('Data inválida')