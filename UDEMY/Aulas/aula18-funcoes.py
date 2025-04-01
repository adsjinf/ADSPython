def mostrarNaTela():
    print('Ola mundo!')
    print('Fim do programa')

def somaNumeros(n1, n2):
    print(f'A soma dos números é {n1+n2}')

def retornaMaior(*list):
    print(list)
    print(max(list))

mostrarNaTela()

somaNumeros(10, 20)

retornaMaior(1, 3, 5, 6, 10, 80, 11)