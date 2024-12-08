from datetime import datetime, timedelta
import pyautogui
import pytesseract
import time
from PIL import Image
import schedule
import subprocess
import threading

class CapturaTela:
    """Captura de tela e OCR"""

    def capturar_tela_inteira(self):
        return pyautogui.screenshot()

    def verificar_texto_na_imagem(self, screenshot):
        return pytesseract.image_to_string(screenshot)

    def encontrar_texto_na_imagem(self, screenshot, texto_busca):
        texto_extraido = pytesseract.image_to_string(screenshot)
        print("Texto extraído da imagem:", texto_extraido)
        return texto_busca.lower() in texto_extraido.lower()

class ControleMouse:
    """Controle do mouse"""

    def clicar_imagem(self, img_path, confidence=0.6):
        pyautogui.sleep(1)
        img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)
        if img is not None:
            pyautogui.click(img.x, img.y)
        else:
            print(f"Imagem {img_path} não encontrada na tela.")

    def ativar_visualizacao_janelas(self):
        pyautogui.hotkey('win', 'tab')
        pyautogui.sleep(1)

class Agendador:
    """Agendamento de tarefas"""

    def __init__(self, automacao):
        self.automacao = automacao

    def agendar_acao(self):
        schedule.every().day.at("18:00").do(self.automacao.realizar_acao_18h)
        schedule.every().day.at("12:50").do(self.automacao.acao_diaria)

    def iniciar_agendamento(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

class Automacao:
    """Automação principal"""

    def __init__(self):
        self.controle_mouse = ControleMouse()
        self.captura_tela = CapturaTela()
        self.agendador = Agendador(self)

    def verificar_entrada_em_batalha(self, img_batalha_path):
        img_batalha = pyautogui.locateCenterOnScreen(img_batalha_path, confidence=0.8)
        if img_batalha is not None:
            print("Entrou em batalha!")
            return True
        else:
            print("Nenhuma batalha detectada.")
            return False

    def tratar_batalha(self):
        while self.verificar_entrada_em_batalha("verificacaobatalha.png"):
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
            break

    def verificar_batalha_periodicamente(self, intervalo_verificacao_batalha):
        while True:
            if self.verificar_entrada_em_batalha("verificacaobatalha.png"):
                self.tratar_batalha()
            time.sleep(intervalo_verificacao_batalha)

    def iniciar_verificacao_batalha(self, intervalo_verificacao_batalha):
        batalha_thread = threading.Thread(target=self.verificar_batalha_periodicamente, args=(intervalo_verificacao_batalha,))
        batalha_thread.start()

    def acao_repetitiva_com_laco(self, hora_inicio, hora_fim, intervalo):
        print("Iniciando loop...")

        self.iniciar_verificacao_batalha(10)

        while datetime.now() < hora_fim:
            if datetime.now() >= hora_inicio:
                self.rotina_guardiao()
                time.sleep(intervalo)
                hora_atual = datetime.now()
                print("Hora Atual no Loop:", hora_atual)

        print(f"Loop encerrado em {hora_atual}")

    def realizar_acao_18h(self):
        print("Executando ações programadas para as 18h")
        self.controle_mouse.ativar_visualizacao_janelas()
        screenshot = self.captura_tela.capturar_tela_inteira()
        texto = self.captura_tela.verificar_texto_na_imagem(screenshot)
        print(f"Texto na imagem: {texto}")

    def acao_diaria(self):
        print("Executando ações programadas para as 12:50")
        self.controle_mouse.ativar_visualizacao_janelas()

    def rotina_guardiao(self):
        self.controle_mouse.ativar_visualizacao_janelas()
        self.controle_mouse.clicar_imagem("maxicon.png", 0.8)
        self.controle_mouse.clicar_imagem("bauatv.png", 0.8)
        self.controle_mouse.clicar_imagem("korumaplat.png", 0.8)

    def iniciar_automacao(self):
        self.agendador.agendar_acao()
        self.agendador.iniciar_agendamento()

    def desligar_computador(self):
        subprocess.run(["shutdown", "/s", "/t", "1"])

"""# Código principal para iniciar a automação
if __name__ == "__main__":
    automacao = Automacao()

    data_hoje = datetime.now().date()
    hora_inicio = datetime.combine(data_hoje, datetime.strptime("12:50", "%H:%M").time())
    tempo_total_execucao = 3300
    intervalo_execucao = 540
    hora_fim = hora_inicio + timedelta(seconds=tempo_total_execucao)

    while datetime.now() < hora_inicio:
        time.sleep(1)

    automacao.acao_repetitiva_com_laco(datetime.now(), hora_fim, intervalo_execucao)
    automacao.desligar_computador()"""
