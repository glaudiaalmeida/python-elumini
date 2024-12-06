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

#função len() - tamanho da lista
print(len(lista))

#fazer partição de listas - muito usado em BD
#sintaxe: lista[inicio:fim] - tenho que inserir no fim o indice desejado somando 1

print(f'As notas do {lista[0]}  são: {lista[1:4]}')

#posso definir até onde quero da lista ou a partir de onde.
#Até onde:
print(lista[:3])

#a partir de:
print(lista[3:])

#exibir toda lista
print(lista[:])

#métodos:

#append() - adiciona um elemento ao final da lista
lista.append(media)
print(lista)

#extend() - adiciona elementos ao final da lista - aqui adiciona vários elementos de uma única vez
lista.extend([10.0, 8.0, 9.0])
print(lista)

#remove() - remove um elemento da lista
lista.remove(10.0)
print(lista)

raca_caes = ['Labrador Retriever', 'Bulldog Francês', 'Pastor Alemão', 'Poodle']
print(raca_caes)

#insert() - insere um elemento em um determinado indice da lista.
#sintaxe: lista.insert(indice, elemento)
raca_caes.insert(1, 'Golden Retriever')
print(raca_caes)

#pop() - remove o elemento de uma determinada posição da lista
raca_caes.pop(1)
print(raca_caes)

#index() - retorna o indice de um elemento especifico da lista
print(raca_caes.index('Poodle'))

#sort() - organiza os elementos da lista em ordwem crescente ou decrescente.
raca_caes.sort()
print(raca_caes)