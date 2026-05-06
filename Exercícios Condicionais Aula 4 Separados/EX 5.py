#Exercício 5: Par ou Ímpar

#Peça ao usuário que digite um número inteiro.

#● Use o operador de resto (%) para verificar se o número é par ou ímpar.

#● Exiba a mensagem correspondente

numero = int (input("Digite algum número inteiro: "))
numero = numero % 2

if numero == 0:
    print("O número é par!")
else:
    print("O número é impar!")