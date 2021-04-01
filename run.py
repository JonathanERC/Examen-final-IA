import os
import subprocess

rutaDatos = os.path.expanduser('~/IA')
carpetaDatos = os.path.expanduser(rutaDatos + '/'+'Data')

#Definición del metodo que corre el entrenamiento del modelo
def entrenarModelo():
    print('Modelo no entrenado')
    print('Inicializando entrenamiento...')
    print('Capturando rostros...')
    subprocess.call(['python','capturandoRostros.py'], shell=True)
    print('Entrenando modelos...')
    subprocess.call(['python','entrenando.py'], shell=True)
    print('Reconocimiento Facial con Emociones...')
    subprocess.call(['python','reconocimientoEmociones.py'], shell=True)

#Condición que detecta si las dependencias del modelo existen, en caso contrario las instala
if not os.path.exists(rutaDatos and carpetaDatos):
    print('Dependencias no encontradas...')
    print('Instalando dependencias...')
    subprocess.call(['pip','install', 'opencv-contrib-python'], shell=True)
    subprocess.call(['pip','install', 'imutils'], shell=True)
    subprocess.call(['pip','install', 'numpy'], shell=True)
    subprocess.call(['pip','install', 'times'], shell=True)
    entrenarModelo()
#Condición que detecta si la carpeta de datos existe para entrenar el modelo
elif not os.path.exists(carpetaDatos):
    entrenarModelo()
#Si ninguna de las condiciones anteriores se dan, entonces correr el programa
else:
    subprocess.call(['python', 'reconocimientoEmociones.py'], shell=True)
