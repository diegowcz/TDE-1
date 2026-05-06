#Exercício 9: Classificação de Triângulos

#Peça os três lados de um triângulo ao usuário e verifique:

#● Se todos os lados forem iguais: "Equilátero".

#● Se apenas dois forem iguais: "Isósceles".

#● Se todos forem diferentes: "Escaleno".

lado1 = float(input("Informe o primeiro lado do triangulo: "))

lado2 = float(input("Informe o segundo lado do triangulo: "))

lado3 = float(input("Informe o terceiro lado do triangulo: "))

if lado1==lado2==lado3:
    print("Triangulo Equilátero")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print("Triangulo Isóceles")
else:
    print("Triangulo Escaleno")
    