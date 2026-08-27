import re

codigo = input("Digite um código: ")

while not re.fullmatch(r"[a-z0-9]{5}", codigo):
    codigo = input("Digite um código: ")

print("Código aceito!")
