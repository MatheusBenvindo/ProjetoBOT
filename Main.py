from datetime import datetime, timedelta
import pyautogui
import pytesseract
import time
from PIL import Image
import schedule
import subprocess

class CapturaTela:
    """Classe responsável pelas funções de captura de tela e OCR (Reconhecimento Óptico de Caracteres)"""

    def capturar_tela_inteira(self):
        """Captura a tela inteira e retorna uma imagem PIL."""
        screenshot = pyautogui.screenshot()  # Captura a tela inteira
        return screenshot

    def verificar_texto_na_imagem(self, screenshot):
        """Verifica o texto de uma imagem utilizando OCR (Tesseract)."""
        texto = pytesseract.image_to_string(screenshot)  # Realiza OCR na imagem
        return texto

    def encontrar_texto_na_imagem(self, screenshot, texto_busca):
        """Localiza a presença de um texto específico na tela usando OCR."""
        texto_extraido = pytesseract.image_to_string(screenshot)  # OCR na imagem
        print("Texto extraído da imagem:", texto_extraido)
        return texto_busca.lower() in texto_extraido.lower()

class ControleMouse:
    """Classe responsável pelas ações de controle do mouse (clicar nas imagens, marcar checkboxes, etc.)"""

    def clicar_imagem(self, img_path, confidence=0.6):
        """Clica em uma imagem na tela com uma confiança especificada"""
        pyautogui.sleep(1)
        img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)
        if img is not None:
            pyautogui.sleep(1)
            pyautogui.click(img.x, img.y)
        else:
            print(f"Imagem {img_path} não encontrada na tela.")

    def ativar_visualizacao_janelas(self):
        """Ativa a visualização das janelas (Windows + Tab)"""
        pyautogui.hotkey('win', 'tab')
        pyautogui.sleep(1)

class Agendador:
    """Classe responsável por agendar e gerenciar as tarefas com o schedule"""

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
    """Classe principal que orquestra a automação"""

    def __init__(self):
        self.controle_mouse = ControleMouse()
        self.captura_tela = CapturaTela()
        self.agendador = Agendador(self)

    def verificar_entrada_em_batalha(self, img_batalha_path):
        """Função que verifica se entrou em batalha pela imagem"""
        img_batalha = pyautogui.locateCenterOnScreen(img_batalha_path, confidence=0.8)
        
        if img_batalha is not None:
            print("Entrou em batalha!")
            self.tratar_batalha()
        else:
            print("Nenhuma batalha detectada.")

    def tratar_batalha(self):
        while (self.verificar_entrada_em_batalha):
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

    def iniciar_verificacao_batalha(self, img_batalha_path, intervalo):
        """Inicia a verificação de batalha com intervalo ajustável"""
        self.intervalo_verificacao_batalha = intervalo
        while True:
            self.verificar_entrada_em_batalha(img_batalha_path)
            time.sleep(self.intervalo_verificacao_batalha)

    def realizar_acao_18h(self):
        """Ação a ser realizada às 18h"""
        print("Executando ações programadas para as 18h")
        self.controle_mouse.ativar_visualizacao_janelas()
        screenshot = self.captura_tela.capturar_tela_inteira()
        texto = self.captura_tela.verificar_texto_na_imagem(screenshot)
        print(f"Texto na imagem: {texto}")

    def acao_diaria(self):
        """Ação a ser realizada periodicamente (exemplo às 12:50)"""
        print("Executando ações programadas para as 12:50")
        self.controle_mouse.ativar_visualizacao_janelas()

    def rotina_guardiao(self):
        """Rotina guardião que ativa janelas e realiza cliques de acordo com imagens"""
        self.controle_mouse.ativar_visualizacao_janelas()
        self.controle_mouse.clicar_imagem("maxicon.png", 0.8)
        self.controle_mouse.clicar_imagem("bauatv.png", 0.8)
        self.controle_mouse.clicar_imagem("korumaplat.png", 0.8)
        self.iniciar_verificacao_batalha("verificacaobatalha.png", 10)

    def acao_repetitiva_com_laco(self, hora_inicio, hora_fim, intervalo):
        """Executa ações repetitivas entre uma hora de início e uma hora de fim, em intervalos especificados"""
        print("Iniciando loop...")
        while datetime.now() < hora_fim:
            if datetime.now() >= hora_inicio:
                self.rotina_guardiao()
                time.sleep(intervalo)
                # Atualiza a hora atual e imprime para verificação
                hora_atual = datetime.now()
                print("Hora Atual no Loop:", hora_atual)
        print(f"Loop encerrado em {hora_atual}")

    def iniciar_automacao(self):
        """Inicia a automação e começa o agendamento das tarefas"""
        self.agendador.agendar_acao()
        self.agendador.iniciar_agendamento()
    def desligar_computador():
    # Executa o comando de desligamento do Windows
        subprocess.run(["shutdown", "/s", "/t", "1"])
