arquivo = open("loremipsum.txt", "r")

conteudo = arquivo.read()
print("Conteúdo completo:\n", conteudo)

arquivo.seek(0)
print("\nPrimeira linha:", arquivo.readline())

arquivo.seek(0)
print("\n3 primeiros caracteres:", arquivo.read(3))

arquivo.close()

with open("loremipsum.txt", "r") as f:
    print("\nUsando with:\n", f.read())
