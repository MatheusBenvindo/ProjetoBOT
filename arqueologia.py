import cv2
import numpy as np
import pyautogui
import logging
import time
from Main import ControleMouse, AutomacaoBatalha, Agendador, Automacao

# Configuração de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    mouse = ControleMouse()

    mouse.clicar_imagem("arredores.png", confidence=0.7)
    time.sleep(15)
    mouse.clicar_imagem("arqueologia1.png", confidence=0.7)
    time.sleep(1)
    mouse.clicar_imagem("arqueologia3.png", confidence=0.7)
    time.sleep(3)

    for _ in range(35):
        mouse.clicar_imagem("arqueologia4.png", confidence=0.7)
        time.sleep(30)
    mouse.clicar_imagem("arredores.png")

    # LAB1
    mouse.clicar_imagem("lab.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.4.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.1.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.2")
    time.sleep(3)
    mouse.clicar_imagem("fechartela.png")
    # LAB2
    mouse.clicar_imagem("lab.png")
    time.sleep(3)
    mouse.clicar_imagem("lab2.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.4.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.1.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.2")
    time.sleep(3)
    mouse.clicar_imagem("fechartela.png")
    # LAB3
    mouse.clicar_imagem("lab.png")
    time.sleep(3)
    mouse.clicar_imagem("lab3.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.4.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.1.png")
    time.sleep(3)
    mouse.clicar_imagem("lab1.2")
    time.sleep(3)
    mouse.clicar_imagem("fechartela.png")

    imgg = [
        "guilda1.4.png",
        "guilda1.4.1.png",
        "guilda1.5.png",
        "guilda2.3.png",
        "guilda2.4.png",
        "guilda2.5.png",
    ]

    imgg1 = [
        "guilda1.7,png",
        "guilda1.8.png",
        "guilda1.9.png",
        "guilda2.png",
    ]

    for imagem in imgg:
        mouse.localizar_imagem_na_area(imagem, "guildacompra.png")
        pyautogui.hotkey("0")
        time.sleep(2)
        pyautogui.hotkey("0")
        time.sleep(2)
        pyautogui.hotkey("0")
        pyautogui.hotkey("0")
        time.sleep(3)
        mouse.clicar_imagem("guildaconfirmacompra.png")
        time.sleep(6)

    mouse.clicar_imagem("guilda2.6.png")

    for imagem in imgg1:
        mouse.localizar_imagem_na_area(imagem, "guildacompra.png")
        pyautogui.hotkey("0")
        time.sleep(2)
        pyautogui.hotkey("0")
        time.sleep(2)
        pyautogui.hotkey("0")
        pyautogui.hotkey("0")
        time.sleep(3)
        mouse.clicar_imagem("guildaconfirmacompra.png")
        time.sleep(6)
pyautogui.hotkey("esc")
time.sleep(1)
mouse.clicar_imagem("fechartela.png")

mouse.clicar_imagem("mapa.png")
time.sleep(3)
mouse.clicar_imagem("deusa.png")
time.sleep(25)
mouse.clicar_imagem("deusa1.1.png")
time.sleep(3)
mouse.clicar_imagem("deusa1.2.png")
time.sleep(5)
mouse.clicar_imagem("deusa1.3.png")
time.sleep(5)
mouse.clicar_imagem("deusa1.7.png")
time.sleep(2)
pyautogui.hotkey("0")
time.sleep(2)
pyautogui.hotkey("0")
time.sleep(2)
pyautogui.hotkey("0")
time.sleep(2)
pyautogui.hotkey("0")
time.sleep(2)
mouse.clicar_imagem("deusa1.4.png")
time.sleep(2)
mouse.clicar_imagem("deusa1.5.png")
time.sleep(30)
mouse.clicar_imagem("deusa1.6.png")

for _ in range(3):
    mouse.clicar_imagem("fechartela.png")
