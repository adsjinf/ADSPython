
try:
    x = int(input('Digite sua idade: '))
except:
    print('Você não digitou a sua idade.')
else:
    print(f'Sua idade é {x}')
finally:
    print('Muito obrigado por acessar este programa.')