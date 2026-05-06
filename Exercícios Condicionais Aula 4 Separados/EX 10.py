#Exercício 10: Múltiplo de 5

#● Peça um número ao usuário e informe se ele é um múltiplo de 5.

numero = float(input("Informe um número: "))
div = numero % 5
if div == 0:
    print(f"Seu numero ({numero}) é divisivel por 5")
else:
    print(f"Seu número ({numero}) não é divisivel por 5")
    