import os
import pyautogui

# Limpar a tela do terminal (em sistemas Windows)
os.system('cls')

# Função para clicar em uma imagem na tela
def clicar_imagem(img_path, confidence=0.6):
    pyautogui.sleep(1)
    
    # Localiza o centro da imagem na tela
    img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)
    pyautogui.sleep(1)
    
    # Se a imagem foi encontrada, clica nela
    if img is not None:
        pyautogui.sleep(1)
        pyautogui.click(img.x, img.y)
    else:
        print(f"Imagem {img_path} não encontrada na tela.")

# Função para acionar a visualização de múltiplas janelas no Windows (Win + Tab)
def ativar_visualizacao_janelas():
    pyautogui.hotkey('win', 'tab')
    pyautogui.sleep(1)

# Ativar a visualização de janelas
ativar_visualizacao_janelas()
clicar_imagem ('teste.png', confidence=0.6)