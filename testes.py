from datetime import datetime, timedelta
import pyautogui
import pytesseract
import time
from PIL import Image
import schedule
import tkinter as tk
from tkinter import ttk
from petdiário import CapturaTela, ControleMouse, Agendador, Automacao

# Função para criar a janela de seleção
def criar_janela_selecao():
    root = tk.Tk()
    root.title("Seleção de Classe")

    # Variável para armazenar a opção selecionada
    opcao = tk.StringVar(value="não contém titã")

    # Função para capturar a opção selecionada e fechar a janela
    def confirmar():
        root.destroy()

    # Layout da janela
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Selecione a Classe:").grid(row=0, column=0, pady=5, sticky=tk.W)
    
    ttk.Radiobutton(frame, text="Contém Titã", variable=opcao, value="contém titã").grid(row=1, column=0, pady=5, sticky=tk.W)
    ttk.Radiobutton(frame, text="Não Contém Titã", variable=opcao, value="não contém titã").grid(row=2, column=0, pady=5, sticky=tk.W)
    
    ttk.Button(frame, text="Confirmar", command=confirmar).grid(row=3, column=0, pady=10)

    root.mainloop()
    
    return opcao.get()

# Função para executar a sequência de teclas com base na opção selecionada
def executar_sequencia_teclas(opcao):
    if opcao == "contém titã":
        for _ in range(4):
            pyautogui.hotkey('2')
            pyautogui.sleep(2)
        
        for _ in range(4):
            pyautogui.hotkey('space')
            pyautogui.sleep(2)

        for _ in range(7):
            pyautogui.hotkey('2')
            pyautogui.sleep(2)

        for _ in range(7):
            pyautogui.hotkey('1')
            pyautogui.sleep(2)

        for _ in range(7):
            pyautogui.hotkey('5')
    else:
        for _ in range(4):
            pyautogui.hotkey('3')
            pyautogui.sleep(2)
        
        for _ in range(4):
            pyautogui.hotkey('space')
            pyautogui.sleep(2)

        for _ in range(7):
            pyautogui.hotkey('3')
            pyautogui.sleep(2)

        for _ in range(7):
            pyautogui.hotkey('4')
            pyautogui.sleep(2)

        for _ in range(7):
            pyautogui.hotkey('6')

if __name__ == "__main__":
    automacao = Automacao()
    mouse = ControleMouse()

    # Chamar a função para criar a janela de seleção
    opcao_selecionada = criar_janela_selecao()

    mouse.clicar_imagem('mapa.png', 0.8)
    pyautogui.sleep(1)
    mouse.clicar_imagem('gloria.png', 0.8)
    pyautogui.sleep(5)
    mouse.clicar_imagem('gloria1.png', 0.8)
    pyautogui.sleep(2)
    
    imagens = ['gloria0.1.png', 'gloria0.2.png', 'gloria0.3.png', 'gloria0.4.png', 'gloria0.5.png', 'gloria0.6.png', 'gloria0.7.png', 'gloria0.8.png', 'gloria0.9.png', 'gloria1.1.png', 'gloria1.1.1.png', 'gloria1.1.2.png', 'gloria1.1.3.png', 'gloria1.1.4.png', 'gloria1.1.5.png']
    
    for imagem in imagens:
        img = mouse.clicar_imagem(imagem, 0.8)
        if img is not None:
            print(f"Imagem {imagem} encontrada e clicada.")
            break
        else:
            print(f"Imagem {imagem} não encontrada, tentando a próxima.")

    if img is None:
        print("Nenhuma das imagens foi encontrada. Saindo do loop.")
    else:
        pyautogui.sleep(1)
        mouse.localizar_imagem_na_area('gloria1.4.png', 'gloria1.2.png')
        pyautogui.sleep(3.5)

        # Executar a sequência de teclas com base na opção selecionada
        executar_sequencia_teclas(opcao_selecionada)