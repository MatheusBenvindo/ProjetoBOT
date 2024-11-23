from datetime import datetime
import pyautogui
import pytesseract
import os
import time
from PIL import Image
import schedule

def capturar_tela_inteira():
    """Captura a tela inteira e retorna uma imagem PIL."""
    screenshot = pyautogui.screenshot()  # Captura a tela inteira
    return screenshot

def verificar_texto_na_imagem(screenshot):
    """Verifica o texto de uma imagem utilizando OCR (Tesseract)."""
    texto = pytesseract.image_to_string(screenshot)  # Realiza OCR na imagem
    return texto

def encontrar_texto_na_imagem(screenshot, texto_busca):
    """
    Localiza a presença de um texto específico na tela usando OCR.
    Retorna True se o texto de busca for encontrado, caso contrário, False.
    """
    texto_extraido = pytesseract.image_to_string(screenshot)  # OCR na imagem
    print("Texto extraído da imagem:", texto_extraido)

    # Verifica se o texto de busca está no texto extraído
    if texto_busca.lower() in texto_extraido.lower():
        return True
    else:
        return False

def clicar_imagem(img_path, confidence=0.6):
    """Clica em uma imagem na tela com uma confiança especificada"""
    pyautogui.sleep(1)
    img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)

    if img is not None:
        pyautogui.sleep(1)
        pyautogui.click(img.x, img.y)
    else:
        print(f"Imagem {img_path} não encontrada na tela.")

def ativar_visualizacao_janelas():
    """Ativa a visualização das janelas (Windows + Tab)"""
    pyautogui.hotkey('win', 'tab')
    pyautogui.sleep(1)

def realizar_acao_18h():
    """Ação a ser realizada às 18h"""
    print("Executando ações programadas para as 18h")
    ativar_visualizacao_janelas()
    screenshot = capturar_tela_inteira()
    texto = verificar_texto_na_imagem(screenshot)
    print(f"Texto na imagem: {texto}")

def acao_diaria():
    """Ação a ser realizada periodicamente (exemplo às 12:50)"""
    print("Executando ações programadas para as 12:50")
    ativar_visualizacao_janelas()

def rotina_guardiao():
    """Rotina guardião que ativa janelas e realiza cliques de acordo com imagens"""
    ativar_visualizacao_janelas()
    clicar_imagem("maxicon.png", 0.8)
    clicar_imagem("bauatv.png", 0.8)
    clicar_imagem("korumaplat.png", 0.8)
    clicar_imagem("entrar.png", 0.8)

def agendar_acao():
    # Agendar ações diárias ou específicas
    schedule.every().day.at("18:00").do(realizar_acao_18h)  # Exemplo de ação agendada para às 18h
    schedule.every().day.at("12:50").do(acao_diaria)  # Exemplo para realizar ações às 12:50

def iniciar_agendamento():
    while True:
        schedule.run_pending()  # Executa as tarefas pendentes
        time.sleep(1)  # Espera 1 segundo antes de verificar novamente

def acao_repetitiva_com_laco(hora_inicio, hora_fim, intervalo):
    """Executa ações repetitivas entre uma hora de início e uma hora de fim, em intervalos especificados"""
    while datetime.now() < hora_fim:
        if datetime.now() >= hora_inicio:
            rotina_guardiao()
            time.sleep(intervalo)

def verificar_checkbox_por_texto(screenshot, texto_busca):
    """Função para verificar a presença de uma checkbox com base em um texto específico"""
    # Aqui você pode adicionar a lógica para verificar a checkbox com base no texto extraído da imagem
    # Isso pode incluir localizar a checkbox e verificar seu estado
    texto_extraido = pytesseract.image_to_string(screenshot)
    print("Texto extraído da imagem para checkbox:", texto_extraido)

    if texto_busca.lower() in texto_extraido.lower():
        # Lógica para verificar o estado da checkbox
        checkbox_loc = pyautogui.locateCenterOnScreen("checkbox.png", confidence=0.8)
        if checkbox_loc is not None:
            print("Checkbox encontrada.")
            return True
        else:
            print("Checkbox não encontrada.")
            return False
    else:
        print("Texto para checkbox não encontrado.")
        return False

if __name__ == "__main__":
    # Exemplo de agendamento de uma tarefa repetitiva:
    hora_inicio = datetime.strptime("12:50", "%H:%M")  # Hora de início da ação repetitiva
    hora_fim = datetime.strptime("13:50", "%H:%M")     # Hora de fim da ação repetitiva
    intervalo = 600  # Intervalo de 10 minutos entre as ações
    acao_repetitiva_com_laco(hora_inicio, hora_fim, intervalo)

    rotina_guardiao()

    pyautogui.sleep(1)

    # Definir as variáveis para a ação repetitiva com timer
    hora_inicio1 = datetime.strptime("12:50", "%H:%M")  # Hora de início da ação
    hora_fim1 = datetime.strptime("13:50", "%H:%M")     # Hora de fim da ação
    intervalo1 = 600  # Intervalo de 10 minutos entre as ações

    # Chama a função de ação repetitiva com timer
    acao_repetitiva_com_laco(hora_inicio1, hora_fim1, intervalo1)

    # Comandos adicionais (fechar janelas, etc.)
    for _ in range(2):
        pyautogui.hotkey("alt", "f4")  # Fecha as janelas abertas
    for _ in range(3):
        pyautogui.hotkey("tab")  # Alterna entre as janelas abertas
    pyautogui.hotkey("enter")  # Pressiona Enter