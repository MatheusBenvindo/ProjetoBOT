from datetime import datetime, timedelta
import pyautogui
import time

# Obter a data atual
data_hoje = datetime.now().date()

# Teste da função datetime.strptime com data atual
hora_inicio = datetime.combine(data_hoje, datetime.strptime("10:35", "%H:%M").time())
print("Hora de Início:", hora_inicio)

# Teste da função timedelta para adicionar segundos
tempo_total_execucao = 600  # 600 segundos = 10 minutos
hora_fim = hora_inicio + timedelta(seconds=tempo_total_execucao)
print("Hora de Fim:", hora_fim)

# Teste da função datetime.now
hora_atual = datetime.now()
print("Hora Atual:", hora_atual)

# Teste da função time.sleep
print("Iniciando pausa de 20 segundos...")
time.sleep(20)
print("Fim da pausa de 20 segundos")

# Teste de loop com hora atual e hora de fim
print("Iniciando loop...")
while datetime.now() < hora_fim:
    hora_atual = datetime.now()
    print("Hora Atual no Loop:", hora_atual)
    time.sleep(10)  # Pausa de 10 segundos
print(f"Loop encerrado em {hora_atual}")
