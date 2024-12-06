"""Os operadores de formatação de strings com % não funcionam diretamente com valores
booleanos. Uma maneira de lidar com isso é convertendo o valor booleano para uma string
antes de usá-lo na formatação com a função str().
Por exemplo:
"""
x = True
print("O valor de x: %s" % str(x))