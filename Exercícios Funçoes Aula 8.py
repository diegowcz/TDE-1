# EXERCICIOS FUNCOES - AULA 8

# Ex 1 ->

# def somar(a, b):
#     return a + b
#
# print(somar(10, 5))

#---------------------------------------------------
# Ex 2 ->

# def multiplicar(a, b):
#     return a * b
#
# print(multiplicar(10, 5))

#---------------------------------------------------
# Ex 3 ->

# def mensagem(nome):
#     print(f"Olá, {nome}")
#
# mensagem("Heitor")

#---------------------------------------------------
# Ex 4 ->
#
# def maior(a, b):
#     return max(a, b)
#
# print(maior(10, 5))

#---------------------------------------------------
# Ex 5 ->
#
# def dividir(a, b):
#     quoc = a / b
#     resto = a % b
#     return f"Quociente: {quoc}\nResto: {resto}"
#
# print(dividir(10, 3))

#---------------------------------------------------
# Ex 6 ->

# def par_ou_impar(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# n = int(input("Digite um número inteiro: "))
# if par_ou_impar(n):
#     print(f"{n} é par")
# else:
#     print(f"{n} é impar")

#---------------------------------------------------
# Ex 7 ->
# Resp: Retorna None

#---------------------------------------------------
# Ex 8, 9, 10 ->

# def apresentar(nome, cidade, idade):
#     print(f"Nome: {nome}")
#     print(f"Cidade: {cidade}")
#     print(f"Idade: {idade}")
#
# apresentar("Ana", "Curitiba", 20)

#---------------------------------------------------
# Ex 11 ->

# def saudacao(nome, periodo="dia"):
#     if periodo == "noite":
#         cumprimento = "Boa noite"
#     else:
#         cumprimento = f"Bom {periodo}"
#     print(f"{cumprimento}, {nome}")
#
# nome = input("Digite seu nome: ")
# saudacao(nome)

#---------------------------------------------------
# Ex 12 ->

# def saudacao(nome="Dudeck", periodo="dia"):
#     if periodo == "noite":
#         cumprimento = "Boa noite"
#     else:
#         cumprimento = f"Bom {periodo}"
#     print(f"{cumprimento}, {nome}")
#
# nome = input("Digite seu nome: ")
# periodo = input("Periodo (dia/tarde/noite): ")
# saudacao(nome, periodo)

#---------------------------------------------------
# Ex 13 ->
# Se a funcao tem dois argumentos, e apenas um deles tem um
# valor padrao, ele tem que ser sempre o segundo
# def exemplo(b, a=1):

#---------------------------------------------------
# Ex 14 ->

# def somar_todos(*numeros):
#     return sum(numeros)
#
# print(somar_todos(1, 2, 3, 4, 5))

#---------------------------------------------------
# Ex 15 ->

# def mostrar_dados(**dados):
#     for k,v in dados.items():
#         print(f"{k}: {v}")
#
# mostrar_dados(dado_1=1, dado_2=2, dado_3=3)

#---------------------------------------------------
# Ex 16 ->
# *args transforma os argumentos em uma lista
# **kwargs transforma os argumentos em um dicionario

#---------------------------------------------------
# Ex 17 ->
# Output:
# 5
# 10

#---------------------------------------------------
# Ex 18 ->

# contador = 0
#
# def incrementar(contador):
#     return contador + 1
# contador = incrementar(contador)
# print(contador)

#---------------------------------------------------
# Ex 19 ->

# def triplo(x):
#     return x * 3
#
# print(triplo(10))

#---------------------------------------------------
# Ex 20 ->
from tokenize import Triple


def executar(funcao, valor):
  return funcao(valor)

print(executar(Triple, 5))