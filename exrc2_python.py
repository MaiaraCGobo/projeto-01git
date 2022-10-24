# https://wiki.python.org.br/EstruturaSequencial
# EstruturaSequencial

# Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Alo mundo!')

# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
n1 = int(input('Digite um numero: '))
print('O numero informado foi ', n1)

# Faça um Programa que peça dois números e imprima a soma.
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
r = n1+n2
print('O resultado da soma dos dois numeros foi ', r)

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input('Digite a primeira bimestral nota: '))
nota2 = float(input('Digite a segunda bimestral nota: '))
nota3 = float(input('Digite a terceira bimestral nota: '))
nota4 = float(input('Digite a quarta bimestral nota: '))
media = nota1+nota2+nota3+nota4/4
print('A media foi de: ', media)

# Faça um Programa que converta metros para centímetros.
# 1 metro e = a 100cm
metros = float(input('Metros? '))
centimetros = metros * 100
print(centimetros, ' cm')
