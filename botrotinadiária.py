from datetime import datetime, timedelta
import pyautogui
import pytesseract
import time
from PIL import Image
import schedule

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

    def clicar_varias_vezes(self, img_path, num_cliques, delay=0.1, confidence=0.822):
        """Clica em uma posição específica várias vezes rapidamente, utilizando a confiança especificada"""
        img = pyautogui.locateCenterOnScreen(img_path, confidence=confidence)
        if img is not None:
            for _ in range(num_cliques):
                pyautogui.click(img)
                time.sleep(delay)  # Pequeno atraso entre os cliques para garantir que todos sejam registrados
            print(f"Imagem {img_path} clicada {num_cliques} vezes com confiança {confidence}.")
    
        else:
            print(f"Imagem {img_path} não encontrada para clicar várias vezes com confiança {confidence}.")

    def localizar_imagem_na_area(self, larger_img_path, smaller_img_path, confidence=0.6):
        """Localiza uma imagem menor dentro de uma imagem maior e clica nela"""
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
        self.controle_mouse.clicar_imagem("entrar.png", 0.8)

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

if __name__ == "__main__":
    automacao = Automacao()
    mouse = ControleMouse()

    mouse.clicar_imagem('mapa.png', 0.8)
    pyautogui.sleep(1)
    mouse.clicar_varias_vezes('mapa1.1.png', 29, delay=0.1, confidence=0.6)
    mouse.clicar_imagem('pet1.png',0.8)
    pyautogui.sleep(9)
    mouse.clicar_imagem('pet1.1.png', 0.8)
    pyautogui.sleep(5)
    mouse.clicar_imagem('pet1.2.png', 0.6)
    pyautogui.sleep(5)
    mouse.clicar_imagem('pet1.3.png', 0.6)
    pyautogui.sleep(5)
    mouse.clicar_varias_vezes('pet1.3.png', 25, delay=2, confidence=0.8)

    mouse.clicar_imagem('mapa.png', 0.8)
    pyautogui.sleep(1)
    mouse.clicar_varias_vezes('mapa1.1.png', 29, delay=0.1, confidence=0.6)
    mouse.clicar_imagem ('gloria.png', 0.8)
    pyautogui.sleep(5)
    mouse.clicar_imagem('gloria1.png', 0.8)