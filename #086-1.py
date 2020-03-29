# Versão "Light" do exercício #086
matriz = [[], [], []]
for linha in range(3):
    for coluna in range(3):
        while True:
            try:
                matriz[linha].append(int(input(f"Insira a célula ({linha + 1}, {coluna + 1}): ")))
                break
            except ValueError:
                print("Tente novamente.")
for linha in matriz:
    for cel in linha:
        print(f"[{cel:^5}]", end='')
    print()
