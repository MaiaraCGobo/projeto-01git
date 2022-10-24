# https://wiki.python.org.br/EstruturaDeDecisao
# EstruturaDeDecisao

# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('O numero', n1, 'e maior que', n2)
if n1 < n2:
    print('O numero', n1, 'nao e maior que', n2)
if n1 == n2:
    print('Os numeros sao iguais.')

# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

v1 = int(input('Digite um numero: '))
if v1 >= 0:
    print('O numero', v1, 'e positivo.')
else:
    print('O numero', v1, 'e negativo.')

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
