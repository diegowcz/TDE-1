#Exercício 6: Comparando Dois Números

#Peça dois números ao usuário.

#● O programa deve informar qual deles é o maior.

#● Caso sejam iguais, o programa também precisará informar

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero1>numero2:
    print(f"O {numero1} é maior que o {numero2}")
elif numero2>numero1:
    print(f"O {numero2} é maior que o {numero1}")
else:
    print(f"O {numero1} é igual ao {numero2}")