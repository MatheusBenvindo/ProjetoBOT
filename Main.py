from datetime import datetime, timedelta
import pyautogui
import pytesseract
import time
from PIL import Image
import schedule
import subprocess
import threading
import logging
import random

# Configuração de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class CapturaTela:
    def capturar_tela_inteira(self):
        return pyautogui.screenshot()

    def verificar_texto_na_imagem(self, screenshot):
        return pytesseract.image_to_string(screenshot)

    def encontrar_texto_na_imagem(self, screenshot, texto_busca):
        texto_extraido = pytesseract.image_to_string(screenshot)
        logging.info(f"Texto extraído da imagem: {texto_extraido}")
        return texto_busca.lower() in texto_extraido.lower()


class ControleMouse:
    def clicar_imagem(self, img_path, confidence=0.6):
        pyautogui.sleep(1)  # Pausa curta antes da ação
        img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)

        if img is not None:
            # Clica nas coordenadas da imagem encontrada
            pyautogui.click(img.x, img.y)
            logging.info(
                f"Imagem {img_path} encontrada e clicada nas coordenadas ({img.x}, {img.y})."
            )
            return True  # Retorna True quando o clique é bem-sucedido
        else:
            logging.warning(f"Imagem {img_path} não encontrada na tela.")
            return False  # Retorna False caso a imagem não seja encontrada

    def clicar_varias_vezes(self, img_path, num_cliques, delay=0.1, confidence=0.822):
        img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)
        if img is not None:
            for _ in range(num_cliques):
                pyautogui.click(img)
                time.sleep(delay)
            logging.info(
                f"Imagem {img_path} clicada {num_cliques} vezes com confiança {confidence}."
            )
        else:
            logging.warning(
                f"Imagem {img_path} não encontrada para clicar várias vezes."
            )

    def localizar_imagem_na_area(
        self, larger_img_path, smaller_img_path, confidence=0.6
    ):
        larger_img = pyautogui.locateOnScreen(larger_img_path, confidence=confidence)
        if larger_img is not None:
            region = (
                larger_img.left,
                larger_img.top,
                larger_img.width,
                larger_img.height,
            )
            smaller_img = pyautogui.locateCenterOnScreen(
                smaller_img_path, region=region, confidence=confidence
            )
            if smaller_img is not None:
                pyautogui.click(smaller_img)
                logging.info(
                    f"Imagem {smaller_img_path} encontrada e clicada dentro de {larger_img_path}."
                )
            else:
                logging.warning(
                    f"Imagem {smaller_img_path} não encontrada dentro de {larger_img_path}."
                )
        else:
            logging.warning(f"Imagem maior {larger_img_path} não encontrada na tela.")

    def ativar_visualizacao_janelas(self):
        pyautogui.hotkey("win", "tab")
        pyautogui.sleep(1)
        logging.info("Visualização das janelas ativada.")

    def clicar_posicao_aleatoria(self, imagem, confidence):
        localizacoes = list(pyautogui.locateAllOnScreen(imagem, confidence=confidence))
        if localizacoes:
            localizacao_aleatoria = random.choice(localizacoes)
            x, y = pyautogui.center(localizacao_aleatoria)
            pyautogui.click(x, y)
            return True
        else:
            print("Imagem repetida não encontrada na tela")
            return False


class Agendador:
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
    def __init__(self):
        self.controle_mouse = ControleMouse()
        self.captura_tela = CapturaTela()
        self.agendador = Agendador(self)

    def verificar_entrada_em_batalha(self, img_batalha_path):
        img_batalha = pyautogui.locateCenterOnScreen(img_batalha_path, confidence=0.8)
        if img_batalha is not None:
            logging.info("Entrou em batalha!")
            return True
        else:
            logging.info("Nenhuma batalha detectada.")
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
            logging.info("Executando ações de batalha...")
            break

    def verificar_batalha_periodicamente(self, intervalo_verificacao_batalha):
        while True:
            if self.verificar_entrada_em_batalha("verificacaobatalha.png"):
                self.tratar_batalha()
            time.sleep(intervalo_verificacao_batalha)

    def iniciar_verificacao_batalha(self, intervalo_verificacao_batalha):
        batalha_thread = threading.Thread(
            target=self.verificar_batalha_periodicamente,
            args=(intervalo_verificacao_batalha,),
        )
        batalha_thread.start()

    def acao_repetitiva_com_laco(self, hora_inicio, hora_fim, intervalo):
        logging.info("Iniciando loop...")
        self.iniciar_verificacao_batalha(10)

        while datetime.now() < hora_fim:
            if datetime.now() >= hora_inicio:
                self.rotina_guardiao()
                time.sleep(intervalo)
                hora_atual = datetime.now()
                logging.info(f"Hora Atual no Loop: {hora_atual}")

        logging.info(f"Loop encerrado em {hora_atual}")

    def realizar_acao_18h(self):
        logging.info("Executando ações programadas para as 18h")
        self.controle_mouse.ativar_visualizacao_janelas()
        screenshot = self.captura_tela.capturar_tela_inteira()
        texto = self.captura_tela.verificar_texto_na_imagem(screenshot)
        logging.info(f"Texto na imagem: {texto}")

    def acao_diaria(self):
        logging.info("Executando ações programadas para as 12:50")
        self.controle_mouse.ativar_visualizacao_janelas()

    def rotina_guardiao(self):
        self.controle_mouse.ativar_visualizacao_janelas()
        self.controle_mouse.clicar_imagem("maxicon.png", 0.8)
        self.controle_mouse.clicar_imagem("bauatv.png", 0.8)
        self.controle_mouse.clicar_imagem("korumaplat.png", 0.8)
        self.controle_mouse.clicar_imagem("entrar.png", 0.8)

    def iniciar_automacao(self):
        self.agendador.agendar_acao()
        self.agendador.iniciar_agendamento()

    def desligar_computador(self):
        subprocess.run(["shutdown", "/s", "/t", "1"])


class AutomacaoBatalha:
    def __init__(self):
        self.controle_mouse = ControleMouse()
        self.stop_event = threading.Event()

    def verificar_imagem_e_apertar_espaco(self, imagem_path, confidence=0.8):
        try:
            if self.controle_mouse.clicar_imagem(imagem_path, confidence):
                pyautogui.press("space")
                return True
        except pyautogui.ImageNotFoundException:
            # Suprimir mensagens de erro para imagens não encontradas
            pass
        return False

    def iniciar_sequencia_principal(self):
        sequencia_imagens = ["dragao1.png", "dragao2.png", "dragao3.png", "dragao4.png"]
        for imagem in sequencia_imagens:
            try:
                self.controle_mouse.clicar_imagem(imagem, 0.8)
                time.sleep(5)
            except pyautogui.ImageNotFoundException:
                # Suprimir mensagens de erro para imagens não encontradas
                continue

    def iniciar_sequencia_alternativa(self):
        sequencia_imagens = ["odin2.png", "odinex.png", "odin5.png"]
        for imagem in sequencia_imagens:
            try:
                self.controle_mouse.clicar_imagem(imagem, 0.8)
                time.sleep(5)
            except pyautogui.ImageNotFoundException:
                # Suprimir mensagens de erro para imagens não encontradas
                continue

    def verificar_batalha_com_imagens(self):
        end_time = datetime.now() + timedelta(hours=1)
        while not self.stop_event.is_set():
            if datetime.now() > end_time:
                break
            if self.verificar_imagem_e_apertar_espaco("dragaopet.png", 0.8):
                self.iniciar_sequencia_alternativa()
            else:
                self.iniciar_sequencia_principal()
            time.sleep(1)
        print("Verificação de batalha concluída.")

    def iniciar_verificacao_batalha_imagens(self):
        batalha_thread = threading.Thread(target=self.verificar_batalha_com_imagens)
        batalha_thread.start()

    def parar_verificacao_batalha_imagens(self):
        self.stop_event.set()
