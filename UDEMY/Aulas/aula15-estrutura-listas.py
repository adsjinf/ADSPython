
'''
Criação de lista
minha_lista = [1, 2, 3, 4, 5]  # Cria uma lista com números
lista_vazia = []              # Lista vazia

Adição de elementos
minha_lista.append(6)        # Adiciona o elemento 6 no final da lista
minha_lista.insert(2, 99)    # Insere o número 99 na posição 2
minha_lista += [7, 8]        # Adiciona múltiplos elementos usando operador +

Remoção de elementos
minha_lista.remove(99)       # Remove o primeiro elemento com valor 99
minha_lista.pop()            # Remove e retorna o último elemento
minha_lista.pop(1)           # Remove e retorna o elemento da posição 1
minha_lista.clear()          # Remove todos os elementos da lista

Busca e informações
minha_lista = [10, 20, 30, 40, 50]
print(minha_lista.index(30))   # Retorna o índice do elemento 30
print(40 in minha_lista)       # Verifica se 40 está na lista (True/False)
print(minha_lista.count(20))   # Conta quantas vezes 20 aparece na lista
print(len(minha_lista))        # Tamanho da lista (número de elementos)

Ordenação e inversão
minha_lista.sort()             # Ordena a lista (em ordem crescente por padrão)
minha_lista.sort(reverse=True) # Ordena em ordem decrescente
minha_lista.reverse()          # Inverte a ordem dos elementos

Acesso a elementos
print(minha_lista[0])        # Acessa o primeiro elemento
print(minha_lista[-1])       # Acessa o último elemento
print(minha_lista[1:4])      # Fatiamento: do índice 1 ao 3 (exclui o 4)

Cópia de listas
nova_lista = minha_lista.copy()     # Faz uma cópia independente da lista
nova_lista = list(minha_lista)      # Outra forma de copiar

Listas com outros tipos
lista_mista = [1, "texto", 3.14, True]  # Pode ter diferentes tipos de dados

Percorrer lista com loop
for item in minha_lista:
    print(item)                  # Percorre cada item da lista

for i in range(len(minha_lista)):
    print(minha_lista[i])        # Percorre usando índices

Compreensão de listas (List Comprehension)
quadrados = [x**2 for x in range(10)]  # Cria lista com os quadrados de 0 a 9
pares = [x for x in range(10) if x % 2 == 0]  # Filtra apenas os pares

Concatenar listas
a = [1, 2]
b = [3, 4]
c = a + b             # Resultado: [1, 2, 3, 4]
a.extend(b)           # Adiciona todos os elementos de b em a

Converter outras estruturas em lista
lista_de_string = list("python")     # ['p', 'y', 't', 'h', 'o', 'n']
lista_de_tupla = list((1, 2, 3))     # [1, 2, 3]

append
insert(0, 'x')
pop(1)
remove('x')
len()
sort()
reverse

max()
min()
sum()
'''

idade =[18, 20, 30, 40, 15]
print(idade)
idade.insert(0,'x')
print(idade)
idade.remove('x')
print(idade)
print(len(idade))
idade.sort()
print(idade)
idade.sort(reverse=True)
print(idade)
print(min(idade))
print(max(idade))
print(sum(idade))
