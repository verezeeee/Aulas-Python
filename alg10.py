#Exercício 15
matricula = int(input('Digite o número da matrícula: '))
nome = input('Digite o nome completo do aluno: ')
genero = int(input('Selecione o gênero do aluno: \n 1-Masculino \n 2-Feminino \n'))
curso = int(input('Selecione o curso do aluno: \n 1-Bacharelado em Engenharia de Software \n 2-Bacharelado em Engenharia de Computação \n 3-Análise e Desenvolvimento de Sistemas \n'))
coeficiente = int(input('Digite o coeficiente de rendimento do aluno: '))

print(f'Matrícula: {matricula} \n Nome: {nome} \n Gênero: {genero} \n Curso: {curso} \n Coeficiente: {coeficiente}')
#Condições para o coeficiente de rendimento	
if coeficiente >= 90 and coeficiente <= 100:
    print('Excelente')
elif coeficiente >= 70 and coeficiente < 90:
    print('Bom')
elif coeficiente >= 50 and coeficiente < 70:
    print('Regular')
elif coeficiente >= 30 and coeficiente < 50:
    print('Necessita melhoras')
elif coeficiente >= 0 and coeficiente < 30:
    print('Preocupante')
else:
    print('Coeficiente inválido')

