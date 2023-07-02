# Kwema Bacteria

Este es un proyecto Django que calcula la propagación de una bacteria basada en ciertos parámetros. Se utiliza Python 3.10.5 y Django 4.2.2.

## Instalación

Sigue los siguientes pasos para instalar y ejecutar el proyecto:

1. Clona el repositorio:
git clone https://github.com/MVargasP/PropagacionBacteriana.git


2. Navega hasta la carpeta del proyecto:
cd kwema


3. Crea un entorno virtual y actívalo:
python3 -m venv <nombre de tu entorno virtual>
source <nombre de tu entorno virtual>/bin/activate


4. Instala las dependencias del proyecto:
pip install -r requirements.txt

5. Realiza las migraciones:
python manage.py migrate

## Ejecución

Para ejecutar el servidor, utiliza el comando:

python manage.py runserver


El servidor debería empezar a correr en `http://127.0.0.1:8000/`.

## Pruebas

Para ejecutar las pruebas, utiliza el comando:

python manage.py test


## Uso de la API

La API proporciona varias rutas para interactuar con el modelo `BacterialStrain`. Estas incluyen un CRUD completo para `BacterialStrain` y una ruta especial para calcular la propagación de una bacteria. A continuación se muestran algunos ejemplos de cómo interactuar con la API.

Para crear una nueva cepa de bacteria:
POST /api/strains/
Body: {
"maturation_period": 1,
"life_expectancy": 4,
"reproduction_rate": 2
}

Para obtener una lista de todas las cepas de bacterias:
GET /api/strains/


Para calcular la propagación de una bacteria:
POST /api/population/
y puede enviar los siguientes parametros 
{ "strain_id": 1, "days": 60, "initial_state": [2, 3, 3, 1, 2] }

para ello previamente debio crear una cepa de bacteria en la api anterior de lo contrario obtendra un status 404