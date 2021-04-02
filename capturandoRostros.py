import cv2
import os
import imutils

#Crear arreglo de emociones
emociones = []
cantEmociones = int(input('\nIngrese la cantidad de emociones a entrenar: '))

#Loop para agregar emociones al arreglo
for i in range(0, cantEmociones):
	elementos = input('Ingrese nombre de la emoción: ')
	emociones.append(elementos) # adding the element

#Definir carpeta donde se almacenaran todos los datos
carpetaDatos = os.path.expanduser('~/IA')

#Cantidad de fotos maximas para entrenar el modelo
txtPic = carpetaDatos+'/'+'cantPic.txt'

cantPic = int(300)
if not os.path.exists(txtPic):
	inputCantPic = input('\nIndique la cantidad de fotos a tomar para poblar la DB: ')
	crearCantPic = open(txtPic, 'w')
	crearCantPic.write(inputCantPic)
	crearCantPic.close()
	rawCantPic = open(txtPic, 'r')
	cantPic = int(rawCantPic.read())
else:
	#Leer el archivo donde esta almacenado la cantidad maxima de fotos
	rawCantPic = open(txtPic, 'r')
	cantPic = int(rawCantPic.read())

#Loop para poblar la base de datos de emociones
for nombreEmocion in emociones:
	#Pausa entre cada emocion
	pausa = input('Presiona "Enter" para entrenar la emoción de ' + nombreEmocion)

	#Definir carpeta donde se guardaran las fotos de las emociones
	rutaDatos = carpetaDatos + '/Data'
	#Concatenar rutaDatos y carpetaDatos
	rutaEmociones = rutaDatos + '/' + nombreEmocion

	#Condicion que valida si la ruta de emociones existe, en caso contrario crearlo
	if not os.path.exists(rutaEmociones):
		print('Carpeta creada: ',rutaEmociones)
		os.makedirs(rutaEmociones)

	#Definir como la camara el driver principal de capturador de video
	camara = cv2.VideoCapture(0,cv2.CAP_DSHOW)

	#Usar el entrenador de rostros de OpenCV Haar-cascade
	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
	contador = 0

	while True:

		#Crear el tamaño de la ventana y usar camara como input de la ventana
		ret, frame = camara.read()
		if ret == False: break
		frame =  imutils.resize(frame, width=640)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		auxFrame = frame.copy()

		#Detectar la cara en el input de la camara
		faces = faceClassif.detectMultiScale(gray,1.3,5)

		#Loop para hacer una foto cada vez que reconozca una cara
		for (x,y,w,h) in faces:
			#Crear un rectangulo sobre la cara reconocida
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			rostro = auxFrame[y:y+h,x:x+w]
			rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
			#Hacer una foto cada vez que se reconozca una cara
			cv2.imwrite(rutaEmociones + '/rostro_{}.jpg'.format(contador),rostro)
			contador = contador + 1

		#Crear ventana
		cv2.imshow('Reconocimiento facial',frame)

		#Definicion de cuando se detendra el loop
		teclaEsc =  cv2.waitKey(1)
		if teclaEsc == 27 or contador >= cantPic:
			break

	#Cerrar ventanas y matar los procesos cuando se haya terminado
	camara.release()
	cv2.destroyAllWindows()