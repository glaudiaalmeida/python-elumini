"""
format
É possível também usar o método format() para fazer a formatação de strings.
Ele é mais flexível e permite passar as variáveis diretamente dentro da string,
sem a necessidade dos operadores %. Seus marcadores são apenas as {}.
Exemplo:
"""
nome_aluno = 'Fabrício Daniel'
print('Nome do aluno: {}'.format(nome_aluno))

"""Do mesmo modo que é feito com o operador, conseguimos aplicar com mais variáveis:"""

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é {}, ele tem {} anos e sua média é {}.'
      .format(nome_aluno, idade_aluno, media_aluno))

"""Note que, com o format, não temos o problema das casas decimais do ponto flutuante.
 Esse problema também não é presente no formato f-string.

Em resumo, cada uma dessas formas tem suas vantagens e desvantagens. 
Indico utilizar a forma f-string, pois é mais legível e fácil de usar. Mesmo assim, 
cada pessoa desenvolvedora pode escolher a forma que achar mais apropriada."""
