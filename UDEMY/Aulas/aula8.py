nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2
nome = nome.lower().title()

if media >= 6 and idade >= 18:
    print('O aluno ' + nome + f' foi aprovado com a media {media}')
else:
    print('O aluno ' + nome + f' foi reprovado com a media {media}')