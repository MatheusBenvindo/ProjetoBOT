from datetime import datetime, timedelta
import pyautogui
import pytesseract
import time
from PIL import Image
import schedule

def captura_tela(area=None):
    if area and all(isinstance(coord, int) for coord in area):
        screenshot = pyautogui.screenshot(region=area)
    else:
        screenshot = pyautogui.screenshot()
    return screenshot

def localizar_imagem(imagem, confidence=0.8):
    try:
        return pyautogui.locateOnScreen(imagem, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        return None

def clicar_imagem(imagem, confidence=0.8):
    localizacao = localizar_imagem(imagem, confidence)
    if localizacao:
        pyautogui.click(localizacao)
        print(f"Imagem {imagem} encontrada e clicada.")
        return localizacao
    else:
        print(f"Imagem {imagem} não encontrada.")
        return None

def localizar_imagem_na_area(larger_img_path, smaller_img_path, confidence=0.6):
    """Localiza uma imagem menor dentro de uma imagem maior e clica nela"""
    try:
        larger_img = pyautogui.locateOnScreen(larger_img_path, confidence=confidence)
        if larger_img is not None:
            # Define a região delimitada pela imagem maior
            region = (larger_img.left, larger_img.top, larger_img.width, larger_img.height)
            # Procura a imagem menor dentro da região delimitada
            smaller_img = pyautogui.locateCenterOnScreen(smaller_img_path, region=region, confidence=confidence)
            if smaller_img is not None:
                pyautogui.click(smaller_img)
                print(f"Imagem {smaller_img_path} encontrada e clicada dentro de {larger_img_path}.")
            else:
                print(f"Imagem {smaller_img_path} não encontrada dentro de {larger_img_path}.")
        else:
            print(f"Imagem maior {larger_img_path} não encontrada na tela.")
    except pyautogui.ImageNotFoundException:
        print(f"Imagem {larger_img_path} ou {smaller_img_path} não pôde ser localizada.")

def mover_cursor_neutro():
    # Mover o cursor para o canto superior direito da tela
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width - 10, 10)
    pyautogui.sleep(1)

def verificar_e_realizar_acao(imagem_verificar, confidence=0.8):
    img_verificar = localizar_imagem(imagem_verificar, confidence=confidence)
    if img_verificar is not None:
        print(f"Imagem {imagem_verificar} encontrada. Realizando ação.")
        pyautogui.click(img_verificar)
        pyautogui.sleep(5)
        mover_cursor_neutro()
        print(f"Ação na imagem {imagem_verificar} confirmada.")
        realizar_acao_restante()
        return True
    else:
        print(f"Imagem {imagem_verificar} não encontrada.")
        return False

def realizar_acao_restante():
    pyautogui.sleep(1)
    clicar_imagem("garantia1.png", 0.8)
    localizar_imagem_na_area('gloria1.4.png', 'gloria1.2.png')
    pyautogui.sleep(3.5)
    mover_cursor_neutro()

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
        pyautogui.sleep(2)

def verificar_imagem_adicional():
    time.sleep(30)
    if clicar_imagem('gloria0.2.1.png', 0.6):
        pyautogui.sleep(8)
        localizar_imagem_na_area('fechatelaouro.png', 'fechatelagloria.png')
    elif clicar_imagem('gloria0.3.1.png', 0.6):
        pyautogui.sleep(8)
        localizar_imagem_na_area('fechatelaouro.png', 'fechatelagloria.png')

def clicar_imagem_gloria0_1():
    if clicar_imagem('gloria0.1.png'):
        verificar_e_realizar_acao('gloriasegdia.png')
        verificar_imagem_adicional()

def clicar_imagem_gloria0_2():
    if clicar_imagem('gloria0.2.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria0_3():
    if clicar_imagem('gloria0.3.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria0_4():
    if clicar_imagem('gloria0.4.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria0_5():
    if clicar_imagem('gloria0.5.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria0_6():
    if clicar_imagem('gloria0.6.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria0_7():
    if clicar_imagem('gloria0.7.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria0_8():
    if clicar_imagem('gloria0.8.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria0_9():
    if clicar_imagem('gloria0.9.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria1_1():
    if clicar_imagem('gloria1.1.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria1_1_1():
    if clicar_imagem('gloria1.1.1.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria1_1_2():
    if clicar_imagem('gloria1.1.2.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria1_1_3():
    if clicar_imagem('gloria1.1.3.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria1_1_4():
    if clicar_imagem('gloria1.1.4.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

def clicar_imagem_gloria1_1_5():
    if clicar_imagem('gloria1.1.5.png'):
        realizar_acao_restante()
        verificar_imagem_adicional()

if __name__ == "__main__":
    # Ações iniciais antes de tentar clicar nas imagens
    clicar_imagem('mapa.png', 0.8)
    pyautogui.sleep(1)
    clicar_imagem('gloria.png', 0.8)
    pyautogui.sleep(10)
    clicar_imagem('gloria1.png', 0.8)
    pyautogui.sleep(2)
    mover_cursor_neutro()

    # Tentar clicar em cada imagem separadamente com mensagens de confirmação
    if clicar_imagem_gloria0_1():
        pass
    elif clicar_imagem_gloria0_2():
        pass
    elif clicar_imagem_gloria0_3():
        pass
    elif clicar_imagem_gloria0_4():
        pass
    elif clicar_imagem_gloria0_5():
        pass
    elif clicar_imagem_gloria0_6():
        pass
    elif clicar_imagem_gloria0_7():
        pass
    elif clicar_imagem_gloria0_8():
        pass
    elif clicar_imagem_gloria0_9():
        pass
    elif clicar_imagem_gloria1_1():
        pass
    elif clicar_imagem_gloria1_1_1():
        pass
    elif clicar_imagem_gloria1_1_2():
        pass
    elif clicar_imagem_gloria1_1_3():
        pass
    elif clicar_imagem_gloria1_1_4():
        pass
    elif clicar_imagem_gloria1_1_5():
        pass
    else:
        print("Nenhuma das imagens foi encontrada. Saindo do processo.")
        exit()
