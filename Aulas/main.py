comando = "Equipar foice"
partes = comando.split()

print(partes[0])
print(partes[-1]) #Para achar o ultimo numero pode se usar -1 o penultimo -2 e....

acao = partes[0]
item = partes[1]

if acao == "Equipar":
    print(f"Equipando {item}")
elif acao == "Desequipar":
    print(f"Desequipar {item}")
else:
    print("Comando desconhecido!")
