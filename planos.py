import random
from collections import deque

# Definindo o tamanho do mapa
N = 10  # Exemplo de tamanho 10x10

# Função para criar um mapa com objeto em posição fixa
def criar_mapa(padrao):
    mapa = [[0 for _ in range(N)] for _ in range(N)]
    if padrao == 1:
        mapa[2][3] = 2  # Objeto na posição (2, 3)
    elif padrao == 2:
        mapa[5][7] = 2  # Objeto na posição (5, 7)
    elif padrao == 3:
        mapa[8][1] = 2  # Objeto na posição (8, 1)
    elif padrao == 4:
        mapa[4][4] = 2  # Objeto na posição (4, 4)
    elif padrao == 5:
        mapa[7][9] = 2  # Objeto na posição (7, 9)
    return mapa

# Função para revelar uma célula e suas adjacências
def revelar(mapa, x, y):
    if 0 <= x < N and 0 <= y < N and mapa[x][y] == 0:
        mapa[x][y] = 1
        return True
    return False

# Função de busca adaptada para cliques
def buscar_objeto(mapa, start_x, start_y):
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita
    fila = deque([(start_x, start_y)])
    revelar(mapa, start_x, start_y)

    while fila:
        x, y = fila.popleft()
        if mapa[x][y] == 2:
            return (x, y)  # Objeto encontrado

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if revelar(mapa, nx, ny):
                fila.append((nx, ny))
    
    return None  # Objeto não encontrado

# Escolher um padrão de mapa aleatório
padrao_mapa = random.randint(1, 5)
mapa = criar_mapa(padrao_mapa)

# Posição inicial aleatória
inicio_x, inicio_y = random.randint(0, N-1), random.randint(0, N-1)

# Buscando o objeto
resultado = buscar_objeto(mapa, inicio_x, inicio_y)

if resultado:
    print(f"Objeto encontrado na posição: {resultado}")
else:
    print("Objeto não encontrado no mapa.")

# Função para imprimir o mapa (opcional, para visualização)
def imprimir_mapa(mapa):
    for linha in mapa:
        print(" ".join(str(celula) for celula in linha))

# Exibir o mapa final (para ver as áreas reveladas)
imprimir_mapa(mapa)
