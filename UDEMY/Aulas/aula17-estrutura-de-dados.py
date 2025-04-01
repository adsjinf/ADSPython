x = {'nome': 'Caio', 'idade': 18, 'telefone': '1234-1234'}

print(x)
print(x['telefone'])
print(len(x))
x.pop('idade')
print(x)

cadastroPessoas = [
    {'nome': 'Caio', 'idade': 18, 'telefone': '1234-1234', 'cpf': '12345678901'},
    {'nome': 'Ana', 'idade': 25, 'telefone': '9876-5432', 'cpf': '23456789012'},
    {'nome': 'Bruno', 'idade': 32, 'telefone': '8765-4321', 'cpf': '34567890123'},
    {'nome': 'Fernanda', 'idade': 29, 'telefone': '7654-3210', 'cpf': '45678901234'},
    {'nome': 'Lucas', 'idade': 21, 'telefone': '6543-2109', 'cpf': '56789012345'},
    {'nome': 'Juliana', 'idade': 40, 'telefone': '5432-1098', 'cpf': '67890123456'}
]

print(cadastroPessoas)
print(cadastroPessoas[0])
print(cadastroPessoas[0]['nome'])

'''Lista os nomes cadastrados'''
for pessoa in cadastroPessoas:
    print(pessoa['nome'])
