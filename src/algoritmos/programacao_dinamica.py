def linha_montagem_dp(a, t, e, x):
    n = len(a[0])
    T1 = [0] * n
    T2 = [0] * n
    L1 = [0] * n
    L2 = [0] * n

    T1[0] = e[0] + a[0][0]
    T2[0] = e[1] + a[1][0]

    for i in range(1, n):
        if T1[i-1] + a[0][i] <= T2[i-1] + t[1][i-1] + a[0][i]:
            T1[i] = T1[i-1] + a[0][i]
            L1[i] = 0
        else:
            T1[i] = T2[i-1] + t[1][i-1] + a[0][i]
            L1[i] = 1

        if T2[i-1] + a[1][i] <= T1[i-1] + t[0][i-1] + a[1][i]:
            T2[i] = T2[i-1] + a[1][i]
            L2[i] = 1
        else:
            T2[i] = T1[i-1] + t[0][i-1] + a[1][i]
            L2[i] = 0

    if T1[n-1] + x[0] <= T2[n-1] + x[1]:
        tempo_total = T1[n-1] + x[0]
        linha = 0
    else:
        tempo_total = T2[n-1] + x[1]
        linha = 1

    caminho = [0] * n
    caminho[n-1] = linha
    for i in range(n-2, -1, -1):
        linha = L1[i+1] if linha == 0 else L2[i+1]
        caminho[i] = linha

    caminho = [(linha, j) for j, linha in enumerate(caminho)]
    return tempo_total, caminho