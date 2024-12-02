import pyautogui
import time
import keyboard  # Biblioteca correta para verificar teclas pressionadas
from pynput import mouse, keyboard as pynput_keyboard

# Lista para armazenar eventos
eventos = []

# Função para gravar eventos de mouse
def on_click(x, y, button, pressed):
    if pressed:
        eventos.append(('click', x, y, time.time()))
        print(f"Clique registrado em: ({x}, {y})")
    return not keyboard.is_pressed('q')

# Função para gravar eventos de teclado
def on_key_press(key):
    try:
        eventos.append(('key', key.char, time.time()))
    except AttributeError:
        eventos.append(('key', key, time.time()))
    return not keyboard.is_pressed('q')

# Função para gravar eventos
def gravar_eventos():
    print("Gravação de eventos iniciada. Pressione 'q' para parar a gravação.")
    
    # Listener de mouse e teclado
    with mouse.Listener(on_click=on_click) as mouse_listener, \
         pynput_keyboard.Listener(on_press=on_key_press) as keyboard_listener:
        
        mouse_listener.join()
        keyboard_listener.join()

# Chamar a função de gravação
gravar_eventos()
print("Gravação de eventos finalizada.")
print(eventos)  # Exibe os eventos gravados

# Salvar os eventos em um arquivo (opcional)
with open("eventos_gravados.txt", "w") as f:
    for evento in eventos:
        f.write(f"{evento}\n")
