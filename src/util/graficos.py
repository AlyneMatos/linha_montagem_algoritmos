import matplotlib.pyplot as plt
import csv

def graficos():
    ns, tempos_dp, tempos_guloso, melhorias = [], [], [], []

    with open("data/resultados.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ns.append(int(row["n"]))
            tempos_dp.append(float(row["tempo_dp"]))
            tempos_guloso.append(float(row["tempo_guloso"]))
            melhorias.append(float(row["melhoria"]))

    plt.figure()
    plt.plot(ns, tempos_dp, label='Programação Dinâmica')
    plt.plot(ns, tempos_guloso, label='Guloso')
    plt.xlabel('Tamanho da entrada (n)')
    plt.ylabel('Tempo médio de execução (s)')
    plt.title('Tempo de Execução')
    plt.legend()
    plt.grid(True)
    plt.savefig("data/graficos/tempo_execucao.png")

    plt.figure()
    plt.plot(ns, melhorias)
    plt.xlabel('Tamanho da entrada (n)')
    plt.ylabel('Melhoria média')
    plt.title('Melhoria do algoritmo ótimo sobre o guloso')
    plt.grid(True)
    plt.savefig("data/graficos/qualidade_solucao.png")