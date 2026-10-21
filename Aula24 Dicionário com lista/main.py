personagem = {
    "nome": "Sal Fisher",
    "classe": "Especialista",
    "nivel": 1,
    "inventario": [] # Lista dentro do dicionario
}
item1 = input("Digite um item: ")
item2 = input("Digite outro item: ")
personagem["inventario"].append(item1)
personagem["inventario"].append(item2)

print("\nNome: ", personagem ["nome"])
print("Classe: ", personagem ["classe"])
print("Nivel: ", personagem ["nivel"])
print("-----Inventario-----")
for item in personagem["inventario"]:
    print("-", item)
