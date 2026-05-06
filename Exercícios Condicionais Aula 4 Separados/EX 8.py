#Exercício 8: Calculadora de IMC Simples

#Peça o peso e a altura do usuário.

#● Calcule o IMC ($peso / altura^2$).

#● Se o IMC for maior que 25, exiba "Acima do peso ideal".

#● Caso contrário, exiba "Peso dentro da normalidade".

peso = float(input("Digite o peso do usuário: "))
altura = float(input("Digite a altura do usuário: "))

soma = peso / (altura**2)
print(soma)
if soma > 25:
    print("O usuário está acima do peso ideal")
else:
    print("O usuário está com o peso dentro da normalidade ")