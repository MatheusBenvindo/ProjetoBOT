import threading
import time
from datetime import datetime, timedelta
from Main import Automacao, ControleMouse


def executar_acao_por_uma_hora():
    automacao = Automacao()
    mouse = ControleMouse()

    end_time = datetime.now() + timedelta(hours=1)
    while datetime.now() < end_time:
        if mouse.clicar_posicao_aleatoria("imagemdasemana.png", 0.7):
            print("Imagem repetida escolhida aleatoriamente.")
        time.sleep(15)


if __name__ == "__main__":
    # Iniciar a thread
    thread = threading.Thread(target=executar_acao_por_uma_hora)
    thread.start()
    thread.join()
