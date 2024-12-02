from pynput import mouse
import time
import keyboard
import pyautogui

cliques = []
screen_width, screen_height = pyautogui.size()

def on_click(x, y, button, pressed):
    if pressed:
        # Normalizar as coordenadas pelo tamanho da tela
        normalized_x = x / screen_width
        normalized_y = y / screen_height
        cliques.append((normalized_x, normalized_y))
        print(f"Registrado clique normalizado em: ({normalized_x}, {normalized_y})")
    return not keyboard.is_pressed('q')

def gravar_cliques():
    print("Iniciando a gravação de cliques. Mova o mouse e clique para registrar. Pressione 'q' para terminar.")

    # Iniciar o Listener do mouse
    with mouse.Listener(on_click=on_click) as listener:
        while True:
            if keyboard.is_pressed('q'):
                listener.stop()
                print("Gravação encerrada.")
                break
            time.sleep(0.1)

    return cliques

# Coletar os cliques
cliques_registrados = gravar_cliques()
print(f"Cliques gravados: {cliques_registrados}")

def executar_cliques(cliques):
    current_screen_width, current_screen_height = pyautogui.size()
    print("Executando cliques gravados...")

    for (normalized_x, normalized_y) in cliques:
        # Ajustar as coordenadas para a resolução atual da tela
        x = int(normalized_x * current_screen_width)
        y = int(normalized_y * current_screen_height)
        pyautogui.click(x, y)
        print(f"Clique executado em: ({x}, {y})")
        time.sleep(0.5)  # Tempo entre os cliques

