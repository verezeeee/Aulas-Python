# Exercício 10
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media >= 7:
    print(f'Aluno aprovado com média {media}')
else:
    print(f'Aluno reprovado com média {media}')

# Exercício 11
n1 = float(input('Digite a primeira nota: '))
p1 = float(input('Digite o peso da primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
p2 = float(input('Digite o peso da segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
p3 = float(input('Digite o peso da terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1 * p1 + n2 * p2 + n3 * p3 + n4 * 4) / 10

if media >= 7:
    print(f'Aluno aprovado com média {media}')
else:
    print(f'Aluno reprovado com média {media}')
