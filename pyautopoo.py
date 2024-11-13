import os
import pyautogui

# Classe para automação de tarefas com pyautogui
class AutomacaoPyAutoGui:
    def __init__(self):
        # Limpar a tela do terminal (em sistemas Windows)
        os.system('cls')

    def ativar_visualizacao_janelas(self):
        # Ativa a visualização de janelas no Windows (Win + Tab)
        pyautogui.hotkey('win', 'tab')
        pyautogui.sleep(1)
    
    def clicar_imagem(self, img_path, confidence=0.6):
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
            
# Criando uma instância da classe AutomacaoPyAutoGui
automacao = AutomacaoPyAutoGui()

# Ativar a visualização de janelas
automacao.ativar_visualizacao_janelas()

# Clicar na imagem 'teste.png'
automacao.clicar_imagem('teste.png', confidence=0.6)
