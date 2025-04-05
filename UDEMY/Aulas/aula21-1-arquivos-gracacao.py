dados = [
    ('Ana Maria', '(11) 91234-5678'),
    ('Bruno Silva', '(21) 99876-5432'),
    ('Carlos Alberto', '(31) 98765-4321'),
    ('Daniela Souza', '(41) 97654-3210'),
    ('Eduardo Lima', '(51) 96543-2109'),
    ('Fernanda Costa', '(61) 95432-1098'),
    ('Gustavo Rocha', '(71) 94321-0987'),
    ('Helena Martins', '(81) 93210-9876'),
    ('Igor Ferreira', '(91) 92109-8765'),
    ('Juliana Dias', '(31) 91098-7654')
]

with open('cadastro.txt', 'w', encoding='utf-8') as arquivo:
    for i, (nome, telefone) in enumerate(dados, start=1):
        id_formatado = str(i).zfill(5)                 # ID com zeros à esquerda
        nome_formatado = nome.ljust(50)               # Nome com 50 caracteres, espaços à direita
        linha = f"{id_formatado}{nome_formatado}{telefone}\n"
        arquivo.write(linha)
