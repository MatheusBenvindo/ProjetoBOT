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
    mouse.clicar_varias_vezes('mapa1.1.png', 29, delay=0.1, confidence=0.6)
    mouse.clicar_imagem('pet1.png',0.8)
    pyautogui.sleep(15)
    mouse.clicar_imagem('pet1.1.png', 0.8)
    pyautogui.sleep(5)
    mouse.clicar_imagem('pet1.2.png', 0.6)
    pyautogui.sleep(5)
    mouse.clicar_imagem('pet1.3.png', 0.6)
    pyautogui.sleep(5)
    mouse.clicar_varias_vezes('pet1.3.png', 25, delay=2, confidence=0.8)