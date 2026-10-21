'''
def cadastrar_usuario(nome, idade, cidade="Não informado"):
    print(f"Cadastro: {nome}, {idade}, {cidade}")
    
cadastrar_usuario(idade = 18, nome = "Alexandre Takeo", cidade = "Kyoto")
'''
numero = 20 #Variável global
def calcular():
    numero = 10 # Variável local
    return numero
print(calcular())
print(numero)

saldo = 5000
def deposito():
    global saldo # Utilizar para acessar a função global senão não acessa
    saldo = saldo + 100
    return saldo
print(deposito())