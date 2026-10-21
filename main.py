personagens = []

def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")
    classe = input("Digite a classe do seu personagem: ")
    nivel = int(input("Digite o nível do seu personagem: "))
    
    personagem = {
        "nome": nome,
        "classe": classe,
        "nível": nivel
    }
    
    personagens.append(personagem) #Add no final da lista
    
        
    #print("DADOS DOS PERSONAGENS CRIADO")
    #print("Nome: ", personagem["nome"])
    #print("Classe: ", personagem["classe"])
    #print("nível: ", personagem["nível"])
    
quantidade = int(input("Quentos personagens criar?: "))

for i in range(quantidade):
    print(f"★ Criando personagem {i + 1}!\n")
    criar_personagem()
    print("\n")
    
print("------LISTA FINAL DE PERSONAGENS CRIADOS------\n")
for personagem in personagens:
    print("Nome: ", personagem["nome"])
    print("Classe: ", personagem["classe"])
    print("nível: ", personagem["nível"])
    print("\n")












