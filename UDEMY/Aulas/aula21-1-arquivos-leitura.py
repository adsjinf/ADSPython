with open('cadastro.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        id_linha = linha[0:5]
        nome = linha[5:55].strip()
        telefone = linha[55:].strip()

        print(f"ID: {id_linha} | Nome: {nome} | Telefone: {telefone}")
