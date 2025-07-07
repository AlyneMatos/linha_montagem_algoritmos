import random

def gerar_instancia(n):
    a = [[random.randint(1, 2 * n) for _ in range(n)] for _ in range(2)]
    t = [[random.randint(1, n) for _ in range(n-1)] for _ in range(2)]
    e = [random.randint(1, n) for _ in range(2)]
    x = [random.randint(1, n) for _ in range(2)]
    return a, t, e, x
