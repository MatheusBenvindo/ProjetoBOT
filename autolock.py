import cv2
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

# Carregar o classificador Haar Cascade para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Função para verificar a presença (se rosto detectado)
def is_face_detected():
    # Inicializar a captura da câmera (usando a câmera padrão)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Força o uso do DirectShow
    # Verificar se a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Erro ao acessar a câmera")
        return False
    
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar imagem")
        cap.release()
        return False

    # Converter a imagem para escala de cinza (necessário para o classificador)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Se pelo menos um rosto for detectado, retorna True (pessoa presente)
    cap.release()
    
    return len(faces) > 0

# Função para bloquear o computador e mostrar uma caixa de alerta
def lock_computer():
    # Exibir uma caixa de mensagem (alerta)
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal do Tkinter
    messagebox.showwarning("Alerta", "Nenhuma pessoa detectada. Bloqueando o computador...")
    
    # Simular a ação de bloquear o Windows
    pyautogui.hotkey('win', 'l')  # Usando o atalho para bloquear o Windows

# Loop que roda a cada 30 segundos
while True:
    if not is_face_detected():
        lock_computer()
    
    # Espera 30 segundos antes de realizar a próxima verificação
    time.sleep(10)