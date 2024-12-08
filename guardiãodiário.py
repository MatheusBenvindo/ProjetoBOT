from datetime import datetime, timedelta
import pyautogui
import pytesseract
import time
from PIL import Image
import schedule
import subprocess
import threading
from Main import CapturaTela, ControleMouse, Agendador, Automacao


if __name__ == "__main__":
    automacao = Automacao()

    data_hoje = datetime.now().date()
    hora_inicio = datetime.combine(data_hoje, datetime.strptime("13:00", "%H:%M").time())
    tempo_total_execucao = 3300
    intervalo_execucao = 540
    hora_fim = hora_inicio + timedelta(seconds=tempo_total_execucao)

    while datetime.now() < hora_inicio:
        time.sleep(1)

    automacao.acao_repetitiva_com_laco(datetime.now(), hora_fim, intervalo_execucao)
    automacao.desligar_computador()