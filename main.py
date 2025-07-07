from src.avaliador.avaliador import comparar_algoritmos
from src.util.graficos import graficos

if __name__ == "__main__":
    comparar_algoritmos(k_min=100, k_max=200, n_min=10, n_max=10000)
    graficos()
