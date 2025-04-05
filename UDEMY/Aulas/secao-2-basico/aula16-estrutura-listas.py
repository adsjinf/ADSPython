x = []

for i in range(1, 11):
    x.append(i)
print(x)
print('='*20)

x = list(range(2, 11,2))
print(x)
print('='*20)

x = [1, 2, 3, 4, 5]
print(x)
y = int(input('Digite um numero para apagar da lista: '))
if y in x:
    x.remove(y)
    print(f'O número {y} foi removido da lista')
else:
    print(f'Número {y} não consta na lista')
print(x)