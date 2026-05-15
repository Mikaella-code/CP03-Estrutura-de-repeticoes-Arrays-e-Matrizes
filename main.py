temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]]

media = [0, 0, 0, 0]
for i in range(0,4):
    critico = [0,0,0,0]
    for j in range(0,4):
        if temperaturas[i][j] >= 33:
            critico[i] += 1
        media[i] += temperaturas[i][j]

    print(" ")
    print(f"Sala {i + 1}\nMedia:",media[i] / 4)
    print("critico:", critico[i])
    if critico[i] > critico[i-1]:
        valorCritico = i + 1

print("\nSala com maior risco: sala", valorCritico)