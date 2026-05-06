#Exercício 11: Categorias de Atleta

#Solicite a idade de um nadador e classifique-o:

#● 5 a 7 anos: Infantil A.

#● 8 a 10 anos: Infantil B.

#● 11 a 13 anos: Juvenil A.

#● 14 a 17 anos: Juvenil B.

#● Maiores de 18: Adulto.

idade = int(input("Informe sua idade: "))
if idade>18:
    print("Adulto")
elif 17>= idade >=14:
    print("Juvenil B")
elif 13 >= idade >= 11:
    print("Juvenil A")
elif 10 >= idade >= 8:
    print("Infantil B")
elif 7>= idade >=5:
    print("Juvenil A")
else:
    print("idade inválida")
