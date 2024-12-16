import cv2
import numpy as np
import pyautogui
import logging
import random
import time
from Main import ControleMouse, AutomacaoBatalha, Agendador, Automacao


def comparar_histogramas(imagem1, imagem2):
    img1 = cv2.imread(imagem1)
    img2 = cv2.imread(imagem2)

    hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

    hist1 = cv2.normalize(hist1, hist1).flatten()
    hist2 = cv2.normalize(hist2, hist2).flatten()

    correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return correlation


def tentar_clicar(imagem, confidence=0.6):
    try:
        encontrado = mouse.clicar_imagem(imagem, confidence)
        time.sleep(3)
        return encontrado
    except pyautogui.ImageNotFoundException:
        logging.error(f"Imagem {imagem} não encontrada.")
        return False


def tentar_localizar_imagem_na_area(larger_img, smaller_img, confidence=0.6):
    larger_img_path = f"{larger_img}"
    smaller_img_path = f"{smaller_img}"

    try:
        larger_img_loc = pyautogui.locateOnScreen(
            larger_img_path, confidence=confidence
        )
        if larger_img_loc:
            region = (
                larger_img_loc.left,
                larger_img_loc.top,
                larger_img_loc.width,
                larger_img_loc.height,
            )
            smaller_img_loc = pyautogui.locateCenterOnScreen(
                smaller_img_path, region=region, confidence=confidence
            )
            if smaller_img_loc:
                pyautogui.click(smaller_img_loc)
                logging.info(
                    f"Imagem {smaller_img_path} encontrada e clicada dentro da área de {larger_img_path}."
                )
                return True
            else:
                logging.error(
                    f"Imagem {smaller_img_path} não encontrada dentro da área de {larger_img_path}."
                )
                return False
        else:
            logging.error(f"Imagem {larger_img_path} não encontrada na tela.")
            return False
    except pyautogui.ImageNotFoundException:
        logging.error(
            f"Imagem {smaller_img_path} não encontrada na área de {larger_img_path}."
        )
        return False


if __name__ == "__main__":
    mouse = ControleMouse()

    # Gemas
    mouse.clicar_imagem("gema5.png")
    time.sleep(3)
    mouse.clicar_imagem("gema5.1.png")
    time.sleep(3)

    gemp = [
        "gemaprincipal1.4.png",
        "gemaprincipal1.3.png",
        "gemaprincipal1.2.png",
        "gemaprincipal1.1.png",
        "gemaprincipal1.png",
    ]
    gemn = [
        "gema1.png",
        "gema2.png",
        "gema2,1.png",
        "gema2.1.1.png",
        "gema2.1.2.png",
        "gema2.1.3.png",
        "gema2.1.4.png",
        "gema2.1.5.png",
        "gema2.1.6.png",
        "gema2.1.7.png",
        "gema2.1.8.png",
        "gema2.1.9.png",
        "gema3.png",
        "gema3.1.png",
        "gema3.1.1.png",
        "gema3.1.2.png",
        "gema3.1.3.png",
        "gema3.1.4.png",
        "gema3.1.5.png",
        "gema3.1.6.png",
        "gema3.1.7.png",
        "gema3.1.8.png",
        "gema3.1.9.png",
        "gema4.png",
        "gema4.1.png",
        "gema4.1.png",
        "gema4.1.1.png",
        "gema4.1.2.png",
        "gema4.1.3.png",
        "gema4.1.4.png",
        "gema4.1.5.png",
    ]

    selected_image = random.choice(gemn)

    # Clicar na imagem selecionada e procurar as imagens da primeira lista
    for selected_image in gemn:
        mouse.duplo_clique(selected_image, 0.9)
        time.sleep(2)

        for image in gemp:
            # Verificar similaridade do histograma

            similaridade = comparar_histogramas(selected_image, image)
            if similaridade > 0.9:  # Ajuste o valor do limiar conforme necessário
                encontrado = tentar_localizar_imagem_na_area(selected_image, image, 0.6)
                if encontrado:
                    try:
                        mouse.clicar_imagem("gema1.1.png", 0.9)
                        time.sleep(4)
                        mouse.clicar_imagem("gema1.2.png", 0.9)
                    except pyautogui.ImageNotFoundException:
                        logging.error(f"Imagens subsequentes não encontradas.")
                else:
                    logging.error(f"{image} não encontrada na lista gemp.")
            else:
                logging.error(f"{image} não tem similaridade suficiente.")
            time.sleep(3)
