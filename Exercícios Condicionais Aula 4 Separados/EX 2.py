#Exercício 2: Positivo, Negativo ou Zero

#● Se o número for menor que zero, exiba: "O número X é negativo."

#● Senão, exiba: "O número é Zero."

numero= int(input("Informe um número inteiro: "))
if numero > 0:
    print(f"O número {numero} é Positivo.")
elif numero < 0:
    print(f"O número {numero} é Negativo.")
else:
    print("O número é Zero.")
