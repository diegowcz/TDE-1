#Exercício 13: Verificação de Ano Bissexto

#● Peça ao usuário um ano (ex.: 2024).

#● Informe se ele é bissexto (divisível por 4).

ano = int(input("Escreva um ano: "))
bissexto = ano % 4
if bissexto == 0:
    print("Esse é um ano bissexto!")
else:
    print("Não é um ano bissexto")