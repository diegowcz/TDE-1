#Exercício 18: Aprovação de Empréstimo

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 

#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 

#A prestação mensal não pode exceder 30% do salário ou o empréstimo será negado.

#Na sequência, classifique as estruturas condicionais dos algoritmos desenvolvidos em: 
#estrutura condicional simples, estrutura condicional composta e estrutura condicional aninhada e justifique.

valor_casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salário do comprador: "))  
anos = int(input("Informe em quantos anos ele vai pagar: "))
prestacao_mensal = valor_casa / (anos * 12) 
if prestacao_mensal > (salario * 0.3):
    print("Empréstimo negado")
else:
    print("Empréstimo aprovado")

#Estrutura condicional composta, 
#pois há uma condição (prestação mensal) que é comparada a outra (30% do salário) e dependendo do resultado, 
#o programa executa um bloco de código (empréstimo negado ou aprovado).
