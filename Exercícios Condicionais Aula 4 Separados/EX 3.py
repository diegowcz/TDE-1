#Exercício 3: O Desconto do Cliente

#Peça ao usuário que digite o valor total de uma compra (use float() ).

#● Se o valor da compra for maior que R$ 100.00, aplique um desconto de 10% e mostre o valor final a ser pago.

#● Se for menor ou igual a R$ 100.00, o cliente não ganha desconto. Exiba o
#valor normal da compra e uma mensagem: 
#"Nas compras acima de R$ 100, você ganha 10% de desconto!".

valor = float (input("Digite o valor da sua conta: "))
if valor >100:
    desc = (valor * 0.9)
    print(f"valor total igual a: {desc}")
else:
    print(f"valor total igual a: {valor}\n Nas compras acima de R$100, você ganha 10% de desconto")
