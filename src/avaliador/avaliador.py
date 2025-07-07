import random
import numpy as np
import csv
import json
import time

from src.algoritmos.guloso import guloso_completo
from src.algoritmos.programacao_dinamica import linha_montagem_dp
from src.gerador.gerador import gerar_instancia


def comparar_algoritmos(k_min=100, k_max=200, n_min=10, n_max=10000):
    k = random.randint(k_min, k_max)
    n_vals = np.linspace(n_min, n_max, k, dtype=int)
    m = random.randint(10, 20)

    with open("data/resultados.csv", "w", newline="") as csvfile_resultados, \
            open("data/solucoes_detalhadas.csv", "w", newline="") as csvfile_solucoes:

        writer_resultados = csv.writer(csvfile_resultados)
        writer_solucoes = csv.writer(csvfile_solucoes)

        writer_resultados.writerow(["n", "tempo_dp", "tempo_guloso", "melhoria", "solucao_dp", "solucao_guloso"])
        writer_solucoes.writerow(["n", "instancia", "solucao_dp", "caminho_dp", "solucao_guloso", "caminho_guloso"])

        for n in n_vals:
            tempo_dp_total = 0
            tempo_g_total = 0
            melhoria_total = 0
            soma_opt_val = 0
            soma_g_val = 0

            for instancia in range(m):
                a, t, e, x = gerar_instancia(n)

                # Algoritmo de Programação Dinamica
                ini = time.perf_counter()
                opt_val, caminho_dp = linha_montagem_dp(a, t, e, x)
                fim = time.perf_counter()
                tempo_dp_total += fim - ini

                # Algoritmo Guloso
                ini = time.perf_counter()
                g_val, caminho_guloso = guloso_completo(a, t, e, x)
                fim = time.perf_counter()
                tempo_g_total += fim - ini

                melhoria = (g_val - opt_val) / opt_val if opt_val != 0 else 0
                melhoria_total += melhoria
                soma_opt_val += opt_val
                soma_g_val += g_val

                writer_solucoes.writerow([
                    n,
                    instancia + 1,
                    opt_val,
                    json.dumps(caminho_dp),
                    g_val,
                    json.dumps(caminho_guloso)
                ])

            writer_resultados.writerow([
                n,
                tempo_dp_total / m,
                tempo_g_total / m,
                melhoria_total / m,
                soma_opt_val / m,
                soma_g_val / m
            ])
