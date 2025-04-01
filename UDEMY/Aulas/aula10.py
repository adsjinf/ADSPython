x=1
while x<11:
    print(x)
    x = x +1
print('acabou o laço')

desicao=0
while desicao !=3:
    desicao = int(input('Digite 1 para loga, 2 para cadastrar e 3 para sair '))

    if desicao == 1:
        print('Logando')
    elif desicao == 2:
        print('Cadastrando')
