"""
1 - Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a
soma dos dois valores.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('A soma entre ', num1, ' e ', num2, 'é: ', num1 + num2)

2 - Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a
 soma dos três valores.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
print(num1, ' + ', num2, ' + ', num3 ' = ', num1 + num2 + num3)

3 - Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a
 subtração do primeiro pelo o segundo valor.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('A diferença entre ', num1, ' e ', num2, 'é: ', num1 - num2)

4 - Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a
multiplicação dos dois valores.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('A multiplicação entre ', num1, ' e ', num2, 'é: ', num1 * num2)

5 - Crie um programa que solicite dois valores numéricos, um numerador e um denominador,
e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não
pode ser 0.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num2 == 0:
    num2 = int(input('Digite um numero diferente de zero: '))
calculo = num1 / num2
print('A divisão entre ', num1, ' e ', num2, 'é: ', calculo)

6 - Crie um programa que solicite dois valores numéricos, um operador e uma potência,
e realize a exponenciação entre esses dois valores.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
oper = input('Digite qual operação realizar: ')
valorPotencia  = int(input('Digite qual valor usaremos para exponenciar: '))
calculoPotencia = float(num1**valorPotencia)
print('O calculo da potencia foi: %s ** %d = %e' %(num1, valorPotencia, calculoPotencia))


7 - Crie um programa que solicite dois valores numéricos, um numerador e um denominador
e realize a divisão inteira entre os dois valores. Deixe claro que o valor do
denominador não pode ser 0.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num2 == 0:
    num2 = int(input('Digite um numero diferente de zero: '))
calculo = float(num1 /num2)
print('%s / %d é: %2.f' %(num1, num2, calculo))

8 - Crie um programa que solicite dois valores numéricos, um numerador e um denominador,
e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do
denominador não pode ser 0.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num2 == 0:
    num2 = int(input('Digite um numero diferente de zero: '))
calculo = num1 % num2
print('O resto da divisão entre %s e %d é: %2.f' %(num1, num2, calculo))

9 - Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = float((nota1 + nota2 + nota3) / 3)
print('Média: %s' %(float(media)))

10 - Crie um código que calcule e imprima a média ponderada dos números
 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

mp = float((5 * 1 + 12 * 2 + 20 * 3 + 15 * 4) / (5 + 12 + 20 + 15))
print("Valor\tPeso\n5\t1\n12\t2\n20\t3\n15\t4")
print('A média ponderada da tabela acima é: %f' %mp)

"""
