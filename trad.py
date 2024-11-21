import cv2
import numpy as np
import pyautogui
import pytesseract
from googletrans import Translator
import time
import threading
import tkinter as tk
from tkinter import scrolledtext

# Função para capturar a tela em uma região específica (como uma área de chat)
def capture_chat_area(region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

# Função para comparar se houve mudança na área capturada
def has_area_changed(prev_image, curr_image, threshold=10000):
    prev_gray = cv2.cvtColor(prev_image, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(curr_image, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(prev_gray, curr_gray)
    _, diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    non_zero_count = cv2.countNonZero(diff)
    return non_zero_count > threshold

# Função para realizar o template matching e desenhar o retângulo
def detect_chat_template(screenshot, template):
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    locations = np.where(result >= threshold)
    return locations

# Função para extrair texto da imagem usando OCR
def extract_text_from_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_image)
    return text

# Função para traduzir o texto utilizando Google Translate
def translate_text(text, src_lang='auto', target_lang='en'):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=target_lang)
    return translated.text

# Função para iniciar a captura e tradução
def start_translation():
    global capturing
    capturing = True
    prev_screenshot = capture_chat_area(chat_region)
    
    while capturing:
        curr_screenshot = capture_chat_area(chat_region)
        if has_area_changed(prev_screenshot, curr_screenshot):
            extracted_text = extract_text_from_image(curr_screenshot)
            if extracted_text.strip():
                translated_text = translate_text(extracted_text, target_lang='pt')  # Traduz para Português
                display_translation(translated_text)
        prev_screenshot = curr_screenshot
        time.sleep(0.5)

# Função para parar a captura
def stop_translation():
    global capturing
    capturing = False

# Função para atualizar a área de texto com a tradução
def display_translation(text):
    translation_display.insert(tk.END, f"Tradução: {text}\n")
    translation_display.yview(tk.END)

# Configuração da interface gráfica com Tkinter
root = tk.Tk()
root.title("Tradutor de Chat em Tempo Real")

# Configurar o layout
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Botões de Start/Stop
start_button = tk.Button(frame, text="Iniciar Captura", width=20, command=lambda: threading.Thread(target=start_translation, daemon=True).start())
start_button.grid(row=0, column=0, padx=5, pady=5)

stop_button = tk.Button(frame, text="Parar Captura", width=20, command=stop_translation)
stop_button.grid(row=0, column=1, padx=5, pady=5)

# Caixa de texto para mostrar as traduções
translation_display = scrolledtext.ScrolledText(root, width=50, height=15, wrap=tk.WORD)
translation_display.pack(padx=10, pady=10)
translation_display.insert(tk.END, "Aguardando mensagens...\n")

# Definir a região do chat na tela (ajuste conforme necessário)
screen_width, screen_height = pyautogui.size()
chat_region = (int(screen_width * 0.10), int(screen_height * 0.20), int(screen_width * 0.25), int(screen_height * 0.30))

# Carregar o template (imagem do chat)
template = cv2.imread('chat_template.png', 0)

# Variável de controle para saber se a captura deve ser interrompida
capturing = False

# Iniciar a interface gráfica
root.mainloop()
