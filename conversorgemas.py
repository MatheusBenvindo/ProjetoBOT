import subprocess

def desligar_computador():
    #desligamento do Windows
    subprocess.run(["shutdown", "/s", "/t", "1"])

desligar_computador()
