#Exercício 15: Simulador de Radar

#Pergunte ao usuário a velocidade de um carro.

#● Se ultrapassar 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. A multa custa R$ 7,00 por cada km acima do limite.

velocidade = float(input("Informe a velocidade de um carro: "))
if velocidade>80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado, a multa vai custar: R${multa}")
else:
    print("Sem Infrações")