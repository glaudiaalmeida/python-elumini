"""
1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input('Digite outro número inteiro: '))
if num_1 < num_2:
    print(num_2)
else: print(num_1)

===========================================================================================
2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e
 informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

percentual = float(input('Digite o percentual de crescimento de produção da empresa: '))
if percentual > 0:
    print('Houve crescimento na produção.')
else:
    print('Houve queda na produção.')

============================================================================================
3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária
 é uma vogal ou consoante.

 vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']
print(vogais)
caractere = input('Digite uma letra qualquer: ')
if caractere in vogais:
    print('A letra que você digitou é uma vogal - f'{caractere}')
elif caractere in consoantes:
    print('A letra que você digitou é uma consoante - f'{caractere}')
else:
    print('O caractere que você digitou é um número, pontuação ou símbolo - f'{caractere}')

============================================================================================
4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos
 consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

preco_ano_1 = float(input('Digite o preço médio do carro no primeiro ano da análise: '))
preco_ano_2 = float(input('Digite o preço médio do carro no segundo ano da análise: '))
preco_ano_3 = float(input('Digite o preço médio do carro no terceiro ano da análise: '))

if preco_ano_1 > preco_ano_2 and preco_ano_1 > preco_ano_3:
    maior_preco = preco_ano_1
elif preco_ano_2 > preco_ano_1 and preco_ano_2 > preco_ano_3:
    maior_preco = preco_ano_2
else:
    maior_preco = preco_ano_3

if preco_ano_1 < preco_ano_2 and preco_ano_1 < preco_ano_3:
    menor_preco = preco_ano_1
elif preco_ano_2 < preco_ano_1 and preco_ano_2 < preco_ano_3:
    menor_preco = preco_ano_2
else:
    menor_preco = preco_ano_3

print(f'O valor mais alto, deste veículo, entre três anos consecutivos foi: R$ {maior_preco:.2f}')
print(f'O valor mais baixo, deste veículo, entre três anos consecutivos foi: R$ {menor_preco:.2f}')

============================================================================================
5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o
 produto mais barato para comprar.
valor_prod_1 = float(input('Digite o valor do primeiro produto: '))
valor_prod_2 = float(input('Digite o valor do segundo produto: '))
valor_prod_3 = float(input('Digite o valor do terceiro produto: '))

if valor_prod_1 < valor_prod_2 and valor_prod_1 < valor_prod_3:
        print("O produto de menor valor para ser comprado é o produto 1.")
elif valor_prod_2 < valor_prod_1 and valor_prod_2 < valor_prod_3:
    print("O produto de menor valor para ser comprado é o produto 2.")
else:
    print("O produto de menor valor para ser comprado é o produto 3.")

============================================================================================
6) Escreva um programa que leia três números e os exiba em ordem decrescente.

num_1 = int(input('Digite o primeiro numero inteiro: '))
num_2 = int(input('Digite o segundo numero inteiro: '))
num_3 = int(input('Digite o terceiro numero inteiro: '))

if num_1 >= num_2 and num_1 >= num_3:
    if num_2 >= num_3:
        print(f"Ordem decrescente: {num_1}, {num_2}, {num_3}")
    else:
        print(f"Ordem decrescente: {num_1}, {num_3}, {num_2}")
elif num_2 >= num_1 and num_2 >= num_3:
    if num_1 >= num_3:
        print(f"Ordem decrescente: {num_2}, {num_1}, {num_3}")
    else:
        print(f"Ordem decrescente: {num_2}, {num_3}, {num_1}")
else:
    if num_3 >= num_2:
        print(f"Ordem decrescente: {num_3}, {num_1}, {num_2}")
    else:
        print(f"Ordem decrescente: {num_3}, {num_2}, {num_1}")

============================================================================================

7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda
("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!",
 ou "Valor Inválido!", conforme o caso.

turno = input('Informe qual turno você estuda: ')

if turno == 'manhã':
    print('Bom dia!!! Bons Estudos!!!')
elif turno == 'tarde':
    print('Boa Tarde!!! Bons Estudos!!!')
else:
    print('Boa Noite!!! Bora focar no sucesso!!')

============================================================================================
8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par
 ou ímpar. Dica: Você pode utilizar o operador módulo %.

num = int(input('Digite um número: '))
if num % 2 == 0:
    print('Você digitou um número par!!!')
else:
    print('Você digitou um número impar!!!')

============================================================================================
9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

numero = input('Digite um número: ')

if '.' in numero:
    print('O número é decimal!')
else:
    print('O número é inteiro!!')

============================================================================================
Momento dos projetos
10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa
usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações
sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

# Coletamos os números a serem operados e solicitamos a operação desejada pela pessoa usuária
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
operacao = input('Informe a operação desejada (+, -, *, /): ')

# Verificamos o operador que foi selecionado e executa a operação matemática conforme a seleção
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else: # Especificamos um resultado caso a pessoa usuária não digite alguma das operações corretamente.
    print('Operação inválida, resultado da operação será 0')
    resultado = 0

#  Fazemos as mesmas verificações das questões anteriores para fazer o relatório do cálculo entre números
if resultado % 1 == 0:
    print('O resultado é inteiro.')
else:
    print('O resultado é decimal.')

if resultado > 0:
    print('O resultado é positivo.')
elif resultado == 0:
    print('O resultado é neutro.')
else:
    print('O resultado é negativo.')

if resultado % 2 == 0:
    print('O resultado é par.')
else:
    print('O resultado é ímpar.')
============================================================================================
11) Escreva um programa que peça à pessoa usuária três números que representam os lados
de um triângulo. O programa deve informar se os valores podem ser utilizados para formar
um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em
mente algumas dicas:

============================================================================================
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes.

# Coletamos os lados de um triângulo
print('Coletaremos os lados de um triângulo.')
lado1 = float(input('Digite o comprimento do primeiro lado: '))
lado2 = float(input('Digite o comprimento do segundo lado: '))
lado3 = float(input('Digite o comprimento do terceiro lado: '))

# Verificamos de os lados formam um triângulo
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print('Os valores podem formar um triângulo!')
    # comparamos os lados para verificar o tipo de triângulo
    if (lado1 == lado2) and (lado2 == lado3):
        print('O triângulo é equilátero.')
    elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
        print('O triângulo é escaleno.')
    else:
        print('O triângulo é isósceles.')
else:
    print('Os valores não podem formar um triângulo!')

============================================================================================
12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se
a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário,
será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros,
o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do
litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um
programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol
e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o
valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela
quantidade de litros menos o valor de desconto resultante do cálculo.

# Coletamos a quantidade de litros e o tipo de combustível,
# já deixando o caractere em maiúsculo para facilitar nossa análise
quantidade_litros = float(input('Informe a quantidade de litros vendidos: '))
tipo_combustivel = input('Informe o tipo de combustível (E para etanol e D para diesel): ').upper()

#  Verificamos primeiro o tipo de combustível
if tipo_combustivel == 'E':
  # Taxamos o valor do preço em litros do etanol
  preco_litro = 1.70
  # De acordo com o valor da quantidade de litros, taxamos também o desconto
  if quantidade_litros <= 15:
    desconto = 0.02
  else:
    desconto = 0.04
elif tipo_combustivel == 'D':
  # Taxamos o valor do preço em litros do disel
  preco_litro = 2.00
  # De acordo com o valor da quantidade de litros, taxamos também o desconto
  if quantidade_litros <= 15:
    desconto = 0.03
  else:
    desconto = 0.05
# Caso ocorra um erro na especificação de tipo de combustível,
# consideramos entradas inválidas, e os preços são taxados em 0
else:
    print('Entradas inválidas!')
    preco_litro = 0
    desconto = 0

# Fazemos o cálculo do valor de desconto, seguido do cálculo do preço descontado
valor_desconto = preco_litro * quantidade_litros * desconto
valor_pago = preco_litro * quantidade_litros - valor_desconto

# Resultado
print(f'Valor a ser pago pelo cliente: R$ {valor_pago}')

============================================================================================
13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de
vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados
de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual.
A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.
# Coletamos as vendas dos dois anos
venda_2022 = float(input('Informe a quantidade de vendas em 2022: '))
venda_2023 = float(input('Informe a quantidade de vendas em 2023: '))

# Calculamos a variação percentual entre as vendas dos anos de 2022 e 2023
var_percentual = 100 * (venda_2023 - venda_2022) / (venda_2022)

# Análise condicional da variação percentual para determinar a sugestão a ser enviada
if var_percentual > 20:
    print('Bonificação para o time de vendas.')
elif 2 <= var_percentual <= 20:
    print('Pequena bonificação para time de vendas.')
elif -10 <= var_percentual < 2:
    print('Planejamento de políticas de incentivo às vendas.')
else:
    print('Corte de gastos.')

============================================================================
14 - exercicio da IA - testar se é decimal ou inteiro

# Solicita um número ao usuário
numero = float(input("Digite um número: "))

# Verifica se o número é inteiro ou decimal
if numero == int(numero):  # Se o número for igual à sua versão inteira, é inteiro
    print("O número é inteiro.")
else:
    print("O número é decimal.")
"""

