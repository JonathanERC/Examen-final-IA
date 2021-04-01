# Reconocedor de emociones

### Tabla de Contenidos
+ [Reconocedor de emociones](#reconocedor-de-emociones)
	+ [Funciones](#funciones)
	+ [Como instalar](#como-instalar)
		+ [Requisitos](#requisitos)
	+ [Como usar](#como-usar)
	+ [Trabajo en proceso](#trabajo-en-proceso)
		+ [Bugs](#bugs)
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
WIP


------------
Se puede probar la población de la base de datos de emociones con el siguiente ejecutando el siguiente script:
`.\capturandoRostros.py`.

Se creará una carpeta en `%USERPROFILE%` llamada `IA`, en esta se almacenarán todos los datos del programa. Dentro de esta carpeta se encontrará una llamada `Data`, en esta se crearán las subcarpetas por cada emoción, donde se guardarán las fotos de las bases de datos de emociones.

debería quedar así: `%USERPROFILE%/IA/Data/{carpetasEmociones}`.

El algoritmo está programado para que tome una foto cada vez que identifique una cara alimentando la base de datos con un total de 200 fotos por emociones.

------------
## Trabajo en proceso
- [x] Reconocimiento facial. (Prioridad Alta)
- [x] Entrenador de reconocimiento del mismo rostro. (Prioridad Alta)
- [x] Entrenador de Emociones. (Prioridad Alta)
- [x] Limpiar el código. (Prioridad Media)
- [ ] Comentar código. (Prioridad Media)
- [ ] Agregar variable para poblar la BD a conveniencia. (Prioridad Baja)
- [ ] Agregar Emociones como un objeto para añadir cuantas sean necesarias. (Prioridad Baja)

### Bugs
- ~~Por alguna razón el entrenador de reconocimiento del mismo rostro solo funciona con OpenCV 4.2 y no con la versión más reciente.~~ Corregido, había conflictos entre **"OpenCV"** y **"OpenCV Contrib"**, se ha dejado únicamente a **"OpenCV Contrib"** para el procesamiento basado únicamente en CPU y no en GPU.

## Créditos
- Jonathan Rondón por la implementación del código.
- Marieli Germán por la colaboración en el algoritmo de reconocimiento facial.
- Miguel Guerrero por la colaboración en el algoritmo de tonalidades.
- [Gabriela Solano](https://omes-va.com/ "Gabriela Solano") por la colaboración en el código.
