lista = ['Fabricio Daniel', 9.5, 9.0, 8.0, True]

#coletando dados através do indices
print(lista[0])
print(lista[1])
print(lista[-1]) #acesso ao último elemento da lista

#acessando elementos com o laço for
for elemento in lista:
    print(elemento)

#atualizando um elemento da lista
lista[3] = 10
print(lista)

#calcular a média com os valores da lista
media = (lista[1] + lista[2] + lista[3])/3
print(media)

# uma string é uma lista

linguagem = 'Python'

print(len(linguagem))
print(linguagem[0])
print(linguagem[1])
print(linguagem[2])
print(linguagem[3])
print(linguagem[4])
print(linguagem[5])

#transformar uma string(frase) em lista
duvida = 'Quem veio antes? O ovo? Ou foi a serpente?'
lista_palavras = duvida.split('?')
print(lista_palavras)

#se não definirmos limitador no split(), a string será segregada por todos os espaços em branco no texto.
duvida = 'Quem veio antes? O ovo? Ou foi a serpente?'
lista_palavras = duvida.split()
print(lista_palavras)

# a função join() transforma uma lista em uma string. Na funçãio join() temos que definir um inificador.
misturas = ['Tintas: vermelho, azul e amarelo',
            'Verde: mistura de azul e amarelo',
            'Laranja: mistura de vermelho e amarelo',
            'Roxo: mistura de vermelho e azul']
unificador = '. '
string_misturas = unificador.join(misturas)
print(string_misturas)