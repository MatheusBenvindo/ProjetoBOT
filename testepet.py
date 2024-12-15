from Main import Automacao, ControleMouse
import pyautogui
import threading
import time

def verificar_batalha_continuamente(automacao):
    """Função que verifica a batalha continuamente a cada 2 segundos"""
    while True:
        automacao.iniciar_verificacao_batalha(2)
        time.sleep(2)

if __name__ == "__main__":
    automacao = Automacao()
    mouse = ControleMouse()

    for _ in range(10):
        if mouse.clique_imagem_repetida_aleatoria('pet3.2.png', 0.7):
            print('Imagem repetida escolhida aleatoriamente')
            time.sleep(15)
            mouse.clicar_imagem('finalizarbatalhapet.png')
            time.sleep(9)
    if mouse.clicar_imagem("fechartela.png"):
        print ("localizado e clicado.")
    
    pyautogui.sleep(6)