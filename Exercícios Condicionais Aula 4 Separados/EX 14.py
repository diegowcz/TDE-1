#Exercício 14: Aumento Salarial

#Peça o salário de um funcionário.

#● Se o salário for superior a R$ 1.621,00, calcule um aumento de 10%.

#● Para inferiores ou iguais, o aumento é de 15%.

salario = float(input("Informe seu salário: "))
if salario > 1621:
    aumento = salario * 1.1
    print(f"salario com aumento igual a {aumento}")
else:
    aumento = salario * 1.15
    print(f"salario com aumento igual a {aumento}")