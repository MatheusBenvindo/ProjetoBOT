import threading
import time
from Main import Automacao, ControleMouse


# Função para verificar batalha continuamente
def verificar_batalha_continuamente(automacao, intervalo):
    while True:
        automacao.iniciar_verificacao_batalha("verificacaobatalha.png", intervalo)
        time.sleep(intervalo)


if __name__ == "__main__":
    automacao = Automacao()
    mouse = ControleMouse()

    # Iniciar verificação de batalha em thread separada
    batalha_thread = threading.Thread(
        target=verificar_batalha_continuamente, args=(automacao, 2)
    )
    batalha_thread.daemon = (
        True  # Permite que a thread seja finalizada ao encerrar o programa
    )
    batalha_thread.start()

    # Primeira parte do fluxo
    if mouse.clicar_imagem("mapa.png", 0.8):
        print("Imagem 'mapa.png' encontrada e clicada.")
    time.sleep(1)

    if mouse.clicar_varias_vezes("mapa1.1.png", 29, delay=0.1, confidence=0.6):
        print("Imagem 'mapa1.1.png' encontrada e clicada várias vezes.")

    if mouse.clicar_imagem("pet1.png", 0.8):
        print("Imagem 'pet1.png' encontrada e clicada.")
    time.sleep(25)

    if mouse.clicar_imagem("pet1.1.png", 0.8):
        print("Imagem 'pet1.1.png' encontrada e clicada.")
    time.sleep(7)

    if mouse.clicar_imagem("pet1.2.png", 0.6):
        print("Imagem 'pet1.2.png' encontrada e clicada.")
    time.sleep(7)

    if mouse.clicar_imagem("pet1.3.png", 0.6):
        print("Imagem 'pet1.3.png' encontrada e clicada.")
    time.sleep(7)

    if mouse.clicar_varias_vezes("pet1.3.png", 35, delay=8, confidence=0.8):
        print("Imagem 'pet1.3.png' encontrada e clicada várias vezes.")

    # Segunda parte do fluxo
    if mouse.clicar_imagem("sair.png", 0.8):
        print("Imagem 'sair.png' encontrada e clicada.")
    time.sleep(10)

    if mouse.clicar_imagem("mapa.png", 0.7):
        print("Imagem 'mapa.png' clicada.")
    time.sleep(4)

    if mouse.clicar_varias_vezes("mapa1.1.png", 15, delay=0.1, confidence=0.6):
        print("Imagem 'mapa1.1.png' encontrada e clicada várias vezes.")
    time.sleep(5)

    if mouse.clicar_imagem("pet3.png", 0.7):
        print("Imagem 'pet3.png' clicada.")
    time.sleep(7)

    if mouse.clicar_imagem("pet3.1.png", 0.7):
        print("Imagem 'pet3.1.png' clicada.")
    time.sleep(6)

    for _ in range(10):
        if mouse.clicar_posicao_aleatoria("pet3.2.png", 0.7):
            print("Imagem repetida escolhida aleatoriamente.")
            time.sleep(15)
            mouse.clicar_imagem("finalizarbatalhapet.png")
            time.sleep(9)

    if mouse.clicar_imagem("fechartela.png"):
        print("Imagem 'fechartela.png' localizada e clicada.")

    # Terceira parte do fluxo
    if mouse.clicar_imagem("mapa.png", 0.7):
        print("Imagem 'mapa.png' clicada.")
    time.sleep(4)

    if mouse.clicar_imagem("pet2.png", 0.7):
        print("Imagem 'pet2.png' clicada.")
    time.sleep(25)

    passos = [
        "pet2.1.png",
        "pet2.1.1.png",
        "pet2.1.2.png",
        "pet2.1.3.png",
        "pet2.1.4.png",
        "pet2.1.5.png",
        "pet2.1.7.png",
        "pet2.1.8.png",
    ]

    for passo in passos:
        if mouse.clicar_imagem(passo, 0.7):
            print(f"Imagem '{passo}' clicada.")
        time.sleep(10)

    if mouse.clicar_imagem("fechartela.png"):
        print("Imagem 'fechartela.png' localizada e clicada.")
