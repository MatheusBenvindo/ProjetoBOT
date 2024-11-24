from datetime import datetime, timedelta
import pyautogui
import pytesseract
import time
from PIL import Image
import schedule

from botrotinadiária import CapturaTela, ControleMouse, Agendador, Automacao

if __name__ == "__main__":
    automacao = Automacao()
    mouse = ControleMouse()

    mouse.clicar_imagem('mapa.png', 0.8)
    pyautogui.sleep(1)
    mouse.clicar_imagem ('gloria.png', 0.8)
    pyautogui.sleep(5)
    mouse.clicar_imagem('gloria1.png', 0.8)
    pyautogui.sleep(2)
    
    # Lista de imagens para tentar clicar
    imagens = ['gloria0.1.png', 'gloria0.2.png', 'gloria0.3.png', 'gloria0.4.png', 'gloria0.5.png', 'gloria0.6.png', 'gloria0.7.png', 'gloria0.8.png', 'gloria0.9.png', 'gloria1.1.png', 'gloria1.1.1.png', 'gloria1.1.2.png', 'gloria1.1.3.png', 'gloria1.1.4.png', 'gloria1.1.5.png']
    
    # Clicar nas imagens da lista até encontrar uma que funcione
    for imagem in imagens:
        img = mouse.clicar_imagem(imagem, 0.8)
        if img is not None:
            print(f"Imagem {imagem} encontrada e clicada.")
            break
        else:
            print(f"Imagem {imagem} não encontrada, tentando a próxima.")

    if img is None:
        print("Nenhuma das imagens foi encontrada. Saindo do loop.")
    else:
        # Verifica se uma imagem específica aparece após clicar em 'gloria1.png'
        mouse.clicar_imagem('gloria1.png', 0.8)
        pyautogui.sleep(2)
        imagem_verificar = 'imagem_especifica.png'  # Substitua pelo nome da imagem específica a ser verificada
        img_verificar = pyautogui.locateOnScreen(imagem_verificar, confidence=0.8)
        
        if img_verificar is not None:
            print(f"Imagem {imagem_verificar} encontrada. Realizando ação.")
            pyautogui.click(img_verificar)
            pyautogui.sleep(1)
        else:
            print(f"Imagem {imagem_verificar} não encontrada. Continuando o loop.")
        
        # Continuar com as ações restantes
        pyautogui.sleep(1)
        mouse.localizar_imagem_na_area('gloria1.4.png', 'gloria1.2.png')
        pyautogui.sleep(3.5)

        for _ in range(4):
            pyautogui.hotkey('2')
            pyautogui.sleep(2)  

        for _ in range(4):
            pyautogui.hotkey('space')
            pyautogui.sleep(2)

        for _ in range(7):
            pyautogui.hotkey('2')
            pyautogui.sleep(2)

        for _ in range(7):
            pyautogui.hotkey('1')
            pyautogui.sleep(2)

        for _ in range(7):
            pyautogui.hotkey('5')




