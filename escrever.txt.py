texto = list()
texto.append("Primeira linha")
texto.append("Segunda linha")
texto.append("Terceira linha")

with open("texto.txt", "w") as f:
    for linha in texto:
        f.write(linha + "\n")

print("Arquivo texto.txt criado com sucesso!")