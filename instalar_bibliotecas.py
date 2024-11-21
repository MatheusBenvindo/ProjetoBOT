# instalar_bibliotecas.py
import subprocess
import sys

def instalar_bibliotecas():
    """
    Verifica se as bibliotecas necessárias estão instaladas.
    Se não estiverem, instala-as automaticamente.
    """
    bibliotecas = [
        'pyautogui',
        'pytesseract',
        'schedule',
        'pillow'
    ]

    for biblioteca in bibliotecas:
        try:
            # Tenta importar a biblioteca
            __import__(biblioteca)
            print(f"{biblioteca} já está instalado.")
        except ImportError:
            print(f"{biblioteca} não encontrado. Instalando...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])

if __name__ == "__main__":
    instalar_bibliotecas()
