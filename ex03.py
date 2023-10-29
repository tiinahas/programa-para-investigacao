# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a) "Telefonou para a vítima?"
# b) "Esteve no local do crime?"
# c) "Mora perto da vítima?"
# d) "Devia para a vítima?"
# e) "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita".
# Entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

print("Olá, vamos começar? Preciso fazer algumas perguntas.")
nome = input("Qual o seu nome?")
idade = input ("Qual sua idade?")
telefonar = input("Telefonou para a vitima?")
local = input("Esteve no local do crime?")
morar = input("Mora perto da vitíma?")
dever = input("Devia a vítima?")
trabalhar = input("Já trabalhou com a vítima?")

# Contagem de respostas positivas
# O lower converte a resposta do usuário para minúscula antes de comparar com a string sim. isso faz com que o programa conte todas as respostas positivas, independente de estar em maiúscula ou minúscula.
# Cada resposta positiva, o contador incrementa +1.

contagem = 0
if "sim" in telefonar.lower():
    contagem += 1
if "sim" in local.lower():
    contagem += 1
if "sim" in morar.lower():
    contagem += 1
if "sim" in dever.lower():
    contagem += 1
if "sim" in trabalhar.lower():
    contagem += 1
    
# Classificação
# O programa verifica o número de respostas positivas e imprime a mensagem indicando a classificação da pessoa em relação ao crime.

if contagem == 5:
    classificação = "Assassino"
elif contagem >= 3:
    classificação = "Cúmplice"
elif contagem >= 2:
    classificação = "Suspeita"
else:
    classificação = "Inocente"

print(f"Você foi considerado como {classificação}.")