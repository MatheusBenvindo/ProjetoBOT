def acao_repetitiva_com_laco(self, hora_inicio, hora_fim, intervalo):
        """Executa ações repetitivas entre uma hora de início e uma hora de fim, em intervalos especificados"""
        print("Iniciando loop...")
        img_batalha_path = "verificacaobatalha.png"
        intervalo_verificacao_batalha = 70  # Intervalo de verificação em segundos
        while datetime.now() < hora_fim:
            if datetime.now() >= hora_inicio:
                self.rotina_guardiao()
                time.sleep(intervalo)
                hora_atual = datetime.now()
                print("Hora Atual no Loop:", hora_atual)

                # Verificação de batalha
                img_batalha = pyautogui.locateCenterOnScreen(img_batalha_path, confidence=0.8)
                if img_batalha is not None:
                    print("Entrou em batalha!")
                    while True:
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
                        print("Executando ações de batalha...")
                        break  # Sai do loop após uma execução
                else:
                    print("Nenhuma batalha detectada.")
                time.sleep(intervalo_verificacao_batalha)
        print(f"Loop encerrado em {hora_atual}")

