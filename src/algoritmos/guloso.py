def guloso_completo(a, t, e, x):
    n = len(a[0])

    tempo_linha0 = e[0] + a[0][0]
    tempo_linha1 = e[1] + a[1][0]

    if tempo_linha0 <= tempo_linha1:
        linha = 0
        tempo_total = tempo_linha0
    else:
        linha = 1
        tempo_total = tempo_linha1

    caminho = [(linha, 0)]

    for j in range(1, n):

        tempo_ficar = tempo_total + a[linha][j]
        tempo_trocar = tempo_total + t[linha][j - 1] + a[1 - linha][j]

        if tempo_ficar <= tempo_trocar:
            tempo_total = tempo_ficar
        else:
            tempo_total = tempo_trocar
            linha = 1 - linha

        caminho.append((linha, j))

    tempo_total += x[linha]

    return tempo_total, caminho
