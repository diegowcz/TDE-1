#Exercício 17: Loja de Tintas

#● Peça o tamanho em metros quadrados da área a ser pintada. 

# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros (R$ 80,00). 

# Informe ao usuário se ele precisa de apenas uma lata ou mais de uma.

area = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
litros = area / 3
if litros <= 18:
    print("Você precisa de apenas uma lata de tinta")
else:    
    latas = litros / 18 
    print(f"Você precisa de {latas:.2f} latas de tinta")
         