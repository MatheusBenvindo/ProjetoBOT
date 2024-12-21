import cv2
import numpy as np
import pyautogui
import logging
import pytesseract
from PIL import Image

# Configuração de logging corrigida
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class CapturaTela:
    def capturar_tela_inteira(self):
        return pyautogui.screenshot()

    def verificar_texto_na_imagem(self, imagem_path):
        # Carregar a imagem especificada
        imagem = Image.open(imagem_path)
        return pytesseract.image_to_string(imagem)

    def encontrar_texto_na_imagem(self, imagem_path, texto_busca):
        # Carregar a imagem especificada
        imagem = Image.open(imagem_path)
        texto_extraido = pytesseract.image_to_string(imagem)
        logging.info(f"Texto extraído da imagem: {texto_extraido}")
        return texto_busca.lower() in texto_extraido.lower()

    def clicar_no_texto(self, imagem_path, texto_busca):
        # Carregar a imagem especificada
        imagem = Image.open(imagem_path)
        screenshot = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)

        # Converter a imagem para escala de cinza
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Usar pytesseract para obter os dados dos boxes de texto
        d = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

        # Procurar pelo texto dentro dos dados retornados
        n_boxes = len(d["level"])
        for i in range(n_boxes):
            if texto_busca.lower() in d["text"][i].lower():
                (x, y, w, h) = (
                    d["left"][i],
                    d["top"][i],
                    d["width"][i],
                    d["height"][i],
                )
                pyautogui.click(x + w / 2, y + h / 2)
                logging.info(
                    f"Texto '{texto_busca}' encontrado e clicado na posição ({x}, {y})."
                )
                return True

        logging.warning(f"Texto '{texto_busca}' não encontrado na imagem.")
        return False


# Funções Auxiliares
def encontrar_e_clicar_imagem(imagem, template, confidence):
    """Encontra e clica na imagem localizada se a confiança for suficiente."""
    result = cv2.matchTemplate(imagem, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= confidence:
        h, w, _ = template.shape
        pyautogui.click(max_loc[0] + w / 2, max_loc[1] + h / 2)
        logging.info("Imagem encontrada e clicada.")
        return (
            int(max_loc[0]),
            int(max_loc[1]),
            int(w),
            int(h),
        )  # Retorna as coordenadas da imagem encontrada, convertidas para int
    else:
        logging.warning("Imagem não encontrada com a confiança necessária.")
        return None


def localizar_imagem_dentro_da_imagem(imagem_base, imagem_procurada, confidence):
    """Localiza a imagem procurada dentro da imagem base."""
    screenshot = pyautogui.screenshot(region=imagem_base)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(imagem_procurada, cv2.IMREAD_COLOR)
    return encontrar_e_clicar_imagem(screenshot, template, confidence)


# Função Principal
def localizar_imagens_encadeadas(
    imagem1, imagem2, capturador, texto_busca, confidence=0.6
):
    imagem1_area = pyautogui.locateOnScreen(imagem1, confidence=confidence)
    if imagem1_area is not None:
        logging.info(f"Imagem 1 ({imagem1}) encontrada.")
        region1 = (
            int(imagem1_area.left),
            int(imagem1_area.top),
            int(imagem1_area.width),
            int(imagem1_area.height),
        )
        screenshot1 = pyautogui.screenshot(region=region1)
        screenshot1 = cv2.cvtColor(np.array(screenshot1), cv2.COLOR_RGB2BGR)

        # Procurar e clicar na Imagem 2 dentro da Imagem 1
        imagem2_area = encontrar_e_clicar_imagem(
            screenshot1, cv2.imread(imagem2, cv2.IMREAD_COLOR), confidence
        )
        if imagem2_area is not None:
            logging.info(f"Imagem 2 ({imagem2}) encontrada dentro de {imagem1}.")
            region2 = (
                int(imagem2_area[0]),
                int(imagem2_area[1]),
                int(imagem2_area[2]),
                int(imagem2_area[3]),
            )
            screenshot2 = pyautogui.screenshot(region=region2)
            screenshot2 = cv2.cvtColor(np.array(screenshot2), cv2.COLOR_RGB2BGR)

            # Procurar e clicar no texto dentro da Imagem 2 usando CapturaTela
            if capturador.clicar_no_texto(imagem2, texto_busca):
                logging.info(
                    f"Texto '{texto_busca}' encontrado e clicado dentro de {imagem2}."
                )
            else:
                logging.warning(
                    f"Texto '{texto_busca}' não encontrado dentro de {imagem2}."
                )
        else:
            logging.warning(f"Imagem 2 ({imagem2}) não encontrada dentro de {imagem1}.")
    else:
        logging.warning(f"Imagem 1 ({imagem1}) não encontrada na tela.")


if __name__ == "__main__":
    imagem1 = "comprageral.bmp"
    imagem2 = "guilda2.4.bmp"
    texto_busca = "Satin Al"

    # Instanciando a classe CapturaTela
    capturador = CapturaTela()

    # Chamando a função localizar_imagens_encadeadas com CapturaTela
    localizar_imagens_encadeadas(
        imagem1, imagem2, capturador, texto_busca, confidence=0.8
    )
