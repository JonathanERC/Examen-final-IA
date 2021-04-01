import cv2
import os
import imutils

#Lista de emociones
emociones = ['Alegre', 'Triste', 'Enfadado', 'Neutro']

#Loop para poblar la base de datos de emociones
for nombreEmocion in emociones:
	#Pausa entre cada emocion
	pausa = input('Presiona "Enter" para entrenar la emoción de ' + nombreEmocion)

	#Definir carpeta donde se almacenaran todos los datos
	carpetaDatos = os.path.expanduser('~/IA')
	#Definir carpeta donde se guardaran las fotos de las emociones
	rutaDatos = carpetaDatos + '/Data'
	#Concatenar rutaDatos y carpetaDatos
	rutaEmociones = rutaDatos + '/' + nombreEmocion

	#Condicion que valida si la ruta de emociones existe, en caso contrario crearlo
	if not os.path.exists(rutaEmociones):
		print('Carpeta creada: ',rutaEmociones)
		os.makedirs(rutaEmociones)

	#Usar como input del modelo la capturadora de video
	camara = cv2.VideoCapture(0,cv2.CAP_DSHOW)

	#Usar el entrenador de rostros de OpenCV Haar-cascade
	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
	count = 0

	while True:

		ret, frame = camara.read()
		if ret == False: break
		frame =  imutils.resize(frame, width=640)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		auxFrame = frame.copy()

		faces = faceClassif.detectMultiScale(gray,1.3,5)

		for (x,y,w,h) in faces:
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			rostro = auxFrame[y:y+h,x:x+w]
			rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
			cv2.imwrite(rutaEmociones + '/rostro_{}.jpg'.format(count),rostro)
			count = count + 1
		cv2.imshow('frame',frame)

		k =  cv2.waitKey(1)
		if k == 27 or count >= 200:
			break

	camara.release()
	cv2.destroyAllWindows()