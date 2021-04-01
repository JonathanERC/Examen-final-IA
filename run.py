import os
import subprocess

dataPath = os.path.expanduser('~/IA')
dataName = os.path.expanduser(dataPath + '/'+'Data')

def entrenarModelo():
    print('Modelo no entrenado')
    print('Inicializando entrenamiento...')
    print('Capturando rostros...')
    subprocess.call(['python','capturandoRostros.py'], shell=True)
    print('Entrenando modelos...')
    subprocess.call(['python','entrenando.py'], shell=True)
    print('Reconocimiento Facial con Emociones...')
    subprocess.call(['python','reconocimientoEmociones.py'], shell=True)

if not os.path.exists(dataPath and dataPath):
    print('Dependencias no encontradas...')
    print('Instalando dependencias...')
    subprocess.call(['pip','install', 'opencv-contrib-python'], shell=True)
    subprocess.call(['pip','install', 'imutils'], shell=True)
    subprocess.call(['pip','install', 'numpy'], shell=True)
    subprocess.call(['pip','install', 'times'], shell=True)
    entrenarModelo()
elif not os.path.exists(dataName):
    entrenarModelo()
else:
    subprocess.call(['python', 'reconocimientoEmociones.py'], shell=True)