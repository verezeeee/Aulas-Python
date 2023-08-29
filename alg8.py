animais = ['pato', 'águia', 'galinha', 'avestruz', 'pinguim', 'morcego', 'ornitorrinco', 'leão', 'gato', 'onça pintada', 'baleia', 'tubarão', 'lambari', 'enguia', 'arraia']
print(f'Pense em um animal dessa lista: \n {animais}')
ave = int(input('O animal é uma ave? \n 1-Sim \n 2-Não \n'))
if ave == 1:
    nada = int(input('O animal é aquático? \n 1-Sim 2-Não \n'))
    if nada == 1:
        neve = int(input('O habitat natural do animal é a Antártida? \n 1-Sim \n 2-Não \n'))
        if neve == 1:
            print('Seu animal é um pinguim!!')
        else:
            print('O seu animal é um pato!')
    else:
        