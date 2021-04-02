import cv2
import os
import numpy as np

#Definir carpeta donde estan almacenados los datos
carpetaDatos = os.path.expanduser('~/IA')
#Definir archivo donde esta almacenado el modelo por defecto
txtModelo = carpetaDatos+'/'+'modelo.txt'

#Menú para seleccionar el modelo de reconocimiento a utilizar
method = 'EigenFaces'
if not os.path.exists(txtModelo):
	print('Seleccione el modelo que desea utilizar:'
	'\n1. EigenFaces - Reconocedor facial enfocado en facciones de la cara.'
	'\n2. FisherFaces - Reconocedor facial enfocado en reconocer diferentes tonalidades.'
	'\n3. LBPH - Reconocedor facial enfocado en patrones faciales.')
	modelo = input('\nModelo a utilizar: ')
	if modelo == '1':
		print('Has seleccionado el modelo EigenFaces')
		method = 'EigenFaces'
	elif modelo == '2':
		print('Has seleccionado el modelo FisherFaces')
		method = 'FisherFaces'
	elif modelo == '3':
		print('Has seleccionado el modelo LBPH')
		method = 'LBPH'
	else:
		print('Utilizando modelo por defecto EigenFaces')
		method = 'EigenFaces'

	#Crear archivo donde almacenar el metodo seleccionado
	crearTxtModelo = open(txtModelo, 'w')
	crearTxtModelo.write(method)
	crearTxtModelo.close()
	rawMethod = open(txtModelo, 'r')
	method = rawMethod.read()
else:
	#Leer el archivo donde esta almacenado el metodo seleccionado
	rawMethod = open(txtModelo, 'r')
	method = rawMethod.read()

#Definir el reconocedor de emociones a partir del metodo seleccionado
if method == 'EigenFaces': emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
if method == 'FisherFaces': emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
if method == 'LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

#Directorio donde están almacenados los modelos de entrenamiento
emotion_recognizer.read(carpetaDatos + '/' + 'modelo'+method+'.xml')
#Definir carpeta donde estan almacenadas las fotos de las emociones
rutaDatos = carpetaDatos + '/Data'

imagePaths = os.listdir(rutaDatos)
print('Lista de emociones: ',imagePaths)
print('Presione la tecla "Esc" para cerrar la ventana')

#Definir como la camara el driver principal de capturador de video
camara = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Usar el entrenador de rostros de OpenCV Haar-cascade
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:

	#Crear el tamaño de la ventana y usar camara como input de la ventana
	ret,frame = camara.read()
	if ret == False: break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = gray.copy()

	#Detectar la cara en el input de la camara
	faces = faceClassif.detectMultiScale(gray,1.3,5)

	#Loop para asignar una emoción cada vez que reconozca una cara
	for (x,y,w,h) in faces:
		#Definicion de las dimensiones de la cara
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
		result = emotion_recognizer.predict(rostro)

		#Colocar el texto correspondiente a cada emocion encima del rectangulo de la cara reconocida
		cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

		# EigenFaces
		if method == 'EigenFaces':
			#Compara las coordenadas de la cara con las coordenadas del modelo entrenando para predecir una emocion
			if result[1] < 5700:
				#Dibujar un rectangulo sobre la cara reconocida con el texto de la emoción
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			else:
				#Dibujar un rectangulo rojo con el texto 'No identificado' cuando no se reconozca una emoción
				cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		
		# FisherFace
		if method == 'FisherFaces':
			#Compara las coordenadas de la cara con las coordenadas del modelo entrenando para predecir una emocion
			if result[1] < 500:
				#Dibujar un rectangulo sobre la cara reconocida con el texto de la emoción
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			else:
				#Dibujar un rectangulo rojo con el texto 'No identificado' cuando no se reconozca una emoción
				cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		
		# LBPHFace
		if method == 'LBPH':
			#Compara las coordenadas de la cara con las coordenadas del modelo entrenando para predecir una emocion
			if result[1] < 60:
				#Dibujar un rectangulo sobre la cara reconocida con el texto de la emoción
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			else:
				#Dibujar un rectangulo rojo con el texto 'No identificado' cuando no se reconozca una emoción
				cv2.putText(frame,'No identificado',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

	#Crear ventana
	cv2.imshow('Reconocimiento facial con emociones',frame)

	#Definicion de cuando se detendra el loop
	teclaEsc = cv2.waitKey(1)
	if teclaEsc == 27:
		break

#Cerrar ventanas y matar los procesos cuando se haya terminado
camara.release()
cv2.destroyAllWindows()