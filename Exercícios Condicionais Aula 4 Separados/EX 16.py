#Exercício 16: Conversor de Temperatura

#Peça ao usuário uma temperatura em Celsius.

#● Pergunte se o ele quer converter para Fahrenheit (F) ou Kelvin (K).

#● Exiba o resultado da opção escolhida.

#Obs: fórmula para converter de Celsius para Fahrenheit : (°C × 9/5) + 32, fórmula para converter de Celsius para Kelvin: °C + 273,15

temp = float(input("Digite uma temperatura em Celsius: "))
conv = input("Escolha para converter em fahrenheit(F) ou Kelvin(K): ").upper()
if conv == "F":
    far = (temp * 9/5) + 32
    print(f"A temperatura em fahrenheit é {far}")
elif conv == "K":
    kel = temp + 273.15
    print(f"A temperatura em kelvin é {kel}")
else:
    print("Letra inválida")