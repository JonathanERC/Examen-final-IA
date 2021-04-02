import cv2
import os
import numpy as np
import time

#Definir carpeta donde se almacenan todos los datos
carpetaDatos = os.path.expanduser('~/IA')

#Metodo para obtener modelos de reconocimiento facial
def obtenerModelo(method,facesData,labels):
	if method == 'EigenFaces': emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
	if method == 'FisherFaces': emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
	if method == 'LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

	#Entrenando el reconocedor de rostros
	print("Entrenando ( "+method+" )...")
	inicio = time.time()
	emotion_recognizer.train(facesData, np.array(labels))
	#Tiempo en segundos que se toma cada modelo en entrenarse
	tiempoEntrenamiento = time.time()-inicio
	print("Tiempo de entrenamiento ( "+method+" ): ", tiempoEntrenamiento)

	#Almacenando el modelo obtenido
	emotion_recognizer.write(carpetaDatos + '/' + 'modelo'+method+'.xml')

#Definir carpeta donde se guardaran las fotos de las emociones
rutaDatos = carpetaDatos + '/Data'

#Definir lista de emociones a partir de los directorios existentes
listaEmociones = os.listdir(rutaDatos)
print('Lista de emociones: ', listaEmociones)
print('Presione la tecla "Esc" para cerrar la ventana')

#Arreglo donde se almacenan las emociones identificadas
labels = []
#Arreglo donde se almacenaran las caras identificadas
facesData = []
label = 0

#Loop para listar directorios de emociones y almacenarlo en el arreglo de labels
for nameDir in listaEmociones:
	rutaEmociones = rutaDatos + '/' + nameDir

	for fileName in os.listdir(rutaEmociones):
		labels.append(label)
		facesData.append(cv2.imread(rutaEmociones+'/'+fileName,0))

	label = label + 1

#Enviar parametros a los modelos de entrenamiento
obtenerModelo('EigenFaces',facesData,labels)
obtenerModelo('FisherFaces',facesData,labels)
obtenerModelo('LBPH',facesData,labels)