"""Função .format()
Esse operador de formatação permite a inserção de variáveis em pontos específicos na string
com o operador %. Esse operadorv funciona como um marcador, informando onde o valor da
variável vai ser exposto na string.
O % precisa ser acompanhado de uma palavra-chave para cada tipo de variável que se deseja
adicionar conforme tabela:
string => %s
inteiro => %d
float => %f
caractere => %c

Desse modo para inserirmos uma variável, podemos adicionar o operador pela string no ponto
desejado. Após o fim da string, adicionamos novamente o %, mas agora especificando a variável
entre parenteses. conforme exemplo abaixo.
"""

nome_aluno = 'Fabricio Daniel'
print('Nome do aluno: %s' %(nome_aluno))

"""Caso tenha mais de uma variável, devemos ordená-las conforme seu surgimento no texto e 
separá-las por vírgula"""

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é %s, ele tem %d anos e sua média é %f.'
      %(nome_aluno, idade_aluno, media_aluno))

"""Quando trabalhamos com pontos flutuantes(float), podemos determinar a quantidade de casas
decimais após a vírgula usando sintaxe %f, na qual x é o número de casas desejadas.
Utilizando as mesmas variáveis do exemplo anterior, o código com %.xf fica da seguinte
maneira:"""

print('Nome do aluno é %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno, idade_aluno, media_aluno))

