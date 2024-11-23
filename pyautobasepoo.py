import threading
from datetime import datetime
import pytz
import pyautogui
import schedule
import time

# Fuso horário de Brasília
BRASILIA_TZ = pytz.timezone('America/Sao_Paulo')

class CapturaTela:
    """Classe responsável pelas funções de captura de tela e OCR (Reconhecimento Óptico de Caracteres)"""

    def capturar_tela_inteira(self):
        """Captura a tela inteira e retorna uma imagem PIL."""
        screenshot = pyautogui.screenshot()  # Captura a tela inteira
        return screenshot

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
        # Agendar ações diárias ou específicas
        schedule.every().day.at("18:00").do(self.automacao.realizar_acao_18h)  # Exemplo de ação agendada para às 18h
        schedule.every().day.at("12:50").do(self.automacao.acao_diaria)  # Exemplo para realizar ações às 12:50

    def iniciar_agendamento(self):
        while True:
            schedule.run_pending()  # Executa as tarefas pendentes
            time.sleep(1)  # Espera 1 segundo antes de verificar novamente

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
        while datetime.now(BRASILIA_TZ) < hora_fim:
            if datetime.now(BRASILIA_TZ) >= hora_inicio:
                self.rotina_guardiao()
                print(f"Ação executada em: {datetime.now(BRASILIA_TZ).strftime('%Y-%m-%d %H:%M:%S')}")
                time.sleep(intervalo)
            else:
                print("Fora do horário especificado, finalizando a execução.")
                break

    def iniciar_automacao(self):
        """Inicia a automação e começa o agendamento das tarefas"""
        self.agendador.agendar_acao()
        self.agendador.iniciar_agendamento()

# Função para iniciar a rotina repetitiva em uma thread separada
def iniciar_rotina_repetitiva(automacao):
    hora_inicio = datetime.strptime("00:51", "%H:%M").replace(tzinfo=BRASILIA_TZ)  # Hora de início da ação ajustada para fuso horário
    hora_fim = datetime.strptime("00:53", "%H:%M").replace(tzinfo=BRASILIA_TZ)     # Hora de fim da ação ajustada para fuso horário
    intervalo = 10  # Intervalo de 10 segundos entre as ações
    automacao.acao_repetitiva_com_laco(hora_inicio, hora_fim, intervalo)

if __name__ == "__main__":
    automacao = Automacao()

    # Inicia a rotina repetitiva em uma thread separada para não bloquear o restante do código
    rotina_thread = threading.Thread(target=iniciar_rotina_repetitiva, args=(automacao,))
    rotina_thread.start()

    # Inicia o agendador de tarefas
    agendador_thread = threading.Thread(target=automacao.iniciar_automacao)
    agendador_thread.start()

    # Aguarda a thread da rotina repetitiva terminar
    rotina_thread.join()

    # Aguarda a thread do agendador terminar (isso garantirá que o script continue rodando)
    agendador_thread.join()
