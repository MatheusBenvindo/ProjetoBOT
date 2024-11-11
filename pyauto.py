import os
os.system ('cls')

import pyautogui



pyautogui.hotkey('win', 'tab')
pyautogui.sleep(1)

def clic(img_path, confidence=0.6):
    pyautogui.sleep(1)
    
    img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)
    pyautogui.sleep(1)
    
    if img is not None:
        pyautogui.sleep(1)
        pyautogui.click(img.x, img.y)
    else:
        print(f"Imagem {img_path} não encontrada na tela.")

clic('teste.png', confidence=0.6)




