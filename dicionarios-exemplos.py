"""
sintaxe:
dicionario = {chave: valor}

dicionario = {
    'chave_1': 1,
    'chave_2': 2
              }

print(dicionario)


usado para armazenar dados
situação: vamos criar um conjunto de dados com informações de matricula de um estudante.
os dados são:
matricula: 2000168933
dia de cadastro: 25
mês de cadastro: 10
turma: 2E 

"""
cadastro = {
    'matricula': 2000168933,
    'dia_cadastro': 25,
    'mes_cadastro': 10,
    'turma': '2E'
}
print(cadastro)
print(cadastro['matricula'])

#É possivel substituir os valores dentro de uma chave.
cadastro['turma'] = '2G'
print(cadastro)

#Podemos inserir novos dados no dicionario
cadastro['modalidade'] = 'EAD'
print(cadastro)

#método pop() - remove um item do dicionario.
cadastro.pop('turma')
print(cadastro)

#método items() - retorna uma lista de pares chave-valor do dicionário
print(cadastro.items())

#metodo keys() - retorna uma lista das chaves do dicionario
print(cadastro.keys())

#método values() - retorna uma lista dos valores do dicionário

print(cadastro.values())

#lendo o dicionário com o laço for => mostra na tela cada chave em uma linha
for chaves in cadastro.keys():
    print(cadastro[chaves])

#ler o dicionario com for e método values
for valores in cadastro.values():
    print(valores)

#ler o dicionario com o laço for passando dois elementos para consulta
for chaves, valores in cadastro.items():
    print(chaves, valores)

#outro exemplo:
loja = {
    'nomes': [ 
        'televisão',
        'celular',
        'notebook',
        'geladeira',
        'fogão'
    ],
    'precos': [
        2000,
        1500,
        3500,
        1500
    ]
}

for chave, elementos in loja.items():
    print(f'Chave: {chave}\nElementos:')
    for dado in elementos:
        print(dado)
    