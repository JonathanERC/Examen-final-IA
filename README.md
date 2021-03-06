# Reconocedor de emociones

### Tabla de Contenidos
+ [Reconocedor de emociones](#reconocedor-de-emociones)
	+ [Funciones](#funciones)
	+ [Como instalar](#como-instalar)
		+ [Requisitos](#requisitos)
	+ [Como usar](#como-usar)
		+ [Bugs](#bugs)
	+ [Trabajo en proceso](#trabajo-en-proceso)
		+ [Argumentos disponibles](#argumentos-disponibles)
	+ [Créditos](#créditos)

## Funciones
- Creación de base de datos de Emociones
- Entrenamiento de 3 algoritmos de reconocimiento facial
	- EigenFaces (Reconocedor facial)
	- FisherFaces (Reconocedor facial en diferentes tonalidades)
	- LBPH (Reconocedor de emociones)

## Como instalar
### Requisitos
* Python3.6 en adelante
	* Pip
		* ~~OpenCV (*pip install opencv-python*)~~
		* OpenCV Contrib (*pip install opencv-contrib-python*)
		* iMutils (*pip install imutils*)
		* Numpy (*pip install numpy*)
		* Time (*pip install times*)

## Como usar
El sistema esta hecho para ser autosuficiente, por lo que con ejecutar el archivo `.\run.py` es suficiente para instalar, entrenar y poner en marcha el modelo.

Al ejecutar el modelo se creará una carpeta en `%USERPROFILE%` llamada `IA`, en esta se almacenarán todos los datos del programa.
- En la raíz de la carpeta `%USERPROFILE%/IA/` se almacenarán los archivos `XML` de cada modelo de entrenamiento utilizado.
- Dentro de la carpeta `%USERPROFILE%/IA/Data/` se crearán subcarpetas por cada emoción donde se guardarán las fotos de las bases de datos de emociones. El algoritmo está programado para que tome una foto cada vez que identifique una cara alimentando la base de datos con un total de 200 fotos por emociones.

### Argumentos disponibles
     -r      Reentrenar modelos.
     -p      Indicar cantidad maxima de fotos para entrenamientos.
     -m      Selecionar modelo de reconocimiento.
     -h      Lista de argumentos.
     -t      Reiniciar todo el sistema y parametros.

------------
## Trabajo en proceso
- [x] Reconocimiento facial. (Prioridad Alta)
- [x] Entrenador de reconocimiento del mismo rostro. (Prioridad Alta)
- [x] Entrenador de Emociones. (Prioridad Alta)
- [x] Limpiar el código. (Prioridad Media)
- [x] Comentar código. (Prioridad Media)
- [x] Agregar variable para poblar la BD a conveniencia. (Prioridad Baja)
- [x] Agregar opción para reentrenar el modelo. (Prioridad Baja)
- [x] Agregar Emociones como un objeto para añadir cuantas sean necesarias. (Prioridad Baja)

### Bugs
- ~~Por alguna razón el entrenador de reconocimiento del mismo rostro solo funciona con OpenCV 4.2 y no con la versión más reciente.~~ Corregido, había conflictos entre **"OpenCV"** y **"OpenCV Contrib"**, se ha dejado únicamente a **"OpenCV Contrib"** para el procesamiento basado solo en CPU.

## Créditos
- [Gabriela Solano](https://omes-va.com/ "Gabriela Solano"). Este codigo es un Fork de un proyecto [suyo](https://omes-va.com/reconocimiento-de-emociones-opencv-python/ "suyo"), todos los creditos para ella por proveer la plantilla inicial en la que se basó este proyecto.
