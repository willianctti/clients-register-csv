nome = input("Digite seu nome: ")

with open("base_dados.csv", "a") as arquivo:
    arquivo.write(f"{nome}\n")

print("Dados salvos com sucesso!") 