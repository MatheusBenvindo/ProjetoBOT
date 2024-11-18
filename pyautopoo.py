import os
import pyautogui

class AutomacaoPyAutoGui:
    def __init__(self):
        os.system('cls')

    def ativar_visualizacao_janelas(self):
        pyautogui.hotkey('win', 'tab')
        pyautogui.sleep(1)
    
    def clicar_imagem(self, img_path, confidence=0.6):
        pyautogui.sleep(1)
        
        img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)
        pyautogui.sleep(1)
        
        if img is not None:
            pyautogui.sleep(1)
            pyautogui.click(img.x, img.y)
        else:
            print(f"Imagem {img_path} não encontrada na tela.")
            
automacao = AutomacaoPyAutoGui()

automacao.ativar_visualizacao_janelas()

automacao.clicar_imagem('teste.png', confidence=0.6)
