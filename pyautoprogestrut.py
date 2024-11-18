import os
import pyautogui
import time

os.system('cls')

def clicar_imagem(img_path, confidence=0.6):
    pyautogui.sleep(1)
    
    img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)
    pyautogui.sleep(1)
    
    if img is not None:
        pyautogui.sleep(1)
        pyautogui.click(img.x, img.y)
    else:
        print(f"Imagem {img_path} não encontrada na tela.")

def ativar_visualizacao_janelas():
    pyautogui.hotkey('win', 'tab')
    pyautogui.sleep(1)

# Horário de 12:00 - Arena Guardião 
# Abre o visualizador de tarefas e entra onde o jogo está rodando
ativar_visualizacao_janelas()
clicar_imagem ('teste.png', confidence=0.6)

#localiza e clica no icone da batalha
clicar_imagem ('teste1.png', confidence=0.6)

#fecha ao terminar use biblioteca time

