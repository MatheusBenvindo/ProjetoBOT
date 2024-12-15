from Main import Automacao, ControleMouse, AutomacaoBatalha, Agendador
import threading
import logging
import time

# Configuração de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    mouse = ControleMouse()

    mouse.clicar_imagem("arredores.png")
    time.sleep(15)
    mouse.clicar_imagem("arqueologia1.png")
    time.sleep(1)
    mouse.clicar_imagem("arqueologia3.png")
    time.sleep(3)

    for _ in range(30):
        mouse.clicar_imagem("arqueologia4.png")
        time.sleep(30)
