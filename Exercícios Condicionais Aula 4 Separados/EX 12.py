#Exercício 12: Calculadora de Viagem

#Pergunte a distância que um passageiro deseja percorrer em km.

#● Calcule o preço da passagem:

#● Cobrando R$ 0,50 por km para viagens de até 200km.

#● Cobrando R$ 0,45 para viagens mais longas.

distancia = float(input("Qual distancia deseja percorrer? "))
if distancia > 200:
    custo = distancia * 0.5
    print(f"Sua viagem custará R${custo}")
else:
    custo = distancia * 0.45
    print(f"Sua viagem custará R${custo}")

    