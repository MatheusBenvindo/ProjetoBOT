import pytesseract
from PIL import Image
import pyautogui

# Captura uma parte da tela onde os checkboxes estão
screenshot = pyautogui.screenshot(region=(0, 0, 800, 600))  # região da tela a ser capturada
screenshot.save('screenshot.png')

# Usar o pytesseract para realizar OCR na imagem
texto_detectado = pytesseract.image_to_string(Image.open('screenshot.png'))

# Verificar se o texto desejado está presente e localizar o checkbox
if 'Segundo' in texto_detectado:
    # Aqui você pode usar pyautogui.locateOnScreen() para clicar no checkbox que está ao lado do texto encontrado
    posicao = pyautogui.locateOnScreen('checkbox2.png')
    if posicao:
        pyautogui.click(posicao)
    else:
        print("Checkbox não encontrado.")
else:
    print("Texto não encontrado.")
