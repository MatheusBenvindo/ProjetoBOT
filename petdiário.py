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
    pyautogui.sleep(25)
    
    if mouse.clicar_imagem('pet1.1.png', 0.8):
        print("Imagem 'pet1.1.png' encontrada e clicada.")
    pyautogui.sleep(7)
    
    if mouse.clicar_imagem('pet1.2.png', 0.6):
        print("Imagem 'pet1.2.png' encontrada e clicada.")
    pyautogui.sleep(7)
    
    if mouse.clicar_imagem('pet1.3.png', 0.6):
        print("Imagem 'pet1.3.png' encontrada e clicada.")
    pyautogui.sleep(7)
    
    if mouse.clicar_varias_vezes('pet1.3.png', 35, delay=8, confidence=0.8):
        print("Imagem 'pet1.3.png' encontrada e clicada várias vezes.")
    
    if mouse.clicar_imagem('sair.png', 0.8):
        print("Imagem 'sair.png' encontrada clicada.")
    pyautogui.sleep(10)
    if mouse.clicar_imagem("mapa.png", 0.7):
        print('imagem mapa clicada')
    pyautogui.sleep(4)
    if mouse.clicar_varias_vezes('mapa1.1.png', 15, delay=0.1, confidence=0.6):
        print("Imagem 'mapa1.1.png' encontrada e clicada várias vezes.")
    pyautogui.sleep(5)
    if mouse.clicar_imagem("pet3.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(7)
    if mouse.clicar_imagem("pet3.1.png", 0.7):
        print('imagem entrar clicada')
    pyautogui.sleep(6)

    for _ in range(10):
        if mouse.clique_imagem_repetida_aleatoria('pet3.2.png', 0.7):
            print('Imagem repetida escolhida aleatoriamente')
            time.sleep(15)
            mouse.clicar_imagem('finalizarbatalhapet.png')
            time.sleep(9)
    if mouse.clicar_imagem("fechartela.png"):
        print ("localizado e clicado.")

    if mouse.clicar_imagem("mapa.png", 0.7):
        print('imagem mapa clicada')
    pyautogui.sleep(4)
    if mouse.clicar_imagem("pet2.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(25)
    if mouse.clicar_imagem("pet2.1.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(10)
    if mouse.clicar_imagem("pet2.1.1.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(10)
    if mouse.clicar_imagem("pet2.1.2.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(10)
    if mouse.clicar_imagem("pet2.1.3.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(10)
    if mouse.clicar_imagem("pet2.1.4.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(10)
    if mouse.clicar_imagem("pet2.1.5.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(10)
    if mouse.clicar_imagem("pet2.1.7.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(10)
    if mouse.clicar_imagem("pet2.1.8.png", 0.7):
        print('imagem local clicada')
    pyautogui.sleep(15)
    if mouse.clicar_imagem('fechartela.png'):
        print('imagem localizada e clicada')