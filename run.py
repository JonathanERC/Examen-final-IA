import os
import subprocess
import sys, getopt
import shutil

#Definir carpeta donde estan almacenados los datos
rutaDatos = os.path.expanduser('~/IA')
carpetaDatos = os.path.expanduser(rutaDatos + '/'+'Data')
txtModelo = rutaDatos+'/'+'modelo.txt'
txtPic = rutaDatos+'/'+'cantPic.txt'

#Definición del metodo que corre el entrenamiento del modelo
def entrenarModelo():
    print('\nModelo no entrenado')
    print('Inicializando entrenamiento...')
    print('Capturando rostros...')
    subprocess.call(['python','capturandoRostros.py'], shell=True)
    print('Entrenando modelos...')
    subprocess.call(['python','entrenando.py'], shell=True)
    print('\nReconocimiento Facial con Emociones...')
    subprocess.call(['python','reconocimientoEmociones.py'], shell=True)

#Argumentos validos
def argumentos():
    print('Argumentos disponibles:'
    '\n -r      Reentrenar modelos.'
    '\n -p      Indicar cantidad maxima de fotos para entrenamientos.'
    '\n -m      Selecionar modelo de reconocimiento.'
    '\n -h      Lista de argumentos.'
    '\n -t      Reiniciar todo el sistema y parametros.')

try:
    opts, args = getopt.getopt(sys.argv[1:],'hrpmt')
except getopt.GetoptError:
    print ('Argumento invalido, coloque -h para la lista de argumentos.')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        argumentos()
        sys.exit()
    elif opt == "-r":
        print('Reentrenando modelos...')
        shutil.rmtree(carpetaDatos)
        entrenarModelo()
    elif opt == "-p":
        print('Reiniciando cantidad maxima de fotos para entrenamiento...')
        os.remove(txtPic)
        entrenarModelo()
    elif opt == "-m":
        print('Reiniciando modelo de reconocimeinto...')
        os.remove(txtModelo)
        entrenarModelo()
    elif opt == "-t":
        print('Reiniciando todo el sistema y parametros...')
        shutil.rmtree(rutaDatos)
        entrenarModelo()

#Condición que detecta si las dependencias del modelo existen, en caso contrario las instala
if not os.path.exists(rutaDatos):
    print('Dependencias no encontradas...')
    print('Instalando dependencias...')
    subprocess.call(['pip','install', 'opencv-contrib-python'], shell=True)
    subprocess.call(['pip','install', 'imutils'], shell=True)
    subprocess.call(['pip','install', 'numpy'], shell=True)
    subprocess.call(['pip','install', 'times'], shell=True)
    os.makedirs(rutaDatos)
    entrenarModelo()
#Condición que detecta si la carpeta de datos existe para entrenar el modelo
elif not os.path.exists(carpetaDatos or txtModelo or txtPic):
    entrenarModelo()
#Si ninguna de las condiciones anteriores se dan, entonces correr el programa
else:
    subprocess.call(['python', 'reconocimientoEmociones.py'], shell=True)
