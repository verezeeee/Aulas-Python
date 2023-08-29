nivelAlerta = int(input('Qual o nível do alerta? '))
if nivelAlerta > 10:
    print('Insira um número entre 0 e 10.')
elif nivelAlerta < 0:
    print('Insira um número entre 0 e 10.')
if nivelAlerta >= 0 and nivelAlerta <= 3:
    print('O nível de alerta é BAIXO')
elif nivelAlerta <= 6:
    print('O nível de alerta é MÉDIO')
elif nivelAlerta <=9:
    print('O nível de alerta é ALTO')
else:
    print("O nível é GRAVE")