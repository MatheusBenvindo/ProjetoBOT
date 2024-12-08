from datetime import datetime, timedelta
import pyautogui
import pytesseract
import time
from PIL import Image
import schedule
from Main import CapturaTela, ControleMouse, Agendador, Automacao



def batalha():
    img_batalha_path = "verificacaobatalha.png"
    intervalo_verificacao_batalha = 70  # Intervalo de verificação em segundos
    while True:
        img_batalha = pyautogui.locateCenterOnScreen(img_batalha_path, confidence=0.8)
        if img_batalha is not None:
            print("Entrou em batalha!")
            while True:
                for _ in range(7):
                    pyautogui.hotkey("4")
                for _ in range(7):
                    pyautogui.hotkey("3")
                for _ in range(7):
                    pyautogui.hotkey("2")
                for _ in range(7):
                    pyautogui.hotkey("5")
                for _ in range(7):
                    pyautogui.hotkey("1")
                print("Executando ações de batalha...")
                break  # Sai do loop após uma execução
        else:
            print("Nenhuma batalha detectada.")
        time.sleep(intervalo_verificacao_batalha)

if __name__ == "__main__":
    automacao = Automacao()

    # data atual
    data_hoje = datetime.now().date()

    # hora de início
    hora_inicio = datetime.combine(data_hoje, datetime.strptime("13:00", "%H:%M").time())
    # segundos (600 segundos = 10 minutos)
    tempo_total_execucao = 3300 
    # Intervalo segundos
    intervalo_execucao = 540  

    # Calcula a hora final com base no tempo total de execução
    hora_fim = hora_inicio + timedelta(seconds=tempo_total_execucao)

    # Aguarda até a hora de início
    while datetime.now() < hora_inicio:
        time.sleep(1)

    # Chama a função de ação repetitiva com intervalo
    automacao.acao_repetitiva_com_laco(datetime.now(), hora_fim, intervalo_execucao)

automacao.desligar_computador()
