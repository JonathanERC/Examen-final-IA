import os
import subprocess

rutaDatos = os.path.expanduser('~/IA')
carpetaDatos = os.path.expanduser(rutaDatos + '/'+'Data')

def entrenarModelo():
    print('Modelo no entrenado')
    print('Inicializando entrenamiento...')
    print('Capturando rostros...')
    subprocess.call(['python','capturandoRostros.py'], shell=True)
    print('Entrenando modelos...')
    subprocess.call(['python','entrenando.py'], shell=True)
    print('Reconocimiento Facial con Emociones...')
    subprocess.call(['python','reconocimientoEmociones.py'], shell=True)

if not os.path.exists(rutaDatos and carpetaDatos):
    print('Dependencias no encontradas...')
    print('Instalando dependencias...')
    subprocess.call(['pip','install', 'opencv-contrib-python'], shell=True)
    subprocess.call(['pip','install', 'imutils'], shell=True)
    subprocess.call(['pip','install', 'numpy'], shell=True)
    subprocess.call(['pip','install', 'times'], shell=True)
    entrenarModelo()
elif not os.path.exists(carpetaDatos):
    entrenarModelo()
else:
    subprocess.call(['python', 'reconocimientoEmociones.py'], shell=True)