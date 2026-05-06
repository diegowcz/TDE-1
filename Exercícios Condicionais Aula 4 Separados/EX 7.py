#Exercício 7: Verificação de Login

#Crie uma variável chamada usuario_correto com o valor "admin".

#● Peça para o usuário digitar um nome de usuário.

#● Se for igual ao armazenado, exiba "Acesso concedido".

#● Caso contrário, "Usuário desconhecido".

while True:

    usuario_correto = "admin"

    usuario = input("Digite o nome do usuário: ").lower()
    if usuario_correto == usuario:
        print("Acesso concedido")
        break
    else:
        print("Acesso negado")
