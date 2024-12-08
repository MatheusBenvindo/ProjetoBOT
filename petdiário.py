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

    # Iniciar verificação de batalha em thread separado
    batalha_thread = threading.Thread(target=verificar_batalha_continuamente, args=(automacao,))
    batalha_thread.start()

    if mouse.clicar_imagem('mapa.png', 0.8):
        print("Imagem 'mapa.png' encontrada e clicada.")
    pyautogui.sleep(1)
    
    if mouse.clicar_varias_vezes('mapa1.1.png', 29, delay=0.1, confidence=0.6):
        print("Imagem 'mapa1.1.png' encontrada e clicada várias vezes.")
    
    if mouse.clicar_imagem('pet1.png', 0.8):
        print("Imagem 'pet1.png' encontrada e clicada.")
    pyautogui.sleep(9)
    
    if mouse.clicar_imagem('pet1.1.png', 0.8):
        print("Imagem 'pet1.1.png' encontrada e clicada.")
    pyautogui.sleep(5)
    
    if mouse.clicar_imagem('pet1.2.png', 0.6):
        print("Imagem 'pet1.2.png' encontrada e clicada.")
    pyautogui.sleep(5)
    
    if mouse.clicar_imagem('pet1.3.png', 0.6):
        print("Imagem 'pet1.3.png' encontrada e clicada.")
    pyautogui.sleep(5)
    
    if mouse.clicar_varias_vezes('pet1.3.png', 25, delay=5, confidence=0.8):
        print("Imagem 'pet1.3.png' encontrada e clicada várias vezes.")
    
